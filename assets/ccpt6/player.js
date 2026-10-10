/* ccpt-6 page player: one narration per page, measured cues, gentle follow-scroll. */
(()=>{
 if(window.ccptCleanup)window.ccptCleanup();
 const root=document.querySelector('.ccpt6');if(!root)return;
 const ctl=new AbortController(),on=(el,ev,fn,opt)=>el&&el.addEventListener(ev,fn,Object.assign({signal:ctl.signal},opt||{}));
 const audio=root.querySelector('audio'),button=root.querySelector('.speak'),speedBtn=root.querySelector('.speed'),status=root.querySelector('.audio-status');
 let data={};try{data=JSON.parse(root.querySelector('.cc-data')?.textContent||'{}');}catch(e){data={};}
 const cues=(data.narration&&data.narration.cues)||[],pending=root.dataset.audioPending==='1';
 const reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
 const encoded=parseFloat(speedBtn?.dataset.encoded||'2')||2;let speed=encoded;
 const voiceLabel=(status?.textContent||'').split('·')[0].trim(),total=(data.narration&&data.narration.duration)||0;
 const clock=s=>{s=Math.max(0,Math.round(s));return Math.floor(s/60)+':'+String(s%60).padStart(2,'0');};
 const remaining=()=>total?' · 剩 '+clock((total-audio.currentTime)*encoded/speed):'';
 let cleaned=false,failed=false,active=null,lastUserScroll=0;
 const target=id=>id===null||id==='title'?root.querySelector('h1'):root.querySelector(`[data-node="${CSS.escape(id)}"]`);
 function label(){if(speedBtn){speedBtn.textContent=speed+'×';speedBtn.dataset.speed=String(speed);}}
 function setStatus(t){if(status)status.textContent=t;}
 function unavailable(){button.textContent='▶';button.setAttribute('aria-pressed','false');setStatus(pending?(root.dataset.audioMessage||'语音未生成'):'语音未能播放，请检查本地音频');}
 if(pending||!audio?.getAttribute('src')){if(button)button.disabled=true;if(speedBtn)speedBtn.disabled=true;unavailable();}
 function clearCue(){root.querySelectorAll('.narrating').forEach(n=>n.classList.remove('narrating'));root.classList.remove('narration-paused');active=null;}
 const head=root.querySelector('.cc-head'),foot=root.querySelector('.cc-foot');
 function inView(el){const r=el.getBoundingClientRect(),h=window.innerHeight||document.documentElement.clientHeight;
  const top=(head?head.getBoundingClientRect().bottom:0)+6,bottom=h-(foot?foot.offsetHeight:0)-6;
  return r.top>=top&&(r.bottom<=bottom||r.height>bottom-top);}
 function follow(){
  if(cleaned||!cues.length)return;
  if(audio.ended){clearCue();return;}
  const t=audio.currentTime;let cue=null;for(const c of cues){if(t>=c.start)cue=c;else break;}if(cue&&t>cue.end+0.4)cue=null;
  if(cue!==active){
   clearCue();active=cue;
   const el=cue&&target(cue.target);
   if(el){el.classList.add('narrating');
    // Keep the narrated part visible, but never fight a reader who just scrolled.
    const free=!audio.paused&&Date.now()-lastUserScroll>2500;
    if(free&&!inView(el))el.scrollIntoView({block:'center',behavior:reduce?'auto':'smooth'});
    // A framed spot on a board that pans sideways (phone): bring it into the visible part of the board.
    const pan=el.closest('.bd-scroll');
    if(free&&pan){const r=el.getBoundingClientRect(),b=pan.getBoundingClientRect();
     if(r.left<b.left||r.right>b.right)pan.scrollTo({left:pan.scrollLeft+(r.left-b.left)-Math.max(0,(b.width-r.width)/2),behavior:reduce?'auto':'smooth'});}}
  }
  root.classList.toggle('narration-paused',audio.paused&&!!active);
 }
 // Board crops: a tap switches between the whole board and the legible size; boards wider than the column say they pan.
 function markPan(){root.querySelectorAll('.bd-crop').forEach(c=>{const s=c.querySelector('.bd-scroll');c.classList.toggle('bd-pan',!!s&&s.scrollWidth>s.clientWidth+2);});}
 on(root,'click',e=>{const s=e.target.closest&&e.target.closest('.bd-scroll');if(!s)return;s.closest('.bd-crop').classList.toggle('bd-alt');markPan();});
 root.querySelectorAll('.bd-img').forEach(img=>on(img,'load',markPan));
 on(window,'resize',markPan);markPan();
 on(window,'wheel',()=>{lastUserScroll=Date.now();},{passive:true});
 on(window,'touchmove',()=>{lastUserScroll=Date.now();},{passive:true});
 on(button,'click',async()=>{
  if(cleaned||pending||button.disabled)return;
  if(!audio.paused){audio.pause();return;}
  if(audio.ended)audio.currentTime=0;
  try{if(audio.error)audio.load();failed=false;audio.preservesPitch=true;audio.webkitPreservesPitch=true;audio.playbackRate=speed/encoded;await audio.play();if(cleaned)audio.pause();}
  catch(e){if(cleaned)return;
   // A host that requires a user gesture for audio (Anki: "Don't play audio automatically") rejects play() from a key
   // routed through the add-on; the file is fine, so ask for a click instead of reporting broken audio.
   if(e&&e.name==='NotAllowedError'){button.textContent='▶';button.setAttribute('aria-pressed','false');setStatus('点 ▶ 播放（这台设备要求先点一下）');return;}
   failed=true;unavailable();}
 });
 const playing=()=>`${voiceLabel} · ${speed}×${remaining()}`;
 on(speedBtn,'click',()=>{if(pending)return;speed=speed===2?1.5:2;label();audio.playbackRate=speed/encoded;
  if(!audio.paused)setStatus(playing());
  else if(!audio.ended&&audio.currentTime>0)setStatus('已暂停'+remaining()+' · Space 继续');
  else if(!audio.ended&&total)setStatus(`${voiceLabel} · ${speed}× · ${clock(total*encoded/speed)}`);});
 let shownSecond=-1;
 on(audio,'timeupdate',()=>{if(audio.paused)return;const sec=Math.round(audio.currentTime*encoded/speed);if(sec!==shownSecond){shownSecond=sec;setStatus(playing());}});
 on(audio,'play',()=>{button.textContent='Ⅱ';button.setAttribute('aria-pressed','true');setStatus(playing());follow();});
 on(audio,'pause',()=>{if(pending||failed||audio.error){unavailable();return;}button.textContent=audio.ended?'↻':'▶';button.setAttribute('aria-pressed','false');setStatus(audio.ended?'讲解结束 · Space 重播':'已暂停'+remaining()+' · Space 继续');follow();});
 on(audio,'error',()=>{failed=true;clearCue();unavailable();});
 on(audio,'ended',()=>{button.textContent='↻';setStatus('讲解结束 · Space 重播');clearCue();});
 for(const ev of ['timeupdate','seeking','seeked'])on(audio,ev,follow);
 label();
 // Old Android WebViews (before Chromium 109) cannot lay out MathML: fall back to the host's MathJax, else readable TeX.
 (()=>{const probe=document.createElement('div');probe.style.cssText='position:absolute;visibility:hidden';probe.innerHTML='<math><mspace width="40px"></mspace></math>';document.body.appendChild(probe);
  const ok=probe.firstChild.getBoundingClientRect().width>30;probe.remove();if(ok)return;
  root.querySelectorAll('.math[data-tex]').forEach(m=>{const d=m.classList.contains('math-display');m.textContent=(d?'\\[':'\\(')+m.dataset.tex+(d?'\\]':'\\)');});
  if(window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise([root]).catch(()=>{});})();
 if(window.ccptLayout)window.ccptLayout(root,ctl.signal);
 window.ccptAudit=()=>{
  const runs=[],walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
  while(walker.nextNode()){
   const node=walker.currentNode,el=node.parentElement;
   if(!node.textContent.trim()||!el||el.closest('script,style,title,defs,[hidden]'))continue;
   const st=getComputedStyle(el);if(st.display==='none'||st.visibility==='hidden')continue;
   const rg=document.createRange();rg.selectNodeContents(node);const b=rg.getBoundingClientRect();if(!b.width||!b.height)continue;
   let k=1;const sc=el.closest('[data-scale]');if(sc)k=parseFloat(sc.dataset.scale)||1;
   if(el instanceof SVGElement){const m=el.getScreenCTM();if(m)k=Math.hypot(m.c,m.d);}
   const chrome=!!el.closest('.cc-meta,.cc-foot,.mark-badge,.tagline,.def-label,.def-src,.pf-src,.tbl-cap,.cc-player,.mm-rel,.blk-label,.mm-label,.ao-badge,.def-lists h4,.subgoal-mark,.step-n,.step-mark,.ch-rel-cond,.pf-src-type,.cc-fb,.heur-ex,.bd-where,.cc-gap,.bd-note-head,.bd-note-exam');
   const math=!!el.closest('math');
   runs.push({text:node.textContent.trim().slice(0,60),font:+(parseFloat(st.fontSize)*k).toFixed(1),kind:math?'math':chrome?'chrome':'content'});
  }
  const vw=document.documentElement.clientWidth;
  const nodes=[...root.querySelectorAll('.mm-node')].map(n=>n.getBoundingClientRect());
  const overlaps=[];nodes.forEach((a,i)=>nodes.slice(i+1).forEach((b,j)=>{if(a.left<b.right-1&&a.right>b.left+1&&a.top<b.bottom-1&&a.bottom>b.top+1)overlaps.push([i,i+j+1]);}));
  const min=kind=>Math.min(...runs.filter(r=>r.kind===kind).map(r=>r.font),99);
  const floor={content:15,chrome:12,math:9.5};
  return {viewport:[vw,window.innerHeight],pageHeight:document.documentElement.scrollHeight,minFont:min('content'),minChrome:min('chrome'),minMath:min('math'),
   smallText:runs.filter(r=>r.font<floor[r.kind]).slice(0,10),horizontalOverflow:document.documentElement.scrollWidth>vw+1,
   clipped:[...root.querySelectorAll('.blk,.blk *')].filter(b=>{const o=getComputedStyle(b).overflowX;return (o==='hidden'||o==='clip')&&b.scrollWidth>b.clientWidth+2&&!b.closest('svg,math');}).map(b=>b.closest('[data-node]')?.dataset.node||b.className).slice(0,8),
   scrollers:[...root.querySelectorAll('.step-do,.math-display,.tbl-wrap,.ccmm,.ccchain')].filter(b=>b.scrollWidth>b.clientWidth+2).map(b=>(b.matches('.step-do,.math-display')?'math:':'wide:')+(b.closest('[data-node]')?.dataset.node||b.className)).slice(0,8),
   lineStartPunct:(()=>{const bad=[];root.querySelectorAll('.cc-body p,.cc-body li,.cc-body dd,.cc-body .mm-node,.cc-body .ch-node').forEach(el=>{const w=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);let lastTop=null;while(w.nextNode()){const t=w.currentNode;for(let i=0;i<t.length;i++){if(!'，。；：、）'.includes(t.data[i]))continue;const r=document.createRange();r.setStart(t,i);r.setEnd(t,i+1);const b=r.getBoundingClientRect();const prev=document.createRange();if(i>0){prev.setStart(t,i-1);prev.setEnd(t,i);const pb=prev.getBoundingClientRect();if(pb.top<b.top-4&&b.left<=el.getBoundingClientRect().left+24)bad.push(t.data.slice(Math.max(0,i-6),i+1));}}}});return bad.slice(0,6);})(),
   fontsFailed:document.fonts?[...document.fonts].filter(f=>f.status==='error').map(f=>f.family):[],
   mapOverlaps:overlaps.length+(window.CCMap?CCMap.audit(document).overlaps.length:0),maps:[...root.querySelectorAll('.mm')].map(m=>({layout:m.dataset.applied||m.dataset.layout,depth:+m.dataset.depth})),
   images:root.querySelectorAll('img').length,brokenImages:[...root.querySelectorAll('img')].filter(i=>i.complete&&!i.naturalWidth).map(i=>i.getAttribute('src')).slice(0,6),
   boardScale:Math.min(...[...root.querySelectorAll('.bd-img')].filter(i=>i.naturalWidth).map(i=>+(i.getBoundingClientRect().width/i.naturalWidth).toFixed(2)),9),
   players:root.querySelectorAll('.speak').length,math:root.querySelectorAll('math').length,cues:cues.length,speed,encoded,pending};
 };
 window.ccptCleanup=()=>{cleaned=true;ctl.abort();try{audio.pause();audio.currentTime=0;}catch(e){}clearCue();if(window.ccptLayoutCleanup)window.ccptLayoutCleanup();if(window.ccptSingleCleanup)window.ccptSingleCleanup();};
 on(window,'pagehide',window.ccptCleanup,{once:true});
})();
