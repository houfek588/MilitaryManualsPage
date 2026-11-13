"""Sestaví statický web edice do složky docs/ (GitHub Pages i offline otevření dvojklikem).

Použití:  python -I nastroje/build.py
Vstup:    knihy/<kniha>/{kniha.yaml, glosar.yaml, strany/*.yaml, obrazky/*}
          nastroje/web/{app.js, app.css, kniha.html, index.html}
Výstup:   docs/index.html                 rozcestník knih
          docs/assets/app.js, app.css     společná aplikace
          docs/<kniha>/index.html         čtečka knihy
          docs/<kniha>/data.js            data knihy (window.EDICE = {...}); <script src>, takže funguje i z file://
          docs/<kniha>/obrazky/*
"""
import json, re, shutil, sys, time, unicodedata, pathlib
import yaml

KOREN = pathlib.Path(__file__).resolve().parent.parent
WEB = KOREN / 'nastroje' / 'web'
DOCS = KOREN / 'docs'
VERZE = time.strftime('%Y%m%d%H%M')  # proti zastaralé mezipaměti prohlížeče


def slug(s, maxlen=48):
    s = re.sub(r'\{[^}]*\}|\[[^\]]*\]|\[\^\d+\]', '', s or '')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return (s[:maxlen].rstrip('-') or 'oddil')


def plain(v):
    if v is None:
        return ''
    if isinstance(v, list):
        return ' '.join(plain(x) for x in v)
    s = re.sub(r'\[\^\d+\]', '', str(v))
    s = re.sub(r'\{([^}]*)\}\*?', r'[\1]', s)
    return re.sub(r'[*_]', '', s)


def norm_de(s):
    s = s.lower().replace('ſ', 's').replace('å', 'a').replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('ů', 'u')
    s = s.replace('ß', 'ss').replace('th', 't').replace('ey', 'ei').replace('ff', 'f').replace('dt', 't')
    return re.sub(r'[^a-z]', '', s)


def poradi(kniha_dir, meta):
    front = meta.get('predsadka', [])
    ids = [f.stem for f in (kniha_dir / 'strany').glob('*.yaml')]

    def key(i):
        if i in front:
            return (0, front.index(i))
        return (1, int(i[:3]) * 2 + (i[3] == 'v'))
    return sorted(ids, key=key)


def build_kniha(kniha_dir):
    meta = yaml.safe_load((kniha_dir / 'kniha.yaml').read_text(encoding='utf-8'))
    glos = yaml.safe_load((kniha_dir / 'glosar.yaml').read_text(encoding='utf-8'))
    pages, blocks, sections = [], [], []
    stack = []  # otevřené oddíly (indexy do sections)
    used_slugs = set()

    def new_section(uroven, cs, de, pidx, bidx):
        base = slug(cs or de)
        s, k = base, 2
        while s in used_slugs:
            s, k = f'{base}-{k}', k + 1
        used_slugs.add(s)
        while stack and sections[stack[-1]]['u'] >= uroven:
            sections[stack.pop()]['do'] = bidx
        sec = dict(id=s, u=uroven, cs=cs or '', de=de or '', od=bidx, do=None, p=pidx,
                   rodic=sections[stack[-1]]['id'] if stack else None)
        sections.append(sec)
        stack.append(len(sections) - 1)
        return sec

    for pidx, pid in enumerate(poradi(kniha_dir, meta)):
        try:
            d = yaml.safe_load((kniha_dir / 'strany' / f'{pid}.yaml').read_text(encoding='utf-8'))
        except Exception as e:  # rozpracovaný soubor – stranu vynech, build nesmí spadnout
            print(f'  ! {pid}: chyba YAML, strana vynechána ({str(e).splitlines()[0]})')
            d = dict(id=pid, stav='chybi_original', bloky=[])
        od = len(blocks)
        prvni = (d.get('bloky') or [{}])[0]
        if pid == meta.get('predsadka', ['titul'])[0] and not sections and prvni.get('typ') != 'nadpis':
            new_section(1, 'Titulní list', 'Titelblatt', pidx, od)
        for b in d.get('bloky') or []:
            t = b.get('typ')
            if t == 'nadpis':
                new_section(int(b.get('uroven') or 2), plain(b.get('cs')), plain(b.get('de')), pidx, len(blocks))
            if not sections:
                new_section(1, 'Úvod', '', pidx, len(blocks))
            rec = dict(t=t, p=pidx, s=sections[stack[-1]]['id'])
            for k_src, k_dst in (('de', 'de'), ('cs', 'cs'), ('uroven', 'u'), ('soubor', 'img'), ('popis', 'popis')):
                if b.get(k_src) is not None:
                    rec[k_dst] = b[k_src]
            if b.get('pokracovani'):
                rec['c'] = 1
            if b.get('zarovnat'):
                rec['z'] = 1
            blocks.append(rec)
        pages.append(dict(id=pid, list=d.get('list'), strana=d.get('strana'), sken=d.get('sken'),
                          stav=d.get('stav'), od=od, do=len(blocks),
                          pozn={str(n['n']): n['text'] for n in d.get('poznamky') or []}))
        if d.get('overeno_clovekem'):  # ruční kontrola člověkem
            pages[-1]['ov'] = dict(datum=str(d.get('overeno_datum') or ''), kdo=d.get('overeno_kdo') or '')
    for i in stack:
        sections[i]['do'] = len(blocks)

    # ---- glosář / rejstřík: výskyty
    de_map = {}
    for h in glos['hesla']:
        for v in h.get('de', []):
            de_map.setdefault(norm_de(v), h['id'])
    hesla = []
    for h in glos['hesla']:
        rx = [re.compile(x, re.I) for x in h.get('hledat', [])]
        dn = {norm_de(v) for v in h.get('de', [])}
        vys = []
        for bi, b in enumerate(blocks):
            cs = plain(b.get('cs'))
            if not cs:
                continue
            hit = None
            for m in re.finditer(r'\[([^\]]+)\]', cs):
                if norm_de(m.group(1).split('/')[0]) in dn:
                    hit = m
                    break
            if not hit:
                for r in rx:
                    hit = r.search(cs)
                    if hit:
                        break
            if hit:
                a, z = max(0, hit.start() - 70), min(len(cs), hit.end() + 70)
                vys.append(dict(b=bi, k=('…' if a else '') + cs[a:hit.start()], h=hit.group(0),
                                z=cs[hit.end():z] + ('…' if z < len(cs) else '')))
        hesla.append(dict(id=h['id'], cs=h['cs'], de=h.get('de', []), kat=h.get('kategorie'), pozn=h.get('pozn', ''), v=vys))

    # ---- obrázky
    out = DOCS / meta['id']
    (out / 'obrazky').mkdir(parents=True, exist_ok=True)
    for f in (kniha_dir / 'obrazky').glob('*'):
        shutil.copy2(f, out / 'obrazky' / f.name)

    stats = {}
    for p in pages:
        stats[p['stav']] = stats.get(p['stav'], 0) + 1
    data = dict(meta={k: meta[k] for k in meta if k not in ('poznamky_k_prekladu',)},
                kategorie=glos.get('kategorie', {}), stranky=pages, bloky=blocks, oddily=sections,
                hesla=hesla, demap=de_map, stav=stats, overeno=sum(1 for p in pages if p.get('ov')))
    js = 'window.EDICE = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n'
    (out / 'data.js').write_text(js, encoding='utf-8')
    html = (WEB / 'kniha.html').read_text(encoding='utf-8')
    html = html.replace('src="data.js"', f'src="data.js?v={VERZE}"').replace('app.js"', f'app.js?v={VERZE}"').replace('app.css"', f'app.css?v={VERZE}"')
    html = html.replace('{{NAZEV}}', meta['nazev']).replace('{{AUTOR}}', meta['autor']).replace('{{ROK}}', str(meta['rok']))
    (out / 'index.html').write_text(html, encoding='utf-8')
    print(f"{meta['id']}: {len(pages)} stran (ověřeno člověkem {data['overeno']}), {len(blocks)} bloků, {len(sections)} oddílů, {len(hesla)} hesel, data.js {len(js) // 1024} kB, {stats}")
    return dict(id=meta['id'], nazev=meta['nazev'], nazev_orig=meta['nazev_orig'], autor=meta['autor'], rok=meta['rok'],
                popis=meta.get('popis', ''), stav=stats, stran=len(pages), overeno=data['overeno'])


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    DOCS.mkdir(exist_ok=True)
    (DOCS / 'assets').mkdir(exist_ok=True)
    for f in ('app.js', 'app.css'):
        shutil.copy2(WEB / f, DOCS / 'assets' / f)
    knihy = [build_kniha(d) for d in sorted((KOREN / 'knihy').iterdir()) if (d / 'kniha.yaml').exists()]
    idx = (WEB / 'index.html').read_text(encoding='utf-8')
    idx = idx.replace('/*KNIHY*/[]', json.dumps(knihy, ensure_ascii=False)).replace('app.css"', f'app.css?v={VERZE}"')
    (DOCS / 'index.html').write_text(idx, encoding='utf-8')
    (DOCS / '.nojekyll').write_text('', encoding='utf-8')


if __name__ == '__main__':
    main()
