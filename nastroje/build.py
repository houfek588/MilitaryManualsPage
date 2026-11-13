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
import html as htmlmod, json, re, shutil, sys, time, unicodedata, urllib.parse, pathlib
import yaml

KOREN = pathlib.Path(__file__).resolve().parent.parent
WEB = KOREN / 'nastroje' / 'web'
DOCS = KOREN / 'docs'
VERZE = time.strftime('%Y%m%d%H%M')  # proti zastaralé mezipaměti prohlížeče
PROJEKT = yaml.safe_load((KOREN / 'projekt.yaml').read_text(encoding='utf-8'))
esc = lambda t: htmlmod.escape(str(t or ''), quote=True)


# Ikony sociálních sítí (Simple Icons, CC0) – vkládají se přímo do HTML, fungují i offline.
IKONY = {
    'facebook': ('Facebook', 'M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z'),
    'instagram': ('Instagram', 'M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913a5.885 5.885 0 001.384 2.126A5.868 5.868 0 004.14 23.37c.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558a5.898 5.898 0 002.126-1.384 5.86 5.86 0 001.384-2.126c.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913a5.89 5.89 0 00-1.384-2.126A5.847 5.847 0 0019.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227a3.81 3.81 0 01-.899 1.382 3.744 3.744 0 01-1.38.896c-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421a3.716 3.716 0 01-1.379-.899 3.644 3.644 0 01-.9-1.38c-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03zm0 3.678a6.162 6.162 0 100 12.324 6.162 6.162 0 100-12.324zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405a1.441 1.441 0 01-2.88 0 1.44 1.44 0 012.88 0z'),
}


def socialni_html():
    out = []
    for klic, url in (PROJEKT.get('socialni') or {}).items():
        if not url or klic not in IKONY:
            continue
        nazev, d = IKONY[klic]
        out.append(f'<a href="{esc(url)}" target="_blank" rel="noopener" title="{nazev} – {esc((PROJEKT.get("skupina") or {}).get("nazev"))}" '
                   f'aria-label="{nazev}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="{d}"/></svg></a>')
    return ''.join(out)


def varovani(html, zdroj):
    """Vloží do vygenerovaného HTML upozornění, že se needituje (přepíše ho další build)."""
    pozn = (f'<!-- VYGENEROVÁNO nástrojem nastroje/build.py – NEEDITUJ, změny se při dalším sestavení přepíšou.\n'
            f'     Text uprav v {zdroj}, nastavení (autor, kontakt, skupina, dar) v projekt.yaml. -->\n')
    return html.replace('<!doctype html>\n', '<!doctype html>\n' + pozn, 1)


def staticka_stranka(sablona, knihy=None):
    """Rozcestník a O projektu: doplní údaje z projekt.yaml."""
    P = PROJEKT
    sk = P.get('skupina') or {}
    dar = P.get('dar') or {}
    casti = []
    if dar.get('odkaz'):
        casti.append(f'<p><a class="tl velke" href="{esc(dar["odkaz"])}" target="_blank" rel="noopener">{esc(dar.get("odkaz_text") or "Podpořit projekt")}</a></p>')
    if dar.get('ucet') or dar.get('qr'):
        zprava = f' se zprávou pro příjemce <b>{esc(dar["zprava"])}</b>' if dar.get('zprava') else ''
        ucet = f'<p>Převodem na účet <b>{esc(dar["ucet"])}</b>{zprava}.</p>' if dar.get('ucet') else ''
        qr = (f'<figure><img src="assets/{esc(dar["qr"])}" alt="QR kód pro platbu{" na účet " + esc(dar["ucet"]) if dar.get("ucet") else ""}" width="200" height="206">'
              '<figcaption>Naskenujte v mobilní aplikaci své banky (QR platba).</figcaption></figure>') if dar.get('qr') else ''
        casti.append(f'<div class="dar-qr">{qr}<div>{ucet}</div></div>')
    if not casti:
        casti.append(f'<p>Chcete-li projekt podpořit, napište mi prosím na <a href="mailto:{esc(P["email"])}?subject=Podpora%20projektu">{esc(P["email"])}</a> – rád pošlu podrobnosti.</p>')
    dar_html = ('<div class="dar"><p>Překlady vznikají ve volném čase a jejich zpracování (výpočetní kapacita pro AI, '
                'čas na ruční kontrolu, případně tisk) něco stojí. Pokud vám edice pomáhá, ať při reenactmentu, '
                'studiu, výzkumu nebo vedení skupiny, budu vděčný za jakýkoli příspěvek. Děkuji!</p>' + ''.join(casti) + '</div>')
    repo = (f' Případně založte issue na <a href="{esc(P["repozitar"])}/issues" target="_blank" rel="noopener">GitHubu</a>.'
            if P.get('repozitar') else '')
    paticka = (f'<a href="index.html">Knihovna</a> · <a href="o-projektu.html">O projektu</a> · '
               f'{esc(P["autor"])}, <a href="mailto:{esc(P["email"])}">{esc(P["email"])}</a> · '
               f'pro skupinu <a href="{esc(sk.get("url"))}" target="_blank" rel="noopener">{esc(sk.get("nazev"))}</a>')
    t = (WEB / sablona).read_text(encoding='utf-8')
    for k, v in {'{{WEB}}': esc(P['nazev']), '{{PODTITUL}}': esc(P.get('podtitul')), '{{AUTOR}}': esc(P['autor']),
                 '{{EMAIL}}': esc(P['email']), '{{SKUPINA}}': esc(sk.get('nazev')), '{{SKUPINA_URL}}': esc(sk.get('url')),
                 '{{DAR}}': dar_html, '{{REPO}}': repo, '{{PATICKA}}': paticka, '{{SOCIALNI}}': socialni_html()}.items():
        t = t.replace(k, v)
    if knihy is not None:
        t = t.replace('/*KNIHY*/[]', json.dumps(knihy, ensure_ascii=False))
    return t.replace('app.css"', f'app.css?v={VERZE}"').replace('tema.js"', f'tema.js?v={VERZE}"')


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
                projekt=dict(nazev=PROJEKT['nazev'], email=PROJEKT['email'], autor=PROJEKT['autor']),
                kategorie=glos.get('kategorie', {}), stranky=pages, bloky=blocks, oddily=sections,
                hesla=hesla, demap=de_map, stav=stats, overeno=sum(1 for p in pages if p.get('ov')))
    js = 'window.EDICE = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n'
    (out / 'data.js').write_text(js, encoding='utf-8')
    html = (WEB / 'kniha.html').read_text(encoding='utf-8')
    html = html.replace('src="data.js"', f'src="data.js?v={VERZE}"').replace('app.js"', f'app.js?v={VERZE}"').replace('app.css"', f'app.css?v={VERZE}"').replace('tema.js"', f'tema.js?v={VERZE}"')
    html = html.replace('{{NAZEV}}', meta['nazev']).replace('{{AUTOR}}', meta['autor']).replace('{{ROK}}', str(meta['rok']))
    html = html.replace('{{WEB}}', esc(PROJEKT['nazev'])).replace('{{EMAIL}}', esc(PROJEKT['email']))
    html = html.replace('{{SOCIALNI}}', socialni_html())
    html = html.replace('{{PREDMET}}', urllib.parse.quote(f"{meta['nazev']} – oprava"))
    (out / 'index.html').write_text(varovani(html, 'nastroje/web/kniha.html (texty knihy v knihy/<kniha>/)'), encoding='utf-8')
    print(f"{meta['id']}: {len(pages)} stran (ověřeno člověkem {data['overeno']}), {len(blocks)} bloků, {len(sections)} oddílů, {len(hesla)} hesel, data.js {len(js) // 1024} kB, {stats}")
    return dict(id=meta['id'], nazev=meta['nazev'], nazev_orig=meta['nazev_orig'], autor=meta['autor'], rok=meta['rok'],
                popis=meta.get('popis', ''), stav=stats, stran=len(pages), overeno=data['overeno'])


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    DOCS.mkdir(exist_ok=True)
    (DOCS / 'assets').mkdir(exist_ok=True)
    for f in ('app.js', 'app.css', 'tema.js', 'logo.png', 'favicon.png', 'fonts.css'):
        shutil.copy2(WEB / f, DOCS / 'assets' / f)
    shutil.copytree(WEB / 'fonts', DOCS / 'assets' / 'fonts', dirs_exist_ok=True)
    if (PROJEKT.get('dar') or {}).get('qr'):
        shutil.copy2(WEB / PROJEKT['dar']['qr'], DOCS / 'assets' / PROJEKT['dar']['qr'])
    knihy = [build_kniha(d) for d in sorted((KOREN / 'knihy').iterdir()) if (d / 'kniha.yaml').exists()]
    (DOCS / 'index.html').write_text(varovani(staticka_stranka('index.html', knihy), 'nastroje/web/index.html'), encoding='utf-8')
    (DOCS / 'o-projektu.html').write_text(varovani(staticka_stranka('o-projektu.html'), 'nastroje/web/o-projektu.html'), encoding='utf-8')
    (DOCS / '.nojekyll').write_text('', encoding='utf-8')


if __name__ == '__main__':
    main()
