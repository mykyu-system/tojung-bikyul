(function(root,factory){
'use strict';
const api=factory();
if(typeof module==='object'&&module.exports)module.exports=api;
if(root)root.TojungReadingArt=api;
})(typeof globalThis!=='undefined'?globalThis:this,function(){
'use strict';

const THEMES=[
  {name:'Dawn',skyTop:'#ead4c5',skyBottom:'#fbf2df',far:'#c8b69b',mid:'#899788',near:'#4e665b',water:'#9cb8b0',accent:'#bd6349',gold:'#b98b48',mist:'#fff8e9',ink:'#2d2940'},
  {name:'Spring',skyTop:'#dbe7dd',skyBottom:'#f7f1dd',far:'#b9bea2',mid:'#84977d',near:'#496354',water:'#8faeaa',accent:'#b96d62',gold:'#b48a47',mist:'#fffced',ink:'#292d3d'},
  {name:'Clear Sky',skyTop:'#d8e4e6',skyBottom:'#f8edda',far:'#b7b5a0',mid:'#7d9188',near:'#445f59',water:'#85aaa9',accent:'#bd7650',gold:'#bc914c',mist:'#fff9e8',ink:'#282c40'},
  {name:'Sunset',skyTop:'#d8b8b4',skyBottom:'#f3dfc9',far:'#b49d92',mid:'#7f8179',near:'#4c5a55',water:'#819b9a',accent:'#b65647',gold:'#c08b46',mist:'#f9ead8',ink:'#30283b'},
  {name:'Moonlight',skyTop:'#45445d',skyBottom:'#aaa3a5',far:'#85858d',mid:'#65736f',near:'#303e3c',water:'#647f83',accent:'#b97868',gold:'#d0b274',mist:'#e7e3d8',ink:'#242335'},
  {name:'Mist',skyTop:'#dfddd5',skyBottom:'#f4eddf',far:'#c4bdad',mid:'#93998c',near:'#56675e',water:'#9aacab',accent:'#a96758',gold:'#b59a68',mist:'#fffdf2',ink:'#343142'}
];
const UPPER_NAMES=['Heaven','Lake','Fire','Thunder','Wind','Water','Mountain','Earth'];
const LOWER_NAMES=['Stone Path','Moon Bridge','Flowering Branch'];

function whole(value,min,max){
  const number=Math.trunc(Number(value));
  return Number.isFinite(number)&&number>=min&&number<=max?number:min;
}

function atmosphere(index,c,mood){
  const glow=(.62+mood*.3).toFixed(2);
  switch(index){
    case 1:return `<circle cx="258" cy="38" r="18" fill="${c.accent}" opacity="${glow}"/><circle cx="258" cy="38" r="25" fill="none" stroke="${c.gold}" stroke-width="1" opacity=".28"/><path d="M34 49c18-13 36-11 50 1 14-13 35-14 52 2M184 66c13-10 28-9 39 1 11-9 25-9 36 1" fill="none" stroke="${c.mist}" stroke-width="7" stroke-linecap="round" opacity=".72"/>`;
    case 2:return `<circle cx="70" cy="34" r="15" fill="${c.gold}" opacity="${glow}"/><path d="M20 67c20-15 43-13 57 2 16-14 37-14 52 1M210 45c12-9 26-8 36 1 10-8 22-8 31 0" fill="none" stroke="${c.mist}" stroke-width="8" stroke-linecap="round" opacity=".7"/><path d="M70 11v9M47 20l7 7M93 20l-7 7" stroke="${c.gold}" stroke-width="1.5" stroke-linecap="round" opacity=".55"/>`;
    case 3:return `<circle cx="160" cy="31" r="22" fill="${c.mist}" opacity=".42"/><circle cx="160" cy="31" r="12" fill="${c.gold}" opacity="${glow}"/><path d="M60 43q7-8 14 0q7-8 14 0M240 56q6-7 12 0q6-7 12 0" fill="none" stroke="${c.ink}" stroke-width="1.5" stroke-linecap="round" opacity=".62"/>`;
    case 4:return `<circle cx="258" cy="101" r="23" fill="${c.accent}" opacity="${glow}"/><path d="M20 45c25-10 47-8 67 4M103 61c28-12 59-10 82 3M214 40c20-8 39-6 55 3" fill="none" stroke="${c.mist}" stroke-width="6" stroke-linecap="round" opacity=".48"/>`;
    case 5:return `<path d="M260 19a18 18 0 1 0 15 28 15 15 0 1 1-15-28Z" fill="${c.mist}" opacity="${glow}"/><g fill="${c.gold}" opacity=".72"><circle cx="52" cy="29" r="1.5"/><circle cx="98" cy="47" r="1.2"/><circle cx="181" cy="24" r="1.4"/><circle cx="225" cy="57" r="1.1"/></g><path d="M26 69c20-10 39-8 55 2M154 64c19-10 39-9 55 1" fill="none" stroke="${c.mist}" stroke-width="6" stroke-linecap="round" opacity=".28"/>`;
    default:return `<circle cx="247" cy="42" r="19" fill="${c.mist}" opacity=".48"/><path d="M8 45c45 16 88 14 131 1s88-14 173 5M-4 75c50 13 97 10 140-2 48-14 105-11 188 5M18 101c46 10 96 7 142-4 50-12 95-8 147 5" fill="none" stroke="${c.mist}" stroke-width="11" stroke-linecap="round" opacity=".55"/>`;
  }
}

function upperScene(index,c){
  switch(index){
    case 1:return `<path d="M0 133C35 111 61 114 88 124c28-31 57-45 92-10 31-25 66-21 90 7 20-8 35-6 50 2v53H0Z" fill="${c.far}" opacity=".55"/><path d="M-8 139c29-9 54-7 73 5 18-16 43-18 66-4 21-20 52-24 79-7 23-14 54-12 84 7 13-5 23-6 34-3" fill="none" stroke="${c.mist}" stroke-width="15" stroke-linecap="round" opacity=".55"/><path d="M75 84q8-9 16 0q8-9 16 0M202 76q7-8 14 0q7-8 14 0" fill="none" stroke="${c.ink}" stroke-width="2" stroke-linecap="round" opacity=".72"/>`;
    case 2:return `<path d="M0 97Q72 86 141 98t179-2v80H0Z" fill="${c.water}" opacity=".72"/><path d="M0 111q48-9 96 0t96 0 128 0M7 128q54-7 105 1t102-1 102 1" fill="none" stroke="${c.mist}" stroke-width="2" opacity=".5"/><g stroke="${c.near}" stroke-width="2" stroke-linecap="round" opacity=".82"><path d="M53 142V98m11 42v-35m196 37V93m-12 47v-29"/><path d="M53 106l-7-13m8 8 9-15m197 18-7-16m7 9 10-13"/></g><g fill="${c.accent}" opacity=".78"><circle cx="105" cy="117" r="5"/><circle cx="219" cy="128" r="4"/></g><path d="M90 122q15-11 31 0M203 133q15-10 31 0" fill="${c.mid}" opacity=".74"/>`;
    case 3:return `<path d="M0 142 47 111l35 18 48-67 39 51 34-29 50 53 29-18 38 23v34H0Z" fill="${c.mid}" opacity=".69"/><path d="M110 119c18-21 10-35 24-53 3 17 15 22 12 41 11-9 14-20 15-32 17 24 25 45 5 62M212 128c12-13 9-24 17-36 2 11 9 16 8 28" fill="none" stroke="${c.accent}" stroke-width="5" stroke-linecap="round" opacity=".78"/><path d="M0 148c58-15 112-11 158 3 51-17 107-17 162-3v28H0Z" fill="${c.near}" opacity=".66"/>`;
    case 4:return `<path d="M0 135 58 112l43 15 51-26 54 26 48-20 66 28v41H0Z" fill="${c.mid}" opacity=".64"/><path d="M48 54c18-19 45-17 57 1 19-17 49-10 55 12 24-9 47 3 51 24H37c-6-15-1-28 11-37Z" fill="${c.ink}" opacity=".67"/><path d="m137 83-15 25h13l-12 25 31-35h-14l13-15Z" fill="${c.gold}" opacity=".88"/><g stroke="${c.mist}" stroke-width="1.5" opacity=".5"><path d="m66 98-8 17m34-17-8 19m92-17-8 17m29-19-8 18"/></g>`;
    case 5:return `<path d="M0 146c50-21 102-19 151-2 57-20 114-19 169 1v31H0Z" fill="${c.mid}" opacity=".54"/><g stroke="${c.near}" stroke-linecap="round"><path d="M61 160 76 72M92 164 98 82M247 164l-8-84" stroke-width="5"/><path d="m70 103-18-9m20-8 18-12m5 39-17-8m21-4 18-13m125 18-19-11m18-7 16-14" stroke-width="2.5"/></g><g fill="${c.near}" opacity=".86"><ellipse cx="52" cy="94" rx="12" ry="4" transform="rotate(24 52 94)"/><ellipse cx="89" cy="75" rx="13" ry="4" transform="rotate(-31 89 75)"/><ellipse cx="78" cy="105" rx="11" ry="4" transform="rotate(25 78 105)"/><ellipse cx="116" cy="87" rx="13" ry="4" transform="rotate(-28 116 87)"/><ellipse cx="222" cy="105" rx="13" ry="4" transform="rotate(25 222 105)"/><ellipse cx="257" cy="91" rx="12" ry="4" transform="rotate(-29 257 91)"/></g><path d="M20 72c46 18 85 14 119-1M164 87c41 16 84 12 124-5" fill="none" stroke="${c.gold}" stroke-width="1.5" stroke-linecap="round" opacity=".55"/>`;
    case 6:return `<path d="M0 91Q43 75 81 94t83 0 82 0 74-1v83H0Z" fill="${c.water}" opacity=".76"/><g fill="none" stroke-linecap="round"><path d="M-4 111q22-21 44 0t44 0 44 0 44 0 44 0 44 0 44 0 44 0" stroke="${c.mist}" stroke-width="4" opacity=".72"/><path d="M-8 132q18-18 36 0t36 0 36 0 36 0 36 0 36 0 36 0 36 0" stroke="${c.ink}" stroke-width="2" opacity=".5"/><path d="M5 151q25-12 50 0t50 0 50 0 50 0 50 0 50 0" stroke="${c.gold}" stroke-width="1.5" opacity=".55"/></g><g fill="${c.accent}" opacity=".72"><ellipse cx="91" cy="124" rx="12" ry="5" transform="rotate(-8 91 124)"/><path d="m79 124-10-7v14Z"/><ellipse cx="230" cy="146" rx="10" ry="4" transform="rotate(8 230 146)"/><path d="m240 146 9-6v12Z"/></g>`;
    case 7:return `<path d="M0 147 58 93l34 28 69-79 50 83 37-42 72 67v26H0Z" fill="${c.far}" opacity=".67"/><path d="m58 93 21 17 13 11 69-79 13 31 37 52 37-42 20 30" fill="none" stroke="${c.mist}" stroke-width="5" stroke-linejoin="round" opacity=".48"/><path d="M0 155c59-24 105-18 151 1 53-22 109-21 169-2v22H0Z" fill="${c.near}" opacity=".74"/><g stroke="${c.ink}" stroke-linecap="round" opacity=".78"><path d="M257 148v-43" stroke-width="3"/><path d="m257 111-17 10m18-2 19 10m-20-3-13 13" stroke-width="2"/></g><g fill="${c.near}"><ellipse cx="238" cy="119" rx="13" ry="5" transform="rotate(-25 238 119)"/><ellipse cx="276" cy="127" rx="14" ry="5" transform="rotate(28 276 127)"/><ellipse cx="243" cy="137" rx="12" ry="5" transform="rotate(-20 243 137)"/></g>`;
    default:return `<path d="M0 113c44-25 88-24 132 0 42-31 93-30 139 0 17-7 33-6 49 1v62H0Z" fill="${c.mid}" opacity=".61"/><path d="M0 139c55-17 104-14 153 1 54-19 108-18 167 0v36H0Z" fill="${c.near}" opacity=".58"/><g fill="none" stroke="${c.gold}" stroke-width="1.4" opacity=".61"><path d="M13 151c47-11 94-8 140 1m15 0c49-12 96-11 141 0"/><path d="M46 129v42m52-49v51m121-49v49m48-44v42"/></g><g fill="${c.accent}" opacity=".74"><circle cx="37" cy="121" r="3"/><circle cx="111" cy="135" r="3"/><circle cx="205" cy="119" r="3"/><circle cx="282" cy="132" r="3"/></g>`;
  }
}

function foreground(index,c){
  switch(index){
    case 1:return `<g fill="${c.mist}" stroke="${c.gold}" stroke-width="1" opacity=".86"><ellipse cx="160" cy="164" rx="30" ry="8"/><ellipse cx="148" cy="148" rx="22" ry="6"/><ellipse cx="160" cy="135" rx="15" ry="4.5"/><ellipse cx="153" cy="124" rx="10" ry="3.5"/></g>`;
    case 2:return `<path d="M69 163Q160 92 251 163" fill="none" stroke="${c.ink}" stroke-width="10" stroke-linecap="round" opacity=".9"/><path d="M76 158Q160 105 244 158" fill="none" stroke="${c.gold}" stroke-width="2" opacity=".82"/><path d="M84 145v19m34-42v25m84-25v25m34-2v19" stroke="${c.ink}" stroke-width="2" opacity=".76"/>`;
    default:return `<path d="M326 175c-35-19-45-48-79-63-23-11-42-10-65-25" fill="none" stroke="${c.ink}" stroke-width="7" stroke-linecap="round" opacity=".88"/><path d="M272 128c-5-20-2-37 10-52M239 111c-15-12-29-17-45-16" fill="none" stroke="${c.ink}" stroke-width="3" stroke-linecap="round" opacity=".76"/><g fill="${c.accent}" stroke="${c.mist}" stroke-width="1" opacity=".92"><circle cx="281" cy="82" r="7"/><circle cx="264" cy="103" r="6"/><circle cx="225" cy="101" r="6"/><circle cx="198" cy="94" r="5"/><circle cx="291" cy="117" r="5"/></g><g fill="${c.gold}" opacity=".8"><circle cx="281" cy="82" r="2"/><circle cx="264" cy="103" r="2"/><circle cx="225" cy="101" r="2"/><circle cx="198" cy="94" r="1.7"/><circle cx="291" cy="117" r="1.7"/></g>`;
  }
}

function render(options){
  const input=options||{},upper=whole(input.upper,1,8),middle=whole(input.middle,1,6),lower=whole(input.lower,1,3),score=Math.max(0,Math.min(100,Number(input.score)||70));
  const c=THEMES[middle-1],code=`${upper}-${middle}-${lower}`,id=`ra${upper}${middle}${lower}`,seed=upper*100+middle*10+lower,mood=Math.max(.35,Math.min(1,score/90)),veil=(.24-mood*.14).toFixed(2);
  return `<svg class="reading-art-svg" viewBox="0 0 320 176" preserveAspectRatio="xMidYMid meet" aria-hidden="true" focusable="false" data-reading-code="${code}" data-scene="${UPPER_NAMES[upper-1]}" data-atmosphere="${c.name}" data-foreground="${LOWER_NAMES[lower-1]}" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="${id}sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${c.skyTop}"/><stop offset="1" stop-color="${c.skyBottom}"/></linearGradient><clipPath id="${id}clip"><rect x="1" y="1" width="318" height="174" rx="18"/></clipPath><filter id="${id}grain" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".72" numOctaves="2" seed="${seed}"/><feColorMatrix values="0 0 0 0 .42 0 0 0 0 .34 0 0 0 0 .28 0 0 0 .14 0"/></filter></defs><g clip-path="url(#${id}clip)"><rect width="320" height="176" fill="url(#${id}sky)"/>${atmosphere(middle,c,mood)}${upperScene(upper,c)}${foreground(lower,c)}<rect width="320" height="176" fill="${c.ink}" opacity="${veil}"/><rect width="320" height="176" filter="url(#${id}grain)" opacity=".18"/></g><rect x="1" y="1" width="318" height="174" rx="18" fill="none" stroke="${c.gold}" stroke-width="1.25" opacity=".56"/></svg>`;
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
