"""Deck-level checks for ccpt-6: exam lock, research trail, two-way coverage, card identity.

These checks keep the promises traceable (every card belongs to the locked
syllabus, every in-scope point has a card, every board point is accounted
for). They cannot prove that the syllabus was read correctly or that the mark
schemes were understood; that remains the author's review work.
"""
import re

GENRES = {
    'term': '术语', 'derivation': '推导', 'method': '方法', 'chain': '因果', 'map': '导图', 'diagram': '图解',
    'compare': '辨析', 'essay': '论述', 'pitfall': '易错', 'overview': '全景', 'formula': '公式', 'case': '案例',
}
THEMES = {'editorial', 'paper', 'lab', 'blueprint', 'manuscript'}
RESEARCH_TYPES = {'spec', 'qp', 'ms', 'er', 'exemplar', 'specimen', 'textbook', 'board', 'teacher', 'other'}
ITEM_CLASSES = {'core', 'prerequisite', 'excluded'}
SPEEDS = {2.0, 1.5}


class DeckError(ValueError):
    pass


def need(cond, message):
    if not cond:
        raise DeckError(message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def texts(value, nonempty=True):
    return isinstance(value, list) and (bool(value) or not nonempty) and all(text(v) for v in value)


def positive_int(value):
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def check_deck(data):
    deck = data.get('deck')
    need(isinstance(deck, dict), 'deck: give {name, deck_id, model_id, model_name, namespace}')
    need(text(deck.get('name')) and text(deck.get('model_name')) and text(deck.get('namespace')), 'deck: name, model_name and namespace must be text')
    need(positive_int(deck.get('deck_id')) and positive_int(deck.get('model_id')), 'deck: deck_id and model_id must be positive integers')
    style = data.setdefault('style', {})
    need(isinstance(style, dict), 'style must be an object')
    need(style.get('theme', 'editorial') in THEMES, f'style.theme must be one of {sorted(THEMES)}')
    speed = style.get('speed', 'auto')
    need(speed == 'auto' or (isinstance(speed, (int, float)) and float(speed) in SPEEDS),
         'style.speed: "auto" (default: 2× unless the card is genuinely dense), or 2.0 / 1.5 for the whole deck')
    if speed != 'auto' and float(speed) == 1.5:
        need(text(style.get('speed_reason')), 'style.speed 1.5 for a whole deck needs style.speed_reason')
    need(style.get('voice', 'xiaoxiao') in ('xiaoxiao', 'yunyang', 'zh-CN-XiaoxiaoNeural', 'zh-CN-YunyangNeural', 'yunxi', 'zh-CN-YunxiNeural'),
         'style.voice: xiaoxiao (default) or yunyang; one voice per deck (yunxi only for maintaining old cards)')
    lexicon = data.get('speech_lexicon', {})
    need(isinstance(lexicon, dict) and all(text(k) and isinstance(v, str) for k, v in lexicon.items()),
         'speech_lexicon maps written forms to how they should be read, e.g. {"λ": "lambda"}')


def check_exam(data):
    exam = data.get('exam')
    need(isinstance(exam, dict), 'exam: lock the exact exam before making exam cards (or set "academic": false for non-exam material)')
    for key in ('board', 'qualification', 'code', 'spec_version', 'spec_url'):
        need(text(exam.get(key)), f'exam.{key} must be text')
    need(texts(exam.get('units')), 'exam.units: list the unit or paper codes in scope, e.g. ["WST02"] or ["9708/4"]')
    need(texts(exam.get('evidence')), 'exam.evidence: list the concrete clues that identify this exam')
    identified = exam.get('identified_by')
    need(identified in ('paper-code', 'exclusive-content', 'user'), 'exam.identified_by: paper-code, exclusive-content or user')
    ruled_out = exam.get('ruled_out', [])
    need(isinstance(ruled_out, list), 'exam.ruled_out must be a list')
    if identified == 'exclusive-content':
        need(ruled_out and all(isinstance(r, dict) and text(r.get('candidate')) and text(r.get('why_not')) for r in ruled_out),
             'exam.ruled_out: name each near-miss exam and the evidence that excludes it')


def check_research(data):
    records = data.get('research')
    need(isinstance(records, list) and records, 'research: record the sources actually read')
    kinds = set()
    for i, r in enumerate(records):
        need(isinstance(r, dict) and r.get('type') in RESEARCH_TYPES, f'research[{i}].type must be one of {sorted(RESEARCH_TYPES)}')
        for key in ('ref', 'read', 'used_for'):
            need(text(r.get(key)), f'research[{i}].{key} must say what was read and how it changed the cards')
        kinds.add(r['type'])
    need('spec' in kinds, 'research: read the official specification/syllabus for the locked units')
    need('ms' in kinds, 'research: read mark schemes for this content to calibrate the required level')
    gaps = data.get('research_gaps', '')
    need(isinstance(gaps, str), 'research_gaps must be text')
    if not kinds & {'er', 'exemplar', 'specimen'}:
        need(gaps.strip(), 'research: read examiner reports or real/specimen answers, or state in research_gaps what could not be obtained')


def check_coverage(data, card_ids, card_covers):
    cov = data.get('coverage')
    need(isinstance(cov, dict), 'coverage: list the syllabus points in scope and how they are taught')
    need(text(cov.get('scope')), 'coverage.scope must name the syllabus boundary of this deck')
    status = cov.get('status')
    need(status in ('complete', 'partial'), 'coverage.status: complete or partial')
    remaining = cov.get('remaining', '')
    need(isinstance(remaining, str) and (bool(remaining.strip()) == (status == 'partial')),
         'coverage.remaining: required for partial, empty for complete')
    items = cov.get('items')
    need(isinstance(items, list) and items, 'coverage.items: decompose the syllabus scope into examinable points')
    by_id = {}
    for i, item in enumerate(items):
        need(isinstance(item, dict), f'coverage.items[{i}] must be an object')
        for key in ('id', 'spec', 'point'):
            need(text(item.get(key)), f'coverage.items[{i}].{key} must be text')
        need(item['id'] not in by_id, f'coverage item id {item["id"]} is duplicated')
        cls = item.get('class')
        need(cls in ITEM_CLASSES, f'coverage.items[{i}].class: core, prerequisite or excluded')
        if cls == 'core':
            need(text(item.get('level')), f'coverage.items[{i}].level: state what the mark schemes require (wording, method, diagram, evaluation)')
        else:
            need(text(item.get('reason')), f'coverage.items[{i}].reason: justify why this is a prerequisite or excluded')
        by_id[item['id']] = item
    taught = {}
    for cid, covers in card_covers.items():
        for item_id in covers:
            need(item_id in by_id, f'card {cid} covers unknown item {item_id}')
            need(by_id[item_id]['class'] != 'excluded', f'card {cid} teaches excluded item {item_id}')
            taught.setdefault(item_id, []).append(cid)
    # A point already taught well by an existing card counts when that card is named.
    missing = [k for k, v in by_id.items() if v['class'] != 'excluded' and k not in taught and not text(v.get('existing'))]
    if status == 'complete':
        need(not missing, f'coverage is complete but these points have no card: {missing}')
    board = data.get('board', [])
    need(isinstance(board, list), 'board must be a list of board points')
    for i, point in enumerate(board):
        need(isinstance(point, dict) and text(point.get('id')) and text(point.get('where')) and text(point.get('point')),
             f'board[{i}] needs id, where and point')
        mapped = point.get('items', [])
        need(isinstance(mapped, list) and all(m in by_id for m in mapped), f'board[{i}].items must reference coverage item ids')
        need(mapped or text(point.get('note')), f'board[{i}] maps to no syllabus point; explain in note (correction, digression or out of scope)')
    return {'items': len(by_id), 'taught': len(taught), 'missing': missing}


def check_cards(data):
    cards = data.get('cards')
    need(isinstance(cards, list) and cards, 'cards: at least one card')
    ids = set()
    for i, c in enumerate(cards):
        need(isinstance(c, dict), f'cards[{i}] must be an object')
        need(text(c.get('id')) and re.fullmatch(r'[A-Za-z0-9_.-]+', c['id']), f'cards[{i}].id: letters, digits, _ . - only')
        need(c['id'] not in ids, f'card id {c["id"]} is duplicated')
        ids.add(c['id'])
        need(c.get('genre') in GENRES, f'card {c["id"]}: genre must be one of {sorted(GENRES)}')
        need(text(c.get('title')), f'card {c["id"]}: title must be text')
        need(isinstance(c.get('blocks'), list) and c['blocks'], f'card {c["id"]}: blocks must be a non-empty list')
        if 'speed' in c:
            need(float(c['speed']) in SPEEDS, f'card {c["id"]}: speed is 2.0 or 1.5')
            if float(c['speed']) == 1.5:
                need(text(c.get('speed_reason')), f'card {c["id"]}: say why this card is complex enough for 1.5×')
        need(texts(c.get('sources', []), nonempty=False), f'card {c["id"]}: sources must be a list of text locations')
        need('voice' not in c, f'card {c["id"]}: voice is set once per deck in style.voice; switching voices mid-deck costs listening effort')
        check_genre(c)
    return ids


def blocks_of(card, kind):
    return [b for b in card['blocks'] if isinstance(b, dict) and b.get('type') == kind]


def check_genre(c):
    """Minimum teaching structure per card type (evidence: references/learning-science.md)."""
    cid = c['id']
    if c['genre'] == 'term':
        defs = blocks_of(c, 'definition')
        need(defs, f'card {cid}: a term card states the exam definition in a definition block')
        idea_units = len(defs[0].get('keywords', [])) >= 2 or blocks_of(c, 'unpack')
        need(idea_units, f'card {cid}: split the definition into idea units (≥2 keywords or an unpack block)')
        if not text(c.get('examples_waived')):
            ex = blocks_of(c, 'examples')
            yes = sum(len(b.get('yes', [])) for b in ex)
            no = [n for b in ex for n in b.get('no', [])]
            need(yes >= 1 and no, f'card {cid}: give at least one example and one non-example (or explain in examples_waived)')
            need(all(isinstance(n, dict) and text(n.get('why')) for n in no),
                 f'card {cid}: each non-example says which part of the definition it fails (why)')
    if c['genre'] == 'derivation':
        need(blocks_of(c, 'steps'), f'card {cid}: a derivation card works through steps')
        need(blocks_of(c, 'finish'), f'card {cid}: end a derivation with a finish block (exact form, accuracy, range, conclusion)')


def check(data):
    check_deck(data)
    ids = check_cards(data)
    summary = {'cards': len(ids)}
    if data.get('academic', True):
        check_exam(data)
        check_research(data)
        covers = {}
        for c in data['cards']:
            need(texts(c.get('covers')), f'card {c["id"]}: covers must list the coverage item ids it teaches')
            covers[c['id']] = c['covers']
        summary['coverage'] = check_coverage(data, ids, covers)
    return summary
