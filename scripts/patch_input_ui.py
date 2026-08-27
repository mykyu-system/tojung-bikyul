from pathlib import Path
import base64
import re

p = Path('english-app4.html')
img_path = Path('assets/hojakdo-final.webp')

s = p.read_text(encoding='utf-8')
if not img_path.exists():
    raise SystemExit('Hojakdo image asset not found')

# Embed the approved Hojakdo image directly in the HTML so Blogger/GitHub Pages
# cannot lose it because of asset paths, caching, or nested iframes.
img64 = base64.b64encode(img_path.read_bytes()).decode('ascii')
data_uri = 'data:image/webp;base64,' + img64

img_tag = f'<img class="hojakdo-img" src="{data_uri}" alt="Hojakdo tiger and gat-wearing magpie illustration">'

# Replace the existing approved image element, or insert it if an older version is present.
pattern = r'<img\s+class="hojakdo-img"[^>]*>'
if re.search(pattern, s):
    s = re.sub(pattern, img_tag, s, count=1)
else:
    old_aside = '<aside class="fortune-art" aria-label="Approved Hojakdo visual"></aside>'
    new_aside = '<aside class="fortune-art" aria-label="Approved Hojakdo visual">' + img_tag + '</aside>'
    if old_aside not in s:
        raise SystemExit('Hojakdo display area not found; no changes made')
    s = s.replace(old_aside, new_aside, 1)

# The visible picture now comes from the img element, not a CSS URL.
s = re.sub(
    r"background-image:url\(['\"]?\./assets/hojakdo-final\.webp['\"]?\);",
    'background-image:none;',
    s,
    count=1,
)

# Ensure the image fills the approved left panel.
if '.hojakdo-img{' not in s:
    marker = '.input-panel{'
    css = '''.hojakdo-img{\n  position:absolute;\n  inset:0;\n  display:block;\n  width:100%;\n  height:100%;\n  object-fit:cover;\n  object-position:left top;\n  z-index:2;\n}\n\n'''
    if marker in s:
        s = s.replace(marker, css + marker, 1)

# Ensure the containing art panel can host an absolutely positioned image.
s = s.replace('.fortune-art{\n  min-height:', '.fortune-art{\n  position:relative;\n  overflow:hidden;\n  min-height:', 1)

p.write_text(s, encoding='utf-8')
print('Approved Hojakdo image embedded directly into english-app4.html. Calculation/result logic unchanged.')
