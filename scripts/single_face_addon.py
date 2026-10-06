"""CCPT single-face reading cards for Anki desktop: Space plays/pauses narration, Enter = Good,
1 = Again, seen again on the next learning day. Other cards keep Anki's own keys, and nothing is
intercepted while the focus is in an editable field.

"1 = next learning day" needs learning and relearning steps of at least one day; with Anki's defaults
(1m 10m) a card answered 1, and a new card answered Enter, comes back within minutes. So the first time a
CCPT card (template contains data-ccpt-single) from a deck is shown and that deck's steps are shorter than
a day (or empty, which does not promise the next day), the add-on gives the deck family the reading preset
by itself: the highest ancestor that shares the deck's preset, with the subdecks that share it, moves to
"CCPT 阅读（<old preset>）", a copy of the old preset whose new and lapse steps are 1 day and whose leech
action only tags; nothing else changes. The copy is made once and reused. Subdecks with their own preset,
decks that hold cards but no CCPT card, and filtered decks keep their settings. A tooltip says what
changed and how to undo it; no dialog ever opens during review, so no keypress meant for grading can
answer one.

Tools menu: "CCPT：牌组使用阅读预设" applies the preset on request to every deck family holding CCPT cards
(tag ccpt6 or the single-face template), whatever deck is current; "CCPT：撤销阅读预设" puts back the
presets the add-on replaced, and the add-on never changes those decks by itself again. Each decision is
kept per Anki profile and top deck in the add-on config (Tools → Add-ons → Config, config.json written by
scripts/package_addon.py), so it survives restarts and reinstalls; "auto_reading_preset": false turns the
automatic change off (a tooltip then points to the Tools menu once per session).

Install by double-clicking ccpt_single_face.ankiaddon (written next to every built deck by
scripts/build_cards.py, or by scripts/package_addon.py).
Checked against aqt 26.9.3: Reviewer.state/_showAnswer/_answerCard, AnkiWebView.setPlaybackRequiresGesture,
gui_hooks.state_shortcuts_will_change, reviewer_did_show_question, AddonManager.getConfig/writeConfig,
mw.pm.name, DeckManager.config_dict_for_deck_id/add_config_returning_id/set_config_id_for_deck_dict/
deck_and_child_ids. Needs Anki 2.1.50 or newer (manifest min_point_version).
Tests: scripts/test_addon.py drives this module with a stubbed aqt (keys are simulated, not pressed in a
real Anki window) and checks the resulting schedule against a real anki collection.
"""
import copy
import traceback

from anki.decks import DeckManager
from aqt import mw, gui_hooks
from aqt.qt import Qt, QTimer, QAction
from aqt.reviewer import Reviewer
from aqt.utils import tooltip, askUser

MARKER = 'data-ccpt-single'
TAG = 'ccpt6'
ONE_DAY = 1440.0
PRESET_PREFIX = 'CCPT 阅读'
DEFAULT_CONFIG = {'auto_reading_preset': True, 'decided': {}}  # same as the config.json scripts/package_addon.py ships
UNDO_HINT = '不想要：工具 → CCPT：撤销阅读预设。'
_checked_decks = set()  # (profile, deck id) whose steps were looked at this session
_session = {'config': None, 'hinted': False}
_api_ok = (all(hasattr(Reviewer, name) for name in ('_answerCard', '_showAnswer'))
           and all(hasattr(DeckManager, name) for name in ('config_dict_for_deck_id', 'add_config_returning_id',
                                                             'set_config_id_for_deck_dict', 'deck_and_child_ids'))
           and hasattr(gui_hooks, 'state_shortcuts_will_change'))


def is_reading(reviewer):
    if not _api_ok or mw.state != 'review' or not getattr(reviewer, 'card', None):
        return False
    return MARKER in reviewer.card.template().get('qfmt', '')


# ---------------------------------------------------------------- keys

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
            QTimer.singleShot(0, lambda: auto_preset_once(card))
    QTimer.singleShot(0, ready)


gui_hooks.reviewer_did_show_question.append(show_complete)

# Holding a key does not grade a stream of cards: Anki registers reviewer shortcuts without auto-repeat,
# and the page ignores repeated Space (assets/single-face.js).


# ---------------------------------------------------------------- decks and presets

def steps_are_daily(did):
    """Every learning and relearning step is at least a day. Empty steps do not count: they do not promise
    that a card answered 1 comes back on the next learning day."""
    conf = mw.col.decks.config_dict_for_deck_id(did)
    new, lapse = list(conf['new']['delays']), list(conf['lapse']['delays'])
    return bool(new) and bool(lapse) and all(d >= ONE_DAY for d in new + lapse)


def family_top(did):
    """The highest ancestor that shares this deck's preset, so one decision covers the whole delivered deck
    (cards usually live in subdecks such as Deck::Terms)."""
    decks = mw.col.decks
    conf_id = decks.config_dict_for_deck_id(did)['id']
    top = did
    for parent in lineage(did)[1:]:
        if decks.get(parent).get('dyn') or decks.config_dict_for_deck_id(parent)['id'] != conf_id:
            break
        top = parent
    return top


def lineage(did):
    """The deck and its ancestors, nearest first."""
    decks = mw.col.decks
    out, name = [did], decks.name(did)
    while '::' in name:
        name = name.rsplit('::', 1)[0]
        parent = decks.by_name(name)
        if not parent:
            break
        out.append(parent['id'])
    return out


def ccpt_query():
    """Search for CCPT cards: the ccpt6 tag, or any note type whose template carries the single-face marker."""
    mids = [m['id'] for m in mw.col.models.all() if any(MARKER in t.get('qfmt', '') for t in m.get('tmpls', []))]
    return '(' + ' or '.join([f'tag:{TAG}'] + [f'mid:{mid}' for mid in mids]) + ')'


def only_other_cards(did, query):
    """The deck itself holds cards and none of them is a CCPT card (say, the user's own deck sharing the preset)."""
    find = mw.col.find_cards
    return bool(find(f'did:{did}')) and not find(f'did:{did} {query}')


def ccpt_family_tops():
    """family_top of every deck that holds CCPT cards (home deck for cards in a filtered deck), by name."""
    col = mw.col
    homes = set()
    for cid in col.find_cards(ccpt_query()):
        card = col.get_card(cid)
        homes.add(card.odid or card.did)
    return sorted({family_top(d) for d in homes}, key=col.decks.name)


def apply_reading_preset(did):
    """Give the deck, and the subdecks that share its preset, a copy of that preset whose learning and relearning
    steps are 1 day and whose leech action only tags. Subdecks with their own preset and decks that hold cards but
    no CCPT card keep theirs; a preset that is already a CCPT reading preset is used as it is, and the copy made
    earlier from the same preset is reused rather than cloned again. Returns what undo needs, or None for a
    filtered or missing deck. The caller stores the record and refreshes the study queue."""
    decks = mw.col.decks
    deck = decks.get(did, default=False)
    if not deck:
        return None
    if deck.get('dyn'):
        tooltip('这是筛选牌组：请在卡片原来的牌组上使用阅读预设。', period=5000)
        return None
    current = decks.config_dict_for_deck_id(deck['id'])
    family = [d for d in decks.deck_and_child_ids(deck['id']) if not decks.get(d).get('dyn')]
    query = ccpt_query()
    targets = [d for d in family
               if decks.config_dict_for_deck_id(d)['id'] == current['id'] and not only_other_cards(d, query)]
    fresh = False
    if current['name'].startswith(PRESET_PREFIX):
        conf = current
    else:
        name = f'{PRESET_PREFIX}（{current["name"]}）'
        conf = next((c for c in decks.all_config() if c['name'] == name), None)
        if conf is None:
            conf, fresh = decks.get_config(decks.add_config_returning_id(name, clone_from=current)), True
    before = {'new': list(conf['new']['delays']), 'lapse': list(conf['lapse']['delays']),
              'leechAction': conf['lapse'].get('leechAction')}
    after = {'new': [ONE_DAY], 'lapse': [ONE_DAY], 'leechAction': 1}
    conf['new']['delays'] = list(after['new'])
    conf['lapse']['delays'] = list(after['lapse'])
    conf['lapse']['leechAction'] = after['leechAction']
    decks.update_config(conf)
    original = {}
    for d_id in targets:
        old = decks.config_dict_for_deck_id(d_id)['id']
        if old != conf['id']:
            original[str(d_id)] = old
            decks.set_config_id_for_deck_dict(decks.get(d_id), conf['id'])  # saves the deck
    record = {'state': 'applied', 'deck': deck['name'], 'preset': conf['id'], 'original': original,
              'kept': [decks.name(d) for d in family if d not in targets]}
    if not fresh and before != after:  # an existing preset changed in place: undo puts these values back
        record['preset_before'] = before
    return record


def restore(record):
    """Put back the presets recorded by apply_reading_preset. A deck moved to another preset by hand since then
    keeps it. Returns (number restored, names left as they are)."""
    decks = mw.col.decks
    restored, left = 0, []
    for did_s, old in (record.get('original') or {}).items():
        deck = decks.get(int(did_s), default=False)
        if not deck:
            continue
        if decks.config_dict_for_deck_id(deck['id'])['id'] != record.get('preset'):
            left.append(deck['name'])
            continue
        decks.set_config_id_for_deck_dict(deck, old if decks.get_config(old) else 1)
        restored += 1
    before = record.get('preset_before')
    conf = decks.get_config(record['preset']) if before and record.get('preset') else None
    if conf:
        conf['new']['delays'] = before['new']
        conf['lapse']['delays'] = before['lapse']
        if before.get('leechAction') is not None:
            conf['lapse']['leechAction'] = before['leechAction']
        decks.update_config(conf)
    return restored, left


# ---------------------------------------------------------------- decisions (add-on config)

def _profile():
    return getattr(getattr(mw, 'pm', None), 'name', None) or ''


def load_config():
    """config.json merged with the user's saved values; kept for this session only when there is no add-on manager."""
    cfg = None
    manager = getattr(mw, 'addonManager', None)
    if manager is not None:
        try:
            cfg = manager.getConfig(__name__)
        except Exception:  # noqa: BLE001 - a broken config must not stop reviewing
            traceback.print_exc()
    if not isinstance(cfg, dict):
        cfg = _session['config'] if _session['config'] is not None else copy.deepcopy(DEFAULT_CONFIG)
    cfg.setdefault('auto_reading_preset', True)
    if not isinstance(cfg.get('decided'), dict):
        cfg['decided'] = {}
    return cfg


def save_config(cfg):
    _session['config'] = cfg
    manager = getattr(mw, 'addonManager', None)
    if manager is not None:
        try:
            manager.writeConfig(__name__, cfg)
        except Exception:  # noqa: BLE001
            traceback.print_exc()


def profile_decisions(cfg):
    """{str(top deck id): record} for the open profile; deck ids belong to one collection, so profiles are kept apart."""
    decided = cfg['decided']
    if not isinstance(decided.get(_profile()), dict):
        decided[_profile()] = {}
    return decided[_profile()]


def _state(decided, did):
    record = decided.get(str(did))
    return record.get('state') if isinstance(record, dict) else record


def merge_record(old, new):
    """Re-applying to a family that is still applied keeps the presets recorded first for decks not changed now."""
    if isinstance(old, dict) and old.get('state') == 'applied' and old.get('preset') == new['preset']:
        new['original'] = {**(old.get('original') or {}), **new['original']}
        if old.get('preset_before'):
            new['preset_before'] = old['preset_before']
    return new


def _hint_once(top):
    if _session['hinted']:
        return
    _session['hinted'] = True
    tooltip(f'“{mw.col.decks.name(top)}”的学习步长短于 1 天：按 1 的卡今天几分钟后还会再出现。'
            '要隔天再看：工具 → CCPT：牌组使用阅读预设。', period=8000)


def auto_preset_once(card):
    """First CCPT card from a deck this session: give its family the reading preset unless the steps are already
    daily, the user undid it before (never again), it was applied before (later edits by the user win), or the
    user switched this off. Runs during review, so it shows tooltips only, never a dialog."""
    if not _api_ok or not mw.col:
        return
    did = card.odid or card.did
    if (_profile(), did) in _checked_decks:
        return
    _checked_decks.add((_profile(), did))
    try:
        if steps_are_daily(did):
            return
        top = family_top(did)
        cfg = load_config()
        decided = profile_decisions(cfg)
        if any(_state(decided, d) == 'declined' for d in lineage(did)):
            return
        if (str(top) in decided or not cfg.get('auto_reading_preset', True)
                or mw.col.decks.config_dict_for_deck_id(top)['name'].startswith(PRESET_PREFIX)):
            _hint_once(top)  # decided before, switched off, or a reading preset whose steps were shortened by hand
            return
        record = apply_reading_preset(top)
        if not record:
            return
        decided[str(top)] = record
        save_config(cfg)
        mw.reset()  # rebuild the queue so the card on screen is graded with the new steps too
        kept = f'（有自己预设或不含 CCPT 卡的 {len(record["kept"])} 个子牌组未改）' if record['kept'] else ''
        tooltip(f'已为“{record["deck"]}”自动启用 CCPT 阅读预设{kept}：学习步长改为 1 天，按 1 的卡下一个学习日再出现，'
                f'不会几分钟后又回来。{UNDO_HINT}', period=10000)
    except Exception:  # noqa: BLE001 - never interrupt review with an error dialog
        traceback.print_exc()
        tooltip('CCPT：没能自动设置阅读预设，可用“工具 → CCPT：牌组使用阅读预设”。', period=6000)


# ---------------------------------------------------------------- Tools menu

def _listing(names, limit=12):
    return '\n'.join('· ' + n for n in names[:limit]) + (f'\n…共 {len(names)} 个' if len(names) > limit else '')


def apply_to_ccpt_decks():
    """Tools menu: the reading preset for every deck family that holds CCPT cards, whatever deck is current."""
    if not mw.col or not _api_ok:
        return
    tops = ccpt_family_tops()
    if not tops:
        tooltip('没有找到 CCPT 卡（标签 ccpt6 或 CCPT 单面模板）：没有更改任何牌组。', period=6000)
        return
    todo = [t for t in tops if not steps_are_daily(t)]
    if not todo:
        tooltip('含 CCPT 卡的牌组学习步长都已不短于 1 天：按 1 就是下一个学习日再看，无需更改。', period=6000)
        return
    if not askUser('把这些含 CCPT 卡的牌组（及共用同一预设的子牌组）设为 CCPT 阅读预设？\n\n'
                   + _listing([mw.col.decks.name(t) for t in todo]) + '\n\n'
                   '只改两项：新卡与遗忘卡的学习步长都设为 1 天（按 1 = 下一个学习日再看，不会几分钟后又出现）；'
                   'leech 只加标签不暂停。其余选项（每日数量、FSRS、retention）沿用原预设。有自己预设的子牌组、'
                   '不含 CCPT 卡的牌组和筛选牌组不改。之后可用“工具 → CCPT：撤销阅读预设”恢复。'):
        return
    cfg = load_config()
    decided = profile_decisions(cfg)
    done = []
    for top in todo:
        record = apply_reading_preset(top)
        if record:
            decided[str(top)] = merge_record(decided.get(str(top)), record)
            done.append(record['deck'])
    save_config(cfg)
    mw.reset()
    tooltip(f'已应用 CCPT 阅读预设：{"、".join(done)}。按 1 的卡在下一个学习日出现；已在今天学习队列里的卡不会被移动。',
            period=8000)


def undo_reading_preset():
    """Tools menu: put back the presets the add-on replaced in this profile; those decks are never changed
    automatically again (the apply action above still works on request)."""
    if not mw.col or not _api_ok:
        return
    cfg = load_config()
    decided = profile_decisions(cfg)
    applied = {top: r for top, r in decided.items() if isinstance(r, dict) and r.get('state') == 'applied'}
    if not applied:
        tooltip('插件没有改过这个 Anki 用户的牌组预设，无需撤销。', period=5000)
        return
    if not askUser('把这些牌组恢复为插件改动前的预设？\n\n' + _listing([r.get('deck', top) for top, r in applied.items()])
                   + '\n\n恢复后按 1 的卡按原来的学习步长再出现（Anki 默认是几分钟后）。插件不会再自动修改这些牌组；'
                   '需要时仍可用“工具 → CCPT：牌组使用阅读预设”。'):
        return
    restored, left = 0, []
    for record in applied.values():
        n, kept = restore(record)
        restored, left = restored + n, left + kept
        record['state'] = 'declined'
    save_config(cfg)
    mw.reset()
    note = ('这些牌组之后被手动换过预设，保持不变：' + '、'.join(left[:6])) if left else ''
    tooltip(f'已恢复 {restored} 个牌组原来的预设，插件不会再自动修改它们。{note}', period=8000)


_menu_apply = QAction('CCPT：牌组使用阅读预设（1 = 隔天再看）', mw)
_menu_apply.triggered.connect(lambda *_: apply_to_ccpt_decks())
mw.form.menuTools.addAction(_menu_apply)
_menu_undo = QAction('CCPT：撤销阅读预设', mw)
_menu_undo.triggered.connect(lambda *_: undo_reading_preset())
mw.form.menuTools.addAction(_menu_undo)

if not _api_ok:
    gui_hooks.main_window_did_init.append(lambda: tooltip('CCPT 单面卡插件：这个 Anki 版本缺少需要的接口（需要 2.1.50 或更新），插件未接管按键。', period=8000))
