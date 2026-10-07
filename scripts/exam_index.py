"""Query the exam registries in references/exams/: syllabus items and indexed past-paper questions.

The registries save routine research for exams already catalogued (CIE 9708 A Level, all Pearson IAL
Mathematics units). They are a dated snapshot, not a substitute: confirm the syllabus version and target
series, look for series newer than the registry, and fill the gaps that --gaps lists.

Usage:
  python scripts/exam_index.py --list                         # registries, units, entry counts, latest series
  python scripts/exam_index.py WMA14 --spec 4.1               # questions on P4 item 4.1 (binomial series)
  python scripts/exam_index.py WST02 --grep "sampling frame"  # full-text search in asks / MS / ER notes
  python scripts/exam_index.py 9708/4 --spec 8.1.1 --since 2024-01
  python scripts/exam_index.py 9708 --spec 7.4                # "9708" = 9708/3 and 9708/4
  python scripts/exam_index.py WMA14 --coverage               # how often each spec item has been examined
  python scripts/exam_index.py WMA14 --spec 4.1 --demands     # entries shaped for deck.json "demands"
  python scripts/exam_index.py WST02 --gaps                   # expected papers not indexed, MS / ER not held
  python scripts/exam_index.py --completeness                 # every computed gap is listed in versions.json
  python scripts/exam_index.py --check                        # validate every registry (used by the tests)
  python scripts/exam_index.py --check-file registry-additions/WST02.questions.json

Unit codes are case-insensitive; short names (P4, S2, FP1 ...) work for the Pearson units. Every query
prints a one-line banner to stderr: snapshot date, latest indexed series, expected papers not indexed,
and how many returned parts have no MS / ER. Variant papers that reuse another variant word for word
(entries with "same_as") are skipped unless --all-variants is given.
"""
import argparse
import difflib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMS = ROOT / 'references' / 'exams'
SERIES = re.compile(r'^\d{4}-(0[1-9]|1[0-2])$')
PART_FIELDS = ('part', 'marks', 'spec', 'command', 'ask', 'final_form', 'ms', 'er')
DOCS = ('qp', 'ms', 'er')
# A locator someone with only the skill zip can follow (see references/exams/README.md, "原件怎么取").
LOCATOR = re.compile(r'\b(?:drive|github|finder):|https://')
PUBLIC = re.compile(r'https://|\b(?:github|finder):')
DOCUMENT = re.compile(r'https://\S+\.(?:pdf|png)\b|\bdrive:')  # a PDF or page image, not only extracted text
_CODE = r'[dD]{0,3}[MABE][1-9]\d?(?:\*|ft)?'
MS_CODE = re.compile(r'([dD]{0,3}[MABE])([1-9]\d?)(\*|ft)?')
# the run of mark codes that opens an MS clause: "M1A1 gradient …", "(i) dM1 solve …", "B1cso …"
MS_LEAD = re.compile(rf'^\s*(?:\([a-z]+\)\s*)*((?:{_CODE}(?:cso|cao)?(?=[\s,;:().]|$|[dD]{{0,3}}[MABE]\d)[\s,]*)+)')
MONTH_CODE = {'January': '01', 'June': '06', 'October': '10'}


class UnknownName(ValueError):
    """An unknown unit or spec id; carries the nearest known names."""

    def __init__(self, what, name, nearest, known=()):
        self.what, self.name, self.nearest, self.known = what, name, list(nearest), list(known)
        hint = f'; nearest: {", ".join(self.nearest)}' if self.nearest else ''
        if not self.nearest and self.known:
            hint = f'; known: {", ".join(self.known)}'
        super().__init__(f'unknown {what} {name!r}{hint}')


# ---------------------------------------------------------------- loading

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


def load_versions(base=EXAMS):
    path = Path(base) / 'versions.json'
    return json.loads(path.read_text(encoding='utf-8')) if path.is_file() else {}


def snapshot(versions):
    return (versions or {}).get('checked', 'unknown date')


def spec_unit(entry):
    """The spec-items key an entry's spec ids refer to (9708 papers share one syllabus)."""
    unit = entry if isinstance(entry, str) else entry.get('unit', '')
    return '9708' if str(unit).startswith('9708') else unit


def canonical(sid, catalogue):
    """Printed-numbering fixes: WST01 '5.1#2' is item 6.1, WFM02 '7.1#2' is item 7.2 (spec-items "alias")."""
    return (catalogue or {}).get(sid, {}).get('alias', sid)


# ---------------------------------------------------------------- validation

def check_entries(entries, items, where_of=lambda e: e.get('id')):
    problems = []
    seen = set()
    for e in entries:
        where = where_of(e)
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
        catalogue = items.get(spec_unit(e), {})
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
        sources = e.get('sources') if isinstance(e.get('sources'), dict) else {}
        for doc in DOCS:
            text = sources.get(doc, '')
            if text and not LOCATOR.search(str(text)):
                problems.append(f'{where}: sources.{doc} has no resolvable locator (drive:, github:, finder: or https://)')
    return problems


def check(base=EXAMS):
    """Every entry well formed, marks add up, spec ids exist, ids unique, sources resolvable, duplicates consistent."""
    problems = []
    for board, reg in registries(base).items():
        problems += check_entries(reg['questions'], reg['items'], lambda e: f'{e.get("_file")}:{e.get("id")}')
        by_id = {e.get('id'): e for e in reg['questions']}
        for e in reg['questions']:
            if 'same_as' not in e:
                continue
            where = f'{e.get("_file")}:{e.get("id")}'
            kept = by_id.get(e['same_as'])
            if not kept:
                problems.append(f'{where}: same_as {e["same_as"]} not found')
                continue
            if e['paper'] not in kept.get('papers', []) or kept['paper'] not in kept.get('papers', []):
                problems.append(f'{where}: {kept["id"]} must list both paper codes in "papers"')
            if [(p['part'], p['marks'], p['ask']) for p in e['parts']] != [(p['part'], p['marks'], p['ask']) for p in kept['parts']]:
                problems.append(f'{where}: parts differ from {kept["id"]}; same_as is only for word-for-word reused papers')
    return problems


def check_file(path, base=EXAMS):
    """Validate a registry-additions file (same format as units/<unit>.questions.json) against the shipped catalogues."""
    path = Path(path)
    try:
        entries = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return [f'{path}: cannot read JSON ({exc})'], []
    if not isinstance(entries, list):
        return [f'{path}: expected a JSON list of question entries'], []
    regs = registries(base)
    items = {u: c for r in regs.values() for u, c in r['items'].items()}
    problems = check_entries(entries, items, lambda e: f'{path.name}:{e.get("id")}')
    known_units = {e['unit'] for r in regs.values() for e in r['questions']}
    for e in entries:
        if e.get('unit') not in known_units:
            problems.append(f'{path.name}:{e.get("id")}: unit {e.get("unit")!r} is not a registered unit')
    existing = {e['id'] for r in regs.values() for e in r['questions']}
    notes = [f'{e["id"]} is already in the registry (merging replaces that entry)' for e in entries if e.get('id') in existing]
    return problems, notes


# ---------------------------------------------------------------- names

def known_units(questions):
    return sorted({e['unit'] for e in questions})


def short_names(versions):
    return {v.get('unit', '').upper(): code for code, v in ((versions or {}).get('ial', {}).get('units', {}) or {}).items() if v.get('unit')}


def resolve_units(name, questions, versions=None):
    """'wst02' → ['WST02']; '9708' → ['9708/3', '9708/4']; 'S2' → ['WST02']. Unknown names raise UnknownName."""
    units = known_units(questions)
    key = re.sub(r'\s+', '', str(name)).upper()
    if key in units:
        return [key]
    group = [u for u in units if u.startswith(key + '/')]
    if group:
        return group
    m = re.fullmatch(r'(9708)/([34])\d', key)
    if m and f'{m[1]}/{m[2]}' in units:
        return [f'{m[1]}/{m[2]}']
    if key.split('/')[0] in units:  # a paper code such as WMA14/01A
        return [key.split('/')[0]]
    shorts = short_names(versions)
    if key in shorts and shorts[key] in units:
        return [shorts[key]]
    choices = units + sorted(shorts) + sorted({u.split('/')[0] for u in units if '/' in u})
    raise UnknownName('unit', name, difflib.get_close_matches(key, choices, n=5, cutoff=0.5), units)


def resolve_spec(spec, catalogue):
    """Accept a spec id or prefix ('4', '4.1', '8.1.1'), an alias ('6.1') or a raw key ('5.1#2'); return the canonical id."""
    spec = str(spec).strip()
    ids = sorted({canonical(s, catalogue) for s in catalogue})
    if spec in catalogue:
        return canonical(spec, catalogue)
    if spec in ids or any(i.startswith(spec + '.') for i in ids):
        return spec
    raise UnknownName('spec item', spec, difflib.get_close_matches(spec, ids, n=5, cutoff=0.5), ids[:12])


def spec_match(sid, spec, catalogue=None):
    c = canonical(sid, catalogue)
    return c == spec or c.startswith(spec + '.')


# ---------------------------------------------------------------- queries

def select(questions, unit=None, spec=None, grep=None, since=None, items=None, all_variants=False):
    units = [unit] if isinstance(unit, str) else unit
    rx = re.compile(re.escape(grep), re.I) if grep else None
    out = []
    for e in questions:
        if units and e.get('unit') not in units:
            continue
        if since and e.get('series', '') < since:
            continue
        if e.get('same_as') and not all_variants:
            continue
        catalogue = (items or {}).get(spec_unit(e), {})
        parts = e['parts']
        if spec:
            parts = [p for p in parts if any(spec_match(s, spec, catalogue) for s in p.get('spec', []))]
        if rx:
            parts = [p for p in parts if rx.search(' '.join(str(p.get(k, '')) for k in ('ask', 'final_form', 'ms', 'er', 'command')))]
        if parts:
            out.append(dict(e, parts=parts))
    return sorted(out, key=lambda e: (e['series'], e.get('paper', ''), str(e['q']).zfill(3)), reverse=True)


def ms_codes(ms, marks):
    """'M1 dx/du …; A1* given answer' → 'M1 A1*' when the leading codes of each clause add up to the part's marks."""
    if not ms or not isinstance(marks, int):
        return None
    codes = []
    for clause in re.split(r';', ms):
        lead = MS_LEAD.match(clause)
        if lead:
            codes += [''.join(c) for c in MS_CODE.findall(lead.group(1))]
    total = sum(int(MS_CODE.fullmatch(c).group(2)) for c in codes) if codes else 0
    return ' '.join(codes) if codes and total == marks else None


def as_demands(entries, snap=None):
    """Entries shaped for deck.json "demands": points and cards are filled by the card maker.

    marks = the MS mark codes ("M1 A1") when they can be read off the MS summary and add up, else the
    number as text; marks_total = the integer. ms_source says where ms_notes comes from."""
    snap = snap or snapshot(load_versions())
    out = []
    for e in entries:
        sources = e.get('sources', {})
        for p in e['parts']:
            n = p['marks']
            held_ms = bool(p['ms'])
            if p['er']:
                er = p['er']
            elif sources.get('er'):
                er = 'ER held; no comment on this part'
            else:
                er = f'ER not held in registry (snapshot {snap})'
            out.append({'id': f'{e["id"]}{p["part"]}', 'series': e['series'], 'paper': ' = '.join(e.get('papers', [e.get('paper', '')])),
                        'q': f'Q{e["q"]}{p["part"]}', 'command': p['command'], 'ask': p['ask'], 'final_form': p['final_form'],
                        'marks': ms_codes(p['ms'], n) or str(n), 'marks_total': n,
                        'ms_notes': p['ms'] if held_ms else f'MS not held in registry (snapshot {snap})',
                        'ms_source': 'registry summary' if held_ms else 'not held',
                        'er_notes': er, 'spec': p['spec'], 'points': [], 'cards': [], 'source': sources})
    return out


def coverage(questions, items, unit, all_variants=False):
    units = [unit] if isinstance(unit, str) else unit
    catalogue = items.get(spec_unit(units[0]), {})
    counts = Counter(canonical(s, catalogue) for e in questions if e.get('unit') in units and (all_variants or not e.get('same_as'))
                     for p in e['parts'] for s in p.get('spec', []))
    rows = [(canonical(sid, catalogue), catalogue[sid].get('title', ''), counts.get(canonical(sid, catalogue), 0)) for sid in catalogue]
    known = {r[0] for r in rows}
    rows += [(sid, '(not in catalogue)', n) for sid, n in counts.items() if sid not in known]
    return rows


# ---------------------------------------------------------------- expected papers and gaps

def ial_series(info, rules, through):
    """Series a Pearson IAL unit sits under the 2018 spec, up to `through` (versions.json expected_papers rules)."""
    months = [MONTH_CODE[m] for m in info.get('series_offered', [])]
    first = info['first_series']
    out = set(info.get('pre_june_2020_availability_2018_spec', []))
    start = rules['regular_from']
    for year in range(int(start[:4]), int(through[:4]) + 1):
        for mm in months:
            s = f'{year}-{mm}'
            if start <= s <= through and s >= first:
                out.add(s)
    out |= {s for s in rules.get('all_units', []) if first <= s <= through}
    out -= set(rules.get('cancelled', []))
    return sorted(out)


def expected_papers(unit, versions):
    """[(series, paper code)] the unit should have up to versions.json expected_papers.through; [] if no rules."""
    exp = (versions or {}).get('expected_papers', {})
    through = exp.get('through')
    if not through:
        return []
    if unit.startswith('9708'):
        table = exp.get('cie-9708', {}).get(unit, {})
        return [(s, f'9708/{v}') for s, variants in sorted(table.items()) if s <= through for v in variants]
    info = versions.get('ial', {}).get('units', {}).get(unit)
    rules = exp.get('pearson-ial-maths', {})
    if not info or not rules:
        return []
    out = [(s, f'{unit}/01') for s in ial_series(info, rules, through)]
    for variant, by_series in rules.get('variants', {}).items():
        for s, units in by_series.items():
            if s <= through and (units == 'all' or unit in units):
                out.append((s, f'{unit}/{variant}'))
    return sorted(out)


def papers_of(questions, unit):
    """{(series, paper): summary} for one unit's indexed papers (duplicates included: they are indexed papers)."""
    out = {}
    for e in questions:
        if e.get('unit') != unit:
            continue
        key = (e['series'], e['paper'])
        row = out.setdefault(key, {'questions': 0, 'parts': 0, 'no_ms': 0, 'no_er': 0, 'same_as': bool(e.get('same_as')),
                                   'held': {d: [] for d in DOCS}, 'public': {d: [] for d in DOCS}, 'text_only': []})
        row['questions'] += 1
        row['parts'] += len(e['parts'])
        row['no_ms'] += sum(1 for p in e['parts'] if not p.get('ms'))
        row['no_er'] += sum(1 for p in e['parts'] if not p.get('er'))
        for d in DOCS:
            text = str(e.get('sources', {}).get(d, ''))
            row['held'][d].append(bool(text))
            if text:
                row['public'][d].append(bool(PUBLIC.search(text)))
        qp = str(e.get('sources', {}).get('qp', ''))
        row['text_only'].append(bool(qp) and not DOCUMENT.search(qp))
    return out


def compute_gaps(unit, questions, versions):
    """Gaps derived from the data. Each gap: {unit, kind, series, paper}; kinds: paper (expected paper not indexed),
    ms / er (indexed paper whose MS / examiner report is not held), ms-partial / er-partial (held for some of its
    questions only), qp-text (QP only as extracted text), qp- / ms- / er-drive-only (a source with no public locator)."""
    gaps = []
    indexed = papers_of(questions, unit)
    for s, paper in expected_papers(unit, versions):
        if (s, paper) not in indexed:
            gaps.append({'unit': unit, 'kind': 'paper', 'series': s, 'paper': paper})
    for (s, paper), row in sorted(indexed.items()):
        for d in ('ms', 'er'):
            if not any(row['held'][d]):
                gaps.append({'unit': unit, 'kind': d, 'series': s, 'paper': paper})
            elif not all(row['held'][d]):
                gaps.append({'unit': unit, 'kind': f'{d}-partial', 'series': s, 'paper': paper})
        if any(row['text_only']):
            gaps.append({'unit': unit, 'kind': 'qp-text', 'series': s, 'paper': paper})
        for d in DOCS:
            if not all(row['public'][d]):
                gaps.append({'unit': unit, 'kind': f'{d}-drive-only', 'series': s, 'paper': paper})
    return gaps


def listed_gaps(versions):
    """{(unit, kind, 'series paper'): reason} from versions.json gaps.items."""
    out = {}
    for item in (versions or {}).get('gaps', {}).get('items', []):
        for ref in item.get('papers', []):
            out[(item['unit'], item['kind'], ref)] = item.get('reason', '')
    return out


def gap_key(g):
    return (g['unit'], g['kind'], f'{g["series"]} {g["paper"]}')


def banner(unit, questions, versions, found=None):
    unit_qs = [e for e in questions if e.get('unit') == unit]
    latest = max((e['series'] for e in unit_qs), default='none')
    indexed = papers_of(questions, unit)
    missing = [(s, p) for s, p in expected_papers(unit, versions) if (s, p) not in indexed]
    through = (versions or {}).get('expected_papers', {}).get('through', '?')
    series = sorted({s for s, _ in missing})
    text = (f'[registry snapshot {snapshot(versions)}] {unit}: latest indexed series {latest}; '
            f'{len(series)} expected series not fully indexed through {through} ({len(missing)} papers'
            f'{": " + ", ".join(series) if series else ""}; see --gaps)')
    if found is not None:
        parts = [p for e in found if e.get('unit') == unit for p in e['parts']]
        text += (f'; returned {len(parts)} parts: {sum(1 for p in parts if not p.get("ms"))} without MS, '
                 f'{sum(1 for p in parts if not p.get("er"))} without ER notes')
    return text


def print_gaps(unit, questions, versions, out=sys.stdout):
    listed = listed_gaps(versions)
    gaps = compute_gaps(unit, questions, versions)
    exp = (versions or {}).get('expected_papers', {})
    print(f'{unit} gaps (snapshot {snapshot(versions)}; expected papers through {exp.get("through", "?")}, rules in versions.json expected_papers)', file=out)
    labels = {'paper': 'expected papers not indexed', 'ms': 'indexed papers whose MS is not held',
              'ms-partial': 'MS held for only some questions', 'er': 'indexed papers whose examiner report is not held',
              'er-partial': 'examiner report held for only some questions', 'qp-text': 'QP held only as extracted text (Edexcel-Finder)',
              'qp-drive-only': 'QP only on Drive (no public copy located)', 'ms-drive-only': 'MS only on Drive (no public copy located)',
              'er-drive-only': 'ER only on Drive (no public copy located)'}
    for kind, label in labels.items():
        rows = [g for g in gaps if g['kind'] == kind]
        print(f'  {label}: {len(rows)}', file=out)
        for g in rows:
            reason = listed.get(gap_key(g))
            print(f'    {g["series"]}  {g["paper"]:<14} {"listed: " + reason if reason else "UNLISTED"}', file=out)
    print('  indexed papers (parts without MS / ER notes):', file=out)
    print(f'    {"series":<8} {"paper":<14} {"Qs":>3} {"parts":>5} {"noMS":>5} {"noER":>5}  docs', file=out)
    for (s, paper), row in sorted(papers_of(questions, unit).items()):
        docs = ' '.join(d.upper() if any(row['held'][d]) else '-' for d in DOCS)
        dup = '  (same paper as another variant)' if row['same_as'] else ''
        print(f'    {s:<8} {paper[:14]:<14} {row["questions"]:>3} {row["parts"]:>5} {row["no_ms"]:>5} {row["no_er"]:>5}  {docs}{dup}', file=out)
    return gaps


def completeness(questions, versions):
    """(unlisted computed gaps, stale listed gaps) over every registered unit."""
    listed = listed_gaps(versions)
    computed = {}
    for unit in known_units(questions):
        for g in compute_gaps(unit, questions, versions):
            computed[gap_key(g)] = g
    unlisted = [computed[k] for k in sorted(computed) if k not in listed]
    stale = [k for k in sorted(listed) if k not in computed]
    return unlisted, stale, computed


# ---------------------------------------------------------------- CLI

def _utf8():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding='utf-8', errors='replace')
        except (AttributeError, ValueError):
            pass


def main(argv=None):
    _utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('unit', nargs='?', help='unit code, e.g. WMA14, wst02, S2, 9708/3, 9708/4, 9708 (both)')
    ap.add_argument('--spec', help='spec item id, e.g. 4.1 or 8.1.1 (prefix match; WST01 6.1 and WFM02 7.2 are aliases)')
    ap.add_argument('--grep', help='case-insensitive text in ask / final form / MS / ER notes')
    ap.add_argument('--since', help='earliest series, YYYY-MM')
    ap.add_argument('--coverage', action='store_true')
    ap.add_argument('--demands', action='store_true', help='print JSON shaped for deck.json demands')
    ap.add_argument('--gaps', action='store_true', help='gaps of this unit, computed from versions.json and the index')
    ap.add_argument('--completeness', action='store_true', help='fail if a computed gap is not listed in versions.json gaps (or a listed one is filled)')
    ap.add_argument('--json', action='store_true', help='with --gaps or --completeness: machine-readable output')
    ap.add_argument('--all-variants', action='store_true', help='include variant papers that duplicate another variant (same_as)')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--check-file', metavar='PATH', help='validate a registry-additions/<unit>.questions.json file')
    a = ap.parse_args(argv)
    regs = registries()
    versions = load_versions()
    questions = [e for r in regs.values() for e in r['questions']]
    items = {u: c for r in regs.values() for u, c in r['items'].items()}
    if a.check:
        problems = check()
        print('\n'.join(problems) or f'ok: {len(questions)} entries')
        return 1 if problems else 0
    if a.check_file:
        problems, notes = check_file(a.check_file)
        for n in notes:
            print(f'note: {n}')
        print('\n'.join(problems) or f'ok: {a.check_file}')
        return 1 if problems else 0
    if a.completeness:
        unlisted, stale, computed = completeness(questions, versions)
        if a.json:
            print(json.dumps({'snapshot': snapshot(versions), 'computed': len(computed), 'unlisted': unlisted,
                              'stale': [dict(zip(('unit', 'kind', 'paper'), k)) for k in stale]}, ensure_ascii=False, indent=1))
        else:
            by_unit = Counter(k[0] for k in computed)
            print(f'snapshot {snapshot(versions)}: {len(computed)} computed gaps over {len(known_units(questions))} units '
                  f'({", ".join(f"{u} {n}" for u, n in sorted(by_unit.items()))})')
            for g in unlisted:
                print(f'UNLISTED  {g["unit"]} {g["kind"]} {g["series"]} {g["paper"]}')
            for k in stale:
                print(f'STALE     {k[0]} {k[1]} {k[2]} (listed in versions.json gaps but no longer a gap)')
            print('ok: every computed gap is listed with a reason' if not (unlisted or stale) else
                  f'{len(unlisted)} unlisted, {len(stale)} stale: update versions.json "gaps"')
        return 1 if (unlisted or stale) else 0
    if a.list or not a.unit:
        for board, reg in regs.items():
            by_unit = Counter(e['unit'] for e in reg['questions'] if not e.get('same_as'))
            latest = {}
            for e in reg['questions']:
                latest[e['unit']] = max(latest.get(e['unit'], ''), e['series'])
            print(f'{board}: ' + ', '.join(f'{u} {n} questions (latest {latest[u]})' for u, n in sorted(by_unit.items())))
        print(f'snapshot {snapshot(versions)}; duplicate-variant entries (same_as) not counted; gaps: --gaps / --completeness')
        return 0
    try:
        units = resolve_units(a.unit, questions, versions)
        spec = resolve_spec(a.spec, items.get(spec_unit(units[0]), {})) if a.spec else None
        if a.since and not SERIES.match(a.since):
            raise UnknownName('series (want YYYY-MM)', a.since, [])
    except UnknownName as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 2
    if a.gaps:
        if a.json:
            print(json.dumps([g for u in units for g in compute_gaps(u, questions, versions)], ensure_ascii=False, indent=1))
        else:
            for u in units:
                print(banner(u, questions, versions), file=sys.stderr)
                print_gaps(u, questions, versions)
        return 0
    if a.coverage:
        for u in units:
            print(banner(u, questions, versions), file=sys.stderr)
        for sid, title, n in coverage(questions, items, units, a.all_variants):
            print(f'{sid:>8}  {n:3d}  {title}')
        return 0
    found = select(questions, units, spec, a.grep, a.since, items, a.all_variants)
    for u in units:
        print(banner(u, questions, versions, found), file=sys.stderr)
    if a.demands:
        print(json.dumps(as_demands(found, snapshot(versions)), ensure_ascii=False, indent=1))
        return 0
    for e in found:
        codes = ' = '.join(e.get('papers', [e['paper']]))
        print(f'{codes} {e["series"]} Q{e["q"]} ({e["marks"]} marks)  [{e.get("sources", {}).get("qp", "")}]')
        catalogue = items.get(spec_unit(e), {})
        for p in e['parts']:
            print(f'  ({p["part"] or "-"}) {p["marks"]}m {",".join(canonical(s, catalogue) for s in p["spec"])} {p["command"]}: {p["ask"]}')
            for key in ('final_form', 'ms', 'er'):
                if p.get(key):
                    print(f'      {key}: {p[key]}')
    print(f'{len(found)} questions', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
