"""Označí strany jako ověřené člověkem (ruční kontrola překladu), nebo označení zruší.

Použití:
  python -I nastroje/overeno_clovekem.py knihy/fronsberger-1564 001r 001v 002r          # označit
  python -I nastroje/overeno_clovekem.py knihy/fronsberger-1564 001r-010v --kdo "J. Novák"  # rozsah stran + jméno
  python -I nastroje/overeno_clovekem.py knihy/fronsberger-1564 004v --zrusit             # zrušit označení
  python -I nastroje/overeno_clovekem.py knihy/fronsberger-1564 --prehled                 # kolik je ověřeno

V souboru strany nastaví:
  overeno_clovekem: true
  overeno_datum: 'RRRR-MM-DD'
  overeno_kdo: jméno            (jen s --kdo)
Ostatní obsah souboru zůstane beze změny. Strana by měla mít stav `zkontrolovano`; jinak skript varuje.
"""
import datetime, re, sys, pathlib
import yaml


def poradi(kniha):
    meta = yaml.safe_load((kniha / 'kniha.yaml').read_text(encoding='utf-8'))
    front = meta.get('predsadka', [])
    ids = [f.stem for f in (kniha / 'strany').glob('*.yaml')]
    return sorted(ids, key=lambda i: (0, front.index(i)) if i in front else (1, int(i[:3]) * 2 + (i[3] == 'v')))


def rozbal(args, vse):
    out = []
    for a in args:
        if '-' in a and a.split('-')[0] in vse and a.split('-', 1)[1] in vse:
            od, do = a.split('-', 1)
            out += vse[vse.index(od):vse.index(do) + 1]
        elif a in vse:
            out.append(a)
        else:
            sys.exit(f'Neznámá strana: {a}')
    return out


def nastav(text, pole, hodnota):
    """Nahradí řádek `pole: …`, nebo ho vloží za řádek overeno_clovekem / stav."""
    nl = '\r\n' if '\r\n' in text else '\n'
    radek = f'{pole}: {hodnota}'
    if re.search(rf'^{pole}: .*$', text, flags=re.M):
        return re.sub(rf'^{pole}: [^\r\n]*', radek, text, count=1, flags=re.M)
    kotva = 'overeno_clovekem' if pole != 'overeno_clovekem' else 'stav'
    return re.sub(rf'^({kotva}: [^\r\n]*)', lambda m: m.group(1) + nl + radek, text, count=1, flags=re.M)


def smaz(text, pole):
    return re.sub(rf'^{pole}: [^\r\n]*\r?\n', '', text, flags=re.M)


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:]
    kniha = pathlib.Path(a.pop(0))
    vse = poradi(kniha)
    if '--prehled' in a:
        ov = [i for i in vse if yaml.safe_load((kniha / 'strany' / f'{i}.yaml').read_text(encoding='utf-8')).get('overeno_clovekem')]
        print(f'Ověřeno člověkem: {len(ov)} z {len(vse)} stran')
        if ov:
            print(' '.join(ov))
        return
    zrusit = '--zrusit' in a
    kdo = None
    if '--kdo' in a:
        k = a.index('--kdo')
        kdo = a[k + 1]
        del a[k:k + 2]
    strany = rozbal([x for x in a if not x.startswith('--')], vse)
    dnes = datetime.date.today().isoformat()
    for pid in strany:
        f = kniha / 'strany' / f'{pid}.yaml'
        t = f.read_bytes().decode('utf-8')
        if zrusit:
            t = nastav(t, 'overeno_clovekem', 'false')
            t = smaz(smaz(t, 'overeno_datum'), 'overeno_kdo')
        else:
            stav = yaml.safe_load(t).get('stav')
            if stav != 'zkontrolovano':
                print(f'{pid}: VAROVÁNÍ – stav je „{stav}“, ne „zkontrolovano“')
            t = nastav(t, 'overeno_clovekem', 'true')
            t = nastav(t, 'overeno_datum', f"'{dnes}'")
            if kdo:
                t = nastav(t, 'overeno_kdo', f"'{kdo}'")
        yaml.safe_load(t)  # pojistka: soubor musí zůstat platný
        f.write_bytes(t.encode('utf-8'))
        print(f'{pid}: {"označení zrušeno" if zrusit else "ověřeno člověkem"}')


if __name__ == '__main__':
    main()
