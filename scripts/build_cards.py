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

from blocks import inline, render_block, esc, BlockError, strip_tags
from deck_rules import check, GENRES, DeckError
from speech_backend import resolve_voice, DEFAULT_VOICE, DEFAULT_SPEED
import narration

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets' / 'ccpt6'
FIELDS = ['StableID', 'Title', 'Page', 'Source', 'Narration']
KEYS_HINT = 'Space 播音 · Enter 继续 · 1 明天再看'


def asset_css(extra=''):
    parts = [(ASSETS / 'base.css').read_text()]
    parts += [p.read_text() for p in sorted((ASSETS / 'themes').glob('*.css'))]
    return '\n'.join(parts) + ('\n' + extra if extra else '')


def asset_js():
    # Layout first: the player calls window.ccptLayout once the page is wired.
    return '\n'.join((ASSETS / name).read_text() for name in ('layout.js', 'player.js')) + '\n' + (ROOT / 'assets' / 'single-face.js').read_text()


def card_tag(data, card):
    if card.get('tag'):
        return card['tag']
    exam = data.get('exam') or {}
    units = '/'.join(exam.get('units', [])[:2])
    return ' · '.join(x for x in (exam.get('code'), units) if x)


def complexity(page_html, card):
    maths = page_html.count('<math')
    steps = sum(len(b.get('items', [])) for b in card['blocks'] if b.get('type') == 'steps')
    depth = max([int(d) for d in re.findall(r'data-depth="(\d+)"', page_html)] or [0])
    chars = len(strip_tags(page_html))
    complex_ = (steps >= 5 and maths >= 6) or maths >= 14 or depth >= 5 or chars >= 1500
    return {'math': maths, 'steps': steps, 'map_depth': depth, 'visible_chars': chars, 'suggest_slower': complex_}


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
    voice = resolve_voice(card.get('voice') or style.get('voice') or DEFAULT_VOICE)
    speed = float(card.get('speed', style.get('speed', DEFAULT_SPEED)))
    theme = card.get('theme') or style.get('theme', 'editorial')
    return {'title_html': title.html, 'sections': sections, 'parts': parts, 'voice': voice, 'speed': speed, 'theme': theme}


def page(data, card, r, audio_name, cues, pending_message=None):
    genre = card['genre']
    speed_label = f'{r["speed"]:g}×'
    voice_label = {'zh-CN-XiaoxiaoNeural': '晓晓', 'zh-CN-YunyangNeural': '云扬', 'zh-CN-YunxiNeural': '云希'}.get(r['voice'], r['voice'])
    attrs = f'class="ccpt6" data-ccpt-single="1" data-side="read" data-theme="{esc(r["theme"])}" data-genre="{esc(genre)}" data-note="{esc(card["id"])}"'
    if pending_message:
        attrs += f' data-audio-pending="1" data-audio-message="{esc(pending_message)}"'
    player = (f'<button class="speak" data-audio="{"" if pending_message else esc(audio_name)}" aria-label="整页讲解：播放、暂停或继续" aria-pressed="false"'
              + (f' disabled title="{esc(pending_message)}"' if pending_message else '') + '>▶</button>'
              f'<button class="speed" type="button" data-speed="{r["speed"]:g}" data-encoded="{r["speed"]:g}" title="点击在 2× 与 1.5× 之间切换">{speed_label}</button>')
    status = esc(pending_message) if pending_message else f'{voice_label} · {speed_label}'
    out = (f'<main {attrs}><header class="cc-head"><div class="cc-meta"><span class="cc-genre">{GENRES[genre]}</span>'
           f'<span class="cc-tag">{esc(card_tag(data, card))}</span></div>'
           f'<div class="cc-titlebar"><h1 data-node="title">{r["title_html"]}</h1><div class="cc-player">{player}</div></div></header>'
           f'<article class="cc-body">{"".join(r["sections"])}</article>'
           f'<footer class="cc-foot"><span class="audio-status">{status}</span><span class="keys">{KEYS_HINT if not pending_message else "Enter 继续 · 1 明天再看"}</span></footer>')
    payload = json.dumps({'narration': cues}, ensure_ascii=False)
    out += f'<div hidden class="cc-data">{esc(payload)}</div>'
    src = '' if pending_message else ' src="' + esc(audio_name) + '"'
    out += f'<audio preload="none"{src}></audio></main>'
    return out


def source_record(data, card):
    record = {'schema': 'ccpt-6', 'card': card['id'], 'covers': card.get('covers', []), 'sources': card.get('sources', []),
              'exam': data.get('exam'), 'coverage_scope': (data.get('coverage') or {}).get('scope')}
    if card.get('speed_reason'):
        record['speed_reason'] = card['speed_reason']
    # Anki stores fields as HTML; JSON escapes keep json.loads exact without HTML-escaping.
    return json.dumps(record, ensure_ascii=False).replace('<', r'<').replace('>', r'>').replace('&', r'&')


def subdeck_id(base, name):
    return base + int(hashlib.sha256(name.encode()).hexdigest()[:6], 16)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('input', type=Path)
    ap.add_argument('output', type=Path)
    ap.add_argument('--preview', action='store_true', help='write preview pages only; no audio, no package')
    ap.add_argument('--audio-pending', action='store_true', help='package without narration; pages say so and the player is disabled')
    a = ap.parse_args(argv)

    data = json.loads(a.input.read_text())
    try:
        summary = check(data)
        rendered = {c['id']: render_card(data, c, data['style']) for c in data['cards']}
    except (DeckError, BlockError) as error:
        sys.exit(f'✗ {error}')

    out = a.output
    media = out / 'media'
    out.mkdir(parents=True, exist_ok=True)
    media.mkdir(exist_ok=True)
    plans = {cid: narration.plan(cid, r['parts'], r['voice'], r['speed']) for cid, r in rendered.items()}
    cues, audio_report = {}, {}
    pending = a.preview or a.audio_pending
    if not pending:
        try:
            asyncio.run(narration.synthesize_clips(list(plans.values()), media, report=audio_report))
        except Exception as error:  # noqa: BLE001 - explain, never substitute a voice
            sys.exit(f'✗ Narration failed: {error}\n  Run: python scripts/speech_backend.py --check --voice {next(iter(plans.values()))["voice"]}\n'
                     '  To deliver pages now, rebuild with --audio-pending and fill narration later on a machine that can reach the voice service.')
        for cid, p in plans.items():
            cues[cid] = narration.assemble(p, media)

    css = asset_css(data.get('css', ''))
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
            message = '语音待补 · 本机运行生成器即可补齐'
        body = page(data, card, r, p['file'], cues.get(card['id']), message)
        pages[card['id']] = body
        name = deck_info['name'] + ('::' + card['subdeck'] if card.get('subdeck') else '')
        did = deck_info['deck_id'] if not card.get('subdeck') else subdeck_id(deck_info['deck_id'], name)
        deck = decks.setdefault(name, genanki.Deck(did, name))
        title_text = strip_tags(r['title_html'])
        tags = ['ccpt6', card['genre']] + ([re.sub(r'\W+', '_', data['exam']['code'])] if data.get('exam') else [])
        deck.add_note(genanki.Note(model=model, fields=[card['id'], title_text, body, source_record(data, card), p['text']],
                                   guid=genanki.guid_for(deck_info['namespace'], card['id']), tags=tags, due=i + 1))
        preview = body.replace(f'data-audio="{p["file"]}"', f'data-audio="media/{p["file"]}"').replace(f'src="{p["file"]}"', f'src="media/{p["file"]}"')
        (out / f'{card["id"]}.html').write_text(
            '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title_text)}</title><style>{css}</style><body class="card">{preview}<script>{js}</script></body></html>')
        stats = complexity(body, card)
        warn = []
        if stats['suggest_slower'] and r['speed'] > 1.5:
            warn.append('内容密度高，考虑 speed 1.5 并写 speed_reason')
        odd = narration.speech_lint(p['text'])
        if odd:
            warn.append('朗读文本含难读符号 ' + ' '.join(odd) + '：改写成文字读法')
        report_cards.append({'id': card['id'], 'genre': card['genre'], 'title': title_text, 'speed': r['speed'], 'voice': r['voice'],
                             'theme': r['theme'], 'segments': len(p['segments']), 'narration_chars': len(p['text']), **stats, 'warnings': warn})

    (out / 'pages.json').write_text(json.dumps(pages, ensure_ascii=False, indent=1))
    manifest = [{'card': cid, 'file': p['file'], 'voice': p['voice'], 'speed': p['speed'], 'tempo_filter': narration.tempo_chain(p['speed']),
                 'segments': p['segments'], 'available': cid in cues, 'narration': cues.get(cid)} for cid, p in plans.items()]
    (out / 'speech-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
    package = None
    if not a.preview:
        pkg = genanki.Package(list(decks.values()))
        pkg.media_files = [] if a.audio_pending else [str(media / p['file']) for p in plans.values()]
        safe = re.sub(r'[^\w一-鿿.-]+', '_', deck_info['name'])[:60]
        package = out / f'{safe}.apkg'
        pkg.write_to_file(str(package))
    report = {'cards': report_cards, 'summary': summary, 'audio': 'preview' if a.preview else 'pending' if a.audio_pending else 'complete',
              'package': str(package) if package else None}
    (out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=1))
    warnings = [f'{c["id"]}: {w}' for c in report_cards for w in c['warnings']]
    print(json.dumps({'cards': len(report_cards), 'audio': report['audio'], 'package': report['package'], 'coverage': summary.get('coverage'),
                      'warnings': warnings}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
