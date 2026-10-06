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
 const voiceLabel=(status?.textContent||'').split('·')[0].trim();
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
    if(!audio.paused&&!inView(el)&&Date.now()-lastUserScroll>2500)el.scrollIntoView({block:'center',behavior:reduce?'auto':'smooth'});}
  }
  root.classList.toggle('narration-paused',audio.paused&&!!active);
 }
 on(window,'wheel',()=>{lastUserScroll=Date.now();},{passive:true});
 on(window,'touchmove',()=>{lastUserScroll=Date.now();},{passive:true});
 on(button,'click',async()=>{
  if(cleaned||pending||button.disabled)return;
  if(!audio.paused){audio.pause();return;}
  if(audio.ended)audio.currentTime=0;
  try{if(audio.error)audio.load();failed=false;audio.preservesPitch=true;audio.playbackRate=speed/encoded;await audio.play();if(cleaned)audio.pause();}
  catch(e){if(!cleaned){failed=true;unavailable();}}
 });
 on(speedBtn,'click',()=>{if(pending)return;speed=speed===2?1.5:2;label();audio.playbackRate=speed/encoded;if(!audio.paused)setStatus(`${voiceLabel} · ${speed}×`);});
 on(audio,'play',()=>{button.textContent='Ⅱ';button.setAttribute('aria-pressed','true');setStatus(`${voiceLabel} · ${speed}×`);follow();});
 on(audio,'pause',()=>{if(pending||failed||audio.error){unavailable();return;}button.textContent=audio.ended?'↻':'▶';button.setAttribute('aria-pressed','false');setStatus(audio.ended?'讲解结束 · Space 重播':'已暂停 · Space 继续');follow();});
 on(audio,'error',()=>{failed=true;clearCue();unavailable();});
 on(audio,'ended',()=>{button.textContent='↻';setStatus('讲解结束 · Space 重播');clearCue();});
 for(const ev of ['timeupdate','seeking','seeked'])on(audio,ev,follow);
 label();
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
   const chrome=!!el.closest('.cc-meta,.cc-foot,.mark-badge,.tagline,.def-label,.def-src,.pf-src,.tbl-cap,.cc-player,.mm-rel,.blk-label,.mm-label,.ao-badge,.def-lists h4');
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
   clipped:[...root.querySelectorAll('.blk')].filter(b=>b.scrollWidth>b.clientWidth+2&&getComputedStyle(b).overflowX!=='auto').map(b=>b.dataset.node),
   mapOverlaps:overlaps.length,maps:[...root.querySelectorAll('.mm')].map(m=>({layout:m.dataset.applied||m.dataset.layout,depth:+m.dataset.depth})),
   players:root.querySelectorAll('.speak').length,math:root.querySelectorAll('math').length,cues:cues.length,speed,encoded,pending};
 };
 window.ccptCleanup=()=>{cleaned=true;ctl.abort();try{audio.pause();audio.currentTime=0;}catch(e){}clearCue();if(window.ccptLayoutCleanup)window.ccptLayoutCleanup();if(window.ccptSingleCleanup)window.ccptSingleCleanup();};
 on(window,'pagehide',window.ccptCleanup,{once:true});
})();
