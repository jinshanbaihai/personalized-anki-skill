(function(){
 if(window.ccptSingleCleanup)window.ccptSingleCleanup();
 const root=document.querySelector('[data-ccpt-single]');if(!root)return;
 const ctl=new AbortController(),button=root.querySelector('button[data-audio],button[data-control="play"]');
 if(button){button.title='Space：播音 / 暂停 / 继续';button.setAttribute('aria-keyshortcuts','Space');}
 const editable=()=>{const e=document.activeElement;return e?.isContentEditable||/^(INPUT|TEXTAREA|SELECT)$/.test(e?.tagName||'');};
 window.ccptSingleAction=function(action){
  if(editable())return;
  if(action==='audio'){button?.click();return;}
  if((action==='good'||action==='again')&&typeof pycmd==='function')pycmd('ccpt-single:'+action);
 };
 document.addEventListener('keydown',e=>{
  if(e.repeat||e.isComposing||e.ctrlKey||e.metaKey||e.altKey||e.shiftKey||editable())return;
  let action=e.code==='Space'||e.key===' '?'audio':e.key==='Enter'?'good':e.key==='1'?'again':null;
  if(!action)return;e.preventDefault();e.stopImmediatePropagation();window.ccptSingleAction(action);
 },{capture:true,signal:ctl.signal});
 window.ccptSingleCleanup=()=>{ctl.abort();delete window.ccptSingleAction;};
})();
