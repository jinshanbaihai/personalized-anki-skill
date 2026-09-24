(function(){
 if(window.ccptCleanup)window.ccptCleanup();
 const root=document.querySelector('.ccptv4');if(!root)return;
 let player=null,disposed=false;
 const button=root.querySelector('button[data-audio]'),status=root.querySelector('.audio-status');
 function label(text,pressed=false){button.textContent=text;button.setAttribute('aria-pressed',String(pressed));button.setAttribute('aria-label',text+'本页讲解');}
 function stop(){keyboard.abort();disposed=true;if(player){player.pause();player.removeAttribute('src');player.load();player=null;}label('▶');}
 window.ccptCleanup=stop;
 const keyboard=new AbortController();
 button.title='J：播音 / 暂停 / 继续';button.setAttribute('aria-keyshortcuts','J');
 document.addEventListener('keydown',e=>{
  const t=e.target;
  if(root.closest('[data-ccpt-single]')||e.repeat||e.isComposing||e.ctrlKey||e.metaKey||e.altKey||e.shiftKey||t?.isContentEditable||/^(INPUT|TEXTAREA|SELECT)$/.test(t?.tagName||''))return;
  if(e.code==='KeyJ'||e.key.toLowerCase()==='j'){e.preventDefault();e.stopPropagation();button.click();}
 },{capture:true,signal:keyboard.signal});

 button.addEventListener('click',e=>{
  e.preventDefault();e.stopPropagation();
  if(!player){player=new Audio(button.dataset.audio);player.playbackRate=1;player.onended=()=>{label('↻');status.textContent='本页讲解结束 · 点击重播';};player.onerror=()=>{label('▶');status.textContent='音频暂时无法播放';};}
  if(player.ended)player.currentTime=0;
  if(!player.paused){player.pause();label('▶');status.textContent='已暂停 · 点击继续';return;}
  player.play().then(()=>{if(!disposed){label('Ⅱ',true);status.textContent='整页讲解 · 1.5× · 点击暂停';}}).catch(()=>{if(!disposed){label('▶');status.textContent='音频暂时无法播放';}});
 });
 document.addEventListener('visibilitychange',()=>{if(document.hidden&&player){player.pause();label('▶');status.textContent='已暂停 · 点击继续';}},{signal:keyboard.signal});
 const key='ccpt-v4-choice-'+root.dataset.note;
 function stored(){try{return sessionStorage.getItem(key);}catch(_){return null;}}
 function mark(i){root.querySelectorAll('[data-choice]').forEach(x=>{const yes=x.dataset.choice===String(i);x.setAttribute('aria-checked',String(yes));x.querySelector('.mark').textContent=yes?' ✓':'';});const dest=root.querySelector('.selection');if(dest)dest.textContent=i===null?'':('已选 '+String.fromCharCode(65+Number(i))+' · 可改选，翻面后看理由');}
 if(root.dataset.side==='front'){
  mark(stored());root.querySelectorAll('[data-choice]').forEach(x=>x.addEventListener('click',()=>{try{sessionStorage.setItem(key,x.dataset.choice);}catch(_){}mark(x.dataset.choice);}));
 }else{const i=stored();root.querySelectorAll('[data-feedback]').forEach(x=>{if(i===x.dataset.feedback){const tag=document.createElement('span');tag.textContent=' · 你的选择';x.querySelector('.result-label').append(tag);}});try{sessionStorage.removeItem(key);}catch(_){}}
 function drawMap(){root.querySelectorAll('.mindmap').forEach(map=>{const svg=map.querySelector('.map-lines'),r=map.getBoundingClientRect();svg.setAttribute('viewBox',`0 0 ${r.width} ${r.height}`);svg.innerHTML='';const narrow=false;function connect(a,b,level){const x=a.getBoundingClientRect(),y=b.getBoundingClientRect();let d;if(level>1){const sx=x.left-r.left+12,sy=x.bottom-r.top,ex=y.left-r.left,ey=y.top+y.height/2-r.top;d=`M ${sx} ${sy} V ${ey} H ${ex}`;}else if(narrow){const sx=(level===0?r.left+10:x.left-12)-r.left,sy=(level===0?x.bottom:x.top+x.height/2)-r.top,ex=y.left-r.left,ey=y.top+y.height/2-r.top;d=`M ${sx} ${sy} V ${ey} H ${ex}`;}else{const sx=x.right-r.left,sy=x.top+x.height/2-r.top,ex=y.left-r.left,ey=y.top+y.height/2-r.top,mx=sx+(ex-sx)*.5;d=`M ${sx} ${sy} H ${mx} V ${ey} H ${ex}`;}const path=document.createElementNS('http://www.w3.org/2000/svg','path');path.setAttribute('d',d);svg.appendChild(path);}const top=map.querySelector('.map-root');map.querySelectorAll('.map > .branch').forEach(branch=>{const head=branch.querySelector('.branch-head');connect(top,head,0);function descend(parent,list,depth){if(!list)return;Array.from(list.children).filter(x=>x.classList.contains('leaf')).forEach(leaf=>{const node=leaf.querySelector(':scope > .unit');connect(parent,node,depth);descend(node,leaf.querySelector(':scope > .leaves'),depth+1);});}descend(head,branch.querySelector(':scope > .leaves'),1);});});}
 function fit(){const box=root.querySelector('.canvas-fit'),board=root.querySelector('.board-content');if(!box||!board)return;board.style.transform='none';board.style.left='0px';board.style.top='0px';drawMap();if(box.classList.contains('zoomed'))return;const scale=Math.min(box.clientWidth/board.offsetWidth,box.clientHeight/board.offsetHeight,1);board.style.transform=`scale(${scale})`;board.style.left=((box.clientWidth-board.offsetWidth*scale)/2)+'px';board.style.top=((box.clientHeight-board.offsetHeight*scale)/2)+'px';}
 root.querySelector('[data-view=fit]')?.addEventListener('click',()=>{root.querySelector('.canvas-fit').classList.remove('zoomed');fit();});root.querySelector('[data-view=zoom]')?.addEventListener('click',()=>{root.querySelector('.canvas-fit').classList.add('zoomed');fit();});
 const resize=new ResizeObserver(fit);resize.observe(root);requestAnimationFrame(fit);document.fonts?.ready.then(fit);
const cleanup=window.ccptCleanup;window.ccptCleanup=()=>{cleanup();resize.disconnect();};
 const mo=new MutationObserver(()=>{if(!root.isConnected){stop();resize.disconnect();mo.disconnect();}});mo.observe(document.body,{childList:true,subtree:true});window.addEventListener('pagehide',stop,{once:true});
})();
