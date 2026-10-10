"""Isolated import and media regression for ccpt-6 (and earlier single-face) packages; not a learning-effect test.

  python scripts/validate_package.py out/<deck>.apkg                    # audio-pending packages are recognised and reported
  python scripts/validate_package.py out/<deck>.apkg --require-audio    # a finished package: every page must carry decodable audio
  python scripts/validate_package.py out/<deck>.apkg --output out/validate.json

Needs the `anki` Python package (pip install -r scripts/requirements-validate.txt) and ffmpeg for decoding audio.
"""
import argparse, json, shutil, sys, tempfile, subprocess
from pathlib import Path
from html.parser import HTMLParser


class ValidationError(AssertionError):
    pass


def ensure(cond, message):
    if not cond:
        raise ValidationError(message)


class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.sides=[];self.players=[];self.audio=[];self.pending=False;self.quiz_attributes=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        self.quiz_attributes.extend(name for name in ('data-choice','data-correct') if name in a)
        if 'data-side' in a:self.sides.append(a['data-side'])
        if a.get('data-audio-pending')=='1':self.pending=True
        if tag=='button' and ('data-audio' in a or a.get('data-control')=='play'):self.players.append(a)
        if tag=='audio':self.audio.append(a.get('src',''))

def inspect_page(markup, allow_pending=True):
    page=Page();page.feed(markup)
    ensure(not page.quiz_attributes, 'Default cards must not contain quiz attributes')
    ensure(page.sides==['read'] and len(page.players)==1, 'Single complete page and exactly one narration control required')
    ensure(len(page.audio)==1, 'Exactly one page audio element required')
    player=page.players[0];name=player.get('data-audio','').strip()
    if page.pending:
        ensure(allow_pending, 'Audio pending: this package has no narration yet (built with --audio-pending); fill it as 补语音.txt says, or drop --require-audio')
        ensure(not name and not page.audio[0] and 'disabled' in player, 'Pending audio must be empty and its player disabled')
        return None
    ensure(name and page.audio[0]==name and 'disabled' not in player, 'Narration control and audio must reference the same nonempty local media')
    ensure(Path(name).name==name and name not in ('.','..') and ':' not in name, 'Narration must use a bundled media filename')
    return name

def load_anki(extra_path=None):
    if extra_path:sys.path.insert(0,str(extra_path))
    try:
        from anki.collection import Collection
        from anki import import_export_pb2,buildinfo
        from anki.scheduler.v3 import CardAnswer
    except ImportError:
        sys.exit('✗ anki_missing: the anki Python package is needed to import the deck in isolation.\n'
                 '  Run: pip install -r scripts/requirements-validate.txt   (about 30 MB; not needed for building or filling audio)\n'
                 '  If it cannot be installed here, skip this check and say "未做导入验证" in the delivery note.')
    return Collection,import_export_pb2,buildinfo,CardAnswer

def validate(package, allow_pending=True, anki_packages=None):
    Collection,import_export_pb2,buildinfo,CardAnswer=load_anki(anki_packages)
    with tempfile.TemporaryDirectory(prefix='ccpt-validation-') as temp:
        col=Collection(str(Path(temp)/'collection.anki2'))
        req=import_export_pb2.ImportAnkiPackageRequest(package_path=str(Path(package).resolve()),options=import_export_pb2.ImportAnkiPackageOptions(with_scheduling=False))
        col.import_anki_package(req)
        ensure(col.card_count()>0, 'The package imported no cards')
        decoded=[];pending=0
        for cid in col.find_cards(''):
            card=col.get_card(cid);note=card.note();q=card.question();name=inspect_page(q,allow_pending)
            if 'FrontHTML' in note.keys():
                ensure(note['FrontHTML']==note['BackHTML'],'Both templates must expose the same complete lesson')
            else:
                ensure('Page' in note.keys() and note['Page'].strip(),'ccpt-6 notes carry the complete page in Page')
            ensure(card.template()['qfmt']==card.template()['afmt'], 'Front and back templates must be the same single page')
            if name is None:
                pending+=1
            else:
                media=Path(col.media.dir())/name;ensure(media.is_file(),f'missing media {name}')
                ensure(shutil.which('ffmpeg'), 'ffmpeg_missing: install ffmpeg to decode the narration (Windows: winget install Gyan.FFmpeg | macOS: brew install ffmpeg | Linux: sudo apt install ffmpeg)')
                result=subprocess.run(['ffmpeg','-v','error','-i',str(media),'-f','null','-'],capture_output=True)
                ensure(result.returncode==0, result.stderr.decode(errors='replace'));decoded.append(name)
        # Create a real scheduler record in the isolated collection before repeat import.
        col.decks.select(col.get_card(col.find_cards('')[0]).did)
        queued=col.sched.get_queued_cards()
        ensure(queued and queued.cards, 'No card is due after import')
        qc=queued.cards[0];card=col.get_card(qc.card.id);card.start_timer();answer=col.sched.build_answer(card=card,states=qc.states,rating=CardAnswer.GOOD)
        col.sched.answer_card(answer)
        before=col.db.all('select id,nid,did,ord,type,queue,due,ivl,factor,reps,lapses,left,odue,odid,flags,data from cards order by id')
        logs=col.db.all('select * from revlog order by id');guids=col.db.all('select id,guid from notes order by id');ensure(logs, 'Answering a card wrote no review log')
        col.import_anki_package(req)
        ensure(before==col.db.all('select id,nid,did,ord,type,queue,due,ivl,factor,reps,lapses,left,odue,odid,flags,data from cards order by id'), 'Re-import changed card identity or scheduling')
        ensure(logs==col.db.all('select * from revlog order by id') and guids==col.db.all('select id,guid from notes order by id'), 'Re-import changed review logs or note GUIDs')
        missing=list(col.media.check().missing);ensure(not missing, f'missing media: {missing}')
        result={'anki_backend':buildinfo.version,'cards':col.card_count(),'notes':col.note_count(),'decoded_audio':len(set(decoded)),'audio_pending_cards':pending,
                'audio':'pending' if pending else 'complete','repeat_import_preserved_card_identity_schedule_and_review_log':True,
                'scope':'Isolated backend only; real rendering, sound and shortcuts require native checks.'}
        col.close()
    return result

def main(argv=None):
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8',errors='replace')
    p=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('package',type=Path);p.add_argument('--anki-packages',type=Path,help='folder holding the anki package if it is not installed')
    p.add_argument('--require-audio',action='store_true',help='fail on audio-pending pages (use for a finished package)')
    p.add_argument('--allow-text-only-test',action='store_true',help=argparse.SUPPRESS)  # accepted for compatibility; audio-pending packages pass by default
    p.add_argument('--output',type=Path,help='also write the result as JSON here')
    a=p.parse_args(argv)
    try:
        result=validate(a.package,allow_pending=not a.require_audio,anki_packages=a.anki_packages)
    except ValidationError as error:
        sys.exit(f'✗ {error}')
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2), encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))

if __name__=="__main__":main()
