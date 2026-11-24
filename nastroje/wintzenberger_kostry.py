"""Wintzenberger, Beschreibung einer Kriegs-Ordnung (Drážďany 1588): kostry stran ze skenu BSB bsb00032546.

List [N] r = sken 2N + 3, [N] v = sken 2N + 4; titul = sken 5. Skeny 1–4 a 116–120 (desky, měřítko, prázdné) se
nezakládají. Strany vznikají ve stavu chybi_original – přepis a překlad doplní agent podle OCR a skenu.
Použití: python -I nastroje/wintzenberger_kostry.py   (existující strany nepřepisuje)
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from import_md import dump

K = pathlib.Path(__file__).resolve().parent.parent / 'knihy' / 'wintzenberger-1588' / 'strany'
nove = 0
for sken in range(5, 116):
    n, zb = divmod(sken - 3, 2)          # sken 5 → list 1 r, 6 → 1 v
    strana = 'recto' if zb == 0 else 'verso'
    pid = 'titul' if sken == 5 else f'{n:03d}{"r" if zb == 0 else "v"}'
    lst = 'titulní list [1] r' if sken == 5 else f'[{n}] {"r" if zb == 0 else "v"}'
    f = K / f'{pid}.yaml'
    if f.exists():
        continue
    dump(dict(id=pid, list=lst, strana=strana, sken=sken, stav='chybi_original', overeno_clovekem=False, bloky=[]), f)
    nove += 1
print('založeno stran:', nove)
