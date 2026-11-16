"""Jednorázový import pracovního překladu Bernské příručky (1615) do YAML stran.

Použití: python -I nastroje/import_bern.py
Vstup:  Bern/Des Kriegs Exercitij vnd Vbung_.md
Výstup: knihy/bern-1615/strany/<id>.yaml, obrazky/erb-bern.png, zdroje/import_report.txt
"""
import base64, re, sys, pathlib
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import import_md as IM  # parse_blocks, clean_inline, strip_emph, gale_church, merge, dump

KOREN = pathlib.Path(__file__).resolve().parent.parent
MD = KOREN / 'Bern' / 'Des Kriegs Exercitij vnd Vbung_.md'
KNIHA = KOREN / 'knihy' / 'bern-1615'

SUBSEKCE_RE = re.compile(
    r'^(Die Wörter|Povelová slova|Folget die Schiltwacht|Následuje stráž|'
    r'Commandement|Auslegung|Výklad těchto)',
    re.I,
)


def normalizuj_de(s):
    s = s.replace('vñ', 'vnd').replace('Vñ', 'Vnd')
    s = s.replace('ſ', 's')
    return s


def parse_bern_blocks(lines):
    """Rozparsuje bloky jedné jazykové poloviny (nadpisy, číslované seznamy, odstavce, obrázky)."""
    blocks, buf = [], []

    def clean_text(raw_list):
        return [IM.clean_inline(x).replace('\xad', '').replace('\\!', '!') for x in raw_list]

    def flush():
        if not buf:
            return
        raw = clean_text(buf)
        buf.clear()
        first = raw[0].lstrip()
        if first.startswith('> '):
            raw = [r.lstrip()[2:] if r.lstrip().startswith('> ') else r for r in raw]
            first = raw[0].lstrip()

        m = re.match(r'^(#{1,4})\s*(.*)$', first)
        if m and len(raw) == 1:
            lvl_raw = len(m.group(1))
            txt = re.sub(r'\s*\{#[^}]*\}', '', m.group(2)).strip()
            txt = IM.strip_emph(txt)
            img = re.search(r'!\[\]\[(image\d+)\]', txt)
            if img:
                blocks.append(dict(typ='obrazek', obrazek=img.group(1)))
                return
            if txt and not re.fullmatch(r'[\s*]*', txt):
                if lvl_raw <= 2:
                    u = 1
                elif SUBSEKCE_RE.match(txt):
                    u = 2
                else:
                    u = 3
                blocks.append(dict(typ='nadpis', uroven=u, text=txt))
            return

        stripped = [r.strip() for r in raw if r.strip()]
        if not stripped:
            return

        # obrázek v samostatném řádku nebo na konci odstavce
        joined = ' '.join(stripped)
        img = re.search(r'!\[\]\[(image\d+)\]', joined)
        if img:
            before = re.sub(r'\*?!\[\]\[image\d+\]\*?', '', joined).strip()
            if before:
                blocks.append(dict(typ='odstavec', text=IM.strip_emph(before)))
            blocks.append(dict(typ='obrazek', obrazek=img.group(1)))
            return

        # číslovaný seznam povelů: řádky začínající `1. ...` (po clean_inline je `1\.` -> `1.`)
        if all(re.match(r'^\d+\.\s+', r) for r in stripped):
            items = []
            for r in stripped:
                mm = re.match(r'^(\d+\.)\s+(.*)$', r)
                items.append(f'{mm.group(1)} {IM.strip_emph(mm.group(2))}')
            blocks.append(dict(typ='seznam', polozky=items))
            return

        # jednotlivé řádky oddělené dvěma mezerami (např. citáty nebo podpisy) – zachováme zalomení řádku
        if len(raw) > 1 and any(r.endswith('  ') for r in raw[:-1]):
            lines_clean = [IM.strip_emph(r) for r in stripped]
            blocks.append(dict(typ='odstavec', text='\n'.join(l for l in lines_clean if l)))
            return

        txt = IM.strip_emph(' '.join(stripped))
        if txt:
            blocks.append(dict(typ='odstavec', text=txt))

    for l in lines:
        s = l.strip()
        if not s:
            flush()
        elif re.match(r'^#{1,4}\s*$', s):
            continue
        elif re.match(r'^\s*(#{1,4}|> #)', l):
            flush()
            buf.append(l)
            flush()
        elif re.match(r'^\s*\d+\\?\.\s+', l):
            if buf and not all(re.match(r'^\s*\d+\\?\.\s+', x) for x in buf):
                flush()
            buf.append(l)
        else:
            if buf and all(re.match(r'^\s*\d+\\?\.\s+', x) for x in buf):
                flush()
            buf.append(l)
    flush()
    return blocks


def page_meta(tnum, scan):
    if scan == 3:
        return dict(id='titul', list='titulní list', strana='recto', sken=3)
    if scan == 4:
        return dict(id='citaty', list='citáty', strana='verso', sken=4)
    if 5 <= scan <= 18:
        return dict(
            id=f'predmluva-{scan - 4:02d}',
            list='předmluva',
            strana=('recto' if scan % 2 else 'verso'),
            sken=scan,
        )
    return dict(
        id=f'{int(tnum):03d}',
        list=str(int(tnum)),
        strana=('recto' if scan % 2 else 'verso'),
        sken=scan,
    )


def pair_blocks(de_blocks, cs_blocks, warn):
    """Spáruje bloky DE a CS mezi kotvami (nadpisy a obrázky)."""
    out = []
    # rozděl na úseky podle obrázků (obrázek je jen v jedné polovině)
    imgs = [b for b in de_blocks + cs_blocks if b['typ'] == 'obrazek']
    de_clean = [b for b in de_blocks if b['typ'] != 'obrazek']
    cs_clean = [b for b in cs_blocks if b['typ'] != 'obrazek']

    if not cs_clean:
        for b in de_clean:
            if b['typ'] == 'nadpis':
                out.append(dict(typ='nadpis', uroven=b['uroven'], de=b['text'], cs=None))
            elif b['typ'] == 'seznam':
                out.append(dict(typ='seznam', de=b['polozky'], cs=None))
            else:
                out.append(dict(typ='odstavec', de=b['text'], cs=None))
    elif len(de_clean) == len(cs_clean) and all(
        d['typ'] == c['typ'] for d, c in zip(de_clean, cs_clean)
    ):
        for d, c in zip(de_clean, cs_clean):
            if d['typ'] == 'nadpis':
                out.append(dict(typ='nadpis', uroven=d['uroven'], de=d['text'], cs=c['text']))
            elif d['typ'] == 'seznam':
                rec = dict(typ='seznam', de=d['polozky'], cs=c['polozky'])
                if len(d['polozky']) != len(c['polozky']):
                    rec['zarovnat'] = True
                    warn.append(f'seznam DE {len(d["polozky"])} / CS {len(c["polozky"])}')
                out.append(rec)
            else:
                out.append(dict(typ='odstavec', de=d['text'], cs=c['text']))
    else:
        warn.append(f'neshodný počet bloků DE {len(de_clean)} / CS {len(cs_clean)}')
        pairs = IM.gale_church(de_clean, cs_clean)
        for di, ci in pairs:
            dv, dt = IM.merge([de_clean[k] for k in di]) if di else (None, None)
            cv, ct = IM.merge([cs_clean[k] for k in ci]) if ci else (None, None)
            typ = dt or ct
            if dt and ct and dt != ct:
                typ = 'nadpis' if 'nadpis' in (dt, ct) and len(di) == len(ci) == 1 else 'odstavec'
                if isinstance(dv, list):
                    dv = '\n'.join(dv)
                if isinstance(cv, list):
                    cv = '\n'.join(cv)
            if typ == 'nadpis':
                u = (de_clean[di[0]] if di else cs_clean[ci[0]]).get('uroven', 3)
                rec = dict(typ='nadpis', uroven=u, de=dv, cs=cv)
            else:
                rec = dict(typ=typ, de=dv, cs=cv)
            if len(di) != 1 or len(ci) != 1:
                rec['zarovnat'] = True
            out.append(rec)

    for im in imgs:
        out.append(dict(typ='obrazek', soubor='erb-bern.png' if im['obrazek'] == 'image1' else im['obrazek'], popis=''))
    return out


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    lines = MD.read_text(encoding='utf-8').splitlines()
    (KNIHA / 'obrazky').mkdir(parents=True, exist_ok=True)
    (KNIHA / 'strany').mkdir(parents=True, exist_ok=True)
    (KNIHA / 'zdroje').mkdir(parents=True, exist_ok=True)

    images = {}
    for l in lines:
        m = re.match(r'^\[(image\d+)\]: <data:image/(\w+);base64,(.*)>$', l)
        if m:
            fn = 'erb-bern.' + m.group(2) if m.group(1) == 'image1' else f'{m.group(1)}.{m.group(2)}'
            (KNIHA / 'obrazky' / fn).write_bytes(base64.b64decode(m.group(3)))
            images[m.group(1)] = fn

    raw_pages, cur = [], None
    for l in lines:
        if l.startswith('[image1]:'):
            break
        m = re.match(r'^#\s*\*str\.\s*(?:(\d+)\s*)?\\?\[(\d+)\\?\]\*', l.strip())
        if m:
            cur = (m.group(1), int(m.group(2)), [])
            raw_pages.append(cur)
            continue
        if cur is not None:
            cur[2].append(l)

    report = []
    out_pages = []
    prev_ended_mid = False

    for tnum, scan, plines in raw_pages:
        meta = page_meta(tnum, scan)
        sep_idx = next((i for i, l in enumerate(plines) if l.strip().lstrip('# ') == '---'), None)
        if sep_idx is None:
            de_lines, cs_lines = plines, []
        else:
            de_lines, cs_lines = plines[:sep_idx], plines[sep_idx + 1:]

        de_blocks = parse_bern_blocks(de_lines)
        for b in de_blocks:
            if 'text' in b:
                b['text'] = normalizuj_de(b['text'])
            if 'polozky' in b:
                b['polozky'] = [normalizuj_de(x) for x in b['polozky']]
        cs_blocks = parse_bern_blocks(cs_lines)

        warn = []
        # předmluva-01: na skenu 5 je tištěný nadpis „Vorred.“
        if meta['id'] == 'predmluva-01':
            de_blocks.insert(0, dict(typ='nadpis', uroven=1, text='Vorred.'))
            cs_blocks.insert(0, dict(typ='nadpis', uroven=1, text='Předmluva'))

        bloky = pair_blocks(de_blocks, cs_blocks, warn)

        # titul: sloučit 5 řádků nadpisu do struktury titul.yaml (1 nadpis + podtitul + tiráž)
        if meta['id'] == 'titul':
            bloky = [
                dict(
                    typ='nadpis',
                    uroven=1,
                    de='Kurtzer Begriff vnd Anleitung Des Kriegs Exercitij vnd Vbung/',
                    cs='Stručný přehled a průvodce vojenským výcvikem a manévry',
                ),
                dict(
                    typ='odstavec',
                    de=(
                        'Also kurtzlich zum Nutz vnd Gebrauch der Löblichen Republic zu Bern/ vnd derselben '
                        'Stetten/ vnd Landschafft zu samen getragen. Vnd Des Durchleuchtigen/ Hochgebornen '
                        'Fürsten vnd Herren/ Herrn MAVRITII, Fürsten zu Oranien/ vndt Graffen zu Nassaw/ etc. '
                        'gleichförmig gemachet vnd angeordnet.'
                    ),
                    cs=(
                        'takto krátce sestavený k užitku a potřebě chvályhodné Republiky Bern i jejích měst '
                        'a venkova, a uspořádaný i přizpůsobený podle řádu jasného, vysokorozeného knížete '
                        'a pána, pana Mořice, knížete oranžského a hraběte z Nasavska atd.'
                    ),
                ),
                dict(
                    typ='odstavec',
                    de='Gedruckt zu Bern/ Im Jar. 1615.',
                    cs='Vytištěno v Bernu roku 1615.',
                ),
            ]
            warn = [w for w in warn if not w.startswith('neshodný')]

        # pokracovani: true, pokud předchozí strana skončila neukončenou větou a první blok této strany je odstavec
        if prev_ended_mid and bloky and bloky[0]['typ'] == 'odstavec':
            bloky[0]['pokracovani'] = True

        # zjisti konec této strany pro další stranu
        text_bloky = [b for b in bloky if b['typ'] in ('odstavec', 'seznam')]
        if text_bloky:
            last_de = text_bloky[-1].get('de')
            if isinstance(last_de, list):
                last_de = last_de[-1]
            prev_ended_mid = bool(last_de and not re.search(r'[.!?:»"\)]$', last_de.strip()))
        else:
            prev_ended_mid = False

        has_cs = any(b.get('cs') for b in bloky if b['typ'] != 'obrazek')
        has_missing_cs = any(b.get('de') and not b.get('cs') for b in bloky if b['typ'] != 'obrazek')
        stav = 'chybi_preklad' if not has_cs else ('castecne' if has_missing_cs else 'prelozeno')

        page = dict(
            id=meta['id'],
            list=meta['list'],
            strana=meta['strana'],
            sken=meta['sken'],
            stav=stav,
            overeno_clovekem=False,
            bloky=bloky,
        )
        out_pages.append(page)
        if warn:
            report.append(f"{meta['id']}: " + '; '.join(warn))

    for p in out_pages:
        IM.dump(p, KNIHA / 'strany' / f"{p['id']}.yaml")
    (KNIHA / 'zdroje' / 'import_report.txt').write_text('\n'.join(report), encoding='utf-8')
    st = Counter(p['stav'] for p in out_pages)
    print('stran:', len(out_pages), dict(st), '| varování:', len(report), '| obrázků:', len(images))
    for r in report:
        print(' ', r)


if __name__ == '__main__':
    main()
