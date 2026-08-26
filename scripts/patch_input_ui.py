from pathlib import Path

p = Path('english-app4.html')
s = p.read_text(encoding='utf-8')

# Replace only the information-entry section. All existing input IDs and calculation behavior are preserved.
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
      <div class="input-heading"><h2>Enter Your Information</h2></div>
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
body{
  background:#eee4d2;
  color:#29233a;
}
.wrap{max-width:1180px;padding:18px 14px 52px}

/* FINAL APPROVED INPUT MOCKUP */
.input-card{
  margin:0 0 22px;
  padding:0;
  overflow:hidden;
  border:1px solid #bba2d2;
  border-radius:28px;
  background:#fffaf1;
  box-shadow:0 22px 60px rgba(54,36,72,.14);
}
.input-shell{
  display:grid;
  grid-template-columns:minmax(360px,.95fr) minmax(0,1.55fr);
  min-height:760px;
}
.fortune-art{
  min-height:760px;
  background-color:#eadfc9;
  background-image:url('./assets/hojakdo-final.webp');
  background-repeat:no-repeat;
  background-position:left top;
  background-size:cover;
  border-right:1px solid rgba(106,75,145,.15);
}
.input-panel{
  position:relative;
  padding:34px 38px 34px;
  background:
    radial-gradient(circle at 85% 2%,rgba(110,79,151,.06),transparent 26%),
    linear-gradient(180deg,#fffdfa 0%,#fbf7ef 100%);
}
.privacy-top{
  margin:0 0 34px;
  text-align:right;
  color:#4f4953;
  font-size:11px;
  line-height:1.4;
}
.input-heading{
  margin:0 0 34px;
  text-align:center;
}
.input-heading h2{
  position:relative;
  display:inline-block;
  margin:0;
  padding:0 48px;
  color:#38235f;
  font-family:Georgia,"Times New Roman",serif;
  font-size:34px;
  line-height:1.15;
  letter-spacing:-.02em;
}
.input-heading h2:before,.input-heading h2:after{
  content:'☁';
  position:absolute;
  top:50%;
  transform:translateY(-50%);
  color:#7956a2;
  font-size:24px;
  font-family:serif;
  font-weight:400;
}
.input-heading h2:before{left:0}
.input-heading h2:after{right:0}
.input-card .grid{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:28px 18px;
  padding:26px 20px;
  border:1px solid #ddd3cb;
  border-radius:18px;
  background:rgba(255,255,255,.50);
}
.input-card label{
  margin:0 0 9px;
  font-size:12px;
  font-weight:800;
  color:#4c2f78;
}
.input-card input,
.input-card select{
  height:52px;
  padding:0 14px;
  border:1px solid #d9d0c8;
  border-radius:9px;
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
  height:66px;
  margin-top:24px;
  border:1px solid #9e79c4;
  border-radius:12px;
  background:linear-gradient(180deg,#5f398d 0%,#42236f 100%);
  color:#fff8e8;
  font-family:Georgia,"Times New Roman",serif;
  font-size:22px;
  letter-spacing:.01em;
  font-weight:700;
  box-shadow:0 10px 22px rgba(66,35,111,.24),inset 0 0 0 2px rgba(255,255,255,.10);
}
.input-card #go:hover{background:linear-gradient(180deg,#6a4297 0%,#4b2977 100%)}
.under-button{
  margin-top:13px;
  text-align:center;
  color:#6f6873;
  font-size:12px;
}
.input-card #err{
  margin-top:7px;
  min-height:16px;
  text-align:center;
}

/* RESULT AREA: same cream / purple / folk-art visual language; result data is unchanged */
#result{
  position:relative;
  margin-top:18px;
  padding:76px 18px 18px;
  border:1px solid #bba2d2;
  border-radius:28px;
  background:linear-gradient(180deg,#fffdf8 0%,#fbf5e9 100%);
  box-shadow:0 18px 45px rgba(54,36,72,.10);
}
#result:before{
  content:'☁  Your 144 Readings Result  ☁';
  position:absolute;
  top:24px;
  left:20px;
  right:20px;
  text-align:center;
  color:#38235f;
  font-family:Georgia,"Times New Roman",serif;
  font-size:28px;
  font-weight:700;
}
#result>.card{
  border:1px solid #dfd2c4;
  border-radius:18px;
  background:rgba(255,252,246,.92);
  box-shadow:none;
}
#result h2,#result h3{
  color:#38235f;
  font-family:Georgia,"Times New Roman",serif;
}
#result .hero{
  border-color:#cdb8df;
  background:linear-gradient(180deg,#fffdf9 0%,#fbf5eb 100%);
}
#result .badge,#result .pill{
  background:#ede3f5;
  color:#5a3683;
}
#result .score{color:#4b2a78}
#result .table td{border-top-color:#e5d8ca}
#result .table td:first-child{color:#655675}
#result .field{border-top-color:#e5d8ca}
#result .month{
  border-color:#dfd2c4;
  background:#fffaf2;
}
#result .bar{background:#e9dfd3}
#result .bar i{background:#5b3587}
body>.wrap>.note{
  margin-top:18px;
  padding:14px 18px;
  border:1px solid #ded0bf;
  border-radius:16px;
  background:rgba(255,250,241,.82);
  text-align:center;
  color:#756b70;
}

@media(max-width:920px){
  .input-shell{grid-template-columns:1fr;min-height:0}
  .fortune-art{
    min-height:640px;
    background-size:cover;
    background-position:left top;
    border-right:0;
    border-bottom:1px solid rgba(106,75,145,.14);
  }
  .input-panel{padding:30px 24px}
}
@media(max-width:700px){
  .input-card{border-radius:20px}
  .fortune-art{min-height:560px;background-size:cover;background-position:left top}
  .input-panel{padding:24px 16px}
  .privacy-top{text-align:center;font-size:10px;margin-bottom:26px}
  .input-heading h2{font-size:27px;padding:0 38px}
  .input-card .grid{grid-template-columns:1fr;gap:14px;padding:16px}
  .input-card input,.input-card select{height:50px}
  .input-card #go{height:59px;font-size:19px}
  #result{padding:70px 10px 10px;border-radius:20px}
  #result:before{font-size:23px;top:22px}
}
/* INPUT_UI_END */
'''

s = s.replace('</style>', css + '\n</style>', 1)
p.write_text(s, encoding='utf-8')
print('Final approved Hojakdo mockup styling applied. Calculation and result data unchanged.')
