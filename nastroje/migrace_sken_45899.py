"""Jednorázová migrace edice Fronsperger 1564 z neúplného skenu bsb10150061 na úplný sken bsb00045899.

bsb10150061 (= Google Books 7aBMAAAAcAAJ) vynechává tři dvojstrany: XXXVIII v + XXXIX r, LVIII v + LIX r,
LXVIII v + LXIX r. Pracovní překlad proto měl rub následujícího listu pod chybným číslem.
V bsb00045899 platí bez výjimky: list N r = sken 7 + 2N, list N v = sken 8 + 2N.

Kroky: 038v→039v, 058v→059v, 068v→069v (obsah je rub následujícího listu); nové prázdné strany
038v, 039r, 058v, 059r, 068v, 069r; přepočet `sken` u všech stran; přejmenování drevorez-<starý sken>.jpg.
"""
import pathlib, re, shutil, sys
import yaml
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from import_md import dump

KNIHA = pathlib.Path(__file__).resolve().parent.parent / 'knihy' / 'fronsberger-1564'
S = KNIHA / 'strany'
PREDSADKA = {'titul': 1, 'venovani-1': 3, 'venovani-2': 4, 'predmluva-1': 5, 'predmluva-2': 6}
ROMAN = [(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IIII'), (1, 'I')]


def roman(n):
    s = ''
    for v, r in ROMAN:
        while n >= v:
            s += r; n -= v
    return s


def novy_sken(pid):
    if pid in PREDSADKA:
        return PREDSADKA[pid]
    return 7 + 2 * int(pid[:3]) + (pid[3] == 'v')


def stary_na_novy(c):
    """číslo skenu v bsb10150061 → bsb00045899"""
    if c <= 83:
        return c
    if c <= 121:
        return c + 2
    if c <= 139:
        return c + 4
    return c + 6


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    for stary, novy in (('038v', '039v'), ('058v', '059v'), ('068v', '069v')):
        src, dst = S / f'{stary}.yaml', S / f'{novy}.yaml'
        assert src.exists() and not dst.exists(), (src, dst)
        d = yaml.safe_load(src.read_text(encoding='utf-8'))
        d['id'], d['list'] = novy, roman(int(novy[:3]))
        dump(d, dst)
        src.unlink()
        print(f'{stary} → {novy}')
    for pid in ('038v', '039r', '058v', '059r', '068v', '069r'):
        dump(dict(id=pid, list=roman(int(pid[:3])), strana='verso' if pid[3] == 'v' else 'recto',
                  sken=novy_sken(pid), stav='chybi_original', overeno_clovekem=False, bloky=[]), S / f'{pid}.yaml')
        print(f'nová prázdná strana {pid}')
    prejmenovat = {}
    for f in sorted(S.glob('*.yaml')):
        d = yaml.safe_load(f.read_text(encoding='utf-8'))
        zmena = False
        if d.get('sken') != novy_sken(d['id']):
            d['sken'] = novy_sken(d['id'])
            zmena = True
        for b in d.get('bloky') or []:
            m = re.fullmatch(r'drevorez-(\d+)(b?)\.jpg', str(b.get('soubor', '')))
            if m:
                nove = f'drevorez-{stary_na_novy(int(m.group(1)))}{m.group(2)}.jpg'
                if nove != b['soubor']:
                    prejmenovat[b['soubor']] = nove
                    b['soubor'] = nove
                    zmena = True
        if zmena:
            dump(d, f)
    for a, b in prejmenovat.items():
        if (KNIHA / 'obrazky' / a).exists():
            shutil.move(KNIHA / 'obrazky' / a, KNIHA / 'obrazky' / b)
    print('dřevořezy přečíslovány:', prejmenovat)
    # kontrola: sken musí sedět s popiskem v manifestu (recto má římské číslo v OCR záhlaví)


if __name__ == '__main__':
    main()
