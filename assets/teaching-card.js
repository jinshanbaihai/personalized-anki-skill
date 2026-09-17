window.ccptInit=function(){
 if(window.ccptCleanup)window.ccptCleanup();
 const root=document.querySelector('.ccpt');if(!root)return;
 const scenes=[...root.querySelectorAll('.scene')],play=root.querySelector('[data-control=play]'),status=root.querySelector('.flash-status');const playLabel='听整页';let at=0,current=null,file='',disposed=false;const a=new AbortController();
 const on=(e,t,f)=>{if(e)e.addEventListener(t,f,{signal:a.signal})};
 if(play){play.title='J：播音 / 暂停 / 继续';play.setAttribute('aria-keyshortcuts','J');}
 on(document,'keydown',e=>{
  const t=e.target;
  if(root.closest('[data-ccpt-single]')||e.repeat||e.isComposing||e.ctrlKey||e.metaKey||e.altKey||e.shiftKey||t?.isContentEditable||/^(INPUT|TEXTAREA|SELECT)$/.test(t?.tagName||''))return;
  if(e.code==='KeyJ'||e.key.toLowerCase()==='j'){e.preventDefault();e.stopPropagation();play?.click();}
 });

 function stop(){if(current){const old=current;current=null;old.pause();old.removeAttribute('src');old.load();}file='';if(play){play.textContent='▶ '+playLabel+' · 1.75×';play.setAttribute('aria-pressed','false');}}
 function safePlay(node){node.play().catch(e=>{if(current===node&&!disposed&&e.name!=='AbortError')fail();});}
 function fail(){if(disposed)return;stop();if(status)status.textContent='语音暂时没有播放，请查看文字讲解。';}
 const queue=JSON.parse(root.dataset.pagePlaylist||'[]');let clip=0;
 function startClip(){
  const item=queue[clip];if(!item){stop();play.textContent='↻ 重播整页';clip=0;return;}
  if(item.stage>=0)stage(item.stage,true);
  file=item.file;current=new Audio(file);current.playbackRate=1;const node=current;
  node.onended=()=>{if(current!==node||disposed)return;clip++;startClip();};
  node.onerror=()=>{if(current===node&&!disposed)fail();};safePlay(node);play.textContent='Ⅱ 暂停';play.setAttribute('aria-pressed','true');
 }
 function speak(){
  if(!queue.length)return;
  if(current){if(current.paused){safePlay(current);play.textContent='Ⅱ 暂停';play.setAttribute('aria-pressed','true');}else{current.pause();play.textContent='▶ 继续听';play.setAttribute('aria-pressed','false');}return;}
  clip=0;startClip();
 }
 function stage(n,keepAudio=false){if(!keepAudio)stop();at=Math.max(0,Math.min(scenes.length-1,n));scenes.forEach((s,i)=>s.classList.toggle('active',i===at));root.querySelectorAll('[data-stage]').forEach(e=>e.setAttribute('aria-selected',String(+e.dataset.stage===at)));const selector=root.querySelector('.chapter');if(selector)selector.value=String(at);root.querySelectorAll('.learning-nav [data-stage]').forEach(e=>e.setAttribute('aria-selected',String(scenes[+e.dataset.stage].dataset.section===scenes[at].dataset.section)));let c=root.querySelector('.counter');if(c)c.textContent=(at+1)+' / '+scenes.length;let p=root.querySelector('[data-control=prev]'),nxt=root.querySelector('[data-control=next]');if(p)p.disabled=at===0;if(nxt){nxt.disabled=at===scenes.length-1;nxt.textContent=at===scenes.length-1?'讲解已到最后':'继续看：'+scenes[at+1].dataset.heading;}if(status)status.textContent='';}
 on(play,'click',()=>speak());on(root.querySelector('[data-control=prev]'),'click',()=>stage(at-1));on(root.querySelector('[data-control=next]'),'click',()=>stage(at+1));root.querySelectorAll('[data-stage]').forEach(e=>on(e,'click',()=>stage(+e.dataset.stage)));
 const reveal=()=>{stop();if(typeof pycmd==='function')pycmd('ans');else{let t=root.querySelector('template.ccpt-answer');if(t){root.replaceWith(t.content.firstElementChild.cloneNode(true));window.ccptInit();}}};on(root.querySelector('[data-control=reveal]'),'click',reveal);
 const modal=root.querySelector('.modal,.transcript');on(root.querySelector('[data-control=text]'),'click',()=>{stop();modal.hidden=false;modal.querySelector('.narration').textContent=scenes.filter(s=>!s.querySelector('.quiz')).map(s=>s.dataset.heading+'\n'+s.dataset.narration).join('\n\n');modal.querySelector('[data-control=close]')?.focus();});on(root.querySelector('[data-control=close]'),'click',()=>{modal.hidden=true});on(document,'keydown',e=>{if(e.key==='Escape'){stop();if(modal)modal.hidden=true;}});on(window,'pagehide',stop);on(document,'visibilitychange',()=>{if(document.hidden)stop()});const obs=new MutationObserver(()=>{if(!root.isConnected)cleanup()});obs.observe(document.body,{childList:true,subtree:true});function cleanup(){disposed=true;stop();obs.disconnect();a.abort()} // Teaching interactions are scoped to this card; they never grade Anki for the learner.
 const chapter=root.querySelector('.chapter');on(chapter,'change',()=>stage(+chapter.value));
 window.ccptGo=stage;
 on(root.querySelector('[data-control=test]'),'click',()=>{try{sessionStorage.setItem('ccpt-test-'+root.dataset.note,'1')}catch(e){}reveal()});
 root.querySelectorAll('.quiz').forEach(q=>{
  let chosen=null,submitted=false;const msg=q.querySelector('.selected-message'),fb=q.querySelector('.feedback'),confirm=q.querySelector('.confirm');
  q.querySelectorAll('.choice').forEach(btn=>on(btn,'click',()=>{
   stop();chosen=+btn.dataset.choice;submitted=false;fb.hidden=true;fb.textContent='';confirm.disabled=false;
   q.querySelectorAll('.choice').forEach(x=>{const yes=+x.dataset.choice===chosen;x.setAttribute('aria-pressed',String(yes));x.querySelector('.selection').textContent=yes?'✓':''});
   msg.textContent='已选择 '+String.fromCharCode(65+chosen)+'。确认后查看解释。';
  }));
  on(confirm,'click',()=>{
   if(chosen===null)return;stop();submitted=true;const correct=+q.dataset.correct;
   fb.replaceChildren();const title=document.createElement('strong');title.textContent=chosen===correct?'这个判断成立。':'这次选择需要调整。';fb.appendChild(title);
   fb.appendChild(q.querySelectorAll('.feedback-copy')[chosen].content.cloneNode(true));
   const right=document.createElement('p');right.textContent='对应答案：'+String.fromCharCode(65+correct)+'。'+q.querySelectorAll('.choice')[correct].querySelector('span').textContent;fb.appendChild(right);
   const repair=document.createElement('button');repair.textContent='回到相关图解';on(repair,'click',()=>stage(+q.dataset.repair));fb.appendChild(repair);fb.hidden=false;
   msg.textContent='已确认 '+String.fromCharCode(65+chosen)+'，下方显示判断理由。';fb.scrollIntoView({block:'nearest',behavior:'auto'});
  });
 });
 root.querySelectorAll('.lab').forEach(lab=>{
  const sc=lab.closest('.scene'),svg=sc.querySelector('svg'),out=lab.querySelector('output');
  function update(){
   if(lab.dataset.lab==='measurement'){
    const bias=+lab.querySelector('[data-param=bias]').value,spread=+lab.querySelector('[data-param=spread]').value;
    svg.querySelectorAll('[data-offset]').forEach(c=>c.setAttribute('cx',220+(bias+(+c.dataset.offset)*spread/.2)*40));
    out.textContent='平均值 '+(100+bias).toFixed(1)+' g　读数范围 '+(2*spread).toFixed(1)+' g';
   }else{
    const angle=+lab.querySelector('[data-param=angle]').value,a=angle*Math.PI/180,ux=Math.cos(a),uy=-Math.sin(a),ox=112,oy=180,px=395,py=180;
    const dot=(ox-px)*ux,hx=px+dot*ux,hy=py+dot*uy,ex=px+135*ux,ey=py+135*uy,group=svg.querySelector('[data-rotating-force]');
    const line=(x,y,u,v,c,w=3,extra='')=>`<path d="M${x} ${y}L${u} ${v}" fill="none" stroke="var(--${c})" stroke-width="${w}" ${extra}/>`;
    const marker=`<path d="M${ex} ${ey}l${-14*ux-6*uy} ${-14*uy+6*ux}l${12*uy} ${-12*ux}Z" fill="var(--blue)"/>`;
    const fAudio=group.querySelector('[data-audio]')?.dataset.audio||'';
    group.innerHTML='<defs><clipPath id="plotclip"><rect x="60" y="60" width="530" height="260"/></clipPath></defs>'+line(px,py,ex,ey,'blue',5)+marker+`<g clip-path="url(#plotclip)">`+line(px-360*ux,py-360*uy,px+160*ux,py+160*uy,'blue',2,'stroke-dasharray="6 6"')+'</g>'+line(px,py,px+70,py,'muted',1,'stroke-dasharray="4 4"')+(angle>2?`<path d="M${px+52} ${py}A52 52 0 0 0 ${px+52*ux} ${py+52*uy}" fill="none" stroke="var(--muted)" stroke-width="2"/><text x="${px+75}" y="${py-8}" fill="var(--muted)" font-size="24">${angle}°</text>`:'')+line(ox,oy,hx,hy,'orange',5)+(angle>2?`<path d="M${hx-12*ux} ${hy-12*uy}l${-12*uy} ${12*ux}l${12*ux} ${12*uy}" fill="none" stroke="var(--orange)" stroke-width="2"/>`:'')+`<g data-audio="${fAudio}" role="button" tabindex="0"><text x="${px+100*ux+18}" y="${py+100*uy-14}" fill="var(--blue)" font-size="24">F = 5 N ◖))</text></g><text x="${(ox+hx)/2-14}" y="${(oy+hy)/2-18}" fill="var(--orange)" font-size="27">d</text>`;
    out.textContent='夹角 '+angle+'°　d = '+(2*Math.sin(a)).toFixed(2)+' m　moment = '+(10*Math.sin(a)).toFixed(2)+' N m';
   }
  }
  lab.querySelectorAll('input').forEach(e=>on(e,'input',()=>{stop();update()}));
  lab.querySelectorAll('[data-preset]').forEach(e=>on(e,'click',()=>{
   stop();let p=e.dataset.preset;
   if(lab.dataset.lab==='measurement'){
    if(p==='bias')lab.querySelector('[data-param=bias]').value=0;
    if(p==='spread')lab.querySelector('[data-param=spread]').value=2;
    if(p==='reset'){lab.querySelector('[data-param=bias]').value=6;lab.querySelector('[data-param=spread]').value=.2;}
   }else lab.querySelector('[data-param=angle]').value=p;
   update();
  }));update();
 });

window.ccptCleanup=cleanup;let start=0;try{if(root.dataset.side==='back'&&sessionStorage.getItem('ccpt-test-'+root.dataset.note)){sessionStorage.removeItem('ccpt-test-'+root.dataset.note);start=scenes.findIndex(s=>s.querySelector('.quiz'));}}catch(e){}stage(start<0?0:start);root.classList.add('ready');
};window.ccptInit();
