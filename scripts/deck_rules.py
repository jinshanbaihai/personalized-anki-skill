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
    'board': '板书',
}
THEMES = {'editorial', 'paper', 'lab', 'blueprint', 'manuscript'}
RESEARCH_TYPES = {'spec', 'qp', 'ms', 'er', 'exemplar', 'specimen', 'textbook', 'board', 'teacher', 'other'}
ITEM_CLASSES = {'core', 'prerequisite', 'adjacent', 'excluded'}
ITEM_KINDS = {'term', 'method', 'formula', 'diagram', 'chain', 'essay', 'command', 'fact'}
SPEEDS = {2.0, 1.5}
PAPER_FORMATS = {'mcq', 'structured', 'data-response', 'essay', 'practical', 'oral'}
FORMULA_BOOKLET = {'given', 'memorise', 'derive'}


class DeckError(ValueError):
    pass


# Deliverables leave the learner's machine: marked scripts are recorded as question + mark + scored or not,
# never as one identified person's script (SKILL.md step 1). Names cannot be detected; these patterns can.
SCRIPT = r'(?:答卷|卷面|试卷|卷子|本卷|模考|mock|script|paper)'
PRIVATE = [
    (re.compile(r'你的(?:卷面|答卷|试卷|卷子)|你(?:在|这)[^。；\n]{0,8}(?:丢|被扣|扣了|漏了)|你丢了?\s*\d+\s*分|你被扣'),
     'addresses the author of a marked script as 你'),
    (re.compile(r'\byour (?:script|exam paper|answer sheet|answer booklet|mock)\b|\byou (?:lost|dropped) (?:the |a |an )?(?:\d+ marks?|[BMA]\d)', re.I),
     'addresses the author of a marked script as "you"'),
    (re.compile(r'考生号|准考证号|中心号|candidate (?:no\.?|number)|cand\.\s*no\b|cent(?:re|er) (?:no\.?|number)|(?:centre|center|candidate)\s*[:：#]\s*\d{3,}', re.I),
     'a candidate or centre number'),
    (re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}'), 'an e-mail address'),
    # a total on a script: "总分 49/75", "卷面 49／75", "本卷得分 49 分（满分 75）", "Total: 49 out of 75"
    (re.compile(SCRIPT + r'[^。；\n]{0,8}?(?<![\d/])\d{1,3}\s*(?:/|／|out of)\s*\d{2,3}(?![\d/])|总分[^。；\n]{0,6}?(?<![\d/])\d{1,3}\s*(?:分|/|／)'
                r'|' + SCRIPT + r'[^。；\n]{0,6}?得分?\s*(?<![\d/])\d{1,3}\s*分\s*[（(]\s*满分|\b(?:total(?: score)?|scored)\s*[:：]?\s*(?<![\d/])\d{1,3}\s*(?:/|／|out of)\s*\d{2,3}\b'
                r'|(?<![\d/])\d{1,3}\s*[/／]\s*\d{2,3}(?![\d/])[^。\n]{0,6}?(?:丢\s*[MABC]?\s*\d|失分|扣\s*[MABC]?\s*\d|lost)|(?<![\d/])\d{1,3}\s*[/／]\s*\d{2,3}(?![\d/])[^。\n]{0,12}?(?:模考|卷面|答卷|本卷)', re.I),
     'a total score on a script'),
]


def walk_strings(value, path=''):
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for k, v in value.items():
            yield from walk_strings(v, f'{path}.{k}' if path else str(k))
    elif isinstance(value, list):
        for i, v in enumerate(value):
            yield from walk_strings(v, f'{path}[{i}]')


def check_privacy(data):
    """Personal framing, IDs, e-mails and script totals stop the build. A deck only for the learner themselves may set
    "personal": true; a single reviewed false positive is listed by path in privacy_reviewed instead."""
    if data.get('personal') is True:
        return
    reviewed = data.get('privacy_reviewed', [])
    need(texts(reviewed, nonempty=False), 'privacy_reviewed lists the paths (as printed by the error) of strings checked by hand and found not personal')
    for path, value in walk_strings(data):
        if path in reviewed or path.startswith('privacy_reviewed'):
            continue
        for pattern, what in PRIVATE:
            m = pattern.search(value)
            need(not m, f'{path}: "{m.group(0) if m else ""}" looks like {what}. Record a marked script neutrally — question, mark, scored or not '
                        '(e.g. "本卷批改记录：Q9(a) M1、A1 未得") — never "你", never a name, ID or total. If this string is not personal '
                        f'(e.g. a probability), add "{path}" to privacy_reviewed; a deck only for the learner themselves may set "personal": true')


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
    themes_by = style.get('theme_by_subdeck', {})
    need(isinstance(themes_by, dict) and all(text(k) and v in THEMES for k, v in themes_by.items()),
         f'style.theme_by_subdeck maps a subdeck name to one of {sorted(THEMES)} (e.g. statistics in lab, pure maths in paper)')
    speed = style.get('speed', 'auto')
    need(speed == 'auto' or (isinstance(speed, (int, float)) and float(speed) in SPEEDS),
         'style.speed: "auto" (default: 2× unless the card is genuinely dense), or 2.0 / 1.5 for the whole deck')
    if speed != 'auto' and float(speed) == 1.5:
        need(text(style.get('speed_reason')), 'style.speed 1.5 for a whole deck needs style.speed_reason')
    voices = ('xiaoxiao', 'yunyang', 'zh-CN-XiaoxiaoNeural', 'zh-CN-YunyangNeural')
    if style.get('legacy_voice') is True:  # Yunxi only where old cards are maintained in their original voice
        voices += ('yunxi', 'zh-CN-YunxiNeural')
    need(style.get('voice', 'xiaoxiao') in voices, 'style.voice: xiaoxiao (default) or yunyang (yunxi only with style.legacy_voice: true, for maintaining old cards)')
    by_sub = style.get('voice_by_subdeck', {})
    need(isinstance(by_sub, dict) and all(text(k) and v in voices for k, v in by_sub.items()),
         'style.voice_by_subdeck maps a subdeck name to xiaoxiao or yunyang (one voice per subdeck)')
    if 'speed_review' in style:
        need(text(style['speed_review']), 'style.speed_review: say why this deck is dense enough that over 30% of its cards are 1.5×')
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
    need(text(exam.get('session')), 'exam.session: the target exam series (e.g. "January 2027"); if unknown, give your assumption and set session_assumed: true')
    identified = exam.get('identified_by')
    need(identified in ('paper-code', 'exclusive-content', 'user'), 'exam.identified_by: paper-code, exclusive-content or user')
    ruled_out = exam.get('ruled_out', [])
    need(isinstance(ruled_out, list), 'exam.ruled_out must be a list')
    if identified == 'exclusive-content':
        need(ruled_out and all(isinstance(r, dict) and text(r.get('candidate')) and text(r.get('why_not')) for r in ruled_out),
             'exam.ruled_out: name each near-miss exam and the evidence that excludes it')
    papers = exam.get('papers')
    need(isinstance(papers, list) and papers and all(isinstance(p, dict) and text(p.get('code')) and p.get('format') in PAPER_FORMATS for p in papers),
         f'exam.papers: list each paper that examines this content as {{code, format}}, format one of {sorted(PAPER_FORMATS)} '
         '(e.g. 9708 externalities: [{"code": "9708/3", "format": "mcq"}, {"code": "9708/4", "format": "essay"}])')


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
    gaps = data.get('research_gaps', '')
    need(isinstance(gaps, str), 'research_gaps must be text')
    for i, r in enumerate(records):
        if 'via' in r:
            need(r['via'] in ('original', 'registry'), f'research[{i}].via: "original" (the document itself) or "registry" (the skill\'s registry summary; give the paper and series in ref)')
    if 'ms' not in kinds:
        # Without any mark scheme the required level is a guess: allowed only for a partial deck that says why.
        need((data.get('coverage') or {}).get('status') == 'partial' and gaps.strip(),
             'research: read mark schemes for this content (the original or, for registered exams, the registry summary with via: "registry"); '
             'if none exists anywhere, set coverage.status "partial" and explain in research_gaps (and put it in the first line of the delivery note)')
    if not kinds & {'er', 'exemplar', 'specimen'}:
        need(gaps.strip(), 'research: read examiner reports or real/specimen answers, or state in research_gaps what could not be obtained')
    # Every paper format that examines this content is calibrated separately (an MCQ asks for different mastery than an essay).
    read_papers = set()
    for r in records:
        value = r.get('paper', [])
        read_papers |= {value} if isinstance(value, str) else set(value) if isinstance(value, list) else set()
    for p in (data.get('exam') or {}).get('papers', []):
        named_in_gaps = re.search(r'(?<![A-Za-z0-9/])' + re.escape(p['code']) + r'(?![A-Za-z0-9/])', gaps)
        need(p['code'] in read_papers or named_in_gaps,
             f'research: no source tagged paper "{p["code"]}" ({p["format"]}); read its mark scheme or examiner report, or name the gap in research_gaps')
    return research_warnings(data, records, gaps)


SCRIPT_PAGES = re.compile(r'\bpp?\.\s*\d|第\s*\d+\s*(?:[–—-]\s*\d+\s*)?页|\d+\s*[–—-]\s*\d+\s*页|script\s*pp?\.?\s*\d', re.I)
# "it is only an image" is not a reason the scripts could not be read
NOT_A_GAP = re.compile(r'no ocr|without ocr|无\s*OCR|没有\s*OCR|image[- ]only|only (?:as )?images?|(?:只有|只是|是|仅有)(?:扫描)?图片|没有文字层', re.I)


def research_warnings(data, records, gaps):
    """Advisory: essay and data-response papers are calibrated against real scripts read page by page."""
    out = []
    formats = {p.get('format') for p in (data.get('exam') or {}).get('papers', []) if isinstance(p, dict)}
    if formats & {'essay', 'data-response'}:
        read_scripts = any(r.get('type') in ('exemplar', 'specimen') and SCRIPT_PAGES.search(r.get('read', '')) for r in records)
        explained = re.search(r'exemplar|ECR|example candidate|范文|答卷|样卷', gaps, re.I) and not NOT_A_GAP.search(gaps)
        if not read_scripts and not explained:
            out.append('essay／数据题：没有读真实答卷的记录（exemplar／specimen 的 read 要写明读了哪几页，例如 "script pp.15–21 read"）；'
                       '扫描图要用 pdftoppm 渲染后看图读，“是图片／无 OCR”不算取不到；原件确实拿不到时写进 research_gaps')
    return out


def check_coverage(data, card_ids, card_covers, planning=False, preview=False):
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
        need(cls in ITEM_CLASSES, f'coverage.items[{i}].class: core, prerequisite, adjacent (same syllabus section, later batch) or excluded')
        if cls == 'core':
            need(text(item.get('level')), f'coverage.items[{i}].level: state what the mark schemes require (wording, method, diagram, evaluation)')
            need(item.get('kind') in ITEM_KINDS, f'coverage.items[{i}].kind: one of {sorted(ITEM_KINDS)} (what kind of mastery the point needs)')
            evidence = item.get('evidence', [])
            distinct = {re.sub(r'\W+', '', e).lower() for e in evidence if text(e)} if isinstance(evidence, list) else set()
            need(len(distinct) >= 2 or text(item.get('evidence_gap')),
                 f'coverage.items[{i}].evidence: cite at least two past-paper mark schemes or examiner reports from different series, or explain evidence_gap')
        else:
            need(text(item.get('reason')), f'coverage.items[{i}].reason: justify why this is a prerequisite or excluded')
        by_id[item['id']] = item
    taught = {}
    genres = {c['id']: c['genre'] for c in data['cards']}
    for cid, covers in card_covers.items():
        for item_id in covers:
            need(item_id in by_id, f'card {cid} covers unknown item {item_id}')
            need(by_id[item_id]['class'] != 'excluded', f'card {cid} teaches excluded item {item_id}')
            need(by_id[item_id]['class'] != 'adjacent', f'card {cid} teaches {item_id}, marked adjacent (later batch); reclassify it as core if this deck teaches it')
            taught.setdefault(item_id, []).append(cid)
    # A point already taught well by an existing card counts when that card is named.
    missing = [k for k, v in by_id.items() if v['class'] in ('core', 'prerequisite') and k not in taught and not text(v.get('existing'))]
    structure = {c['id']: {b.get('type') for b in c['blocks'] if isinstance(b, dict)} for c in data['cards']}
    for k, v in by_id.items():
        if planning or k not in taught or text(v.get('existing')):
            continue
        # A board card counts when the learner's own board shows the definition or the arrows (references/card-genres.md);
        # when it does not, the deck adds a term or chain card after it.
        if v.get('kind') in ('term', 'command'):
            need(any(genres[c] in ('term', 'board') for c in taught[k]),
                 f'coverage item {k} is a {v["kind"]}: give it its own term card (or a board card whose board shows it), not only a mention inside another card')
        if v.get('kind') == 'chain':
            need(any(structure[c] & {'chain', 'map', 'board'} for c in taught[k]),
                 f'coverage item {k} is a causal chain: teach it with a chain or map block (arrows), or a board card showing the board\'s own arrows, not paragraphs')
    if status == 'complete' and not planning:
        need(not missing, f'coverage is complete but these points have no card: {missing}')
    board = data.get('board', [])
    if not planning and any(True for _ in board_crops(data)):
        # Board first: where the board shows a point, the card shows the board; typed cards only add what it lacks.
        on_board = {}
        for point in board if isinstance(board, list) else []:
            if isinstance(point, dict) and 'lost' not in point and not text(point.get('not_shown')):
                for item in point.get('items', []) if isinstance(point.get('items'), list) else []:
                    on_board.setdefault(item, []).append(point.get('id'))
        for item, points in on_board.items():
            if item in taught:
                need(any(genres[c] == 'board' for c in taught[item]),
                     f'coverage item {item} is on the board ({", ".join(points)}) but only typed cards teach it: show it with a board card '
                     '(crop the board points that carry it); a typed card may follow only for what the board lacks (board_gap)')
    need(isinstance(board, list), 'board must be a list of board points')
    for i, point in enumerate(board):
        need(isinstance(point, dict) and text(point.get('id')) and text(point.get('where')) and text(point.get('point')),
             f'board[{i}] needs id, where and point')
        mapped = point.get('items', [])
        need(isinstance(mapped, list) and all(m in by_id for m in mapped), f'board[{i}].items must reference coverage item ids')
        need(mapped or text(point.get('note')), f'board[{i}] maps to no syllabus point; explain in note (correction, digression or out of scope)')
        need(point.get('legibility', 'ok') in ('ok', 'low'), f'board[{i}].legibility: ok or low')
        score = point.get('score')
        need(score is None or (isinstance(score, int) and not isinstance(score, bool) and score >= 0), f'board[{i}].score is a whole number of marks scored')
        if (PER_MARK.fullmatch(point['id']) and score is None) or score == 0:
            need('lost' in point, f'board[{i}] {point["id"]} is a per-mark record from a marked script: add "lost" (e.g. "A1") for a 0, and the card that fixes it')
        if 'lost' in point:  # a mark the learner lost on their own script (e.g. Q01A2 = 0)
            need(text(point['lost']), f'board[{i}].lost names the lost mark, e.g. "A1"')
            linked = point.get('cards', [])
            need(isinstance(linked, list) and (planning or all(c in set(genres) for c in linked)), f'board[{i}].cards must list card ids')
            need(planning or linked or text(point.get('not_carded')), f'board[{i}] records a lost mark: name the card that fixes it (M0 → method/derivation card, A0 → pitfall and finish item, B0 → term card) or explain not_carded')
        if point.get('legibility') == 'low':
            need(text(point.get('confirmed_by')), f'board[{i}] is hard to read: say which source confirmed the content (confirmed_by); never fill in guessed words')
        if 'issue' in point:  # where the board itself gets in the way of understanding what the exam needs
            need(point['issue'] in BOARD_ISSUES, f'board[{i}].issue says what is wrong with the board here: one of {sorted(BOARD_ISSUES)}')
            need(text(point.get('issue_note')), f'board[{i}].issue_note says in one line what the problem is (e.g. "the shifted supply is labelled MPC + subsidy")')
    check_board_shown(data, board, planning)
    need(board or text(data.get('board_waived')), 'board: list the board points (B01…), or say in board_waived why this deck has no board (e.g. made from a syllabus section only)')
    undemanded = check_demands(data, by_id, set(genres), planning)
    adjacent = [k for k, v in by_id.items() if v['class'] == 'adjacent']
    # The omission tests are run on finished cards, so a plan is not asked for them yet.
    backcheck, coldread = (None, None) if planning else check_trail(cov, status, set(genres), preview)
    return {'items': len(by_id), 'taught': len(taught), 'missing': missing, 'undemanded': undemanded, 'adjacent': adjacent,
            'backcheck': backcheck, 'coldread': coldread}


def check_trail(cov, status, card_ids, preview=False):
    """Omission tests leave a record: past questions answered only from the cards, and the cold-read keyword test."""
    backcheck = cov.get('backcheck', [])
    need(isinstance(backcheck, list), 'coverage.backcheck must be a list')
    for i, b in enumerate(backcheck):
        w = f'coverage.backcheck[{i}]'
        need(isinstance(b, dict) and text(b.get('paper')) and text(b.get('series')) and text(str(b.get('q', ''))),
             f'{w}: give paper, series and q of the past question answered using only the cards')
        need(b.get('result') in ('pass', 'gap'), f'{w}.result: pass (every mark supported by a card) or gap')
        fixed = b.get('fixed_by', [])
        need(isinstance(fixed, list) and all(c in card_ids for c in fixed), f'{w}.fixed_by must list card ids')
        if b['result'] == 'gap':
            need(fixed, f'{w}: a gap names the cards added or changed to close it (fixed_by)')
    if status == 'complete' and not preview:
        need(len({b['series'] for b in backcheck}) >= 2,
             'coverage.backcheck: a complete deck records at least two past questions from different series answered using only the cards '
             '(paper, series, q, result pass/gap, fixed_by); see references/review-and-delivery.md §一')
    coldread = cov.get('coldread', [])
    need(isinstance(coldread, list), 'coverage.coldread must be a list')
    for i, c in enumerate(coldread):
        w = f'coverage.coldread[{i}]'
        need(isinstance(c, dict) and c.get('card') in card_ids, f'{w}.card must be a card id')
        missing = c.get('missing', [])
        need(isinstance(missing, list) and all(text(m) for m in missing), f'{w}.missing lists the keywords that could not be recalled from the card')
        fixed = c.get('fixed_by', [])
        need(isinstance(fixed, list) and all(f in card_ids for f in fixed), f'{w}.fixed_by must list card ids')
        need(not missing or fixed, f'{w}: missing keywords need the card that now carries them (fixed_by)')
    return ({'records': len(backcheck), 'gaps': sum(b['result'] == 'gap' for b in backcheck), 'series': sorted({b['series'] for b in backcheck})},
            {'records': len(coldread), 'missing': sum(len(c.get('missing', [])) for c in coldread)})


# Kept in step with blocks.BOARD_NEEDS (the annotation's "need"); deck_rules does not import the renderer.
BOARD_ISSUES = ('slip', 'illegible', 'skipped', 'ambiguous', 'overstated', 'shorthand')


def board_crops(data):
    for c in data.get('cards', []):
        for b in c.get('blocks', []) if isinstance(c, dict) else []:
            if isinstance(b, dict) and b.get('type') == 'board':
                yield c, b, [x for x in b.get('crops', []) if isinstance(x, dict)]


def check_board_shown(data, board, planning=False):
    """Board mode: the learner read the whole board once, so every board point that teaches something appears on a board card
    (a crop lists it in "points"), or says in not_shown why it does not (an aside, a corrected slip, a mark record)."""
    if planning:
        return
    ids = {p.get('id') for p in board if isinstance(p, dict)}
    # A board point that is wrong, illegible, skips a step, reads two ways, overstates or uses unlabelled shorthand is
    # exactly where the learner may misread the board: the crop that shows it carries an annotation beside it.
    troubled = {p['id']: p.get('issue', 'illegible') for p in board if isinstance(p, dict) and p.get('id')
                and ('issue' in p or p.get('legibility') == 'low')}
    shown = set()
    any_board = False
    for card, block, crops in board_crops(data):
        any_board = True
        for j, crop in enumerate(crops):
            points = crop.get('points', [])
            need(isinstance(points, list) and all(x in ids for x in points),
                 f'card {card["id"]}: crops[{j}].points must list board point ids (B01…) shown in that crop')
            shown |= set(points)
            hard = [x for x in points if x in troubled]
            if hard and not isinstance(crop.get('annotate'), dict):
                need(False, f'card {card["id"]}: crops[{j}] shows board point {", ".join(f"{x} ({troubled[x]})" for x in hard)}, '
                            'where the board itself may be misread: add "annotate", a small mind map beside the crop that says what the board '
                            'means here, limited to what the exam needs (references/card-genres.md, 板书卡)')
    if not any_board:
        return
    for i, point in enumerate(board):
        if 'lost' in point or point.get('id') in shown:
            continue
        need(text(point.get('not_shown')),
             f'board[{i}] {point.get("id")} is on the board but on no board card: add it to the "points" of the crop that shows it, '
             'or say in not_shown why it is left out (an aside, a corrected slip, outside the exam)')


PER_MARK = re.compile(r'Q\d+(?:[a-z]|\([a-z]+\)|\([ivx]+\))*\s*[BMAC]\d*\*?')


def check_demands(data, by_id, card_ids, planning=False):
    """The past-paper demand inventory: every way the locked papers have asked about this content."""
    demands = data.get('demands')
    need(isinstance(demands, list) and demands,
         'demands: list the past-paper questions that examine this content ({id, series, q, ask, points, cards}); see references/coverage-ledger.md')
    need(text((data.get('coverage') or {}).get('saturation')),
         'coverage.saturation: say which series were read for demands and why reading stopped (e.g. "the last 3 series added no new kind of question")')
    seen, used = set(), set()
    for i, d in enumerate(demands):
        need(isinstance(d, dict), f'demands[{i}] must be an object')
        for key in ('id', 'series', 'q', 'ask'):
            need(text(d.get(key)), f'demands[{i}].{key} must be text')
        need(d['id'] not in seen, f'demand id {d["id"]} is duplicated')
        seen.add(d['id'])
        points = d.get('points')
        need(texts(points) and all(p in by_id for p in points), f'demands[{i}].points must list coverage item ids')
        cards = d.get('cards', [])
        need(isinstance(cards, list) and (planning or all(c in card_ids for c in cards)), f'demands[{i}].cards must list card ids')
        need(planning or cards or text(d.get('not_carded')), f'demands[{i}] has no card: name the card that prepares it, or explain not_carded')
        used |= set(points)
    return [k for k, v in by_id.items() if v['class'] == 'core' and k not in used]


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
        need('voice' not in c, f'card {c["id"]}: voices are chosen per deck (style.voice) or per subdeck (style.voice_by_subdeck), not per card')
        need(c.get('formula_booklet', 'given') in FORMULA_BOOKLET,
             f'card {c["id"]}: formula_booklet is given (printed in the exam formula booklet), memorise or derive')
        need(c.get('theme', 'editorial') in THEMES, f'card {c["id"]}: theme must be one of {sorted(THEMES)}')
        check_genre(c, data.get('academic', True))
    if any(True for _ in board_crops(data)):
        for c in cards:
            if c.get('genre') != 'board':
                need(text(c.get('board_gap')),
                     f'card {c["id"]}: this deck shows the board, so a typed card exists only for what the board does not cover: '
                     'say in board_gap what is missing from the board (e.g. "板书没有 MS 认可的定义原句"); content the board shows goes on a board card')
    genres = {c['id']: c['genre'] for c in cards}
    known = data.get('terms_known', [])
    need(isinstance(known, list), 'terms_known must be a list')
    for i, t in enumerate(known):
        if isinstance(t, dict):
            need(text(t.get('term')), f'terms_known[{i}].term must be text')
            taught = t.get('taught_in', [])
            need(isinstance(taught, list) and taught and all(x in ids for x in taught),
                 f'terms_known[{i}] ({t.get("term")}): taught_in lists the cards of this deck that teach it; a word taught elsewhere gets a gloss "word（中文）" on the card')
        else:
            need(text(t), f'terms_known[{i}] must be text or {{term, taught_in}}')
    need(texts(data.get('ignore_words', []), nonempty=False), 'ignore_words lists function words the term ledger should skip')
    for c in cards:
        links = c.get('links', [])
        need(isinstance(links, list) and all(l in ids for l in links), f'card {c["id"]}: links must list card ids')
        if c['genre'] == 'essay':
            arrows = blocks_of(c, 'chain') or blocks_of(c, 'map') or any(genres[l] in ('chain', 'map', 'overview') for l in links)
            need(arrows, f'card {c["id"]}: an essay card shows its argument as arrows: add a chain or map block, or link the chain/map cards in "links"')
    return ids


def blocks_of(card, kind):
    return [b for b in card['blocks'] if isinstance(b, dict) and b.get('type') == kind]


def check_genre(c, academic=True):
    """Minimum teaching structure per card type (evidence: references/learning-science.md)."""
    cid = c['id']
    if c['genre'] == 'term':
        defs = blocks_of(c, 'definition')
        need(defs, f'card {cid}: a term card states the exam definition in a definition block')
        need(not academic or text(defs[0].get('source')), f'card {cid}: say where the exam definition comes from (mark scheme, examiner report, syllabus or an endorsed textbook glossary) in definition.source')
        if academic:
            unpack = blocks_of(c, 'unpack')
            need(unpack and len(unpack[0].get('items', [])) >= 2,
                 f'card {cid}: explain why each key part of the definition is there (an unpack block with at least 2 items; highlighting keywords is not an explanation)')
            need(blocks_of(c, 'exam') or text(c.get('exam_waived')), f'card {cid}: say how the term is examined (an exam block: command word, marks, accepted wording) or explain exam_waived')
        else:
            idea_units = len(defs[0].get('keywords', [])) >= 2 or blocks_of(c, 'unpack')
            need(idea_units, f'card {cid}: split the definition into idea units (≥2 keywords or an unpack block)')
        if not text(c.get('examples_waived')):
            ex = blocks_of(c, 'examples')
            yes = sum(len(b.get('yes', [])) for b in ex)
            no = [n for b in ex for n in b.get('no', [])]
            need(yes >= 1 and no, f'card {cid}: give at least one example and one non-example (or explain in examples_waived)')
            need(all(isinstance(n, dict) and text(n.get('why')) for n in no),
                 f'card {cid}: each non-example says which part of the definition it fails (why)')
    if c['genre'] == 'chain':
        need(blocks_of(c, 'chain'), f'card {cid}: a causal card draws its chain with a chain block (arrows with relation words)')
    if c['genre'] in ('map', 'overview'):
        need(blocks_of(c, 'map'), f'card {cid}: a {c["genre"]} card needs a map block')
    if c['genre'] == 'essay':
        need(blocks_of(c, 'sections'), f'card {cid}: an essay card gives the paragraph skeleton in a sections block')
    if c['genre'] == 'derivation':
        need(blocks_of(c, 'steps'), f'card {cid}: a derivation card works through steps')
        need(blocks_of(c, 'finish'), f'card {cid}: end a derivation with a finish block (exact form, accuracy, range, conclusion)')
    if c['genre'] == 'method':
        need(blocks_of(c, 'steps'), f'card {cid}: a method card works through its steps (a steps block), each with why')
    if c['genre'] == 'formula':
        need(blocks_of(c, 'unpack') or blocks_of(c, 'steps'), f'card {cid}: a formula card explains each part (unpack) or derives it (steps)')
        need(not academic or c.get('formula_booklet') in FORMULA_BOOKLET,
             f'card {cid}: say whether the exam formula booklet gives this formula (formula_booklet: given, memorise or derive)')
    if c['genre'] == 'case':
        need(blocks_of(c, 'chain') or blocks_of(c, 'map') or blocks_of(c, 'sections'),
             f'card {cid}: a case card ties the real case to the theory with a chain, map or sections block')
    if c['genre'] == 'board':
        need(blocks_of(c, 'board'), f'card {cid}: a board card shows the learner\'s own board: give it a board block (src + crops)')
    for b in blocks_of(c, 'board'):
        need(text(b.get('src')), f'card {cid}: a board block names its image in "src" (relative to deck.json)')
        crops = b.get('crops')
        need(isinstance(crops, list) and crops and all(isinstance(x, dict) for x in crops),
             f'card {cid}: a board block lists its crops (the parts of the board this knowledge point needs)')


def check_plan(data):
    """Before cards exist: privacy, exam lock, research trail and the coverage/demand plan (cards may be empty)."""
    check_privacy(data)
    check_exam(data)
    warnings = check_research(data)
    cards = [c for c in data.get('cards', []) if isinstance(c, dict) and text(c.get('id'))]
    plan = dict(data, cards=[{'id': c['id'], 'genre': c.get('genre', 'term'), 'blocks': c.get('blocks', [])} for c in cards])
    covers = {c['id']: c.get('covers', []) for c in cards}
    return {'cards': len(cards), 'coverage': check_coverage(plan, set(covers), covers, planning=True), 'warnings': warnings}


def check(data, preview=False):
    check_privacy(data)
    if data.get('academic', True) is False:
        need(not data.get('exam') and not any(c.get('covers') for c in data.get('cards', []) if isinstance(c, dict)),
             'academic: false is only for non-exam material; a deck with an exam target needs research, coverage and demands')
    check_deck(data)
    ids = check_cards(data)
    summary = {'cards': len(ids)}
    if data.get('academic', True):
        check_exam(data)
        summary['warnings'] = check_research(data)
        covers = {}
        for c in data['cards']:
            need(texts(c.get('covers')), f'card {c["id"]}: covers must list the coverage item ids it teaches')
            covers[c['id']] = c['covers']
        summary['coverage'] = check_coverage(data, ids, covers, preview=preview)
        if preview and (data.get('coverage') or {}).get('status') == 'complete' and summary['coverage']['backcheck']['records'] < 2:
            summary['warnings'].append('预览：complete 卡组打包前要有两道不同考季的真题回查（coverage.backcheck），见 review-and-delivery.md §一')
    return summary
