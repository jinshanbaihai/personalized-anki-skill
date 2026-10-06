"""Judge actual HTML attributes, not words in compatibility scripts or teaching text."""
import json
from validate_package import inspect_page

base = '<main data-side="read"><button data-audio="ccpt_fixture.mp3">Play</button><audio src="ccpt_fixture.mp3"></audio>{content}</main>'
for content in (
    '<script>const selectors = "[data-choice], [data-correct]";</script>',
    '<p>说明中可以出现 <code>data-choice</code> 或 data-correct。</p>',
    '<!-- <button data-choice="old">retired example</button> -->',
    '<p data-note="data-choice">An unrelated attribute value is not a quiz.</p>',
):
    assert inspect_page(base.format(content=content)) == 'ccpt_fixture.mp3'

for content in (
    '<div data-choice="A">An actual answer choice</div>',
    '<span data-correct>Actual answer metadata</span>',
    '<button DATA-CHOICE="B">Uppercase HTML attribute</button>',
):
    try:
        inspect_page(base.format(content=content))
    except AssertionError as error:
        assert 'quiz attributes' in str(error), str(error)
    else:
        raise AssertionError('Actual quiz attributes must be rejected: ' + content)

print(json.dumps({'script_text_teaching_text_and_comments_are_not_quizzes':True,'actual_quiz_attributes_rejected':3,'case_insensitive_html_attributes_checked':True}))
