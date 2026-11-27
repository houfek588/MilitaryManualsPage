"""Založí prázdné strany knihy (stav chybi_original) podle čísel snímků – pro knihu bez pracovního překladu.

Převod snímek → strana tisku zadáš snímkem prvního listu / první strany (`--prvni`). Číslování bere z kniha.yaml:
  strankovani: folio   → list N r = snímek  prvni + 2(N−1), list N v = o snímek dál; id 001r, 001v …, list '[N] r'
                         listy od `--foliace-od` mají číslo z tisku bez závorek ('12' → fol. 12 r)
  strankovani: strany  → strana N = snímek prvni + (N−1); id 001, 002 …
Snímek titulního listu (`--titul`) dostane id `titul`. Prázdné snímky, desky a měřítko vynech (`--vynech`).
Existující strany nepřepisuje. Nejdřív spusť se `--zkouska` a ověř převod na několika místech podle skenu.

Použití:
  python -I nastroje/zaloz_strany.py knihy/<kniha> --od 5 --do 115 --prvni 5 --titul 5 [--foliace-od 5] [--vynech 2,84] [--zkouska]
"""
import argparse, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import yaml
from import_md import dump

ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
ap.add_argument('kniha', help='složka knihy, např. knihy/ott-1530')
ap.add_argument('--od', type=int, required=True, help='první zakládaný snímek')
ap.add_argument('--do', type=int, required=True, help='poslední zakládaný snímek')
ap.add_argument('--prvni', type=int, required=True, help='snímek listu [1] r (folio) nebo strany 1 (strany)')
ap.add_argument('--titul', type=int, help='snímek titulního listu (id `titul`)')
ap.add_argument('--foliace-od', type=int, help='první list s tištěným (arabským) číslem; dřívější listy jsou [N]')
ap.add_argument('--predpona', default='', help='předpona id (např. u → u001r) pro nečíslovaný úvod před foliovanou částí')
ap.add_argument('--vynech', default='', help='snímky, které se nezakládají (čárkami: 2,84)')
ap.add_argument('--zkouska', action='store_true', help='jen vypsat, nic nezapisovat')
a = ap.parse_args()
sys.stdout.reconfigure(encoding="utf-8")

K = pathlib.Path(a.kniha)
meta = yaml.safe_load((K / 'kniha.yaml').read_text(encoding='utf-8'))
folio = meta.get('strankovani', 'folio') != 'strany'
vynech = {int(x) for x in a.vynech.split(',') if x.strip()}
(K / 'strany').mkdir(exist_ok=True)

nove = existuje = 0
for sken in range(a.od, a.do + 1):
    if sken in vynech:
        continue
    d = sken - a.prvni
    if d < 0 and sken != a.titul:
        sys.exit(f'snímek {sken} je před prvním listem ({a.prvni}) – předsádku založ ručně (id např. predmluva-1) nebo uprav --od')
    if folio:
        n, zb = divmod(d, 2)
        n += 1
        strana = 'recto' if zb == 0 else 'verso'
        pid = f'{a.predpona}{n:03d}{"r" if zb == 0 else "v"}'
        lst = str(n) if a.foliace_od and n >= a.foliace_od else f'[{n}] {"r" if zb == 0 else "v"}'
    else:
        n = d + 1
        strana = 'recto' if n % 2 else 'verso'
        pid, lst = f'{a.predpona}{n:03d}', str(n)
    if sken == a.titul:
        pid, lst = 'titul', f'titulní list {lst}' if folio else 'titulní list'
    f = K / 'strany' / f'{pid}.yaml'
    if f.exists():
        existuje += 1
        continue
    if a.zkouska:
        print(f'snímek {sken:4d} → {pid:6s} ({lst}, {strana})')
    else:
        dump(dict(id=pid, list=lst, strana=strana, sken=sken, stav='chybi_original', overeno_clovekem=False, bloky=[]), f)
    nove += 1
print(f'{"k založení" if a.zkouska else "založeno"} stran: {nove}, už existuje: {existuje}')
