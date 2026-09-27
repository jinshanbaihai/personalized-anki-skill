"""Author-controlled single-page mind maps. Layout choices remain pedagogical decisions."""
import argparse, asyncio, hashlib, html, json, re, shutil, subprocess, tempfile
from pathlib import Path
import genanki
from build_deck import audio, synthesize, SPEECH, check_svg, duration
from speech_backend import DEFAULT_VOICE
ASSETS = Path(__file__).resolve().parent.parent / 'assets'
FIELDS = ['StableID','Label','Prompt','Answer','FrontHTML','BackHTML','Source','Target']
def esc(t): return html.escape(str(t), quote=True)
def passive_html(value):
    assert isinstance(value, str) and value.strip(), 'Expected nonempty local HTML'
    assert not re.search(r'<(?:script|iframe|audio|button)\b|\son\w+\s*=|(?:src|href)=["\'](?:https?:|file:|javascript:)', value, re.I), 'Use passive local content; extend renderer deliberately for interactions'
    for svg in re.findall(r'<svg\b[\s\S]*?</svg>', value): check_svg(svg)

def validate(data, *, legacy_coverage=False):
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
            assert c.get('scope') and c.get('exam_use'), 'Academic scope and evidenced use are required'
            basis = c.get('answer_basis') or data.get('answer_basis', {})
            assert isinstance(basis, dict) and all(isinstance(basis.get(k), str) and basis[k].strip() for k in ('question_refs', 'human_answer_refs', 'quality_review', 'marking_refs', 'teaching_refs', 'difficulty_review')), 'Record the shared human-answer research before drafting academic cards'
            relevance = c.get('research_use') or c.get('answer_basis', {}).get('answer_moves')
            assert isinstance(relevance, str) and relevance.strip(), 'Explain how this research informs this card, without forcing an answer template'
            if legacy_coverage:
                coverage = c.get('answer_coverage', {})
                for key in ('question', 'standard', 'worked_answer', 'reconstruction_review'):
                    assert isinstance(coverage.get(key), str) and coverage[key].strip(), 'Missing legacy coverage: '+key
                items = coverage.get('requirements', [])
                assert items, 'Map actual assessment requirements to visible teaching nodes'
                for item in items:
                    assert all(isinstance(item.get(k), str) and item[k].strip() for k in ('requirement', 'evidence', 'teaching')), 'Coverage must explain the requirement, source and reasoning'
                    assert item.get('nodes') and all(k in nodes for k in item['nodes']), 'Coverage references missing visible nodes'
            else:
                unit = c.get('learning_unit', {})
                assert isinstance(unit, dict) and all(isinstance(unit.get(k), str) and unit[k].strip() for k in ('starting_point', 'boundary', 'explanation_review')), 'Define the local learning scope, reader starting point and substantive explanation review'
            # Presence is a traceability gate, never proof of understanding or source quality.
    if data.get('academic') and not legacy_coverage:
        tasks = data.get('task_coverage', [])
        assert isinstance(tasks, list) and tasks, 'Record shared task coverage; partial teaching must identify remaining scope'
        card_nodes = {c['id']: {n['id'] for n in c['nodes']} for c in data['cards']}
        mapped_cards = set()
        for coverage in tasks:
            assert isinstance(coverage, dict)
            for key in ('question', 'standard', 'worked_answer', 'reconstruction_review'):
                assert isinstance(coverage.get(key), str) and coverage[key].strip(), 'Missing shared coverage: '+key
            status = coverage.get('status')
            assert status in ('partial', 'complete'), 'State partial or complete task coverage'
            remaining = coverage.get('remaining', '')
            assert isinstance(remaining, str), 'Remaining scope must be explicit text'
            assert remaining.strip() if status == 'partial' else not remaining.strip(), 'Partial coverage needs remaining scope; complete coverage cannot have unresolved gaps'
            items = coverage.get('requirements', [])
            assert isinstance(items, list) and items, 'Map the requirements supported by this delivery'
            for item in items:
                assert all(isinstance(item.get(k), str) and item[k].strip() for k in ('requirement', 'evidence', 'teaching')), 'Coverage needs actual requirements, evidence and reasoning'
                locations = item.get('locations', [])
                assert isinstance(locations, list) and locations, 'Map requirements to cards and visible nodes'
                for loc in locations:
                    cid = loc.get('card')
                    assert cid in card_nodes, 'Coverage references a missing card'
                    assert isinstance(loc.get('nodes'), list) and loc['nodes'] and all(n in card_nodes[cid] for n in loc['nodes']), 'Coverage references missing visible nodes'
                    mapped_cards.add(cid)
        assert mapped_cards == set(card_nodes), 'Explain each card’s contribution, including foundational teaching'

def source_record(data, c):
    """Keep local scope and shared task coverage separate in the exported note."""
    return {'sources':c['sources'], 'scope':c.get('scope'), 'exam_use':c.get('exam_use'),
            'exam_task':data.get('exam_task'),
            'answer_basis':c.get('answer_basis') or data.get('answer_basis'),
            'research_use':c.get('research_use') or c.get('answer_basis',{}).get('answer_moves'),
            'learning_unit':c.get('learning_unit'), 'task_coverage':data.get('task_coverage'),
            'answer_coverage':c.get('answer_coverage')}

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
def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('output',type=Path);ap.add_argument('--preview',action='store_true');ap.add_argument('--text-only-test',action='store_true',help='Explicit test-deck draft only; voice unavailable is visibly disclosed');ap.add_argument('--legacy-coverage-maintenance',action='store_true',help='Preserve historical per-card coverage metadata during technical maintenance only');a=ap.parse_args()
    data=json.loads(a.input.read_text());validate(data, legacy_coverage=a.legacy_coverage_maintenance);SPEECH.clear()
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
            body=body.replace('class="ccpt-map"','class="ccpt-map" data-audio-pending="1"').replace('class="speak"','class="speak" disabled title="目标 voice 不可用；当前为图文测试"').replace(f'data-audio="{name}"','data-audio=""').replace(f'<audio preload="none" src="{name}"></audio>','<audio preload="none"></audio>').replace('整页讲解 · 1.5×','图文测试 · 云希语音待补')
        rendered[c['id']]={'page':body,'narration':text,'narration_follow':narration.get(c['id'])}
        deck=decks.setdefault(c['deck_id'],genanki.Deck(c['deck_id'],c['deck']))
        source=json.dumps(source_record(data,c),ensure_ascii=False)
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
