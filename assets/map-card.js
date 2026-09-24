(()=>{
 if(window.ccptCleanup)window.ccptCleanup();
 const root=document.querySelector('.ccpt-map');if(!root)return;
 const board=root.querySelector('.map-board'),vp=root.querySelector('.map-viewport'),svg=root.querySelector('.map-edges'),data=JSON.parse(root.querySelector('.map-data').textContent),ctl=new AbortController();
 const nodes=Object.fromEntries([...root.querySelectorAll('[data-node]')].map(n=>[n.dataset.node,n]));
 function fit(){
  const scale=Math.min(1,vp.clientWidth/board.offsetWidth,vp.clientHeight/board.offsetHeight);
  board.style.transform=`scale(${scale})`;board.style.left=Math.max(0,(vp.clientWidth-board.offsetWidth*scale)/2)+'px';board.style.top=Math.max(0,(vp.clientHeight-board.offsetHeight*scale)/2)+'px';
  svg.innerHTML='<defs><marker id="ccptArrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#82a5aa"/></marker></defs>';
  data.edges.forEach(e=>{const a=nodes[e.from],b=nodes[e.to],down=e.direction==='down';let x1=down?a.offsetLeft+a.offsetWidth/2:a.offsetLeft+a.offsetWidth,y1=down?a.offsetTop+a.offsetHeight:a.offsetTop+a.offsetHeight/2,x2=down?b.offsetLeft+b.offsetWidth/2:b.offsetLeft,y2=down?b.offsetTop:b.offsetTop+b.offsetHeight/2,mx=(x1+x2)/2,my=(y1+y2)/2;const path=document.createElementNS('http://www.w3.org/2000/svg','path');path.setAttribute('d',down?`M${x1} ${y1} V${my} H${x2} V${y2}`:`M${x1} ${y1} H${mx} V${y2} H${x2}`);path.setAttribute('fill','none');path.setAttribute('stroke','#82a5aa');path.setAttribute('stroke-width','2');if(e.arrow)path.setAttribute('marker-end','url(#ccptArrow)');const title=document.createElementNS('http://www.w3.org/2000/svg','title');title.textContent=e.meaning;path.append(title);svg.append(path);});
 }
 const ro=new ResizeObserver(fit);ro.observe(vp);document.fonts.ready.then(fit);fit();
 const audio=root.querySelector('audio'),button=root.querySelector('.speak'),status=root.querySelector('.audio-status');
 button.addEventListener('click',async()=>{if(!audio.paused){audio.pause();return;}if(audio.ended)audio.currentTime=0;try{audio.playbackRate=1;await audio.play();}catch(e){status.textContent='语音未能播放，请检查本地音频';}},{signal:ctl.signal});
 audio.addEventListener('play',()=>{button.textContent='Ⅱ';button.setAttribute('aria-pressed','true');status.textContent='整页讲解 · 1.5×';});
 audio.addEventListener('pause',()=>{button.textContent=audio.ended?'↻':'▶';button.setAttribute('aria-pressed','false');status.textContent=audio.ended?'讲解结束 · 可重播':'已暂停 · Space 继续';});
 audio.addEventListener('ended',()=>{button.textContent='↻';status.textContent='讲解结束 · 可重播';});
 window.ccptAudit=()=>{const scale=board.getBoundingClientRect().width/board.offsetWidth,rects=Object.values(nodes).map(n=>({id:n.dataset.node,x:n.offsetLeft,y:n.offsetTop,w:n.offsetWidth,h:n.offsetHeight,font:parseFloat(getComputedStyle(n).fontSize)*scale}));return {viewport:[vp.clientWidth,vp.clientHeight],scale,minFont:Math.min(...rects.map(n=>n.font)),overflow:rects.filter(n=>n.x+n.w>board.offsetWidth+1||n.y+n.h>board.offsetHeight+1),overlaps:rects.flatMap((a,i)=>rects.slice(i+1).filter(b=>a.x<b.x+b.w&&a.x+a.w>b.x&&a.y<b.y+b.h&&a.y+a.h>b.y).map(b=>[a.id,b.id])),buttons:root.querySelectorAll('.speak').length,nodes:rects,math:root.querySelectorAll('math').length,tables:root.querySelectorAll('table').length,figures:root.querySelectorAll('.map-node svg').length};};
 window.ccptCleanup=()=>{audio.pause();audio.currentTime=0;ro.disconnect();ctl.abort();if(window.ccptSingleCleanup)window.ccptSingleCleanup();};
 window.addEventListener('pagehide',window.ccptCleanup,{once:true,signal:ctl.signal});
})();
