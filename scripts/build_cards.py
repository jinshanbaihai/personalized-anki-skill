"""Build ccpt-6 exam knowledge cards: one complete page per card, one narration player.

Usage:
  python build_cards.py deck.json out/ --preview          # pages only, no audio, no package
  python build_cards.py deck.json out/                    # synthesize narration, write .apkg
  python build_cards.py deck.json out/ --audio-pending    # package now, narration filled later

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
import sys
from pathlib import Path

import genanki

from blocks import inline, render_block, esc, BlockError, strip_tags, REL_RULES, MATH
from deck_rules import check, GENRES, DeckError
from speech_backend import resolve_voice, inspect_voice, DEFAULT_VOICE
import narration
from package_addon import write_addon

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
    if card.get('tag'):
        return card['tag']
    exam = data.get('exam') or {}
    units = '/'.join(exam.get('units', [])[:2])
    return ' · '.join(x for x in (exam.get('code'), units) if x)


def render_card(data, card, style):
    where = f'card {card["id"]}'
    title = inline(card['title'], f'{where}.title')
    if title.unspoken and not card.get('title_speech'):
        raise BlockError(f'{where}.title: add 〔读法〕 after each formula or give title_speech')
    sections, parts = [], [(None, card.get('title_speech') or title.speech)]
    for i, block in enumerate(card['blocks']):
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
    # Anki stores fields as HTML; JSON escapes keep json.loads exact without HTML-escaping.
    return json.dumps(record, ensure_ascii=False).replace('<', r'\u003c').replace('>', r'\u003e').replace('&', r'\u0026')


def subdeck_id(base, name):
    return base + int(hashlib.sha256(name.encode()).hexdigest()[:6], 16)


def write_term_sampler(data, out, media, lexicon):
    """Edge cannot take phoneme hints, so the user hears every term once and fixes speech_lexicon if needed."""
    style = data['style']
    by_voice = {}
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


COMMON_EN = set('''a an the of to in on for and or is are be by with from as at it its this that these those than then not no can may must
which who what when where how per each all any one two three four five first second third more most less least very only also
both either neither such same other into onto over under above below between about after before during while because since
there here their they them then thus hence therefore however although though if else unless whether so do does did done
have has had having get gets got give given gives make makes made take takes taken use used uses using show shows shown write
written find found work works answer answers question questions value values number numbers part parts total marks mark
state states explain explains give gives calculate hence otherwise form forms correct simplest following below above
example examples note notes level levels card cards page step steps reason reasons true false yes
june january october november march may definition root'''.split())


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


def lint_card(card, academic=True):
    """Advisory checks that keep cards explained, readable and in the user's preferred shape."""
    out = []
    worked = card.get('genre') in ('derivation', 'method', 'formula')
    for b in card['blocks']:
        if not isinstance(b, dict):
            continue
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
        if b.get('type') == 'sections' and any(isinstance(i, dict) and len(plain(i.get('text', ''))) > 60 for i in b.get('items', [])):
            out.append('sections 有超过 60 字的长段：文科展开改用 chain 或 map 的箭头结构')
        if b.get('type') in ('lead', 'note') and card.get('genre') in ('chain', 'map', 'essay', 'overview') and len(plain(b.get('text', ''))) > 80:
            out.append(f'{b["type"]} 超过 80 字：因果展开写进 chain 或 map 的节点，不写成段落')
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
    return out


def term_ledger(data, pages):
    """English subject words on the cards that no term card, <abbr>, gloss or terms_known explains.
    Single words count too (externality, integrand, separable); words inside a definition's own sentence do not."""
    defined = set(k.lower() for k in data.get('terms_known', []))
    for c in data['cards']:
        for b in c['blocks']:
            if b.get('type') == 'definition':
                defined.add(strip_tags(inline(b['term'], 'ledger').html).lower())
    defined_words = {w for d in defined for w in re.findall(r'[a-z]+', d)}
    seen = {}
    for cid, body in pages.items():
        # chrome, citations and the definition sentence itself are not teaching vocabulary
        body = re.sub(r'<header[\s\S]*?</header>|<footer[\s\S]*?</footer>|<div hidden[\s\S]*?</div>', ' ', body)
        body = re.sub(r'<(p|span|div) class="(?:def-text|def-label|def-src|pf-src|tbl-cap|marks-basis)[^"]*"[^>]*>[\s\S]*?</\1>', ' ', body)
        body = re.sub(r'<math[\s\S]*?</math>', ' ', body)
        defined_here = {m.lower() for m in re.findall(r'<abbr[^>]*>(.*?)</abbr>', body)}
        visible = re.sub(r'<[^>]+>', ' ', body)  # a space at every tag boundary, so adjacent spans never merge
        visible = strip_tags(visible)
        # a gloss written right after the word counts as an explanation: integrand（被积函数）
        defined_here |= {m.lower() for m in re.findall(r'([A-Za-z][A-Za-z ]{2,40}?)\s*[（(][^）)]*[\u4e00-\u9fff][^）)]*[）)]', visible)}
        for phrase in re.findall(r'\b[A-Za-z][a-z]{3,}(?: [a-z]{2,}){0,2}\b|\b[A-Z]{2,5}\b', visible):
            words = [w for w in phrase.split() if w.lower() not in COMMON_EN]
            if not words:
                continue
            key = ' '.join(w if w.isupper() else w.lower() for w in words)
            if key.lower() in defined or key.lower() in defined_here or any(key.lower() in d for d in defined_here) \
                    or all(w.lower() in defined_words for w in words):
                continue
            seen.setdefault(key, set()).add(cid)
    ranked = sorted(seen.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    return [{'term': t, 'cards': sorted(c)} for t, c in ranked][:30]


def preflight(voice):
    """Fail fast with a clear class instead of hanging on a blocked network."""
    report = asyncio.run(inspect_voice(voice))
    if report['route'] != 'unavailable':
        return
    if report.get('edge_list_available') is False:
        print(f'✗ network_blocked: the Edge voice service could not be reached ({report.get("edge_error")}) and no Azure Speech is configured.\n'
              '  Deliver now with --audio-pending; run the same command without it on a machine that can reach speech.platform.bing.com.', file=sys.stderr)
        sys.exit(2)
    print(f'✗ voice_missing: {voice} is not offered by the Edge service; no voice was substituted.', file=sys.stderr)
    sys.exit(3)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('input', type=Path)
    ap.add_argument('output', type=Path)
    ap.add_argument('--preview', action='store_true', help='write preview pages only; no audio, no package')
    ap.add_argument('--audio-pending', action='store_true', help='package without narration; pages say so and the player is disabled')
    ap.add_argument('--term-sampler', action='store_true', help='also write term-sampler.mp3: every English term in a carrier sentence, for a one-minute pronunciation check')
    a = ap.parse_args(argv)

    data = json.loads(a.input.read_text(encoding='utf-8'))
    try:
        summary = check(data)
        rendered = {}
        for c in data['cards']:
            try:
                rendered[c['id']] = render_card(data, c, data['style'])
            except (DeckError, BlockError):
                raise
            except Exception as error:  # noqa: BLE001 - name the card instead of a bare traceback
                raise BlockError(f'card {c["id"]}: {type(error).__name__}: {error}') from error
    except (DeckError, BlockError) as error:
        sys.exit(f'✗ {error}')

    out = a.output
    media = out / 'media'
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
    cues, audio_report = {}, {}
    pending = a.preview or a.audio_pending
    if not pending:
        missing = narration.missing_originals(plans.values())
        if missing:
            preflight(missing[0][0])
        try:
            asyncio.run(narration.synthesize_clips(list(plans.values()), media, report=audio_report))
        except Exception as error:  # noqa: BLE001 - explain, never substitute a voice
            sys.exit(f'✗ Narration failed: {error}\n  Run: python scripts/speech_backend.py --check --voice {next(iter(plans.values()))["voice"]}\n'
                     '  To deliver pages now, rebuild with --audio-pending and run this same command later where the voice service is reachable.')
        for cid, p in plans.items():
            cues[cid] = narration.assemble(p, media)
        if a.term_sampler:
            write_term_sampler(data, out, media, lexicon)

    css, fonts = bundle_fonts(asset_css(data.get('css', '')), sorted({r['theme'] for r in rendered.values()}))
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
        warn += lint_card(card, data.get('academic', True))
        odd = narration.speech_lint(p['text'], lexicon)
        if odd:
            warn.append('朗读文本含难读符号 ' + ' '.join(odd) + '：改写成文字读法')
        report_cards.append({'id': card['id'], 'genre': card['genre'], 'title': title_text, 'speed': r['speed'], 'speed_reason': r['speed_reason'],
                             'voice': r['voice'], 'theme': r['theme'], 'segments': len(p['segments']), 'narration_chars': len(p['text']),
                             'duration': (cues.get(card['id']) or {}).get('duration'), 'metrics': metrics[card['id']], 'warnings': warn})

    (out / 'pages.json').write_text(json.dumps(pages, ensure_ascii=False, indent=1), encoding='utf-8')
    manifest = [{'card': cid, 'file': p['file'], 'voice': p['voice'], 'speed': p['speed'], 'tempo_filter': narration.tempo_chain(p['speed']),
                 'segments': p['segments'], 'available': cid in cues, 'narration': cues.get(cid)} for cid, p in plans.items()]
    (out / 'speech-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding='utf-8')
    package = None
    if not a.preview:
        pkg = genanki.Package(list(decks.values()))
        pkg.media_files = [str(out / hashed) for _, hashed in fonts] + ([] if a.audio_pending else [str(media / p['file']) for p in plans.values()])
        safe = re.sub(r'[^\w一-鿿.-]+', '_', deck_info['name'])[:60]
        package = out / f'{safe}.apkg'
        pkg.write_to_file(str(package))
    write_addon(out)
    if not pending:
        (out / '补语音.txt').unlink(missing_ok=True)  # audio is complete now; the old note would mislead
    if a.audio_pending:
        (out / 'deck.json').write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
        (out / '补语音.txt').write_text(
            '这个包先交付了图文，语音待补。在能访问 speech.platform.bing.com 的电脑上，进入本 skill 目录运行：\n\n'
            '  python scripts/build_cards.py <本文件夹>/deck.json <本文件夹>\n\n'
            '生成的新 .apkg 导入 Anki 即可原位补上语音（同一张卡，复习记录保留）。\n', encoding='utf-8')
    slow = [c for c in report_cards if c['speed'] < 2]
    deck_warnings = []
    if len(report_cards) >= 5 and len(slow) > 0.3 * len(report_cards):
        deck_warnings.append(f'{len(slow)}/{len(report_cards)} 张卡判为 1.5×，超过三成：复核速度规则或卡片是否过密')
    cov = summary.get('coverage') or {}
    if cov.get('undemanded'):
        deck_warnings.append('这些 core 考点没有出现在任何真题需求里（新考点或漏读真题？）：' + '、'.join(cov['undemanded']))
    if cov.get('adjacent'):
        deck_warnings.append('同节相邻、留给下一批的考点（交付时告诉用户）：' + '、'.join(cov['adjacent']))
    ledger = term_ledger(data, pages) if data.get('academic', True) else []
    if ledger:
        deck_warnings.append('这些 English 词出现在卡上，但没有术语卡、就地释义（<abbr> 或“词（中文）”）或 terms_known：' + '、'.join(x['term'] for x in ledger[:10]))
    report = {'deck_warnings': deck_warnings, 'term_ledger': ledger, 'cards': report_cards, 'summary': summary, 'audio': 'preview' if a.preview else 'pending' if a.audio_pending else 'complete',
              'package': str(package) if package else None}
    (out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
    warnings = deck_warnings + [f'{c["id"]}: {w}' for c in report_cards for w in c['warnings']]
    print(json.dumps({'cards': len(report_cards), 'audio': report['audio'], 'package': report['package'], 'coverage': summary.get('coverage'),
                      'warnings': warnings}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
