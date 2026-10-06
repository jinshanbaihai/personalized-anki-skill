"""Regression tests for the ccpt-6 builder. Synthetic content checks structure, not teaching quality."""
import copy
import json
import re
import shutil
import subprocess
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
        'style': {'theme': 'lab', 'voice': 'xiaoxiao', 'speed': 2.0},
        'exam': {'board': 'Pearson Edexcel', 'qualification': 'IAL Mathematics', 'code': 'YMA01', 'units': ['WST02'],
                 'spec_version': 'Issue 3 (April 2019)', 'spec_url': 'https://example.invalid/spec.pdf',
                 'identified_by': 'exclusive-content', 'evidence': ['synthetic evidence'],
                 'ruled_out': [{'candidate': 'UK 9MA0', 'why_not': 'synthetic reason'}]},
        'research': [
            {'type': 'spec', 'ref': 'synthetic spec', 'read': 'p.59', 'used_for': 'scope'},
            {'type': 'ms', 'ref': 'synthetic MS', 'read': 'Q2', 'used_for': 'keywords'},
            {'type': 'er', 'ref': 'synthetic ER', 'read': 'Q2', 'used_for': 'pitfalls'},
        ],
        'board': [{'id': 'B01', 'where': 'p1', 'point': 'statistic definition', 'items': ['S-1']}],
        'coverage': {'scope': 'synthetic 4.2', 'status': 'complete', 'remaining': '', 'items': [
            {'id': 'S-1', 'spec': '4.2', 'point': 'statistic', 'class': 'core', 'level': 'MS keywords'},
            {'id': 'X-1', 'spec': 'S3 3.6', 'point': 'CLT', 'class': 'excluded', 'reason': 'other unit'}]},
        'cards': [{
            'id': 'T01', 'genre': 'term', 'title': 'Statistic', 'covers': ['S-1'], 'sources': ['synthetic'],
            'blocks': [
                {'type': 'lead', 'text': '只用样本就能算出的量'},
                {'type': 'definition', 'term': 'Statistic', 'text': 'A quantity calculated only from the sample, containing no unknown parameters.',
                 'keywords': ['only from the sample', 'no unknown parameters'], 'reject': ['because it is known']},
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
    (lambda d: d['coverage']['items'].append({'id': 'S-2', 'spec': '4.1', 'point': 'frame', 'class': 'core', 'level': 'x'}), 'no card'),
    (lambda d: d['coverage']['items'][0].pop('level'), 'level'),
    (lambda d: d['board'][0].update(items=[]), 'maps to no syllabus point'),
    (lambda d: d['cards'][0].update(speed=1.5), 'complex enough'),
    (lambda d: d['style'].update(speed=3), 'style.speed'),
])
def test_deck_rules_reject(mutate, message):
    d = deck()
    mutate(d)
    with pytest.raises(deck_rules.DeckError, match=message):
        deck_rules.check(d)


def test_existing_card_counts_as_coverage():
    d = deck()
    d['coverage']['items'].append({'id': 'S-2', 'spec': '4.1', 'point': 'frame', 'class': 'core', 'level': 'x', 'existing': 'IAL S2::T07'})
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
    raw = build_cards.source_record(d, d['cards'][0])
    assert '<' not in raw and json.loads(raw)['covers'] == ['S-1']


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
    d = deck()
    d['cards'][0]['speed'] = 1.5
    d['cards'][0]['speed_reason'] = 'test'
    src = tmp_path / 'deck.json'
    src.write_text(json.dumps(d, ensure_ascii=False))
    build_cards.main([str(src), str(tmp_path / 'out')])
    manifest = json.loads((tmp_path / 'out' / 'speech-manifest.json').read_text())[0]
    assert manifest['available'] and manifest['speed'] == 1.5 and manifest['tempo_filter'] == 'atempo=1.5'
    cues = manifest['narration']['cues']
    assert cues[0]['target'] is None and [c['target'] for c in cues][1:4] == ['b0', 'b1', 'b2-s0']
    page = json.loads((tmp_path / 'out' / 'pages.json').read_text())['T01']
    assert inspect_page(page) == manifest['file'] and 'data-encoded="1.5"' in page
