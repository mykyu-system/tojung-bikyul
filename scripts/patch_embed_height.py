from pathlib import Path

# 1) Make the production wrapper report its real rendered height to Blogger.
p = Path('english-v4.html')
s = p.read_text(encoding='utf-8')
old = """    const h=Math.max(900,h1,h2+12);\n    shell.style.height=Math.min(14000,h)+'px';\n    if(app&&h2)app.style.height=Math.min(14000,h2+4)+'px';"""
new = """    const h=Math.max(620,h1,h2+12);\n    const finalH=Math.min(14000,h);\n    shell.style.height=finalH+'px';\n    if(app&&h2)app.style.height=Math.min(14000,h2+4)+'px';\n    try{parent.postMessage({type:'TOJEONG_EMBED_HEIGHT',height:finalH},'*')}catch(e){}"""
if old not in s:
    raise SystemExit('syncHeight target not found')
s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')

# 2) Replace the fixed 5200px Blogger iframe with a responsive height listener.
wrapper = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><meta http-equiv="Pragma" content="no-cache"><meta http-equiv="Expires" content="0"><title>Mykyu-system Personal Fortune</title><style>html,body{margin:0;padding:0;background:#fff;overflow-x:hidden}#app{display:block;width:100%;height:1400px;min-height:0;border:0;background:#efe6d8;transition:height .16s ease}</style></head><body><iframe id="app" title="Mykyu-system Personal Fortune" loading="eager" allow="fullscreen"></iframe><script>(function(){const app=document.getElementById('app');app.src='https://mykyu-system.github.io/tojung-bikyul/english.html?v=embed-fit-'+Date.now();window.addEventListener('message',function(e){if(e.origin!=='https://mykyu-system.github.io')return;const d=e.data||{};if(d.type!=='TOJEONG_EMBED_HEIGHT')return;const n=Number(d.height);if(!Number.isFinite(n)||n<300)return;app.style.height=Math.max(620,Math.min(14000,Math.ceil(n+2)))+'px';});})();</script></body></html>'''
for name in ('blogger-english.html','blogger.html'):
    Path(name).write_text(wrapper, encoding='utf-8')

# 3) Bust the production wrapper cache.
e = Path('english.html')
t = e.read_text(encoding='utf-8')
t = t.replace('20260828-luxury3','20260828-luxury4')
e.write_text(t, encoding='utf-8')

print('dynamic embed height patch applied')
