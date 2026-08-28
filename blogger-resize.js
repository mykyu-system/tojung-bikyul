(function(){
  'use strict';
  const ORIGIN='https://mykyu-system.github.io';
  const MATCH='mykyu-system.github.io/tojung-bikyul';
  const INITIAL_FALLBACK=window.matchMedia('(max-width:640px)').matches?1180:620;
  const states=new WeakMap();

  function targetFrames(){return Array.from(document.querySelectorAll('iframe[src*="'+MATCH+'"]'))}

  function setFrameHeight(frame,height,mode){
    if(!frame)return;
    const state=states.get(frame)||{result:false};
    if(mode==='result'){
      if(state.result)return;
      state.result=true;
    }else if(state.result){return}
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
      if(!states.has(frame))states.set(frame,{result:false});
      if(!states.get(frame).result)setFrameHeight(frame,INITIAL_FALLBACK,'initial');
    });
  }

  function requestHeights(){
    normalizeExisting();
    targetFrames().forEach(frame=>{try{frame.contentWindow.postMessage({type:'TOJEONG_REQUEST_HEIGHT'},ORIGIN)}catch(e){}});
  }

  window.addEventListener('message',function(e){
    if(e.origin!==ORIGIN||!e.data||e.data.type!=='TOJEONG_BLOGGER_HEIGHT')return;
    const frame=targetFrames().find(f=>f.contentWindow===e.source);
    if(!frame)return;
    if(e.data.mode==='result')setFrameHeight(frame,e.data.height,'result');
  });

  function start(){normalizeExisting();requestHeights();setTimeout(requestHeights,500)}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});else start();
  window.addEventListener('load',requestHeights,{once:true});
})();
