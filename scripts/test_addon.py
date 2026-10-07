"""Tests for the Anki desktop add-on (single_face_addon.py) and its package (package_addon.py).

aqt and PyQt are not needed: every test imports the add-on fresh against stub aqt modules, which pytest
removes again afterwards. Deck logic runs twice, against a small in-memory collection ("fake") and, when the
anki package is importable, against a real anki Collection in a temporary folder ("real"); the real one
also checks the schedule Anki produces. Keys are simulated by calling the reviewer shortcuts the add-on
installs; nothing here presses keys in a real Anki window.
"""
import copy
import enum
import importlib.util
import json
import re
import sys
import types
import zipfile
from pathlib import Path

import pytest

import package_addon

ADDON = Path(__file__).resolve().parent / 'single_face_addon.py'
MARKER_QFMT = '<div class="ccpt6-card" data-ccpt-single="1">{{Page}}</div>'
PROFILE = 'User 1'
DAY = 1440.0
READING = 'CCPT 阅读（{}）'


# ---------------------------------------------------------------- stub aqt

class Key(enum.Enum):
    Key_Space = 1
    Key_Return = 2
    Key_Enter = 3
    Key_F5 = 4


def _module(name, **attrs):
    module = types.ModuleType(name)
    module.__dict__.update(attrs)
    return module


class StubCard:
    def __init__(self, cid=5, did=7, odid=0, qfmt=MARKER_QFMT):
        self.id, self.did, self.odid, self._qfmt = cid, did, odid, qfmt

    def template(self):
        return {'qfmt': self._qfmt, 'afmt': self._qfmt}


class StubDeckManager:
    """Only the class attributes the add-on checks for; deck calls go to the collection's own manager."""
    config_dict_for_deck_id = add_config_returning_id = set_config_id_for_deck_dict = deck_and_child_ids = None


class Harness:
    """mw, reviewer, hooks and aqt.utils stubs around one fresh import of the add-on."""

    def __init__(self, monkeypatch, col, store, deck_manager=StubDeckManager, reviewer_api=True,
                 profile=PROFILE, addon_manager=True):
        h = self
        self.timers, self.tooltips, self.asks, self.answers, self.evals, self.fallbacks = [], [], [], [], [], []
        self.resets, self.gesture, self.ask_reply, self.editable, self.menu = 0, None, True, False, []

        class Reviewer:
            def _answerCard(self, ease):
                h.answers.append(ease)
                self.state = 'transition'

            def _showAnswer(self):
                self.state = 'answer'
        if not reviewer_api:
            del Reviewer._answerCard

        class Web:
            def eval(self, js):
                h.evals.append(js)

            def evalWithCallback(self, js, callback):
                callback(h.editable)

            def setPlaybackRequiresGesture(self, value):
                h.gesture = value

        class Signal:
            def __init__(self):
                self.slots = []

            def connect(self, fn):
                self.slots.append(fn)

        class QAction:
            def __init__(self, text, parent=None):
                self.text, self.triggered = text, Signal()

        class QTimer:
            @staticmethod
            def singleShot(ms, fn):
                h.timers.append(fn)

        class AddonManager:
            """Like aqt's: config.json defaults merged with the saved user config (meta.json, JSON round trip)."""
            def getConfig(self, module):
                h.config_module = module
                if store['defaults'] is None:
                    return None
                cfg = copy.deepcopy(store['defaults'])
                cfg.update(copy.deepcopy(store['user'] or {}))
                return cfg

            def writeConfig(self, module, conf):
                store['user'] = json.loads(json.dumps(conf))

        self.reviewer = Reviewer()
        self.reviewer.web, self.reviewer.state, self.reviewer.card = Web(), 'question', None
        self.hooks = types.SimpleNamespace(state_shortcuts_will_change=[], reviewer_did_show_question=[],
                                           main_window_did_init=[])
        self.mw = types.SimpleNamespace(col=col, state='review', reviewer=self.reviewer, reset=self._reset,
                                        form=types.SimpleNamespace(menuTools=types.SimpleNamespace(addAction=self.menu.append)),
                                        pm=types.SimpleNamespace(name=profile))
        if addon_manager:
            self.mw.addonManager = AddonManager()
        stubs = {'aqt': _module('aqt', mw=self.mw, gui_hooks=self.hooks),
                 'aqt.qt': _module('aqt.qt', Qt=types.SimpleNamespace(Key=Key), QTimer=QTimer, QAction=QAction),
                 'aqt.reviewer': _module('aqt.reviewer', Reviewer=Reviewer),
                 'aqt.utils': _module('aqt.utils', tooltip=self._tooltip, askUser=self._ask)}
        if deck_manager is not None:  # None: the real anki.decks (a real collection is in use)
            stubs['anki.decks'] = _module('anki.decks', DeckManager=deck_manager)
            if 'anki' not in sys.modules:
                stubs['anki'] = _module('anki')
        for name, module in stubs.items():
            monkeypatch.setitem(sys.modules, name, module)
        spec = importlib.util.spec_from_file_location('ccpt_single_face', ADDON)
        self.addon = importlib.util.module_from_spec(spec)
        monkeypatch.setitem(sys.modules, 'ccpt_single_face', self.addon)
        spec.loader.exec_module(self.addon)

    def _tooltip(self, msg, period=3000, **kw):
        self.tooltips.append(msg)

    def _ask(self, text, parent=None, help=None, defaultno=False, **kw):
        self.asks.append({'text': text, 'defaultno': defaultno})
        return self.ask_reply

    def _reset(self):
        """Like mw.reset() while reviewing: the queue is rebuilt and the same card is shown again."""
        self.resets += 1
        card = self.reviewer.card
        if self.mw.state == 'review' and card is not None:
            if hasattr(card, 'load'):
                card.load()
            self.reviewer.state = 'question'
            for fn in self.hooks.reviewer_did_show_question:
                fn(card)

    def flush(self):
        """Run QTimer.singleShot(0) callbacks the way the Qt event loop would, after the current handler."""
        for _ in range(100):
            if not self.timers:
                return
            self.timers.pop(0)()
        raise AssertionError('timers keep rescheduling themselves')

    def show(self, card):
        self.reviewer.card, self.reviewer.state = card, 'question'
        for fn in self.hooks.reviewer_did_show_question:
            fn(card)
        self.flush()

    def shortcuts(self, one_key='1'):
        """Anki's reviewer shortcuts (the part the add-on touches), passed through state_shortcuts_will_change."""
        def fallback(name):
            return lambda: self.fallbacks.append(name)
        keys = [('e', fallback('edit')), (' ', fallback('space')), (Key.Key_Return, fallback('return')),
                (Key.Key_Enter, fallback('enter')), (one_key, fallback('ease1')), ('3', fallback('ease3'))]
        for fn in self.hooks.state_shortcuts_will_change:
            fn('review', keys)
        return keys

    def trigger(self, prefix):
        action = next(a for a in self.menu if a.text.startswith(prefix))
        for slot in action.triggered.slots:
            slot(False)  # QAction.triggered(bool checked)


# ---------------------------------------------------------------- collections

def _preset(cid, name):
    return {'id': cid, 'name': name, 'maxTaken': 60, 'new': {'delays': [1.0, 10.0]},
            'lapse': {'delays': [10.0], 'leechAction': 0}}


class FakeDecks:
    """The DeckManager calls the add-on makes, with anki's semantics (reads return copies, parents are created)."""

    def __init__(self):
        self._decks = {1: {'id': 1, 'name': 'Default', 'conf': 1, 'dyn': 0}}
        self._confs = {1: _preset(1, 'Default')}
        self._ids = iter(range(1000, 10 ** 6))

    def id(self, name):
        found = self.by_name(name)
        if found:
            return found['id']
        if '::' in name:
            self.id(name.rsplit('::', 1)[0])
        did = next(self._ids)
        self._decks[did] = {'id': did, 'name': name, 'conf': 1, 'dyn': 0}
        return did

    def new_filtered(self, name):
        did = next(self._ids)
        self._decks[did] = {'id': did, 'name': name, 'dyn': 1}
        return did

    def get(self, did, default=True):
        deck = self._decks.get(int(did)) if did else None
        return copy.deepcopy(deck if deck or not default else self._decks[1])

    def name(self, did):
        return self._decks[did]['name']

    def by_name(self, name):
        return copy.deepcopy(next((d for d in self._decks.values() if d['name'] == name), None))

    def current(self):
        return self.get(1)

    def deck_and_child_ids(self, did):
        prefix = self.name(did) + '::'
        return [did] + sorted(d for d, deck in self._decks.items() if deck['name'].startswith(prefix))

    def config_dict_for_deck_id(self, did):
        deck = self._decks[did]
        return copy.deepcopy(deck if deck.get('dyn') else self._confs.get(deck['conf']) or self._confs[1])

    def all_config(self):
        return [copy.deepcopy(c) for c in self._confs.values()]

    def get_config(self, cid):
        return copy.deepcopy(self._confs.get(cid))

    def add_config_returning_id(self, name, clone_from=None):
        cid = next(self._ids)
        conf = copy.deepcopy(clone_from) if clone_from else _preset(cid, name)
        conf.update(id=cid, name=name)
        self._confs[cid] = conf
        return cid

    def update_config(self, conf):
        assert conf['id'] in self._confs
        self._confs[conf['id']] = copy.deepcopy(conf)

    def set_config_id_for_deck_dict(self, deck, cid):
        deck['conf'] = cid
        self._decks[deck['id']] = copy.deepcopy(deck)


class FakeCard(StubCard):
    def __init__(self, cid, did, mid, tags, qfmt):
        super().__init__(cid, did, 0, qfmt)
        self.mid, self.tags = mid, tags


class FakeCol:
    MODELS = {10: {'id': 10, 'name': 'Basic', 'tmpls': [{'qfmt': '{{Front}}'}]},
              20: {'id': 20, 'name': 'CCPT 单面', 'tmpls': [{'qfmt': MARKER_QFMT}]}}
    QUERY = re.compile(r'(?:did:(\d+))?\s*(\(tag:ccpt6(?: or mid:\d+)*\))?')

    def __init__(self):
        self.decks = FakeDecks()
        self.models = types.SimpleNamespace(all=lambda: copy.deepcopy(list(self.MODELS.values())))
        self.cards = {}
        self._ids = iter(range(10 ** 6, 10 ** 7))

    def add(self, did, mid, tags):
        cid = next(self._ids)
        self.cards[cid] = FakeCard(cid, did, mid, list(tags), self.MODELS[mid]['tmpls'][0]['qfmt'])
        return self.cards[cid]

    def get_card(self, cid):
        return self.cards[cid]

    def find_cards(self, query):
        m = self.QUERY.fullmatch(query.strip())
        assert m and (m.group(1) or m.group(2)), f'fake collection cannot evaluate {query!r}'
        did, ccpt = m.group(1), m.group(2)
        mids = {int(x) for x in re.findall(r'mid:(\d+)', ccpt or '')}
        return [c.id for c in self.cards.values()
                if (not did or int(did) in (c.did, c.odid)) and (not ccpt or 'ccpt6' in c.tags or c.mid in mids)]


class World:
    """One collection plus the few set-up steps the tests need; same API for the fake and the real collection."""
    deck_manager = StubDeckManager

    def deck(self, name):
        return self.col.decks.id(name)

    def preset(self, deck_name):
        return self.col.decks.config_dict_for_deck_id(self.deck(deck_name))

    def use_preset(self, deck_names, preset_name, new=(1.0, 10.0), lapse=(10.0,)):
        decks = self.col.decks
        cid = decks.add_config_returning_id(preset_name)
        conf = decks.get_config(cid)
        conf['new']['delays'], conf['lapse']['delays'] = list(new), list(lapse)
        decks.update_config(conf)
        for name in deck_names:
            decks.set_config_id_for_deck_dict(decks.get(self.deck(name)), cid)
        return cid

    def set_steps(self, deck_name, new, lapse):
        conf = self.preset(deck_name)
        conf['new']['delays'], conf['lapse']['delays'] = list(new), list(lapse)
        self.col.decks.update_config(conf)

    def reading_presets(self):
        return [c['name'] for c in self.col.decks.all_config() if c['name'].startswith('CCPT 阅读')]

    def close(self):
        pass


class FakeWorld(World):
    kind = 'fake'

    def __init__(self, tmp_path):
        self.col = FakeCol()

    def ccpt_card(self, deck_name, tags=('ccpt6',)):
        return self.col.add(self.deck(deck_name), 20, tags)

    def plain_card(self, deck_name):
        return self.col.add(self.deck(deck_name), 10, ())

    def filtered(self, name):
        return self.col.decks.new_filtered(name)

    def move_to_filtered(self, card, name):
        card.odid, card.did = card.did, self.filtered(name)
        return card


class RealWorld(World):
    kind = 'real'
    deck_manager = None  # the add-on imports the real anki.decks

    def __init__(self, tmp_path):
        collection = pytest.importorskip('anki.collection')  # import order matters: anki.decks alone is circular
        self.col = collection.Collection(str(tmp_path / 'collection.anki2'))
        models = self.col.models
        notetype = models.new('CCPT 单面')
        models.add_field(notetype, models.new_field('Page'))
        template = models.new_template('单面阅读')
        template['qfmt'] = template['afmt'] = MARKER_QFMT
        models.add_template(notetype, template)
        models.add(notetype)
        self._ccpt, self._basic, self._n = models.by_name('CCPT 单面'), models.by_name('Basic'), 0

    def _add(self, notetype, field, deck_name, tags):
        self._n += 1
        note = self.col.new_note(notetype)
        note[field] = f'card {self._n}'
        note.tags = list(tags)
        self.col.add_note(note, self.deck(deck_name))
        return self.col.get_card(note.card_ids()[0])

    def ccpt_card(self, deck_name, tags=('ccpt6',)):
        return self._add(self._ccpt, 'Page', deck_name, tags)

    def plain_card(self, deck_name):
        return self._add(self._basic, 'Front', deck_name, ())

    def filtered(self, name):
        return self.col.decks.new_filtered(name)

    def move_to_filtered(self, card, name):
        did = self.filtered(name)
        deck = self.col.decks.get(did)
        deck['terms'] = [[f'cid:{card.id}', 10, 0]]
        self.col.decks.save(deck)
        self.col.sched.rebuild_filtered_deck(did)
        card.load()
        assert (card.did, card.odid) == (did, self.deck('D::Sub'))
        return card

    def close(self):
        self.col.close()


@pytest.fixture(params=['fake', 'real'])
def world(request, tmp_path):
    w = (RealWorld if request.param == 'real' else FakeWorld)(tmp_path)
    yield w
    w.close()


@pytest.fixture
def store():
    """What Anki keeps for the add-on: config.json defaults (as shipped) and the user's saved config."""
    return {'defaults': copy.deepcopy(package_addon.CONFIG), 'user': None}


@pytest.fixture
def load(monkeypatch, store):
    def _load(world=None, **kw):
        if world is not None:
            kw.setdefault('deck_manager', world.deck_manager)
        return Harness(monkeypatch, world.col if world else None, store, **kw)
    return _load


def decisions(store, profile=PROFILE):
    return ((store['user'] or {}).get('decided') or {}).get(profile, {})


# ---------------------------------------------------------------- keys

def test_route_ccpt_card_space_enter_one(load):
    h = load()
    keys = dict(h.shortcuts())
    h.reviewer.card, h.reviewer.state = StubCard(), 'answer'
    keys[' ']()
    assert h.evals == ["window.ccptSingleAction && window.ccptSingleAction('audio');"] and h.answers == []
    keys[Key.Key_Return]()
    h.reviewer.state = 'answer'
    keys[Key.Key_Enter]()
    h.reviewer.state = 'answer'
    keys['1']()
    assert h.answers == [3, 3, 1]
    assert h.fallbacks == []


def test_route_other_cards_keep_anki_callbacks(load):
    h = load()
    keys = dict(h.shortcuts())
    h.reviewer.card, h.reviewer.state = StubCard(qfmt='{{Front}}'), 'answer'
    for key in (' ', Key.Key_Return, Key.Key_Enter, '1', 'e'):
        keys[key]()
    assert h.fallbacks == ['space', 'return', 'enter', 'ease1', 'edit']
    assert h.answers == [] and h.evals == []


def test_route_adds_1_when_again_is_remapped(load):
    h = load()
    keys = h.shortcuts(one_key='j')
    assert [k for k, _ in keys].count('1') == 1
    h.reviewer.card, h.reviewer.state = StubCard(), 'answer'
    dict(keys)['1']()
    assert h.answers == [1]
    assert [k for k, _ in load().shortcuts()].count('1') == 1  # not added twice when present


def test_grade_only_on_reading_card_in_answer_state(load):
    h = load()
    h.reviewer.card, h.reviewer.state = StubCard(), 'question'
    h.addon.grade(h.reviewer, 3)
    h.reviewer.state, h.mw.state = 'answer', 'overview'
    h.addon.grade(h.reviewer, 3)
    h.mw.state, h.reviewer.card = 'review', StubCard(qfmt='{{Front}}')
    h.addon.grade(h.reviewer, 3)
    assert h.answers == [] and h.evals == []
    h.reviewer.card = StubCard()
    h.addon.grade(h.reviewer, 3)
    assert h.answers == [3] and h.evals == ['if(window.ccptCleanup)window.ccptCleanup();']


def test_editable_focus_suppresses_actions(load):
    h = load()
    keys = dict(h.shortcuts())
    h.reviewer.card, h.reviewer.state, h.editable = StubCard(), 'answer', True
    for key in (' ', Key.Key_Return, Key.Key_Enter, '1'):
        keys[key]()
    assert h.answers == [] and h.evals == [] and h.fallbacks == []


def test_show_lifts_gesture_and_opens_answer_state(load):
    h = load()
    h.show(StubCard())
    assert h.gesture is False and h.reviewer.state == 'answer' and h.asks == []
    other = load()
    other.show(StubCard(qfmt='{{Front}}'))
    assert other.gesture is None and other.reviewer.state == 'question'


def test_old_anki_without_api_takes_over_nothing(load):
    h = load(reviewer_api=False)
    assert h.addon._api_ok is False
    keys = dict(h.shortcuts())
    h.reviewer.card, h.reviewer.state = StubCard(), 'answer'
    keys[' ']()
    keys['1']()
    assert h.fallbacks == ['space', 'ease1'] and h.answers == []
    assert len(h.hooks.main_window_did_init) == 1


# ---------------------------------------------------------------- automatic reading preset on first review

def test_first_review_applies_preset_without_dialog(world, load, store):
    card = world.ccpt_card('D::Sub')
    world.plain_card('Mine')
    h = load(world)
    h.show(card)
    assert h.asks == []  # never a modal during review
    assert h.resets == 1 and h.reviewer.state == 'answer'  # queue rebuilt, same card graded with new steps
    assert len(h.tooltips) == 1 and '撤销阅读预设' in h.tooltips[0]
    for name in ('D', 'D::Sub'):
        conf = world.preset(name)
        assert conf['name'] == READING.format('Default')
        assert conf['new']['delays'] == [DAY] and conf['lapse']['delays'] == [DAY] and conf['lapse']['leechAction'] == 1
    for name in ('Default', 'Mine'):
        assert world.preset(name)['id'] == 1 and world.preset(name)['new']['delays'] == [1.0, 10.0]
    record = decisions(store)[str(world.deck('D'))]
    assert record['state'] == 'applied'
    assert record['original'] == {str(world.deck('D')): 1, str(world.deck('D::Sub')): 1}
    assert h.config_module == 'ccpt_single_face'
    h.show(world.ccpt_card('D::Sub'))  # more cards from the family: nothing more happens
    assert h.resets == 1 and len(h.tooltips) == 1


def test_decision_persists_into_next_session(world, load, store):
    card = world.ccpt_card('D::Sub')
    load(world).show(card)
    assert decisions(store)[str(world.deck('D'))]['state'] == 'applied'
    for name in ('D', 'D::Sub'):  # the user moves the decks back by hand (not with the undo action)
        world.col.decks.set_config_id_for_deck_dict(world.col.decks.get(world.deck(name)), 1)
    h = load(world)  # Anki restarted: fresh import, same saved config
    h.show(card)
    assert world.preset('D::Sub')['id'] == 1 and h.resets == 0 and h.asks == []
    assert len(h.tooltips) <= 1 and all('撤销' not in t for t in h.tooltips)  # at most the Tools-menu hint


def test_declined_family_is_never_changed(world, load, store):
    card = world.ccpt_card('D::Sub')
    store['user'] = {'decided': {PROFILE: {str(world.deck('D')): {'state': 'declined'}}}}
    h = load(world)
    h.show(card)
    h.show(world.ccpt_card('D::Sub::Deeper'))  # a deck added under the declined family later
    assert world.preset('D::Sub')['id'] == 1 and world.preset('D::Sub::Deeper')['id'] == 1
    assert world.reading_presets() == [] and h.tooltips == [] and h.resets == 0


def test_decision_in_another_profile_does_not_count(world, load, store):
    card = world.ccpt_card('D::Sub')
    store['user'] = {'decided': {'Other profile': {str(world.deck('D')): {'state': 'declined'}}}}
    load(world).show(card)
    assert world.preset('D::Sub')['name'] == READING.format('Default')
    assert decisions(store, 'Other profile')[str(world.deck('D'))]['state'] == 'declined'


def test_daily_steps_are_left_alone(world, load, store):
    card = world.ccpt_card('D::Sub')
    world.set_steps('D::Sub', [DAY], [DAY])
    h = load(world)
    h.show(card)
    assert world.reading_presets() == [] and store['user'] is None
    assert h.tooltips == [] and h.resets == 0 and h.reviewer.state == 'answer'


def test_empty_steps_get_the_preset(world, load):
    """Empty steps do not promise that a card answered 1 comes back on the next learning day."""
    card = world.ccpt_card('D::Sub')
    world.set_steps('D::Sub', [], [])
    load(world).show(card)
    assert world.preset('D::Sub')['new']['delays'] == [DAY] and world.preset('D::Sub')['lapse']['delays'] == [DAY]


def test_card_in_filtered_deck_sets_home_family(world, load, store):
    card = world.move_to_filtered(world.ccpt_card('D::Sub'), 'Cram')
    h = load(world)
    h.show(card)
    assert world.preset('D::Sub')['name'] == READING.format('Default') and h.asks == []
    assert list(decisions(store)) == [str(world.deck('D'))]


def test_switched_off_only_hints_once(world, load, store):
    first, second = world.ccpt_card('A::Sub'), world.ccpt_card('B')
    world.use_preset(['B'], 'Own')
    store['user'] = {'auto_reading_preset': False}
    h = load(world)
    h.show(first)
    h.show(second)
    assert world.reading_presets() == [] and h.asks == [] and h.resets == 0
    assert len(h.tooltips) == 1 and '工具 → CCPT：牌组使用阅读预设' in h.tooltips[0]


def test_hand_shortened_reading_preset_is_respected(world, load):
    card = world.ccpt_card('D')
    world.use_preset(['D'], READING.format('Default'))  # made by an older add-on, steps shortened by the user
    h = load(world)
    h.show(card)
    assert world.preset('D')['new']['delays'] == [1.0, 10.0] and h.resets == 0 and len(h.tooltips) == 1


def test_works_without_addon_manager(world, load):
    card = world.ccpt_card('D::Sub')
    h = load(world, addon_manager=False)
    h.show(card)
    assert world.preset('D::Sub')['name'] == READING.format('Default') and h.resets == 1
    world.set_steps('D::Sub', [1.0], [1.0])
    h.addon._checked_decks.clear()
    h.show(card)  # decided earlier this session: not applied again
    assert world.preset('D::Sub')['new']['delays'] == [1.0] and h.resets == 1


# ---------------------------------------------------------------- apply_reading_preset

def test_apply_clones_once_then_reuses(world, load):
    world.ccpt_card('A')
    world.ccpt_card('B')
    h = load(world)
    first = h.addon.apply_reading_preset(world.deck('A'))
    second = h.addon.apply_reading_preset(world.deck('B'))
    again = h.addon.apply_reading_preset(world.deck('A'))
    assert world.reading_presets() == [READING.format('Default')]
    assert first['preset'] == second['preset'] == again['preset'] == world.preset('A')['id'] == world.preset('B')['id']
    assert first['original'] == {str(world.deck('A')): 1} and again['original'] == {}
    assert 'preset_before' not in first and 'preset_before' not in again


def test_apply_keeps_own_presets_and_unrelated_decks(world, load):
    econ = world.ccpt_card('School::Econ')
    world.plain_card('School::French')
    world.ccpt_card('School::Own')
    own = world.use_preset(['School::Own'], 'Own')
    h = load(world)
    top = h.addon.family_top(econ.did)
    assert top == world.deck('School')
    record = h.addon.apply_reading_preset(top)
    assert world.preset('School')['name'] == world.preset('School::Econ')['name'] == READING.format('Default')
    assert world.preset('School::French')['id'] == 1 and world.preset('School::Own')['id'] == own
    assert sorted(record['kept']) == ['School::French', 'School::Own']


def test_apply_refuses_filtered_deck(world, load):
    world.ccpt_card('D')
    filtered = world.filtered('Filtered')
    h = load(world)
    assert h.addon.apply_reading_preset(filtered) is None
    assert world.reading_presets() == [] and '筛选牌组' in h.tooltips[-1]


# ---------------------------------------------------------------- Tools menu

def test_menu_changes_ccpt_family_not_current_deck(world, load, store):
    """robust-03: the current deck is Default, which holds no CCPT card."""
    world.ccpt_card('D::Sub')
    world.plain_card('Mine')
    world.plain_card('Default')
    assert world.col.decks.current()['name'] == 'Default'
    h = load(world)
    h.mw.state = 'deckBrowser'
    h.trigger('CCPT：牌组使用阅读预设')
    assert len(h.asks) == 1 and h.asks[0]['defaultno'] is False and '· D\n' in h.asks[0]['text'] + '\n'
    assert world.preset('D')['name'] == world.preset('D::Sub')['name'] == READING.format('Default')
    assert world.preset('Default')['id'] == 1 and world.preset('Mine')['id'] == 1
    assert world.preset('Default')['new']['delays'] == [1.0, 10.0]
    assert decisions(store)[str(world.deck('D'))]['state'] == 'applied' and h.resets == 1
    h.trigger('CCPT：牌组使用阅读预设')  # second time: steps are daily now
    assert len(h.asks) == 1 and '无需更改' in h.tooltips[-1]


def test_menu_fixes_shortened_reading_preset_in_place_and_undo_restores(world, load):
    world.ccpt_card('D')
    cid = world.use_preset(['D'], READING.format('Default'))
    leech = world.preset('D')['lapse']['leechAction']
    h = load(world)
    h.mw.state = 'deckBrowser'
    h.trigger('CCPT：牌组使用阅读预设')
    assert world.preset('D')['id'] == cid and world.preset('D')['new']['delays'] == [DAY]
    assert world.reading_presets() == [READING.format('Default')]
    h.trigger('CCPT：撤销阅读预设')
    conf = world.preset('D')
    assert conf['id'] == cid and conf['new']['delays'] == [1.0, 10.0] and conf['lapse']['delays'] == [10.0]
    assert conf['lapse']['leechAction'] == leech


def test_menu_without_ccpt_cards_changes_nothing(world, load, store):
    world.plain_card('Mine')
    h = load(world)
    h.trigger('CCPT：牌组使用阅读预设')
    assert h.asks == [] and world.reading_presets() == [] and store['user'] is None
    assert '没有找到 CCPT 卡' in h.tooltips[-1]


def test_menu_answer_no_changes_nothing(world, load, store):
    world.ccpt_card('D')
    h = load(world)
    h.ask_reply = False
    h.trigger('CCPT：牌组使用阅读预设')
    assert len(h.asks) == 1 and world.reading_presets() == [] and store['user'] is None and h.resets == 0


def test_undo_restores_presets_and_declines(world, load, store):
    card = world.ccpt_card('D::Sub')
    mine = world.use_preset(['D', 'D::Sub'], 'Mine')
    load(world).show(card)
    assert world.preset('D::Sub')['name'] == READING.format('Mine')
    h = load(world)
    h.mw.state = 'deckBrowser'
    h.trigger('CCPT：撤销阅读预设')
    assert len(h.asks) == 1 and h.asks[0]['defaultno'] is False and 'D' in h.asks[0]['text']
    assert world.preset('D')['id'] == world.preset('D::Sub')['id'] == mine
    assert world.preset('D::Sub')['new']['delays'] == [1.0, 10.0]
    assert decisions(store)[str(world.deck('D'))]['state'] == 'declined' and h.resets == 1
    later = load(world)
    later.show(card)  # next session: the undone family is left alone
    assert world.preset('D::Sub')['id'] == mine and later.resets == 0
    later.trigger('CCPT：牌组使用阅读预设')  # ...but the menu still applies it on request
    assert world.preset('D::Sub')['name'] == READING.format('Mine')
    assert decisions(store)[str(world.deck('D'))]['state'] == 'applied'


def test_undo_with_nothing_applied(world, load):
    world.ccpt_card('D')
    h = load(world)
    h.trigger('CCPT：撤销阅读预设')
    assert h.asks == [] and '无需撤销' in h.tooltips[-1]


# ---------------------------------------------------------------- real scheduler

@pytest.mark.parametrize('fsrs', [False, True], ids=['sm2', 'fsrs'])
def test_real_schedule_after_auto_preset(tmp_path, load, fsrs):
    """After the add-on's automatic preset, a new card answered Again (1) or Good (Enter) is due on the next
    day, never minutes later; an unrelated deck keeps Anki's default minute steps."""
    world = RealWorld(tmp_path)
    from anki.scheduler.v3 import CardAnswer
    try:
        col = world.col
        if fsrs:
            col.set_config('fsrs', True)
        cards = [world.ccpt_card('D::Sub') for _ in range(3)]
        world.plain_card('Mine')
        load(world).show(cards[0])
        assert world.preset('D::Sub')['name'] == READING.format('Default')

        def answer_first(deck_name, rating):
            col.decks.select(world.deck(deck_name))
            queued = col.sched.get_queued_cards().cards[0]
            card = col.get_card(queued.card.id)
            card.start_timer()
            col.sched.answer_card(col.sched.build_answer(card=card, states=queued.states, rating=rating))
            return col.get_card(card.id)

        today = col.sched.today
        again = answer_first('D::Sub', CardAnswer.AGAIN)
        good = answer_first('D::Sub', CardAnswer.GOOD)
        assert (again.queue, again.due) == (3, today + 1)  # interday learning, next day
        assert good.queue == 2 and good.due >= today + 1  # review card, not today
        if not fsrs:
            assert good.due == today + 1 and good.ivl == 1
        col.decks.select(world.deck('D::Sub'))
        left_today = {q.card.id for q in col.sched.get_queued_cards(fetch_limit=100).cards}
        assert again.id not in left_today and good.id not in left_today
        control = answer_first('Mine', CardAnswer.AGAIN)
        assert control.queue == 1  # minutes: the unrelated deck kept Anki's default steps
    finally:
        world.close()


# ---------------------------------------------------------------- package

def test_package_ships_config(tmp_path, load):
    target = package_addon.write_addon(tmp_path)
    with zipfile.ZipFile(target) as z:
        assert sorted(z.namelist()) == ['__init__.py', 'config.json', 'config.md', 'manifest.json']
        assert z.read('__init__.py') == ADDON.read_bytes()
        manifest = json.loads(z.read('manifest.json'))
        config = json.loads(z.read('config.json'))
        help_text = z.read('config.md').decode('utf-8')
    assert manifest['package'] == 'ccpt_single_face' and manifest['min_point_version'] == 50
    assert config == {'auto_reading_preset': True, 'decided': {}} == load().addon.DEFAULT_CONFIG
    assert 'auto_reading_preset' in help_text and '撤销阅读预设' in help_text and '1d' in help_text
