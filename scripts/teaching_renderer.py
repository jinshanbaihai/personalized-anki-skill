import re
def install(b):
 readbutton,audio,render_svg=b.readbutton,b.audio,b.render_svg
 esc=lambda v:b.esc(v).replace("\n","&#10;")
 def side(card,data,back=False):
  which='back' if back else 'front';voice=card.get('voice',data.get('voice','zh-CN-YunxiNeural'));scenes=card[which]
  out=f'<main class="ccpt teaching" data-note="{esc(card["id"])}" data-side="{which}"><header class="title-row row"><h1 class="title">{esc(card["title"])}</h1>'+readbutton(card['title'],voice)+'</header>'
  if back:
   out+='<div class="learning-nav">'
   for name in ['概念讲解','理解检查','难点应用']:
    idx=next((i for i,s in enumerate(scenes) if s.get('section')==name),None)
    if idx is not None:out+=f'<button data-stage="{idx}">{name}</button>'
   out+='<select class="chapter" aria-label="选择讲解或检查">'+''.join(f'<option value="{i}">{i+1}. {esc(s["heading"])}</option>' for i,s in enumerate(scenes))+'</select></div>'
  out+='<div class="canvas">'
  for i,s in enumerate(scenes):
   voice=s.get('voice',card.get('voice',data.get('voice','zh-CN-YunxiNeural')))
   out+=f'<section class="scene {"front" if not back else ""}{" active" if i==0 else ""}" data-section="{esc(s.get("section","概念讲解"))}" data-audio="{audio(s["narration"],voice)}" data-heading="{esc(s["heading"])}" data-narration="{esc(s["narration"])}">'
   out+='<div class="visual">'+render_svg(s['svg'],voice)
   lab_markup=''
   if s.get('lab'):
    lab_start=len(out)
    name=s['lab'];out+=f'<div class="lab" data-lab="{name}">'
    buttons=[('bias','移回基准','把整组读数移到基准，保持分散程度。'),('spread','扩大分散','保持平均位置，扩大读数的分散。'),('reset','恢复原状','恢复到开始时的读数。')] if name=='measurement' else [('0','沿杆推','force 沿着杆，作用线经过 pivot。'),('30','斜着推','force 与杆夹角为三十度。'),('90','垂直推','force 与杆垂直，perpendicular distance 等于杆长。')]
    out+='<div class="presets">'+''.join(f'<span><button data-preset="{v}">{label}</button>'+readbutton(speech,voice)+'</span>' for v,label,speech in buttons)+'</div>'
    inputs=[('bias','平均位置',0,6,6,.1,'移动平均位置，保持读数之间的间隔。'),('spread','分散程度',.2,2,.2,.1,'改变分散程度，保持平均位置。')] if name=='measurement' else [('angle','force 与杆的夹角',0,90,35,1,'改变 force 与杆的夹角，保持 force 的大小和施力点。')]
    for key,label,lo,hi,value,step,speech in inputs:
     out+=f'<label class="slider-label"><span>{label}</span><input aria-label="{label}" type="range" data-param="{key}" min="{lo}" max="{hi}" step="{step}" value="{value}">'+readbutton(speech,voice)+'</label>'
    out+='<output class="lab-values" aria-live="polite"></output></div>'
    lab_markup=out[lab_start:];out=out[:lab_start]
   out+='</div><div class="explain">'
   if not back:
    out+='<div class="case"><span>'+esc(card['context'])+'</span>'+readbutton(card['context'],voice)+'</div><div class="task"><p class="question">'+esc(card['question'])+'</p>'+readbutton(card['question'],voice)+'</div><p class="entry-note">初次接触可以从概念讲解开始；熟悉后可以直接做判断。过程无需书写记录。</p>'
   else:
    out+='<div class="section-heading row"><h2>'+esc(s['heading'])+'</h2>'+readbutton(s['heading'],voice)+'</div>'
    out+=lab_markup
    if 'quiz' in s:
     q=s['quiz'];out+=f'<div class="quiz" data-correct="{q["correct"]}" data-repair="{q["repair"]}"><div class="row caption-row"><p class="caption">{esc(q["question"])}</p>'+readbutton(q['question'],voice)+'</div><div class="choices" role="group" aria-label="四个选项">'
     for k,(choice,reason) in enumerate(zip(q['choices'],q['reasons'])):
      out+=f'<div class="choice-line"><button class="choice" data-choice="{k}" aria-pressed="false"><b>{chr(65+k)}</b><span>{esc(choice)}</span><span class="selection"></span></button>'+readbutton(choice,voice)+f'<template class="feedback-copy"><p>{esc(reason)}</p>'+readbutton(reason,voice)+'</template></div>'
     out+='</div><p class="selected-message" aria-live="polite">选择后可以修改，再确认判断。</p><button class="confirm primary" disabled>确认判断</button><div class="feedback" hidden aria-live="polite"></div></div>'
    else:
     out+=''.join('<div class="row caption-row"><p class="caption">'+esc(p)+'</p>'+readbutton(p,voice)+'</div>' for p in s['caption'].split('\n\n'))
   out+='</div></section>'
  out+='</div><nav class="controls">'
  if not back:
   out+='<button data-control="reveal" class="primary">先理解概念</button><button data-control="test">直接做判断</button>'
  else:out+='<button data-control="prev">上一段</button>'
  out+='<button data-control="play" class="audio-main">▶ 听这一段 · 1.5×</button>'
  if back:out+='<button data-control="next">下一段</button><span class="counter"></span>'
  out+='<span class="spacer"></span><button data-control="text" class="more">全文与出处</button></nav><div class="flash-status" aria-live="polite"></div><aside class="modal" hidden><div class="sheet"><button data-control="close">返回图解</button><p class="narration"></p><p class="source">'+esc(card['source'])+'</p></div></aside></main>'
  names=sorted(set(re.findall('data-audio="([^"]+)"',out)))
  out=out.removesuffix('</main>')+'<div class="media-index" aria-hidden="true">'+''.join('<audio preload="none" src="'+name+'"></audio>' for name in names)+'</div></main>'
  return out
 b.side=side
