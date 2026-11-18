"""Solms: založí kostry stran Šesté až Deváté knihy (skeny 491–681) a stáhne obrázkové strany ze skenu BSB.

Foliace (ověřeno podle čísel listů v OCR): sudé skeny jsou rubové strany, liché lícové.
  6. kniha: titul 491, list N r = 491 + 2N (1r = 493 … 27r = 545)
  7. kniha: erb 546 (rub 6-027r), titul 547, list N r = 547 + 2N (1r = 549 … 18r = 583)
  8. kniha: erb 585, titul 587, list N r = 587 + 2N (1r = 589 … 14v = 616)
  9. kniha: erb 617, titul 619, list N r = 619 + 2N (1r = 621 … 30v = 680); erb 681 na konci svazku
Prázdné strany (jen prosvítání protější sazby) se nezakládají: 492, 548, 584, 586, 588, 618, 620; 682–687 (prázdné listy, deska).
Strany vznikají ve stavu chybi_original (bloky doplní překladatel podle OCR a skenu); obrázkové strany mají připravený blok obrazek.

Použití: python -I nastroje/solms_kostry_6_9.py   (existující strany nepřepisuje)
"""
import pathlib, sys, time, urllib.request
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from import_md import dump

K = pathlib.Path(__file__).resolve().parent.parent / 'knihy' / 'solms-1559'
PRAZDNE = {492, 548, 584, 586, 588, 618, 620}
OBRAZKY = {491, 546, 547, 555, 556, 557, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 585, 587, 610, 617, 619, 681}
KNIHY = [  # (kniha, první sken, poslední sken, sken titulu, zvláštní strany {sken: (id, list, frontispis)})
    (6, 491, 545, 491, {}),
    (7, 546, 584, 547, {546: ('7-erb-solms', 'předsádka (7. kniha)', True)}),
    (8, 585, 616, 587, {585: ('8-erb-solms', 'předsádka (8. kniha)', True)}),
    (9, 617, 681, 619, {617: ('9-erb-solms', 'předsádka (9. kniha)', True),
                        681: ('9-erb-konec', 'erbovní list na konci svazku', False)}),
]


def stahni(sken):
    f = K / 'obrazky' / f'drevorez-{sken}.jpg'
    if f.exists():
        return
    url = f'https://api.digitale-sammlungen.de/iiif/image/v2/bsb00085168_{sken:05d}/full/1400,/0/default.jpg'
    f.write_bytes(urllib.request.urlopen(url, timeout=60).read())
    time.sleep(0.3)


nove = 0
for kniha, od, do, titul, zvlast in KNIHY:
    for sken in range(od, do + 1):
        if sken in PRAZDNE:
            continue
        frontispis = False
        if sken in zvlast:
            pid, lst, frontispis = zvlast[sken]
            strana = 'verso' if sken % 2 == 0 else 'recto'
        elif sken == titul:
            pid, lst, strana = f'{kniha}-titul', f'titulní list ({kniha}. kniha)', 'recto'
        else:
            n, zb = divmod(sken - titul, 2)          # titul + 2N = N r, titul + 2N + 1 = N v
            strana = 'recto' if zb == 0 else 'verso'
            pid = f'{kniha}-{n:03d}{"r" if zb == 0 else "v"}'
            lst = f'{n} ({kniha}. kniha)'
        f = K / 'strany' / f'{pid}.yaml'
        if f.exists():
            continue
        d = {'id': pid, 'list': lst, 'strana': strana, 'sken': sken}
        if frontispis:
            d['frontispis'] = True
        d.update(stav='chybi_original', overeno_clovekem=False, bloky=[])
        if sken in OBRAZKY:
            stahni(sken)
            d['bloky'] = [{'typ': 'obrazek', 'soubor': f'drevorez-{sken}.jpg', 'popis': ''}]
        dump(d, f)
        nove += 1
print('založeno stran:', nove)
