from pathlib import Path
import sys,json,copy,subprocess,ast
p=Path(__file__).resolve().parent.parent;sys.path.insert(0,str(p/'scripts'))
from build_map_deck import validate,render
fixture=json.loads((p/'assets/map-example.json').read_text());validate(fixture)
html=render(fixture['cards'][0],'test.mp3')
assert all(x in html for x in ['<table','<math','<svg','data-side="read"','data-ccpt-single="1"'])
assert html.count('class="speak"')==1 and 'data-choice' not in html
for failure in ['missing-narration','disconnected','duplicate-order','bad-edge','academic-no-scope']:
 d=copy.deepcopy(fixture);c=d['cards'][0]
 if failure=='missing-narration':del c['nodes'][1]['speech']
 if failure=='disconnected':c['edges']=[]
 if failure=='duplicate-order':c['reading_order']=['a','b','b']
 if failure=='bad-edge':c['edges'][0]['to']='nonexistent'
 if failure=='academic-no-scope':d['academic']=True;d['syllabus']={'url':'test','edition':'test'}
 try:validate(d)
 except (AssertionError,KeyError):pass
 else:raise AssertionError(failure+' not detected')
# Synthetic metadata exercises the gate only; it is not a publishable academic card.
academic = copy.deepcopy(fixture)
academic.update(academic=True, syllabus={'url':'fixture-only', 'edition':'fixture-only'}, exam_task={k:'synthetic test only' for k in ('qualification','authority','version','component','task_type')})
for card in academic['cards']:
 card.update(scope='synthetic test only', exam_use='synthetic test only', answer_basis={k:'synthetic test only' for k in ('question_refs','human_answer_refs','quality_review','marking_refs','teaching_refs','difficulty_review','answer_moves','ai_additions')})
for card in academic['cards']:
 card['answer_coverage']={k:'Synthetic gate test' for k in ('question','standard','worked_answer','reconstruction_review')}
 card['answer_coverage']['requirements']=[dict(requirement='Synthetic comparison',evidence='Fixture',teaching='Synthetic relationship',nodes=['a','b'])]
validate(academic)
for failure in ['no-coverage','empty-requirements','unknown-node','empty-reasoning']:
 bad=copy.deepcopy(academic);c=bad['cards'][0]
 if failure=='no-coverage':del c['answer_coverage']
 elif failure=='empty-requirements':c['answer_coverage']['requirements']=[]
 elif failure=='unknown-node':c['answer_coverage']['requirements'][0]['nodes']=['missing']
 else:c['answer_coverage']['requirements'][0]['teaching']=''
 try:validate(bad)
 except AssertionError:pass
 else:raise AssertionError('Coverage gate missed '+failure)
for missing in ['exam_task','human_answer_refs','quality_review','answer_moves','teaching_refs','difficulty_review']:
 d=copy.deepcopy(academic)
 if missing=='exam_task':del d[missing]
 else:del d['cards'][0]['answer_basis'][missing]
 try:validate(d)
 except AssertionError:pass
 else:raise AssertionError(missing+' missing evidence not detected')
# Shared research must work across cards, without six copied answer fields.
shared=copy.deepcopy(academic)
shared['answer_basis']=shared['cards'][0].pop('answer_basis')
shared['cards'][0]['research_use']='Fixture: shared sources guide the teaching scope'
shared['cards'][0]['title_html']='<math><mfrac><mi>x</mi><mi>y</mi></mfrac></math>'
shared['cards'][0]['title_speech']='x 除以 y'
validate(shared)
page=render(shared['cards'][0],'test.mp3')
assert '<h1><math>' in page and '&lt;math' not in page
bad=copy.deepcopy(shared);del bad['cards'][0]['title_speech']
try:validate(bad)
except AssertionError:pass
else:raise AssertionError('Formula title missing natural narration was accepted')
from validate_package import inspect_page
assert inspect_page(page)=='test.mp3'
for broken in [page.replace('data-audio="test.mp3"','data-audio=""'),page.replace('src="test.mp3"','src="other.mp3"'),page.replace('<audio preload="none" src="test.mp3"></audio>',''),page.replace('class="speak"','class="speak" disabled')]:
 try:inspect_page(broken)
 except AssertionError:pass
 else:raise AssertionError('Missing, mismatched or disabled narration was accepted')
pending=page.replace('data-side="read"','data-side="read" data-audio-pending="1"').replace('class="speak"','class="speak" disabled').replace('data-audio="test.mp3"','data-audio=""').replace('src="test.mp3"','src=""')
assert inspect_page(pending,True) is None
try:inspect_page(pending)
except AssertionError:pass
else:raise AssertionError('Incomplete audio accepted as delivery')
r=subprocess.run([sys.executable,str(p/'scripts/native_once.py')],capture_output=True,text=True)
assert r.returncode and 'Retired' in r.stderr
for f in (p/'scripts').glob('*.py'):ast.parse(f.read_text())
for script in ['build_deck.py','build_consumer_deck.py','build_teaching_deck.py','legacy_logic_deck.py']:
 r=subprocess.run([sys.executable,str(p/'scripts'/script)],capture_output=True,text=True);assert r.returncode and 'Legacy maintenance only' in r.stderr,(script,r.stderr)
# Check tangent and budget geometry independently at plotted E.
epsilon=1e-5;assert abs((18/(6+epsilon)-18/(6-epsilon))/(2*epsilon)+.5)<1e-8
assert 18/6==6-6/2
result={'mixed_nodes_preserved':True,'invalid_inputs_rejected':21,'coverage_reference_gate':True,'shared_research_supported':True,'math_title_supported':True,'missing_media_rejected':True,'legacy_native_runner_retired':True,'legacy_routes_fenced':4,'all_python_parse':True,'IC_tangency_verified':True}
print(json.dumps(result,indent=2))

# Simulate Anki extracting every script, then recover the map's semantic data.
import re, html as html_module
card_dom = re.sub(r"<script\b[^>]*>.*?</script>", "", html, flags=re.S | re.I)
payload = re.search(r'<div hidden class="map-data">(.*?)</div>', card_dom, re.S)
assert payload, "Native DOM lost map data after script extraction"
parsed = json.loads(html_module.unescape(payload.group(1)))
assert parsed['edges'] == fixture['cards'][0]['edges']
assert parsed['reading_order'] == fixture['cards'][0]['reading_order']
