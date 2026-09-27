"""Semantic scope regression checks; synthetic data is not academic teaching."""
import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from build_map_deck import validate, source_record

ROOT = Path(__file__).resolve().parent.parent
sample = json.loads((ROOT/'assets/map-example.json').read_text())
data = copy.deepcopy(sample)
data.update(academic=True, test_deck=True,
    syllabus={'url':'synthetic-fixture', 'edition':'synthetic'},
    exam_task={k:'Synthetic fixture, not an exam source' for k in ('qualification','authority','version','component','task_type')},
    answer_basis={k:'Synthetic validation only; not read research' for k in ('question_refs','human_answer_refs','quality_review','marking_refs','teaching_refs','difficulty_review')})
first = data['cards'][0]
first.update(scope='Synthetic scope', exam_use='First local relationship supports the combined task', research_use='Synthetic shared evidence',
    learning_unit={'starting_point':'The local explanation establishes its own objects', 'boundary':'First relationship only, not the entire task', 'explanation_review':'Synthetic review: the local causal steps are present'})
second=copy.deepcopy(first);second['id']='fixture-second'
second['learning_unit']['boundary']='Second relationship and its connection to the first'
data['cards'].append(second)
data['task_coverage']=[{
    'question':'Synthetic combined task', 'standard':'Both relationships and their connection',
    'worked_answer':'Synthetic whole-task answer for validation only',
    'reconstruction_review':'Synthetic mapping verifies references, not actual pedagogy',
    'status':'complete', 'remaining':'',
    'requirements':[{'requirement':'Combined relationship', 'evidence':'Synthetic evidence', 'teaching':'First local cause connects to the second',
        'locations':[{'card':first['id'],'nodes':['a','b']},{'card':second['id'],'nodes':['b']}]}]}]
validate(data)
# Each card teaches a local scope; neither needs a whole-question answer record.
assert all('answer_coverage' not in c for c in data['cards'])
partial=copy.deepcopy(data);partial['cards']=partial['cards'][:1]
partial['task_coverage'][0].update(status='partial',remaining='Second relationship and integration not delivered')
partial['task_coverage'][0]['requirements'][0]['locations']=partial['task_coverage'][0]['requirements'][0]['locations'][:1]
validate(partial)
rejected=[]
def reject(label, mutate, source=data):
    bad=copy.deepcopy(source);mutate(bad)
    try:validate(bad)
    except AssertionError:rejected.append(label)
    else:raise AssertionError(label+' was accepted')
reject('local scope missing',lambda d:d['cards'][0].pop('learning_unit'))
reject('starting point missing',lambda d:d['cards'][0]['learning_unit'].update(starting_point=''))
reject('boundary missing',lambda d:d['cards'][0]['learning_unit'].update(boundary=''))
reject('substantive review missing',lambda d:d['cards'][0]['learning_unit'].update(explanation_review=''))
reject('shared coverage missing',lambda d:d.pop('task_coverage'))
reject('unresolved gaps called complete',lambda d:d['task_coverage'][0].update(remaining='Missing second relationship'))
reject('partial without remaining scope',lambda d:d['task_coverage'][0].update(status='partial'))
reject('unknown card reference',lambda d:d['task_coverage'][0]['requirements'][0]['locations'][0].update(card='missing'))
reject('unknown node reference',lambda d:d['task_coverage'][0]['requirements'][0]['locations'][0].update(nodes=['missing']))
reject('missing card contribution',lambda d:d['task_coverage'][0]['requirements'][0]['locations'].pop())
reject('empty requirements',lambda d:d['task_coverage'][0].update(requirements=[]))
reject('no reasoning',lambda d:d['task_coverage'][0]['requirements'][0].update(teaching=''))
reject('no integration review',lambda d:d['task_coverage'][0].update(reconstruction_review=''))
reject('no exam task',lambda d:d.pop('exam_task'))
for key in ('human_answer_refs','quality_review','marking_refs','teaching_refs','difficulty_review'):
    reject('missing research '+key,lambda d,k=key:d['answer_basis'].pop(k))
reject('no local research application',lambda d:d['cards'][0].pop('research_use'))
exported=source_record(data,first)
assert exported['learning_unit']==first['learning_unit']
assert exported['task_coverage']==data['task_coverage']
assert exported['answer_basis']==data['answer_basis']
# Run the actual default entry point with complete and partial scoped batches.
with tempfile.TemporaryDirectory() as tmp:
    tmp=Path(tmp)
    for name,value in [('complete',data),('partial',partial)]:
        source=tmp/(name+'.json');source.write_text(json.dumps(value))
        result=subprocess.run([sys.executable,str(ROOT/'scripts/build_logic_deck.py'),str(source),str(tmp/name),'--preview'],capture_output=True,text=True)
        assert result.returncode==0,result.stderr
        pages=list((tmp/name).glob('*-read.html'))
        assert len(pages)==len(value['cards'])
        assert all(page.read_text().count('class="speak"')==1 for page in pages)
print(json.dumps({'two_local_cards_joint_task':True,'partial_delivery_is_explicit':True,'source_scope_preserved':True,'default_builder_complete_and_partial':True,'invalid_states_rejected':len(rejected)},indent=2))
