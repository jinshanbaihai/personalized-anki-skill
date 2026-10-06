"""Regression tests for the ccpt-6 builder. Synthetic content checks structure, not teaching quality."""
import copy
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import pytest

import blocks
import build_cards
import deck_rules
import narration
from validate_package import inspect_page

ROOT = Path(__file__).resolve().parent.parent


def deck():
    return {
        'schema': 'ccpt-6',
        'deck': {'name': 'CCPT6 test', 'deck_id': 1790000000101, 'model_id': 1790000000102, 'model_name': 'CCPT6 test', 'namespace': 'ccpt6-test'},
        'style': {'theme': 'lab', 'voice': 'xiaoxiao'},
        'exam': {'board': 'Pearson Edexcel', 'qualification': 'IAL Mathematics', 'code': 'YMA01', 'units': ['WST02'],
                 'spec_version': 'Issue 3 (April 2019)', 'spec_url': 'https://example.invalid/spec.pdf',
                 'identified_by': 'exclusive-content', 'evidence': ['synthetic evidence'], 'session': 'January 2027',
                 'ruled_out': [{'candidate': 'UK 9MA0', 'why_not': 'synthetic reason'}]},
        'research': [
            {'type': 'spec', 'ref': 'synthetic spec', 'read': 'p.59', 'used_for': 'scope'},
            {'type': 'ms', 'ref': 'synthetic MS', 'read': 'Q2', 'used_for': 'keywords'},
            {'type': 'er', 'ref': 'synthetic ER', 'read': 'Q2', 'used_for': 'pitfalls'},
        ],
        'board': [{'id': 'B01', 'where': 'p1', 'point': 'statistic definition', 'items': ['S-1']}],
        'coverage': {'scope': 'synthetic 4.2', 'status': 'complete', 'remaining': '', 'items': [
            {'id': 'S-1', 'spec': '4.2', 'point': 'statistic', 'class': 'core', 'level': 'MS keywords', 'kind': 'term',
             'evidence': ['WST02 Jan 2025 Q2 MS', 'WST02 Jun 2023 ER Q2']},
            {'id': 'X-1', 'spec': 'S3 3.6', 'point': 'CLT', 'class': 'excluded', 'reason': 'other unit'}]},
        'cards': [{
            'id': 'T01', 'genre': 'term', 'title': 'Statistic', 'covers': ['S-1'], 'sources': ['synthetic'],
            'blocks': [
                {'type': 'lead', 'text': '只用样本就能算出的量'},
                {'type': 'definition', 'term': 'Statistic', 'text': 'A quantity calculated only from the sample, containing no unknown parameters.',
                 'keywords': ['only from the sample', 'no unknown parameters'], 'reject': ['because it is known']},
                {'type': 'examples', 'yes': [{'text': 'sample mean', 'why': 'only sample values'}], 'no': [{'text': 'population mean', 'why': 'unknown parameter'}]},
                {'type': 'steps', 'items': [{'do': '$\\frac{9}{245}$〔245 分之 9〕', 'why': '不放回', 'mark': 'B1'}]},
                {'type': 'map', 'root': {'text': 'root', 'children': [{'text': 'a', 'rel': '导致', 'children': [{'text': 'b', 'rel': '所以'}]}]}},
            ]}],
    }


def test_inline_math_needs_spoken_form():
    with pytest.raises(blocks.BlockError, match='spoken form'):
        blocks.render_block({'type': 'lead', 'text': 'x = $\\frac12$'}, 'b0', 'w')
    html, parts = blocks.render_block({'type': 'lead', 'text': 'x = $\\frac12$〔二分之一〕'}, 'b0', 'w')
    assert '<math' in html and parts[0].text.endswith('二分之一')


def test_block_speech_override_allows_unspoken_math():
    html, parts = blocks.render_block({'type': 'lead', 'text': '$\\frac12$', 'speech': '一半'}, 'b0', 'w')
    assert parts[0].text == '一半'


def test_keywords_must_appear_verbatim():
    with pytest.raises(blocks.BlockError, match='verbatim'):
        blocks.render_block({'type': 'definition', 'term': 'X', 'text': 'abc', 'keywords': ['zzz']}, 'b0', 'w')


def test_steps_need_reasons_and_valid_marks():
    with pytest.raises(blocks.BlockError, match='explain each step'):
        blocks.render_block({'type': 'steps', 'items': [{'do': 'x'}]}, 'b0', 'w')
    with pytest.raises(blocks.BlockError, match='mark-scheme notation'):
        blocks.render_block({'type': 'steps', 'items': [{'do': 'x', 'why': 'y', 'mark': 'two marks'}]}, 'b0', 'w')
    html, parts = blocks.render_block({'type': 'steps', 'items': [{'do': 'x', 'why': 'y', 'mark': 'dM1'}, {'do': 'z', 'basis': 'w', 'mark': 'A1 A1'}]}, 'b0', 'w')
    assert [p.target for p in parts] == ['b0-s0', 'b0-s1'] and 'dM1' in html


def test_literal_less_than_is_rejected():
    with pytest.raises(blocks.BlockError):
        blocks.render_block({'type': 'lead', 'text': 'MSB<MSC 时'}, 'b0', 'w')


def test_active_content_is_rejected():
    for markup in ('<script>x</script>', '<img src="https://x/y.png">', '<span onclick="x()">a</span>'):
        with pytest.raises(blocks.BlockError):
            blocks.render_block({'type': 'html', 'html': markup, 'speech': 'x'}, 'b0', 'w')


def test_map_depth_and_parts():
    root = {'text': 'r', 'children': [{'text': f'c{i}', 'rel': '导致', 'children': [{'text': 'g', 'children': [{'text': 'gg', 'kind': 'evaluation'}]}]} for i in range(3)]}
    html, parts = blocks.render_block({'type': 'map', 'root': root}, 'b0', 'w')
    assert 'data-depth="3"' in html and len(parts) == 4  # root + one part per first-level branch


def test_deck_rules_accept_valid_deck():
    summary = deck_rules.check(deck())
    assert summary['coverage']['missing'] == []


@pytest.mark.parametrize('mutate, message', [
    (lambda d: d.pop('exam'), 'lock the exact exam'),
    (lambda d: d['exam'].update(ruled_out=[]), 'near-miss'),
    (lambda d: d['research'].pop(1), 'mark schemes'),
    (lambda d: d['cards'][0].update(covers=['X-1']), 'excluded'),
    (lambda d: d['coverage']['items'].append({'id': 'S-2', 'spec': '4.1', 'point': 'frame', 'class': 'core', 'level': 'x', 'kind': 'term', 'evidence_gap': 'x'}), 'no card'),
    (lambda d: d['exam'].pop('session'), 'exam.session'),
    (lambda d: d['coverage']['items'][0].pop('kind'), 'kind'),
    (lambda d: d['coverage']['items'][0].update(evidence=['one']), 'two past-paper'),
    (lambda d: d['coverage']['items'][0].pop('level'), 'level'),
    (lambda d: d['board'][0].update(items=[]), 'maps to no syllabus point'),
    (lambda d: d['cards'][0].update(speed=1.5), 'complex enough'),
    (lambda d: d['style'].update(speed=3), 'style.speed'),
    (lambda d: d['style'].update(speed=1.5), 'speed_reason'),
    (lambda d: d.update(speech_lexicon={'λ': 3}), 'speech_lexicon'),
])
def test_deck_rules_reject(mutate, message):
    d = deck()
    mutate(d)
    with pytest.raises(deck_rules.DeckError, match=message):
        deck_rules.check(d)


def test_existing_card_counts_as_coverage():
    d = deck()
    d['coverage']['items'].append({'id': 'S-2', 'spec': '4.1', 'point': 'frame', 'class': 'core', 'level': 'x', 'kind': 'term', 'evidence_gap': 'x', 'existing': 'IAL S2::T07'})
    assert deck_rules.check(d)['coverage']['missing'] == []


def test_partial_needs_remaining():
    d = deck()
    d['coverage']['status'] = 'partial'
    with pytest.raises(deck_rules.DeckError, match='remaining'):
        deck_rules.check(d)


def test_tempo_chain():
    assert narration.tempo_chain(2.0) == 'atempo=2'
    assert narration.tempo_chain(1.5) == 'atempo=1.5'
    assert narration.tempo_chain(3.0) == 'atempo=2.0,atempo=1.5'


def test_speed_and_voice_change_audio_names():
    a = narration.plan('c', [(None, '你好')], 'xiaoxiao', 2.0)
    b = narration.plan('c', [(None, '你好')], 'xiaoxiao', 1.5)
    c = narration.plan('c', [(None, '你好')], 'yunyang', 2.0)
    assert len({a['file'], b['file'], c['file']}) == 3 and a['voice'] == 'zh-CN-XiaoxiaoNeural'


@pytest.mark.skipif(not shutil.which('ffmpeg'), reason='ffmpeg needed')
def test_assemble_measures_cues(tmp_path):
    p = narration.plan('c', [(None, 'a'), ('b0', 'b')], 'xiaoxiao', 2.0)
    for i, s in enumerate(p['segments']):
        subprocess.run(['ffmpeg', '-v', 'error', '-f', 'lavfi', '-i', f'sine=frequency=440:duration={1 + i}', '-ar', '24000', '-ac', '1',
                        '-codec:a', 'libmp3lame', str(tmp_path / s['file'])], check=True)
    result = narration.assemble(p, tmp_path)
    cues = result['cues']
    assert [c['target'] for c in cues] == [None, 'b0'] and cues[1]['start'] > cues[0]['end']
    assert abs(result['duration'] - narration.duration(tmp_path / p['file'])) < 0.15


def test_preview_and_pending_package(tmp_path):
    src = tmp_path / 'deck.json'
    src.write_text(json.dumps(deck(), ensure_ascii=False))
    build_cards.main([str(src), str(tmp_path / 'preview'), '--preview'])
    page = (tmp_path / 'preview' / 'T01.html').read_text()
    assert 'data-theme="lab"' in page and '<math' in page and 'mark class="kw"' in page
    build_cards.main([str(src), str(tmp_path / 'pending'), '--audio-pending'])
    pages = json.loads((tmp_path / 'pending' / 'pages.json').read_text())
    assert inspect_page(pages['T01'], allow_pending=True) is None
    with pytest.raises(AssertionError, match='Audio pending'):
        inspect_page(pages['T01'])
    report = json.loads((tmp_path / 'pending' / 'report.json').read_text())
    assert report['audio'] == 'pending' and list((tmp_path / 'pending').glob('*.apkg'))


def test_source_field_round_trips():
    d = deck()
    d['cards'][0]['sources'] = ['MSB < MSC & P > Q']
    raw = build_cards.source_record(d, d['cards'][0], 2.0)
    assert '<' not in raw and '&' not in raw and '>' not in raw
    assert json.loads(raw)['sources'] == ['MSB < MSC & P > Q'] and json.loads(raw)['exam'] == 'YMA01 WST02'


def test_note_fields_are_frozen():
    """Changing fields would stop in-place updates of every existing card."""
    assert build_cards.FIELDS == ['StableID', 'Title', 'Page', 'Source', 'Narration']


def test_themes_define_light_and_night_tokens():
    for css in (ROOT / 'assets/ccpt6/themes').glob('*.css'):
        text = css.read_text()
        name = css.stem
        assert f'.ccpt6[data-theme="{name}"]' in text and f'.nightMode .ccpt6[data-theme="{name}"]' in text
        assert name in deck_rules.THEMES


# Comparisons from real economics boards that were once swallowed as HTML tags.
SWALLOWED = ['若 MSB<MSC，多一单位反而净损失，应该减少。', '<strong>MSC<MPC，MPB=MSB</strong>', 'Qm<Q*：少做的那些单位原本 MSB>MSC。',
             'Qm<Q*。红线是 <strong>MPC−subsidy</strong>。', 'MSC<MPC，MPB=MSB。企业得不到全部社会 benefit，市场停在较低 Qm。']


@pytest.mark.parametrize('text', SWALLOWED)
def test_board_comparisons_must_be_escaped(text):
    with pytest.raises(blocks.BlockError):
        blocks.render_block({'type': 'lead', 'text': text}, 'b0', 'w')
    html, parts = blocks.render_block({'type': 'lead', 'text': text.replace('<M', '&lt;M').replace('<Q', '&lt;Q')}, 'b0', 'w')
    assert '&lt;' in html and '<' in parts[0].text


def test_quiz_attributes_are_not_default_cards():
    base = '<main data-side="read"><button class="speak" data-audio="ccpt_x.mp3">▶</button><audio src="ccpt_x.mp3"></audio>{}</main>'
    assert inspect_page(base.format('<p>说明中可以出现 <code>data-choice</code>。</p>')) == 'ccpt_x.mp3'
    with pytest.raises(AssertionError, match='quiz attributes'):
        inspect_page(base.format('<div data-choice="A">choice</div>'))


@pytest.mark.skipif(not shutil.which('ffmpeg'), reason='ffmpeg needed')
def test_full_audio_pipeline_offline(tmp_path, monkeypatch):
    """Replace only the network voice with a local tone; tempo, joining, cues, packaging stay real."""
    async def fake_voice(text, voice, output):
        seconds = max(0.6, len(text) / 8)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', f'sine=frequency=330:duration={seconds}', '-ar', '24000', '-ac', '1',
                        '-codec:a', 'libmp3lame', str(output)], check=True)
        return 'test-tone'
    monkeypatch.setattr(narration, 'synthesize_original', fake_voice)
    monkeypatch.setattr(build_cards, 'preflight', lambda voice: None)
    monkeypatch.setenv('CCPT_TTS_CACHE', str(tmp_path / 'tts-cache'))
    d = deck()
    d['cards'][0]['speed'] = 1.5
    d['cards'][0]['speed_reason'] = 'test'
    src = tmp_path / 'deck.json'
    src.write_text(json.dumps(d, ensure_ascii=False))
    build_cards.main([str(src), str(tmp_path / 'out')])
    manifest = json.loads((tmp_path / 'out' / 'speech-manifest.json').read_text())[0]
    assert manifest['available'] and manifest['speed'] == 1.5 and manifest['tempo_filter'] == 'atempo=1.5'
    cues = manifest['narration']['cues']
    assert cues[0]['target'] is None and [c['target'] for c in cues][1:5] == ['b0', 'b1', 'b2-yes0', 'b2-no0']
    page = json.loads((tmp_path / 'out' / 'pages.json').read_text())['T01']
    assert inspect_page(page) == manifest['file'] and 'data-encoded="1.5"' in page
    # Designed pauses: 0.5 s after the title and between blocks, 0.3 s inside a block.
    gaps = [round(b['start'] - a['end'], 2) for a, b in zip(cues, cues[1:])]
    assert gaps[0] == 0.5 and 0.3 in gaps
    # Originals are cached without speed: a 2× rebuild needs no new synthesis.
    calls = []
    async def counting_voice(text, voice, output):
        calls.append(text)
        return await fake_voice(text, voice, output)
    monkeypatch.setattr(narration, 'synthesize_original', counting_voice)
    d['cards'][0]['speed'] = 2.0
    src.write_text(json.dumps(d, ensure_ascii=False))
    build_cards.main([str(src), str(tmp_path / 'out2')])
    assert calls == [] and json.loads((tmp_path / 'out2' / 'speech-manifest.json').read_text())[0]['speed'] == 2.0


def test_speed_rule_ignores_visible_structure():
    chain = {'genre': 'chain', 'title': 'x', 'blocks': [{'type': 'chain', 'items': [{'text': 'a'}] + [{'rel': r, 'text': 'b'} for r in ('所以', '因此', '从而', '仅当', '但是')]}]}
    assert narration.decide_speed(narration.speed_metrics(chain, '因果' * 80, set()))[0] == 2.0
    table = {'genre': 'term', 'title': 'x', 'blocks': [{'type': 'definition', 'term': 'X', 'text': 'y'},
             {'type': 'table', 'head': ['m', 'P'], 'rows': [['4', '9/245'], ['5.5', '6/49'], ['7', '71/245'], ['8.5', '15/49'], ['10', '12/49']]}]}
    assert narration.decide_speed(narration.speed_metrics(table, '分布' * 80, set()))[0] == 2.0


def test_speed_rule():
    dense = {'genre': 'derivation', 'title': 'x', 'blocks': [{'type': 'steps', 'items': [
        {'do': f'$x^{i}$〔x 的 {i} 次方〕', 'why': 'w'} for i in range(5)]}]}
    m = narration.speed_metrics(dense, '讲解' * 40, set())
    assert narration.decide_speed(m)[0] == 1.5 and '5 步推导' in narration.decide_speed(m)[1]
    term = {'genre': 'term', 'title': 'Statistic', 'blocks': [{'type': 'definition', 'term': 'Statistic', 'text': 'A quantity'}]}
    assert narration.decide_speed(narration.speed_metrics(term, '一个只用样本算出来的量' * 30, set()))[0] == 2.0
    proof = {'genre': 'derivation', 'title': 'Proof by contradiction', 'blocks': [{'type': 'steps', 'items': [{'do': 'a', 'why': 'b'}] * 3}]}
    assert narration.decide_speed(narration.speed_metrics(proof, '证明', set()))[1] == '证明结构'


def test_lexicon_and_lint():
    assert narration.apply_lexicon('r = a + λ b，e.g. vs', {'ILATE': 'I L A T E'}) == 'r = a + lambda b，例如 对比'
    assert narration.apply_lexicon('x = −2，MPC − s', {}) == 'x = 负2，MPC 减 s'
    assert narration.apply_lexicon('use ILATE', {'ILATE': 'I L A T E'}) == 'use I L A T E'
    assert narration.speech_lint('MU/P') == ['MU/P']


def test_term_and_derivation_structure():
    d = deck()
    d['cards'][0]['blocks'] = [b for b in d['cards'][0]['blocks'] if b['type'] != 'examples']
    with pytest.raises(deck_rules.DeckError, match='non-example'):
        deck_rules.check(d)
    d['cards'][0]['examples_waived'] = 'no natural non-example'
    deck_rules.check(d)
    d = deck()
    d['cards'][0]['genre'] = 'derivation'
    with pytest.raises(deck_rules.DeckError, match='finish block'):
        deck_rules.check(d)
    d = deck()
    d['cards'][0]['genre'] = 'overview'
    with pytest.raises(deck_rules.DeckError, match='own term card'):
        deck_rules.check(d)


def test_voice_is_per_deck():
    d = deck()
    d['cards'][0]['voice'] = 'yunyang'
    with pytest.raises(deck_rules.DeckError, match='per deck'):
        deck_rules.check(d)


def test_subgoal_and_trivial_steps():
    html, parts = blocks.render_block({'type': 'steps', 'items': [
        {'subgoal': '把括号首项化成 1', 'do': 'a', 'why': 'b'}, {'subgoal': '把括号首项化成 1', 'do': 'c', 'trivial': True},
        {'subgoal': '代入公式', 'do': 'e', 'basis': 'f'}]}, 'b0', 'w')
    assert html.count('class="subgoal"') == 2 and 'step trivial' in html
    assert parts[0].text.startswith('把括号首项化成 1') and not parts[1].text.startswith('把括号')


def test_tidy_latex():
    assert blocks.tidy_latex(r'|x|<\frac14') == r'\left|x\right|<\frac14'
    assert blocks.tidy_latex(r'P(A|B)+P(C|D)') == r'P(A|B)+P(C|D)'
    assert blocks.tidy_latex(r'(-\frac23)') == r'({-}\frac23)'


def test_svg_colours_follow_theme():
    ok = '<svg viewBox="0 0 10 10"><line class="ax" x1="0" y1="0" x2="5" y2="5"/><rect fill="none" stroke="var(--ink)" width="1" height="1"/></svg>'
    blocks.render_block({'type': 'figure', 'svg': ok, 'caption': 'x'}, 'b0', 'w')
    with pytest.raises(blocks.BlockError, match='night mode'):
        blocks.render_block({'type': 'figure', 'svg': '<svg viewBox="0 0 10 10"><line stroke="#000" x1="0" y1="0" x2="5" y2="5"/></svg>', 'caption': 'x'}, 'b0', 'w')


def test_math_punctuation_nowrap_is_local():
    html, _ = blocks.render_block({'type': 'lead', 'text': '甲 $a$〔a〕可以；而 $b$〔b〕含 $c$〔c〕，不是'}, 'b0', 'w')
    assert html.count('class="nw"') == 1
    inner = html.split('class="nw">', 1)[1].split('，</span>', 1)[0]
    assert inner.count('class="math"') == 1


def test_theme_contrast_meets_wcag():
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/contrast_check.py')], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout[-800:]


def test_css_stays_within_anki_engines():
    """Anki 25.02 ships Chromium 112: no CSS nesting, light-dark(), color-mix() or container queries."""
    for css in [ROOT / 'assets/ccpt6/base.css', *(ROOT / 'assets/ccpt6/themes').glob('*.css')]:
        text = re.sub(r'/\*[\s\S]*?\*/', '', css.read_text())
        for banned in ('light-dark(', 'color-mix(', '@container'):
            assert banned not in text, f'{css.name} uses {banned}'
        assert not re.search(r'{[^{}]*&', text), f'{css.name} uses CSS nesting'
    for css in (ROOT / 'assets/ccpt6/themes').glob('*.css'):
        text = css.read_text()
        assert f'.night_mode .ccpt6[data-theme="{css.stem}"]' in text and f'.nightMode.card:has(.ccpt6[data-theme="{css.stem}"])' in text


def test_fonts_are_bundled_with_content_hashes(tmp_path):
    src = tmp_path / 'deck.json'
    src.write_text(json.dumps(deck(), ensure_ascii=False))
    build_cards.main([str(src), str(tmp_path / 'out'), '--audio-pending'])
    fonts = sorted(p.name for p in (tmp_path / 'out').glob('_ccpt6-*.woff2'))
    assert fonts and all(re.fullmatch(r'_ccpt6-[\w-]+\.[0-9a-f]{8}\.woff2', f) for f in fonts)
    with zipfile.ZipFile(next((tmp_path / 'out').glob('*.apkg'))) as z:
        names = json.loads(z.read('media')).values()
    assert set(fonts) <= set(names)


def test_in_place_update_keeps_history(tmp_path):
    """v1 → study → v2 with new wording and CSS: content updates, schedule and review log stay."""
    anki = pytest.importorskip('anki.collection')
    from anki import import_export_pb2
    from anki.scheduler.v3 import CardAnswer
    d = deck()
    src = tmp_path / 'deck.json'
    src.write_text(json.dumps(d, ensure_ascii=False))
    build_cards.main([str(src), str(tmp_path / 'v1'), '--audio-pending'])
    path = str(tmp_path / 'c.anki2')
    col = anki.Collection(path)

    def load(folder):
        req = import_export_pb2.ImportAnkiPackageRequest(package_path=str(next((tmp_path / folder).glob('*.apkg'))),
                                                         options=import_export_pb2.ImportAnkiPackageOptions(with_scheduling=False))
        col.import_anki_package(req)
    load('v1')
    cid = col.find_cards('')[0]
    col.decks.select(col.get_card(cid).did)
    queued = col.sched.get_queued_cards().cards[0]
    card = col.get_card(queued.card.id)
    card.start_timer()
    col.sched.answer_card(col.sched.build_answer(card=card, states=queued.states, rating=CardAnswer.GOOD))
    before = col.db.all('select id,nid,did,due,ivl,reps,type,queue from cards')
    logs = col.db.all('select * from revlog')
    col.close()
    import time
    time.sleep(1.1)  # Anki's default "update if newer" compares note modification seconds
    d['cards'][0]['blocks'][0]['text'] = '改写后的主干句'
    d['css'] = '.ccpt6 .lead{letter-spacing:.01em}'
    src.write_text(json.dumps(d, ensure_ascii=False))
    build_cards.main([str(src), str(tmp_path / 'v2'), '--audio-pending'])
    col = anki.Collection(path)
    load('v2')
    col.close()
    col = anki.Collection(path)  # reopen: the notetype cache would otherwise show stale CSS
    note = col.get_card(cid).note()
    assert '改写后的主干句' in note['Page'] and 'letter-spacing:.01em' in note.note_type()['css']
    assert col.db.all('select id,nid,did,due,ivl,reps,type,queue from cards') == before
    assert col.db.all('select * from revlog') == logs
    col.close()
