"""Vyřízne dřevořezy ze skenů BSB pro bloky `typ: obrazek, soubor: drevorez-<sken>[b].jpg`, které ještě nemají soubor.

Princip: z hOCR skenu se vezmou obdélníky řádků textu; největší svislá mezera mezi nimi (bez textu) je vyobrazení.
Výřez se stáhne přímo z IIIF serveru (region x,y,w,h) – není potřeba knihovna na obrázky.
Druhý obrázek na téže straně (…b.jpg) = druhá největší mezera. Výsledek vždy zkontroluj okem
(ruční oprava: parametr --region sken:x,y,w,h, souřadnice v pixelech plného skenu).

Použití: python -I nastroje/vyrez_drevorezy.py knihy/fronsberger-1564 [--prepsat] [--region 16:120,400,1900,1800]
"""
import json, re, sys, time, pathlib, urllib.request
import yaml

MIN_MEZERA = 250  # px v plném rozlišení skenu


def hocr_radky(bsb, sken):
    url = f'https://api.digitale-sammlungen.de/ocr/{bsb}/{sken}'
    s = urllib.request.urlopen(url, timeout=60).read().decode('utf-8')
    page = re.search(r"ocr_page[^>]*bbox 0 0 (\d+) (\d+)", s)
    w, h = int(page.group(1)), int(page.group(2))
    radky = [tuple(map(int, m)) for m in re.findall(r"class=.ocr_line. title=.bbox (\d+) (\d+) (\d+) (\d+)", s)]
    # šum OCR uvnitř obrázku: krátké „řádky“ (1–2 znaky) mají malou šířku – vynech
    radky = [r for r in radky if (r[2] - r[0]) > w * 0.12 and (r[3] - r[1]) < 140]
    return w, h, sorted(radky, key=lambda r: r[1])


def mezery(w, h, radky):
    okraj_h, okraj_d = int(h * 0.05), int(h * 0.96)
    ys = [(okraj_h, okraj_h)] + [(r[1], r[3]) for r in radky] + [(okraj_d, okraj_d)]
    out = []
    for (a1, a2), (b1, b2) in zip(ys, ys[1:]):
        if b1 - a2 >= MIN_MEZERA:
            out.append((a2 + 10, b1 - 10))
    return sorted(out, key=lambda g: -(g[1] - g[0]))


def main():
    kniha = pathlib.Path(sys.argv[1])
    prepsat = '--prepsat' in sys.argv
    rucne = {}
    for a in sys.argv:
        if a.startswith('--region'):
            pass
    if '--region' in sys.argv:
        for spec in sys.argv[sys.argv.index('--region') + 1].split(';'):
            k, v = spec.split(':')
            rucne[k] = v
    meta = yaml.safe_load((kniha / 'kniha.yaml').read_text(encoding='utf-8'))
    bsb = meta['sken']['id']
    man = json.loads((kniha / 'zdroje' / f'manifest_{bsb}.json').read_text(encoding='utf-8'))
    rozmer = {i: (c['width'], c['height']) for i, c in enumerate(man['sequences'][0]['canvases'], 1)}
    potreba = {}
    for f in sorted((kniha / 'strany').glob('*.yaml')):
        d = yaml.safe_load(f.read_text(encoding='utf-8'))
        for b in d.get('bloky') or []:
            m = re.fullmatch(r'drevorez-(\d+)(b?)\.jpg', str(b.get('soubor', '')))
            if b.get('typ') == 'obrazek' and m:
                cil = kniha / 'obrazky' / b['soubor']
                if prepsat or not cil.exists():
                    potreba.setdefault(int(m.group(1)), []).append((m.group(2), cil))
    for sken, cile in sorted(potreba.items()):
        try:
            w, h, radky = hocr_radky(bsb, sken)
        except Exception as e:
            print(f'sken {sken}: hOCR nedostupné ({e})')
            continue
        gaps = mezery(w, h, radky)
        for suffix, cil in sorted(cile):
            klic = f'{sken}{suffix}'
            if klic in rucne:
                region = rucne[klic]
            else:
                k = 1 if suffix == 'b' else 0
                if k >= len(gaps):
                    print(f'{cil.name}: nenalezena mezera bez textu – zadej --region {klic}:x,y,w,h')
                    continue
                y1, y2 = gaps[k]
                if suffix == '' and len(gaps) > 1:  # pořadí shora dolů
                    y1, y2 = sorted(gaps[:2])[0] if any(c[0] == 'b' for c in cile) else (y1, y2)
                elif suffix == 'b':
                    y1, y2 = sorted(gaps[:2])[1]
                # hOCR může mít jiné rozlišení než obrázek IIIF → přepočet
                kw, kh = rozmer.get(sken, (w, h))
                sx, sy = kw / w, kh / h
                x1, x2 = int(kw * 0.06), int(kw * 0.94)
                region = f'{x1},{int(y1 * sy)},{x2 - x1},{int((y2 - y1) * sy)}'
            url = f'https://api.digitale-sammlungen.de/iiif/image/v2/{bsb}_{sken:05d}/{region}/1000,/0/default.jpg'
            try:
                cil.write_bytes(urllib.request.urlopen(url, timeout=60).read())
                print(f'{cil.name}: region {region}')
            except Exception as e:
                print(f'{cil.name}: stažení selhalo ({e})')
            time.sleep(0.3)


if __name__ == '__main__':
    main()
