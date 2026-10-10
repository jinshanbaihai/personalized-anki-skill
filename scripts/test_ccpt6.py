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
                 'ruled_out': [{'candidate': 'UK 9MA0', 'why_not': 'synthetic reason'}], 'papers': [{'code': 'WST02', 'format': 'structured'}]},
        'research': [
            {'type': 'spec', 'ref': 'synthetic spec', 'read': 'p.59', 'used_for': 'scope'},
            {'type': 'ms', 'ref': 'synthetic MS', 'read': 'Q2', 'used_for': 'keywords', 'paper': 'WST02'},
            {'type': 'er', 'ref': 'synthetic ER', 'read': 'Q2', 'used_for': 'pitfalls'},
        ],
        'board': [{'id': 'B01', 'where': 'p1', 'point': 'statistic definition', 'items': ['S-1']}],
        'demands': [{'id': 'D1', 'series': 'Jan 2025', 'q': 'Q2(a)', 'ask': 'Explain why X is a statistic', 'points': ['S-1'], 'cards': ['T01']}],
        'coverage': {'scope': 'synthetic 4.2', 'status': 'complete', 'remaining': '', 'saturation': 'synthetic: 4 series, last 3 added nothing new',
                     'backcheck': [{'paper': 'WST02/01', 'series': '2024-06', 'q': '3(a)', 'result': 'pass', 'fixed_by': []},
                                   {'paper': 'WST02/01', 'series': '2023-01', 'q': '5(b)', 'result': 'gap', 'fixed_by': ['T01']}],
                     'coldread': [{'card': 'T01', 'missing': [], 'fixed_by': []}], 'items': [
            {'id': 'S-1', 'spec': '4.2', 'point': 'statistic', 'class': 'core', 'level': 'MS keywords', 'kind': 'term',
             'evidence': ['WST02 Jan 2025 Q2 MS', 'WST02 Jun 2023 ER Q2']},
            {'id': 'X-1', 'spec': 'S3 3.6', 'point': 'CLT', 'class': 'excluded', 'reason': 'other unit'}]},
        'cards': [{
            'id': 'T01', 'genre': 'term', 'title': 'Statistic', 'covers': ['S-1'], 'sources': ['synthetic'],
            'blocks': [
                {'type': 'lead', 'text': '只用样本就能算出的量'},
                {'type': 'definition', 'term': 'Statistic', 'text': 'A quantity calculated only from the sample, containing no unknown parameters.',
                 'keywords': ['only from the sample', 'no unknown parameters'], 'reject': ['because it is known'], 'source': 'synthetic MS'},
                {'type': 'unpack', 'items': [{'key': 'only from the sample', 'explain': '只用样本观测值计算'}, {'key': 'no unknown parameters', 'explain': '不含未知的总体参数'}]},
                {'type': 'examples', 'yes': [{'text': 'sample mean', 'why': 'only sample values'}], 'no': [{'text': 'population mean', 'why': 'unknown parameter'}]},
                {'type': 'exam', 'items': [{'text': 'State whether … is a statistic. Give a reason.', 'mark': 'B1'}]},
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
    assert 'data-depth="3"' in html and len(parts) == 10  # one narration segment per node, depth first
    assert [p.target for p in parts[:4]] == ['b0-n0', 'b0-n1', 'b0-n2', 'b0-n3']


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
    src.write_text(json.dumps(deck(), ensure_ascii=False), encoding='utf-8')
    build_cards.main([str(src), str(tmp_path / 'preview'), '--preview'])
    page = (tmp_path / 'preview' / 'T01.html').read_text(encoding='utf-8')
    assert 'data-theme="lab"' in page and '<math' in page and 'mark class="kw"' in page
    build_cards.main([str(src), str(tmp_path / 'pending'), '--audio-pending'])
    pages = json.loads((tmp_path / 'pending' / 'pages.json').read_text(encoding='utf-8'))
    assert inspect_page(pages['T01']) is None  # pending pages are recognised by default
    with pytest.raises(AssertionError, match='Audio pending'):
        inspect_page(pages['T01'], allow_pending=False)  # --require-audio
    report = json.loads((tmp_path / 'pending' / 'report.json').read_text(encoding='utf-8'))
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
        text = css.read_text(encoding='utf-8')
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
    src.write_text(json.dumps(d, ensure_ascii=False), encoding='utf-8')
    build_cards.main([str(src), str(tmp_path / 'out')])
    manifest = json.loads((tmp_path / 'out' / 'speech-manifest.json').read_text(encoding='utf-8'))[0]
    assert manifest['available'] and manifest['speed'] == 1.5 and manifest['tempo_filter'] == 'atempo=1.5'
    cues = manifest['narration']['cues']
    assert cues[0]['target'] is None and [c['target'] for c in cues][1:7] == ['b0', 'b1', 'b2-0', 'b2-1', 'b3-yes0', 'b3-no0']
    page = json.loads((tmp_path / 'out' / 'pages.json').read_text(encoding='utf-8'))['T01']
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
    src.write_text(json.dumps(d, ensure_ascii=False), encoding='utf-8')
    build_cards.main([str(src), str(tmp_path / 'out2')])
    assert calls == [] and json.loads((tmp_path / 'out2' / 'speech-manifest.json').read_text(encoding='utf-8'))[0]['speed'] == 2.0


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
    # One signal alone keeps 2×: a three-step proof with no spoken formulas is a structure, not a dense page.
    proof = {'genre': 'derivation', 'title': 'Proof by contradiction', 'blocks': [{'type': 'steps', 'items': [{'do': 'a', 'why': 'b'}] * 3}]}
    m = narration.speed_metrics(proof, '证明', set())
    assert m['signals'] == {'structure': ['证明结构'], 'load': []} and narration.decide_speed(m) == (2.0, '')
    # "show that" is a command word, not a proof.
    shown = {'genre': 'derivation', 'title': 'Show that x = 2', 'blocks': [{'type': 'steps', 'items': [{'do': 'a', 'why': 'b'}] * 3}]}
    assert not narration.speed_metrics(shown, 'x', set())['proof']


def test_speed_rule_needs_two_signals():
    def steps(dos, genre='method'):
        return {'genre': genre, 'title': 't', 'blocks': [{'type': 'steps', 'items': [{'do': d, 'why': '为了把未知量单独留下'} for d in dos]}]}
    # Structure without load: four formula steps, long Chinese reasoning, few values → 2×.
    plain = steps([f'$x_{i}$〔x {i}〕，然后两边同时除以系数，留意符号与定义域的限制条件' for i in range(4)])
    m = narration.speed_metrics(plain, '讲解' * 60, set())
    assert m['signals']['structure'] and not m['signals']['load'] and narration.decide_speed(m)[0] == 2.0, m
    # The same steps carrying many values to hold → structure + load → 1.5×.
    values = steps([f'$x = {a}$〔x 等于 {a}〕，代入 {b} 与 {c}' for a, b, c in ((14, 25, 36), (47, 58, 69), (71, 82, 93), (104, 115, 126))])
    m = narration.speed_metrics(values, '讲解' * 60, set())
    assert narration.decide_speed(m)[0] == 1.5 and '需同时记住' in narration.decide_speed(m)[1], m
    # Symbolic algebra with many readings per step is heavy too, without any numbers (the reviewer's M-binomial case).
    algebra = steps([' '.join(f'$a_{j}$〔a {j}〕' for j in range(7)) + '，整理' for _ in range(5)])
    m = narration.speed_metrics(algebra, '讲解' * 60, set())
    assert narration.decide_speed(m)[0] == 1.5 and '每步约' in narration.decide_speed(m)[1], m
    # Load without structure: a formula-heavy three-step page stays 2×.
    short = steps([' '.join(f'$b_{j}$〔b 的 {j} 次项〕' for j in range(9)) for _ in range(3)])
    m = narration.speed_metrics(short, 'x', set())
    assert m['signals']['load'] and not m['signals']['structure'] and narration.decide_speed(m)[0] == 2.0, m
    # Formulas inside a table are read on screen, and a block whose own speech replaces its readings adds none.
    table = {'genre': 'formula', 'title': 't', 'blocks': [{'type': 'lead', 'text': '下表列出常用结果，讲解只读标题。'},
             {'type': 'table', 'head': ['f', 'F'], 'rows': [[f'$x^{i}$〔x 的 {i} 次方〕', f'$x^{i+1}$〔x 的 {i+1} 次方〕'] for i in range(6)]}]}
    assert narration.speed_metrics(table, 'x', set())['m_share'] < 0.35
    spoken = {'genre': 'formula', 'title': 't', 'blocks': [{'type': 'lead', 'speech': '看图。',
              'text': '$x^2$〔x 的平方，也就是 x 乘以 x 的这个很长的读法〕 和 $y^2$〔y 的平方，也是一段很长的读法〕'}]}
    assert narration.speed_metrics(spoken, 'x', set())['m_share'] <= 1.0



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
    for css in [ROOT / 'assets/ccpt6/base.css', ROOT / 'assets/ccpt6/motifs.css', *(ROOT / 'assets/ccpt6/themes').glob('*.css')]:
        text = re.sub(r'/\*[\s\S]*?\*/', '', css.read_text(encoding='utf-8'))
        for banned in ('light-dark(', 'color-mix(', '@container'):
            assert banned not in text, f'{css.name} uses {banned}'
        assert not re.search(r'{[^{}]*&', text), f'{css.name} uses CSS nesting'
    for css in (ROOT / 'assets/ccpt6/themes').glob('*.css'):
        text = css.read_text(encoding='utf-8')
        assert f'.night_mode .ccpt6[data-theme="{css.stem}"]' in text and f'.nightMode.card:has(.ccpt6[data-theme="{css.stem}"])' in text


def test_fonts_are_bundled_with_content_hashes(tmp_path):
    src = tmp_path / 'deck.json'
    src.write_text(json.dumps(deck(), ensure_ascii=False), encoding='utf-8')
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
    src.write_text(json.dumps(d, ensure_ascii=False), encoding='utf-8')
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
    src.write_text(json.dumps(d, ensure_ascii=False), encoding='utf-8')
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


def test_demand_inventory_is_required_and_linked():
    d = deck()
    del d['demands']
    with pytest.raises(deck_rules.DeckError, match='demands'):
        deck_rules.check(d)
    d = deck()
    d['demands'][0]['cards'] = ['NOPE']
    with pytest.raises(deck_rules.DeckError, match='card ids'):
        deck_rules.check(d)
    d = deck()
    d['demands'][0]['cards'] = []
    with pytest.raises(deck_rules.DeckError, match='not_carded'):
        deck_rules.check(d)
    d = deck()
    d['coverage']['items'].append({'id': 'S-2', 'spec': '4.2', 'point': 'sampling distribution', 'class': 'core', 'level': 'x', 'kind': 'term',
                                   'evidence_gap': 'synthetic', 'existing': 'old deck card'})
    assert deck_rules.check(d)['coverage']['undemanded'] == ['S-2']


def test_adjacent_points_are_listed_not_taught():
    d = deck()
    d['coverage']['items'].append({'id': 'H-1', 'spec': '4.3', 'point': 'critical region', 'class': 'adjacent', 'reason': 'same section, next batch'})
    assert deck_rules.check(deck_rules_copy(d))['coverage']['adjacent'] == ['H-1']
    d['cards'][0]['covers'].append('H-1')
    with pytest.raises(deck_rules.DeckError, match='adjacent'):
        deck_rules.check(d)


def deck_rules_copy(d):
    return copy.deepcopy(d)


def test_each_paper_format_needs_its_own_source():
    d = deck()
    d['exam']['papers'] = [{'code': '9708/3', 'format': 'mcq'}]
    with pytest.raises(deck_rules.DeckError, match='9708/3'):
        deck_rules.check(d)
    d['research'][1]['paper'] = ['9708/3']
    deck_rules.check(d)


def test_blurry_board_points_need_a_confirming_source():
    d = deck()
    d['board'][0]['legibility'] = 'low'
    with pytest.raises(deck_rules.DeckError, match='confirmed_by'):
        deck_rules.check(d)
    d['board'][0]['confirmed_by'] = 'WST02 Jan 2025 MS p.8'
    deck_rules.check(d)


def test_term_definition_needs_a_source():
    d = deck()
    del d['cards'][0]['blocks'][1]['source']
    with pytest.raises(deck_rules.DeckError, match='definition.source'):
        deck_rules.check(d)


def test_heuristic_note_names_exceptions():
    with pytest.raises(blocks.BlockError, match='exceptions'):
        blocks.render_block({'type': 'note', 'tone': 'heuristic', 'text': 'ILATE'}, 'b0', 'w')
    html, parts = blocks.render_block({'type': 'note', 'tone': 'heuristic', 'text': 'ILATE 选 u',
                                       'exceptions': ['$\\int \\ln x\\,dx$〔ln x 的积分〕：把 1 当作 dv']}, 'b0', 'w')
    assert '经验法则' in html and '不是评分要求' in parts[0].text and 'ln x 的积分' in parts[0].text


def test_alternative_method_says_when_to_use_it():
    html, parts = blocks.render_block({'type': 'steps', 'label': '另一种做法', 'when': '分母是一次因式时更快',
                                       'items': [{'do': 'x', 'why': '为了消去 B'}]}, 'b0', 'w')
    assert 'steps-when' in html and parts[0].text.startswith('另一种做法') and '什么时候用这种做法' in parts[0].text


def test_pitfall_source_types_are_labelled():
    with pytest.raises(blocks.BlockError, match='source_type'):
        blocks.render_block({'type': 'pitfall', 'items': [{'wrong': 'a', 'right': 'b', 'source': 'x', 'source_type': 'rumour'}]}, 'b0', 'w')
    html, _ = blocks.render_block({'type': 'pitfall', 'items': [{'wrong': 'a', 'right': 'b', 'source': 'Q01 A2 = 0', 'source_type': 'user-script'}]}, 'b0', 'w')
    assert '本卷批改记录' in html


def test_theme_by_subdeck_and_formula_booklet():
    d = deck()
    d['style']['theme_by_subdeck'] = {'P4': 'paper'}
    d['cards'][0]['subdeck'] = 'P4'
    d['cards'][0]['formula_booklet'] = 'memorise'
    deck_rules.check(d)
    r = build_cards.render_card(d, d['cards'][0], d['style'])
    assert r['theme'] == 'paper'
    d['cards'][0]['formula_booklet'] = 'maybe'
    with pytest.raises(deck_rules.DeckError, match='formula_booklet'):
        deck_rules.check(d)


def test_board_legibility_gate_flags_recompressed_images():
    from PIL import Image
    from slice_board import legibility
    assert legibility(Image.new('RGB', (259, 2000), 'white'))['verdict'] == 'low'
    assert legibility(Image.new('RGB', (1600, 2000), 'white'))['verdict'] == 'ok'
    # A PDF is judged by its embedded image, not by the page rendered at a high dpi; vector pages pass.
    assert legibility(Image.new('RGB', (1680, 2000), 'white'), embedded_width=420, pdf=True)['verdict'] == 'low'
    assert legibility(Image.new('RGB', (1680, 2000), 'white'), embedded_width=None, pdf=True)['verdict'] == 'ok'


def test_slice_board_reads_embedded_pdf_image_width(tmp_path):
    import shutil, subprocess, sys
    if not (shutil.which('pdftoppm') and shutil.which('pdfimages')):
        pytest.skip('poppler not installed')
    from PIL import Image
    pdf = tmp_path / 'board.pdf'
    Image.new('RGB', (420, 900), 'white').save(pdf, 'PDF', resolution=50)  # a chat-recompressed board wrapped in a PDF
    out = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'slice_board.py'), str(pdf), str(tmp_path / 's')], capture_output=True, text=True, encoding='utf-8')
    quality = json.loads((tmp_path / 's' / 'index.json').read_text(encoding='utf-8'))['quality']
    assert [v['verdict'] for v in quality.values()] == ['low'] and quality[next(iter(quality))]['width'] == 420, out.stdout + out.stderr


def test_inline_integrals_are_text_style():
    html = blocks.inline('$\\int_0^1 x\\,dx$〔x 从 0 到 1 的积分〕', 'w').html
    assert 'largeop="false"' in html
    display = blocks.inline('$$\\int_0^1 x\\,dx$$〔x 从 0 到 1 的积分〕', 'w').html
    assert 'largeop="false"' not in display


def test_text_files_are_read_and_written_as_utf8():
    """Windows defaults to cp936/cp1252; every text read or write must name UTF-8."""
    import ast
    for path in (ROOT / 'scripts').glob('*.py'):
        for node in ast.walk(ast.parse(path.read_text(encoding='utf-8'))):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in ('read_text', 'write_text'):
                assert any(k.arg == 'encoding' for k in node.keywords), f'{path.name}:{node.lineno} {node.func.attr} without encoding'


@pytest.mark.parametrize('mark', ['M1', 'dM1', 'ddM1', 'DM1', 'A1', 'A1*', 'A1ft', 'B1ft', 'A1cso', 'A1 cso', 'M1 A1*', 'M1A1', 'B1 oe', 'SC1', 'C1', 'A1 isw', 'M1 A1 A1'])
def test_mark_scheme_notation_is_accepted(mark):
    html, parts = blocks.render_block({'type': 'steps', 'items': [{'do': 'x', 'why': '为了消去 x', 'mark': mark}]}, 'b0', 'w')
    assert '这一步记' in parts[0].text


@pytest.mark.parametrize('mark', ['two marks', 'AO2', 'M', 'M1+A1'])
def test_non_mark_scheme_labels_are_rejected(mark):
    with pytest.raises(blocks.BlockError, match='mark-scheme notation'):
        blocks.render_block({'type': 'steps', 'items': [{'do': 'x', 'why': 'y', 'mark': mark}]}, 'b0', 'w')


def test_keywords_never_touch_markup_or_math():
    html, _ = blocks.render_block({'type': 'definition', 'term': 'span', 'keywords': ['class', 'span', 'span of'],
                                   'text': 'A span of $\\text{span}$〔span〕 is the class of vectors'}, 'b0', 'w')
    assert 'class="math"' in html and '<mark class="kw">span of</mark>' in html and 'data-tex="\\text{span}"' in html
    assert '<mark class="kw">class</mark> of vectors' in html
    with pytest.raises(blocks.BlockError, match='split by formatting'):
        blocks.render_block({'type': 'definition', 'term': 'x', 'keywords': ['only from'], 'text': '<b>only</b> from the sample'}, 'b0', 'w')


def test_spaced_comparison_is_shown_and_spoken():
    t = blocks.inline('当 x < 2 时，P(X < 3) 成立', 'w')
    assert '&lt; 2' in t.html and t.speech == '当 x < 2 时，P(X < 3) 成立'
    assert '小于 2' in narration.apply_lexicon(t.speech, {})


def test_unspoken_formula_in_a_label_is_caught():
    with pytest.raises(blocks.BlockError, match='spoken form'):
        blocks.render_block({'type': 'steps', 'label': '求 $\\int x e^x dx$', 'items': [{'do': 'x', 'why': '为了 y'}]}, 'b0', 'w')
    with pytest.raises(blocks.BlockError, match='spoken form'):
        blocks.render_block({'type': 'finish', 'label': '$x$ 的范围', 'items': ['a']}, 'b0', 'w')


def test_currency_reads_as_dollars():
    t = blocks.inline('每单位征税 \\$2，补贴 \\$1.5', 'w')
    assert '$2' in t.html and t.speech == '每单位征税 2 美元，补贴 1.5 美元' and '$' not in t.speech


def test_item_shorthand_gets_a_clear_error():
    with pytest.raises(blocks.BlockError, match='object with named fields'):
        blocks.render_block({'type': 'steps', 'items': ['x = 2']}, 'b0', 'w')
    with pytest.raises(blocks.BlockError, match='caption, points'):
        blocks.render_block({'type': 'figure', 'svg': '<svg viewBox="0 0 10 10"></svg>'}, 'b0', 'w')


def test_scoring_information_is_narrated():
    _, parts = blocks.render_block({'type': 'steps', 'items': [{'do': 'x', 'why': '为了消去 y', 'mark': 'A1*', 'mark_note': '漏写结论丢 A1'}]}, 'b0', 'w')
    assert 'A 1 星' in parts[0].text and '评分注意：漏写结论丢 A1' in parts[0].text
    _, parts = blocks.render_block({'type': 'pitfall', 'items': [{'wrong': 'a', 'right': 'b', 'lost': 'A1'}]}, 'b0', 'w')
    assert '会丢 A 1' in parts[0].text
    _, parts = blocks.render_block({'type': 'table', 'head': ['a', 'b'], 'rows': [['x', ''], ['y', 'z']], 'caption': '表注'}, 'b0', 'w')
    assert parts[0].text == 'x' and parts[-1].text.endswith('表注')


def test_math_spacing_and_bars():
    html = blocks.inline('$\\bar{X}$〔X 拔〕 与 $({-}\\frac23)$〔负三分之二〕 与 $\\ln x$〔ln x〕', 'w').html
    assert '&#x02015;' in html and 'form="prefix"' in html and '<mi>ln</mi><mspace' in html


def test_long_equality_chain_can_wrap():
    html = blocks.inline('$(8+32x)^{\\frac13}=8^{\\frac13}(1+4x)^{\\frac13}=2(1+4x)^{\\frac13}$〔读法〕', 'w').html
    assert html.count('class="math"') == 3 and '​' in html


def test_relation_rules_match_layout_js():
    js = (ROOT / 'assets' / 'ccpt6' / 'layout.js').read_text(encoding='utf-8')
    for rule, _ in blocks.REL_RULES:
        assert rule.pattern in js, rule.pattern[:40]


def test_speed_rule_ignores_citations_and_mark_bands():
    seen = set()
    pitfall = {'id': 'p', 'genre': 'pitfall', 'title': 't', 'blocks': [{'type': 'pitfall', 'items': [
        {'wrong': '写 n ≥ 51', 'right': 'n = 51', 'source': 'WMA14 Jan 2024 ER pp.3、6', 'lost': 'A1'},
        {'wrong': 'a', 'right': 'b', 'source': 'WST02 Jun 2024 MS pp.8–9'}]}]}
    ladder = {'id': 'e', 'genre': 'essay', 'title': 't', 'blocks': [{'type': 'sections', 'items': [
        {'head': 'Level 1（1–5 分）', 'text': '只点名'}, {'head': 'Level 3（11–14 分）', 'text': '多环因果'}, {'head': 'AO3 Level 2（4–6 分）', 'text': '有理由的判断'}]}]}
    for card in (pitfall, ladder):
        m = narration.speed_metrics(card, 'x', seen)
        assert narration.decide_speed(m)[0] == 2.0, (card['id'], m)


def test_display_math_counts_like_inline_math():
    def deriv(d):
        return {'id': 'd', 'genre': 'derivation', 'title': 't', 'blocks': [{'type': 'steps', 'items': [
            {'do': f'{d}x^{i}{d}〔x 的 {i} 次方〕', 'why': '为了化简'} for i in range(4, 9)]}]}
    a = narration.speed_metrics(deriv('$'), 'x 的 4 次方', set())
    b = narration.speed_metrics(deriv('$$'), 'x 的 4 次方', set())
    assert a['M'] == b['M'] == 5


def test_minus_signs_and_symbols_are_read():
    assert narration.apply_lexicon('斜率为−2，取值 −2、−3，[−1, 1]，3 −2，MPC − s', {}) == '斜率为负2，取值 负2、负3，[负1, 1]，3 减2，MPC 减 s'
    assert narration.apply_lexicon('Q* 处价格↑', {}) == 'Q 星 处价格上升'
    assert '⟦' in narration.speech_lint('⟦公式⟧')


def test_board_images_are_turned_upright_and_flattened():
    from PIL import Image
    from slice_board import upright_rgb
    rotated = Image.new('RGB', (300, 100), 'white')
    exif = rotated.getexif()
    exif[0x0112] = 6
    path = ROOT / 'scripts' / '__rot_test.jpg'
    rotated.save(path, exif=exif)
    try:
        assert upright_rgb(Image.open(path)).size == (100, 300)
    finally:
        path.unlink()
    clear = Image.new('RGBA', (10, 10), (0, 0, 0, 0))
    assert upright_rgb(clear).getpixel((5, 5)) == (255, 255, 255)


def test_genre_structure_and_academic_flag():
    d = deck()
    d['cards'].append({'id': 'C01', 'genre': 'chain', 'title': '因果', 'covers': ['S-1'], 'blocks': [{'type': 'lead', 'text': '一段话'}]})
    with pytest.raises(deck_rules.DeckError, match='chain block'):
        deck_rules.check(d)
    d = deck()
    d['academic'] = False
    with pytest.raises(deck_rules.DeckError, match='academic: false'):
        deck_rules.check(d)
    d = deck()
    d['exam']['papers'] = []
    with pytest.raises(deck_rules.DeckError, match='exam.papers'):
        deck_rules.check(d)
    d = deck()
    d['cards'][0]['blocks'] = [b for b in d['cards'][0]['blocks'] if b['type'] != 'unpack']
    with pytest.raises(deck_rules.DeckError, match='unpack'):
        deck_rules.check(d)


def test_lost_marks_on_the_board_need_a_card():
    d = deck()
    d['board'].append({'id': 'Q01A2', 'where': 'p1 右栏', 'point': '系数没乘回 2', 'items': ['S-1'], 'lost': 'A1'})
    with pytest.raises(deck_rules.DeckError, match='lost mark'):
        deck_rules.check(d)
    d['board'][-1]['cards'] = ['T01']
    deck_rules.check(d)


def test_lint_reads_chains_and_maps_like_the_renderer():
    card = {'genre': 'chain', 'blocks': [
        {'type': 'chain', 'items': ['政府征税', '生产者成本']},
        {'type': 'map', 'root': {'text': 'r', 'children': [{'text': '补贴', 'rel': '导致', 'children': [{'text': '好处', 'rel': '包括'}]},
                                                             {'text': '政府干预总是有效的', 'kind': 'evaluation'}]}}]}
    warnings = build_cards.lint_card(card)
    assert any(w.startswith('chain 的因果箭头') for w in warnings)
    assert any(w.startswith('map 的因果箭头') for w in warnings) and any('评价节点' in w for w in warnings)
    assert any('包括' in w for w in warnings)


def test_term_ledger_sees_single_words():
    d = deck()
    pages = {'T01': '<main><header>x</header><article><p>当 externality 存在时，sample mean 可算</p></article></main>'}
    terms = [x['term'] for x in build_cards.term_ledger(d, pages)]
    assert 'externality' in terms and 'statistic' not in terms


def test_comparison_swallowed_by_an_optional_end_tag_is_rejected():
    with pytest.raises(blocks.BlockError, match='attribute name'):
        blocks.render_block({'type': 'html', 'html': '<div>q<p 且 p>0.5 时拒绝</div>', 'speech': 'x'}, 'b0', 'w')


def test_formula_splitting_respects_environments_and_brackets():
    for tex in ('\\mathbf{r}=\\begin{pmatrix}1\\\\2\\end{pmatrix}+\\lambda\\begin{pmatrix}3\\\\-1\\end{pmatrix}+\\mu\\begin{pmatrix}0\\\\1\\end{pmatrix}',
                'f(x)=\\begin{cases}2x & 0\\le x<1\\\\ 3-x & 1\\le x\\le 3\\end{cases}'):
        assert blocks.split_relations(tex) == [tex]
        assert 'class="math"' in blocks.inline(f'${tex}$〔读法〕', 'w').html
    pieces = blocks.split_relations('P(X\\le 3)=P(X=0)+P(X=1)+P(X=2)+P(X=3)=0.6472')
    assert all(p.count('(') == p.count(')') for p in pieces) and len(pieces) == 3


def test_tight_comparison_is_rejected_not_swallowed():
    for text in ('当 p<b 时选 A', 'MSB<MSC 时过度生产', '若 cost<em 则亏损'):
        with pytest.raises(blocks.BlockError, match='touching a letter|reads as a tag|not inline'):
            blocks.inline(text, 'w')
    assert blocks.inline('<b>重点</b> 与 x < 2', 'w').speech == '重点 与 x < 2'


def test_currency_before_punctuation():
    assert blocks.inline('The tax is \\$2, and the subsidy is \\$1.50.', 'w').speech == 'The tax is 2 美元, and the subsidy is 1.50 美元.'


def test_cambridge_mark_counts_are_read():
    _, parts = blocks.render_block({'type': 'steps', 'items': [{'do': 'x', 'why': '为了 y', 'mark': '[2]'}]}, 'b0', 'w')
    assert '这一步记 2 分' in parts[0].text


def test_why_that_restates_the_step_is_flagged():
    assert build_cards.why_echoes('代入得到 2x+3=7', '2x+3=7')
    assert not build_cards.why_echoes('为了消去 B', 'x=1')
    assert not build_cards.why_echoes('比较系数得到 B', 'B=3')


def test_directional_relation_words_count_as_direction():
    card = {'genre': 'chain', 'blocks': [{'type': 'chain', 'items': [{'text': '补贴'}, {'text': '消费量', 'rel': '提高'}]}]}
    assert not any('方向' in w for w in build_cards.lint_card(card))


def test_paper_gap_next_to_chinese_text():
    d = deck()
    d['exam']['papers'] = [{'code': '9708/3', 'format': 'mcq'}]
    d['research_gaps'] = '缺9708/3的考官报告，用 9708/4 ER 替代'
    deck_rules.check(d)


def test_per_mark_board_ids_need_lost():
    d = deck()
    d['board'].append({'id': 'Q01A2', 'where': 'p1', 'point': '没乘回 2', 'note': '粗心'})
    with pytest.raises(deck_rules.DeckError, match='per-mark record'):
        deck_rules.check(d)


def test_minus_after_symbols_is_subtraction():
    assert narration.apply_lexicon('x² − 1，σ − 2，Q* − 3', {}) == 'x的平方 减 1，sigma 减 2，Q 星 减 3'


def test_term_ledger_skips_chrome_and_glosses():
    d = deck()
    pages = {'T01': ('<main><article><span class="def-label">Definition</span><p class="def-src">June 2024 MS</p>'
                     '<span class="ex-text">population mean</span><span class="ex-why">unknown parameter</span>'
                     '<p>integrand（被积函数）与 separable 方程，MPC 上移，MS（评分方案）给分</p></article></main>')}
    terms = [x['term'] for x in build_cards.term_ledger(d, pages)]
    assert 'definition' not in terms and 'june' not in terms and 'integrand' not in terms and 'MS' not in terms
    assert 'separable' in terms and 'MPC' in terms and not any('meanunknown' in t for t in terms)
    # The ledger is uncapped, plurals fold onto the singular, and taught terms_known / ignore_words are honoured.
    many = {'T01': '<p>' + '，'.join(f'zork{chr(97 + i)}{chr(97 + j)}' for i in range(6) for j in range(6)) + '，integrands，residuals</p>'}
    d['terms_known'] = [{'term': 'residual', 'taught_in': ['T01']}]
    d['ignore_words'] = ['zorkaa']
    terms = [x['term'] for x in build_cards.term_ledger(d, many)]
    assert len(terms) == 36 and 'residual' not in terms and 'zorkaa' not in terms and 'integrand' in terms


def test_untranslated_quotes_and_plain_math_are_flagged():
    pages = {'A': '<p>Explain why the government might tax goods with a negative externality.</p>',
             'B': '<p>Explain why the government might tax goods with a negative externality.</p><p>解释政府为何对负外部性商品征税。</p>'}
    assert set(build_cards.untranslated(pages)) == {'A'}
    card = {'id': 'x', 'genre': 'method', 'title': 't', 'blocks': [{'type': 'lead', 'text': '先算 P(X = 2)，再用 √n 与 3/8；只得 7/14 分，满分 14'},
                                                               {'type': 'lead', 'text': '$\\frac{3}{8}$〔八分之三〕', 'source': 'MS p.3 3/8'}]}
    hits = build_cards.plain_math(card)
    assert len(hits) == 3, hits  # P(, √ and 3/8; the mark tally and the source citation are not maths
    tally = {'id': 'y', 'genre': 'essay', 'title': 't', 'blocks': [{'type': 'lead', 'text': '只得 7/14 分；at least 4/6 marks'}]}
    assert build_cards.plain_math(tally) == []


def test_exam_registries_are_valid():
    """Every registry in references/exams validates (marks add up, spec ids exist, ids unique)."""
    import exam_index
    assert exam_index.check() == []


def test_exam_index_queries(tmp_path):
    import exam_index
    board = tmp_path / 'demo'
    (board / 'units').mkdir(parents=True)
    (board / 'spec-items.json').write_text(json.dumps({'WMA14': {'4.1': {'title': 'binomial series', 'page': 27, 'level': 'unit'},
                                                                 '6.4': {'title': 'separable DE', 'page': 28, 'level': 'unit'}}}), encoding='utf-8')
    entry = {'id': 'WMA14-2406-01-Q1', 'unit': 'WMA14', 'paper': 'WMA14/01', 'series': '2024-06', 'q': '1', 'marks': 5,
             'parts': [{'part': 'a', 'marks': 4, 'spec': ['4.1'], 'command': 'Find', 'ask': 'first four terms', 'final_form': 'simplest form',
                        'ms': 'M1 B1 A1 A1', 'er': 'coefficient slips'},
                       {'part': 'b', 'marks': 1, 'spec': ['4.1'], 'command': 'State', 'ask': 'validity', 'final_form': '|x|<1/4', 'ms': 'B1', 'er': ''}],
             'sources': {'qp': 'drive:x', 'ms': 'drive:y', 'er': ''}}
    (board / 'units' / 'WMA14.questions.json').write_text(json.dumps([entry]), encoding='utf-8')
    assert exam_index.check(tmp_path) == []
    regs = exam_index.registries(tmp_path)
    qs = regs['demo']['questions']
    assert len(exam_index.select(qs, 'WMA14', spec='4.1')) == 1 and exam_index.select(qs, 'WMA14', spec='6.4') == []
    assert exam_index.select(qs, 'WMA14', grep='VALIDITY')[0]['parts'][0]['part'] == 'b'
    assert exam_index.as_demands(exam_index.select(qs, 'WMA14'))[0]['q'] == 'Q1a'
    assert dict((s, n) for s, _, n in exam_index.coverage(qs, regs['demo']['items'], 'WMA14')) == {'4.1': 2, '6.4': 0}
    entry['parts'][0]['spec'] = ['9.9']
    entry['marks'] = 6
    (board / 'units' / 'WMA14.questions.json').write_text(json.dumps([entry]), encoding='utf-8')
    problems = exam_index.check(tmp_path)
    assert any('unknown spec item 9.9' in p for p in problems) and any('part marks 5 != total 6' in p for p in problems)


def test_skill_package_is_uploadable(tmp_path):
    import package_skill
    out, count = package_skill.package(tmp_path, files=package_skill.tracked_files(strict=False))
    names = zipfile.ZipFile(out).namelist()
    assert 'anki-ccpt-skill/SKILL.md' in names and any(n.startswith('anki-ccpt-skill/assets/ccpt6/fonts/') for n in names)
    assert not any('/test_' in n or '__pycache__' in n or n.endswith('.env') for n in names)
    # Personal data and secrets stop the packer.
    assert package_skill.leaks('references/x.md', b'contact someone@example.com')
    assert package_skill.leaks('references/x.md', b'see https://drive.google.com/file/d/abc')
    assert package_skill.leaks('scripts/x.txt', b'AZURE_SPEECH_KEY=3f9c2a7be1d04c55a0')
    assert not package_skill.leaks('scripts/x.py', b"key = os.environ.get('AZURE_SPEECH_KEY')")


def test_exam_fingerprint_grades_follow_exam_lock():
    import exam_fingerprint
    lone = exam_fingerprint.scan('Negative externalities (Total for Question 3 is 8 marks)')
    assert lone['board_candidates'][0]['best_grade'].startswith('B-partial') and not lone['board_candidates'][0]['lockable']
    assert lone['topics'][0]['grade'].startswith('C')
    full = exam_fingerprint.scan('(Total for Question 3 is 8 marks) r = a + λb, partial fractions')
    assert full['board_candidates'][0]['best_grade'] == 'B' and full['board_candidates'][0]['lockable']
    coded = exam_fingerprint.scan('Paper reference WMA14/01A')
    assert coded['board_candidates'][0]['best_grade'] == 'A'


def test_privacy_blocks_personal_framing_ids_and_scores():
    d = deck()
    d['cards'][0]['blocks'][0]['text'] = '你的卷面 Q4 丢了 A1：终点没写成最简形式'
    with pytest.raises(deck_rules.DeckError, match='你'):
        deck_rules.check(d)
    # One reviewed false positive is listed by path instead of switching the whole gate off.
    d['privacy_reviewed'] = ['cards[0].blocks[0].text']
    deck_rules.check(d)
    del d['privacy_reviewed']
    d['personal'] = True  # a deck only for the learner themselves
    deck_rules.check(d)
    d = deck()
    d['research'][0]['used_for'] = '总分 49/75，丢分集中在 A 分'
    with pytest.raises(deck_rules.DeckError, match='total score'):
        deck_rules.check(d)
    d = deck()
    d['research'][0]['read'] = 'cover page: candidate number 0123'
    with pytest.raises(deck_rules.DeckError, match='candidate'):
        deck_rules.check(d)
    d = deck()
    # Neutral records, generic teaching phrases and probabilities pass.
    d['cards'][0]['blocks'][0]['text'] = ('本卷批改记录：Q9(a) M1、A1 未得；如果不写 +c，你丢 A1；Expected score E(S) = 13/125；'
                                          'a total of 3/100 of the output is defective；只得 7 分（满分 14）')
    deck_rules.check(d)
    for personal in ('卷面总分 49／75', '本卷得分 49 分（满分 75）', 'Total: 49 out of 75', '你在 Q5 丢了 1 分', 'On your script you lost the A1',
                     'Candidate No. 0123'):
        d = deck()
        d['research'][0]['read'] = personal
        with pytest.raises(deck_rules.DeckError):
            deck_rules.check(d)


def test_backcheck_trail_and_planning_mode(tmp_path, capsys):
    d = deck()
    d['coverage']['backcheck'] = d['coverage']['backcheck'][:1]
    with pytest.raises(deck_rules.DeckError, match='two past questions'):
        deck_rules.check(d)
    d['coverage']['backcheck'] = [{'paper': 'WST02/01', 'series': '2024-06', 'q': '3', 'result': 'gap', 'fixed_by': []},
                                  {'paper': 'WST02/01', 'series': '2023-01', 'q': '5', 'result': 'pass', 'fixed_by': []}]
    with pytest.raises(deck_rules.DeckError, match='fixed_by'):
        deck_rules.check(d)
    # Before any card exists the research and coverage plan can be checked on its own.
    plan = deck()
    plan['cards'] = []
    plan['demands'][0]['cards'] = []
    src = tmp_path / 'plan.json'
    src.write_text(json.dumps(plan, ensure_ascii=False), encoding='utf-8')
    build_cards.main([str(src), '--check-research'])
    out = json.loads(capsys.readouterr().out)
    assert out['cards'] == 0 and out['coverage']['missing'] == ['S-1']


def test_genre_structure_and_legacy_voice():
    d = deck()
    d['cards'].append({'id': 'M01', 'genre': 'method', 'title': 'm', 'covers': ['S-1'], 'blocks': [{'type': 'lead', 'text': 'x'}]})
    with pytest.raises(deck_rules.DeckError, match='method card'):
        deck_rules.check(d)
    d = deck()
    d['cards'].append({'id': 'F01', 'genre': 'formula', 'title': 'f', 'covers': ['S-1'],
                       'blocks': [{'type': 'unpack', 'items': [{'key': 'a', 'explain': 'b'}, {'key': 'c', 'explain': 'd'}]}]})
    with pytest.raises(deck_rules.DeckError, match='formula_booklet'):
        deck_rules.check(d)
    d = deck()
    d['style']['voice'] = 'yunxi'
    with pytest.raises(deck_rules.DeckError, match='legacy_voice'):
        deck_rules.check(d)
    d['style']['legacy_voice'] = True
    deck_rules.check(d)


def test_audio_note_tag_and_package_name(tmp_path):
    d = deck()
    d['deck']['name'] = 'Pearson IAL Statistics 2 WST02 Populations samples and statistics extended edition'
    d['exam']['code'], d['exam']['units'] = '9708', ['9708/3', '9708/4']
    assert build_cards.card_tag(d, d['cards'][0]) == '9708 · P3 · P4'
    src = tmp_path / 'deck.json'
    src.write_text(json.dumps(d, ensure_ascii=False), encoding='utf-8')
    build_cards.main([str(src), str(tmp_path / 'out'), '--audio-pending'])
    note = (tmp_path / 'out' / '补语音.txt').read_text(encoding='utf-8')
    for needed in ('Python 3.10', 'python3 -m venv .venv', '.venv/bin/python -m pip install -r skill/scripts/requirements.txt',
                   r'.\.venv\Scripts\python', 'winget install Gyan.FFmpeg', 'brew install ffmpeg', 'sudo apt install ffmpeg',
                   'speech_backend.py --check', 'build_cards.py deck.json . --term-sampler', 'Claude Code'):
        assert needed in note, needed
    assert str(tmp_path) not in note and (tmp_path / 'out' / 'deck.json').is_file()
    # The delivered folder alone can rebuild: its bundled skill copy builds the bundled deck.json.
    bundled = tmp_path / 'out' / 'skill' / 'scripts' / 'build_cards.py'
    assert bundled.is_file() and (tmp_path / 'out' / 'skill' / 'assets' / 'ccpt6' / 'base.css').is_file()
    import subprocess, sys
    run = subprocess.run([sys.executable, str(bundled), 'deck.json', 'rebuilt', '--audio-pending'], cwd=tmp_path / 'out',
                         capture_output=True, text=True, encoding='utf-8')
    assert run.returncode == 0, run.stderr
    assert list((tmp_path / 'out' / 'rebuilt').glob('*.apkg'))
    pkg = next((tmp_path / 'out').glob('*.apkg')).stem
    assert len(pkg) <= 60 and not pkg.endswith('_') and pkg.split('_')[-1] in d['deck']['name'].split()


def test_review_round_regressions(tmp_path):
    # A lost mark written with brackets is still a per-mark record that needs its card.
    d = deck()
    d['board'].append({'id': 'Q9(a)M1', 'where': 'p2', 'point': 'Q9(a) M1 未得', 'items': ['S-1'], 'score': 0})
    with pytest.raises(deck_rules.DeckError, match='lost'):
        deck_rules.check(d)
    # Preview of a complete deck without the trail warns instead of failing; a package still requires it.
    d = deck()
    d['coverage']['backcheck'] = []
    assert any('回查' in w for w in deck_rules.check(d, preview=True)['warnings'])
    with pytest.raises(deck_rules.DeckError, match='two past questions'):
        deck_rules.check(d)
    # Planning mode accepts planned card ids that do not exist yet.
    plan = deck()
    plan['cards'] = []
    assert deck_rules.check_plan(plan)['coverage']['items'] == 2
    # Exemplar pages must be real page numbers; "only images" is not a gap, a real absence is.
    d = deck()
    d['exam']['papers'] = [{'code': 'WST02', 'format': 'essay'}]
    d['research'].append({'type': 'exemplar', 'ref': 'ECR', 'read': '封面页与目录', 'used_for': 'x', 'paper': 'WST02'})
    assert deck_rules.check(d)['warnings']
    d['research'][-1]['read'] = 'script pp.15–21 read: high, middle, low'
    assert not deck_rules.check(d)['warnings']
    d['research'][-1]['read'] = '封面页与目录'
    d['research_gaps'] = 'ECR 原件网上连扫描图片版也找不到'
    assert not deck_rules.check(d)['warnings']
    d['research_gaps'] = 'ECR 只有扫描图片，无 OCR'
    assert deck_rules.check(d)['warnings']
    # Reports carry no absolute build paths.
    src = tmp_path / 'deck.json'
    src.write_text(json.dumps(deck(), ensure_ascii=False), encoding='utf-8')
    build_cards.main([str(src), str(tmp_path / 'out'), '--audio-pending'])
    report = json.loads((tmp_path / 'out' / 'report.json').read_text(encoding='utf-8'))
    assert str(tmp_path) not in json.dumps(report, ensure_ascii=False)


# ---------------------------------------------------------------- dry-eye paper and board cards

def test_light_themes_stay_below_the_dry_eye_paper(tmp_path):
    """No light-mode page, panel or tinted box is brighter than the reference paper #f6f1e7; a white panel fails."""
    themes = tmp_path / 'themes'
    shutil.copytree(ROOT / 'assets/ccpt6/themes', themes)
    paper = themes / 'paper.css'
    text = paper.read_text(encoding='utf-8')
    assert '--surface:#f6f1e7' in text and '#ffffff;--surface-2' not in text
    paper.write_text(text.replace('--surface:#f6f1e7', '--surface:#ffffff', 1), encoding='utf-8')
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/contrast_check.py'), str(themes)], capture_output=True, text=True)
    assert result.returncode == 1 and 'dry-eye paper cap' in result.stdout
    for css in (ROOT / 'assets/ccpt6/themes').glob('*.css'):  # night palettes were not part of the change
        assert re.search(r'\.nightMode \.ccpt6\[data-theme="[a-z]+"\],\.night_mode', css.read_text(encoding='utf-8'))


def board_png(path, name_row=True):
    """A white 1300-px board: an optional private header, then three ink blocks of two lines each."""
    from PIL import Image, ImageDraw
    image = Image.new('RGB', (1300, 1400), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    if name_row:
        draw.rectangle((60, 30, 500, 70), fill=(90, 90, 90))           # the "student name" line to be masked
    for top, colour in ((200, (20, 20, 20)), (600, (210, 30, 30)), (1000, (20, 70, 200))):
        for line in range(2):
            y = top + line * 60
            draw.rectangle((80, y, 700, y + 30), fill=colour)
    image.save(path)
    return path


def board_deck(tmp_path):
    board_png(tmp_path / 'board.png')
    d = deck()
    d['board'] = [{'id': 'B01', 'where': '板书上方', 'point': 'statistic 的定义', 'items': ['S-1']},
                  {'id': 'B02', 'where': '板书中部', 'point': '红笔：参数不是统计量', 'items': ['S-1']},
                  {'id': 'B03', 'where': '板书下方', 'point': '离题例子', 'items': [], 'note': '离题', 'not_shown': '老师的题外话'}]
    d['cards'] = [{'id': 'BD1', 'genre': 'board', 'title': 'Statistic：只用样本算出的量', 'covers': ['S-1'], 'sources': ['本课板书'],
                   'blocks': [{'type': 'board', 'src': 'board.png', 'masks': [[50, 20, 520, 80]], 'crops': [
                       {'box': [40, 10, 760, 300], 'where': '板书上方', 'points': ['B01'], 'speech': '这一块是定义。',
                        'spots': [{'box': [70, 190, 720, 240], 'speech': '第一行：只用样本。', 'step': True},
                                  {'box': [70, 250, 720, 300], 'speech': '第二行：不含未知参数。'}]},
                       {'box': [60, 580, 720, 700], 'where': '板书中部', 'points': ['B02'], 'speech': '红笔提醒：总体参数不是统计量。'}]}]}]
    d['demands'][0]['cards'] = ['BD1']
    d['coverage']['backcheck'][1]['fixed_by'] = ['BD1']
    d['coverage']['coldread'] = [{'card': 'BD1', 'missing': [], 'fixed_by': []}]
    return d


def test_board_card_builds_masks_and_delivers_crop_only_sources(tmp_path):
    from PIL import Image
    d = board_deck(tmp_path)
    assert deck_rules.check(d)['coverage']['missing'] == []        # a term point is taught by the board that shows it
    src = tmp_path / 'deck.json'
    src.write_text(json.dumps(d, ensure_ascii=False), encoding='utf-8')
    out = tmp_path / 'out'
    build_cards.main([str(src), str(out), '--audio-pending'])
    page = json.loads((out / 'pages.json').read_text(encoding='utf-8'))['BD1']
    names = re.findall(r'src="(ccpt6-board-[0-9a-f]{16}\.png)"', page)
    assert len(names) == 2 and 'data-tone="light"' in page and page.count('class="bd-spot"') == 2 and 'bd-sep' in page
    assert 'data-genre="board"' in page and '板书' in page
    with zipfile.ZipFile(next(out.glob('*.apkg'))) as z:
        assert set(names) <= set(json.loads(z.read('media')).values())
    # The masked header is painted out in the crop that overlaps it.
    first = Image.open(out / 'media' / names[0]).convert('RGB')
    assert first.getpixel((100, 40)) == (255, 255, 255)
    # Narration: the crop first, then its spots in order, then the next crop.
    manifest = json.loads((out / 'speech-manifest.json').read_text(encoding='utf-8'))[0]
    assert [s['target'] for s in manifest['segments']] == [None, 'b0-c0', 'b0-c0-s0', 'b0-c0-s1', 'b0-c1']
    # The delivered folder rebuilds alone, and its board copy holds only the cropped areas (header masked).
    delivered = json.loads((out / 'deck.json').read_text(encoding='utf-8'))
    copy = delivered['cards'][0]['blocks'][0]['src']
    assert copy.startswith('board/') and 'masks' not in delivered['cards'][0]['blocks'][0]
    sheet = Image.open(out / copy).convert('RGB')
    assert sheet.getpixel((100, 40)) == (255, 255, 255) and sheet.getpixel((300, 1010)) == (255, 255, 255)  # name, uncropped block
    assert sheet.getpixel((300, 210)) == (20, 20, 20)
    build_cards.main([str(out / 'deck.json'), str(tmp_path / 'again'), '--preview'])
    preview = (tmp_path / 'again' / 'BD1.html').read_text(encoding='utf-8')
    assert sorted(re.findall(r'src="media/(ccpt6-board-[0-9a-f]{16}\.png)"', preview)) == sorted(names)
    # Speed rule: spots marked "step" are the teacher's derivation steps.
    report = json.loads((out / 'report.json').read_text(encoding='utf-8'))
    assert report['cards'][0]['metrics']['S'] == 1 and report['cards'][0]['metrics']['worked']


@pytest.mark.parametrize('mutate, error, message', [
    (lambda d: d['board'][1].update(not_shown=None) or d['cards'][0]['blocks'][0]['crops'][1].update(points=[]), deck_rules.DeckError, 'not_shown'),
    (lambda d: d['cards'][0]['blocks'][0]['crops'][0].update(points=['B99']), deck_rules.DeckError, 'board point ids'),
    (lambda d: d['cards'][0].update(blocks=[{'type': 'lead', 'text': '只有文字'}]), deck_rules.DeckError, 'board block'),
    (lambda d: d['cards'][0]['blocks'][0]['crops'][1].update(speech=''), blocks.BlockError, 'narration explains the board'),
    (lambda d: d['cards'][0]['blocks'][0]['crops'][1].update(box=[60, 580, 1720, 700]), SystemExit, 'outside the image'),
    (lambda d: d['cards'][0]['blocks'][0]['crops'][0]['spots'][0].update(box=[70, 900, 720, 950]), SystemExit, 'outside its crop'),
    (lambda d: d['cards'][0]['blocks'][0].update(src='missing.png'), SystemExit, 'not found'),
])
def test_board_rules(tmp_path, mutate, error, message, capsys):
    d = board_deck(tmp_path)
    mutate(d)
    if error is SystemExit:
        src = tmp_path / 'deck.json'
        src.write_text(json.dumps(d, ensure_ascii=False), encoding='utf-8')
        with pytest.raises(SystemExit) as stop:
            build_cards.main([str(src), str(tmp_path / 'out'), '--preview'])
        assert message in str(stop.value)
    elif error is blocks.BlockError:
        with pytest.raises(blocks.BlockError, match=message):
            blocks.render_block(d['cards'][0]['blocks'][0], 'b0', 'w')
    else:
        with pytest.raises(error, match=message):
            deck_rules.check(d)


def test_board_lint_keeps_the_board_central():
    card = {'id': 'BD1', 'genre': 'board', 'title': 't', 'blocks': [
        {'type': 'note', 'text': '这是一段很长的打字讲解，' * 14},
        {'type': 'board', 'src': 'b.png', 'crops': [{'box': [0, 0, 10, 10], 'speech': '讲解这一块板书的每一行内容，' * 8}]}]}
    warnings = build_cards.lint_card(card)
    assert any('以板书为主' in w for w in warnings) and any('spots' in w for w in warnings)


def test_board_regions_follow_blank_rows(tmp_path):
    import board_images
    from PIL import Image
    board_png(tmp_path / 'b.png', name_row=False)
    image = Image.open(tmp_path / 'b.png').convert('RGB')
    bg, regions = board_images.propose(image)
    assert bg == (255, 255, 255) and board_images.tone_of(bg) == 'light'
    assert [r['box'][1] // 100 for r in regions] == [1, 5, 9]          # three blocks; the two lines of each stay together
    out = tmp_path / 'regions'
    board_images.main([str(tmp_path / 'b.png'), str(out)])
    info = json.loads((out / 'regions.json').read_text(encoding='utf-8'))
    assert len(info['regions']) == 3 and info['pages'] and Path(info['pages'][0]['file']).is_file()
    assert info['crop_template'][0]['box'] == info['regions'][0]['box']
    assert board_images.union([r['box'] for r in regions[:2]]) == [regions[0]['box'][0], regions[0]['box'][1], regions[1]['box'][2], regions[1]['box'][3]]
    assert board_images.tone_of((25, 60, 40)) == 'dark' and board_images.tone_of((128, 128, 128)) == 'keep'
