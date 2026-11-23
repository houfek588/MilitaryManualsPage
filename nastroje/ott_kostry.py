"""Ott von Echterdingen, Kriegsordnung (kolem 1530): založí kostry stran ze skenu BSB bsb00089558.

List [N] r = sken 2N−1, [N] v = sken 2N. Sken 1 = titulní list (id `titul`), skeny 2 a 84 jsou prázdné.
Strany vznikají ve stavu chybi_original s prázdnými bloky – přepis a překlad doplní agent podle OCR a skenu.
Použití: python -I nastroje/ott_kostry.py   (existující strany nepřepisuje)
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from import_md import dump

K = pathlib.Path(__file__).resolve().parent.parent / 'knihy' / 'ott-1530' / 'strany'
PRAZDNE = {2, 84}
nove = 0
for sken in range(1, 85):
    if sken in PRAZDNE:
        continue
    n, zb = divmod(sken + 1, 2)            # sken 1 → list 1 r, sken 3 → list 2 r, sken 4 → list 2 v
    strana = 'recto' if zb == 0 else 'verso'
    pid = 'titul' if sken == 1 else f'{n:03d}{"r" if zb == 0 else "v"}'
    lst = 'titulní list [1] r' if sken == 1 else f'[{n}] {"r" if zb == 0 else "v"}'
    f = K / f'{pid}.yaml'
    if f.exists():
        continue
    dump(dict(id=pid, list=lst, strana=strana, sken=sken, stav='chybi_original', overeno_clovekem=False, bloky=[]), f)
    nove += 1
print('založeno stran:', nove)
