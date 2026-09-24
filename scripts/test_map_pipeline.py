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
 card.update(scope='synthetic test only', exam_use='synthetic test only', answer_basis={k:'synthetic test only' for k in ('question_refs','human_answer_refs','quality_review','marking_refs','answer_moves','ai_additions')})
validate(academic)
for missing in ['exam_task','human_answer_refs','quality_review','answer_moves']:
 d=copy.deepcopy(academic)
 if missing=='exam_task':del d[missing]
 else:del d['cards'][0]['answer_basis'][missing]
 try:validate(d)
 except AssertionError:pass
 else:raise AssertionError(missing+' missing evidence not detected')
for f in (p/'scripts').glob('*.py'):ast.parse(f.read_text())
for script in ['build_deck.py','build_consumer_deck.py','build_teaching_deck.py','legacy_logic_deck.py']:
 r=subprocess.run([sys.executable,str(p/'scripts'/script)],capture_output=True,text=True);assert r.returncode and 'Legacy maintenance only' in r.stderr,(script,r.stderr)
# Check tangent and budget geometry independently at plotted E.
epsilon=1e-5;assert abs((18/(6+epsilon)-18/(6-epsilon))/(2*epsilon)+.5)<1e-8
assert 18/6==6-6/2
result={'mixed_nodes_preserved':True,'invalid_inputs_rejected':9,'legacy_routes_fenced':4,'all_python_parse':True,'IC_tangency_verified':True}
print(json.dumps(result,indent=2))
