"""Scoped desktop adapter for CCPT single-face reading cards. No scheduling overrides."""
from functools import wraps
from aqt import mw, gui_hooks
from aqt.qt import Qt, QTimer, QApplication, QObject, QEvent
from aqt.reviewer import Reviewer

MARKER = 'data-ccpt-single'
def is_reading(reviewer):
    if mw.state != 'review' or not reviewer.card:
        return False
    return MARKER in reviewer.card.template().get('qfmt', '')

def grade(reviewer, ease):
    if not is_reading(reviewer) or reviewer.state != 'answer':
        return
    reviewer.web.eval('if(window.ccptCleanup)window.ccptCleanup();')
    reviewer._answerCard(ease)

def action(reviewer, name):
    if not is_reading(reviewer):
        return
    card_id = reviewer.card.id
    def checked(editable):
        if editable or not is_reading(reviewer) or reviewer.card.id != card_id:
            return
        if name == 'audio':
            reviewer.web.eval("window.ccptSingleAction && window.ccptSingleAction('audio');")
        elif name == 'good':
            grade(reviewer, 3)
        elif name == 'again':
            grade(reviewer, 1)
    reviewer.web.evalWithCallback("(()=>{const e=document.activeElement;return !!(e?.isContentEditable||/^(INPUT|TEXTAREA|SELECT)$/.test(e?.tagName||''));})()", checked)

_original_shortcuts = Reviewer._shortcutKeys
@wraps(_original_shortcuts)
def shortcuts(self):
    rows = list(_original_shortcuts(self))
    controls = {' ': 'audio', Qt.Key.Key_Space: 'audio', Qt.Key.Key_Return: 'good', Qt.Key.Key_Enter: 'good', '1': 'again'}
    result = []
    found_one = False
    for key, callback in rows:
        name = controls.get(key)
        if name:
            if key == '1': found_one = True
            def routed(name=name, fallback=callback):
                if is_reading(self): action(self, name)
                else: fallback()
            result.append((key, routed))
        else:
            result.append((key, callback))
    if not found_one:
        result.append(('1', lambda: action(self, 'again')))
    return result
Reviewer._shortcutKeys = shortcuts

def show_complete(card):
    reviewer = mw.reviewer
    if not is_reading(reviewer): return
    card_id = card.id
    def ready():
        if is_reading(reviewer) and reviewer.card.id == card_id and reviewer.state == 'question':
            reviewer._showAnswer()
    QTimer.singleShot(0, ready)
gui_hooks.reviewer_did_show_question.append(show_complete)

def message(handled, message, context):
    if handled[0] or message not in ('ccpt-single:good', 'ccpt-single:again'):
        return handled
    if context is mw.reviewer and is_reading(mw.reviewer):
        grade(mw.reviewer, 3 if message.endswith('good') else 1)
        return (True, None)
    return handled
gui_hooks.webview_did_receive_js_message.append(message)

class RepeatGuard(QObject):
    def eventFilter(self, obj, event):
        if event.type() in (QEvent.Type.ShortcutOverride, QEvent.Type.KeyPress) and event.isAutoRepeat():
            if event.key() in (Qt.Key.Key_Space, Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_1) and is_reading(mw.reviewer):
                event.accept()
                return True
        return False
_repeat_guard = RepeatGuard(mw)
QApplication.instance().installEventFilter(_repeat_guard)
