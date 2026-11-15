"""Jednorázový import pracovního překladu Lavaterova Kriegs-Büchlein (export Google Docs .md) do YAML stran.

Použití: python -I nastroje/import_lavater.py
Vstup:  Lavater/Lavater, Hans Conrad_ Kriegs-Büchlein.md, knihy/lavater-1651/zdroje/dta/*.txt (viz dta_strany.py)
Výstup: knihy/lavater-1651/strany/<id>.yaml, obrazky/, zdroje/import_report.txt

Id stran: 001–134 (stránkování tisku); předsádka a tabule s mědirytinami viz PREDSADKA a TABULE.
`sken` = číslo snímku DTA (z <pb n= facs=> v TEI). Strany, které v pracovním překladu chybějí,
se založí prázdné (stav chybi_original) – text doplní překladatel podle zdroje/dta.
"""
import base64, re, sys, pathlib
from collections import Counter
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import import_md as IM   # sdílené pomůcky: parse_blocks, lang, bracket_terms, gale_church, merge, dump
from dta_strany import normalizuj

KOREN = pathlib.Path(__file__).resolve().parent.parent
MD = KOREN / 'Lavater' / 'Lavater, Hans Conrad_ Kriegs-Büchlein.md'
KNIHA = KOREN / 'knihy' / 'lavater-1651'

# předsádka a závěr: id → (popis, číslo snímku)
PREDSADKA = [('frontispis', 'frontispis', 1), ('titul', 'titulní list', 3), ('vazba', 'pokyn knihaři', 4),
             ('venovani', 'věnování', 5), ('predmluva-1', 'věnování (předmluva)', 6), ('predmluva-2', 'věnování (předmluva)', 7),
             ('predmluva-3', 'věnování (předmluva)', 8), ('vyklad-1', 'výklad cizích slov', 9), ('vyklad-2', 'výklad cizích slov', 10),
             ('vyklad-3', 'výklad cizích slov', 11), ('vyklad-4', 'výklad cizích slov', 12),
             ('slovnicek-1', 'slovníček', 13), ('slovnicek-2', 'slovníček', 14),
             ('basne-1', 'básně', 15), ('basne-2', 'básně', 16), ('basne-3', 'básně', 17), ('basne-4', 'básně', 18)]
TABULE = [('tab-01', 20), ('tab-02', 22), ('tab-03', 24), ('tab-04', 27), ('tab-05', 30), ('tab-06', 33),
          ('tab-07', 116), ('tab-08', 118), ('tab-09', 120), ('tab-10', 121), ('tab-11', 123), ('tab-12', 125)]
ZAVER = [('errata', 'tiskové chyby', 181)]


def cisla_stran():
    """číslo strany → snímek, z hlaviček zdroje/dta/NNNN.txt"""
    out = {}
    for f in (KNIHA / 'zdroje' / 'dta').glob('*.txt'):
        m = re.match(r'# strana (\d+)\b', f.read_text(encoding='utf-8'))
        if m:
            out[int(m.group(1))] = int(f.stem)
    return out


def kulate_terminy(s):
    """(Brustwehr) → {Brustwehr}: německé termíny v kulatých závorkách v českém textu."""
    def rep(m):
        inner = m.group(1).strip()
        if any(c in IM.CZ for c in inner) or any(c in IM.CZ_SOFT for c in inner) or re.search(r'\d', inner):
            return m.group(0)
        if len(inner.split()) > 6:
            return m.group(0)
        if re.search(r'(ß|ſ|[äöüÄÖÜ]|ey|ck|tz|th|ff|sch|^[A-Z][a-zäöü]+(\s|$))', inner):
            return '{' + inner + '}'
        return m.group(0)
    return re.sub(r'\(([^()]{2,80})\)', rep, s)


def roman(n):
    return str(n)


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    lines = MD.read_text(encoding='utf-8').split('\n')
    (KNIHA / 'obrazky').mkdir(parents=True, exist_ok=True)
    (KNIHA / 'strany').mkdir(parents=True, exist_ok=True)
    images = {}
    for l in lines:
        m = re.match(r'^\[(image\d+)\]: <data:image/(\w+);base64,(.*)>$', l)
        if m:
            fn = f'prekladatel-{m.group(1)}.{m.group(2)}'
            (KNIHA / 'obrazky' / fn).write_bytes(base64.b64decode(m.group(3)))
            images[m.group(1)] = fn
    end = next(i for i, l in enumerate(lines) if l.startswith('[image1]:'))
    body = lines[:end]
    pg_re = re.compile(r'^#### \*\*\*str\. (\d+)')
    pages, cur = {}, None
    for l in body:
        m = pg_re.match(l.strip())
        if m:
            cur = int(m.group(1))
            pages[cur] = []
            continue
        if cur is not None:
            if l.strip() in ('####', '#', '##', '###'):
                continue
            pages[cur].append(l)

    sken = cisla_stran()
    report, starred = [], Counter()
    vystup = []
    for n in range(1, 135):
        pid = f'{n:03d}'
        lines_p = pages.get(n)
        zaklad = dict(id=pid, list=str(n), strana='recto' if n % 2 else 'verso', sken=sken[n])
        if not lines_p:
            vystup.append(dict(zaklad, stav='chybi_original', overeno_clovekem=False, bloky=[]))
            report.append(f'{pid}: v pracovním překladu chybí (text je pravděpodobně sloučen se sousední stranou)')
            continue
        lines_p = [re.sub(r'\s*\{#[^}]*\}', '', l) for l in lines_p]   # kotvy nadpisů z Google Docs
        blocks = IM.parse_blocks(lines_p)
        last = 'de'
        for b in blocks:
            if b['typ'] == 'obrazek':
                b['lang'] = None
                continue
            lg = IM.lang(IM.block_text(b), b.get('italic', False)) or last
            b['lang'] = lg
            last = lg
        for b in blocks:
            if b.get('lang') == 'cs':
                for key in ('text',):
                    if key in b:
                        b[key] = kulate_terminy(IM.bracket_terms(b[key], starred))
                for key in ('polozky', 'radky'):
                    if key in b:
                        b[key] = [kulate_terminy(IM.bracket_terms(x, starred)) for x in b[key]]
            elif b.get('lang') == 'de':
                for key in ('text',):
                    if key in b:
                        b[key] = normalizuj(b[key])
                for key in ('polozky', 'radky'):
                    if key in b:
                        b[key] = [normalizuj(x) for x in b[key]]
        # párování po úsecích DE → CS (stejně jako u Fronspergera)
        out, warn = [], []
        de_run, cs_run, state = [], [], None

        def segment(de_run, cs_run):
            res = []
            dh = [k for k, b in enumerate(de_run) if b['typ'] == 'nadpis']
            ch = [k for k, b in enumerate(cs_run) if b['typ'] == 'nadpis']
            if len(dh) != len(ch):
                warn.append(f'nadpisy DE {len(dh)} / CS {len(ch)}')
            pairs = IM.gale_church(de_run, cs_run) if de_run and cs_run else (
                [([k], []) for k in range(len(de_run))] + [([], [k]) for k in range(len(cs_run))])
            for di, ci in pairs:
                dv, dt = IM.merge([de_run[k] for k in di]) if di else (None, None)
                cv, ct = IM.merge([cs_run[k] for k in ci]) if ci else (None, None)
                typ = dt or ct
                if dt and ct and dt != ct:
                    typ = 'nadpis' if 'nadpis' in (dt, ct) and len(di) == len(ci) == 1 else 'odstavec'
                    if isinstance(dv, list): dv = '\n'.join('- ' + x for x in dv)
                    if isinstance(cv, list): cv = '\n'.join('- ' + x for x in cv)
                pair = dict(typ=typ, de=dv, cs=cv)
                if typ == 'nadpis':
                    pair = dict(typ='nadpis', uroven=min(3, max(1, (de_run[di[0]] if di else cs_run[ci[0]]).get('uroven', 2))), de=dv, cs=cv)
                if len(di) != 1 or len(ci) != 1:
                    pair['zarovnat'] = True
                res.append(pair)
            return res

        for b in blocks + [dict(typ='konec', lang='konec')]:
            if b['typ'] == 'obrazek':
                out += segment(de_run, cs_run) if (de_run or cs_run) else []
                de_run, cs_run, state = [], [], None
                out.append(dict(typ='obrazek', soubor=images.get(b['obrazek'], b['obrazek'])))
                continue
            if b['typ'] == 'konec':
                if de_run or cs_run:
                    out += segment(de_run, cs_run)
                break
            if b['lang'] == 'de':
                if state == 'cs':
                    out += segment(de_run, cs_run)
                    de_run, cs_run = [], []
                de_run.append(b)
                state = 'de'
            else:
                cs_run.append(b)
                state = 'cs'
        stav = 'prelozeno' if any(b.get('cs') for b in out) else 'chybi_preklad'
        vystup.append(dict(zaklad, stav=stav, overeno_clovekem=False, bloky=out))
        if warn:
            report.append(f'{pid}: ' + '; '.join(warn))
        if n in (81, 84):
            report.append(f'{pid}: obsahuje text více stran tisku (82, 83, 85 chybí) – rozdělit podle zdroje/dta')

    for pid, popis, sk in PREDSADKA + ZAVER:
        vystup.append(dict(id=pid, list=popis, strana='recto' if sk % 2 else 'verso', sken=sk,
                           stav='chybi_original', overeno_clovekem=False, bloky=[]))
    for i, (pid, sk) in enumerate(TABULE, 1):
        vystup.append(dict(id=pid, list=f'tabule {i}', strana='recto', sken=sk, stav='chybi_original',
                           overeno_clovekem=False, bloky=[]))
    for p in vystup:
        IM.dump(p, KNIHA / 'strany' / f"{p['id']}.yaml")
    (KNIHA / 'zdroje' / 'import_report.txt').write_text('\n'.join(report), encoding='utf-8')
    st = Counter(p['stav'] for p in vystup)
    print('stran:', len(vystup), dict(st), '| varování:', len(report), '| obrázků:', len(images))


if __name__ == '__main__':
    main()
