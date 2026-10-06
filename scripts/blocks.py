"""Content blocks for ccpt-6 exam cards: inline math, block HTML and narration parts.

Authors write plain text with limited inline HTML and LaTeX math:
  $...$ inline, $$...$$ display; a spoken form may follow in 〔...〕, e.g.
  "P(M=4) = $\\frac{9}{245}$〔245 分之 9〕".
A block that contains math either gives every formula a spoken form or sets
its own "speech". Narration never reads LaTeX source aloud.
"""
import html
import re
from latex2mathml.converter import convert as latex_to_mathml

from html_integrity import validate_markup, check_svg

INLINE_TAGS = {'b', 'strong', 'em', 'i', 'u', 'sub', 'sup', 'br', 'span', 'code', 'mark', 'small', 'abbr', 's'}
MATH = re.compile(r'(?<!\\)(\$\$(.+?)\$\$|\$(.+?)\$)(?:〔(.*?)〕)?', re.S)
PASSIVE_BLOCKERS = re.compile(r'<(?:script|iframe|audio|video|button|object|embed|form|input|link|style)\b|\son\w+\s*=|(?:src|href)\s*=\s*["\']?(?:https?:|file:|javascript:|data:)', re.I)


class BlockError(ValueError):
    pass


def fail(where, message):
    raise BlockError(f'{where}: {message}')


def passive(markup, where):
    """Reject active content; teaching content must remain inert and offline."""
    if PASSIVE_BLOCKERS.search(markup):
        fail(where, 'only passive local content is allowed (no script, media, form, inline event or external link)')
    try:
        validate_markup(markup)
    except AssertionError as error:
        fail(where, str(error))
    for svg in re.findall(r'<svg\b[\s\S]*?</svg>', markup):
        try:
            check_svg(svg)
        except Exception as error:  # noqa: BLE001 - surface the SVG problem to the author
            fail(where, f'invalid SVG: {error}')
    return markup


class Inline:
    """Rendered inline text with its spoken counterpart."""
    __slots__ = ('html', 'speech', 'unspoken')

    def __init__(self, html_text, speech, unspoken):
        self.html, self.speech, self.unspoken = html_text, speech, unspoken

    def __bool__(self):
        return bool(self.html.strip())


def strip_tags(markup):
    text = re.sub(r'<br\s*/?>', '，', markup)
    text = re.sub(r'<[^>]+>', '', text)
    return re.sub(r'\s+', ' ', html.unescape(text)).strip()


def inline(text, where, *, allow_block_html=False):
    """Convert author text to HTML (with MathML) and a speech string."""
    if text is None:
        return Inline('', '', 0)
    if not isinstance(text, str):
        fail(where, 'expected text')
    out_html, out_speech, unspoken, pos = [], [], 0, 0
    for match in MATH.finditer(text):
        before = text[pos:match.start()]
        out_html.append(before)
        out_speech.append(before)
        display = match.group(2) is not None
        source = (match.group(2) if display else match.group(3)).strip()
        try:
            mathml = latex_to_mathml(source, display='block' if display else 'inline')
        except Exception as error:  # noqa: BLE001
            fail(where, f'LaTeX could not be converted: {source!r} ({error})')
        out_html.append(f'<span class="math{" math-display" if display else ""}">{mathml}</span>')
        spoken = match.group(4)
        if spoken is None or not spoken.strip():
            unspoken += 1
            out_speech.append('⟦公式⟧')
        else:
            out_speech.append(spoken.strip())
        pos = match.end()
    out_html.append(text[pos:])
    out_speech.append(text[pos:])
    markup = ''.join(out_html).replace('\\$', '$')
    if not allow_block_html:
        for tag in re.findall(r'</?\s*([a-zA-Z][\w-]*)', re.sub(r'<math\b[\s\S]*?</math>', '', markup)):
            if tag.lower() not in INLINE_TAGS:
                fail(where, f'<{tag}> is not inline text markup; use a block type or an "html" block')
    passive(markup, where)
    return Inline(markup, strip_tags(''.join(out_speech).replace('\\$', '$')), unspoken)


def esc(value):
    return html.escape(str(value), quote=True)


class Part:
    """One narration segment and the visible element it belongs to."""
    __slots__ = ('target', 'text', 'unspoken')

    def __init__(self, target, text, unspoken=0):
        self.target, self.text, self.unspoken = target, text, unspoken


def joined(*pieces):
    out = ''
    for piece in pieces:
        piece = (piece or '').strip()
        if not piece:
            continue
        if out and not re.search(r'[。！？；.!?;:：，,]$', out):
            out += '。'
        out += (' ' if out and out[-1] in '.!?;:,' else '') + piece
    return out


def need_list(block, key, where, *, nonempty=True):
    value = block.get(key)
    if not isinstance(value, list) or (nonempty and not value):
        fail(where, f'"{key}" must be a non-empty list')
    return value


def need_text(block, key, where):
    value = block.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(where, f'"{key}" must be non-empty text')
    return value


def highlight_keywords(markup, keywords, where):
    """Mark the exact wording a mark scheme rewards; each keyword must appear."""
    for word in keywords:
        if not isinstance(word, str) or not word.strip():
            fail(where, 'keywords must be non-empty strings')
        escaped = html.escape(word, quote=False)
        if escaped not in markup:
            fail(where, f'keyword {word!r} does not appear verbatim in the definition text')
        markup = markup.replace(escaped, f'<mark class="kw">{escaped}</mark>')
    return markup


# ---------------------------------------------------------------- renderers
# Each renderer returns (html, [Part]); `bid` is the block id used for cues.

def r_lead(b, bid, where):
    t = inline(need_text(b, 'text', where), where)
    return f'<p class="lead">{t.html}</p>', [Part(bid, t.speech, t.unspoken)]


def r_note(b, bid, where):
    t = inline(need_text(b, 'text', where), where)
    label = inline(b.get('label'), where)
    head = f'<h3 class="blk-label">{label.html}</h3>' if label else ''
    tone = b.get('tone', 'plain')
    if tone not in ('plain', 'key', 'aside', 'warn'):
        fail(where, 'tone must be plain, key, aside or warn')
    return (f'<div class="note tone-{tone}">{head}<p>{t.html}</p></div>',
            [Part(bid, joined(label.speech, t.speech), t.unspoken + label.unspoken)])


def r_definition(b, bid, where):
    term = inline(need_text(b, 'term', where), where)
    text = inline(need_text(b, 'text', where), where)
    keywords = b.get('keywords', [])
    if not isinstance(keywords, list):
        fail(where, '"keywords" must be a list')
    body = highlight_keywords(text.html, keywords, where) if keywords else text.html
    zh = inline(b.get('zh'), where)
    gloss = inline(b.get('gloss'), where)
    source = inline(b.get('source'), where)
    label = esc(b.get('label', 'Definition'))
    out = (f'<div class="def-head"><span class="def-label">{label}</span>'
           f'<h2 class="def-term">{term.html}</h2>' + (f'<span class="def-zh">{zh.html}</span>' if zh else '') + '</div>'
           f'<p class="def-text">{body}</p>')
    if gloss:
        out += f'<p class="def-gloss">{gloss.html}</p>'
    extra_speech, extra_unspoken = [], 0
    lists = []
    for key, title, cls in (('accept', '也给分的说法', 'def-accept'), ('reject', '不给分的说法', 'def-reject')):
        values = b.get(key, [])
        if not isinstance(values, list):
            fail(where, f'"{key}" must be a list')
        if values:
            rendered = [inline(v, f'{where}.{key}') for v in values]
            lists.append(f'<div class="{cls}"><h4>{title}</h4><ul>' + ''.join(f'<li>{r.html}</li>' for r in rendered) + '</ul></div>')
            extra_speech.append(title + '：' + '；'.join(r.speech for r in rendered))
            extra_unspoken += sum(r.unspoken for r in rendered)
    if lists:
        out += f'<div class="def-lists">{"".join(lists)}</div>'
    if source:
        out += f'<p class="def-src">{source.html}</p>'
    speech = joined(term.speech + ('，' + zh.speech if zh else ''), text.speech, gloss.speech, *extra_speech)
    return out, [Part(bid, speech, term.unspoken + text.unspoken + gloss.unspoken + extra_unspoken)]


def r_unpack(b, bid, where):
    items = need_list(b, 'items', where)
    label = inline(b.get('label', '逐词拆解'), where)
    rows, parts = [], []
    for i, item in enumerate(items):
        w = f'{where}.items[{i}]'
        key = inline(need_text(item, 'key', w), w)
        exp = inline(need_text(item, 'explain', w), w)
        nid = f'{bid}-{i}'
        rows.append(f'<div class="u-row" data-node="{nid}"><dt>{key.html}</dt><dd>{exp.html}</dd></div>')
        parts.append(Part(nid, joined(key.speech, exp.speech), key.unspoken + exp.unspoken))
    parts[0].text = joined(label.speech, parts[0].text)
    return f'<h3 class="blk-label">{label.html}</h3><dl class="unpack">{"".join(rows)}</dl>', parts


def r_examples(b, bid, where):
    cols, parts = [], []
    for side, title, mark in (('yes', b.get('yes_label', '是'), '✓'), ('no', b.get('no_label', '不是'), '✗')):
        items = b.get(side, [])
        if not isinstance(items, list):
            fail(where, f'"{side}" must be a list')
        if not items:
            continue
        lis = []
        for i, item in enumerate(items):
            w = f'{where}.{side}[{i}]'
            item = item if isinstance(item, dict) else {'text': item}
            t = inline(need_text(item, 'text', w), w)
            why = inline(item.get('why'), w)
            nid = f'{bid}-{side}{i}'
            lis.append(f'<li data-node="{nid}"><span class="ex-text">{t.html}</span>' + (f'<span class="ex-why">{why.html}</span>' if why else '') + '</li>')
            lead = (title + '的例子：') if i == 0 else ''
            parts.append(Part(nid, joined(lead + t.speech, why.speech), t.unspoken + why.unspoken))
        cols.append(f'<div class="ex-col ex-{side}"><h4><span class="ex-mark">{mark}</span>{esc(title)}</h4><ul>{"".join(lis)}</ul></div>')
    if not cols:
        fail(where, 'give at least one example or non-example')
    label = inline(b.get('label', '例子与反例'), where)
    return f'<h3 class="blk-label">{label.html}</h3><div class="examples">{"".join(cols)}</div>', parts


def r_table(b, bid, where):
    head = need_list(b, 'head', where)
    rows = need_list(b, 'rows', where)
    hcells = [inline(h, f'{where}.head') for h in head]
    out = '<div class="tbl-wrap"><table class="tbl"><thead><tr>' + ''.join(f'<th>{h.html}</th>' for h in hcells) + '</tr></thead><tbody>'
    parts = []
    for i, row in enumerate(rows):
        w = f'{where}.rows[{i}]'
        if not isinstance(row, list) or len(row) != len(head):
            fail(w, 'each row needs one cell per header')
        cells = [inline(c, w) for c in row]
        nid = f'{bid}-r{i}'
        out += f'<tr data-node="{nid}">' + ''.join(f'<td>{c.html}</td>' for c in cells) + '</tr>'
        spoken = '；'.join(f'{h.speech}：{c.speech}' for h, c in zip(hcells[1:], cells[1:]))
        parts.append(Part(nid, joined(cells[0].speech, spoken), sum(c.unspoken for c in cells)))
    out += '</tbody></table></div>'
    caption = inline(b.get('caption'), where)
    label = inline(b.get('label'), where)
    if caption:
        out += f'<p class="tbl-cap">{caption.html}</p>'
    if label:
        out = f'<h3 class="blk-label">{label.html}</h3>' + out
        parts[0].text = joined(label.speech, parts[0].text)
    return out, parts


def r_steps(b, bid, where):
    items = need_list(b, 'items', where)
    label = inline(b.get('label'), where)
    given = inline(b.get('given'), where)
    goal = inline(b.get('goal'), where)
    out = f'<h3 class="blk-label">{label.html}</h3>' if label else ''
    parts = []
    if given:
        out += f'<div class="steps-given" data-node="{bid}-given"><span class="tagline">已知</span>{given.html}</div>'
        parts.append(Part(f'{bid}-given', joined(label.speech, '已知：' + given.speech), given.unspoken))
    out += '<ol class="steps">'
    for i, item in enumerate(items):
        w = f'{where}.items[{i}]'
        do = inline(need_text(item, 'do', w), w)
        why = inline(item.get('why'), w)
        basis = inline(item.get('basis'), w)
        mark = item.get('mark')
        if mark is not None and not re.fullmatch(r'(?:d?[MAB]\d|M\d A\d|B\d B\d|SC|ft|cso|awrt)(?:[ ,]+(?:d?[MAB]\d|ft|cso|awrt))*', str(mark)):
            fail(w, f'mark {mark!r} should use mark-scheme notation such as M1, A1, B1, dM1 or "M1 A1"')
        if not why and not basis:
            fail(w, 'explain each step: give "why" (the reasoning) and/or "basis" (the rule used)')
        note = inline(item.get('mark_note'), w)
        nid = f'{bid}-s{i}'
        out += (f'<li class="step" data-node="{nid}"><span class="step-n">{i + 1}</span><div class="step-body">'
                f'<div class="step-do">{do.html}</div>'
                + (f'<div class="step-why"><span class="tagline">为什么</span>{why.html}</div>' if why else '')
                + (f'<div class="step-basis"><span class="tagline">依据</span>{basis.html}</div>' if basis else '')
                + (f'<div class="step-mark-note">{note.html}</div>' if note else '')
                + '</div>' + (f'<span class="mark-badge">{esc(mark)}</span>' if mark else '') + '</li>')
        speech = joined(f'第{i + 1}步，{do.speech}', ('为什么？' + why.speech) if why else '', ('依据：' + basis.speech) if basis else '')
        if not given and i == 0 and label:
            speech = joined(label.speech, speech)
        parts.append(Part(nid, speech, do.unspoken + why.unspoken + basis.unspoken))
    out += '</ol>'
    basis_note = inline(b.get('marks_basis'), where)
    if basis_note:
        out += f'<p class="marks-basis">{basis_note.html}</p>'
    if goal:
        out += f'<div class="steps-goal" data-node="{bid}-goal"><span class="tagline">结论</span>{goal.html}</div>'
        parts.append(Part(f'{bid}-goal', '结论：' + goal.speech, goal.unspoken))
    return out, parts


REL_DEFAULT = {'cause': '导致', 'reason': '因为', 'condition': '仅当', 'evaluation': '但是', 'example': '例如'}


def r_chain(b, bid, where):
    items = need_list(b, 'items', where)
    if len(items) < 2:
        fail(where, 'a causal chain needs at least two links')
    label = inline(b.get('label'), where)
    out = f'<h3 class="blk-label">{label.html}</h3>' if label else ''
    out += f'<ol class="chain" data-direction="{esc(b.get("direction", "down"))}">'
    parts = []
    for i, item in enumerate(items):
        w = f'{where}.items[{i}]'
        item = item if isinstance(item, dict) else {'text': item}
        text = inline(need_text(item, 'text', w), w)
        note = inline(item.get('note'), w)
        rel = inline(item.get('rel', '导致' if i else None), w)
        nid = f'{bid}-c{i}'
        if i:
            out += f'<li class="chain-rel" aria-hidden="false"><span class="rel-arrow">↓</span><span class="rel-word">{rel.html}</span></li>'
        ao = item.get('ao')
        if ao is not None and ao not in ('AO1', 'AO2', 'AO3', 'AO4'):
            fail(w, 'ao must be AO1, AO2, AO3 or AO4')
        out += (f'<li class="chain-node" data-node="{nid}">' + (f'<span class="ao-badge">{ao}</span>' if ao else '') + f'<div class="chain-text">{text.html}</div>'
                + (f'<div class="chain-note">{note.html}</div>' if note else '') + '</li>')
        speech = joined((rel.speech + '，' if i else '') + text.speech, note.speech)
        if i == 0 and label:
            speech = joined(label.speech, speech)
        parts.append(Part(nid, speech, text.unspoken + note.unspoken + rel.unspoken))
    out += '</ol>'
    return out, parts


MAP_KINDS = {'root', 'topic', 'definition', 'cause', 'effect', 'condition', 'evaluation', 'example', 'step', 'contrast', 'policy', 'limit', 'note'}


def r_map(b, bid, where):
    root = b.get('root')
    if not isinstance(root, dict):
        fail(where, '"root" must be a node object {text, children}')
    layout = b.get('layout', 'auto')
    if layout not in ('auto', 'logic', 'outline'):
        fail(where, 'layout must be auto, logic or outline')
    parts, counter = [], [0]
    depth_seen = [0]

    def node(n, w, depth, top_branch):
        if not isinstance(n, dict):
            fail(w, 'map nodes are objects {text, rel?, kind?, children?}')
        text = inline(need_text(n, 'text', w), w)
        rel = inline(n.get('rel'), w)
        kind = n.get('kind', 'root' if depth == 0 else 'topic')
        if kind not in MAP_KINDS:
            fail(w, f'kind must be one of {sorted(MAP_KINDS)}')
        nid = f'{bid}-n{counter[0]}'
        counter[0] += 1
        depth_seen[0] = max(depth_seen[0], depth)
        children = n.get('children', [])
        if not isinstance(children, list):
            fail(w, '"children" must be a list')
        spoken = joined((rel.speech + '，') + text.speech if rel else text.speech)
        # Narrate per first-level branch so highlighting follows the branch being explained.
        if depth <= 1:
            parts.append(Part(nid, spoken, text.unspoken + rel.unspoken))
        else:
            parts[-1].text = joined(parts[-1].text, spoken)
            parts[-1].unspoken += text.unspoken + rel.unspoken
        kids = ''.join(node(c, f'{w}.children[{i}]', depth + 1, top_branch if depth else i) for i, c in enumerate(children))
        rel_html = f'<span class="mm-rel">{rel.html}</span>' if rel else ''
        sub = f'<ul>{kids}</ul>' if kids else ''
        ao = n.get('ao')
        if ao is not None and ao not in ('AO1', 'AO2', 'AO3', 'AO4'):
            fail(w, 'ao must be AO1, AO2, AO3 or AO4')
        badge = f'<span class="ao-badge">{ao}</span>' if ao else ''
        return f'<li class="mm-item" data-kind="{kind}" data-depth="{depth}">{rel_html}<div class="mm-node" data-node="{nid}">{badge}{text.html}</div>{sub}</li>'

    tree = node(root, f'{where}.root', 0, 0)
    label = inline(b.get('label'), where)
    head = f'<h3 class="blk-label">{label.html}</h3>' if label else ''
    if label:
        parts[0].text = joined(label.speech, parts[0].text)
    return (f'{head}<div class="mm" data-layout="{layout}" data-depth="{depth_seen[0]}"><ul class="mm-tree">{tree}</ul></div>', parts)


def r_figure(b, bid, where):
    svg = need_text(b, 'svg', where)
    if not svg.lstrip().startswith('<svg'):
        fail(where, '"svg" must be an inline <svg> element with a viewBox')
    passive(svg, where)
    caption = inline(b.get('caption'), where)
    points = b.get('points', [])
    if not isinstance(points, list):
        fail(where, '"points" must be a list')
    out = f'<figure class="fig"><div class="fig-svg">{svg}</div>' + (f'<figcaption>{caption.html}</figcaption>' if caption else '') + '</figure>'
    parts = [Part(bid, joined(b.get('speech_intro', ''), caption.speech), caption.unspoken)]
    if points:
        out += '<ol class="fig-points">'
        for i, p in enumerate(points):
            w = f'{where}.points[{i}]'
            t = inline(p, w)
            nid = f'{bid}-p{i}'
            out += f'<li data-node="{nid}">{t.html}</li>'
            parts.append(Part(nid, t.speech, t.unspoken))
        out += '</ol>'
    if not parts[0].text:
        parts = parts[1:] or [Part(bid, '', 1)]
    return out, parts


def r_pitfall(b, bid, where):
    items = need_list(b, 'items', where)
    label = inline(b.get('label', '易错点'), where)
    out = f'<h3 class="blk-label">{label.html}</h3><div class="pitfalls">'
    parts = []
    for i, item in enumerate(items):
        w = f'{where}.items[{i}]'
        wrong = inline(need_text(item, 'wrong', w), w)
        right = inline(need_text(item, 'right', w), w)
        why = inline(item.get('why'), w)
        src = inline(item.get('source'), w)
        lost = item.get('lost')
        nid = f'{bid}-f{i}'
        out += (f'<div class="pf" data-node="{nid}">' + (f'<span class="mark-badge pf-lost" title="丢的分">−{esc(lost)}</span>' if lost else '')
                + f'<div class="pf-wrong"><span class="pf-mark">✗</span>{wrong.html}</div>'
                f'<div class="pf-right"><span class="pf-mark">✓</span>{right.html}</div>'
                + (f'<div class="pf-why">{why.html}</div>' if why else '')
                + (f'<div class="pf-src">{src.html}</div>' if src else '') + '</div>')
        lead = label.speech + '。' if i == 0 else ''
        parts.append(Part(nid, joined(lead + '错误写法：' + wrong.speech, '正确：' + right.speech, why.speech), wrong.unspoken + right.unspoken + why.unspoken))
    return out + '</div>', parts


def r_exam(b, bid, where):
    items = need_list(b, 'items', where)
    label = inline(b.get('label', '考法与得分点'), where)
    out = f'<h3 class="blk-label">{label.html}</h3><ul class="exam-points">'
    parts = []
    for i, item in enumerate(items):
        w = f'{where}.items[{i}]'
        item = item if isinstance(item, dict) else {'text': item}
        t = inline(need_text(item, 'text', w), w)
        mark = item.get('mark')
        nid = f'{bid}-e{i}'
        out += f'<li data-node="{nid}">' + (f'<span class="mark-badge">{esc(mark)}</span>' if mark else '') + f'<span>{t.html}</span></li>'
        parts.append(Part(nid, joined((label.speech + '。') if i == 0 else '', t.speech), t.unspoken))
    return out + '</ul>', parts


def r_finish(b, bid, where):
    items = need_list(b, 'items', where)
    label = inline(b.get('label', '交卷前检查'), where)
    out = f'<h3 class="blk-label">{label.html}</h3><ul class="finish">'
    parts = []
    for i, item in enumerate(items):
        w = f'{where}.items[{i}]'
        t = inline(item if isinstance(item, str) else need_text(item, 'text', w), w)
        nid = f'{bid}-k{i}'
        out += f'<li data-node="{nid}"><span class="finish-box" aria-hidden="true"></span><span>{t.html}</span></li>'
        parts.append(Part(nid, joined((label.speech + '。') if i == 0 else '', t.speech), t.unspoken))
    return out + '</ul>', parts


def r_sections(b, bid, where):
    items = need_list(b, 'items', where)
    label = inline(b.get('label'), where)
    out = (f'<h3 class="blk-label">{label.html}</h3>' if label else '') + '<div class="sections">'
    parts = []
    for i, item in enumerate(items):
        w = f'{where}.items[{i}]'
        head = inline(need_text(item, 'head', w), w)
        text = inline(need_text(item, 'text', w), w)
        mark = item.get('mark')
        nid = f'{bid}-x{i}'
        out += (f'<section class="sec" data-node="{nid}"><h4>{head.html}' + (f'<span class="mark-badge">{esc(mark)}</span>' if mark else '')
                + f'</h4><p>{text.html}</p></section>')
        parts.append(Part(nid, joined((label.speech + '。') if i == 0 and label else '', head.speech, text.speech), head.unspoken + text.unspoken))
    return out + '</div>', parts


def r_html(b, bid, where):
    markup = need_text(b, 'html', where)
    passive(markup, where)
    speech = need_text(b, 'speech', where)
    return f'<div class="raw">{markup}</div>', [Part(bid, speech, 0)]


RENDERERS = {
    'lead': r_lead, 'note': r_note, 'definition': r_definition, 'unpack': r_unpack, 'examples': r_examples,
    'table': r_table, 'steps': r_steps, 'chain': r_chain, 'map': r_map, 'figure': r_figure, 'pitfall': r_pitfall,
    'exam': r_exam, 'finish': r_finish, 'sections': r_sections, 'html': r_html,
}


def render_block(block, bid, where):
    """Return (section_html, parts). An explicit block speech replaces derived parts."""
    if not isinstance(block, dict) or block.get('type') not in RENDERERS:
        fail(where, f'block "type" must be one of {sorted(RENDERERS)}')
    kind = block['type']
    body, parts = RENDERERS[kind](block, bid, where)
    if isinstance(block.get('speech'), str) and block['speech'].strip() and kind != 'html':
        parts = [Part(bid, block['speech'].strip(), 0)]
    missing = sum(p.unspoken for p in parts)
    if missing:
        fail(where, f'{missing} formula(s) have no spoken form; add 〔读法〕 after each $...$ or give the block a "speech"')
    parts = [p for p in parts if p.text.strip()]
    css = f'blk blk-{kind}'
    if block.get('emphasis'):
        css += ' emphasis'
    return f'<section class="{css}" data-node="{bid}">{body}</section>', parts
