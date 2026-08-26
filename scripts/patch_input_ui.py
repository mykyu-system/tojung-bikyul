from pathlib import Path

p = Path('english-app4.html')
s = p.read_text(encoding='utf-8')

old = '<aside class="fortune-art" aria-label="Approved Hojakdo visual"></aside>'
new = '<aside class="fortune-art" aria-label="Approved Hojakdo visual"><img class="hojakdo-img" src="https://mykyu-system.github.io/tojung-bikyul/assets/hojakdo-final.webp?v=20260827-imgfix1" alt="Hojakdo tiger and gat-wearing magpie illustration"></aside>'
if old in s:
    s = s.replace(old, new, 1)

if '.hojakdo-img{' not in s:
    s = s.replace('.fortune-art{\n  min-height:760px;', '.fortune-art{\n  position:relative;\n  overflow:hidden;\n  min-height:760px;', 1)
    css = '''\n.hojakdo-img{\n  position:absolute;\n  inset:0;\n  display:block;\n  width:100%;\n  height:100%;\n  object-fit:cover;\n  object-position:left top;\n  z-index:2;\n}\n'''
    s = s.replace('.input-panel{', css + '\n.input-panel{', 1)

p.write_text(s, encoding='utf-8')
print('Direct Hojakdo image element applied. Calculation and result data unchanged.')
