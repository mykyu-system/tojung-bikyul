from pathlib import Path

src = Path('/tmp/english-app7-base.html')
dst = Path('english-app7.html')
text = src.read_text(encoding='utf-8')

old_inputs = '''<div class="field"><label><span class="icon">▣</span>Birth Date</label><input id="birthDate" type="date" min="1900-01-01" max="2050-12-31"></div><div class="field"><label><span class="icon">◷</span>Birth Time</label><input id="birthTime" type="time"></div>'''
new_inputs = '''<div class="field"><label><span class="icon">▣</span>Birth Date</label><div class="number-entry birth-date-entry"><input id="birthYear" type="text" inputmode="numeric" pattern="[0-9]*" maxlength="4" placeholder="YYYY" aria-label="Birth year"><span class="number-sep">/</span><input id="birthMonth" type="text" inputmode="numeric" pattern="[0-9]*" maxlength="2" placeholder="MM" aria-label="Birth month"><span class="number-sep">/</span><input id="birthDay" type="text" inputmode="numeric" pattern="[0-9]*" maxlength="2" placeholder="DD" aria-label="Birth day"></div><input id="birthDate" type="hidden"></div><div class="field"><label><span class="icon">◷</span>Birth Time</label><div class="number-entry birth-time-entry"><input id="birthHour" type="text" inputmode="numeric" pattern="[0-9]*" maxlength="2" placeholder="HH" aria-label="Birth hour"><span class="number-sep">:</span><input id="birthMinute" type="text" inputmode="numeric" pattern="[0-9]*" maxlength="2" placeholder="MM" aria-label="Birth minute"></div><input id="birthTime" type="hidden"></div>'''
if old_inputs not in text:
    raise SystemExit('birth date/time markup anchor not found')
text = text.replace(old_inputs, new_inputs, 1)

mobile = '''<div class="field"><label><span class="icon">⌕</span>Mobile Number (Optional)</label><input id="mobile" inputmode="tel" placeholder="Optional"></div>'''
if mobile not in text:
    raise SystemExit('mobile field anchor not found')
text = text.replace(mobile, '', 1)

css_anchor = '.leap-mini{display:none;margin-top:7px}.leap-mini.show{display:block}'
css = css_anchor + '.number-entry{display:grid;align-items:center;gap:5px;width:100%}.birth-date-entry{grid-template-columns:minmax(58px,1.45fr) 8px minmax(39px,.8fr) 8px minmax(39px,.8fr)}.birth-time-entry{grid-template-columns:minmax(46px,1fr) 8px minmax(46px,1fr)}.number-entry input{min-width:0!important;padding:0 5px!important;text-align:center!important;font-variant-numeric:tabular-nums!important;letter-spacing:.02em!important}.number-entry input::placeholder{color:#9d96a0;opacity:1}.number-sep{display:block;text-align:center;color:#8a7d8e;font-weight:800;font-size:13px;line-height:1}'
if css_anchor not in text:
    raise SystemExit('css anchor not found')
text = text.replace(css_anchor, css, 1)

js_anchor = "document.querySelectorAll('.gender button').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.gender button').forEach(x=>x.classList.remove('active'));b.classList.add('active');gender=b.dataset.gender}));$('mode').addEventListener('change',()=>{$('leapMini').classList.toggle('show',$('mode').value==='lunar');reportHeight()});"
js = "document.querySelectorAll('.gender button').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.gender button').forEach(x=>x.classList.remove('active'));b.classList.add('active');gender=b.dataset.gender}));function digitsOnly(el,max){el.value=el.value.replace(/\\D/g,'').slice(0,max)}function syncBirthInputs(){const y=$('birthYear').value,m=$('birthMonth').value,d=$('birthDay').value,hh=$('birthHour').value,mm=$('birthMinute').value,yn=Number(y),mn=Number(m),dn=Number(d),hn=Number(hh),minn=Number(mm);$('birthDate').value=(y.length===4&&yn>=1900&&yn<=2050&&mn>=1&&mn<=12&&dn>=1&&dn<=31)?`${y}-${String(mn).padStart(2,'0')}-${String(dn).padStart(2,'0')}`:'';$('birthTime').value=(hh!==''&&mm!==''&&hn>=0&&hn<=23&&minn>=0&&minn<=59)?`${String(hn).padStart(2,'0')}:${String(minn).padStart(2,'0')}`:''}const numericFlow=[['birthYear',4,'birthMonth'],['birthMonth',2,'birthDay'],['birthDay',2,'birthHour'],['birthHour',2,'birthMinute'],['birthMinute',2,null]];numericFlow.forEach(([id,max,next])=>{const el=$(id);el.addEventListener('input',()=>{digitsOnly(el,max);syncBirthInputs();if(next&&el.value.length===max)$(next).focus()});el.addEventListener('blur',()=>{if(id!=='birthYear'&&el.value.length===1)el.value='0'+el.value;syncBirthInputs()})});$('mode').addEventListener('change',()=>{$('leapMini').classList.toggle('show',$('mode').value==='lunar');reportHeight()});"
if js_anchor not in text:
    raise SystemExit('numeric javascript anchor not found')
text = text.replace(js_anchor, js, 1)

birth_anchor = "function getBirth(){const v=$('birthDate').value;if(!v)return null;"
if birth_anchor not in text:
    raise SystemExit('getBirth anchor not found')
text = text.replace(birth_anchor, "function getBirth(){syncBirthInputs();const v=$('birthDate').value;if(!v)return null;", 1)
text = text.replace('Please enter a valid birth date supported by the calendar data.', 'Please enter a valid birth date using numbers (YYYY / MM / DD).', 1)

dst.write_text(text, encoding='utf-8')
print('numeric inputs patched; mobile field removed')
