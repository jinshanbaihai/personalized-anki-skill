from pathlib import Path
import json,re,html,sys,asyncio,shutil,genanki,argparse
import build_deck as old
parser=argparse.ArgumentParser(description='Build semantic maps and diagram cards')
parser.add_argument('input',type=Path);parser.add_argument('output',type=Path);parser.add_argument('--preview',action='store_true');args=parser.parse_args()
ASSETS=Path(__file__).resolve().parent.parent/'assets'
OUT=args.output;OUT.mkdir(parents=True,exist_ok=True);media=OUT/'media';media.mkdir(exist_ok=True)
data=json.loads(args.input.read_text());esc=old.esc
VOICE=data.get('voice','zh-CN-XiaoxiaoNeural')
for card in data['cards']:
 if card.get('kind') not in ('concept','diagram'):
  raise ValueError('This generator creates concept/diagram cards only; quizzes require a separately requested workflow.')
def speech(text):return old.audio(text,VOICE)
def button(text):return '<button class="speak" data-audio="'+speech(text)+'" aria-label="朗读或暂停" aria-pressed="false" title="朗读或暂停">▶</button>'
def rich(text,c):
 # A few useful concept distinctions; other technical words remain readable emphasis.
 roles=c.get('color_roles',[]);terms={term:r['color'] for r in roles for term in r['terms'] if len(term)>1}
 pattern='|'.join(re.escape(t) for t in sorted(terms,key=len,reverse=True))
 if not pattern:return esc(text)
 out=[];end=0
 for m in re.finditer('(?<![A-Za-z])(?:'+pattern+')(?![A-Za-z])',text,re.I):
  out.append(esc(text[end:m.start()]));col=next((v for k,v in terms.items() if k.lower()==m[0].lower()),'#075ac8');out.append('<strong class="term" style="--term:'+col+'">'+esc(m[0])+'</strong>');end=m.end()
 out.append(esc(text[end:]));return ''.join(out)
def unit(text,c):return '<div class="unit"><div class="words">'+rich(text,c)+'</div></div>'
def leaf(node,c):return '<li class="leaf">'+unit(node['text'],c)+('<ul class="leaves">'+''.join(leaf(x,c) for x in node.get('children',[]))+'</ul>' if node.get('children') else '')+'</li>'
def narration(c,back):
 parts=[c['question']]
 has_figure=c.get('figure_svg') and (back or c.get('figure_on_front',True))
 if not back:parts.append(c['context'])
 if has_figure:
  if not c.get('diagram_narration'):raise ValueError(c['id']+': diagram_narration must explain the actual diagram')
  parts.append(c.get('front_diagram_narration',c['diagram_narration']) if not back else c['diagram_narration'])
 if back or c['kind']=='concept':
  parts.append('接下来按分支顺序阅读。'+c.get('map_root',c['question']))
  nodes=c['tree'] if back else [{'text':x} for x in c.get('recall_branches',[x['text'] for x in c['tree']])]
  def walk(n):
   parts.append(n['text'])
   for child in n.get('children',[]):walk(child)
  for n in nodes:walk(n)
 return '。'.join(t.rstrip('。') for t in parts if t)
def body(c,back):
 side='back' if back else 'front';out='<main class="ccptv4" data-note="'+esc(c['id'])+'" data-side="'+side+'">'
 out+='<header class="unit"><h1 class="words">'+rich(c['question'],c)+'</h1>'+button(narration(c,back))+'</header>'
 if not back:out+='<div class="context">'+unit(c['context'],c)+'</div>'
 if back:out+='<div class="answer">'+unit(c['answer'],c)+'</div>'
 out+='<div class="canvas-fit"><div class="board-content '+('has-figure' if c.get('figure_svg') and back else '')+'">'
 if c.get('figure_svg') and (back or c.get('figure_on_front',True)):
  old.check_svg(c['figure_svg']);svg=re.sub(r' data-say="[^"]*"','',c['figure_svg']);out+='<figure>'+svg+'</figure>'

 if back or c['kind']=='concept':
  out+='<div class="mindmap '+('map-outline' if not back else '')+'"><svg class="map-lines" aria-hidden="true"></svg><div class="map-root">'+unit(c.get('map_root',c['question']),c)+'</div><ol class="map">'
  nodes=c['tree'] if back else [{'text':x,'children':[]} for x in c.get('recall_branches',[x['text'] for x in c['tree']])]
  for n in nodes:out+='<li class="branch"><div class="branch-head">'+unit(n['text'],c)+'</div><ul class="leaves">'+''.join(leaf(x,c) for x in n.get('children',[]))+'</ul></li>'
  out+='</ol></div>'
 out+='</div></div>'
 out+='<div class="audio-controls"><span class="audio-status" aria-live="polite"></span><button class="view-button" data-view="fit">全图</button><button class="view-button" data-view="zoom">放大细节</button></div>'
 if back:out+='<details><summary>材料出处</summary><div class="source">'+unit(c['source'],c)+'</div></details>'
 names=set(re.findall('data-audio="([^"]+)"',out));out+='<div class="media-index" aria-hidden="true">'+''.join('<audio preload="none" src="'+n+'"></audio>' for n in sorted(names))+'</div></main>';return out
css=(ASSETS/'teaching-card.css').read_text()+'\n'+(ASSETS/'logic-card.css').read_text()
legacy=(ASSETS/'teaching-card.js').read_text();newjs=(ASSETS/'logic-card.js').read_text();js="if(document.querySelector('.ccptv4')){"+newjs+'}else{'+legacy+'}'
model=genanki.Model(data['model_id'],data.get('model_name','CCPT · 概念关系与讲图'),fields=[{'name':x} for x in ['StableID','Label','Prompt','Answer','FrontHTML','BackHTML','Source','Target']],templates=[{'name':'理解与回忆','qfmt':'{{FrontHTML}}<script>'+js+'</script>','afmt':'{{BackHTML}}<script>'+js+'</script>','bqfmt':'{{Prompt}}','bafmt':'{{Answer}}'}],css=css,sort_field_index=1)
decks={};rendered={}
for i,c in enumerate(data['cards']):
 fh,bh=body(c,False),body(c,True);rendered[c['id']]={'front':fh,'back':bh};did=c['deck_id'];deck=decks.setdefault(did,genanki.Deck(did,c['deck']))
 deck.add_note(genanki.Note(model=model,fields=[c['id'],c['id'],c['question'],c['answer'],fh,bh,esc(c['source']),esc(c['target'])],guid=genanki.guid_for(c['namespace'],c['id']),tags=['ccpt','semantic-v4',c['kind']],due=i+1))
 for side,b in [('front',fh),('back',bh)]:
  b=b.replace('data-audio="ccpt_','data-audio="media/ccpt_').replace('src="ccpt_','src="media/ccpt_')
  (OUT/(c['id']+'-'+side+'.html')).write_text('<!doctype html><html lang="zh-CN"><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(c['question'])+'</title><style>'+css+'</style><body class="card">'+b+'<script>'+js+'</script></body></html>')
(OUT/'cards.json').write_text(json.dumps(data,ensure_ascii=False,indent=2));(OUT/'rendered.json').write_text(json.dumps(rendered,ensure_ascii=False));(OUT/'model.json').write_text(json.dumps({'css':css,'js':js},ensure_ascii=False))
# Reuse locally generated original-speed-then-atempo audio only by exact content hash.
for path in args.output.parent.glob('*/media/ccpt_*.mp3'):
 if path.name in old.SPEECH and not (media/path.name).exists():shutil.copy2(path,media/path.name)
if '--preview' not in sys.argv:
 asyncio.run(old.synthesize(media));(OUT/'speech-manifest.json').write_text(json.dumps(list(old.SPEECH.values()),ensure_ascii=False,indent=2));pkg=genanki.Package(list(decks.values()));pkg.media_files=[str(media/n) for n in old.SPEECH];pkg.write_to_file(str(OUT/'概念关系与讲图.apkg'))
print(json.dumps({'cards':len(data['cards']),'audio':len(old.SPEECH),'output':str(OUT)},ensure_ascii=False),flush=True)
