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
    <aside class="fortune-art" aria-label="Korean folk-art inspired fortune illustration">
      <div class="art-shade"></div>
      <div class="art-copy">
        <span class="art-kicker">KOREAN FOLK FORTUNE</span>
        <h2>Your year,<br>revealed in 144 readings.</h2>
        <p>A modern reading rooted in the traditional Tojeong Bikyeol system.</p>
        <span class="art-seal">MYKYU · 144</span>
      </div>
    </aside>
    <div class="input-panel">
      <div class="input-heading">
        <span>PERSONAL READING</span>
        <h2>Enter Your Information</h2>
        <p>Choose your birth date and the year you want to explore.</p>
      </div>
      <div class="grid">
        <div><label>Date Type</label><select id="mode"><option value="solar">Solar Calendar</option><option value="lunar">Lunar Calendar</option></select></div>
        <div><label>Birth Year</label><input id="by" type="number" min="1900" max="2050"></div>
        <div><label>Birth Month</label><select id="bm"></select></div>
        <div><label>Birth Day</label><input id="bd" type="number" min="1" max="31"></div>
        <div id="leapWrap" style="display:none"><label>Leap Month</label><select id="leap"><option value="0">Regular Month</option><option value="1">Leap Month</option></select></div>
        <div><label>Fortune Year</label><input id="ty" type="number" min="1900" max="2050" value="2026"></div>
      </div>
      <button id="go">✦ Reveal My Fortune</button>
      <div class="privacy-note">Your information is used only for this calculation and is not stored.</div>
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
.input-card{
  margin-top:24px;
  padding:0;
  overflow:hidden;
  border:1px solid #e2d6e6;
  border-radius:28px;
  background:#fffaf5;
  box-shadow:0 22px 60px rgba(47,30,67,.12);
}
.input-shell{
  display:grid;
  grid-template-columns:minmax(300px,.86fr) minmax(0,1.55fr);
  min-height:590px;
}
.fortune-art{
  position:relative;
  min-height:590px;
  overflow:hidden;
  background:#e9dff0 url('./assets/hojakdo-modern.svg') center 46%/cover no-repeat;
}
.art-shade{
  position:absolute;
  inset:0;
  background:linear-gradient(180deg,rgba(34,24,48,.03) 0%,rgba(34,24,48,.05) 50%,rgba(30,20,42,.75) 100%);
}
.art-copy{
  position:absolute;
  z-index:2;
  left:30px;
  right:30px;
  bottom:30px;
  color:#fff;
  text-shadow:0 2px 18px rgba(20,12,30,.32);
}
.art-kicker,
.input-heading>span{
  display:inline-block;
  font-size:11px;
  line-height:1;
  letter-spacing:.18em;
  font-weight:800;
}
.art-kicker{color:#f2d798}
.art-copy h2{
  margin:12px 0 10px;
  font-family:Georgia,"Times New Roman",serif;
  font-size:34px;
  line-height:1.06;
  letter-spacing:-.02em;
}
.art-copy p{
  max-width:330px;
  margin:0;
  font-size:14px;
  line-height:1.65;
  color:rgba(255,255,255,.88);
}
.art-seal{
  display:inline-block;
  margin-top:18px;
  padding:7px 10px;
  border:1px solid rgba(242,215,152,.78);
  border-radius:8px;
  color:#f6dfa9;
  font-size:10px;
  letter-spacing:.14em;
  font-weight:800;
}
.input-panel{
  padding:38px 40px 34px;
  background:
    radial-gradient(circle at 90% 5%,rgba(113,83,154,.08),transparent 28%),
    linear-gradient(180deg,#fffdf9 0%,#fbf7f3 100%);
}
.input-heading{
  margin-bottom:28px;
  text-align:center;
}
.input-heading>span{color:#8a6ba6}
.input-heading h2{
  margin:9px 0 7px;
  color:#2c213b;
  font-family:Georgia,"Times New Roman",serif;
  font-size:30px;
  letter-spacing:-.02em;
}
.input-heading p{
  margin:0;
  color:#84798c;
  font-size:14px;
}
.input-card .grid{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:16px 14px;
}
.input-card label{
  margin:0 0 8px;
  font-size:12px;
  font-weight:800;
  color:#58466e;
}
.input-card input,
.input-card select{
  height:52px;
  padding:0 15px;
  border:1px solid #ded5df;
  border-radius:14px;
  background:rgba(255,255,255,.92);
  color:#2d2733;
  font-size:15px;
  box-shadow:0 3px 10px rgba(58,39,73,.035);
  transition:border-color .16s ease,box-shadow .16s ease,transform .16s ease;
}
.input-card input:focus,
.input-card select:focus{
  outline:none;
  border-color:#8668a6;
  box-shadow:0 0 0 4px rgba(110,79,151,.10),0 5px 16px rgba(58,39,73,.06);
}
.input-card #go{
  height:58px;
  margin-top:22px;
  border-radius:16px;
  background:linear-gradient(135deg,#694b8d 0%,#4f3a78 100%);
  color:#fff9ef;
  font-family:Georgia,"Times New Roman",serif;
  font-size:18px;
  letter-spacing:.01em;
  font-weight:700;
  box-shadow:0 13px 28px rgba(73,48,103,.24),inset 0 1px 0 rgba(255,255,255,.18);
}
.input-card #go:hover{
  background:linear-gradient(135deg,#76559a 0%,#574080 100%);
  transform:translateY(-1px);
}
.privacy-note{
  margin-top:13px;
  text-align:center;
  color:#968b9b;
  font-size:11px;
  line-height:1.5;
}
.input-card #err{
  margin-top:8px;
  min-height:16px;
  text-align:center;
}
@media(max-width:820px){
  .input-shell{grid-template-columns:1fr}
  .fortune-art{min-height:360px;background-position:center 42%}
  .art-copy{left:24px;right:24px;bottom:24px}
  .art-copy h2{font-size:30px}
  .input-panel{padding:30px 24px}
}
@media(max-width:560px){
  .input-card{border-radius:22px}
  .fortune-art{min-height:320px}
  .input-panel{padding:26px 18px 24px}
  .input-heading h2{font-size:26px}
  .input-card .grid{grid-template-columns:1fr;gap:13px}
  .input-card input,.input-card select{height:50px}
  .input-card #go{height:55px;font-size:17px}
}
/* INPUT_UI_END */
'''

s = s.replace('</style>', css + '\n</style>', 1)
p.write_text(s, encoding='utf-8')
print('Hojakdo-inspired input UI applied. Calculation and result scripts unchanged.')
