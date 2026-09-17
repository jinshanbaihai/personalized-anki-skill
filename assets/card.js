window.ccptInit=function(){
 if(window.ccptCleanup)window.ccptCleanup();
 const root=document.querySelector('.ccpt');if(!root)return;
 const scenes=[...root.querySelectorAll('.scene')], play=root.querySelector('[data-control=play]'),counter=root.querySelector('.counter'),overlay=root.querySelector('.transcript');
 let at=0,current=null,file='',disposed=false;const aborter=new AbortController(),signal=aborter.signal;
 const on=(e,t,fn)=>e.addEventListener(t,fn,{signal});
 function stop(){if(current){current.pause();current.removeAttribute('src');current.load();current=null;}file='';play.textContent='▶ 听讲 · 1.75×';play.setAttribute('aria-pressed','false');}
 function speak(src){if(!src)return;if(current&&file===src){if(current.paused){current.play().catch(fail);play.textContent='Ⅱ 暂停';play.setAttribute('aria-pressed','true');}else{current.pause();play.textContent='▶ 继续';play.setAttribute('aria-pressed','false');}return;}stop();file=src;current=new Audio(src);current.playbackRate=1;current.onended=()=>{play.textContent='↻ 再听一遍';play.setAttribute('aria-pressed','false');};current.onerror=fail;current.play().catch(fail);play.textContent='Ⅱ 暂停';play.setAttribute('aria-pressed','true');}
 function fail(){if(disposed)return;stop();play.textContent='语音未就绪';play.classList.add('audio-error');play.title='可以打开文字说明；请检查媒体文件是否完成同步。';}
 function stage(n){stop();at=Math.max(0,Math.min(scenes.length-1,n));scenes.forEach((s,i)=>s.classList.toggle('active',i===at));counter.textContent=(at+1)+' / '+scenes.length;root.querySelector('[data-control=prev]').disabled=at===0;root.querySelector('[data-control=next]').disabled=at===scenes.length-1;overlay.hidden=true;root.querySelector('[data-control=text]').setAttribute('aria-expanded','false');}
 on(play,'click',()=>speak(scenes[at].dataset.audio));
 on(root.querySelector('[data-control=prev]'),'click',()=>stage(at-1));on(root.querySelector('[data-control=next]'),'click',()=>stage(at+1));
 on(root.querySelector('[data-control=text]'),'click',e=>{stop();overlay.hidden=!overlay.hidden;e.currentTarget.setAttribute('aria-expanded',String(!overlay.hidden));overlay.querySelector('.narration').textContent=scenes[at].dataset.narration;});
 root.querySelectorAll('[data-audio]').forEach(e=>{if(e.classList.contains('scene'))return;on(e,'click',ev=>{ev.stopPropagation();speak(e.dataset.audio);});on(e,'keydown',ev=>{if(ev.key==='Enter'||ev.key===' '){ev.preventDefault();ev.stopPropagation();speak(e.dataset.audio);}});});
 const choiceKey='ccpt-choice:'+root.dataset.note;
 let selected=null;try{selected=sessionStorage.getItem(choiceKey);}catch(_){}
 function paint(){root.querySelectorAll('[data-choice]').forEach(e=>{const v=e.dataset.choice;e.setAttribute('aria-pressed',String(v===selected));const letter=e.querySelector('text');if(letter)letter.textContent=v===selected?'✓':'ABCD'[+v];if(root.dataset.side==='back'){e.classList.toggle('correct',v===root.dataset.correct);e.classList.toggle('wrong',v===selected&&v!==root.dataset.correct);}});const status=root.querySelector('.choice-status'),confirm=root.querySelector('[data-control=confirm]');if(status)status.textContent=selected===null?'请选择一个选项':'已选择 '+'ABCD'[+selected];if(confirm)confirm.disabled=selected===null;const result=root.querySelector('.choice-result');if(result){result.hidden=selected===null;result.textContent=selected===root.dataset.correct?'✓ 选择正确 · '+'ABCD'[+selected]:'你的选择：'+'ABCD'[+selected]+' · 正确选项：'+'ABCD'[+root.dataset.correct];}}
 const confirm=root.querySelector('[data-control=confirm]');if(confirm)on(confirm,'click',()=>{if(selected===null)return;const answer=root.querySelector('template.ccpt-answer');if(!answer)return;const next=answer.content.firstElementChild.cloneNode(true);stop();root.replaceWith(next);window.ccptInit();if(typeof pycmd==='function')pycmd('ans');});
 root.querySelectorAll('[data-choice]').forEach(e=>{const select=()=>{selected=e.dataset.choice;try{sessionStorage.setItem(choiceKey,selected);}catch(_){}paint();};on(e,'click',select);on(e,'keydown',ev=>{if(ev.key==='Enter'||ev.key===' '){ev.preventDefault();ev.stopPropagation();select();}});});
 on(document,'keydown',e=>{if(e.key==='Escape'){stop();overlay.hidden=true;}});on(window,'pagehide',stop);on(document,'visibilitychange',()=>{if(document.hidden)stop();});
 const observer=new MutationObserver(()=>{if(!root.isConnected)cleanup();});observer.observe(document.body,{childList:true,subtree:true});
 function cleanup(){disposed=true;stop();observer.disconnect();aborter.abort();}
 window.ccptCleanup=cleanup;stage(0);paint();root.classList.add('ready');
};window.ccptInit();
