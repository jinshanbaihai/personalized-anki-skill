"""CCPT single-face reading cards for Anki desktop: Space plays/pauses narration, Enter = Good,
1 = Again (next learning day with the CCPT reading preset). Other cards keep Anki's own keys.

Install by double-clicking ccpt_single_face.ankiaddon (written next to every built deck by
scripts/build_cards.py, or by scripts/package_addon.py). No scheduling setting is changed unless
the user accepts the one-time prompt (shown when a deck's learning steps are shorter than a day) or picks
Tools → "CCPT：当前牌组使用阅读预设".
Checked against aqt 26.9.3: Reviewer.state/_showAnswer/_answerCard, AnkiWebView.setPlaybackRequiresGesture,
gui_hooks.state_shortcuts_will_change, reviewer_did_show_question,
DeckManager.config_dict_for_deck_id/add_config_returning_id/set_config_id_for_deck_dict/deck_and_child_ids/is_filtered.
Needs Anki 2.1.50 or newer (manifest min_point_version).
"""
from anki.decks import DeckManager
from aqt import mw, gui_hooks
from aqt.qt import Qt, QTimer, QAction
from aqt.reviewer import Reviewer
from aqt.utils import tooltip, askUser

MARKER = 'data-ccpt-single'
ONE_DAY = 1440.0
PRESET_PREFIX = 'CCPT 阅读'
_checked_decks = set()
_api_ok = (all(hasattr(Reviewer, name) for name in ('_answerCard', '_showAnswer'))
           and all(hasattr(DeckManager, name) for name in ('config_dict_for_deck_id', 'add_config_returning_id',
                                                             'set_config_id_for_deck_dict', 'deck_and_child_ids'))
           and hasattr(gui_hooks, 'state_shortcuts_will_change'))


def is_reading(reviewer):
    if not _api_ok or mw.state != 'review' or not getattr(reviewer, 'card', None):
        return False
    return MARKER in reviewer.card.template().get('qfmt', '')


def steps_are_daily(did):
    conf = mw.col.decks.config_dict_for_deck_id(did)
    return all(d >= ONE_DAY for d in conf['new']['delays']) and all(d >= ONE_DAY for d in conf['lapse']['delays'])


def check_steps_once(card):
    """First CCPT card from a deck this session: with Anki's default steps (1m 10m), Enter and 1 bring the
    same long card back within minutes. Offer the reading preset once, before the user wonders why."""
    did = card.odid or card.did
    if did in _checked_decks:
        return
    _checked_decks.add(did)
    try:
        daily = steps_are_daily(did)
    except Exception:  # noqa: BLE001 - a hint must never get in the way of reviewing
        return
    if daily:
        return
    top = family_top(did)
    if askUser(f'“{mw.col.decks.name(top)}”的学习步长短于 1 天：按 Enter 的新卡和按 1 的卡今天几分钟后还会再出现。\n\n'
               '要改成 CCPT 阅读预设吗？（只改学习步长为 1 天、leech 只加标签；其余设置不变。选“否”则什么都不改，之后也可以在“工具”菜单里改。）',
               defaultno=True):
        apply_reading_preset(top)


def family_top(did):
    """The highest ancestor that shares this deck's preset, so one answer covers the whole delivered deck
    (cards usually live in subdecks such as Deck::Terms)."""
    decks = mw.col.decks
    conf_id = decks.config_dict_for_deck_id(did)['id']
    name, top = decks.name(did), did
    while '::' in name:
        name = name.rsplit('::', 1)[0]
        parent = decks.by_name(name)
        if not parent or parent.get('dyn') or decks.config_dict_for_deck_id(parent['id'])['id'] != conf_id:
            break
        top = parent['id']
    return top


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


def on_shortcuts(state, shortcuts):
    if state == 'review' and _api_ok:
        route(shortcuts)


if hasattr(gui_hooks, 'state_shortcuts_will_change'):
    gui_hooks.state_shortcuts_will_change.append(on_shortcuts)


def show_complete(card):
    reviewer = mw.reviewer
    if not is_reading(reviewer):
        return
    card_id = card.id
    # Space reaches the page through the add-on, not as a click; Anki requires a gesture for audio when the
    # deck says "Don't play audio automatically". CCPT audio never autoplays, so lifting it is safe, and Anki
    # resets the flag for the next card in _showQuestion.
    if hasattr(reviewer.web, 'setPlaybackRequiresGesture'):
        reviewer.web.setPlaybackRequiresGesture(False)

    def ready():
        if is_reading(reviewer) and reviewer.card.id == card_id and reviewer.state == 'question':
            reviewer._showAnswer()
            QTimer.singleShot(0, lambda: check_steps_once(card))
    QTimer.singleShot(0, ready)


gui_hooks.reviewer_did_show_question.append(show_complete)




# Holding a key does not grade a stream of cards: Anki registers reviewer shortcuts without auto-repeat,
# and the page ignores repeated Space (assets/single-face.js).


def apply_reading_preset(did=None):
    """Give the deck (and the subdecks that share its options) a copy of its preset whose learning steps are 1 day.
    Subdecks with their own preset keep it; a preset that is already a CCPT reading preset is reused, not cloned again."""
    if not mw.col or not _api_ok:
        return
    decks = mw.col.decks
    deck = decks.get(did) if did else decks.current()
    if deck.get('dyn'):
        tooltip('这是筛选牌组：请在卡片原来的牌组上使用阅读预设。', period=5000)
        return
    current = decks.config_dict_for_deck_id(deck['id'])
    family = [d for d in decks.deck_and_child_ids(deck['id']) if not decks.get(d).get('dyn')]
    same = [d for d in family if decks.config_dict_for_deck_id(d)['id'] == current['id']]
    skipped = [decks.name(d) for d in family if d not in same]
    note = ('\n\n这些子牌组有自己的预设，保持不变：' + '、'.join(skipped[:6])) if skipped else ''
    if did is None and not askUser(f'把“{deck["name"]}”（及共用同一预设的子牌组，共 {len(same)} 个）设为 CCPT 阅读预设？\n\n'
                                   '只改两项：新卡与遗忘卡的学习步长都设为 1 天（按 1 = 下一个学习日再看，Enter 的新卡也隔天出现）；'
                                   'leech 只加标签不暂停。其余选项（每日数量、FSRS、retention）沿用当前预设。' + note):
        return
    if current['name'].startswith(PRESET_PREFIX):
        conf = current
    else:  # reuse a reading preset made earlier from the same preset instead of cloning it again
        name = f'{PRESET_PREFIX}（{current["name"]}）'
        conf = next((c for c in decks.all_config() if c['name'] == name), None) or decks.get_config(decks.add_config_returning_id(name, clone_from=current))
    conf['new']['delays'] = [ONE_DAY]
    conf['lapse']['delays'] = [ONE_DAY]
    conf['lapse']['leechAction'] = 1
    decks.update_config(conf)
    for d_id in same:
        d = decks.get(d_id)
        decks.set_config_id_for_deck_dict(d, conf['id'])
        decks.save(d)
    # Rebuild the study queue so the card on screen is graded with the new steps too.
    mw.reset()
    tooltip('已应用 CCPT 阅读预设：之后按 1 的卡在下一个学习日出现。已在今天学习队列里的卡不会被移动。', period=6000)


_menu = QAction('CCPT：当前牌组使用阅读预设（1 = 隔天再看）', mw)
_menu.triggered.connect(lambda: apply_reading_preset())
mw.form.menuTools.addAction(_menu)

if not _api_ok:
    gui_hooks.main_window_did_init.append(lambda: tooltip('CCPT 单面卡插件：这个 Anki 版本缺少需要的接口（需要 2.1.50 或更新），插件未接管按键。', period=8000))
