"""Stáhne hOCR z MDZ (BSB) pro všechny skeny a uloží čistý text po řádcích.
Použití: python nastroje/stahni_ocr_bsb.py knihy/fronsberger-1564 [bsb-id] [cilova-slozka]
"""
import json, re, html, sys, time, pathlib, urllib.request
kniha = pathlib.Path(sys.argv[1])
bsb = sys.argv[2] if len(sys.argv) > 2 else 'bsb00045899'
mf = kniha/'zdroje'/f'manifest_{bsb}.json'
if not mf.exists():
    mf.write_bytes(urllib.request.urlopen(f'https://api.digitale-sammlungen.de/iiif/presentation/v2/{bsb}/manifest', timeout=60).read())
man = json.loads(mf.read_text(encoding='utf-8'))
out = kniha/'zdroje'/(sys.argv[3] if len(sys.argv) > 3 else 'ocr_bsb'); out.mkdir(parents=True, exist_ok=True)
for i, c in enumerate(man['sequences'][0]['canvases'], 1):
    f = out/f'{i:04d}.txt'
    if f.exists(): continue
    url = c['seeAlso']['@id']
    for pokus in range(3):
        try:
            s = urllib.request.urlopen(url, timeout=60).read().decode('utf-8'); break
        except Exception as e:
            print('chyba', i, e); time.sleep(3)
    else: continue
    radky = []
    for l in re.findall(r'<span class=.ocr_line.*?</span>\s*</span>', s, flags=re.S):
        w = re.findall(r'class=.ocrx_word[^>]*>([^<]*)<', l)
        radky.append(' '.join(html.unescape(x) for x in w))
    f.write_text('\n'.join(radky), encoding='utf-8')
    time.sleep(0.3)
print('hotovo')
