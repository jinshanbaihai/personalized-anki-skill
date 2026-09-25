"""Author-controlled single-page mind maps. Layout choices remain pedagogical decisions."""
import argparse, asyncio, html, json, re, shutil
from pathlib import Path
import genanki
from build_deck import audio, synthesize, SPEECH, check_svg
from speech_backend import DEFAULT_VOICE
ASSETS = Path(__file__).resolve().parent.parent / 'assets'
FIELDS = ['StableID','Label','Prompt','Answer','FrontHTML','BackHTML','Source','Target']
def esc(t): return html.escape(str(t), quote=True)
def passive_html(value):
    assert isinstance(value, str) and value.strip(), 'Expected nonempty local HTML'
    assert not re.search(r'<(?:script|iframe|audio|button)\b|\son\w+\s*=|(?:src|href)=["\'](?:https?:|file:|javascript:)', value, re.I), 'Use passive local content; extend renderer deliberately for interactions'
    for svg in re.findall(r'<svg\b[\s\S]*?</svg>', value): check_svg(svg)

def validate(data):
    ids = [c['id'] for c in data['cards']]
    assert ids and len(ids) == len(set(ids)), 'Card IDs must be unique'
    if data.get('academic'):
        task = data.get('exam_task', {})
        assert isinstance(task, dict) and all(isinstance(task.get(k), str) and task[k].strip() for k in ('qualification', 'authority', 'version', 'component', 'task_type')), 'Confirm the target exam and task before making academic cards'
    for c in data['cards']:
        nodes = {n['id']: n for n in c['nodes']}
        assert len(nodes) == len(c['nodes']) and c['root'] in nodes
        assert set(c['reading_order']) == set(nodes) and len(c['reading_order']) == len(nodes), 'Narration must cover each node exactly once'
        assert c['reading_order'][0] == c['root'], 'Start narration with the map root'
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
            coverage = c.get('answer_coverage', {})
            for key in ('question', 'standard', 'worked_answer', 'reconstruction_review'):
                assert isinstance(coverage.get(key), str) and coverage[key].strip(), 'Missing full-answer coverage: '+key
            items = coverage.get('requirements', [])
            assert items, 'Map actual assessment requirements to visible teaching nodes'
            for item in items:
                assert all(isinstance(item.get(k), str) and item[k].strip() for k in ('requirement', 'evidence', 'teaching')), 'Coverage must explain the requirement, source and reasoning'
                assert item.get('nodes') and all(k in nodes for k in item['nodes']), 'Coverage references missing visible nodes'
            # Presence is a traceability gate, never proof of source authenticity or quality.

def render(c, name):
    out=f'<main class="ccpt-map" data-ccpt-single="1" data-side="read" data-note="{esc(c["id"])}">'
    title = c.get('title_html') or esc(c['title'])
    out+=f'<header><h1>{title}</h1><button class="speak" data-audio="{name}" aria-label="整页讲解：播放、暂停或继续" aria-pressed="false">▶</button></header>'
    out+=f'<div class="map-viewport"><div class="map-board" style="width:{c["width"]}px;height:{c["height"]}px"><svg class="map-edges" aria-hidden="true"></svg>'
    for n in c['nodes']:
        cls='root' if n['id']==c['root'] else n.get('style','leaf')
        assert re.fullmatch(r'[a-z -]+',cls)
        out+=f'<section class="map-node {cls}" data-node="{esc(n["id"])}" style="left:{n["x"]}px;top:{n["y"]}px;width:{n["width"]}px">{n["html"]}</section>'
    out+='</div></div><footer><span class="audio-status">整页讲解 · 1.5×</span><span>Space 播音 · Enter 继续 · 1 明天再看</span></footer>'
    out+='<div hidden class="map-data">'+esc(json.dumps({'edges':c['edges'],'reading_order':c['reading_order']},ensure_ascii=False))+'</div>'
    out+=f'<audio preload="none" src="{name}"></audio></main>'
    return out
def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('output',type=Path);ap.add_argument('--preview',action='store_true');ap.add_argument('--text-only-test',action='store_true',help='Explicit test-deck draft only; voice unavailable is visibly disclosed');a=ap.parse_args()
    data=json.loads(a.input.read_text());validate(data);SPEECH.clear()
    if a.text_only_test: assert data.get('test_deck') is True, 'Audio omission is only available for a designated test deck'
    out=a.output;out.mkdir(parents=True,exist_ok=True);media=out/'media';media.mkdir(exist_ok=True)
    voice=data.get('voice',DEFAULT_VOICE)
    css=(ASSETS/'map-card.css').read_text()+data.get('css','')
    js=(ASSETS/'map-card.js').read_text()+(ASSETS/'single-face.js').read_text()
    fmt='<div data-ccpt-single="1">{{BackHTML}}</div><script>'+js+'</script>'
    model=genanki.Model(data['model_id'],data['model_name'],fields=[{'name':x} for x in FIELDS],templates=[{'name':'单面阅读','qfmt':fmt,'afmt':fmt,'bqfmt':'{{Prompt}}','bafmt':'{{Answer}}'}],css=css,sort_field_index=1)
    decks={};rendered={}
    for i,c in enumerate(data['cards']):
        nodes={n['id']:n for n in c['nodes']};text=c.get('title_speech', c['title'])+'。'+'。'.join(nodes[k]['speech'].rstrip('。') for k in c['reading_order'])
        name=audio(text,voice);body=render(c,name)
        if a.text_only_test:
            body=body.replace('class="ccpt-map"','class="ccpt-map" data-audio-pending="1"').replace('class="speak"','class="speak" disabled title="目标 voice 不可用；当前为图文测试"').replace(f'data-audio="{name}"','data-audio=""').replace(f'<audio preload="none" src="{name}"></audio>','<audio preload="none"></audio>').replace('整页讲解 · 1.5×','图文测试 · 云希语音待补')
        rendered[c['id']]={'page':body,'narration':text}
        deck=decks.setdefault(c['deck_id'],genanki.Deck(c['deck_id'],c['deck']))
        source=json.dumps({'sources':c['sources'],'scope':c.get('scope'),'exam_use':c.get('exam_use'),'exam_task':data.get('exam_task'),'answer_basis':c.get('answer_basis') or data.get('answer_basis'),'research_use':c.get('research_use') or c.get('answer_basis',{}).get('answer_moves'),'answer_coverage':c.get('answer_coverage')},ensure_ascii=False)
        deck.add_note(genanki.Note(model=model,fields=[c['id'],c['id'],c['title'],c['target'],body,body,source,c['target']],guid=genanki.guid_for(c['namespace'],c['id']),tags=['ccpt','ccpt-single','map-v5'],due=i+1))
        preview=body.replace('data-audio="ccpt_','data-audio="media/ccpt_').replace('src="ccpt_','src="media/ccpt_')
        (out/f'{c["id"]}-read.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(c['title'])+'</title><style>'+css+'</style><body class="card">'+preview+'<script>'+js+'</script></body></html>')
    (out/'cards.json').write_text(json.dumps(data,ensure_ascii=False,indent=2));(out/'rendered.json').write_text(json.dumps(rendered,ensure_ascii=False,indent=2))
    if not a.preview:
        if not a.text_only_test: asyncio.run(synthesize(media))
        manifest=out/'speech-manifest.json';previous={v['file']:v for v in json.loads(manifest.read_text())} if manifest.exists() else {}
        entries=[dict(previous.get(k,{}),**v,available=not a.text_only_test) for k,v in SPEECH.items()]
        manifest.write_text(json.dumps(entries,ensure_ascii=False,indent=2))
        pkg=genanki.Package(list(decks.values()));pkg.media_files=[] if a.text_only_test else [str(media/n) for n in SPEECH];pkg.write_to_file(str(out/'CCPT-test.apkg'))
    print(json.dumps({'cards':len(data['cards']),'preview':a.preview,'voice':voice,'output':str(out)},ensure_ascii=False))
if __name__=='__main__':main()
