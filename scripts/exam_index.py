"""Query the exam registries in references/exams/: syllabus items and indexed past-paper questions.

The registries save routine research for exams already catalogued (CIE 9708 A Level, all Pearson IAL
Mathematics units). They are a head start, not a substitute: confirm the syllabus version and target
series, look for series newer than the registry, and research unfamiliar material as usual.

Usage:
  python scripts/exam_index.py --list                         # registries, units, entry counts, latest series
  python scripts/exam_index.py WMA14 --spec 4.1               # questions on P4 item 4.1 (binomial series)
  python scripts/exam_index.py WST02 --grep "sampling frame"  # full-text search in asks / MS / ER notes
  python scripts/exam_index.py 9708/4 --spec 8.1.1 --since 2024-01
  python scripts/exam_index.py WMA14 --coverage               # how often each spec item has been examined
  python scripts/exam_index.py WMA14 --spec 4.1 --demands     # entries shaped for deck.json "demands"
  python scripts/exam_index.py --check                        # validate every registry (used by the tests)
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMS = ROOT / 'references' / 'exams'
SERIES = re.compile(r'^\d{4}-(0[1-9]|1[0-2])$')
PART_FIELDS = ('part', 'marks', 'spec', 'command', 'ask', 'final_form', 'ms', 'er')


def registries(base=EXAMS):
    """{board folder: {'items': {unit: {id: item}}, 'questions': [entries]}}"""
    out = {}
    for folder in sorted(p for p in base.iterdir() if p.is_dir()) if base.is_dir() else []:
        items = {}
        for path in sorted(folder.glob('spec-items*.json')):
            for unit, catalogue in json.loads(path.read_text(encoding='utf-8')).items():
                items.setdefault(unit, {}).update(catalogue)
        questions = []
        for path in sorted(folder.rglob('*.questions.json')):
            for entry in json.loads(path.read_text(encoding='utf-8')):
                entry['_file'] = str(path.relative_to(base))
                questions.append(entry)
        if items or questions:
            out[folder.name] = {'items': items, 'questions': questions}
    return out


def spec_unit(entry):
    """The spec-items key an entry's spec ids refer to (9708 papers share one syllabus)."""
    return '9708' if str(entry.get('unit', '')).startswith('9708') else entry.get('unit')


def check(base=EXAMS):
    """Every entry well formed, marks add up, spec ids exist, ids unique."""
    problems = []
    for board, reg in registries(base).items():
        seen = set()
        for e in reg['questions']:
            where = f'{e.get("_file")}:{e.get("id")}'
            for key in ('id', 'unit', 'paper', 'series', 'q', 'marks', 'parts', 'sources'):
                if key not in e:
                    problems.append(f'{where}: missing {key}')
            if e.get('id') in seen:
                problems.append(f'{where}: duplicate id')
            seen.add(e.get('id'))
            if not SERIES.match(str(e.get('series', ''))):
                problems.append(f'{where}: series must be YYYY-MM')
            parts = e.get('parts') or []
            if not parts:
                problems.append(f'{where}: no parts')
            catalogue = reg['items'].get(spec_unit(e), {})
            for p in parts:
                for key in PART_FIELDS:
                    if key not in p:
                        problems.append(f'{where} part {p.get("part")}: missing {key}')
                for sid in p.get('spec', []):
                    if catalogue and sid not in catalogue:
                        problems.append(f'{where} part {p.get("part")}: unknown spec item {sid}')
            if parts and all(isinstance(p.get('marks'), int) for p in parts) and isinstance(e.get('marks'), int):
                if sum(p['marks'] for p in parts) != e['marks']:
                    problems.append(f'{where}: part marks {sum(p["marks"] for p in parts)} != total {e["marks"]}')
    return problems


def select(questions, unit=None, spec=None, grep=None, since=None):
    out = []
    for e in questions:
        if unit and e.get('unit') != unit:
            continue
        if since and e.get('series', '') < since:
            continue
        parts = e['parts']
        if spec:
            parts = [p for p in parts if any(s == spec or s.startswith(spec + '.') for s in p.get('spec', []))]
        if grep:
            rx = re.compile(re.escape(grep), re.I)
            parts = [p for p in parts if rx.search(' '.join(str(p.get(k, '')) for k in ('ask', 'final_form', 'ms', 'er', 'command')))]
        if parts:
            out.append(dict(e, parts=parts))
    return sorted(out, key=lambda e: (e['series'], e.get('paper', ''), str(e['q']).zfill(3)), reverse=True)


def as_demands(entries):
    """Entries shaped for deck.json "demands": points and cards are filled by the card maker."""
    out = []
    for e in entries:
        for p in e['parts']:
            out.append({'id': f'{e["id"]}{p["part"]}', 'series': e['series'], 'q': f'Q{e["q"]}{p["part"]}', 'command': p['command'],
                        'ask': p['ask'], 'final_form': p['final_form'], 'marks': str(p['marks']), 'ms_notes': p['ms'],
                        'er_notes': p['er'], 'spec': p['spec'], 'points': [], 'cards': [], 'source': e.get('sources', {})})
    return out


def coverage(questions, items, unit):
    counts = Counter(s for e in questions if e.get('unit') == unit for p in e['parts'] for s in p.get('spec', []))
    catalogue = items.get('9708' if unit.startswith('9708') else unit, {})
    rows = [(sid, catalogue[sid].get('title', ''), counts.get(sid, 0)) for sid in catalogue]
    rows += [(sid, '(not in catalogue)', n) for sid, n in counts.items() if sid not in catalogue]
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('unit', nargs='?', help='unit code, e.g. WMA14, WST02, 9708/3, 9708/4')
    ap.add_argument('--spec', help='spec item id, e.g. 4.1 or 8.1.1 (prefix match)')
    ap.add_argument('--grep', help='case-insensitive text in ask / final form / MS / ER notes')
    ap.add_argument('--since', help='earliest series, YYYY-MM')
    ap.add_argument('--coverage', action='store_true')
    ap.add_argument('--demands', action='store_true', help='print JSON shaped for deck.json demands')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args(argv)
    regs = registries()
    if a.check:
        problems = check()
        print('\n'.join(problems) or f'ok: {sum(len(r["questions"]) for r in regs.values())} entries')
        return 1 if problems else 0
    if a.list or not a.unit:
        for board, reg in regs.items():
            by_unit = Counter(e['unit'] for e in reg['questions'])
            latest = {}
            for e in reg['questions']:
                latest[e['unit']] = max(latest.get(e['unit'], ''), e['series'])
            print(f'{board}: ' + ', '.join(f'{u} {n} questions (latest {latest[u]})' for u, n in sorted(by_unit.items())))
        return 0
    questions = [e for r in regs.values() for e in r['questions']]
    items = {u: c for r in regs.values() for u, c in r['items'].items()}
    if a.coverage:
        for sid, title, n in coverage(questions, items, a.unit):
            print(f'{sid:>8}  {n:3d}  {title}')
        return 0
    found = select(questions, a.unit, a.spec, a.grep, a.since)
    if a.demands:
        print(json.dumps(as_demands(found), ensure_ascii=False, indent=1))
        return 0
    for e in found:
        print(f'{e["paper"]} {e["series"]} Q{e["q"]} ({e["marks"]} marks)  [{e.get("sources", {}).get("qp", "")}]')
        for p in e['parts']:
            print(f'  ({p["part"] or "-"}) {p["marks"]}m {",".join(p["spec"])} {p["command"]}: {p["ask"]}')
            for key in ('final_form', 'ms', 'er'):
                if p.get(key):
                    print(f'      {key}: {p[key]}')
    print(f'{len(found)} questions', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
