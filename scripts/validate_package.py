"""Validate packaged media and repeated import in an isolated collection.
Requires a Python environment compatible with the target Anki backend.
python validate_package.py deck.apkg --anki-packages /path/to/app_packages --output report.json
"""
import argparse,json,sys,tempfile,re
from pathlib import Path
from html.parser import HTMLParser
class VisibleFront(HTMLParser):
 def __init__(self):super().__init__();self.depth=0;self.sides=[];self.leak=False
 def handle_starttag(self,tag,attrs):
  if tag=="template":self.depth+=1
  if not self.depth:
   a=dict(attrs)
   if "data-side" in a:self.sides.append(a["data-side"])
   if "data-correct" in a:self.leak=True
 def handle_endtag(self,tag):
  if tag=="template":self.depth-=1
p=argparse.ArgumentParser();p.add_argument('package',type=Path);p.add_argument('--anki-packages',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
if a.anki_packages:sys.path.insert(0,str(a.anki_packages))
from anki.collection import Collection
from anki import import_export_pb2,buildinfo
with tempfile.TemporaryDirectory(prefix='ccpt-validation-') as temp:
 col=Collection(str(Path(temp)/'collection.anki2'))
 req=import_export_pb2.ImportAnkiPackageRequest(package_path=str(a.package.resolve()),options=import_export_pb2.ImportAnkiPackageOptions(with_scheduling=False))
 col.import_anki_package(req);before=col.card_count();notes=col.note_count();assert before>0
 missing=list(col.media.check().missing);assert not missing,missing
 for cid in col.find_cards(''):
  card=col.get_card(cid);q=card.question()
  custom_media=set(re.findall(r'data-audio="([^"]+)"',' '.join(card.note().fields)))
  assert all((Path(col.media.dir())/name).is_file() for name in custom_media),'Custom audio reference missing after import'
  front=VisibleFront();front.feed(q)
  assert front.sides==['front'] and not front.leak,'Visible front contains answer state'
  assert 'data-side="back"' in card.answer()
 col.import_anki_package(req);assert col.card_count()==before and col.note_count()==notes,'Repeated import duplicates notes'
 result={'anki_backend':buildinfo.version,'cards':before,'notes':notes,'repeated_import_cards':col.card_count(),'missing_media':missing,'scope':'Isolated backend import only; actual window and playback require separate verification.'}
 col.close()
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))
