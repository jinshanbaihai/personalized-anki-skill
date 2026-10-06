from html_integrity import validate_markup
"""Regressions from five actual board-card comparison strings swallowed as HTML."""
import json
from html.parser import HTMLParser
from pathlib import Path
from build_map_deck import passive_html, validate

CASES = [
    ('B03/b', '<p>若 MSB<MSC，多一单位反而净损失，应该减少。</p>', '多一单位反而净损失'),
    ('B06/b', '<p><strong>MSC<MPC，MPB=MSB</strong></p>', 'MPC，MPB=MSB'),
    ('B08/b', '<p>Qm<Q*：少做的那些单位原本 MSB>MSC。</p>', '少做的那些单位原本'),
    ('S02/a', '<p>Qm<Q*。红线是 <strong>MPC−subsidy</strong>。</p>', '红线是'),
    ('S03/b', '<p>MSC<MPC，MPB=MSB。企业得不到全部社会 benefit，市场停在较低 Qm。</p>', '企业得不到全部社会'),
]
class ReadText(HTMLParser):
    def __init__(self, value):
        super().__init__(convert_charrefs=True);self.parts=[];self.feed(value);self.close()
    def handle_data(self, text):self.parts.append(text)

for name, bad, lost in CASES:
    assert lost not in ''.join(ReadText(bad).parts), 'Fixture must reproduce actual text loss: '+name
    try:passive_html(bad)
    except AssertionError as e:assert '&lt;' in str(e) and 'Unexpected' in str(e), str(e)
    else:raise AssertionError('Swallowed comparison passed: '+name)
    # Escape the comparison operator alone, preserving real markup.
    fixed=bad.replace('<MSC','&lt;MSC').replace('<MPC','&lt;MPC').replace('<Q*','&lt;Q*')
    passive_html(fixed)
    assert lost in ''.join(ReadText(fixed).parts), 'Corrected teaching must remain visible: '+name

passive_html('<p>Q &lt; Q* and MSB &gt; MSC; P ≥ 0.</p><table><tr><td>net</td><td>+2</td></tr></table>')
passive_html('<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mfrac><msub><mi>P</mi><mi>x</mi></msub><msub><mi>P</mi><mi>y</mi></msub></mfrac><mo>&lt;</mo><mn>1</mn></mrow><annotation-xml encoding="MathML-Content"><apply><lt/><ci>x</ci><cn>1</cn></apply></annotation-xml></semantics></math>')
passive_html('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><title>A labelled graph</title><desc>A passive example</desc><defs><linearGradient id="shade"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient><clipPath id="clip"><rect width="100" height="100"/></clipPath></defs><g clip-path="url(#clip)"><path d="M10 90 L90 10" stroke="#000"/><text x="10" y="20"><tspan>X</tspan></text></g></svg>')
for bad in ['<p>text</mystery>', '<made-up>lost</made-up>']:
    try:passive_html(bad)
    except AssertionError:pass
    else:raise AssertionError('Unknown element accepted')
root=Path(__file__).resolve().parent.parent
for name in ['map-example.json','knowledge-example.json']:
    validate(json.loads((root/'assets'/name).read_text()))
print(json.dumps({'actual_five_swallowed_comparisons_rejected':True,'escaped_comparisons_keep_the_missing_explanations':True,'valid_html_svg_mathml_and_content_annotations_preserved':True,'both_shipped_fixtures_valid':True}))

# Independent review found collisions with legitimate HTML s/q element names.
for bad in ("<p>If D<S the price falls.</p>", "<p>At P<Q and Q<10, shortage persists.</p>", "<p>If D<S the price falls>"):
    try:
        validate_markup(bad)
    except AssertionError:
        pass
    else:
        raise AssertionError("Known-tag comparison must not silently swallow text: " + bad)
for good in ('<p>If D&lt;S the price falls.</p>', '<p>At P&lt;Q and Q&lt;10, shortage persists.</p>', '<p><q>Quoted</q> and <s>replaced</s></p>', '<ul><li>First<li>Second</ul>', '<table><tr><td>A<td>B</table>', '<p title="D<S">Quoted attribute is valid</p>'):
    validate_markup(good)
