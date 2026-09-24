from speech_backend import synthesize_original
"""Build an offline Anki deck from authored SVG scenes and spoken explanations.
Usage: python build_deck.py input.json output_dir [--templates path]
Dependencies: genanki==0.13.1 edge-tts==7.2.8, ffmpeg, ffprobe.
"""
import argparse,asyncio,hashlib,html,json,re,subprocess,tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
import edge_tts,genanki

SPEECH={}
def esc(v):return html.escape(str(v),quote=True)
def audio(text,voice):
 name='ccpt_'+hashlib.sha256((voice+'\0'+text+'\0atempo=1.5').encode()).hexdigest()[:20]+'.mp3'
 SPEECH[name]={'file':name,'text':text,'voice':voice,'speed':1.5,'synthesis_rate':'+0%','tempo_filter':'atempo=1.5'}
 return name

def check_svg(svg):
 root=ET.fromstring(svg)
 assert root.tag.split('}')[-1]=='svg','Scene requires SVG'
 assert 'viewBox' in root.attrib,'SVG needs viewBox'
 for e in root.iter():
  tag=e.tag.split('}')[-1].lower()
  assert tag not in {'script','foreignobject','iframe','audio','video'},'Unsupported active SVG element'
  for k,v in e.attrib.items():
   k=k.split('}')[-1].lower()
   assert not k.startswith('on'),'Inline events are not part of the scene format'
   assert not re.search(r'(?:https?:|javascript:|file:|data:|@import)',v,re.I),'Use bundled local assets only'
   if k in {'href','src'}:assert v.startswith('#'),'External SVG references require an explicit renderer extension'
   assert not re.search(r'url\(\s*["\']?(?!#)[^\s]',v,re.I),'Only internal SVG references allowed'
 return svg

def render_svg(svg,voice):
 check_svg(svg)
 return re.sub(r'data-say="([^"]*)"',lambda m:'data-audio="'+audio(html.unescape(m[1]),voice)+'"',svg)

def readbutton(text,voice):
 return '<button class="read" data-audio="'+audio(text,voice)+'" aria-label="朗读这段内容" title="朗读">◖))</button>'
def side(card,data,back=False):
 which='back' if back else 'front';voice=data.get('voice','zh-CN-YunyiMultilingualNeural');scenes=card[which]
 out=f'<main class="ccpt" data-note="{esc(card["id"])}" data-side="{which}"><header class="{'back-title' if back else ''}"><div class="eyebrow">PHYSICS · 图像概念</div><div class="row title-row"><h1 class="title">{esc(card["title"])}</h1>'+readbutton(card['title'],voice)+'</div></header>'
 if back:
  out+='<div class="steps" role="tablist" aria-label="讲解的三个部分">'+''.join(f'<button data-stage="{i}" role="tab" aria-selected="false">{i+1} · {esc(x["heading"])}</button>' for i,x in enumerate(scenes))+'</div>'
 out+='<div class="canvas">'
 for i,s in enumerate(scenes):
  out+=f'<section class="scene {'front' if not back else ''}{' active' if i==0 else ''}" data-audio="{audio(s["narration"],voice)}" data-heading="{esc(s["heading"])}" data-narration="{esc(s["narration"])}">'+render_svg(s['svg'],voice)
  out+='<div class="explain">'
  if not back:
   out+='<div class="case"><span>'+esc(card['context'])+'</span>'+readbutton(card['context'],voice)+'</div><div class="task"><p class="question">'+esc(card['question'])+'</p>'+readbutton(card['question'],voice)+'</div>'
  else:
   if i==0:out+='<div class="answer"><p>'+esc(card['answer'])+'</p>'+readbutton(card['answer'],voice)+'</div>'
   out+='<h2>'+esc(s['heading'])+'</h2><div class="row caption-row"><p class="caption">'+esc(s['caption'])+'</p>'+readbutton(s['caption'],voice)+'</div>'
   gl=card.get('glossary',[])[:2] if i==0 else []
   if gl:out+='<div class="glossary">'+''.join('<div class="gloss"><span><b>'+esc(k)+'</b><br>'+esc(v)+'</span>'+readbutton(k+'。'+v,voice)+'</div>' for k,v in gl)+'</div>'
  out+='</div>'
  out+='</section>'
 out+='</div>'

 out+='<nav class="controls" aria-label="讲解控制">'
 if not back:out+='<button data-control="reveal" class="primary">看图解</button><span class="helper">可以直接学习，也可以先回答。</span>'
 if back:out+='<button data-control="prev">返回上一段</button>'
 out+='<button data-control="play" class="audio-main" aria-pressed="false">▶ 听这一段 · 1.5×</button>'
 if back:out+='<button data-control="next">继续看</button><span class="counter"></span>'
 out+='<span class="spacer"></span><button data-control="text" class="more">完整文字与出处</button></nav><div class="flash-status" aria-live="polite"></div>'
 out+='<aside class="modal" hidden><div class="sheet"><button data-control="close">返回图解</button><p class="narration"></p><div>'+''.join('<p><b>'+esc(k)+'</b>：'+esc(v)+'</p>' for k,v in card.get('glossary',[]))+'</div><p class="source">'+esc(card.get('source',data['source']))+'</p></div></aside>'
 names=sorted(set(re.findall('data-audio="([^"]+)"',out)))
 out+='<div class="media-index" aria-hidden="true">'+''.join('<audio preload="none" src="'+name+'"></audio>' for name in names)+'</div></main>'
 return out

def duration(p):return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(p)],text=True))
async def synthesize(media):
 limit=asyncio.Semaphore(3)
 async def one(e):
  async with limit:
   dest=media/e['file']
   if not dest.exists():
    with tempfile.TemporaryDirectory() as tmp:
     original=Path(tmp)/'original.mp3'
     for attempt in range(3):
      try:
       e['provider']=await synthesize_original(e['text'],e['voice'],original);break
      except Exception:
       if attempt==2:
        print('Failed speech:',repr(e['text']),flush=True);raise
       await asyncio.sleep(attempt+1)
     e['original_duration']=duration(original)
     subprocess.run(['ffmpeg','-v','error','-y','-i',str(original),'-af','atempo=1.5','-codec:a','libmp3lame','-q:a','3',str(dest)],check=True)
   if 'duration' not in e:e['duration']=duration(dest)
 await asyncio.gather(*(one(e) for e in SPEECH.values()))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('output',type=Path);ap.add_argument('--preview-only',action='store_true');ap.add_argument('--templates',type=Path,default=Path(__file__).resolve().parent.parent/'assets');args=ap.parse_args()
 data=json.loads(args.input.read_text());out=args.output;out.mkdir(parents=True,exist_ok=True);media=out/'media';media.mkdir(exist_ok=True)
 assert data['source'] and data['guid_namespace'];ids=[c['id'] for c in data['cards']];assert len(ids)==len(set(ids))
 css=(args.templates/'teaching-card.css').read_text();js=(args.templates/'teaching-card.js').read_text()
 fields=['StableID','Label','Prompt','Answer','FrontHTML','BackHTML','Source','Target']
 model=genanki.Model(data['model_id'],data.get('model_name','清晰单卡 · 原型 0.1'),fields=[{'name':f} for f in fields],templates=[{'name':'理解与回忆','qfmt':'{{FrontHTML}}<script>'+js+'</script>','afmt':'{{BackHTML}}<script>'+js+'</script>','bqfmt':'{{Prompt}}','bafmt':'{{Answer}}'}],css=css,sort_field_index=1)
 deck=genanki.Deck(data['deck_id'],data['title'])
 for i,c in enumerate(data['cards']):
  assert c['target'] and c['question'] and c['answer'] and c['front'] and c['back']
  if c.get('kind')=='mcq':
   assert c['correct'] in range(4)
   choices=set(re.findall(r'data-choice="([0-3])"',''.join(s['svg'] for s in c['front'])))
   assert choices=={'0','1','2','3'},'MCQ needs four front choices'
  fh,bh=side(c,data),side(c,data,True)
  if True:fh=fh.replace('</main>','<template class="ccpt-answer">'+bh+'</template></main>')
  deck.add_note(genanki.Note(model=model,fields=[c['id'],c['label'],c['question'],c['answer'],fh,bh,esc(c.get('source',data['source'])),esc(c['target'])],guid=genanki.guid_for(data['guid_namespace'],c['id']),tags=['ccpt',c['kind']],due=i+1))
  for which,body in [('front',fh),('back',bh)]:
   preview=body.replace('data-audio="ccpt_','data-audio="media/ccpt_').replace('src="ccpt_','src="media/ccpt_')
   (out/f'preview-{i+1}-{which}.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+css+'</style><body class="card">'+preview+'<script>'+js+'</script></body></html>')
 if args.preview_only:
  (out/'cards.json').write_text(json.dumps(data,ensure_ascii=False,indent=2));print('preview',len(ids));return
 old_manifest=out/'speech-manifest.json'
 if old_manifest.exists():
  for e in json.loads(old_manifest.read_text()):
   if e['file'] in SPEECH and (media/e['file']).exists():
    for key in ['duration','original_duration']:
     if key in e:SPEECH[e['file']][key]=e[key]
 asyncio.run(synthesize(media))
 manifest=out/'speech-manifest.json';old={x['file']:x for x in json.loads(manifest.read_text())} if manifest.exists() else {}
 for name,e in SPEECH.items():
  if 'original_duration' not in e and name in old and 'original_duration' in old[name]:e['original_duration']=old[name]['original_duration']
 manifest.write_text(json.dumps(list(SPEECH.values()),ensure_ascii=False,indent=2))
 package=genanki.Package(deck);package.media_files=[str(media/n) for n in SPEECH];package.write_to_file(str(out/'图像概念卡.apkg'))
 (out/'cards.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(json.dumps({'cards':len(ids),'audio':len(SPEECH),'package':str(out/'图像概念卡.apkg')},ensure_ascii=False))
if __name__=='__main__':
 import teaching_renderer,sys
 teaching_renderer.install(sys.modules[__name__])
 main()
