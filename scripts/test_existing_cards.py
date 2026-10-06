"""Read-only reuse of captured cards; synthetic files are not live Anki evidence."""
import copy
import hashlib
import json
import sqlite3
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
import build_map_deck
from build_map_deck import validate, source_record, FIELDS, SPEECH

ROOT = Path(__file__).resolve().parent.parent
fixture = json.loads((ROOT / 'assets/map-example.json').read_text())
data = copy.deepcopy(fixture)
data.update(academic=True, syllabus={'url': 'synthetic', 'edition': 'synthetic'},
    exam_task={k: 'Synthetic exam context' for k in ('qualification','authority','version','component','task_type')},
    research_basis={k: 'Synthetic fixture; not completed real research' for k in ('input_trace','textbook_refs','reading_record','model_synthesis','source_review','syllabus_refs','question_refs','marking_refs','examiner_refs','human_response_refs')})
card = data['cards'][0]
card.update(scope='Synthetic topic', research_use='Synthetic new relationship', learning_unit={k: 'Synthetic local teaching review' for k in ('starting_point','boundary','explanation_review')})
identity = {'collection': 'Synthetic isolated profile', 'note_id': 1001, 'card_id': 1002, 'model_id': 1003}
snapshot = {'identity': identity, 'capture_source': 'Synthetic rendered DOM fixture; not live Anki', 'captured_at': '2026-10-03T00:00:00Z',
    'html': '<main><section id="old-slope">At fixed prices, income changes the intercepts.</section><p>Existing explanation retained without rewriting the note.</p></main>',
    'nodes': [{'id': 'old-node', 'locator': 'id:old-slope'}, {'id': 'old-text', 'locator': 'text:Existing explanation retained without rewriting the note.'}]}
data['knowledge_coverage'] = {'scope_id': 'synthetic-topic', 'scope': 'One new and one existing relationship', 'status': 'complete', 'remaining': '', 'required_core': ['new', 'existing'],
    'items': [
        {'id':'new','syllabus_item':'1','knowledge':'New relationship','classification':'core','evidence':'Synthetic syllabus 1','locations':[{'card':card['id'],'nodes':['a','b']}]},
        {'id':'existing','syllabus_item':'2','knowledge':'Already taught relationship','classification':'core','evidence':'Synthetic syllabus 2','locations':[{'card':'existing-bl','nodes':['old-node']}]},
    ]}
data['assessment_checks'] = [{'question_refs':'Synthetic assessment','marking_refs':'Synthetic marking','application_review':'An assessment may use existing knowledge only.','locations':[{'card':'existing-bl','nodes':['old-text']}]}]
rejected=[]
with tempfile.TemporaryDirectory() as temp:
    base=Path(temp)/'input';base.mkdir()
    path=base/'old-card.snapshot.json'
    def save_snapshot(value):
        path.write_text(json.dumps(value))
        return hashlib.sha256(path.read_bytes()).hexdigest()
    digest=save_snapshot(snapshot)
    data['existing_cards']=[{'id':'existing-bl','snapshot_path':path.name,'sha256':digest,'identity':identity,'content_review':'Synthetic review: the visible content supports requirement 2, with limitations checked.'}]
    validate(data,source_dir=base)
    record=source_record(data,card,source_dir=base)
    saved=record['existing_cards'][0]
    assert saved['identity']==identity and saved['snapshot_sha256']==digest
    assert saved['nodes'][0]['visible_text']=='At fixed prices, income changes the intercepts.'
    assert 'snapshot_path' not in saved and saved['capture_source']==snapshot['capture_source']

    def reject(label, mutate_data=None, mutate_snapshot=None):
        bad=copy.deepcopy(data);content=copy.deepcopy(snapshot)
        if mutate_snapshot:
            mutate_snapshot(content)
            bad['existing_cards'][0]['sha256']=save_snapshot(content)
        else:
            save_snapshot(snapshot)
        if mutate_data:mutate_data(bad)
        try:validate(bad,source_dir=base)
        except AssertionError:rejected.append(label)
        else:raise AssertionError(label+' was accepted')

    reject('missing snapshot',lambda d:d['existing_cards'][0].update(snapshot_path='absent.json'))
    reject('changed snapshot hash',lambda d:d['existing_cards'][0].update(sha256='0'*64))
    reject('same alias as new card',lambda d:d['existing_cards'][0].update(id=card['id']))
    reject('duplicate external alias',lambda d:d['existing_cards'].append(copy.deepcopy(d['existing_cards'][0])))
    reject('same old card under two aliases',lambda d:d['existing_cards'].append(dict(d['existing_cards'][0],id='another-alias')))
    reject('identity differs from snapshot',lambda d:d['existing_cards'][0]['identity'].update(card_id=7777))
    reject('missing content review',lambda d:d['existing_cards'][0].pop('content_review'))
    reject('no collection identity',lambda d:d['existing_cards'][0]['identity'].pop('collection'))
    reject('coverage refers to absent external node',lambda d:d['knowledge_coverage']['items'][1]['locations'][0].update(nodes=['missing']))
    reject('external-only assessment refers to absent node',lambda d:d['assessment_checks'][0]['locations'][0].update(nodes=['missing']))
    reject('missing capture source',mutate_snapshot=lambda s:s.pop('capture_source'))
    reject('missing capture date',mutate_snapshot=lambda s:s.pop('captured_at'))
    reject('empty snapshot',mutate_snapshot=lambda s:s.update(html=''))
    reject('empty visible node',mutate_snapshot=lambda s:s.update(html=s['html'].replace('At fixed prices, income changes the intercepts.',' ')))
    reject('hidden node',mutate_snapshot=lambda s:s.update(html=s['html'].replace('id="old-slope"','id="old-slope" hidden')))
    reject('inline display none',mutate_snapshot=lambda s:s.update(html=s['html'].replace('id="old-slope"','id="old-slope" style="display:none"')))
    reject('zero opacity',mutate_snapshot=lambda s:s.update(html=s['html'].replace('id="old-slope"','id="old-slope" style="opacity:0"')))
    for tag in ('title', 'desc', 'defs', 'metadata'):
        reject('non-rendered SVG '+tag,mutate_snapshot=lambda s,tag=tag:s.update(html='<svg><'+tag+' id="old-slope">At fixed prices, income changes the intercepts.</'+tag+'></svg><p>Existing explanation retained without rewriting the note.</p>'))
    reject('hidden ancestor',mutate_snapshot=lambda s:s.update(html=s['html'].replace('<main>','<main aria-hidden="true">')))
    reject('missing locator target',mutate_snapshot=lambda s:s['nodes'][0].update(locator='id:absent'))
    reject('unresolved stylesheet snapshot',mutate_snapshot=lambda s:s.update(html='<style>#old-slope{display:none}</style>'+s['html']))
    reject('duplicate location ID',mutate_snapshot=lambda s:s['nodes'][1].update(id='old-node'))
    reject('empty locator inventory',mutate_snapshot=lambda s:s.update(nodes=[]))
    reject('text quotation is not visible',mutate_snapshot=lambda s:s['nodes'][1].update(locator='text:Made up old knowledge'))
    # Replacement without refreshing the reviewed digest cannot silently count as coverage.
    save_snapshot(dict(snapshot,html=snapshot['html'].replace('fixed prices','different prices')))
    try:validate(data,source_dir=base)
    except AssertionError:rejected.append('snapshot replaced after review')
    else:raise AssertionError('Replaced snapshot accepted')
    save_snapshot(snapshot)

    # Visible SVG text is legitimate knowledge; rejecting metadata must not discard it.
    visible_svg=copy.deepcopy(snapshot)
    visible_svg['html']='<svg><text id="old-slope">At fixed prices, income changes the intercepts.</text></svg><p>Existing explanation retained without rewriting the note.</p>'
    svg_data=copy.deepcopy(data);svg_data['existing_cards'][0]['sha256']=save_snapshot(visible_svg)
    validate(svg_data,source_dir=base)
    save_snapshot(snapshot)

    source=base/'input.json';source.write_text(json.dumps(data))
    out=Path(temp)/'out'
    cli=subprocess.run([sys.executable,str(ROOT/'scripts/build_logic_deck.py'),str(source),str(out),'--preview'],capture_output=True,text=True,cwd=Path(temp))
    assert cli.returncode==0,cli.stderr
    assert len(list(out.glob('*-read.html')))==1, 'Read-only cards must not be rebuilt'
    assert not (out/'existing-bl-read.html').exists()

    saved_argv=sys.argv;original_synthesize=build_map_deck.synthesize
    captured_speech=[]
    async def synthetic_audio(media):
        for item in SPEECH.values():
            captured_speech.append(item['text'])
            subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','sine=frequency=440:duration=0.12',str(media/item['file'])],check=True)
    try:
        build_map_deck.synthesize=synthetic_audio
        sys.argv=['build_map_deck.py',str(source),str(out)]
        build_map_deck.main()
    finally:
        sys.argv=saved_argv;build_map_deck.synthesize=original_synthesize
    assert len(captured_speech)==1 and 'fixed prices' not in captured_speech[0]
    with zipfile.ZipFile(out/'CCPT-test.apkg') as archive:
        media=json.loads(archive.read('media'));assert len(media)==1
        collection=Path(temp)/'collection.anki2';collection.write_bytes(archive.read('collection.anki2'))
    with sqlite3.connect(collection) as connection:
        notes=list(connection.execute('select flds from notes'))
        assert len(notes)==1 and len(list(connection.execute('select id from cards')))==1
    note_fields=notes[0][0].split('\x1f');exported=json.loads(note_fields[FIELDS.index('Source')])
    assert exported['existing_cards'][0]['identity']==identity
    assert exported['existing_cards'][0]['nodes'][0]['visible_text']==saved['nodes'][0]['visible_text']
    assert 'fixed prices' not in note_fields[FIELDS.index('BackHTML')]
    assert path.read_bytes()==json.dumps(snapshot).encode(), 'Reuse must never rewrite its snapshot'
print(json.dumps({'existing_knowledge_counts_without_republishing':True,'snapshot_and_identity_checked':True,'old_format_text_and_id_locators_supported':True,'external_only_assessment_supported':True,'relative_path_resolves_from_input_json':True,'only_new_note_and_audio_packaged':True,'reproducible_excerpt_saved_in_Source':True,'invalid_states_rejected':len(rejected)}))
