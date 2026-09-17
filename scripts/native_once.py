"""Temporary Anki add-on. Put config.json beside this file, then restart Anki.
Uses the host app's collection and Qt web view. Removes only its own named folder.
Config: package, deck, output. All paths absolute and supplied by the installer.
"""
from pathlib import Path
import json,shutil,traceback
from aqt import mw,gui_hooks
from aqt.qt import QTimer,Qt,QPoint
from PyQt6.QtTest import QTest
from anki.import_export_pb2 import ImportAnkiPackageRequest,ImportAnkiPackageOptions
BASE=Path(__file__).resolve().parent
CONFIG=json.loads((BASE/'config.json').read_text())
OUT=Path(CONFIG['output']);OUT.mkdir(parents=True,exist_ok=True)
started=False;report={};preview=None
from aqt.browser.previewer import MultiCardPreviewer
class CardPreview(MultiCardPreviewer):
 def __init__(self,cids):
  self.cids=cids;self.index=0;self.previous=None
  super().__init__(None,mw,lambda:None)
 def _on_bridge_cmd(self,cmd):
  if cmd=='ans':self._state='answer';self.render_card()
  else:super()._on_bridge_cmd(cmd)
 def card(self):return mw.col.get_card(self.cids[self.index])
 def card_changed(self):
  cid=self.cids[self.index];changed=cid!=self.previous;self.previous=cid;return changed
 def _on_prev_card(self):
  if self.index>0:self.index-=1;self._state='question';self.render_card()
 def _on_next_card(self):
  if self.index<len(self.cids)-1:self.index+=1;self._state='question';self.render_card()
 def _should_enable_prev(self):return self._state=='answer' or self.index>0
 def _should_enable_next(self):return self._state=='question' or self.index<len(self.cids)-1
 def _render_scheduled(self):super()._render_scheduled();self._updateButtons()
def web():return preview._web if preview else mw.web
def window():return preview if preview else mw
def card():return preview.card() if preview else mw.reviewer.card

def record():
 (OUT/'native-anki-ready.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
def failed():
 report['error']=traceback.format_exc();record()
def prepare():
 global started
 if started or not mw.col:return
 started=True
 try:
  before={int(cid):mw.col.get_card(cid).reps for cid in mw.col.find_cards('')}
  mw.col.import_anki_package(ImportAnkiPackageRequest(package_path=CONFIG['package'],options=ImportAnkiPackageOptions(with_scheduling=False)))
  after={int(cid):mw.col.get_card(cid).reps for cid in mw.col.find_cards('')}
  assert all(after.get(cid)==reps for cid,reps in before.items()),'Existing review counts changed'
  deck=mw.col.decks.by_name(CONFIG['deck']);assert deck
  mw.col.decks.select(deck['id']);mw.reset();mw.showNormal();mw.setGeometry(mw.screen().availableGeometry());mw.raise_();mw.activateWindow();mw.moveToState('overview');QTimer.singleShot(1400,lambda:mw.moveToState('review'))
  report.update(stage='review-requested',history_preserved=True,card_count=len(after),deck_id=int(deck['id']))
  record();QTimer.singleShot(3800,inspect_front)
 except Exception:failed()
JS="""JSON.stringify({hasCard:!!document.querySelector('.ccpt'),side:document.querySelector('.ccpt')?.dataset.side,ready:document.querySelector('.ccpt')?.classList.contains('ready'),window:[innerWidth,innerHeight],scroll:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],base:document.baseURI,audioURL:document.querySelector('.scene')?new URL(document.querySelector('.scene').dataset.audio,document.baseURI).href:null,sceneCount:document.querySelectorAll('.scene').length})"""
def inspect_front():
 try:web().evalWithCallback(JS,front_done)
 except Exception:failed()
def front_done(value):
 try:
  d=json.loads(value);report['front']=d
  if not d['hasCard']:
   global preview
   cids=mw.col.find_cards('deck:"'+CONFIG['deck']+'"')
   assert cids,'Target deck contains no cards'
   preview=CardPreview(cids);mw.ccpt_preview=preview;preview.open();preview.resize(1024,720);preview.raise_();preview.activateWindow();report['mode']='native-preview'
   QTimer.singleShot(1100,inspect_front);return
  window().grab().save(str(OUT/'Anki实际正面.png'))
  web().evalWithCallback("(()=>{let e=document.querySelector('[data-control=reveal]');if(!e)return 'null';let r=e.getBoundingClientRect();return JSON.stringify({x:r.x+r.width/2,y:r.y+r.height/2})})()",reveal)
 except Exception:failed()
def reveal(value):
 try:
  d=json.loads(value)
  if d:
   QTest.mouseClick(web().focusProxy() or web(),Qt.MouseButton.LeftButton,pos=QPoint(int(d['x']),int(d['y'])))
   report['actual_reveal_click']=True
  elif preview:preview._on_next()
  else:mw.reviewer._showAnswer()
  QTimer.singleShot(700,inspect_back)
 except Exception:failed()
def inspect_back():
 try:web().evalWithCallback(JS,back_done)
 except Exception:failed()
def back_done(value):
 try:
  report['back']=json.loads(value);window().grab().save(str(OUT/'Anki实际背面.png'))
  # Qt sends a real click to the player, exercising the normal user-gesture path.
  js="""(()=>{window.ccptProbe={};window.ccptOriginalPlay=Audio.prototype.play;Audio.prototype.play=function(...args){window.ccptProbeAudio=this;this.addEventListener('loadedmetadata',()=>ccptProbe.duration=this.duration,{once:true});return ccptOriginalPlay.apply(this,args).then(()=>{ccptProbe.started=true}).catch(e=>{ccptProbe.error=String(e);throw e;});};let r=document.querySelector('[data-control=play]').getBoundingClientRect();return JSON.stringify({x:r.x+r.width/2,y:r.y+r.height/2});})()"""
  web().evalWithCallback(js,click_player)
 except Exception:failed()
def click_player(value):
 try:
  d=json.loads(value);target=web().focusProxy() or web();QTest.mouseClick(target,Qt.MouseButton.LeftButton,pos=QPoint(int(d['x']),int(d['y'])))
  QTimer.singleShot(1400,await_audio)
 except Exception:failed()
audio_waits=0
def await_audio():
 def done(value):
  global audio_waits
  d=json.loads(value)
  if d.get('started') and d.get('time',0)>0:finish_audio();return
  audio_waits+=1
  if audio_waits<12:QTimer.singleShot(500,await_audio)
  else:report.update(stage='playback-failed',error='Audio did not start after waiting for media loading');record()
 web().evalWithCallback("JSON.stringify({started:ccptProbe.started,time:window.ccptProbeAudio?.currentTime})",done)
def finish_audio():
 try:
  js="""(()=>{let a=window.ccptProbeAudio;if(!a)return JSON.stringify({error:'Click did not start the player'});ccptProbe.currentTime=a.currentTime;ccptProbe.readyState=a.readyState;ccptProbe.paused=a.paused;document.querySelector('[data-control=next]').click();document.querySelector('[data-control=prev]').click();Audio.prototype.play=ccptOriginalPlay;return JSON.stringify(ccptProbe);})()"""
  web().evalWithCallback(js,finish)
 except Exception:failed()
def finish(value):
 try:
  report['audio']=json.loads(value);report.update(state=mw.state,visible=window().isVisible(),card_id=int(card().id))
  assert report['back']['hasCard'] and report['back']['side']=='back'
  assert report['audio'].get('started') and report['audio'].get('currentTime',0)>0,'Actual audio did not advance'
  report['stage']='ready';record()
  if BASE.name=='codex_ccpt_once':shutil.rmtree(BASE)
 except Exception:failed()
gui_hooks.profile_did_open.append(lambda:QTimer.singleShot(6000,prepare))
QTimer.singleShot(7000,prepare)
