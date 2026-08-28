from pathlib import Path

# Fix nested iframe height feedback so the page can shrink as well as grow.
p = Path('english-v4.html')
s = p.read_text(encoding='utf-8')
s = s.replace("#shell{display:block;width:100%;height:1900px;min-height:100vh;border:0;background:transparent}", "#shell{display:block;width:100%;height:620px;min-height:0;border:0;background:transparent}")
old = '''function syncHeight(){
  try{
    const outer=shell.contentDocument;
    if(!outer)return;
    const app=outer.getElementById('app');
    const inner=app&&app.contentDocument;
    const h1=Math.max(0,outer.body?.scrollHeight||0,outer.documentElement?.scrollHeight||0);
    const h2=inner?Math.max(inner.body?.scrollHeight||0,inner.documentElement?.scrollHeight||0):0;
    const h=Math.max(620,h1,h2+12);
    const finalH=Math.min(14000,h);
    shell.style.height=finalH+'px';
    if(app&&h2)app.style.height=Math.min(14000,h2+4)+'px';
    try{parent.postMessage({type:'TOJEONG_EMBED_HEIGHT',height:finalH},'*')}catch(e){}
  }catch(e){}
}
'''
new = '''function syncHeight(){
  try{
    const outer=shell.contentDocument;
    if(!outer)return;
    const app=outer.getElementById('app');
    const inner=app&&app.contentDocument;
    const h2=inner?Math.max(inner.body?.scrollHeight||0,inner.documentElement?.scrollHeight||0):0;
    if(!h2)return;
    const appH=Math.min(14000,Math.max(600,h2+4));
    const finalH=Math.min(14000,Math.max(620,h2+12));
    if(app)app.style.height=appH+'px';
    shell.style.height=finalH+'px';
    try{parent.postMessage({type:'TOJEONG_EMBED_HEIGHT',height:finalH},'*')}catch(e){}
  }catch(e){}
}
'''
if old not in s:
    raise SystemExit('syncHeight block not found')
s = s.replace(old,new)
p.write_text(s,encoding='utf-8')

# Reduce the intermediate wrapper's initial fixed height too.
p = Path('english-v2.html')
s = p.read_text(encoding='utf-8')
s = s.replace("iframe{display:block;width:100%;height:1900px;min-height:100vh;border:0;background:#efe5d3}", "iframe{display:block;width:100%;height:620px;min-height:0;border:0;background:#efe5d3}")
p.write_text(s,encoding='utf-8')

# Make the Blogger helper wrappers start compact. They will grow from postMessage only when needed.
for name in ('blogger-english.html','blogger.html'):
    p=Path(name)
    s=p.read_text(encoding='utf-8')
    s=s.replace('height:1400px;min-height:0','height:620px;min-height:0')
    p.write_text(s,encoding='utf-8')
