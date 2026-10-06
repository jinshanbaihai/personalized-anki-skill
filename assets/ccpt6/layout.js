/* ccpt-6 mind-map layout. The authored nested list is always a readable outline;
   when the card is wide enough it becomes a left-to-right logic chart. If the full
   depth does not fit, deeper levels stay as indented outlines inside their branch,
   so text never shrinks below its reading size. No libraries, works offline. */
(()=>{
 const VGAP=14,MINGAP=60,RELPAD=26,NODE_MAX=300,INLINE_MAX=430,NARROW=640;
 const maps=new Set();
 function parse(li,depth){
  const node=li.querySelector(':scope>.mm-node'),rel=li.querySelector(':scope>.mm-rel'),ul=li.querySelector(':scope>ul');
  const kids=ul?[...ul.children].filter(c=>c.matches('li.mm-item')).map(c=>parse(c,depth+1)):[];
  return {li,node,rel,ul,kids,depth,kind:li.dataset.kind||'topic'};
 }
 const deepest=t=>t.kids.length?Math.max(...t.kids.map(deepest)):t.depth;
 function restore(state){
  if(!state.canvas)return;
  const back=t=>{if(t.rel)t.li.appendChild(t.rel);t.li.appendChild(t.node);if(t.ul)t.li.appendChild(t.ul);t.kids.forEach(back);};
  back(state.tree);
  state.mm.querySelectorAll('.mm-inline').forEach(u=>u.classList.remove('mm-inline'));
  state.canvas.remove();state.canvas=null;state.list.style.display='';
  state.mm.dataset.applied='outline';state.mm.classList.remove('is-logic');
 }
 function build(state,cutoff){
  const {mm,tree}=state;
  const canvas=document.createElement('div');canvas.className='mm-canvas';
  const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('class','mm-wires');svg.setAttribute('aria-hidden','true');
  canvas.appendChild(svg);mm.appendChild(canvas);state.canvas=canvas;
  const shown=[];
  const visit=t=>{
   const box=document.createElement('div');box.className='mm-box';box.dataset.kind=t.kind;box.dataset.depth=t.depth;
   box.appendChild(t.node);
   const inline=t.depth===cutoff&&t.kids.length;
   if(inline){box.appendChild(t.ul);t.ul.classList.add('mm-inline');box.classList.add('has-inline');box.style.maxWidth=INLINE_MAX+'px';}
   else box.style.maxWidth=NODE_MAX+'px';
   canvas.appendChild(box);t.box=box;
   if(t.rel&&t.depth){const lab=document.createElement('div');lab.className='mm-label';lab.appendChild(t.rel);canvas.appendChild(lab);t.label=lab;}
   t.vis=inline?[]:t.kids;shown.push(t);t.vis.forEach(visit);
  };
  visit(tree);
  state.list.style.display='none';
  const measure=()=>{for(const t of shown){t.w=t.box.offsetWidth;t.h=t.box.offsetHeight;if(t.label){t.lw=t.label.offsetWidth;t.lh=t.label.offsetHeight;}}};
  const sub=t=>{if(!t.vis.length){t.sh=t.h;return t.sh;}t.ch=t.vis.reduce((s,k,i)=>s+sub(k)+(i?VGAP:0),0);t.sh=Math.max(t.h,t.ch);return t.sh;};
  const place=(t,top,x)=>{
   t.x=x;t.y=top+(t.sh-t.h)/2;
   if(!t.vis.length)return;
   t.gap=Math.max(MINGAP,...t.vis.map(k=>(k.lw||0)+RELPAD));
   let y=top+(t.sh-t.ch)/2;
   for(const k of t.vis){place(k,y,x+t.w+t.gap);y+=k.sh+VGAP;}
  };
  measure();sub(tree);place(tree,0,0);
  // Branches that hold an inline outline may use the rest of the row; wider means shorter.
  const avail=state.mm.clientWidth;let widened=false;
  for(const t of shown)if(t.box.classList.contains('has-inline')){const room=Math.floor(avail-t.x-4);if(room>INLINE_MAX){t.box.style.maxWidth=room+'px';widened=true;}}
  if(widened){measure();sub(tree);place(tree,0,0);}
  let width=0;
  for(const t of shown){t.box.style.left=t.x+'px';t.box.style.top=t.y+'px';width=Math.max(width,t.x+t.w);}
  canvas.style.height=tree.sh+'px';canvas.style.width=width+'px';
  svg.setAttribute('width',width);svg.setAttribute('height',tree.sh);svg.setAttribute('viewBox',`0 0 ${width} ${tree.sh}`);
  let wires='<defs><marker id="mmArrow" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L8,4 L0,8 z" class="mm-arrowhead"/></marker></defs>';
  for(const t of shown)for(const k of t.vis){
   const x1=t.x+t.w,y1=t.y+t.h/2,x2=k.x-2,y2=k.y+k.h/2,c=(x2-x1)/2;
   wires+=`<path class="mm-wire" data-kind="${k.kind}" d="M${x1} ${y1} C${x1+c} ${y1}, ${x2-c} ${y2}, ${x2} ${y2}" marker-end="url(#mmArrow)"/>`;
   if(k.label){k.label.style.left=(k.x-k.lw-10)+'px';k.label.style.top=(y2-k.lh-3)+'px';}
  }
  svg.innerHTML=wires;
  mm.dataset.applied=cutoff>=state.depth?'logic':'logic+outline';mm.dataset.cutoff=cutoff;mm.classList.add('is-logic');
  return width;
 }
 function layout(state){
  restore(state);
  state.mm.dataset.applied='outline';
  const want=state.mm.dataset.layout||'auto',avail=state.mm.clientWidth;
  if(want==='outline'||!state.tree.kids.length)return;
  if(want==='auto'&&avail<NARROW)return;
  const outlineHeight=state.list.offsetHeight;
  for(let cutoff=state.depth;cutoff>=1;cutoff--){
   const width=build(state,cutoff);
   if(width<=avail+1){
    // A chart taller than the plain outline no longer gives an overview: keep the outline.
    if(want==='auto'&&state.canvas.offsetHeight>outlineHeight*1.15){restore(state);state.mm.dataset.applied='outline';return;}
    return;
   }
   if(want==='logic'&&cutoff===1)return;
   restore(state);
  }
 }
 window.ccptLayout=(root,signal)=>{
  root.querySelectorAll('.mm').forEach(mm=>{
   const list=mm.querySelector(':scope>.mm-tree');if(!list)return;
   const first=list.querySelector(':scope>li.mm-item');if(!first)return;
   const state={mm,list,tree:parse(first,0),canvas:null};state.depth=deepest(state.tree);maps.add(state);
   let lastWidth=-1,frame=0;
   const run=()=>{cancelAnimationFrame(frame);frame=requestAnimationFrame(()=>{const w=mm.clientWidth;if(w===lastWidth)return;lastWidth=w;layout(state);});};
   const ro=new ResizeObserver(run);ro.observe(mm);state.ro=ro;
   (document.fonts?document.fonts.ready:Promise.resolve()).then(()=>{lastWidth=-1;run();});
   run();
   signal&&signal.addEventListener('abort',()=>{ro.disconnect();cancelAnimationFrame(frame);});
  });
 };
 window.ccptLayoutCleanup=()=>{maps.forEach(s=>{s.ro&&s.ro.disconnect();});maps.clear();};
})();
