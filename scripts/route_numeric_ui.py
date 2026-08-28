from pathlib import Path

replacements = {
    'english-v2.html': [
        ('./english-app7.html?v=20260828-premium1', './english-app7.html?v=20260828-numeric1'),
    ],
    'english-v4.html': [
        ('./english-v2.html?v=20260828-luxury2', './english-v2.html?v=20260828-luxury3'),
        ('20260828-luxury2', '20260828-luxury3'),
    ],
    'english.html': [
        ('20260828-luxury2', '20260828-luxury3'),
    ],
}

for name, pairs in replacements.items():
    path = Path(name)
    text = path.read_text(encoding='utf-8')
    changed = False
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new)
            changed = True
    if not changed and not any(new in text for _, new in pairs):
        raise SystemExit(f'cache route anchor not found in {name}')
    path.write_text(text, encoding='utf-8')
    print(f'updated {name}')
