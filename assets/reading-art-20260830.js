(function(root,factory){
'use strict';
const api=factory();
if(typeof module==='object'&&module.exports)module.exports=api;
if(root)root.TojungReadingArt=api;
})(typeof globalThis!=='undefined'?globalThis:this,function(){
'use strict';

const SCENES=[
  {name:'Heaven',file:'heaven.webp',design:'DAHT22zTr08'},
  {name:'Lake',file:'lake.webp',design:'DAHT2y60SRY'},
  {name:'Fire',file:'fire.webp',design:'DAHT2gGWmPY'},
  {name:'Thunder',file:'thunder.webp',design:'DAHT221cCFE'},
  {name:'Wind',file:'wind.webp',design:'DAHT2wAtftc'},
  {name:'Water',file:'water.webp',design:'DAHT22DOeaM'},
  {name:'Mountain',file:'mountain.webp',design:'DAHT20VYU8A'},
  {name:'Earth',file:'earth.webp',design:'DAHT29Vyt4c'}
];
const ATMOSPHERES=[
  {name:'Dawn',start:'#f4cdb0',end:'#d9957f',opacity:.032},
  {name:'Spring',start:'#dbe7cf',end:'#88a58f',opacity:.028},
  {name:'Clear Sky',start:'#e8f1ef',end:'#7e9da9',opacity:.024},
  {name:'Sunset',start:'#f0c3ad',end:'#ad7180',opacity:.040},
  {name:'Moonlight',start:'#7a8398',end:'#343a54',opacity:.052},
  {name:'Mist',start:'#fffdf4',end:'#d8d4c9',opacity:.034}
];
const FINISHES=[
  {name:'Natural',color:'#fffaf0',opacity:.006,edge:'#c4a36b'},
  {name:'Warm Light',color:'#d7a173',opacity:.016,edge:'#c4935e'},
  {name:'Cool Clarity',color:'#78929b',opacity:.014,edge:'#97aaad'}
];

function whole(value,min,max){
  const number=Math.trunc(Number(value));
  return Number.isFinite(number)&&number>=min&&number<=max?number:min;
}

function render(options){
  const input=options||{},upper=whole(input.upper,1,8),middle=whole(input.middle,1,6),lower=whole(input.lower,1,3),score=Math.max(0,Math.min(100,Number(input.score)||70));
  const scene=SCENES[upper-1],atmosphere=ATMOSPHERES[middle-1],finish=FINISHES[lower-1],code=`${upper}-${middle}-${lower}`,id=`ra${upper}${middle}${lower}`;
  const lowVeil=Math.max(0,(68-score)/520).toFixed(3),highGlow=Math.max(0,(score-78)/680).toFixed(3);
  return `<svg class="reading-art-svg" viewBox="0 0 320 176" preserveAspectRatio="xMidYMid meet" aria-hidden="true" focusable="false" data-reading-code="${code}" data-scene="${scene.name}" data-atmosphere="${atmosphere.name}" data-finish="${finish.name}" data-source="canva" data-canva-design="${scene.design}" xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="${id}clip"><rect x="1" y="1" width="318" height="174" rx="18"/></clipPath><linearGradient id="${id}wash" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${atmosphere.start}"/><stop offset="1" stop-color="${atmosphere.end}"/></linearGradient><radialGradient id="${id}tone" cx="50%" cy="45%" r="78%"><stop offset="0" stop-color="#fffdf4" stop-opacity="${highGlow}"/><stop offset="1" stop-color="#202735" stop-opacity="${lowVeil}"/></radialGradient></defs><g clip-path="url(#${id}clip)"><image href="./assets/reading-scenes-20260831/${scene.file}?v=2" x="0" y="0" width="320" height="176" preserveAspectRatio="xMidYMid slice"/><rect width="320" height="176" fill="url(#${id}wash)" opacity="${atmosphere.opacity}"/><rect width="320" height="176" fill="${finish.color}" opacity="${finish.opacity}"/><rect width="320" height="176" fill="url(#${id}tone)"/></g><rect x="1" y="1" width="318" height="174" rx="18" fill="none" stroke="${finish.edge}" stroke-width="1" opacity=".38"/></svg>`;
}

function bind(options){
  const input=options||{},container=input.container,codeElement=input.codeElement,scoreElement=input.scoreElement;
  if(!container||!codeElement)return null;
  const draw=()=>{
    const match=String(codeElement.textContent||'').trim().match(/^(\d+)-(\d+)-(\d+)$/);
    if(!match){container.innerHTML='';return;}
    const scoreMatch=String(scoreElement&&scoreElement.textContent||'').match(/\d+(?:\.\d+)?/);
    container.innerHTML=render({upper:+match[1],middle:+match[2],lower:+match[3],score:scoreMatch?+scoreMatch[0]:70});
  };
  const observer=typeof MutationObserver==='function'?new MutationObserver(draw):null;
  if(observer)observer.observe(codeElement,{childList:true,characterData:true,subtree:true});
  draw();
  return observer;
}

return Object.freeze({render,bind});
});
