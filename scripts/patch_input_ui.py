from pathlib import Path

p = Path('english-app4.html')
s = p.read_text(encoding='utf-8')

# Mark only the first input card. Do not touch result cards or any calculation script.
s = s.replace('<section class="card"><div class="grid">', '<section class="card input-card"><div class="grid">', 1)

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
  padding:24px;
  border:1px solid #e7e1ef;
  border-radius:22px;
  background:linear-gradient(180deg,#fffefd 0%,#fbf9ff 100%);
  box-shadow:0 12px 32px rgba(60,45,90,.07);
}
.input-card .grid{
  display:grid;
  grid-template-columns:repeat(6,minmax(0,1fr));
  gap:14px;
}
.input-card .grid>div{
  grid-column:span 2;
}
.input-card #leapWrap{
  grid-column:span 2;
}
.input-card label{
  margin:0 0 7px;
  font-size:12px;
  font-weight:700;
  color:#6e6579;
}
.input-card input,
.input-card select{
  height:50px;
  padding:0 14px;
  border:1px solid #ded8e8;
  border-radius:14px;
  background:#fff;
  color:#231f2b;
  font-size:15px;
  box-shadow:0 2px 8px rgba(50,40,70,.03);
  transition:border-color .15s ease, box-shadow .15s ease;
}
.input-card input:focus,
.input-card select:focus{
  outline:none;
  border-color:#7b6be2;
  box-shadow:0 0 0 4px rgba(123,107,226,.10);
}
.input-card #go{
  height:54px;
  margin-top:18px;
  border-radius:15px;
  background:#6555d9;
  font-size:15px;
  font-weight:800;
  box-shadow:0 10px 22px rgba(88,72,216,.18);
}
.input-card #go:hover{
  background:#5a4bc8;
}
.input-card #err{
  margin-top:10px;
  min-height:18px;
}
@media(max-width:760px){
  .input-card{padding:18px;border-radius:20px}
  .input-card .grid>div,
  .input-card #leapWrap{grid-column:span 3}
}
@media(max-width:520px){
  .input-card{padding:16px;border-radius:18px}
  .input-card .grid{grid-template-columns:1fr;gap:12px}
  .input-card .grid>div,
  .input-card #leapWrap{grid-column:1}
  .input-card input,
  .input-card select{height:48px}
  .input-card #go{height:52px}
}
/* INPUT_UI_END */
'''

s = s.replace('</style>', css + '\n</style>', 1)
p.write_text(s, encoding='utf-8')
print('Input UI design patch applied. No calculation/result code changed.')
