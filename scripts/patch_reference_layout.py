from pathlib import Path
import re

p = Path('english-app4.html')
s = p.read_text(encoding='utf-8')

# Keep all working input IDs and calculation logic. Replace only the visible input shell.
start = '<section class="card input-card">'
result_marker = '\n<section id="result"'
if start not in s or result_marker not in s:
    raise SystemExit('Input/result markers not found')

a = s.index(start)
b = s.index(result_marker, a)
input_html = '''<section class="card input-card">
  <div class="reference-shell">
    <aside class="reference-art" aria-label="Hojakdo illustration">
      <img src="./assets/hojakdo-reference-left.jpg?v=20260827-ref1" alt="Korean Hojakdo inspired tiger and magpie illustration">
    </aside>
    <div class="reference-form">
      <div class="privacy-line">▣ Your information is used only for this calculation and is not stored.</div>
      <div class="reference-title"><span>☁</span><h2>Enter Your Information</h2><span>☁</span></div>
      <div class="reference-grid">
        <div class="fieldbox"><label>Date Type</label><select id="mode"><option value="solar">Solar Calendar</option><option value="lunar">Lunar Calendar</option></select></div>
        <div class="fieldbox"><label>Birth Year</label><input id="by" type="number" min="1900" max="2050" placeholder="Year"></div>
        <div class="fieldbox"><label>Birth Month</label><select id="bm"></select></div>
        <div class="fieldbox"><label>Birth Day</label><input id="bd" type="number" min="1" max="31" placeholder="Day"></div>
        <div class="fieldbox" id="leapWrap" style="display:none"><label>Leap Month</label><select id="leap"><option value="0">Regular Month</option><option value="1">Leap Month</option></select></div>
        <div class="fieldbox"><label>Fortune Year</label><input id="ty" type="number" min="1900" max="2050" value="2026"></div>
      </div>
      <button id="go">Reveal My Fortune ✨</button>
      <div class="under-button">Click the button above to reveal your 144 readings fortune.</div>
      <div id="err" class="note"></div>
    </div>
  </div>
</section>'''
s = s[:a] + input_html + s[b:]

# Remove prior visual patch blocks while leaving core styles and JS untouched.
for st, en in [
    ('/* INPUT_UI_START */','/* INPUT_UI_END */'),
    ('/* REFERENCE_UI_START */','/* REFERENCE_UI_END */')
]:
    if st in s and en in s:
        x=s.index(st); y=s.index(en,x)+len(en); s=s[:x]+s[y:]

css = r'''
/* REFERENCE_UI_START */
:root{--ink:#271853;--purple:#4a2579;--purple2:#6d4796;--paper:#fbf5e9;--line:#ded2c2;--muted:#6d6570}
body>.wrap>header{display:none}
body{background:#f1e7d5;color:#27233a}
.wrap{max-width:1180px;padding:18px 12px 54px}
.input-card{margin:0 0 18px;padding:0;overflow:hidden;border:1px solid #cdbbd7;border-radius:24px;background:#fffaf2;box-shadow:0 18px 48px rgba(64,42,83,.12)}
.reference-shell{display:grid;grid-template-columns:44% 56%;min-height:760px}
.reference-art{position:relative;overflow:hidden;background:#eee2cb;border-right:1px solid rgba(89,58,118,.14)}
.reference-art img{display:block;width:100%;height:100%;object-fit:cover;object-position:center top}
.reference-form{padding:26px 30px 30px;background:linear-gradient(180deg,#fffdfa,#fbf7ee)}
.privacy-line{text-align:right;font-size:11px;color:#514b54;margin:0 0 26px}
.reference-title{display:flex;align-items:center;justify-content:center;gap:14px;margin:0 0 28px;color:var(--purple2)}
.reference-title span{font-size:26px;line-height:1}
.reference-title h2{margin:0;color:var(--ink);font:700 32px/1.15 Georgia,"Times New Roman",serif}
.reference-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;border:1px solid #e0d7ca;border-radius:16px;overflow:hidden;background:rgba(255,255,255,.45)}
.fieldbox{min-height:125px;padding:20px 14px 16px;border-right:1px solid #e8dfd4;border-bottom:1px solid #e8dfd4}
.fieldbox:nth-child(3n){border-right:0}.fieldbox:nth-last-child(-n+3){border-bottom:0}
.input-card label{display:block;margin:0 0 10px;color:#37206a;font-size:12px;font-weight:700}
.input-card input,.input-card select{height:54px;width:100%;padding:0 13px;border:1px solid #d9d0c7;border-radius:8px;background:#fffdf9;color:#3c3740;font-size:14px;box-shadow:none}
.input-card input:focus,.input-card select:focus{outline:none;border-color:#7554a0;box-shadow:0 0 0 3px rgba(93,58,139,.09)}
.input-card #go{height:70px;margin:22px 0 0;border:1px solid #9c79bf;border-radius:10px;background:linear-gradient(180deg,#5b3289,#3f1f69);color:#fffaf1;font:700 23px/1 Georgia,"Times New Roman",serif;box-shadow:0 10px 20px rgba(60,31,101,.22);letter-spacing:.01em}
.input-card #go:hover{background:linear-gradient(180deg,#684095,#492574)}
.under-button{text-align:center;margin-top:14px;color:#67616b;font-size:12px}.input-card #err{text-align:center;min-height:18px;margin-top:6px}

#result{position:relative;margin-top:18px;padding:70px 16px 16px;border:1px solid #d3c3d9;border-radius:24px;background:linear-gradient(180deg,#fffdf8,#fbf4e7);box-shadow:0 16px 42px rgba(61,39,77,.09)}
#result:before{content:'☁  Your 144 Readings Result  ☁';position:absolute;top:22px;left:16px;right:16px;text-align:center;color:var(--ink);font:700 29px/1.2 Georgia,"Times New Roman",serif}
#result>.card{border:1px solid #e2d4c3;border-radius:16px;background:rgba(255,251,244,.94);box-shadow:none}
#result h2,#result h3{color:var(--ink);font-family:Georgia,"Times New Roman",serif}
#result .hero{border-color:#cfbadb;background:#fffaf1}
#result .badge,#result .pill{background:#eee4f5;color:#572f80}
#result .score{color:#492672}
#result .month{border-color:#e2d4c3;background:#fffaf2}
#result .bar{background:#eadfd1}#result .bar i{background:#53307e}
body>.wrap>.note{margin-top:16px;padding:13px 16px;border:1px solid #dfd1bf;border-radius:14px;background:#fffaf1;color:#756d72;text-align:center}

@media(max-width:900px){.reference-shell{grid-template-columns:1fr}.reference-art{height:680px;border-right:0;border-bottom:1px solid rgba(89,58,118,.14)}.reference-form{padding:26px 22px}.reference-grid{grid-template-columns:repeat(2,1fr)}.fieldbox:nth-child(3n){border-right:1px solid #e8dfd4}.fieldbox:nth-child(2n){border-right:0}.fieldbox:nth-last-child(-n+3){border-bottom:1px solid #e8dfd4}.fieldbox:nth-last-child(-n+2){border-bottom:0}}
@media(max-width:600px){.wrap{padding:8px 6px 40px}.input-card,#result{border-radius:18px}.reference-art{height:560px}.reference-form{padding:20px 13px}.privacy-line{text-align:center;margin-bottom:20px;font-size:10px}.reference-title{gap:8px;margin-bottom:20px}.reference-title h2{font-size:25px}.reference-title span{font-size:20px}.reference-grid{grid-template-columns:1fr}.fieldbox,.fieldbox:nth-child(n){min-height:auto;padding:14px;border-right:0;border-bottom:1px solid #e8dfd4}.fieldbox:last-child{border-bottom:0}.input-card #go{height:60px;font-size:19px}#result{padding:65px 8px 8px}#result:before{top:20px;font-size:22px}}
/* REFERENCE_UI_END */
'''
s = s.replace('</style>', css + '\n</style>', 1)
p.write_text(s, encoding='utf-8')
print('Reference layout applied; calculation logic and data unchanged.')
