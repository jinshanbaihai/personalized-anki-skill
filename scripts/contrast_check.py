"""WCAG 2.x contrast audit of every theme's light and night tokens.

Usage: python scripts/contrast_check.py [assets/ccpt6/themes]

Text pairs must reach 4.5:1 (SC 1.4.3); meaningful non-text marks (map wires, node edges, chart
lines, control borders, narration focus ring) must reach 3:1 (SC 1.4.11). Prints a markdown table
and exits non-zero on any failure.
"""
import re
import sys
from pathlib import Path

THEMES = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / 'assets' / 'ccpt6' / 'themes'
TEXT = [('ink', 'bg'), ('ink', 'surface'), ('ink', 'surface-2'), ('ink-2', 'bg'), ('ink-2', 'surface'), ('ink-2', 'surface-2'),
        ('accent', 'bg'), ('accent', 'surface'), ('accent', 'surface-2'), ('accent-ink', 'accent'), ('ink', 'accent-soft'),
        ('wire', 'bg'), ('wire', 'surface'), ('ink', 'kw'), ('good', 'good-soft'), ('good', 'surface'), ('bad', 'bad-soft'),
        ('bad', 'surface'), ('ink-2', 'good-soft'), ('ink-2', 'bad-soft'), ('pen', 'surface'), ('pen', 'bg'),
        ('mark-ink', 'mark-bg'), ('surface', 'bad'), ('ink', 'good-soft'), ('ink', 'bad-soft'),
        ('good', 'surface-2'), ('bad', 'surface-2'), ('pen', 'surface-2'), ('wire', 'surface-2'), ('accent', 'accent-soft'), ('ink-2', 'accent-soft')]
NONTEXT = [('rule-strong', 'bg'), ('rule-strong', 'surface'), ('wire', 'surface-2'), ('focus', 'bg'), ('focus', 'surface'),
           ('accent', 'surface'), ('c1', 'surface'), ('c2', 'surface'), ('c3', 'surface'), ('c1', 'bg'), ('c2', 'bg'), ('c3', 'bg'),
           ('k-policy', 'surface'), ('k-effect', 'surface'), ('k-cond', 'surface'), ('k-eval', 'accent-soft'),
           ('k-example', 'good-soft'), ('k-limit', 'bad-soft')]


def lum(hexv):
    h = hexv.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    rgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def tokens(block):
    return {m.group(1): m.group(2).strip() for m in re.finditer(r'--([\w-]+):\s*(#[0-9a-fA-F]{3,6})\b', block)}


rows, fails = [], []
for theme in ['editorial', 'paper', 'lab', 'blueprint', 'manuscript']:
    css = (THEMES / f'{theme}.css').read_text(encoding='utf-8')
    light = re.search(r'\.ccpt6\[data-theme="%s"\]\{([^}]*)\}' % theme, css).group(1)
    dark = re.search(r'\.nightMode \.ccpt6\[data-theme="%s"\],\.night_mode \.ccpt6\[data-theme="%s"\]\{([^}]*)\}' % (theme, theme), css).group(1)
    for mode, block in (('light', light), ('night', dark)):
        t = tokens(block)
        worst_text, worst_non = (99, ''), (99, '')
        for kind, pairs, floor in (('text', TEXT, 4.5), ('non-text', NONTEXT, 3.0)):
            for fg, bg in pairs:
                if fg not in t or bg not in t:
                    fails.append(f'{theme}/{mode}: missing token {fg} or {bg}')
                    continue
                r = ratio(t[fg], t[bg])
                if r < floor:
                    fails.append(f'{theme}/{mode}: {kind} {fg} on {bg} = {r:.2f} < {floor}')
                if kind == 'text' and r < worst_text[0]:
                    worst_text = (r, f'{fg}/{bg}')
                if kind == 'non-text' and r < worst_non[0]:
                    worst_non = (r, f'{fg}/{bg}')
        rows.append(f'| {theme} | {mode} | {t["bg"]} | {ratio(t["ink"], t["bg"]):.1f} | {ratio(t["ink-2"], t["bg"]):.1f} | {ratio(t["accent"], t["bg"]):.1f} | '
                    f'{worst_text[0]:.2f} ({worst_text[1]}) | {worst_non[0]:.2f} ({worst_non[1]}) |')
print('| theme | mode | bg | ink | ink-2 | accent | 最低文字对比（对） | 最低非文字对比（对） |')
print('|---|---|---|---|---|---|---|---|')
print('\n'.join(rows))
print(f'\n{len(TEXT)} text pairs (≥4.5) + {len(NONTEXT)} non-text pairs (≥3.0) per theme×mode')
if fails:
    print('\nFAILURES:\n' + '\n'.join(fails))
    sys.exit(1)
print('all pass')
