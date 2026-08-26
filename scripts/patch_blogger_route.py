from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = 'BLOGGER_ROUTE_PATCH'
if marker not in s:
    patch = """<script>/* BLOGGER_ROUTE_PATCH */(function(){try{var q=new URLSearchParams(location.search);if(q.get('blogger')==='1'){location.replace('./english.html?v=blogger-live-'+Date.now());}}catch(e){}})();</script>"""
    if '<head>' not in s:
        raise SystemExit('index.html head marker not found')
    s = s.replace('<head>', '<head>' + patch, 1)
    p.write_text(s, encoding='utf-8')
    print('Legacy Blogger index route redirected to current English app.')
else:
    print('Blogger route patch already present.')
