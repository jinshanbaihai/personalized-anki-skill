"""Isolated current-format import and media regression, not a learning-effect test."""
import argparse, json, re, sys, tempfile, subprocess
from pathlib import Path
from html.parser import HTMLParser
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.sides=[];self.players=[];self.audio=[];self.pending=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'data-side' in a:self.sides.append(a['data-side'])
        if a.get('data-audio-pending')=='1':self.pending=True
        if tag=='button' and ('data-audio' in a or a.get('data-control')=='play'):self.players.append(a)
        if tag=='audio':self.audio.append(a.get('src',''))

def inspect_page(markup, allow_pending=False):
    page=Page();page.feed(markup)
    assert page.sides==['read'] and len(page.players)==1, 'Single complete page and exactly one narration control required'
    assert len(page.audio)==1, 'Exactly one page audio element required'
    player=page.players[0];name=player.get('data-audio','').strip()
    if page.pending:
        assert allow_pending, 'Audio pending: not a completed audio package'
        assert not name and not page.audio[0] and 'disabled' in player, 'Pending audio must be empty and its player disabled'
        return None
    assert name and page.audio[0]==name and 'disabled' not in player, 'Narration control and audio must reference the same nonempty local media'
    assert Path(name).name==name and name not in ('.','..') and ':' not in name, 'Narration must use a bundled media filename'
    return name

def main():
    p=argparse.ArgumentParser();p.add_argument('package',type=Path);p.add_argument('--anki-packages',type=Path);p.add_argument('--allow-text-only-test',action='store_true');p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.anki_packages:sys.path.insert(0,str(a.anki_packages))
    from anki.collection import Collection
    from anki import import_export_pb2,buildinfo
    with tempfile.TemporaryDirectory(prefix='ccpt-validation-') as temp:
        col=Collection(str(Path(temp)/'collection.anki2'))
        req=import_export_pb2.ImportAnkiPackageRequest(package_path=str(a.package.resolve()),options=import_export_pb2.ImportAnkiPackageOptions(with_scheduling=False))
        col.import_anki_package(req)
        assert col.card_count()>0
        decoded=[];pending=0
        for cid in col.find_cards(''):
            card=col.get_card(cid);note=card.note();q=card.question();name=inspect_page(q,a.allow_text_only_test)
            assert note['FrontHTML']==note['BackHTML'],'Both templates must expose the same complete lesson'
            assert card.template()['qfmt']==card.template()['afmt']
            assert not re.search(r'data-choice|data-correct',q),'Default cards must not be quizzes'
            if name is None:
                pending+=1
            else:
                media=Path(col.media.dir())/name;assert media.is_file(),name
                result=subprocess.run(['ffmpeg','-v','error','-i',str(media),'-f','null','-'],capture_output=True)
                assert result.returncode==0, result.stderr.decode();decoded.append(name)
        # Create a real scheduler record in the isolated collection before repeat import.
        col.decks.select(col.get_card(col.find_cards('')[0]).did)
        queued=col.sched.get_queued_cards()
        assert queued and queued.cards
        from anki.scheduler.v3 import CardAnswer
        qc=queued.cards[0];card=col.get_card(qc.card.id);card.start_timer();answer=col.sched.build_answer(card=card,states=qc.states,rating=CardAnswer.GOOD)
        col.sched.answer_card(answer)
        before=col.db.all('select id,nid,did,ord,type,queue,due,ivl,factor,reps,lapses,left,odue,odid,flags,data from cards order by id')
        logs=col.db.all('select * from revlog order by id');guids=col.db.all('select id,guid from notes order by id');assert logs
        col.import_anki_package(req)
        assert before==col.db.all('select id,nid,did,ord,type,queue,due,ivl,factor,reps,lapses,left,odue,odid,flags,data from cards order by id')
        assert logs==col.db.all('select * from revlog order by id') and guids==col.db.all('select id,guid from notes order by id')
        missing=list(col.media.check().missing);assert not missing,missing
        result={'anki_backend':buildinfo.version,'cards':col.card_count(),'notes':col.note_count(),'decoded_audio':len(set(decoded)),'audio_pending_cards':pending,'repeat_import_preserved_card_identity_schedule_and_review_log':True,'scope':'Isolated backend only; real rendering, sound and shortcuts require native checks.'}
        col.close()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))

if __name__=="__main__":main()
