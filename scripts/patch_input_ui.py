from pathlib import Path

p = Path('english-app4.html')
s = p.read_text(encoding='utf-8')

# Replace only the information-entry section. All existing input IDs are preserved.
section_start = '<section class="card input-card">'
result_marker = '\n<section id="result"'
if section_start in s and result_marker in s:
    a = s.index(section_start)
    b = s.index(result_marker, a)
    input_section = '''<section class="card input-card">
  <div class="input-shell">
    <aside class="fortune-art" aria-label="Approved Hojakdo visual"></aside>
    <div class="input-panel">
      <div class="privacy-top">▣ Your information is used only for this calculation and is not stored.</div>
      <div class="input-heading">
        <h2>Enter Your Information</h2>
      </div>
      <div class="grid">
        <div><label>Date Type</label><select id="mode"><option value="solar">Solar Calendar</option><option value="lunar">Lunar Calendar</option></select></div>
        <div><label>Birth Year</label><input id="by" type="number" min="1900" max="2050"></div>
        <div><label>Birth Month</label><select id="bm"></select></div>
        <div><label>Birth Day</label><input id="bd" type="number" min="1" max="31"></div>
        <div id="leapWrap" style="display:none"><label>Leap Month</label><select id="leap"><option value="0">Regular Month</option><option value="1">Leap Month</option></select></div>
        <div><label>Fortune Year</label><input id="ty" type="number" min="1900" max="2050" value="2026"></div>
      </div>
      <button id="go">✦ Reveal My Fortune ✦</button>
      <div class="under-button">Click the button above to reveal your 144 readings fortune.</div>
      <div id="err" class="note"></div>
    </div>
  </div>
</section>'''
    s = s[:a] + input_section + s[b:]
else:
    raise SystemExit('Input section marker not found; no file changes made.')

start = '/* INPUT_UI_START */'
end = '/* INPUT_UI_END */'
if start in s and end in s:
    a = s.index(start)
    b = s.index(end, a) + len(end)
    s = s[:a] + s[b:]

css = r'''
/* INPUT_UI_START */
body>.wrap>header{display:none}
body{background:#efe6d5}
.wrap{max-width:1180px;padding:18px 14px 50px}
.input-card{
  margin:0 0 18px;
  padding:0;
  overflow:hidden;
  border:1px solid #cdbbe0;
  border-radius:28px;
  background:#fffaf2;
  box-shadow:0 22px 60px rgba(54,36,72,.14);
}
.input-shell{
  display:grid;
  grid-template-columns:minmax(330px,.92fr) minmax(0,1.58fr);
  min-height:590px;
}
.fortune-art{
  min-height:590px;
  background-color:#eadfc9;
  background-image:url('./assets/hojakdo-ui-reference.jpg');
  background-repeat:no-repeat;
  background-position:left top;
  background-size:auto 100%;
  border-right:1px solid rgba(106,75,145,.14);
}
.input-panel{
  position:relative;
  padding:30px 34px 30px;
  background:
    radial-gradient(circle at 88% 4%,rgba(114,83,153,.07),transparent 24%),
    linear-gradient(180deg,#fffdfa 0%,#fbf7f0 100%);
}
.privacy-top{
  margin:0 0 20px;
  text-align:right;
  color:#4b4650;
  font-size:11px;
  line-height:1.4;
}
.input-heading{
  margin:4px 0 26px;
  text-align:center;
}
.input-heading h2{
  position:relative;
  display:inline-block;
  margin:0;
  padding:0 42px;
  color:#352358;
  font-family:Georgia,"Times New Roman",serif;
  font-size:31px;
  letter-spacing:-.015em;
}
.input-heading h2:before,.input-heading h2:after{
  content:'☁';
  position:absolute;
  top:50%;
  transform:translateY(-50%);
  color:#8060a5;
  font-size:22px;
  font-family:serif;
  font-weight:400;
}
.input-heading h2:before{left:0}
.input-heading h2:after{right:0}
.input-card .grid{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:18px 14px;
  padding:18px 16px;
  border:1px solid #e0d7d0;
  border-radius:18px;
  background:rgba(255,255,255,.46);
}
.input-card label{
  margin:0 0 8px;
  font-size:12px;
  font-weight:800;
  color:#4f337a;
}
.input-card input,
.input-card select{
  height:50px;
  padding:0 14px;
  border:1px solid #d8d0ca;
  border-radius:10px;
  background:#fffdf9;
  color:#3f3a45;
  font-size:14px;
  box-shadow:0 2px 7px rgba(56,39,73,.035);
  transition:border-color .16s ease,box-shadow .16s ease;
}
.input-card input:focus,
.input-card select:focus{
  outline:none;
  border-color:#76549e;
  box-shadow:0 0 0 3px rgba(101,73,142,.11);
}
.input-card #go{
  height:64px;
  margin-top:20px;
  border:1px solid #9e79c4;
  border-radius:12px;
  background:linear-gradient(180deg,#5e378b 0%,#42236f 100%);
  color:#fff8e8;
  font-family:Georgia,"Times New Roman",serif;
  font-size:21px;
  letter-spacing:.01em;
  font-weight:700;
  box-shadow:0 9px 20px rgba(66,35,111,.25),inset 0 0 0 2px rgba(255,255,255,.10);
}
.input-card #go:hover{background:linear-gradient(180deg,#6b4297 0%,#4b2977 100%)}
.under-button{
  margin-top:12px;
  text-align:center;
  color:#6f6873;
  font-size:12px;
}
.input-card #err{
  margin-top:7px;
  min-height:16px;
  text-align:center;
}
@media(max-width:900px){
  .input-shell{grid-template-columns:1fr}
  .fortune-art{
    min-height:430px;
    background-size:auto 100%;
    background-position:left top;
    border-right:0;
    border-bottom:1px solid rgba(106,75,145,.14);
  }
  .input-panel{padding:28px 24px}
}
@media(max-width:650px){
  .input-card{border-radius:20px}
  .fortune-art{min-height:390px;background-size:auto 100%}
  .input-panel{padding:24px 16px}
  .privacy-top{text-align:center;font-size:10px}
  .input-heading h2{font-size:26px;padding:0 34px}
  .input-card .grid{grid-template-columns:1fr;gap:13px;padding:14px}
  .input-card input,.input-card select{height:49px}
  .input-card #go{height:58px;font-size:18px}
}
/* INPUT_UI_END */
'''

s = s.replace('</style>', css + '\n</style>', 1)
p.write_text(s, encoding='utf-8')
print('Approved UI image applied as-is to the input design. Calculation and result scripts unchanged.')
