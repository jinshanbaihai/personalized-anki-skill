"""Tests for scripts/exam_index.py and the shipped exam registries (references/exams/)."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

import exam_index as x

ROOT = Path(__file__).resolve().parent.parent
EXAMS = ROOT / 'references' / 'exams'


@pytest.fixture(scope='module')
def real():
    regs = x.registries()
    questions = [e for r in regs.values() for e in r['questions']]
    items = {u: c for r in regs.values() for u, c in r['items'].items()}
    return questions, items, x.load_versions()


def run(*args, env=None):
    return subprocess.run([sys.executable, str(ROOT / 'scripts' / 'exam_index.py'), *args], capture_output=True,
                          text=True, encoding='utf-8', errors='replace', env=env)


def entry(series='2024-06', q='1', paper='WMA14/01', ms='M1 B1 A1 A1', sources=None):
    return {'id': f'WMA14-{series}-{paper[-2:]}-Q{q}', 'unit': 'WMA14', 'paper': paper, 'series': series, 'q': q, 'marks': 5,
            'parts': [{'part': 'a', 'marks': 4, 'spec': ['4.1'], 'command': 'Find', 'ask': 'first four terms',
                       'final_form': 'simplest form', 'ms': ms, 'er': ''},
                      {'part': 'b', 'marks': 1, 'spec': ['4.1'], 'command': 'State', 'ask': 'validity', 'final_form': '|x|<1/4',
                       'ms': 'B1' if ms else '', 'er': ''}],
            'sources': sources if sources is not None else {'qp': 'drive:"qp.pdf" (id x)', 'ms': 'https://example.org/ms.pdf' if ms else '', 'er': ''}}


def demo(tmp_path, entries, versions=None):
    board = tmp_path / 'demo'
    (board / 'units').mkdir(parents=True)
    (board / 'spec-items.json').write_text(json.dumps({'WMA14': {'4.1': {'title': 'binomial', 'page': 27},
                                                                 '6.4': {'title': 'DE', 'page': 28}}}), encoding='utf-8')
    (board / 'units' / 'WMA14.questions.json').write_text(json.dumps(entries), encoding='utf-8')
    if versions is not None:
        (tmp_path / 'versions.json').write_text(json.dumps(versions), encoding='utf-8')
    return board


# ------------------------------------------------------------ shipped registry

def test_shipped_registry_checks_and_gaps_are_complete(real):
    questions, items, versions = real
    assert x.check() == []
    unlisted, stale, computed = x.completeness(questions, versions)
    assert unlisted == [] and stale == [], (unlisted[:5], stale[:5])
    assert computed, 'the snapshot has known gaps; an empty list means the rules stopped running'
    reasons = versions['gaps']['reasons']
    assert all(item['reason'] in reasons for item in versions['gaps']['items'])


def test_expected_series_rules_reproduce_the_per_unit_lists(real):
    _, _, versions = real
    rules = versions['expected_papers']['pearson-ial-maths']
    for unit, info in versions['ial']['units'].items():
        assert x.ial_series(info, rules, '2026-06') == info['expected_series_through_2026_06'], unit
    papers = x.expected_papers('9708/3', versions)
    assert ('2023-03', '9708/32') in papers and ('2025-06', '9708/34') in papers and ('2023-03', '9708/31') not in papers


def test_every_source_is_resolvable_and_build_paths_have_a_locator(real):
    questions, _, _ = real
    for e in questions:
        for doc in x.DOCS:
            text = e['sources'][doc]
            if not text:
                continue
            assert x.LOCATOR.search(text), (e['id'], doc)
            assert re.match(r'(Pearson Edexcel IAL|Cambridge International) ', text), (e['id'], doc, 'neutral citation first')
            if 'local:src' in text:
                assert 'https://' in text or 'drive:' in text, (e['id'], doc)


def test_shipped_text_has_no_personal_wording_or_dead_tool_references():
    banned = re.compile(r'用户 ?Drive|用户已|用户自己|user\'s Drive|merge_validate|series_check\.py')
    hits = [f'{p.relative_to(EXAMS)}:{i}' for p in EXAMS.rglob('*') if p.suffix in ('.md', '.json')
            for i, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1) if banned.search(line)]
    assert hits == []


def test_wst02_gaps_are_computed_not_stale(real):
    questions, _, versions = real
    gaps = x.compute_gaps('WST02', questions, versions)
    kinds = {g['kind'] for g in gaps}
    assert 'ms' not in kinds  # every indexed WST02 paper has its MS (older notes said otherwise)
    assert {'2026-01 WST02/01', '2026-06 WST02/01'} <= {f'{g["series"]} {g["paper"]}' for g in gaps if g['kind'] == 'paper'}
    out = run('WST02', '--gaps')
    assert out.returncode == 0 and 'UNLISTED' not in out.stdout and 'listed: pearson_secure' in out.stdout


def test_duplicate_variants_are_marked_and_skipped(real):
    questions, items, _ = real
    dups = [e for e in questions if e.get('same_as')]
    assert {(e['series'], e['paper']) for e in dups} == {('2023-06', '9708/33'), ('2024-06', '9708/33'), ('2025-06', '9708/33'),
                                                         ('2023-06', '9708/43'), ('2024-06', '9708/43'), ('2025-06', '9708/43')}
    by_id = {e['id']: e for e in questions}
    for e in dups:
        kept = by_id[e['same_as']]
        assert e['paper'] in kept['papers'] and kept['paper'] in kept['papers']
        assert [p['ask'] for p in e['parts']] == [p['ask'] for p in kept['parts']]
    default = x.select(questions, ['9708/3', '9708/4'], items=items)
    everything = x.select(questions, ['9708/3', '9708/4'], items=items, all_variants=True)
    assert len(everything) - len(default) == len(dups) and not any(e.get('same_as') for e in default)
    plain = dict((s, n) for s, _, n in x.coverage(questions, items, '9708/3'))
    full = dict((s, n) for s, _, n in x.coverage(questions, items, '9708/3', all_variants=True))
    assert sum(full.values()) > sum(plain.values())


# ------------------------------------------------------------ names, aliases, CLI robustness

def test_unit_names_are_normalised_and_unknown_ones_fail(real):
    questions, _, versions = real
    assert x.resolve_units('wst02', questions, versions) == ['WST02']
    assert x.resolve_units('9708', questions, versions) == ['9708/3', '9708/4']
    assert x.resolve_units('9708/42', questions, versions) == ['9708/4']
    assert x.resolve_units('s2', questions, versions) == ['WST02']
    assert x.resolve_units('WMA14/01A', questions, versions) == ['WMA14']
    with pytest.raises(x.UnknownName) as err:
        x.resolve_units('WSTO2', questions, versions)
    assert 'WST02' in err.value.nearest
    bad = run('WSTO2')
    assert bad.returncode != 0 and 'WST02' in bad.stderr
    assert run('WMA14', '--spec', '9.9').returncode != 0
    assert run('WMA14', '--since', '2024').returncode != 0


def test_misprinted_spec_numbers_have_aliases(real):
    questions, items, _ = real
    cat = items['WST01']
    assert x.resolve_spec('6.1', cat) == '6.1' and x.resolve_spec('5.1#2', cat) == '6.1' and x.resolve_spec('6', cat) == '6'
    normal = x.select(questions, 'WST01', spec='6.1', items=items)
    assert normal and all(any(x.canonical(s, cat) == '6.1' for s in p['spec']) for e in normal for p in e['parts'])
    for spec in ('5.1', '5'):
        for e in x.select(questions, 'WST01', spec=spec, items=items):
            for p in e['parts']:
                assert any(x.canonical(s, cat).startswith('5') for s in p['spec']), (spec, e['id'], p['spec'])
    only_normal = [p for e in x.select(questions, 'WST01', spec='5', items=items) for p in e['parts'] if p['spec'] == ['5.1#2']]
    assert only_normal == []
    assert x.select(questions, 'WFM02', spec='7.2', items=items)
    assert x.resolve_spec('7.2', items['WFM02']) == '7.2'


def test_banner_reports_snapshot_latest_missing_and_empty_parts():
    out = run('WST02', '--spec', '4.1')
    assert out.returncode == 0
    line = out.stderr.splitlines()[0]
    assert '2026-10-06' in line and 'latest indexed series 2025-10' in line
    assert 'expected series not fully indexed' in line and 'without MS' in line and 'without ER' in line


def test_output_is_utf8_safe_on_an_ascii_console():
    env = dict(os.environ, PYTHONIOENCODING='ascii')
    out = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'exam_index.py'), 'WST01', '--spec', '6.1'],
                         capture_output=True, env=env)
    assert out.returncode == 0 and out.stdout


# ------------------------------------------------------------ synthetic registries

def test_gaps_and_completeness_on_a_synthetic_registry(tmp_path):
    versions = {'checked': '2026-10-06',
                'ial': {'units': {'WMA14': {'unit': 'P4', 'first_series': '2024-01', 'series_offered': ['January', 'June'],
                                            'pre_june_2020_availability_2018_spec': []}}},
                'expected_papers': {'through': '2024-06', 'pearson-ial-maths': {'regular_from': '2020-06', 'cancelled': [], 'all_units': [],
                                                                                'variants': {'01A': {'2024-06': ['WMA14']}}}},
                'gaps': {'items': [{'unit': 'WMA14', 'kind': 'paper', 'reason': 'r', 'papers': ['2024-01 WMA14/01']}]}}
    demo(tmp_path, [entry('2024-06', ms='')], versions)
    regs = x.registries(tmp_path)
    qs = regs['demo']['questions']
    v = x.load_versions(tmp_path)
    assert x.expected_papers('WMA14', v) == [('2024-01', 'WMA14/01'), ('2024-06', 'WMA14/01'), ('2024-06', 'WMA14/01A')]
    got = {(g['kind'], g['series'], g['paper']) for g in x.compute_gaps('WMA14', qs, v)}
    assert got == {('paper', '2024-01', 'WMA14/01'), ('paper', '2024-06', 'WMA14/01A'), ('ms', '2024-06', 'WMA14/01'),
                   ('er', '2024-06', 'WMA14/01'), ('qp-drive-only', '2024-06', 'WMA14/01')}
    unlisted, stale, _ = x.completeness(qs, v)
    assert len(unlisted) == 4 and stale == []
    v['gaps']['items'].append({'unit': 'WMA14', 'kind': 'paper', 'reason': 'r', 'papers': ['2023-06 WMA14/01']})
    assert x.completeness(qs, v)[1] == [('WMA14', 'paper', '2023-06 WMA14/01')]


def test_partial_documents_and_mixed_locators_are_gaps(tmp_path):
    with_ms = entry('2024-06', q='1', sources={'qp': 'https://example.org/qp.pdf', 'ms': 'https://example.org/ms.pdf', 'er': ''})
    without = entry('2024-06', q='2', ms='', sources={'qp': 'drive:"qp.pdf" (id x)', 'ms': '', 'er': ''})
    demo(tmp_path, [with_ms, without])
    qs = x.registries(tmp_path)['demo']['questions']
    kinds = {g['kind'] for g in x.compute_gaps('WMA14', qs, {})}
    assert kinds == {'ms-partial', 'er', 'qp-drive-only'}


def test_check_requires_a_resolvable_locator(tmp_path):
    demo(tmp_path, [entry(sources={'qp': 'local:src/WMA14/2024-06_01_qp.pdf', 'ms': 'github:o/r@abc1234 ms.pdf', 'er': ''})])
    problems = x.check(tmp_path)
    assert any('sources.qp has no resolvable locator' in p for p in problems) and not any('sources.ms' in p for p in problems)


def test_demands_fields(tmp_path):
    demo(tmp_path, [entry('2024-06'), entry('2024-01', ms='')])
    qs = x.registries(tmp_path)['demo']['questions']
    held, missing = (x.as_demands(x.select(qs, 'WMA14', since=s), '2026-10-06') for s in ('2024-06', '2024-01'))
    first = held[0]
    assert first['marks'] == 'M1 B1 A1 A1' and first['marks_total'] == 4 and first['ms_source'] == 'registry summary'
    assert first['q'] == 'Q1a' and first['spec'] == ['4.1'] and first['er_notes'].startswith('ER not held')
    gap = [d for d in missing if d['series'] == '2024-01'][0]
    assert gap['ms_notes'] == 'MS not held in registry (snapshot 2026-10-06)' and gap['ms_source'] == 'not held' and gap['marks'] == '4'
    readme = (EXAMS / 'README.md').read_text(encoding='utf-8')
    assert all(f'`{key}`' in readme for key in first), [k for k in first if f'`{k}`' not in readme]


def test_ms_codes():
    assert x.ms_codes('M1A1 gradient; B1 x; M1 y; A1 z', 5) == 'M1 A1 B1 M1 A1'
    assert x.ms_codes('(i) dM1 solve; A1cso.', 2) == 'dM1 A1'
    assert x.ms_codes('B1 each (MS p.16)', 2) is None
    assert x.ms_codes('key: B (MS p.2)', 1) is None


def test_check_file_for_registry_additions(tmp_path):
    good = tmp_path / 'WMA14.questions.json'
    good.write_text(json.dumps([entry('2026-06', paper='WMA14/01')]), encoding='utf-8')
    problems, _ = x.check_file(good)
    assert problems == []
    assert run('--check-file', str(good)).returncode == 0
    bad = entry('2026-06', sources={'qp': 'local:src/x.pdf', 'ms': '', 'er': ''})
    bad['parts'][0]['spec'] = ['9.9']
    bad['unit'] = 'WMA14'
    path = tmp_path / 'bad.questions.json'
    path.write_text(json.dumps([bad]), encoding='utf-8')
    problems, _ = x.check_file(path)
    assert any('unknown spec item 9.9' in p for p in problems) and any('no resolvable locator' in p for p in problems)
    assert run('--check-file', str(path)).returncode == 1
