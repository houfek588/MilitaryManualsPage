"""Kontrola datových souborů stran (struktura, párování, poznámky, terminologie).

Použití:
  python -I nastroje/over_strany.py knihy/fronsberger-1564            # všechny strany
  python -I nastroje/over_strany.py knihy/fronsberger-1564 018r 018v  # vybrané
  … --prisne   # u stran se stavem prelozeno/zkontrolovano hlásí i varování terminologie
Výstup: CHYBA = musí se opravit; VAROVÁNÍ = zkontroluj.
"""
import re, sys, pathlib
import yaml

TYPY = {'nadpis', 'odstavec', 'seznam', 'verse', 'obrazek', 'tabulka'}
STAVY = {'chybi_original', 'chybi_preklad', 'castecne', 'prelozeno', 'zkontrolovano'}


def text_of(v):
    if v is None:
        return ''
    if isinstance(v, list):
        return ' '.join(text_of(x) for x in v)
    return str(v)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    prisne = '--prisne' in sys.argv
    sys.stdout.reconfigure(encoding='utf-8')
    kniha = pathlib.Path(args[0])
    ids = args[1:]
    glos = yaml.safe_load((kniha / 'glosar.yaml').read_text(encoding='utf-8'))
    zakaz = [(re.compile(r'\b' + re.escape(x) + r'\b', re.I), h['cs']) for h in glos['hesla'] for x in h.get('nepouzivat', [])]
    files = [kniha / 'strany' / f'{i}.yaml' for i in ids] if ids else sorted((kniha / 'strany').glob('*.yaml'))
    n_err = n_warn = 0
    for f in files:
        errs, warns = [], []
        try:
            d = yaml.safe_load(f.read_text(encoding='utf-8'))
        except Exception as e:
            print(f'{f.stem}: CHYBA YAML: {e}')
            n_err += 1
            continue
        if d.get('id') != f.stem:
            errs.append(f'id {d.get("id")} ≠ název souboru')
        if d.get('stav') not in STAVY:
            errs.append(f'neznámý stav {d.get("stav")}')
        ov = d.get('overeno_clovekem')
        if ov not in (True, False):
            errs.append('chybí nebo je neplatné pole overeno_clovekem (true/false)')
        elif ov and d.get('stav') != 'zkontrolovano':
            warns.append(f'overeno_clovekem: true, ale stav je {d.get("stav")}')
        elif ov and not d.get('overeno_datum'):
            warns.append('overeno_clovekem: true bez overeno_datum')
        hotovo = d.get('stav') in ('prelozeno', 'zkontrolovano')
        refs = set()
        for k, b in enumerate(d.get('bloky') or [], 1):
            t = b.get('typ')
            if t not in TYPY:
                errs.append(f'blok {k}: neznámý typ {t}')
                continue
            if t == 'obrazek':
                if not (kniha / 'obrazky' / str(b.get('soubor'))).exists():
                    if str(b.get('soubor', '')).startswith('drevorez-'):
                        pass  # výřez ze skenu doplní správce projektu
                    else:
                        errs.append(f'blok {k}: obrázek {b.get("soubor")} neexistuje')
                if hotovo and not b.get('popis'):
                    warns.append(f'blok {k}: obrázek bez popisu')
                continue
            de, cs = b.get('de'), b.get('cs')
            if b.get('zarovnat'):
                (errs if hotovo and d['stav'] == 'zkontrolovano' else warns).append(f'blok {k}: zarovnat: true (nespárováno)')
            if hotovo and not cs:
                errs.append(f'blok {k}: chybí cs')
            if not de and d.get('stav') != 'chybi_original':
                errs.append(f'blok {k}: chybí de')
            if t == 'nadpis' and b.get('uroven') not in (1, 2, 3):
                errs.append(f'blok {k}: nadpis bez úrovně 1–3')
            if t in ('seznam', 'verse', 'tabulka'):
                if de is not None and not isinstance(de, list) or cs is not None and not isinstance(cs, list):
                    errs.append(f'blok {k}: {t} musí mít de i cs jako seznam')
                elif de and cs and len(de) != len(cs):
                    warns.append(f'blok {k}: {t} má DE {len(de)} a CS {len(cs)} položek')
            ct = text_of(cs)
            refs |= {int(x) for x in re.findall(r'\[\^(\d+)\]', ct)}
            if re.search(r'\}\*', ct):
                errs.append(f'blok {k}: nevyřešená značka {{…}}* (poznámka)')
            if '...' in ct or ct.strip().startswith('…') or ct.strip().endswith('…'):
                warns.append(f'blok {k}: „...“/„…“ na hranici – pokračování má být pokracovani: true')
            if re.search(r'[*\\]', text_of(de)):
                warns.append(f'blok {k}: v de zůstalo * nebo \\')
            if de and cs and t == 'odstavec':
                r = len(ct) / max(1, len(text_of(de)))
                if r < 0.55 or r > 1.9:
                    warns.append(f'blok {k}: nepoměr délek CS/DE {r:.2f} – chybí nebo přebývá text?')
            if hotovo and (prisne or d['stav'] == 'zkontrolovano'):
                ct_bez = re.sub(r'\{[^}]*\}', ' ', ct)
                for rx, spr in zakaz:
                    m = rx.search(ct_bez)
                    if m:
                        warns.append(f'blok {k}: „{m.group(0)}“ → podle glosáře „{spr}“')
            if re.search(r'\bf(oll|ift|ein)\b', text_of(de)):
                warns.append(f'blok {k}: v de možná chyba OCR (foll/ift/fein)')
        notes = {int(n['n']) for n in d.get('poznamky') or []}
        if refs - notes:
            errs.append(f'odkaz na neexistující poznámku {sorted(refs - notes)}')
        if notes - refs:
            warns.append(f'poznámka bez odkazu v textu {sorted(notes - refs)}')
        for e in errs:
            print(f'{f.stem}: CHYBA {e}')
        for w in warns:
            print(f'{f.stem}: VAROVÁNÍ {w}')
        n_err += len(errs)
        n_warn += len(warns)
    print(f'— {len(files)} stran, {n_err} chyb, {n_warn} varování')
    sys.exit(1 if n_err else 0)


if __name__ == '__main__':
    main()
