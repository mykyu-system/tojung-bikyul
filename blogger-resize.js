(function(){
  'use strict';
  const ORIGIN='https://mykyu-system.github.io';
  const MATCH='mykyu-system.github.io/tojung-bikyul';
  const INITIAL_FALLBACK=760;
  const states=new WeakMap();

  function targetFrames(){
    return Array.from(document.querySelectorAll('iframe[src*="'+MATCH+'"]'));
  }

  function setFrameHeight(frame,height,mode){
    if(!frame)return;
    const state=states.get(frame)||{initial:false,result:false};
    if(mode==='initial'){
      if(state.initial||state.result)return;
      state.initial=true;
    }else if(mode==='result'){
      if(state.result)return;
      state.result=true;
    }
    const h=Math.max(360,Math.min(24000,Math.ceil(Number(height)||INITIAL_FALLBACK)));
    frame.style.setProperty('height',h+'px','important');
    frame.style.setProperty('max-height','none','important');
    frame.style.setProperty('min-height','0','important');
    frame.style.setProperty('overflow','hidden','important');
    frame.setAttribute('height',String(h));
    frame.setAttribute('scrolling','no');
    states.set(frame,state);
  }

  function normalizeExisting(){
    targetFrames().forEach(frame=>{
      if(!states.has(frame)){
        frame.style.setProperty('height',INITIAL_FALLBACK+'px','important');
        frame.style.setProperty('max-height','none','important');
        frame.style.setProperty('min-height','0','important');
        frame.style.setProperty('overflow','hidden','important');
        frame.setAttribute('height',String(INITIAL_FALLBACK));
        frame.setAttribute('scrolling','no');
        states.set(frame,{initial:false,result:false});
      }
    });
  }

  window.addEventListener('message',function(e){
    if(e.origin!==ORIGIN||!e.data||e.data.type!=='TOJEONG_BLOGGER_HEIGHT')return;
    const frame=targetFrames().find(f=>f.contentWindow===e.source);
    if(!frame)return;
    setFrameHeight(frame,e.data.height,e.data.mode==='result'?'result':'initial');
  });

  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',normalizeExisting,{once:true});
  else normalizeExisting();
  window.addEventListener('load',normalizeExisting,{once:true});
})();
