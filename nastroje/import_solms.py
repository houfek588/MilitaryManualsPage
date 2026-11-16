"""Jednorázový import pracovního překladu a předpřipravení Druhé knihy Reinharda ze Solmsu (1559).

Použití: python -I nastroje/import_solms.py
Vstup:
  Solms/Reinhard zu Solms. Dises Buch vnd Kriegsbeschreibung.md
  knihy/solms-1559/zdroje/ocr_bsb/NNNN.txt
Výstup:
  knihy/solms-1559/strany/<id>.yaml   (158 stran)
  knihy/solms-1559/zdroje/import_report.txt
"""
import pathlib, re, sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import import_md as IM

KOREN = pathlib.Path(__file__).resolve().parent.parent
MD = KOREN / 'Solms' / 'Reinhard zu Solms. Dises Buch vnd Kriegsbeschreibung.md'
KNIHA = KOREN / 'knihy' / 'solms-1559'
OCR_DIR = KNIHA / 'zdroje' / 'ocr_bsb'

WOODCUT_ONLY = {
    92: 'drevorez-092.jpg',
    102: 'tab-01.jpg',
    120: 'drevorez-120.jpg',
    140: 'drevorez-140.jpg',
    146: 'drevorez-146.jpg',
    184: 'drevorez-184.jpg',
    192: 'drevorez-192.jpg',
    210: 'drevorez-210.jpg',
    216: 'drevorez-216.jpg',
    218: 'drevorez-218.jpg',
    220: 'drevorez-220.jpg',
    222: 'drevorez-222.jpg',
    224: 'drevorez-224.jpg',
    226: 'drevorez-226.jpg',
    228: 'drevorez-228.jpg',
}

# Mapování přeskakovaných čísel listů v tisku -> počáteční sken souvislého úseku
FOLIO_RUNS = [
    (1, 4, 93),
    (6, 29, 103),
    (31, 32, 151),
    (34, 46, 155),
    (48, 50, 181),
    (52, 55, 187),
    (57, 57, 195),
    (59, 62, 197),
    (64, 67, 205),
    (69, 69, 213),
    # list 70: sken 215 prázdný líc (vynechán), sken 216 dřevořez rubu -> 070v
    (71, 76, 217),
    (78, 87, 229),
]


def build_inventory():
    pages = [
        dict(id='titul-svazek', list='titulní list svazku', strana='recto', sken=9),
        dict(id='erb-solms', list='erb', strana='verso', sken=90),
        dict(id='titul', list='titulní list', strana='recto', sken=91),
        dict(id='titul-v', list='rub titulního listu', strana='verso', sken=92),
        dict(id='tab-01', list='tabule 1', strana='recto', sken=102),
        dict(id='070v', list='70', strana='verso', sken=216),
    ]
    for f_start, f_end, s_start in FOLIO_RUNS:
        sk = s_start
        for fol in range(f_start, f_end + 1):
            for verso, st in ((False, 'r'), (True, 'v')):
                pages.append(dict(
                    id=f'{fol:03d}{st}',
                    list=str(fol),
                    strana=('verso' if verso else 'recto'),
                    sken=sk,
                ))
                sk += 1
    pages.sort(key=lambda p: p['sken'])
    return pages


def clean_ocr_lines(scan):
    """Načte OCR text daného skenu bez čárového kódu BSB a běžícího záhlaví."""
    f = OCR_DIR / f'{scan:04d}.txt'
    if not f.exists():
        return []
    raw = [l.strip() for l in f.read_text(encoding='utf-8').splitlines() if l.strip()]
    out = []
    for i, l in enumerate(raw):
        if i < 4 and re.fullmatch(r'[\d.,\s]{6,}|000.*', l):
            continue
        if i < 4 and re.match(r'^(Von|Don)\s+be[ſsf]chr.{0,6}bung|^(Das|Dat)\s+ander\s+B[uü]ch', l, re.I):
            continue
        if i < 4 and re.fullmatch(r'\d{1,3}\s*[.,:]?', l):
            continue
        if i == len(raw) - 1 and re.fullmatch(r'[a-p]\s*[iIjJ1234]{0,4}|[A-P]', l):
            continue
        out.append(l)
    return out


def join_ocr_paragraphs(lines):
    """Spojí řádky OCR do předběžných odstavců se sloučením dělení slov."""
    if not lines:
        return []
    paras, cur = [], []
    lengths = [len(l) for l in lines]
    med = sorted(lengths)[len(lengths) // 2] if lengths else 60
    for l in lines:
        if cur and cur[-1].endswith('-'):
            cur[-1] = cur[-1][:-1] + l
        else:
            cur.append(l)
        if len(l) < max(28, med * 0.65) and l.endswith(('.', '?', '!', ':')):
            paras.append(' '.join(cur))
            cur = []
    if cur:
        paras.append(' '.join(cur))
    return paras


def parse_md_sections():
    """Rozdělí Solms/*.md podle značek stran (číslo skenu -> seznam řádků)."""
    text = MD.read_text(encoding='utf-8')
    lines = text.splitlines()
    # odstranit definice obrázků na konci
    end = next((i for i, l in enumerate(lines) if re.match(r'^\[image\d+\]:', l)), len(lines))
    body = lines[:end]

    sec_re = re.compile(r'^(?:#{1,6}\s*)?\*?str\.\s*(\d+)(?:\s*\(\d+\))?\*?\s*$')
    sections = {}
    cur_scan = None
    for l in body:
        s = l.strip()
        m = sec_re.match(s)
        if m:
            cur_scan = int(m.group(1))
            sections[cur_scan] = []
            continue
        if s in ('#####', '##### '):
            continue
        if cur_scan is not None:
            sections[cur_scan].append(l)
    return sections


def split_lang_blocks(lines):
    """Rozparsuje bloky v rámci jedné strany z .md a rozdělí je na DE a CS polovinu."""
    blocks, buf = [], []

    def flush():
        if not buf:
            return
        raw = [IM.clean_inline(x) for x in buf]
        buf.clear()
        first = raw[0].lstrip()
        m = re.match(r'^(#{1,4})\s*(.*)$', first)
        if m and len(raw) == 1:
            txt = IM.strip_emph(m.group(2))
            if txt and not re.fullmatch(r'[\s*]*', txt):
                blocks.append(dict(typ='nadpis', uroven=3, text=txt))
            return
        joined_all = ' '.join(r.strip() for r in raw if r.strip())
        if re.search(r'!\[\]\[(image\d+)\]', joined_all):
            blocks.append(dict(typ='obrazek', obrazek=re.search(r'!\[\]\[(image\d+)\]', joined_all).group(1)))
            return
        stripped = [r.strip() for r in raw if r.strip()]
        if not stripped:
            return
        if all(re.match(r'^[*-]\s+', r) for r in stripped):
            items = [IM.strip_emph(re.sub(r'^[*-]\s+', '', r)) for r in stripped]
            blocks.append(dict(typ='seznam', polozky=items, italic=all(re.match(r'^[*-]\s+\*', r) for r in stripped)))
            return
        if any('\t' in r for r in raw):
            # tabulkový blok (např. rozpis žoldů na s. 205) – zachovat řádky
            txt = '\n'.join(IM.strip_emph(r) for r in stripped)
            blocks.append(dict(typ='odstavec', text=txt, italic=any('*' in r for r in stripped[:3])))
            return
        txt = IM.strip_emph(' '.join(stripped))
        if txt:
            blocks.append(dict(typ='odstavec', text=txt, italic=bool(re.match(r'^\*(?!\*)', stripped[0]))))

    for l in lines:
        if not l.strip():
            flush()
        elif re.match(r'^\s*#{1,4}\s+', l):
            flush()
            buf.append(l)
            flush()
        else:
            if buf and re.match(r'^\s*[*-]\s+', l) and not re.match(r'^\s*[*-]\s+', buf[-1]):
                flush()
            buf.append(l)
    flush()

    blocks_clean = [b for b in blocks if b['typ'] != 'obrazek']
    # Každá strana v Solms/*.md má nejprve všechny DE bloky a pak všechny CS bloky.
    langs = [IM.lang(IM.block_text(b), italic=b.get('italic', False)) for b in blocks_clean]
    # najít bod přechodu z DE na CS
    split_idx = None
    for i, lg in enumerate(langs):
        if lg == 'cs':
            # zkontrolovat, jestli po tomto místě ještě není zřetelný německý blok (kromě chybných)
            rest_de = sum(1 for x in langs[i:] if x == 'de')
            if rest_de == 0:
                split_idx = i
                break
    if split_idx is None:
        # fallback podle půlky nebo postupného průchodu
        first_cs = next((i for i, lg in enumerate(langs) if lg == 'cs'), len(blocks_clean))
        split_idx = first_cs
    return blocks_clean[:split_idx], blocks_clean[split_idx:]


def pair_blocks(de_blocks, cs_blocks, warn):
    out = []
    if len(de_blocks) == len(cs_blocks) and all(d['typ'] == c['typ'] for d, c in zip(de_blocks, cs_blocks)):
        for d, c in zip(de_blocks, cs_blocks):
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
        return out

    warn.append(f'neshodný počet bloků DE {len(de_blocks)} / CS {len(cs_blocks)}')
    pairs = IM.gale_church(de_blocks, cs_blocks)
    for di, ci in pairs:
        dv, dt = IM.merge([de_blocks[k] for k in di]) if di else (None, None)
        cv, ct = IM.merge([cs_blocks[k] for k in ci]) if ci else (None, None)
        typ = dt or ct
        if dt and ct and dt != ct:
            typ = 'nadpis' if 'nadpis' in (dt, ct) and len(di) == len(ci) == 1 else 'odstavec'
            if isinstance(dv, list):
                dv = '\n'.join(dv)
            if isinstance(cv, list):
                cv = '\n'.join(cv)
        if typ == 'nadpis':
            u = (de_blocks[di[0]] if di else cs_blocks[ci[0]]).get('uroven', 3)
            rec = dict(typ='nadpis', uroven=u, de=dv, cs=cv)
        else:
            rec = dict(typ=typ, de=dv, cs=cv)
        if len(di) != 1 or len(ci) != 1:
            rec['zarovnat'] = True
        out.append(rec)
    return out


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    (KNIHA / 'strany').mkdir(parents=True, exist_ok=True)
    inventory = build_inventory()
    md_sections = parse_md_sections()

    report = []
    out_pages = []

    for meta in inventory:
        scan = meta['sken']
        pid = meta['id']
        warn = []

        if scan in WOODCUT_ONLY:
            bloky = [dict(typ='obrazek', soubor=WOODCUT_ONLY[scan], popis='')]
            stav = 'chybi_preklad'
        elif scan == 159:
            # 036r: horní polovina pouze v OCR, dolní (Die Commis...) v .md
            ocr_ls = clean_ocr_lines(159)
            cut = next((i for i, l in enumerate(ocr_ls) if 'Commis' in l), len(ocr_ls))
            top_paras = join_ocr_paragraphs(ocr_ls[:cut])
            bloky = [dict(typ='odstavec', de=p, cs=None) for p in top_paras]
            de_b, cs_b = split_lang_blocks(md_sections[159])
            bloky.extend(pair_blocks(de_b, cs_b, warn))
            stav = 'castecne'
            warn.append('částečně přeložená strana: horní část doplněna z OCR bez překladu')
        elif scan in md_sections:
            de_b, cs_b = split_lang_blocks(md_sections[scan])
            if not cs_b:
                warn.append('v .md nebyl rozpoznán český překlad')
            bloky = pair_blocks(de_b, cs_b, warn)
            has_cs = any(b.get('cs') for b in bloky)
            has_miss = any(b.get('de') and not b.get('cs') for b in bloky)
            stav = 'chybi_preklad' if not has_cs else ('castecne' if has_miss else 'prelozeno')
        else:
            # dosud nepřeložená strana -> předvyplnit z OCR
            if scan == 9:
                ocr_paras = [
                    'Das erst Buch.\nDises Buch vnd Kriegs beschreibung ist vermelten vnd berichten einer guten ordentlichen Kriegsregierung/ nach alter Teutschen ordnung/ gebrauch vnd herkomen/ mit andern noch Büchern von aller Kriegsregierung vnd Rüstung so zu dem Krieg gehört.',
                    'Auch mit jhren augenscheinlichen Figuren zu besserem verstandt/ neben den Beschreibungen souil möglich/ angezeiget.',
                    'Anno Domini/ M. D. Lix.',
                ]
                bloky = [
                    dict(typ='nadpis', uroven=1, de=ocr_paras[0], cs=None),
                    dict(typ='odstavec', de=ocr_paras[1], cs=None),
                    dict(typ='obrazek', soubor='drevorez-1.jpg', popis=''),
                    dict(typ='odstavec', de=ocr_paras[2], cs=None),
                ]
            elif scan == 90:
                ocr_paras = join_ocr_paragraphs(clean_ocr_lines(scan))
                bloky = [dict(typ='odstavec', de=' '.join(ocr_paras), cs=None)] if ocr_paras else []
                bloky.append(dict(typ='obrazek', soubor='drevorez-090.jpg', popis=''))
            else:
                ocr_paras = join_ocr_paragraphs(clean_ocr_lines(scan))
                bloky = [dict(typ='odstavec', de=p, cs=None) for p in ocr_paras]
            stav = 'chybi_preklad'

        page = dict(
            id=pid,
            list=meta['list'],
            strana=meta['strana'],
            sken=scan,
            stav=stav,
            overeno_clovekem=False,
            bloky=bloky,
        )
        out_pages.append(page)
        if warn:
            report.append(f'{pid} (sken {scan}): ' + '; '.join(warn))

    for p in out_pages:
        IM.dump(p, KNIHA / 'strany' / f"{p['id']}.yaml")
    (KNIHA / 'zdroje' / 'import_report.txt').write_text('\n'.join(report), encoding='utf-8')
    st = Counter(p['stav'] for p in out_pages)
    print('stran:', len(out_pages), dict(st), '| varování:', len(report))
    for r in report:
        print(' ', r)


if __name__ == '__main__':
    main()
