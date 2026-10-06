"""Author-controlled single-page mind maps. Layout choices remain pedagogical decisions."""
import argparse, asyncio, hashlib, html, json, re, shutil, subprocess, tempfile
from pathlib import Path
from html.parser import HTMLParser
import genanki
from build_deck import audio, synthesize, SPEECH, check_svg, duration
from speech_backend import DEFAULT_VOICE
from html_integrity import validate_markup
ASSETS = Path(__file__).resolve().parent.parent / 'assets'
FIELDS = ['StableID','Label','Prompt','Answer','FrontHTML','BackHTML','Source','Target']
def esc(t): return html.escape(str(t), quote=True)
def passive_html(value):
    assert isinstance(value, str) and value.strip(), 'Expected nonempty local HTML'
    validate_markup(value)
    assert not re.search(r'<(?:script|iframe|audio|button)\b|\son\w+\s*=|(?:src|href)=["\'](?:https?:|file:|javascript:)', value, re.I), 'Use passive local content; extend renderer deliberately for interactions'
    for svg in re.findall(r'<svg\b[\s\S]*?</svg>', value): check_svg(svg)

def require_text(record, keys, message):
    assert isinstance(record, dict), message
    assert all(isinstance(record.get(k), str) and record[k].strip() for k in keys), message

class SnapshotContent(HTMLParser):
    """Locate recorded visible text without executing a historical card's scripts."""
    def __init__(self, markup):
        super().__init__(convert_charrefs=True)
        self.stack, self.elements, self.text = [], [], []
        self.feed(markup)
    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        hidden = (any(e['hidden'] for e in self.stack) or tag in ('head', 'script', 'style', 'template', 'noscript', 'title', 'desc', 'defs', 'metadata')
                  or 'hidden' in attrs or attrs.get('aria-hidden') == 'true'
                  or bool(re.search(r'(?:display\s*:\s*none|visibility\s*:\s*(?:hidden|collapse)|opacity\s*:\s*0(?:\.0+)?\s*(?:;|!|$))', attrs.get('style', ''), re.I)))
        node = {'tag': tag, 'attrs': attrs, 'hidden': hidden, 'text': []}
        self.elements.append(node)
        if tag not in ('area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'):
            self.stack.append(node)
        self.handle_data(' ')
    def handle_endtag(self, tag):
        self.handle_data(' ')
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]['tag'] == tag:
                del self.stack[i:]
                break
    def handle_data(self, text):
        if not any(e['hidden'] for e in self.stack):
            self.text.append(text)
            for element in self.stack:
                element['text'].append(text)
    @staticmethod
    def normalize(text):
        return ' '.join(text.split())
    def locate(self, locator):
        kind, separator, value = locator.partition(':')
        assert separator and value.strip() and kind in ('id', 'data-node', 'text'), 'Snapshot locators use id:, data-node: or text:'
        if kind == 'text':
            wanted = self.normalize(value)
            visible = self.normalize(''.join(self.text))
            assert visible.count(wanted) == 1, 'Snapshot text location must exist exactly once in visible content'
            return wanted
        matches = [e for e in self.elements if e['attrs'].get(kind) == value and not e['hidden']]
        assert len(matches) == 1, 'Snapshot node must exist exactly once and be visible'
        excerpt = self.normalize(''.join(matches[0]['text']))
        assert excerpt, 'Snapshot node has no visible knowledge text'
        return excerpt

def load_existing_cards(data, source_dir=None):
    """Verify saved artifacts; this does not claim a live Anki collection check."""
    entries = data.get('existing_cards', [])
    assert isinstance(entries, list), 'existing_cards must be a list of verified snapshots'
    current_ids = {c['id'] for c in data['cards']}
    aliases, identities, records = set(), set(), []
    for entry in entries:
        require_text(entry, ('id', 'snapshot_path', 'sha256', 'content_review'), 'Existing coverage needs a real snapshot, hash and content review')
        alias = entry['id']
        assert alias not in current_ids and alias not in aliases, 'Existing aliases must be unique and distinct from cards being published'
        aliases.add(alias)
        expected = entry.get('identity', {})
        require_text(expected, ('collection',), 'Identify the collection or profile of the existing card')
        assert all(isinstance(expected.get(k), int) and not isinstance(expected[k], bool) and expected[k] > 0 for k in ('note_id', 'card_id', 'model_id')), 'Existing identity needs positive Anki note/card/model IDs'
        identity_key = (expected['collection'], expected['card_id'])
        assert identity_key not in identities, 'The same existing card cannot be counted under multiple aliases'
        identities.add(identity_key)
        path = Path(entry['snapshot_path'])
        if not path.is_absolute():
            path = Path(source_dir or Path.cwd()) / path
        assert path.is_file(), 'Existing card snapshot is missing'
        raw = path.read_bytes()
        assert re.fullmatch(r'[0-9a-f]{64}', entry['sha256']) and hashlib.sha256(raw).hexdigest() == entry['sha256'], 'Existing snapshot hash changed; recapture and review before counting coverage'
        try:
            snapshot = json.loads(raw)
        except (ValueError, UnicodeError) as error:
            raise AssertionError('Existing snapshot must be valid JSON') from error
        assert snapshot.get('identity') == expected, 'Existing snapshot identity does not match the referenced card'
        require_text(snapshot, ('capture_source', 'captured_at', 'html'), 'Snapshot must record collection method, time and actual visible content')
        # The capture is rendered visible DOM, not a raw template with unresolved CSS.
        assert not re.search(r'<(?:style|script|template|link)\b', snapshot['html'], re.I), 'Capture resolved visible content, excluding stylesheets, scripts and hidden templates'
        parsed = SnapshotContent(snapshot['html'])
        nodes = snapshot.get('nodes', [])
        assert isinstance(nodes, list) and nodes, 'Existing snapshot needs concrete visible locations'
        node_ids, locations = set(), []
        for node in nodes:
            require_text(node, ('id', 'locator'), 'Snapshot locations need a stable alias and locator')
            assert node['id'] not in node_ids, 'Snapshot location IDs must be unique'
            node_ids.add(node['id'])
            locations.append({'id': node['id'], 'locator': node['locator'], 'visible_text': parsed.locate(node['locator'])})
        records.append({'id': alias, 'identity': expected, 'snapshot_sha256': entry['sha256'],
                        'capture_source': snapshot['capture_source'], 'captured_at': snapshot['captured_at'],
                        'content_review': entry['content_review'], 'nodes': locations})
    return records

def validate_locations(locations, card_nodes, *, required=True):
    assert isinstance(locations, list) and (locations or not required), 'Map taught knowledge to visible card nodes'
    mapped = set()
    for loc in locations:
        assert isinstance(loc, dict) and loc.get('card') in card_nodes, 'Coverage references a missing card'
        cid = loc['card']
        assert isinstance(loc.get('nodes'), list) and loc['nodes'] and all(n in card_nodes[cid] for n in loc['nodes']), 'Coverage references missing visible nodes'
        mapped.add(cid)
    return mapped

def validate_knowledge_coverage(data, source_dir=None):
    """Check traceability, not whether a textbook was read or a syllabus is complete."""
    coverage = data.get('knowledge_coverage', {})
    require_text(coverage, ('scope_id', 'scope'), 'Identify the knowledge scope and its syllabus boundary')
    status = coverage.get('status')
    assert status in ('partial', 'complete'), 'State partial or complete knowledge coverage'
    remaining = coverage.get('remaining', '')
    assert isinstance(remaining, str), 'Remaining knowledge scope must be explicit text'
    assert remaining.strip() if status == 'partial' else not remaining.strip(), 'Partial coverage needs remaining scope; complete coverage cannot have unresolved gaps'
    items = coverage.get('items', [])
    assert isinstance(items, list) and items, 'Decompose the syllabus scope into knowledge requirements'
    required_core = coverage.get('required_core', [])
    assert isinstance(required_core, list) and required_core and all(isinstance(k, str) and k.strip() for k in required_core), 'Keep the core knowledge inventory identified from the input and syllabus before card planning'
    assert len(required_core) == len(set(required_core)), 'Required core knowledge IDs must be unique'
    card_nodes = {c['id']: {n['id'] for n in c['nodes']} for c in data['cards']}
    published_ids = set(card_nodes)
    for existing in load_existing_cards(data, source_dir):
        card_nodes[existing['id']] = {n['id'] for n in existing['nodes']}
    mapped_cards, item_ids, actual_core = set(), set(), set()
    for item in items:
        require_text(item, ('id', 'syllabus_item', 'knowledge', 'evidence'), 'Knowledge items need identity, syllabus position, meaning and evidence')
        assert item['id'] not in item_ids, 'Knowledge item IDs must be unique'
        item_ids.add(item['id'])
        classification = item.get('classification')
        assert classification in ('core', 'prerequisite', 'excluded'), 'Classify knowledge as core, prerequisite or excluded'
        locations = item.get('locations', [])
        if classification in ('prerequisite', 'excluded'):
            require_text(item, ('reason',), 'Prerequisite and excluded knowledge need a substantive scope reason')
        if classification == 'excluded':
            assert locations == [], 'Excluded knowledge cannot be taught in the current card set'
        else:
            if classification == 'core':
                actual_core.add(item['id'])
            mapped_cards.update(validate_locations(locations, card_nodes, required=status == 'complete'))
    assert actual_core == set(required_core), 'Coverage must retain every required core item; do not silently omit or downgrade the research inventory'
    assert published_ids <= mapped_cards, 'Every published card must belong to included knowledge, including justified prerequisites'
    checks = data.get('assessment_checks', [])
    assert isinstance(checks, list), 'Assessment checks must be a list'
    assert checks or status == 'partial', 'A complete scope needs an assessment application review'
    for check in checks:
        require_text(check, ('question_refs', 'marking_refs', 'application_review'), 'Assessment checks need source locations and an actual application review')
        validate_locations(check.get('locations', []), card_nodes)

def validate_legacy_coverage(data):
    """Maintain historical exam-led records only through the explicit CLI flag."""
    card_nodes = {c['id']: {n['id'] for n in c['nodes']} for c in data['cards']}
    tasks = data.get('task_coverage')
    if tasks is not None:
        assert isinstance(tasks, list) and tasks, 'Record historical shared task coverage'
        mapped_cards = set()
        for coverage in tasks:
            require_text(coverage, ('question', 'standard', 'worked_answer', 'reconstruction_review'), 'Missing historical shared coverage')
            status, remaining = coverage.get('status'), coverage.get('remaining', '')
            assert status in ('partial', 'complete') and isinstance(remaining, str)
            assert remaining.strip() if status == 'partial' else not remaining.strip()
            items = coverage.get('requirements', [])
            assert isinstance(items, list) and items
            for item in items:
                require_text(item, ('requirement', 'evidence', 'teaching'), 'Historical coverage needs evidence and reasoning')
                mapped_cards.update(validate_locations(item.get('locations', []), card_nodes))
        assert mapped_cards == set(card_nodes), 'Historical coverage must account for each card'
    else:
        for c in data['cards']:
            coverage = c.get('answer_coverage', {})
            require_text(coverage, ('question', 'standard', 'worked_answer', 'reconstruction_review'), 'Missing historical per-card coverage')
            items = coverage.get('requirements', [])
            assert isinstance(items, list) and items
            for item in items:
                require_text(item, ('requirement', 'evidence', 'teaching'), 'Historical coverage needs evidence and reasoning')
                assert item.get('nodes') and all(n in card_nodes[c['id']] for n in item['nodes']), 'Coverage references missing visible nodes'

def validate(data, *, legacy_coverage=False, source_dir=None):
    ids = [c['id'] for c in data['cards']]
    assert ids and len(ids) == len(set(ids)), 'Card IDs must be unique'
    if data.get('academic'):
        task = data.get('exam_task', {})
        assert isinstance(task, dict) and all(isinstance(task.get(k), str) and task[k].strip() for k in ('qualification', 'authority', 'version', 'component', 'task_type')), 'Confirm the target exam and task before making academic cards'
    for c in data['cards']:
        nodes = {n['id']: n for n in c['nodes']}
        assert len(nodes) == len(c['nodes']) and c['root'] in nodes
        assert set(c['reading_order']) == set(nodes) and len(c['reading_order']) == len(nodes), 'Narration must cover each node exactly once'
        assert isinstance(c.get('narration_follow', data.get('narration_follow', False)), bool), 'narration_follow must be true or false'
        assert c.get('title') and c.get('target') and c.get('sources'), 'Missing teaching goal or sources'
        if not legacy_coverage:
            assert isinstance(c['sources'], list) and all(isinstance(s, str) and s.strip() for s in c['sources']), 'Locate each card\'s knowledge explanations in its sources'
        assert c.get('audit'), 'Record actual teaching review, not just a rendered map'
        if c.get('title_html'):
            passive_html(c['title_html'])
            assert isinstance(c.get('title_speech'), str) and c['title_speech'].strip(), 'Mathematical titles need a natural spoken title'
        reached = {c['root']}
        for _ in nodes:
            for e in c['edges']:
                assert e['from'] in nodes and e['to'] in nodes
                assert e.get('meaning'), 'Every edge needs a meaningful relationship in authoring data'
                if e['from'] in reached: reached.add(e['to'])
        assert reached == set(nodes), 'All content must belong to the mind map'
        for n in nodes.values():
            assert n.get('html') and n.get('speech'), 'Each learning node needs content and explanation audio text'
            assert n['x'] >= 0 and n['y'] >= 0 and n['width'] > 0
            assert n['x'] + n['width'] <= c['width'], 'Node outside canvas'
            passive_html(n['html'])
        if data.get('academic'):
            assert data.get('syllabus') and data['syllabus'].get('url') and data['syllabus'].get('edition')
            assert c.get('scope'), 'Academic knowledge scope is required'
            relevance = c.get('research_use')
            if legacy_coverage:
                assert c.get('exam_use'), 'Historical academic exam use is required'
                basis = c.get('answer_basis') or data.get('answer_basis', {})
                require_text(basis, ('question_refs', 'human_answer_refs', 'quality_review', 'marking_refs', 'teaching_refs', 'difficulty_review'), 'Historical technical maintenance needs its original answer research')
                relevance = relevance or c.get('answer_basis', {}).get('answer_moves')
            else:
                basis = data.get('research_basis', {})
                require_text(basis, ('input_trace', 'textbook_refs', 'reading_record', 'model_synthesis', 'source_review', 'syllabus_refs', 'question_refs', 'marking_refs', 'examiner_refs', 'human_response_refs'), 'Record input trace, textbook study and actual assessment research before making knowledge cards')
            assert isinstance(relevance, str) and relevance.strip(), 'Explain how this research informs this card, without forcing an answer template'
            if not legacy_coverage:
                unit = c.get('learning_unit', {})
                assert isinstance(unit, dict) and all(isinstance(unit.get(k), str) and unit[k].strip() for k in ('starting_point', 'boundary', 'explanation_review')), 'Define the local learning scope, reader starting point and substantive explanation review'
            # Presence is a traceability gate, never proof of understanding or source quality.
    if data.get('academic'):
        if legacy_coverage:
            validate_legacy_coverage(data)
        else:
            validate_knowledge_coverage(data, source_dir)

def source_record(data, c, *, source_dir=None, existing_records=None):
    """Keep research and scope metadata off the readable knowledge map."""
    record = {'sources':c['sources'], 'scope':c.get('scope'), 'exam_task':data.get('exam_task'),
              'research_use':c.get('research_use'), 'learning_unit':c.get('learning_unit')}
    if data.get('research_basis'):
        record.update(research_basis=data['research_basis'], knowledge_coverage=data.get('knowledge_coverage'), assessment_checks=data.get('assessment_checks', []))
        if data.get('existing_cards'):
            record['existing_cards'] = load_existing_cards(data, source_dir) if existing_records is None else existing_records
    elif c.get('answer_basis') or data.get('answer_basis') or c.get('answer_coverage') or data.get('task_coverage'):
        record.update(exam_use=c.get('exam_use'), answer_basis=c.get('answer_basis') or data.get('answer_basis'),
                      research_use=c.get('research_use') or c.get('answer_basis', {}).get('answer_moves'),
                      task_coverage=data.get('task_coverage'), answer_coverage=c.get('answer_coverage'))
    return record

def source_json(record):
    # Anki stores every field as HTML. JSON escapes preserve exact json.loads semantics
    # while keeping literal comparisons and quoted tags out of the HTML parser.
    return json.dumps(record, ensure_ascii=False).replace('<', r'\u003c').replace('>', r'\u003e').replace('&', r'\u0026')

def narration_plan(c, voice, follow=False):
    """The pedagogical reading order need not start with an abstract map root."""
    nodes = {n['id']: n for n in c['nodes']}
    parts = [(None, c.get('title_speech', c['title']))]
    parts += [(key, nodes[key]['speech']) for key in c['reading_order']]
    text = '。'.join(value.rstrip('。') for _, value in parts)
    if not follow:
        return {'file': audio(text, voice), 'text': text, 'segments': []}
    segments = [{'node': node, 'file': audio(value, voice)} for node, value in parts]
    signature = json.dumps({'voice': voice, 'parts': parts, 'speed': 1.5, 'format': 'pcm-cues-v1'}, ensure_ascii=False, separators=(',', ':'))
    name = 'ccpt_' + hashlib.sha256(signature.encode()).hexdigest()[:20] + '.mp3'
    return {'file': name, 'text': text, 'segments': segments, 'voice': voice}

def assemble_narration(plan, media):
    """Join decoded clips; cue boundaries come from actual PCM sample counts.

    Each input was synthesized at original speed and tempo-adjusted by the shared
    backend. Decoding before concatenation avoids accumulating MP3 frame padding.
    Only the resulting page-level MP3 is imported into Anki.
    """
    dest = media / plan['file']
    sidecar = media / (plan['file'] + '.cues.json')
    clip_hashes = [hashlib.sha256((media / s['file']).read_bytes()).hexdigest() for s in plan['segments']]
    if dest.exists() and sidecar.exists():
        try:
            cached = json.loads(sidecar.read_text())
            if cached['clip_hashes'] == clip_hashes and cached['audio_sha256'] == hashlib.sha256(dest.read_bytes()).hexdigest() and duration(dest) > 0:
                return cached['narration']
        except (KeyError, ValueError, OSError, subprocess.SubprocessError):
            pass
    sample_rate = 24000
    cursor = 0
    cues = []
    with tempfile.TemporaryDirectory(dir=media) as tmp:
        pcm = Path(tmp) / 'page.pcm'
        with pcm.open('wb') as stream:
            for segment in plan['segments']:
                decoded = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(media / segment['file']), '-f', 's16le', '-ar', str(sample_rate), '-ac', '1', '-'])
                assert len(decoded) > 0 and len(decoded) % 2 == 0, 'Empty or malformed narration segment'
                samples = len(decoded) // 2
                cues.append({'node': segment['node'], 'start': cursor / sample_rate, 'end': (cursor + samples) / sample_rate})
                stream.write(decoded)
                cursor += samples
        pending = Path(tmp) / 'page.mp3'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 's16le', '-ar', str(sample_rate), '-ac', '1', '-i', str(pcm), '-codec:a', 'libmp3lame', '-q:a', '3', str(pending)], check=True)
        measured = duration(pending)
        assert abs(measured - cursor / sample_rate) < 0.15, 'Concatenated audio and cue clock disagree'
        pending.replace(dest)
    narration = {'timing': 'decoded-pcm-samples', 'sample_rate': sample_rate, 'speed': 1.5, 'duration': cursor / sample_rate, 'cues': cues}
    sidecar.write_text(json.dumps({'clip_hashes': clip_hashes, 'audio_sha256': hashlib.sha256(dest.read_bytes()).hexdigest(), 'narration': narration}, ensure_ascii=False, indent=2))
    return narration

def render(c, name, narration=None):
    out=f'<main class="ccpt-map" data-ccpt-single="1" data-side="read" data-note="{esc(c["id"])}">'
    title = c.get('title_html') or esc(c['title'])
    out+=f'<header><h1>{title}</h1><button class="speak" data-audio="{name}" aria-label="整页讲解：播放、暂停或继续" aria-pressed="false">▶</button></header>'
    out+=f'<div class="map-viewport"><div class="map-board" style="width:{c["width"]}px;height:{c["height"]}px"><svg class="map-edges" aria-hidden="true"></svg>'
    for n in c['nodes']:
        cls='root' if n['id']==c['root'] else n.get('style','leaf')
        assert re.fullmatch(r'[a-z -]+',cls)
        out+=f'<section class="map-node {cls}" data-node="{esc(n["id"])}" style="left:{n["x"]}px;top:{n["y"]}px;width:{n["width"]}px">{n["html"]}</section>'
    out+='</div></div><footer><span class="audio-status">整页讲解 · 1.5×</span><span>Space 播音 · Enter 继续 · 1 明天再看</span></footer>'
    out+='<div hidden class="map-data">'+esc(json.dumps({'edges':c['edges'],'reading_order':c['reading_order'],'narration':narration},ensure_ascii=False))+'</div>'
    out+=f'<audio preload="none" src="{name}"></audio></main>'
    return out

def preview_audio_available(path):
    """A matching filename alone does not make a cached preview playable."""
    if not path.is_file() or not path.stat().st_size:
        return False
    try:
        probe = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', str(path)], capture_output=True, text=True)
        if probe.returncode or not float(probe.stdout.strip()) > 0:
            return False
        decoded = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(path), '-f', 'null', '-'], capture_output=True)
        return decoded.returncode == 0
    except (OSError, ValueError):
        return False

def pending_audio_page(body, name, message):
    """Keep reading usable without offering a player that cannot play."""
    return (body.replace('class="ccpt-map"', 'class="ccpt-map" data-audio-pending="1" data-audio-message="'+esc(message)+'"')
            .replace('class="speak"', 'class="speak" disabled title="'+esc(message)+'"')
            .replace('aria-label="整页讲解：播放、暂停或继续"', 'aria-label="'+esc(message)+'"')
            .replace(f'data-audio="{name}"', 'data-audio=""')
            .replace(f'<audio preload="none" src="{name}"></audio>', '<audio preload="none"></audio>')
            .replace('整页讲解 · 1.5×', esc(message))
            .replace('Space 播音 · Enter 继续', 'Enter 继续'))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('output',type=Path);ap.add_argument('--preview',action='store_true');ap.add_argument('--text-only-test',action='store_true',help='Explicit test-deck draft only; voice unavailable is visibly disclosed');ap.add_argument('--legacy-coverage-maintenance',action='store_true',help='Preserve historical per-card coverage metadata during technical maintenance only');a=ap.parse_args()
    data=json.loads(a.input.read_text());source_dir=a.input.resolve().parent;validate(data, legacy_coverage=a.legacy_coverage_maintenance, source_dir=source_dir);SPEECH.clear()
    existing_records=load_existing_cards(data, source_dir)
    if a.text_only_test: assert data.get('test_deck') is True, 'Audio omission is only available for a designated test deck'
    out=a.output;out.mkdir(parents=True,exist_ok=True);media=out/'media';media.mkdir(exist_ok=True)
    voice=data.get('voice',DEFAULT_VOICE)
    css=(ASSETS/'map-card.css').read_text()+data.get('css','')
    js=(ASSETS/'map-card.js').read_text()+(ASSETS/'single-face.js').read_text()
    fmt='<div data-ccpt-single="1">{{BackHTML}}</div><script>'+js+'</script>'
    model=genanki.Model(data['model_id'],data['model_name'],fields=[{'name':x} for x in FIELDS],templates=[{'name':'单面阅读','qfmt':fmt,'afmt':fmt,'bqfmt':'{{Prompt}}','bafmt':'{{Answer}}'}],css=css,sort_field_index=1)
    decks={};rendered={}
    plans={c['id']:narration_plan(c, voice, c.get('narration_follow', data.get('narration_follow', False))) for c in data['cards']}
    narration={}
    if not a.preview and not a.text_only_test:
        asyncio.run(synthesize(media))
        for cid,plan in plans.items():
            if plan['segments']:
                narration[cid]=assemble_narration(plan, media)
    for i,c in enumerate(data['cards']):
        plan=plans[c['id']];text=plan['text'];name=plan['file'];body=render(c,name,narration.get(c['id']))
        if a.text_only_test:
            body=pending_audio_page(body,name,'图文测试 · 云希语音待补')
        elif a.preview and not preview_audio_available(media/name):
            body=pending_audio_page(body,name,'图文预览，未生成语音')
        rendered[c['id']]={'page':body,'narration':text,'narration_follow':narration.get(c['id'])}
        deck=decks.setdefault(c['deck_id'],genanki.Deck(c['deck_id'],c['deck']))
        source=source_json(source_record(data,c,existing_records=existing_records))
        deck.add_note(genanki.Note(model=model,fields=[c['id'],c['id'],c['title'],c['target'],body,body,source,c['target']],guid=genanki.guid_for(c['namespace'],c['id']),tags=['ccpt','ccpt-single','map-v5'],due=i+1))
        preview=body.replace('data-audio="ccpt_','data-audio="media/ccpt_').replace('src="ccpt_','src="media/ccpt_')
        (out/f'{c["id"]}-read.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(c['title'])+'</title><style>'+css+'</style><body class="card">'+preview+'<script>'+js+'</script></body></html>')
    (out/'cards.json').write_text(json.dumps(data,ensure_ascii=False,indent=2));(out/'rendered.json').write_text(json.dumps(rendered,ensure_ascii=False,indent=2))
    if not a.preview:
        manifest=out/'speech-manifest.json';previous={v['file']:v for v in json.loads(manifest.read_text())} if manifest.exists() else {}
        entries=[]
        for cid,plan in plans.items():
            name=plan['file']
            if plan['segments']:
                entry={'file':name,'text':plan['text'],'voice':voice,'speed':1.5,'synthesis_rate':'+0%','tempo_filter':'atempo=1.5','segments':plan['segments'],'narration_follow':narration.get(cid)}
                if cid in narration:entry['duration']=duration(media/name)
            else:entry=dict(previous.get(name,{}),**SPEECH[name])
            entry['available']=not a.text_only_test
            entries.append(entry)
        manifest.write_text(json.dumps(entries,ensure_ascii=False,indent=2))
        pkg=genanki.Package(list(decks.values()));pkg.media_files=[] if a.text_only_test else [str(media/n) for n in dict.fromkeys(p['file'] for p in plans.values())];pkg.write_to_file(str(out/'CCPT-test.apkg'))
    print(json.dumps({'cards':len(data['cards']),'preview':a.preview,'voice':voice,'output':str(out)},ensure_ascii=False))
if __name__=='__main__':main()
