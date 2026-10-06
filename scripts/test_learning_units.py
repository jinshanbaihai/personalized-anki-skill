"""Knowledge-scope regression checks; synthetic data is not academic research."""
import copy
import json
import sqlite3
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from build_map_deck import validate, source_record, FIELDS

ROOT = Path(__file__).resolve().parent.parent
sample = json.loads((ROOT / 'assets/map-example.json').read_text())
data = copy.deepcopy(sample)
data.update(
    academic=True,
    test_deck=True,
    syllabus={'url': 'synthetic-fixture', 'edition': 'synthetic'},
    exam_task={k: 'Synthetic exam context' for k in ('qualification', 'authority', 'version', 'component', 'task_type')},
    research_basis={
        'input_trace': 'Synthetic board image, page 1, labels A–B; no actual classroom material is claimed.',
        'textbook_refs': 'Synthetic textbook, edition 1, chapter 2, pp. 10–20; no real book is claimed.',
        'reading_record': 'Synthetic record covering the chapter introduction, complete model and conclusion.',
        'model_synthesis': 'Synthetic model: objects → constraint → relationship → condition → conclusion.',
        'source_review': 'Fixture verifies structure, not source quality or completed reading.',
        'syllabus_refs': 'Synthetic syllabus section 2, clauses 1 and 2.',
        'question_refs': 'Synthetic essay and MCQ references with paper and question locations.',
        'marking_refs': 'Synthetic assessment and marking source location.',
        'examiner_refs': 'Synthetic examiner source location; no real report is claimed.',
        'human_response_refs': 'Fixture scenario: full human response unavailable; limitation recorded, with textbook and official assessment evidence supporting these foundation cards.',
    },
)
first = data['cards'][0]
first.update(
    scope='Synthetic syllabus section 2.1',
    research_use='The synthetic textbook explanation supplies the first knowledge relationship.',
    sources=['Synthetic textbook, edition 1, chapter 2, pp. 10–14; fixture only.'],
    learning_unit={
        'starting_point': 'The local card identifies its objects without relying on review order.',
        'boundary': 'Only the first relationship and its necessary condition.',
        'explanation_review': 'Synthetic review retained the causal bridge and removed an unrelated branch.',
    },
)
second = copy.deepcopy(first)
second['id'] = 'fixture-second'
second['scope'] = 'Synthetic syllabus section 2.2'
second['sources'] = ['Synthetic textbook, edition 1, chapter 2, pp. 15–20; fixture only.']
second['learning_unit']['boundary'] = 'The second relationship and its condition.'
data['cards'].append(second)
data['knowledge_coverage'] = {
    'scope_id': 'synthetic-topic',
    'scope': 'Synthetic syllabus section 2: two knowledge relationships.',
    'status': 'complete',
    'remaining': '',
    'required_core': ['k1', 'k2'],
    'items': [
        {'id': 'k1', 'syllabus_item': '2.1', 'knowledge': 'First relationship', 'classification': 'core',
         'evidence': 'Synthetic syllabus clause 2.1 and textbook pp. 10–14.',
         'locations': [{'card': first['id'], 'nodes': ['a', 'b']}]},
        {'id': 'k2', 'syllabus_item': '2.2', 'knowledge': 'Second relationship', 'classification': 'core',
         'evidence': 'Synthetic syllabus clause 2.2 and textbook pp. 15–20.',
         'locations': [{'card': second['id'], 'nodes': ['b']}]},
        {'id': 'p1', 'syllabus_item': 'Prerequisite for 2.1', 'knowledge': 'Necessary object identification',
         'classification': 'prerequisite', 'evidence': 'Synthetic textbook model setup.',
         'reason': 'Required to understand the first relationship; not an independent syllabus outcome.',
         'locations': [{'card': first['id'], 'nodes': ['a']}]},
        {'id': 'x1', 'syllabus_item': 'Outside section 2', 'knowledge': 'Advanced extension',
         'classification': 'excluded', 'evidence': 'Synthetic chapter extension and syllabus boundary.',
         'reason': 'Not required by the confirmed syllabus and unnecessary for the local explanation.', 'locations': []},
    ],
}
data['assessment_checks'] = [{
    'question_refs': 'Synthetic representative question, paper and location.',
    'marking_refs': 'Synthetic marking requirements and level descriptors.',
    'application_review': 'Synthetic review traces an analysis to the first relationship and checks its condition.',
    # The assessment check need not label every foundation card as a separate mark.
    'locations': [{'card': first['id'], 'nodes': ['b']}],
}]
validate(data)
assert 'answer_basis' not in data and all('exam_use' not in c and 'question' not in c for c in data['cards'])
partial = copy.deepcopy(data)
partial['cards'] = partial['cards'][:1]
partial['knowledge_coverage'].update(status='partial', remaining='k2: the second relationship is not delivered.')
partial['knowledge_coverage']['items'][1]['locations'] = []
partial.pop('assessment_checks')
validate(partial)
# A justified foundation can be delivered before its target core relationship.
foundation_only = copy.deepcopy(partial)
foundation_only['knowledge_coverage']['items'][0]['locations'] = []
foundation_only['knowledge_coverage']['items'][2]['locations'] = [{'card': first['id'], 'nodes': ['a', 'b']}]
foundation_only['knowledge_coverage']['remaining'] = 'k1 and k2 remain; this delivery teaches their necessary objects only.'
validate(foundation_only)

rejected = []
def reject(label, mutate, source=data):
    bad = copy.deepcopy(source)
    mutate(bad)
    try:
        validate(bad)
    except AssertionError:
        rejected.append(label)
    else:
        raise AssertionError(label + ' was accepted')

reject('missing local scope', lambda d: d['cards'][0].pop('scope'))
reject('missing learning unit', lambda d: d['cards'][0].pop('learning_unit'))
for key in ('starting_point', 'boundary', 'explanation_review'):
    reject('missing local ' + key, lambda d, k=key: d['cards'][0]['learning_unit'].update({k: ''}))
reject('missing knowledge source', lambda d: d['cards'][0].update(sources=[]))
reject('blank knowledge source', lambda d: d['cards'][0].update(sources=[' ']))
reject('missing local research use', lambda d: d['cards'][0].pop('research_use'))
reject('missing exam context', lambda d: d.pop('exam_task'))
reject('missing textbook study', lambda d: d.pop('research_basis'))
for key in data['research_basis']:
    reject('missing research ' + key, lambda d, k=key: d['research_basis'].pop(k))
reject('missing knowledge coverage', lambda d: d.pop('knowledge_coverage'))
reject('missing scope identity', lambda d: d['knowledge_coverage'].pop('scope_id'))
reject('complete with unresolved gap', lambda d: d['knowledge_coverage'].update(remaining='k2 not taught'))
reject('partial without disclosed remainder', lambda d: d['knowledge_coverage'].update(status='partial'))
reject('unknown coverage status', lambda d: d['knowledge_coverage'].update(status='draft'))
reject('empty knowledge requirements', lambda d: d['knowledge_coverage'].update(items=[]))
reject('missing independent core inventory', lambda d: d['knowledge_coverage'].pop('required_core'))
reject('duplicate core inventory ID', lambda d: d['knowledge_coverage'].update(required_core=['k1', 'k1', 'k2']))
reject('a whole required item silently omitted', lambda d: d['knowledge_coverage']['items'].pop(1))
reject('required item downgraded to excluded', lambda d: d['knowledge_coverage']['items'][1].update(classification='excluded', reason='An invented exclusion cannot override the core inventory.', locations=[]))
reject('required item downgraded to prerequisite', lambda d: d['knowledge_coverage']['items'][1].update(classification='prerequisite', reason='An invented classification cannot override the core inventory.'))
reject('missing syllabus position', lambda d: d['knowledge_coverage']['items'][0].pop('syllabus_item'))
reject('missing knowledge evidence', lambda d: d['knowledge_coverage']['items'][0].update(evidence=''))
reject('duplicate knowledge identity', lambda d: d['knowledge_coverage']['items'][1].update(id='k1'))
reject('unknown knowledge class', lambda d: d['knowledge_coverage']['items'][0].update(classification='interesting'))
reject('core knowledge omitted from complete set', lambda d: d['knowledge_coverage']['items'][1].update(locations=[]))
reject('unmapped card', lambda d: d['knowledge_coverage']['items'][1].update(locations=[{'card': first['id'], 'nodes': ['b']}]))
reject('unknown card reference', lambda d: d['knowledge_coverage']['items'][0]['locations'][0].update(card='missing'))
reject('unknown node reference', lambda d: d['knowledge_coverage']['items'][0]['locations'][0].update(nodes=['missing']))
reject('prerequisite without reason', lambda d: d['knowledge_coverage']['items'][2].pop('reason'))
reject('excluded extension without reason', lambda d: d['knowledge_coverage']['items'][3].pop('reason'))
reject('excluded extension appears in cards', lambda d: d['knowledge_coverage']['items'][3].update(locations=[{'card': first['id'], 'nodes': ['a']}]))
reject('complete without application check', lambda d: d.pop('assessment_checks'))
reject('application review absent', lambda d: d['assessment_checks'][0].update(application_review=''))
reject('application points to missing node', lambda d: d['assessment_checks'][0]['locations'][0].update(nodes=['missing']))
reject('partial application check cannot cite missing node', lambda d: d.update(assessment_checks=[dict(data['assessment_checks'][0], locations=[{'card': first['id'], 'nodes': ['missing']}])]), source=partial)

# Source is JSON stored in an HTML-valued Anki field; keep both layers intact.
data['research_basis']['source_review'] += ' Literal metadata: MSC<MPC, MSB>MPB & quoted <q>labels</q>.'
exported = source_record(data, first)
for key in ('research_basis', 'knowledge_coverage', 'assessment_checks'):
    assert exported[key] == data[key]
assert exported['learning_unit'] == first['learning_unit'] and exported['sources'] == first['sources']
assert all(key not in exported for key in ('answer_basis', 'task_coverage', 'answer_coverage'))

# A historical shared-task record is accepted only for explicit technical maintenance.
legacy = copy.deepcopy(data)
for key in ('research_basis', 'knowledge_coverage', 'assessment_checks'):
    legacy.pop(key)
legacy['answer_basis'] = {k: 'Synthetic historical evidence' for k in ('question_refs', 'human_answer_refs', 'quality_review', 'marking_refs', 'teaching_refs', 'difficulty_review')}
for card in legacy['cards']:
    card['exam_use'] = 'Synthetic historical task use'
legacy['task_coverage'] = [{
    'question': 'Historical synthetic question', 'standard': 'Historical synthetic standard',
    'worked_answer': 'Historical synthetic answer', 'reconstruction_review': 'Historical synthetic review',
    'status': 'complete', 'remaining': '',
    'requirements': [{'requirement': 'Historical combined relationship', 'evidence': 'Synthetic evidence',
                      'teaching': 'Synthetic combined explanation',
                      'locations': [{'card': c['id'], 'nodes': ['a', 'b']} for c in legacy['cards']]}],
}]
validate(legacy, legacy_coverage=True)
legacy_source_text = copy.deepcopy(legacy)
legacy_source_text['cards'][0]['sources'] = 'Historical source text preserved during technical maintenance.'
validate(legacy_source_text, legacy_coverage=True)
assert source_record(legacy_source_text, legacy_source_text['cards'][0])['sources'] == legacy_source_text['cards'][0]['sources']
reject('legacy schema cannot silently authorize new cards', lambda d: None, source=legacy)
assert source_record(legacy, legacy['cards'][0])['task_coverage'] == legacy['task_coverage']

# Exercise the default CLI, render and export path with complete and question-free partial batches.
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    for name, value in [('complete', data), ('partial', partial)]:
        source = tmp / (name + '.json')
        source.write_text(json.dumps(value))
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/build_logic_deck.py'), str(source), str(tmp / name), '--preview'], capture_output=True, text=True)
        assert result.returncode == 0, result.stderr
        pages = list((tmp / name).glob('*-read.html'))
        assert len(pages) == len(value['cards'])
        assert all(page.read_text().count('class="speak"') == 1 for page in pages)
        persisted = json.loads((tmp / name / 'cards.json').read_text())
        assert persisted['knowledge_coverage'] == value['knowledge_coverage']
        assert 'research_basis' in persisted and 'answer_basis' not in persisted
    # Verify the actual note-field export, not only source_record's return value.
    source = tmp / 'complete.json'
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/build_logic_deck.py'), str(source), str(tmp / 'package'), '--text-only-test'], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    with zipfile.ZipFile(tmp / 'package' / 'CCPT-test.apkg') as archive:
        collection = tmp / 'collection.anki2'
        collection.write_bytes(archive.read('collection.anki2'))
    with sqlite3.connect(collection) as connection:
        fields = [row[0].split('\x1f') for row in connection.execute('select flds from notes')]
    assert len(fields) == 2
    for note_fields in fields:
        source_field = note_fields[FIELDS.index('Source')]
        assert not any(char in source_field for char in '<>&'), 'Source JSON must remain inert in Anki HTML fields'
        saved = json.loads(source_field)
        assert saved['research_basis']['source_review'] == data['research_basis']['source_review']
        assert saved['research_basis'] == data['research_basis']
        assert saved['knowledge_coverage']['required_core'] == ['k1', 'k2']
        assert note_fields[FIELDS.index('FrontHTML')] == note_fields[FIELDS.index('BackHTML')]
        assert 'Synthetic textbook, edition 1' not in note_fields[FIELDS.index('BackHTML')]

# Non-exam textbook reading and rendering remain possible without fabricated exam data.
non_exam = copy.deepcopy(sample)
non_exam['academic'] = False
non_exam['cards'][0]['sources'] = ['Synthetic textbook-only source, chapter 1.']
validate(non_exam)
assert 'exam_task' not in non_exam and 'research_basis' not in non_exam
assert 'answer_basis' not in source_record(non_exam, non_exam['cards'][0])
print(json.dumps({
    'knowledge_first_without_human_answer_gate': True,
    'partial_foundation_cards_need_no_question': True,
    'complete_scope_requires_application_check': True,
    'out_of_scope_extension_is_not_taught': True,
    'required_core_cannot_silently_disappear_or_be_downgraded': True,
    'source_provenance_preserved': True,
    'source_metadata_roundtrips_in_actual_package': True,
    'non_exam_textbook_reading_supported': True,
    'legacy_shared_coverage_requires_explicit_maintenance': True,
    'default_builder_complete_and_partial': True,
    'invalid_states_rejected': len(rejected),
}, indent=2))
