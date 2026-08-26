from pathlib import Path

p = Path('english-app4.html')
s = p.read_text(encoding='utf-8')
original = s

# Static reader-facing wording.
s = s.replace('using a 144-Gua calculation system.', 'using a 144-reading system.')
s = s.replace('traditional 144-Gua structure', 'traditional 144-reading structure')
s = s.replace('Traditional Gua calculation using the 60-cycle reference system.', 'Traditional reading calculation using the 60-cycle reference system.')
s = s.replace('traditional Gua names', 'traditional reading names')

# Add direct zodiac + reading-name display helpers inside the calculator itself.
needle = "CYCLE=Array.from({length:60},(_,i)=>STEM[i%10]+'-'+BRANCH[i%12]);"
helper = "const ZODIAC={Zi:'Rat',Chou:'Ox',Yin:'Tiger',Mao:'Rabbit',Chen:'Dragon',Si:'Snake',Wu:'Horse',Wei:'Goat',Shen:'Monkey',You:'Rooster',Xu:'Dog',Hai:'Pig'};const zodiacName=v=>{const b=String(v??'').split('-').pop();return ZODIAC[b]||String(v??'')};const readingName=v=>String(v??'').replace(/\\bGua\\b/gi,'Reading');"
if 'const ZODIAC=' not in s:
    if needle not in s:
        raise SystemExit('Could not find CYCLE insertion point')
    s = s.replace(needle, needle + helper, 1)

# Reader-facing result output: no stem/branch romanization and no Gua terminology.
s = s.replace("x.name='Gua '+String(i+1).padStart(3,'0');", "x.name='Reading '+String(i+1).padStart(3,'0');")
s = s.replace('and ${g.name}, this year shows', 'and ${readingName(g.name)}, this year shows')
s = s.replace("$('qn').textContent=g.name;", "$('qn').textContent=readingName(g.name);")
s = s.replace('`Fortune year ${ty} • Year cycle ${tg} • Birth lunar date ${ly}-${lm}-${ld}`', '`Fortune year ${ty} • Year Zodiac ${zodiacName(tg)} • Birth lunar date ${ly}-${lm}-${ld}`')
s = s.replace("['Year cycle',tg],['Gua code',code]", "['Year Zodiac',zodiacName(tg)],['Reading Code',code]")
s = s.replace("['Year cycle',tg],['Year number',yr.yearNumber]", "['Year Zodiac',zodiacName(tg)],['Year number',yr.yearNumber]")
s = s.replace("['Month cycle',mg],['Month number',mr.monthNumber]", "['Month Zodiac',zodiacName(mg)],['Month number',mr.monthNumber]")
s = s.replace("['Birth-day cycle',dg],['Day number',dr.dayNumber]", "['Birth-day Zodiac',zodiacName(dg)],['Day number',dr.dayNumber]")
s = s.replace("['Upper Gua',code.split('-')[0]]", "['Upper Trigram',code.split('-')[0]]")
s = s.replace("['Middle Gua',code.split('-')[1]]", "['Middle Trigram',code.split('-')[1]]")
s = s.replace("['Lower Gua',code.split('-')[2]]", "['Lower Trigram',code.split('-')[2]]")
s = s.replace("['Final 144 Gua',code]", "['Final Reading',code]")

if s == original:
    raise SystemExit('No changes were applied')

# Sanity checks on the final reader-facing code.
required = [
    "Year Zodiac ${zodiacName(tg)}",
    "['Reading Code',code]",
    "['Upper Trigram',code.split('-')[0]]",
    "['Final Reading',code]",
    "const ZODIAC={Zi:'Rat'",
]
missing = [x for x in required if x not in s]
if missing:
    raise SystemExit('Missing expected patches: ' + repr(missing))

p.write_text(s, encoding='utf-8')
print('Patched english-app4.html reader-facing zodiac and reading labels.')
