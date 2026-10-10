"""Build ccpt-6 exam knowledge cards: one complete page per card, one narration player.

Usage:
  python build_cards.py deck.json out/ --preview          # pages only, no audio, no package
  python build_cards.py deck.json out/                    # synthesize narration, write .apkg
  python build_cards.py deck.json out/ --audio-pending    # package now, narration filled later (writes 补语音.txt)
  python build_cards.py deck.json --check-research        # before writing cards: exam lock, research, coverage plan

Every page is single-sided: Space plays/pauses narration, Enter = Good, 1 = again
next learning day (desktop add-on scripts/single_face_addon.py). Nothing asks the
reader to type or choose an answer.
"""
import argparse
import asyncio
import hashlib
import html
import json
import re
import shutil
import sys
from pathlib import Path

import genanki

from blocks import inline, render_block, esc, BlockError, strip_tags, REL_RULES, MATH, RENDERERS
from deck_rules import check, check_plan, GENRES, DeckError
from speech_backend import resolve_voice, inspect_voice, configured_azure, DEFAULT_VOICE
import narration
from package_addon import write_addon
import board_images

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets' / 'ccpt6'
FIELDS = ['StableID', 'Title', 'Page', 'Source', 'Narration']
KEYS_HINT = 'Space 播音 · Enter 继续 · 1 明天再看'


FONT_URL = re.compile(r'url\("(_ccpt6-[\w.-]+\.woff2)"\)')
ELBOW_THEMES = {'paper', 'lab', 'blueprint'}


def asset_css(extra=''):
    # Card-type motifs load after the subject themes so a theme's block styling never cancels them.
    parts = [(ASSETS / 'base.css').read_text(encoding='utf-8')]
    parts += [p.read_text(encoding='utf-8') for p in sorted((ASSETS / 'themes').glob('*.css'))]
    parts.append((ASSETS / 'motifs.css').read_text(encoding='utf-8'))
    return '\n'.join(parts) + ('\n' + extra if extra else '')


def bundle_fonts(css, themes):
    """Content-hashed font names: Anki never overwrites an existing "_" media file on import,
    so a changed subset under an old name would silently keep stale glyphs."""
    needed = set(FONT_URL.findall((ASSETS / 'base.css').read_text(encoding='utf-8')))
    for theme in themes:
        needed |= set(FONT_URL.findall((ASSETS / 'themes' / f'{theme}.css').read_text(encoding='utf-8')))
    files = []
    for name in sorted(needed):
        source = ASSETS / 'fonts' / name
        if not source.is_file():
            continue
        digest = hashlib.sha1(source.read_bytes()).hexdigest()[:8]
        hashed = name.replace('.woff2', f'.{digest}.woff2')
        css = css.replace(f'url("{name}")', f'url("{hashed}")')
        files.append((source, hashed))
    return css, files


def asset_js():
    # Layout first: the player calls window.ccptLayout once the page is wired.
    return '\n'.join((ASSETS / name).read_text(encoding='utf-8') for name in ('layout.js', 'player.js')) + '\n' + (ROOT / 'assets' / 'single-face.js').read_text(encoding='utf-8')


def card_tag(data, card):
    """Header label: the card's or deck's own tag, else "9708 · P3 · P4" / "YMA01 · WST02"."""
    if card.get('tag') or data['deck'].get('tag'):
        return card.get('tag') or data['deck']['tag']
    exam = data.get('exam') or {}
    code = exam.get('code') or ''
    units = []
    for unit in exam.get('units', []):
        base, _, suffix = unit.partition('/')
        if code and base == code and suffix:  # 9708/3 → P3
            units.append(f'P{suffix}' if suffix.isdigit() else suffix)
        else:                                # WMA14/01 and WMA14/01A → WMA14
            units.append(base)
    parts = list(dict.fromkeys(x for x in [code] + units if x))
    return ' · '.join(parts[:4]) + (' …' if len(parts) > 4 else '')


def render_card(data, card, style, blocks=None):
    """blocks: the card's blocks with board crops prepared (board_images.prepare); defaults to the card's own."""
    where = f'card {card["id"]}'
    title = inline(card['title'], f'{where}.title')
    if title.unspoken and not card.get('title_speech'):
        raise BlockError(f'{where}.title: add 〔读法〕 after each formula or give title_speech')
    sections, parts = [], [(None, card.get('title_speech') or title.speech)]
    for i, block in enumerate(blocks or card['blocks']):
        section, block_parts = render_block(block, f'b{i}', f'{where}.blocks[{i}]')
        sections.append(section)
        parts += [(p.target, p.text) for p in block_parts]
    voice = resolve_voice(style.get('voice_by_subdeck', {}).get(card.get('subdeck', ''), style.get('voice') or DEFAULT_VOICE))
    theme = card.get('theme') or style.get('theme_by_subdeck', {}).get(card.get('subdeck', '')) or style.get('theme', 'editorial')
    if theme in ELBOW_THEMES:  # textbook and engineering themes draw right-angled connectors by default
        sections = [re.sub(r'<div class="mm" (?![^>]*data-edge)', '<div class="mm" data-edge="elbow" ', sec) for sec in sections]
    return {'title_html': title.html, 'sections': sections, 'parts': parts, 'voice': voice, 'theme': theme}


def choose_speed(card, style, narration_text, seen_terms):
    """Card speed: explicit card value, else a deck-wide number, else the computed rule."""
    metrics = narration.speed_metrics(card, narration_text, seen_terms)
    auto_speed, auto_reason = narration.decide_speed(metrics)
    metrics['auto_reason'] = auto_reason
    if 'speed' in card:
        return float(card['speed']), card.get('speed_reason', ''), metrics, auto_speed
    deck_speed = style.get('speed', 'auto')
    if deck_speed != 'auto':
        return float(deck_speed), style.get('speed_reason', ''), metrics, auto_speed
    return auto_speed, auto_reason, metrics, auto_speed


FORMULA_BOOKLET = {'given': '公式表已给', 'memorise': '须背：公式表没有', 'derive': '须会推导'}


def clock(seconds):
    seconds = int(round(seconds))
    return f'{seconds // 60}:{seconds % 60:02d}'


def page(data, card, r, audio_name, cues, pending_message=None):
    genre = card['genre']
    speed_label = f'{r["speed"]:g}×'
    voice_label = {'zh-CN-XiaoxiaoNeural': '晓晓', 'zh-CN-YunyangNeural': '云扬', 'zh-CN-YunxiNeural': '云希'}.get(r['voice'], r['voice'])
    attrs = f'class="ccpt6" data-ccpt-single="1" data-side="read" data-theme="{esc(r["theme"])}" data-genre="{esc(genre)}" data-note="{esc(card["id"])}"'
    if pending_message:
        attrs += f' data-audio-pending="1" data-audio-message="{esc(pending_message)}"'
    player = (f'<button class="speak" data-audio="{"" if pending_message else esc(audio_name)}" aria-label="整页讲解：播放、暂停或继续" aria-pressed="false"'
              + (f' disabled title="{esc(pending_message)}"' if pending_message else '') + '>▶</button>'
              f'<button class="speed" type="button" data-speed="{r["speed"]:g}" data-encoded="{r["speed"]:g}" aria-label="切换 2× 与 1.5×" title="点击在 2× 与 1.5× 之间切换（只对本卡生效）">{speed_label}</button>')
    if r['speed'] < 2 and r.get('speed_reason'):
        player += f'<span class="speed-reason" title="{esc(r["speed_reason"])}">{esc(r["speed_reason"].split("；")[0][:16])}</span>'
    length = f' · {clock(cues["duration"])}' if cues else ''
    status = esc(pending_message) if pending_message else f'{voice_label} · {speed_label}{length}'
    out = (f'<main {attrs}><header class="cc-head"><div class="cc-meta"><span class="cc-genre">{GENRES[genre]}</span>'
           f'<span class="cc-tag">{esc(card_tag(data, card))}</span>'
           + (f'<span class="cc-fb" data-fb="{card["formula_booklet"]}">{FORMULA_BOOKLET[card["formula_booklet"]]}</span>' if card.get('formula_booklet') else '')
           + (f'<span class="cc-gap" title="{esc(card["board_gap"])}">补充 · 板书未写</span>' if card.get('board_gap') else '')
           + '</div>'
           f'<div class="cc-titlebar"><h1 data-node="title">{r["title_html"]}</h1><div class="cc-player">{player}</div></div></header>'
           f'<article class="cc-body">{"".join(r["sections"])}</article>'
           f'<footer class="cc-foot"><span class="audio-status">{status}</span><span class="keys">{KEYS_HINT if not pending_message else "Enter 继续 · 1 明天再看"}</span></footer>')
    payload = json.dumps({'narration': cues}, ensure_ascii=False)
    out += f'<div hidden class="cc-data">{esc(payload)}</div>'
    src = '' if pending_message else ' src="' + esc(audio_name) + '"'
    out += f'<audio preload="none"{src}></audio></main>'
    return out


def source_record(data, card, speed=None, speed_reason=''):
    exam = data.get('exam') or {}
    record = {'schema': 'ccpt-6', 'card': card['id'], 'exam': ' '.join(filter(None, [exam.get('code'), '/'.join(exam.get('units', []))])) or None,
              'covers': card.get('covers', []), 'sources': card.get('sources', []), 'speed': speed}
    if speed_reason:
        record['speed_reason'] = speed_reason
    if card.get('board_gap'):
        record['board_gap'] = card['board_gap']
    # Anki stores fields as HTML; JSON escapes keep json.loads exact without HTML-escaping.
    return json.dumps(record, ensure_ascii=False).replace('<', r'\u003c').replace('>', r'\u003e').replace('&', r'\u0026')


def subdeck_id(base, name):
    return base + int(hashlib.sha256(name.encode()).hexdigest()[:6], 16)


def write_term_sampler(data, out, media, lexicon, plans=()):
    """Edge cannot take phoneme hints, so the listener hears every term and abbreviation once and fixes speech_lexicon if needed.
    Terms come from definition blocks, the lexicon and every all-caps abbreviation heard in the narration (MSC, PED, CLT…)."""
    style = data['style']
    by_voice = {}
    for p in plans:
        by_voice.setdefault(p['voice'], []).extend(re.findall(r'(?<![A-Za-z])[A-Z]{2,6}(?![A-Za-z])', p['text']))
    for card in data['cards']:
        voice = resolve_voice(style.get('voice_by_subdeck', {}).get(card.get('subdeck', ''), style.get('voice') or DEFAULT_VOICE))
        for b in card['blocks']:
            if b.get('type') == 'definition':
                by_voice.setdefault(voice, []).append(strip_tags(inline(b['term'], 'sampler').html))
    deck_voice = resolve_voice(style.get('voice') or DEFAULT_VOICE)
    by_voice.setdefault(deck_voice, []).extend(k for k in lexicon if re_latin(k))
    speed = 2.0 if style.get('speed', 'auto') == 'auto' else float(style['speed'])
    for voice, terms in by_voice.items():
        terms = list(dict.fromkeys(t for t in terms if t))
        if not terms:
            continue
        suffix = '' if voice == deck_voice else '-' + voice.split('-')[-1].replace('Neural', '').lower()
        p = narration.plan('term-sampler', [(f't{i}', f'下面这个词是：{t}。') for i, t in enumerate(terms)], voice, speed, lexicon)
        asyncio.run(narration.synthesize_clips([p], media))
        narration.assemble(p, media)
        (out / f'term-sampler{suffix}.mp3').write_bytes((media / p['file']).read_bytes())
        (out / f'term-sampler{suffix}.txt').write_text('\n'.join(terms), encoding='utf-8')


def re_latin(value):
    return bool(re.search(r'[A-Za-z]', value))


COMMON_EN = {w for line in Path(__file__).with_name('common_en.txt').read_text(encoding='utf-8').splitlines()
             if not line.startswith('#') for w in line.split()}


IRREGULAR = {'matrices': 'matrix', 'vertices': 'vertex', 'indices': 'index', 'appendices': 'appendix', 'data': 'data',
             'criteria': 'criterion', 'phenomena': 'phenomenon', 'hypotheses': 'hypothesis', 'analyses': 'analysis', 'axes': 'axis'}


def singular(word):
    """units → unit, probabilities → probability, prices → price, matrices → matrix (enough to match a term with its plural)."""
    w = word.lower()
    if w in IRREGULAR:
        return IRREGULAR[w]
    if w.endswith('ies') and len(w) > 4:
        return w[:-3] + 'y'
    if re.search(r'(ss|x|ch|sh)es$', w):
        return w[:-2]
    if w.endswith('s') and not re.search(r'(ss|us|is)$', w) and len(w) > 3:
        return w[:-1]
    return w


CAUSAL = r'^(导致|引起|造成|使得|使|所以|因此|从而|进而|于是|带来|因而|结果|以致|引发|促进|推动|产生|加剧|抑制|提高|降低|增加|减少|刺激|leads? to|causes?|so|therefore|raises?|reduces?)'
DIRECTION = (r'上升|下降|增加|增大|减少|减小|扩大|缩小|提高|降低|升高|升至|升到|降至|降到|涨|跌|右移|左移|上移|下移|外移|内移|移动|↑|↓|'
             r'高于|低于|大于|小于|超过|不足|多于|少于|等于|回到|变为|变成|偏离|消除|消失|出现|形成|过度|过少|过多|→|rise|fall|increase|decrease|shift|exceed|'
             r'失灵|短缺|过剩|损失|浪费|低效|无效|有效|效率|均衡|最优|failure|shortage|surplus|loss|efficien|equilibrium|optimum')
CONDITION = r'取决于|如果|假如|若|当|只有|除非|前提|条件|视|depends|unless|only if|provided'
REASONING = r'为了|因为|由于|所以|使|才能|需要|要|否则|根据|满足|成立|保证|目的|以便|定理|法则|公式|定义|条件|规则|性质|等价'
HAN = re.compile(r'[一-鿿]')


def chain_nodes(items, first=True):
    """Chain nodes in reading order; a plain string is a node, and a node without rel reads as 导致."""
    for e in items:
        if isinstance(e, dict) and 'fork' in e:
            for branch in e['fork']:
                yield from chain_nodes(branch, first=False)
        else:
            node = e if isinstance(e, dict) else {'text': str(e)}
            if not first and not node.get('rel'):
                node = dict(node, rel='导致')
            yield node
        first = False


def map_nodes(node, depth=0):
    if isinstance(node, dict):
        yield node, depth
        for child in node.get('children', []) or []:
            yield from map_nodes(child, depth + 1)


def reading_units(text):
    """Length as a reader feels it: each Chinese character and each English word counts once."""
    t = plain(text)
    return len(HAN.findall(t)) + len(re.findall(r'[A-Za-z]+', t))


def plain(text):
    """Author text as words: formulas replaced by their readings, tags removed (lint input)."""
    return strip_tags(MATH.sub(lambda m: ' ' + (m.group(4) or m.group(2) or m.group(3) or '') + ' ', text or ''))


ACTION_WORDS = r'代入|得到|可得|求得|算得|化简|计算|展开|整理|移项|于是|即|所以|就是|然后'


def why_echoes(why, do):
    """A "why" that only restates the step: once the step's own symbols and action words are removed,
    fewer than three meaningful characters remain and no reason (goal, condition, rule) is named."""
    w = re.sub(r'\s|\$|〔[^〕]*〕', '', strip_tags(why))
    d = re.sub(r'\s|\$|〔[^〕]*〕', '', strip_tags(do))
    if not w or re.search(REASONING.replace('所以|', ''), w):
        return False
    residue = re.sub(ACTION_WORDS, '', ''.join(ch for ch in w if ch not in d))
    return len(re.findall(r'[\u4e00-\u9fffA-Za-z]', residue)) < 3


def causal_lint(nodes, out, where):
    """Arrows must say which variable moves which way; evaluation must name its condition."""
    vague, unjudged, long_nodes = [], [], []
    for node, depth in nodes:
        text = plain(node.get('text', ''))
        rel = plain(node.get('rel', '') or '')
        if node.get('kind', 'topic') in ('topic', 'cause', 'effect', 'policy') and re.match(CAUSAL, rel) and not re.search(DIRECTION + '|' + CONDITION, rel + ' ' + text):
            vague.append(text[:12])
        if (node.get('ao') == 'AO3' or node.get('kind') == 'evaluation') and not (
                node.get('cond') or node.get('note') or re.search(CONDITION, text)
                or any(isinstance(c, dict) and c.get('kind') == 'condition' for c in node.get('children', []) or [])):
            unjudged.append(text[:12])
        limit = 20 if where == 'map' and depth <= 1 else 25
        if len(HAN.findall(text)) > limit:
            long_nodes.append(text[:12])
    if vague:
        out.append(f'{where} 的因果箭头没写变量往哪个方向变（如“Q 由 Qm 降到 Q*”“MPC 上移”）：' + '｜'.join(vague[:4]))
    if unjudged:
        out.append(f'{where} 的评价节点缺条件或对结论的影响（cond、note 或条件子节点）：' + '｜'.join(unjudged[:4]))
    if long_nodes:
        out.append(f'{where} 节点超过约 25 个汉字（导图前两层约 20 个）：机制细节放到下一层或下一个节点：' + '｜'.join(long_nodes[:4]))


PROSE_THEMES = {'editorial', 'manuscript'}  # humanities themes: paragraphs become arrows on every card type
SKIP_KEYS = {'source', 'sources', 'marks_basis', 'ref', 'speech', 'type', 'id', 'kind', 'rel', 'arrow', 'ao', 'mark', 'marks', 'lost',
             'cards', 'covers', 'src', 'alt', 'svg', 'html', 'source_type', 'layout', 'edge', 'direction', 'theme', 'cond_speech',
             'box', 'masks', 'tone', 'where', 'aid'}
PLAIN_MATH = re.compile(r'[Σ∑√∫∏]|[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]|(?<![A-Za-z])(?:P|E|Var|Cov)\s*\(|\d\s*×\s*\d|(?<![\d./A-Za-z])(\d{1,3})\s*/\s*(\d{1,3})(?![\d/])')
MARK_AFTER = re.compile(r'^\s*(?:分|marks?\b|个?得分点)', re.I)
# a tally or page reference, not maths: "Level 2（10/14）", "ECR 低档 4/14", "AO3 至少 4/6", "p. 12/13", "只得 7/14"
MARK_BEFORE = re.compile(r'(?:Level\s*\d|L\d|档|AO\d|ECR|band|得|满分|score[sd]?|only|仅|至少|at least|pp?\.|marks?)[^/／\d]{0,6}$', re.I)


def plain_math(card):
    """Maths written as plain text outside $…$: it is neither typeset nor read correctly. Mark tallies (7/14 marks) are not maths."""
    hits = []

    def scan(value, key=''):
        if isinstance(value, dict):
            for k, v in value.items():
                if k not in SKIP_KEYS:
                    scan(v, k)
        elif isinstance(value, list):
            for v in value:
                scan(v, key)
        elif isinstance(value, str):
            visible = re.sub(r'〔[^〕]*〕', ' ', MATH.sub(' ', value))
            visible = re.sub(r'<[^>]+>', ' ', visible)
            for m in PLAIN_MATH.finditer(visible):
                if m.group(1) and (MARK_AFTER.search(visible[m.end():m.end() + 6]) or MARK_BEFORE.search(visible[max(0, m.start() - 14):m.start()])):
                    continue
                hits.append(visible[max(0, m.start() - 8):m.end() + 8].strip())
    scan(card.get('blocks', []))
    scan(card.get('title', ''))
    return hits


def derived_speech(block):
    """What a block would narrate without its own "speech" (formulas without readings count as placeholders)."""
    if block.get('type') not in RENDERERS or block.get('type') == 'html':
        return ''
    try:
        return ' '.join(p.text for p in RENDERERS[block['type']](dict(block, speech=None), 'x', 'lint')[1])
    except BlockError:
        return ''


def lint_card(card, academic=True, theme='editorial', prepared=None):
    """Advisory checks that keep cards explained, readable and in the user's preferred shape.
    prepared: the card's blocks with board crops prepared (board_images.prepare), when there are any."""
    out = []
    worked = card.get('genre') in ('derivation', 'method', 'formula')
    if worked and academic and not card.get('formula_booklet'):
        out.append('推导／方法／公式卡没有 formula_booklet：写明公式表给不给（given／memorise／derive），页眉会显示')
    prose_limit = card.get('genre') in ('chain', 'map', 'essay', 'overview') or theme in PROSE_THEMES
    for b in card['blocks']:
        if not isinstance(b, dict):
            continue
        own = b.get('speech') if isinstance(b.get('speech'), str) else ''
        if own.strip() and b.get('type') != 'html':
            full = derived_speech(b)
            if len(full) >= 40 and len(own) < 0.5 * len(full):
                out.append(f'{b.get("type")} 块自带的 speech 只有卡面内容旁白的 {round(100 * len(own) / len(full))}%：可能漏讲了步骤或理由')
        if b.get('type') == 'steps':
            items = [i for i in b.get('items', []) if isinstance(i, dict)]
            trivial = [i for i in items if i.get('trivial')]
            for i in trivial:
                if re.search(r'\^|\\frac|\d\s*[x(]|[+-]\s*\d', i.get('do', '')):
                    out.append('trivial 步含系数、乘方或符号运算，这正是丢 A 分处，请写 why 或 mark_note')
                    break
            if items and len(trivial) > len(items) * 0.25:
                out.append('trivial 步超过四分之一，检查是否跳过了需要讲的步骤')
            if worked:
                bare = [n + 1 for n, i in enumerate(items) if not i.get('trivial') and not i.get('why') and not i.get('mark_note')]
                if bare:
                    out.append(f'第 {"、".join(map(str, bare))} 步没有“为什么”：推导卡每一步都讲目的、条件或原理')
                if academic and not any(i.get('mark') for i in items) and not b.get('marks_basis'):
                    out.append('推导步骤没有标得分点（mark）也没有 marks_basis：按 MS 标出每一步值什么分')
            if any(i.get('why') and len(plain(i['why'])) < 6 for i in items):
                out.append('有的“为什么”少于 6 个字，可能没讲出原理')
            echo = [n + 1 for n, i in enumerate(items) if i.get('why') and why_echoes(i['why'], i.get('do', ''))]
            if echo:
                out.append(f'第 {"、".join(map(str, echo))} 步的“为什么”像在复述做法：写目的（为了…）、条件（因为…成立）或原理名')
            whys = [plain(i['why']) for i in items if i.get('why')]
            if len(whys) >= 3 and len(set(whys)) == 1:
                out.append('每一步的“为什么”都一样：逐步写出这一步的目的或依据')
        if b.get('type') == 'sections' and any(isinstance(i, dict) and reading_units(i.get('text', '')) > 60 for i in b.get('items', [])):
            out.append('sections 有超过 60 字的长段：文科展开改用 chain 或 map 的箭头结构')
        if b.get('type') in ('lead', 'note') and prose_limit and reading_units(b.get('text', '')) > 80:
            out.append(f'{b["type"]} 超过约 80 字（汉字与英文词合计）：因果展开写进 chain 或 map 的节点，不写成段落')
        if b.get('type') == 'chain':
            causal_lint(((n, 0) for n in chain_nodes(b.get('items', []))), out, 'chain')
        if b.get('type') == 'map':
            root = b.get('root', {})
            nodes = list(map_nodes(root))
            causal_lint(nodes[1:], out, 'map')
            unknown = sorted({plain(n['rel']) for n, _ in nodes if n.get('rel') and not n.get('arrow')
                              and not any(rule.match(plain(n['rel'])) for rule, _ in REL_RULES)})
            if unknown:
                out.append('这些导图关系词不在规则表里，连线画成无箭头的普通线：' + '、'.join(unknown[:6]) + '（若表示因果，改用规则表中的词或给节点写 arrow）')
            branches = root.get('children', [])
            def count(n):
                return 1 + sum(count(c) for c in n.get('children', []))
            if len(branches) > 7:
                out.append(f'导图一级分支 {len(branches)} 个，超过 7 个时考虑分组或拆卡')
            for i, br in enumerate(branches):
                if count(br) > 12:
                    out.append(f'导图第 {i + 1} 个分支有 {count(br)} 个命题，超过 12 个时考虑把这一支拆成子图卡')
    if card.get('genre') == 'board':
        board_lint(card, out, prepared)
    doubted = sorted({m.group(0) for t in walk_text(card.get('title', ''), card.get('blocks', [])) for m in DOUBTING_SOURCE.finditer(plain(t))})
    if doubted:
        out.append('卡上说评分方案或考纲有问题（' + '｜'.join(doubted[:3]) + '）：考纲与评分方案是最高依据，卡面按它们的说法讲，'
                   '不写成“更准确的说法”（SKILL.md“内容以谁为准”）')
    hits = plain_math(card)
    if hits:
        out.append(f'{len(hits)} 处数学写成了纯文本（不排版、不按读法朗读），改成 $…$〔读法〕：' + '｜'.join(hits[:3]))
    return out


BOARD_TEXT_LIMIT = 120   # reading units of typed text a board card may carry beside the board
SPOT_HINT = 90           # a crop explained at this length without spots leaves the eye searching
SHORT_CROP_LINES = 3     # ...unless the crop is itself only a few lines: then it is the line being explained
NOTE_NODES = 7           # an annotation helps read one crop; more than this is new content for a supplementary card
# The syllabus and mark scheme are never wrong and the board almost never is (SKILL.md, 内容以谁为准): narration and
# annotations on a board card explain them and never correct them.
CORRECTING = re.compile(r'笔误|写错|应为|应改|应是|更正|有误|不准确|说得过|过强|不严谨|准确说|更准确|改述|不暗示|其实是')
DOUBTING_SOURCE = re.compile(r'(?:评分方案|考纲|mark scheme|syllabus|\bMS\b)[^。；;]{0,14}(?:写错|有误|不准确|不严谨|错了|不对|宽泛|粗糙)', re.I)


def board_lint(card, out, prepared=None):
    """The board is the card: typed text beside it repeats what the learner already read (redundancy), and a long
    explanation with nothing framed on the board leaves the eye searching for the line being explained (signaling).
    prepared: the card's blocks after board_images.prepare, whose crops know their height in board lines."""
    typed = sum(reading_units(derived_speech(b)) for b in card['blocks'] if isinstance(b, dict) and b.get('type') != 'board')
    if typed > BOARD_TEXT_LIMIT:
        out.append(f'板书卡的文字块约 {typed} 字：卡面以板书为主，讲解放进语音；板书没有、考试要的内容另做补充卡放在这张后面')
    for b in prepared or card['blocks']:
        if not isinstance(b, dict) or b.get('type') != 'board':
            continue
        for j, crop in enumerate(b.get('crops', [])):
            if not isinstance(crop, dict) or crop.get('_media', {}).get('lines', SHORT_CROP_LINES + 1) <= SHORT_CROP_LINES:
                continue
            if not crop.get('spots') and reading_units(crop.get('speech', '')) > SPOT_HINT:
                out.append(f'第 {j + 1} 块板书讲解约 {reading_units(crop.get("speech", ""))} 字却没有 spots：用 spots 框出正在讲的那几行，语音读到哪里就框到哪里')
        heard = []
        for j, crop in enumerate(b.get('crops', [])):
            if isinstance(crop, dict):
                heard.append(crop.get('speech') or '')
                heard += [s.get('speech') or '' for s in crop.get('spots', []) or [] if isinstance(s, dict)]
                note = crop.get('annotate')
                if isinstance(note, dict) and isinstance(note.get('root'), dict):
                    heard += [plain(n.get('text', '')) + ' ' + plain(n.get('rel', '') or '') for n, _ in map_nodes(note['root'])]
        heard += [b2.get('text', '') for b2 in card['blocks'] if isinstance(b2, dict) and b2.get('type') == 'note']
        hits = sorted({m.group(0) for t in heard for m in CORRECTING.finditer(t)})
        if hits:
            out.append('板书卡的讲解或批注里有纠错说法（' + '、'.join(hits) + '）：考纲与评分方案最高、板书其次、制作者的判断最低；'
                       '讲解和批注帮读者理解上一级的说法，不纠正它（SKILL.md“内容以谁为准”）')
        for j, crop in enumerate(b.get('crops', [])):
            note = crop.get('annotate') if isinstance(crop, dict) else None
            if not isinstance(note, dict) or not isinstance(note.get('root'), dict):
                continue
            nodes = list(map_nodes(note['root']))
            if len(nodes) > NOTE_NODES:
                out.append(f'第 {j + 1} 块板书的批注有 {len(nodes)} 个节点（超过 {NOTE_NODES} 个）：批注只帮读懂这块板书，'
                           '板书没讲、考试又要的内容另做补充卡（board_gap）')
            causal_lint(nodes[1:], out, f'第 {j + 1} 块板书的批注')
            if not any(n.get('rel') for n, _ in nodes[1:]):
                out.append(f'第 {j + 1} 块板书的批注没有关系词：子节点写 rel（因为、所以、不是、而是、仅当…），否则只是并列的笔记')


def known_terms(data):
    """terms_known entries: {term, taught_in} objects (taught on a card of this deck) or plain strings (older decks)."""
    return [t['term'] if isinstance(t, dict) else t for t in data.get('terms_known', [])]


FUNCTION_WORDS = set(Path(__file__).with_name('common_en.txt').read_text(encoding='utf-8').split('\n# exam instructions')[0].split())


def protected_words(data):
    """Words of the deck's own definition terms are never treated as common English (a deck about "Evaluate" checks it),
    except plain function words such as "that", "with", "over"."""
    words = set()
    for c in data['cards']:
        for b in c['blocks']:
            if b.get('type') == 'definition':
                words |= {singular(w) for w in re.findall(r'[A-Za-z]{4,}', strip_tags(inline(b['term'], 'ledger').html))}
    return words - {singular(w) for w in FUNCTION_WORDS}


GLOSS = re.compile(r'([A-Za-z][A-Za-z -]{2,40}?)\s*[（(][^）)]*[\u4e00-\u9fff][^）)]*[）)]')
ABBR_GLOSS = re.compile(r'\b([A-Z]{2,5})\s*[（(][^）)]*[\u4e00-\u9fff]')


def term_ledger(data, pages):
    """English subject words on the cards that no term card, <abbr>, gloss or terms_known explains.
    Single words count too (externality, integrand, separable); words inside a definition's own sentence do not.
    Quoted exam stems are scanned too unless a Chinese rendering of the whole sentence sits beside them
    (untranslated quotes are reported separately). Returns the full ledger."""
    defined = {k.lower() for k in known_terms(data)}
    for c in data['cards']:
        for b in c['blocks']:
            if b.get('type') == 'definition':
                defined.add(strip_tags(inline(b['term'], 'ledger').html).lower())
    defined_words = {singular(w) for d in defined for w in re.findall(r'[a-z]+', d)}
    stop = ({singular(w) for w in COMMON_EN} | {singular(w) for w in data.get('ignore_words', [])}) - protected_words(data)
    context = ' '.join(str(x) for x in walk_text(data.get('coverage', {}), data.get('demands', []))).lower()
    seen = {}
    for cid, body in pages.items():
        # chrome, citations and the definition sentence itself are not teaching vocabulary
        body = re.sub(r'<header[\s\S]*?</header>|<footer[\s\S]*?</footer>|<div hidden[\s\S]*?</div>', ' ', body)
        body = re.sub(r'<(p|span|div) class="(?:def-text|def-label|def-src|pf-src|tbl-cap|marks-basis|bd-note-exam)[^"]*"[^>]*>[\s\S]*?</\1>', ' ', body)
        body = re.sub(r'<math[\s\S]*?</math>', ' ', body)
        defined_here = {m.lower() for m in re.findall(r'<abbr[^>]*>(.*?)</abbr>', body)}
        # a quoted sentence (8+ English words) with its Chinese rendering beside it is explained as a whole
        segments = text_segments(body)
        visible = ' '.join(seg for i, seg in enumerate(segments) if not translated_quote(segments, i))
        # a gloss anywhere on the card counts as an explanation: integrand（被积函数）, MS（评分方案）
        whole = ' '.join(segments)
        defined_here |= {m.lower().strip() for m in GLOSS.findall(whole)} | {m.lower() for m in ABBR_GLOSS.findall(whole)}
        # compare glossed phrases in the same reduced form as the keys ("youth club members" → "youth member")
        defined_here |= {' '.join(singular(w) for w in d.split() if singular(w) not in stop and w not in stop) for d in list(defined_here)}
        for phrase in re.findall(r'\b[A-Za-z][a-z]{3,}(?: [a-z]{2,}){0,2}\b|\b[A-Z]{2,5}\b', visible):
            words = [w for w in phrase.split() if singular(w) not in stop and w.lower() not in stop]
            if not words:
                continue
            key = ' '.join(w if w.isupper() else singular(w) for w in words)
            low = key.lower()
            if low in defined or low in defined_here or any(low in d for d in defined_here) \
                    or all(singular(w) in defined_words for w in words):
                continue
            seen.setdefault(key, set()).add(cid)
    ranked = sorted(seen.items(), key=lambda kv: (kv[0].lower() not in context, -len(kv[1]), kv[0]))
    return [{'term': t, 'cards': sorted(c), 'in_scope_text': t.lower() in context} for t, c in ranked]


def walk_text(*values):
    for value in values:
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            yield from walk_text(*value.values())
        elif isinstance(value, list):
            yield from walk_text(*value)


def text_segments(body):
    """Visible text of a page split at block-level tags (paragraphs, list items, cells, nodes)."""
    body = re.sub(r'<header[\s\S]*?</header>|<footer[\s\S]*?</footer>|<div hidden[\s\S]*?</div>|<math[\s\S]*?</math>', ' ', body)
    body = re.sub(r'<(p|span|div) class="(?:def-src|pf-src|tbl-cap|marks-basis|bd-note-exam)[^"]*"[^>]*>[\s\S]*?</\1>', ' ', body)
    segments = [strip_tags(re.sub(r'<[^>]+>', ' ', x)).strip() for x in re.split(r'</?(?:p|li|div|td|th|dd|dt|h1|h2|h3|section|tr)\b[^>]*>', body)]
    return [x for x in segments if x]


def is_quote(segment):
    return len(re.findall(r'[A-Za-z]+', segment)) >= 8


def translated_quote(segments, i):
    """An English sentence with Chinese in it or right beside it (a rendering of the whole sentence)."""
    beside = [segments[j] for j in (i - 1, i + 1) if 0 <= j < len(segments)]
    return is_quote(segments[i]) and (bool(HAN.search(segments[i])) or any(HAN.search(x) for x in beside))


def untranslated(pages):
    """Card ids with an English sentence of 8+ words and no Chinese in it or beside it."""
    out = {}
    for cid, body in pages.items():
        segments = text_segments(body)
        for i, seg in enumerate(segments):
            if is_quote(seg) and not translated_quote(segments, i):
                out.setdefault(cid, []).append(seg[:50])
    return out


AUDIO_NOTE = """这个包先交付了图文，语音待补。照下面做一次，就能给同一副卡原位补上语音（卡片不变，复习记录保留）。
补语音需要的程序已经放在本文件夹的 skill 子文件夹里，不需要另外下载 skill 包。

一、准备（每台电脑做一次）
1. 安装 Python 3.10 或更新版本（python.org 下载；Windows 安装时勾选 "Add python.exe to PATH"）。
   Linux 另装：sudo apt install python3-venv
2. 安装 ffmpeg，装完关掉再重开终端：
     Windows：winget install Gyan.FFmpeg
     macOS：  brew install ffmpeg
     Linux：  sudo apt install ffmpeg
3. 打开终端，进入这个交付文件夹（cd 到 补语音.txt 所在的文件夹）。

二、补语音（电脑要能访问 speech.platform.bing.com）
Windows（PowerShell 或命令提示符）：
  py -m venv .venv
  .\\.venv\\Scripts\\python -m pip install -r skill\\scripts\\requirements.txt
  .\\.venv\\Scripts\\python skill\\scripts\\speech_backend.py --check
  .\\.venv\\Scripts\\python skill\\scripts\\build_cards.py deck.json . --term-sampler

macOS 或 Linux（终端）：
  python3 -m venv .venv
  .venv/bin/python -m pip install -r skill/scripts/requirements.txt
  .venv/bin/python skill/scripts/speech_backend.py --check
  .venv/bin/python skill/scripts/build_cards.py deck.json . --term-sampler

--check 显示 "route": "edge" 才说明语音服务可用；显示 ffmpeg_missing 就回到第 2 步。

三、导入与试听
1. 把本文件夹里新生成的 .apkg 导入 Anki：同一张卡原位更新，复习记录保留。
2. 听一遍 term-sampler.mp3（约一分钟），把读错的词告诉 Claude（新对话里附上本文件夹的 deck.json），写进 speech_lexicon 后重建。

也可以在自己电脑上的 Claude Code 里说“按 补语音.txt 给这副卡补语音”，让 Claude 代为执行。
"""
RUNTIME = ('build_cards.py', 'blocks.py', 'deck_rules.py', 'narration.py', 'speech_backend.py', 'package_addon.py',
           'single_face_addon.py', 'html_integrity.py', 'board_images.py', 'slice_board.py', 'common_en.txt', 'requirements.txt')


def bundle_runtime(out):
    """Copy what a rebuild needs into <out>/skill/, so the delivered folder alone can fill in the audio."""
    dest = (out / 'skill').resolve()
    if dest == ROOT.resolve():
        return  # already running from the bundled copy in this folder
    (dest / 'scripts').mkdir(parents=True, exist_ok=True)
    for name in RUNTIME:
        shutil.copy2(ROOT / 'scripts' / name, dest / 'scripts' / name)
    shutil.copytree(ROOT / 'assets', dest / 'assets', dirs_exist_ok=True, ignore=shutil.ignore_patterns('.DS_Store', '__pycache__'))


def preflight(voice):
    """Fail fast with a clear class instead of hanging on a blocked network."""
    try:
        import edge_tts  # noqa: F401 - only checking that the package is installed
    except ImportError:
        if not configured_azure():
            print('✗ edge_tts_missing: the edge-tts package is not installed (it is not a network problem).\n'
                  '  Run: python -m pip install -r scripts/requirements.txt   (inside the same Python or virtual environment)', file=sys.stderr)
            sys.exit(5)
    report = asyncio.run(inspect_voice(voice))
    if report['route'] != 'unavailable':
        return
    if report.get('edge_list_available') is False:
        print(f'✗ network_blocked: the Edge voice service could not be reached ({report.get("edge_error")}) and no Azure Speech is configured.\n'
              '  这台电脑现在连不上微软语音服务（speech.platform.bing.com）：换一个网络（例如关掉学校或公司的代理）或换一台电脑，再运行同一条命令。\n'
              '  Card makers: deliver now with --audio-pending; run the same command without it where the service is reachable.', file=sys.stderr)
        sys.exit(2)
    print(f'✗ voice_missing: {voice} is not offered by the Edge service; no voice was substituted.', file=sys.stderr)
    sys.exit(3)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('input', type=Path)
    ap.add_argument('output', type=Path, nargs='?')
    ap.add_argument('--check-research', action='store_true', help='before writing cards: check the exam lock, research trail and coverage/demand plan')
    ap.add_argument('--preview', action='store_true', help='write preview pages only; no audio, no package')
    ap.add_argument('--audio-pending', action='store_true', help='package without narration; pages say so and the player is disabled')
    ap.add_argument('--term-sampler', action='store_true', help='also write term-sampler.mp3: every English term in a carrier sentence, for a one-minute pronunciation check')
    a = ap.parse_args(argv)
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    data = json.loads(a.input.read_text(encoding='utf-8'))
    if a.check_research:
        try:
            plan = check_plan(data)
        except DeckError as error:
            sys.exit(f'✗ {error}')
        print(json.dumps(plan, ensure_ascii=False, indent=1))
        return
    if a.output is None:
        ap.error('give an output folder (or --check-research)')
    out = a.output
    media = out / 'media'
    try:
        summary = check(data, preview=a.preview)
        # Board crops are cut from the original pixels before rendering; the delivered folder keeps crop-only copies.
        boards, board_files, board_warnings, delivered = board_images.prepare(
            data, a.input.resolve().parent, media, deliver=None if a.preview else out / 'board')
        rendered = {}
        for c in data['cards']:
            try:
                rendered[c['id']] = render_card(data, c, data['style'], boards.get(c['id']))
            except (DeckError, BlockError):
                raise
            except Exception as error:  # noqa: BLE001 - name the card instead of a bare traceback
                raise BlockError(f'card {c["id"]}: {type(error).__name__}: {error}') from error
    except (DeckError, BlockError, board_images.BoardError) as error:
        sys.exit(f'✗ {error}')

    out.mkdir(parents=True, exist_ok=True)
    media.mkdir(exist_ok=True)
    lexicon = data.get('speech_lexicon', {})
    plans, seen_terms, metrics, auto_speeds = {}, set(), {}, {}
    for card in data['cards']:
        r = rendered[card['id']]
        spoken = narration.apply_lexicon('\n'.join(t for _, t in r['parts']), lexicon)
        leaked = sorted(set(narration.TEX_REMNANT.findall(spoken)))
        if leaked:
            hint = 'write \\$ for a currency amount (read as 美元), or ' if leaked == ['$'] else ''
            sys.exit(f'✗ card {card["id"]}: narration still contains LaTeX ({" ".join(leaked)}); {hint}write the reading in 〔…〕 or give the block a speech')
        r['speed'], r['speed_reason'], metrics[card['id']], auto_speeds[card['id']] = choose_speed(card, data['style'], spoken, seen_terms)
        plans[card['id']] = narration.plan(card['id'], r['parts'], r['voice'], r['speed'], lexicon)
    slowed = [cid for cid in plans if rendered[cid]['speed'] < 2]
    if not a.preview and len(plans) >= 5 and len(slowed) > 0.3 * len(plans) and not data['style'].get('speed_review'):
        sys.exit(f'✗ {len(slowed)}/{len(plans)} cards are 1.5× (over 30%): run --preview, review them (report.json lists each reason) and, if this '
                 'deck really is that dense, say why in style.speed_review; otherwise set speed 2.0 with speed_reason on the cards that are not')
    cues, audio_report = {}, {}
    pending = a.preview or a.audio_pending
    if not pending:
        narration.require_tools()  # ffmpeg/ffprobe first: a missing tool is not a voice-service problem
        try:
            missing = narration.missing_originals(plans.values())
            if missing:
                preflight(missing[0][0])
            asyncio.run(narration.synthesize_clips(list(plans.values()), media, report=audio_report))
        except narration.ToolMissing as error:
            print(f'✗ {error}', file=sys.stderr)
            sys.exit(4)
        except Exception as error:  # noqa: BLE001 - explain, never substitute a voice
            sys.exit(f'✗ Narration failed: {error}\n  Run: python scripts/speech_backend.py --check --voice {next(iter(plans.values()))["voice"]}\n'
                     '  To deliver pages now, rebuild with --audio-pending and run this same command later where the voice service is reachable.')
        for cid, p in plans.items():
            cues[cid] = narration.assemble(p, media)
        if a.term_sampler:
            write_term_sampler(data, out, media, lexicon, plans.values())

    # The notetype carries every theme's CSS, so every theme's fonts ship: a later card in another theme never misses glyphs.
    css, fonts = bundle_fonts(asset_css(data.get('css', '')), sorted(t.stem for t in (ASSETS / 'themes').glob('*.css')))
    for source, hashed in fonts:
        (out / hashed).write_bytes(source.read_bytes())
    js = asset_js()
    template = '<div class="ccpt6-card" data-ccpt-single="1">{{Page}}</div><script>' + js + '</script>'
    deck_info = data['deck']
    model = genanki.Model(deck_info['model_id'], deck_info['model_name'], fields=[{'name': f} for f in FIELDS],
                          templates=[{'name': '单面阅读', 'qfmt': template, 'afmt': template, 'bqfmt': '{{Title}}', 'bafmt': '{{Title}}'}],
                          css=css, sort_field_index=1)
    decks, pages, report_cards = {}, {}, []
    for i, card in enumerate(data['cards']):
        r, p = rendered[card['id']], plans[card['id']]
        message = None
        if a.preview:
            message = '图文预览 · 语音未生成'
        elif a.audio_pending:
            message = '语音待补 · 见交付文件夹里的 补语音.txt'
        body = page(data, card, r, p['file'], cues.get(card['id']), message)
        pages[card['id']] = body
        name = deck_info['name'] + ('::' + card['subdeck'] if card.get('subdeck') else '')
        did = deck_info['deck_id'] if not card.get('subdeck') else subdeck_id(deck_info['deck_id'], name)
        deck = decks.setdefault(name, genanki.Deck(did, name))
        title_text = strip_tags(r['title_html'])
        tags = ['ccpt6', card['genre']] + ([re.sub(r'\W+', '_', data['exam']['code'])] if data.get('exam') else [])
        deck.add_note(genanki.Note(model=model, fields=[card['id'], title_text, body, source_record(data, card, r['speed'], r['speed_reason']), p['text']],
                                   guid=genanki.guid_for(deck_info['namespace'], card['id']), tags=tags, due=i + 1))
        preview = body.replace(f'data-audio="{p["file"]}"', f'data-audio="media/{p["file"]}"').replace(f'src="{p["file"]}"', f'src="media/{p["file"]}"')
        preview = preview.replace(f'src="{board_images.MEDIA_PREFIX}', f'src="media/{board_images.MEDIA_PREFIX}')
        (out / f'{card["id"]}.html').write_text(
            '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title_text)}</title><style>{css}</style><body class="card">{preview}<script>{js}</script></body></html>', encoding='utf-8')
        warn = []
        if 'speed' in card and float(card['speed']) != auto_speeds[card['id']]:
            warn.append(f'手动速度 {card["speed"]}× 与计算规则 {auto_speeds[card["id"]]}× 不同，确认理由')
        elif 'speed' not in card and data['style'].get('speed', 'auto') != 'auto' and r['speed'] != auto_speeds[card['id']]:
            warn.append(f'牌组固定 {r["speed"]:g}×，但规则判为 {auto_speeds[card["id"]]:g}×（{metrics[card["id"]]["auto_reason"] or "不够复杂"}）；默认请用 style.speed "auto"')
        nodes = len(re.findall(r'class="mm-node"', body))
        if nodes > 60:
            warn.append(f'导图 {nodes} 个节点，超过 60 个：拆成全景图加分支子图')
        warn += board_warnings.get(card['id'], [])
        warn += lint_card(card, data.get('academic', True), r['theme'], boards.get(card['id']))
        odd = narration.speech_lint(p['text'], lexicon)
        if odd:
            warn.append('朗读文本含难读符号 ' + ' '.join(odd) + '：改写成文字读法')
        report_cards.append({'id': card['id'], 'genre': card['genre'], 'title': title_text, 'speed': r['speed'], 'speed_reason': r['speed_reason'],
                             'voice': r['voice'], 'theme': r['theme'], 'segments': len(p['segments']), 'narration_chars': len(p['text']),
                             'duration': (cues.get(card['id']) or {}).get('duration'), 'metrics': metrics[card['id']],
                             'plain_math': len(plain_math(card)), 'warnings': warn})

    (out / 'pages.json').write_text(json.dumps(pages, ensure_ascii=False, indent=1), encoding='utf-8')
    manifest = [{'card': cid, 'file': p['file'], 'voice': p['voice'], 'speed': p['speed'], 'tempo_filter': narration.tempo_chain(p['speed']),
                 'segments': p['segments'], 'available': cid in cues, 'narration': cues.get(cid)} for cid, p in plans.items()]
    (out / 'speech-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding='utf-8')
    package = None
    if not a.preview:
        pkg = genanki.Package(list(decks.values()))
        pkg.media_files = ([str(out / hashed) for _, hashed in fonts] + [str(media / name) for name in board_files]
                           + ([] if a.audio_pending else [str(media / p['file']) for p in plans.values()]))
        safe = re.sub(r'[^\w一-鿿.-]+', '_', deck_info['name'])
        if len(safe) > 60:  # cut at a word boundary, not inside a word ("…_stati")
            cut = safe[:60]
            safe = cut[:cut.rfind('_')] if cut.rfind('_') > 20 else cut
        package = out / f'{safe}.apkg'
        pkg.write_to_file(str(package))
    write_addon(out)
    if not pending:
        (out / '补语音.txt').unlink(missing_ok=True)  # audio is complete now; the old note would mislead
    # The deck as built travels with every output: a later session continues from it, and 补语音.txt rebuilds from it.
    if not a.preview:
        # Board sources point at the crop-only copies in out/board/, so the folder rebuilds on its own.
        delivered_data = board_images.delivered_deck(data, a.input.resolve().parent, delivered) if board_files else data
        (out / 'deck.json').write_text(json.dumps(delivered_data, ensure_ascii=False, indent=1), encoding='utf-8')
    if a.audio_pending:
        (out / '补语音.txt').write_text(AUDIO_NOTE, encoding='utf-8')
        bundle_runtime(out)
    slow = [c for c in report_cards if c['speed'] < 2]
    deck_warnings = list(summary.get('warnings', []))
    speed_review = data['style'].get('speed_review', '')
    if len(report_cards) >= 5 and len(slow) > 0.3 * len(report_cards):
        listing = '；'.join(f'{c["id"]}（{c["speed_reason"] or "手动"}）' for c in slow[:12]) + ('…' if len(slow) > 12 else '')
        deck_warnings.append(f'{len(slow)}/{len(report_cards)} 张卡判为 1.5×，超过三成：' + (f'作者说明：{speed_review}' if speed_review else
                             '复核这些卡是否过密，确属整副都密时在 style.speed_review 写明理由并写进交付说明') + '。逐卡：' + listing)
    cov = summary.get('coverage') or {}
    if cov.get('undemanded'):
        deck_warnings.append('这些 core 考点没有出现在任何真题需求里（新考点或漏读真题？）：' + '、'.join(cov['undemanded']))
    if cov.get('adjacent'):
        deck_warnings.append('同节相邻、留给下一批的考点（交付时告诉用户）：' + '、'.join(cov['adjacent']))
    ledger = term_ledger(data, pages) if data.get('academic', True) else []
    if ledger:
        deck_warnings.append(f'术语台账 {len(ledger)} 个 English 词出现在卡上，但没有术语卡、就地释义（<abbr> 或“词（中文）”）或 terms_known（全量见 report.json，前 10 个）：'
                             + '、'.join(x['term'] for x in ledger[:10]))
    plain_known = [t for t in data.get('terms_known', []) if not isinstance(t, dict)]
    if plain_known:
        deck_warnings.append(f'terms_known 里有 {len(plain_known)} 个纯字符串：本卡组讲过的写成 {{"term", "taught_in": [卡 id]}}，功能词移到 ignore_words，其余在卡上就地释义')
    foreign = untranslated(pages) if data.get('academic', True) else {}
    if foreign:
        deck_warnings.append('这些卡有 8 个词以上的英文句子却没有中文：' + '、'.join(f'{cid}（{len(v)}）' for cid, v in foreign.items()))
    waivers = [{'card': c['id'], 'field': k, 'reason': v} for c in data['cards'] for k, v in c.items() if k.endswith('_waived')]
    if data.get('board_waived'):
        waivers.append({'card': None, 'field': 'board_waived', 'reason': data['board_waived']})
    if waivers:
        deck_warnings.append(f'{len(waivers)} 处豁免（*_waived），交付说明里列出：' + '、'.join(f'{w["card"]}.{w["field"]}' for w in waivers[:8]))
    cov = summary.get('coverage') or {}
    report = {'deck_warnings': deck_warnings, 'term_ledger': ledger, 'term_ledger_total': len(ledger), 'untranslated': foreign, 'waivers': waivers,
              'speed': {'slow': len(slow), 'cards': len(report_cards), 'speed_review': speed_review},
              'plain_math_total': sum(c['plain_math'] for c in report_cards), 'backcheck': cov.get('backcheck'), 'coldread': cov.get('coldread'),
              'cards': report_cards, 'summary': summary, 'audio': 'preview' if a.preview else 'pending' if a.audio_pending else 'complete',
              'package': package.name if package else None}
    (out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
    warnings = deck_warnings + [f'{c["id"]}: {w}' for c in report_cards for w in c['warnings']]
    print(json.dumps({'cards': len(report_cards), 'audio': report['audio'], 'package': report['package'], 'coverage': summary.get('coverage'),
                      'warnings': warnings}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
