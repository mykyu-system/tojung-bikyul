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
const THEMES=[
  {name:'Dawn',wash:'#b96752',wash2:'#e8b778',washOpacity:.10,accent:'#bd6349',gold:'#bd9658',mist:'#fff8e9',ink:'#2d2940'},
  {name:'Spring',wash:'#78957c',wash2:'#d8b46d',washOpacity:.09,accent:'#a96762',gold:'#b48a47',mist:'#fffced',ink:'#29363a'},
  {name:'Clear Sky',wash:'#668b9a',wash2:'#f3d9a0',washOpacity:.07,accent:'#b76c4f',gold:'#bc914c',mist:'#fff9e8',ink:'#283142'},
  {name:'Sunset',wash:'#8e5266',wash2:'#d37954',washOpacity:.17,accent:'#b65647',gold:'#c08b46',mist:'#f9ead8',ink:'#30283b'},
  {name:'Moonlight',wash:'#252541',wash2:'#5f617c',washOpacity:.36,accent:'#b97868',gold:'#d0b274',mist:'#eee8d8',ink:'#202033'},
  {name:'Mist',wash:'#f7f1e5',wash2:'#d9d5ca',washOpacity:.21,accent:'#a96758',gold:'#b59a68',mist:'#fffdf2',ink:'#343142'}
];
const LOWER_NAMES=['Stone Path','Moon Bridge','Flowering Branch'];

function whole(value,min,max){
  const number=Math.trunc(Number(value));
  return Number.isFinite(number)&&number>=min&&number<=max?number:min;
}

function atmosphere(index,c,id,mood){
  const glow=(.42+mood*.28).toFixed(2);
  const wash=(c.washOpacity+(1-mood)*.045).toFixed(2);
  const base=`<rect width="320" height="176" fill="url(#${id}wash)" opacity="${wash}" style="mix-blend-mode:multiply"/>`;
  switch(index){
    case 1:return `${base}<path d="M24 47c20-11 41-9 57 2 17-12 38-12 55 1M205 56c14-8 29-7 41 2" fill="none" stroke="${c.mist}" stroke-width="6" stroke-linecap="round" opacity=".36"/><circle cx="275" cy="31" r="20" fill="none" stroke="${c.gold}" stroke-width="1.2" opacity="${(.12+mood*.12).toFixed(2)}"/>`;
    case 2:return `${base}<path d="M17 72c36-17 72-12 103 2M203 46c27-12 56-10 88 3" fill="none" stroke="${c.mist}" stroke-width="7" stroke-linecap="round" opacity=".28"/><g fill="${c.gold}" opacity="${glow}"><ellipse cx="53" cy="43" rx="4" ry="1.4" transform="rotate(-26 53 43)"/><ellipse cx="66" cy="37" rx="4" ry="1.4" transform="rotate(24 66 37)"/><ellipse cx="282" cy="68" rx="3.5" ry="1.2" transform="rotate(-18 282 68)"/></g>`;
    case 3:return `${base}<path d="M61 39q6-7 12 0q6-7 12 0M238 50q6-7 12 0q6-7 12 0" fill="none" stroke="${c.ink}" stroke-width="1.4" stroke-linecap="round" opacity=".55"/><path d="M12 113c70-13 127-9 181 2 42 9 81 8 121-1" fill="none" stroke="${c.mist}" stroke-width="5" opacity=".22"/>`;
    case 4:return `${base}<rect y="102" width="320" height="74" fill="${c.accent}" opacity=".07"/><path d="M21 39c30-10 56-7 80 3M119 54c35-12 70-9 101 3M241 40c19-7 36-5 52 2" fill="none" stroke="${c.mist}" stroke-width="5" stroke-linecap="round" opacity=".30"/>`;
    case 5:return `${base}<rect width="320" height="176" fill="${c.ink}" opacity="${(.08+(1-mood)*.05).toFixed(2)}"/><path d="M270 19a18 18 0 1 0 15 28 15 15 0 1 1-15-28Z" fill="${c.mist}" opacity="${glow}"/><g fill="${c.gold}" opacity=".64"><circle cx="53" cy="29" r="1.4"/><circle cx="111" cy="45" r="1.1"/><circle cx="189" cy="25" r="1.3"/><circle cx="232" cy="58" r="1"/></g>`;
    default:return `${base}<path d="M-5 42c50 15 96 13 139 1 47-13 103-11 190 5M-4 77c56 13 104 9 148-3 49-14 103-10 180 5M8 111c50 10 101 6 149-4 54-11 103-6 161 6" fill="none" stroke="${c.mist}" stroke-width="12" stroke-linecap="round" opacity=".46"/>`;
  }
}

function foreground(index,c){
  switch(index){
    case 1:return `<g fill="${c.mist}" stroke="${c.gold}" stroke-width="1" opacity=".66"><ellipse cx="160" cy="166" rx="27" ry="6.5"/><ellipse cx="150" cy="152" rx="19" ry="5"/><ellipse cx="160" cy="140" rx="13" ry="3.8"/><ellipse cx="154" cy="130" rx="8" ry="2.8"/></g>`;
    case 2:return `<path d="M72 168Q160 111 248 168" fill="none" stroke="${c.ink}" stroke-width="7" stroke-linecap="round" opacity=".68"/><path d="M79 164Q160 121 241 164" fill="none" stroke="${c.gold}" stroke-width="1.5" opacity=".78"/><path d="M91 151v18m32-37v22m74-22v22m32-3v18" stroke="${c.ink}" stroke-width="1.5" opacity=".52"/>`;
    default:return `<path d="M324 176c-31-17-43-42-74-55-20-9-38-9-59-23" fill="none" stroke="${c.ink}" stroke-width="5" stroke-linecap="round" opacity=".68"/><path d="M270 132c-4-16-1-29 9-41M242 120c-13-10-25-14-39-13" fill="none" stroke="${c.ink}" stroke-width="2.2" stroke-linecap="round" opacity=".60"/><g fill="${c.accent}" stroke="${c.mist}" stroke-width=".8" opacity=".78"><circle cx="279" cy="96" r="5.5"/><circle cx="263" cy="115" r="5"/><circle cx="229" cy="112" r="4.8"/><circle cx="204" cy="106" r="4"/><circle cx="288" cy="128" r="4"/></g><g fill="${c.gold}" opacity=".75"><circle cx="279" cy="96" r="1.5"/><circle cx="263" cy="115" r="1.4"/><circle cx="229" cy="112" r="1.3"/><circle cx="204" cy="106" r="1.2"/><circle cx="288" cy="128" r="1.2"/></g>`;
  }
}

function render(options){
  const input=options||{},upper=whole(input.upper,1,8),middle=whole(input.middle,1,6),lower=whole(input.lower,1,3),score=Math.max(0,Math.min(100,Number(input.score)||70));
  const scene=SCENES[upper-1],c=THEMES[middle-1],code=`${upper}-${middle}-${lower}`,id=`ra${upper}${middle}${lower}`,mood=Math.max(.35,Math.min(1,score/90));
  const lowVeil=Math.max(0,(68-score)/310).toFixed(3),highGlow=Math.max(0,(score-78)/420).toFixed(3);
  return `<svg class="reading-art-svg" viewBox="0 0 320 176" preserveAspectRatio="xMidYMid meet" aria-hidden="true" focusable="false" data-reading-code="${code}" data-scene="${scene.name}" data-atmosphere="${c.name}" data-foreground="${LOWER_NAMES[lower-1]}" data-source="canva" data-canva-design="${scene.design}" xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="${id}clip"><rect x="1" y="1" width="318" height="174" rx="18"/></clipPath><linearGradient id="${id}wash" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${c.wash}"/><stop offset="1" stop-color="${c.wash2}"/></linearGradient><radialGradient id="${id}glow" cx="50%" cy="45%" r="72%"><stop offset="0" stop-color="${c.gold}" stop-opacity="${highGlow}"/><stop offset="1" stop-color="${c.ink}" stop-opacity="${lowVeil}"/></radialGradient></defs><g clip-path="url(#${id}clip)"><image href="./assets/reading-scenes-20260831/${scene.file}?v=1" x="0" y="0" width="320" height="176" preserveAspectRatio="xMidYMid slice"/>${atmosphere(middle,c,id,mood)}<rect width="320" height="176" fill="url(#${id}glow)"/>${foreground(lower,c)}</g><rect x="1" y="1" width="318" height="174" rx="18" fill="none" stroke="${c.gold}" stroke-width="1.15" opacity=".50"/></svg>`;
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
