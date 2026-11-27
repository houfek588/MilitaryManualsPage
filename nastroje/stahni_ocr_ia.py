"""Stáhne OCR knihy z Internet Archive (soubor <id>_djvu.xml) a uloží text po stranách.

Číslo strany = číslo listu skenu v archivu (soubory <id>_NNNN.jp2 / .djvu, barevná tabulka na začátku má číslo 0),
tedy stejné číslo, jaké se píše do pole `sken` a do IIIF adresy https://iiif.archive.org/iiif/<id>%24<sken>/….
Výstup: knihy/<kniha>/zdroje/ocr_ia/NNNN.txt (po řádcích), kopie djvu.xml v zdroje/.
Použití: python -I nastroje/stahni_ocr_ia.py knihy/della-valle-1528 vallolibrocotine00dell
"""
import html, pathlib, re, sys, urllib.request

kniha, ident = pathlib.Path(sys.argv[1]), sys.argv[2]
zdroje = kniha / 'zdroje'
zdroje.mkdir(parents=True, exist_ok=True)
xml = zdroje / f'{ident}_djvu.xml'
if not xml.exists():
    xml.write_bytes(urllib.request.urlopen(f'https://archive.org/download/{ident}/{ident}_djvu.xml', timeout=120).read())
s = xml.read_text(encoding='utf-8')
out = zdroje / 'ocr_ia'
out.mkdir(exist_ok=True)
n = 0
for obj in re.findall(r'<OBJECT.*?</OBJECT>', s, flags=re.S):
    m = re.search(r'usemap="[^"]*_(\d+)\.djvu"', obj)
    if not m:
        continue
    radky = [' '.join(html.unescape(w) for w in re.findall(r'<WORD[^>]*>([^<]*)</WORD>', l))
             for l in re.findall(r'<LINE>(.*?)</LINE>', obj, flags=re.S)]
    (out / f'{int(m.group(1)):04d}.txt').write_text('\n'.join(radky), encoding='utf-8')
    n += 1
print('stran OCR:', n)
