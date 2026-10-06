"""CCPT single-face reading cards for Anki desktop: Space plays/pauses narration, Enter = Good,
1 = Again (next learning day with the CCPT reading preset). Other cards keep Anki's own keys.

Install by double-clicking ccpt_single_face.ankiaddon (written next to every built deck by
scripts/build_cards.py, or by scripts/package_addon.py). No scheduling setting is changed unless
the user picks Tools → "CCPT：当前牌组使用阅读预设".
Checked against aqt 26.9.3: Reviewer.state/_showAnswer/_answerCard/_shortcutKeys,
gui_hooks.state_shortcuts_will_change, reviewer_did_show_question, webview_did_receive_js_message.
"""
from aqt import mw, gui_hooks
from aqt.qt import Qt, QTimer, QApplication, QObject, QEvent, QAction
from aqt.reviewer import Reviewer
from aqt.utils import tooltip, askUser

MARKER = 'data-ccpt-single'
ONE_DAY = 1440.0
_hinted = set()
_api_ok = all(hasattr(Reviewer, name) for name in ('_answerCard', '_showAnswer'))


def is_reading(reviewer):
    if not _api_ok or mw.state != 'review' or not getattr(reviewer, 'card', None):
        return False
    return MARKER in reviewer.card.template().get('qfmt', '')


def steps_are_daily(card):
    conf = mw.col.decks.config_dict_for_deck_id(card.odid or card.did)
    return all(d >= ONE_DAY for d in conf['new']['delays']) and all(d >= ONE_DAY for d in conf['lapse']['delays'])


def grade(reviewer, ease):
    if not is_reading(reviewer) or reviewer.state != 'answer':
        return
    card = reviewer.card
    if ease == 1 and card.did not in _hinted and not steps_are_daily(card):
        _hinted.add(card.did)
        tooltip('这个牌组的学习步长短于 1 天，按 1 的卡今天还会再出现。<br>工具 → CCPT：当前牌组使用阅读预设，可改成隔天再看。', period=6000)
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


CONTROLS = {' ': 'audio', 'Space': 'audio', Qt.Key.Key_Space: 'audio', Qt.Key.Key_Return: 'good', Qt.Key.Key_Enter: 'good', '1': 'again'}


def route(shortcuts):
    """Wrap Space/Enter/1 so CCPT cards get the reading actions and every other card keeps its own."""
    reviewer = mw.reviewer
    found_one = False
    for i, (key, callback) in enumerate(list(shortcuts)):
        name = CONTROLS.get(key)
        if not name:
            continue
        found_one = found_one or key == '1'

        def routed(name=name, fallback=callback):
            if is_reading(reviewer):
                action(reviewer, name)
            else:
                fallback()
        shortcuts[i] = (key, routed)
    if not found_one:
        shortcuts.append(('1', lambda: action(reviewer, 'again')))
    return shortcuts


if hasattr(gui_hooks, 'state_shortcuts_will_change'):
    def on_shortcuts(state, shortcuts):
        if state == 'review':
            route(shortcuts)
    gui_hooks.state_shortcuts_will_change.append(on_shortcuts)
elif hasattr(Reviewer, '_shortcutKeys'):  # older Anki: patch the private table instead
    _original = Reviewer._shortcutKeys
    Reviewer._shortcutKeys = lambda self: route(list(_original(self)))


def show_complete(card):
    reviewer = mw.reviewer
    if not is_reading(reviewer):
        return
    card_id = card.id

    def ready():
        if is_reading(reviewer) and reviewer.card.id == card_id and reviewer.state == 'question':
            reviewer._showAnswer()
    QTimer.singleShot(0, ready)


gui_hooks.reviewer_did_show_question.append(show_complete)


def message(handled, msg, context):
    if handled[0] or msg not in ('ccpt-single:good', 'ccpt-single:again'):
        return handled
    if context is mw.reviewer and is_reading(mw.reviewer):
        grade(mw.reviewer, 3 if msg.endswith('good') else 1)
        return (True, None)
    return handled


gui_hooks.webview_did_receive_js_message.append(message)


class RepeatGuard(QObject):
    """Holding a key must not grade a stream of cards."""
    def eventFilter(self, obj, event):
        if event.type() in (QEvent.Type.ShortcutOverride, QEvent.Type.KeyPress) and event.isAutoRepeat():
            if event.key() in (Qt.Key.Key_Space, Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_1) and is_reading(mw.reviewer):
                event.accept()
                return True
        return False


_repeat_guard = RepeatGuard(mw)
QApplication.instance().installEventFilter(_repeat_guard)


def apply_reading_preset():
    """Clone the current deck's options, change only the learning steps to 1 day, assign to the deck tree."""
    if not mw.col:
        return
    deck = mw.col.decks.current()
    current = mw.col.decks.config_dict_for_deck_id(deck['id'])
    names = '、'.join(mw.col.decks.name(d) for d in mw.col.decks.deck_and_child_ids(deck['id'])[:4])
    if not askUser(f'把“{deck["name"]}”（含子牌组：{names}…）设为 CCPT 阅读预设？\n\n只改两项：新卡与遗忘卡的学习步长都设为 1 天（按 1 = 下一个学习日再看，Enter 的新卡也隔天出现）；'
                   'leech 只加标签不暂停。其余选项（每日数量、FSRS、retention）沿用当前预设。'):
        return
    conf_id = mw.col.decks.add_config_returning_id(f'CCPT 阅读（{current["name"]}）', clone_from=current)
    conf = mw.col.decks.get_config(conf_id)
    conf['new']['delays'] = [ONE_DAY]
    conf['lapse']['delays'] = [ONE_DAY]
    conf['lapse']['leechAction'] = 1
    mw.col.decks.update_config(conf)
    for did in mw.col.decks.deck_and_child_ids(deck['id']):
        d = mw.col.decks.get(did)
        mw.col.decks.set_config_id_for_deck_dict(d, conf_id)
        mw.col.decks.save(d)
    tooltip('已应用 CCPT 阅读预设：之后按 1 的卡在下一个学习日出现。已在今天队列里的卡不会被移动。', period=6000)


_menu = QAction('CCPT：当前牌组使用阅读预设（1 = 隔天再看）', mw)
_menu.triggered.connect(apply_reading_preset)
mw.form.menuTools.addAction(_menu)

if not _api_ok:
    gui_hooks.main_window_did_init.append(lambda: tooltip('CCPT 单面卡插件：这个 Anki 版本的 reviewer 接口已变化，请更新插件。', period=8000))
