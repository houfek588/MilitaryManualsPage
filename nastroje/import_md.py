"""Jednorázový import pracovního překladu (export z Google Docs .md) do datového formátu edice.

Vstup:  Fronsberger/Fronsberger, Leonhard. Kriegs Ordnung Vnd Regiment.md
Výstup: knihy/fronsberger-1564/strany/<id>.yaml   (jeden soubor = jedna strana tisku)
        knihy/fronsberger-1564/obrazky/obrazekN.png
        knihy/fronsberger-1564/zdroje/import_report.txt

Co dělá:
 - rozdělí text podle značek stran („str. XVIII (18)“, „str. XVIIIq (18q)“),
 - odstavce rozpozná jako německé / české,
 - spáruje je mezi kotvami (nadpisy) – 1:1, když počty sedí, jinak
   proporcionálně podle délky (Gale–Church; povolené 1:1, 1:2, 2:1, 1:3, 3:1),
 - „(Pozn. překl.: …)“ převede na poznámky pod čarou strany,
 - „[Term]\\*“ zaznamená jako kandidáty glosáře, německé termíny v závorkách
   převede na {Term}, vložky překladatele nechá v [hranatých].
Spouští se jednou; další úpravy se dělají přímo v YAML.
"""
import base64, json, re, sys, pathlib
from collections import Counter, defaultdict
import yaml

KOREN = pathlib.Path(__file__).resolve().parent.parent
MD = KOREN / 'Fronsberger' / 'Fronsberger, Leonhard. Kriegs Ordnung Vnd Regiment.md'
KNIHA = KOREN / 'knihy' / 'fronsberger-1564'

ROMAN = dict(I=1, V=5, X=10, L=50, C=100)


def roman(s):
    s = s.replace('IIII', 'IV').replace('XVIX', 'XIX')  # tisk píše IIII; dokument XVIX = 19
    n = 0
    for i, ch in enumerate(s):
        v = ROMAN[ch]
        n += -v if i + 1 < len(s) and ROMAN[s[i + 1]] > v else v
    return n


def page_id(num, verso):
    return f'{num:03d}{"v" if verso else "r"}'


def canvas(num, verso):
    """Sken BSB bsb10150061 (neúplný, viz migrace_sken_45899.py): fol. I r = sken 9; chybí dvojstrany u listů 39, 59, 69."""
    skip = sum(1 for x in (39, 59, 69) if num > x)
    return 7 + 2 * (num - skip) + (1 if verso else 0)


CZ = set('ěščřžůťďňĚŠČŘŽŮŤĎŇ')
CZ_SOFT = set('ýáíéúÝÁÍÉÚ')
DE_WORDS = set('vnd vnnd ond onnd vnnd soll foll sol der die das auch dann sein ist ift nicht mit von zu jhm ihm jhn dem den item es er so wie oder wo was'.split())


CS_WORDS = set('a je se na v ve s že aby má mají který která které jako nebo pro do k ke od po při jeho jejich tak také když jak být by i ani již jen co kde tom to ten této tento musí nemá nikdo'.split())


def lang(text, italic=False):
    t = re.sub(r'\{[^}]*\}|\[[^\]]*\]', ' ', text)  # termíny v závorkách nerozhodují
    words = re.findall(r'[^\W\d_]+', t.lower())
    de = sum(w in DE_WORDS for w in words) + 2 * sum(c in 'åſß' for c in t) + 0.3 * t.count('/')
    de += sum(1 for w in words if re.match(r'^(vn|vb|vm|jh|zu)', w) or w.endswith(('nn', 'ey', 'eyt', 'ung')))
    cs = 2 * sum(c in CZ for c in t) + sum(w in CS_WORDS for w in words) + 0.5 * sum(c in CZ_SOFT for c in t)
    if italic:
        de += 3
    if de == cs:
        return None
    return 'de' if de > cs else 'cs'


def clean_inline(s):
    s = s.replace('\\[', '[').replace('\\]', ']').replace('\\-', '-').replace('\\.', '.').replace('\\*', '°STAR°')
    s = s.replace('\\(', '(').replace('\\)', ')').replace('\\_', '_').replace('\\#', '#').replace('\\>', '>').replace('\\~', '~')
    return s


def strip_emph(s):
    """Odstraní markdownové zvýraznění, které obaluje celý blok (originál je v exportu kurzívou)."""
    s = s.strip()
    s = re.sub(r'\*{1,3}\s*\*{1,3}', ' ', s)  # „*** ***“ mezi dvěma tučnými úseky
    s = re.sub(r'^\*+|\*+$', '', s).strip()
    s = s.replace('***', '').replace('**', '')
    # osamocené * uvnitř (kurzíva přes řádky) pryč, ale ponech °STAR°
    s = re.sub(r'(?<!\w)\*(?=\S)|(?<=\S)\*(?!\w)', '', s)
    return re.sub(r'\s+', ' ', s).strip()


def bracket_terms(s, starred):
    """[X]°STAR° -> {X} + kandidát glosáře; [X] -> {X}, když X vypadá jako německý termín."""
    def rep(m):
        inner, star = m.group(1).strip(), bool(m.group(2))
        if star:
            starred[inner] += 1
        is_cz = any(c in CZ for c in inner) or any(c in CZ_SOFT for c in inner)
        de_like = bool(re.search(r'(vnd|ß|ſ|eyst|meyst|knecht|[äöüå]|ck|tz|th|ff|sch[a-z]|^[A-Z][a-z]+$)', inner))
        if star:
            return '{' + inner + '}*'   # * = sem patří poznámka překladatele (zpracuje kontrola)
        if not is_cz and de_like:
            return '{' + inner + '}'
        return '[' + inner + ']'
    s = re.sub(r'\[([^\[\]]+)\](°STAR°)?', rep, s)
    return s.replace('°STAR°', '')


def parse_blocks(lines):
    """Řádky jedné strany -> seznam bloků (dict typ, text, lines, uroven)."""
    blocks, buf = [], []

    def flush():
        if not buf:
            return
        raw = [clean_inline(x) for x in buf]
        buf.clear()
        first = raw[0].lstrip()
        if first.startswith('> '):
            raw = [r.lstrip()[2:] if r.lstrip().startswith('> ') else r for r in raw]
            first = raw[0].lstrip()
        m = re.match(r'^(#{1,4})\s*(.*)$', first)
        if m and len(raw) == 1:
            txt = strip_emph(m.group(2).replace(' > ', ' '))
            img = re.search(r'!\[\]\[(image\d+)\]', txt)
            if img:
                blocks.append(dict(typ='obrazek', obrazek=img.group(1)))
                return
            if txt and not re.fullmatch(r'[\s*]*', txt):
                blocks.append(dict(typ='nadpis', uroven=len(m.group(1)), text=txt,
                                   italic=bool(re.match(r'^\*(\*\*)?(?!\*)', m.group(2).strip())) and m.group(2).strip().startswith(('*', '***'))
                                   and not m.group(2).strip().startswith('**') or m.group(2).strip().startswith('***')))
            return
        img = re.search(r'!\[\]\[(image\d+)\]', ' '.join(raw))
        if img:
            blocks.append(dict(typ='obrazek', obrazek=img.group(1)))
            rest = re.sub(r'\*?!\[\]\[image\d+\]\*?', '', ' '.join(raw)).strip(' *')
            if not rest:
                return
            raw = [rest]
        stripped = [r.strip() for r in raw]
        if all(re.match(r'^[*-] ', r) for r in stripped if r):
            items = [strip_emph(re.sub(r'^[*-] ', '', r)) for r in stripped if r]
            blocks.append(dict(typ='seznam', polozky=items, italic=all(re.match(r'^[*-] \*', r) for r in stripped if r)))
            return
        if len(raw) > 1 and all(r.endswith('  ') for r in raw[:-1]):
            blocks.append(dict(typ='verse', radky=[strip_emph(r) for r in raw if r.strip()]))
            return
        txt = strip_emph(' '.join(stripped))
        if txt:
            blocks.append(dict(typ='odstavec', text=txt, italic=bool(re.match(r'^\*(?!\*)', stripped[0]))))

    for l in lines:
        if not l.strip():
            flush()
        elif re.match(r'^\s*(#{1,4}|> #)', l):
            flush(); buf.append(l); flush()
        else:
            # položky seznamu za odstavcem bez prázdného řádku
            if buf and re.match(r'^\s*[*-] ', l) and not re.match(r'^\s*[*-] ', buf[-1]):
                flush()
            buf.append(l)
    flush()
    return blocks


def block_text(b):
    if b['typ'] == 'seznam':
        return ' '.join(b['polozky'])
    if b['typ'] == 'verse':
        return ' '.join(b['radky'])
    return b.get('text', '')


def gale_church(de, cs):
    """Monotónní zarovnání dvou posloupností bloků podle délky. Vrací seznam (de_idx[], cs_idx[])."""
    LD = [max(1, len(block_text(b))) for b in de]
    LC = [max(1, len(block_text(b))) for b in cs]
    ratio = (sum(LC) / max(1, sum(LD))) or 1.0
    n, m = len(de), len(cs)
    INF = float('inf')
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    moves = [(1, 1, 0), (1, 2, 2.5), (2, 1, 2.5), (1, 3, 4.5), (3, 1, 4.5), (2, 2, 3.5), (1, 0, 6), (0, 1, 6)]
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] == INF:
                continue
            for di, dj, pen in moves:
                a, b2 = i + di, j + dj
                if a > n or b2 > m:
                    continue
                ld, lc = sum(LD[i:a]), sum(LC[j:b2])
                if di and dj:
                    cost = abs((lc / ratio) - ld) / ((ld + lc / ratio) / 2) * 4 + pen
                    # typy (seznam / verš) by měly sedět
                    if any(de[k]['typ'] != 'odstavec' for k in range(i, a)) or any(cs[k]['typ'] != 'odstavec' for k in range(j, b2)):
                        if not (di == dj == 1 and de[i]['typ'] == cs[j]['typ']):
                            cost += 3
                else:
                    cost = pen
                if D[i][j] + cost < D[a][b2]:
                    D[a][b2] = D[i][j] + cost
                    B[a][b2] = (i, j)
    path, i, j = [], n, m
    while (i, j) != (0, 0):
        pi, pj = B[i][j]
        path.append((list(range(pi, i)), list(range(pj, j))))
        i, j = pi, pj
    return path[::-1]


def merge(blocks):
    """Sloučí několik bloků jednoho jazyka do jednoho pole pro dvojici."""
    if len(blocks) == 1:
        b = blocks[0]
        if b['typ'] == 'seznam':
            return b['polozky'], 'seznam'
        if b['typ'] == 'verse':
            return b['radky'], 'verse'
        return b['text'], b['typ']
    typs = {b['typ'] for b in blocks}
    if typs == {'seznam'}:
        return sum((b['polozky'] for b in blocks), []), 'seznam'
    return '\n\n'.join(block_text(b) if b['typ'] != 'seznam' else '\n'.join('- ' + x for x in b['polozky']) for b in blocks), 'odstavec'


def main():
    text = MD.read_text(encoding='utf-8')
    lines = text.split('\n')
    # --- obrázky
    (KNIHA / 'obrazky').mkdir(parents=True, exist_ok=True)
    images = {}
    for l in lines:
        m = re.match(r'^\[(image\d+)\]: <data:image/(\w+);base64,(.*)>$', l)
        if m:
            fn = f'{m.group(1).replace("image", "obrazek")}.{m.group(2)}'
            (KNIHA / 'obrazky' / fn).write_bytes(base64.b64decode(m.group(3)))
            images[m.group(1)] = fn
    end = next(i for i, l in enumerate(lines) if l.startswith('[image1]:'))
    body = lines[:end]

    # --- strany
    pg_re = re.compile(r'^(?:#### \*\*\*)?str\.? ([IVXLC]+)([qp]?)\s*\((\d+)[qp]?\)')
    start = next(i for i, l in enumerate(body) if l.startswith('# **Kriegsordnung**'))
    pages = [dict(id='titul', num=0, verso=False, lines=[])]
    for l in body[start:]:
        m = pg_re.match(l.strip())
        if m:
            num = roman(m.group(1))
            verso = bool(m.group(2))
            if num in (39, 59, 69):  # tisk tato čísla listů nemá
                continue
            pages.append(dict(id=page_id(num, verso), num=num, verso=verso, lines=[]))
            continue
        if l.strip() in ('####', '#', '##', '###', '# ', '## '):
            continue
        pages[-1]['lines'].append(l)

    starred = Counter()
    report = []
    (KNIHA / 'strany').mkdir(parents=True, exist_ok=True)
    out_pages = []
    for p in pages:
        blocks = parse_blocks(p['lines'])
        # jazyk
        last = 'de'
        for b in blocks:
            if b['typ'] == 'obrazek':
                b['lang'] = None
                continue
            lg = lang(block_text(b), b.get('italic', False))
            if lg is None:
                lg = last
            b['lang'] = lg
            last = lg
        # poznámky překladatele
        notes, kept, i = [], [], 0
        while i < len(blocks):
            b = blocks[i]
            t = block_text(b)
            if b['lang'] == 'cs' and re.match(r'^\(?\s*Pozn\.\s*p[řr]ekl\.?\s*:?', t):
                parts = [re.sub(r'^\(?\s*Pozn\.\s*p[řr]ekl\.?\s*:?\s*', '', t)] if b['typ'] != 'seznam' else []
                if b['typ'] == 'seznam':
                    parts = b['polozky']
                closed = t.rstrip().endswith(')') and t.count('(') <= t.count(')')
                j = i + 1
                while not closed and j < len(blocks) and blocks[j]['typ'] in ('odstavec', 'seznam') and blocks[j]['lang'] == 'cs':
                    tj = blocks[j]
                    if tj['typ'] == 'seznam':
                        parts += ['– ' + x for x in tj['polozky']]
                        closed = tj['polozky'][-1].rstrip().endswith(')')
                    else:
                        parts.append(tj['text'])
                        closed = tj['text'].rstrip().endswith(')')
                    j += 1
                note = '\n'.join(x for x in parts if x.strip()).strip()
                note = re.sub(r'\)\s*$', '', note).strip() if note.count('(') < note.count(')') or note.endswith(')') and '(' not in note else note
                notes.append(note)
                # odkaz do předchozího českého bloku
                for k in range(len(kept) - 1, -1, -1):
                    if kept[k]['lang'] == 'cs' and kept[k]['typ'] in ('odstavec', 'nadpis'):
                        kept[k]['text'] += f'[^{len(notes)}]'
                        break
                    if kept[k]['lang'] == 'cs' and kept[k]['typ'] == 'seznam':
                        kept[k]['polozky'][-1] += f'[^{len(notes)}]'
                        break
                i = j
                continue
            kept.append(b)
            i += 1
        blocks = kept
        # termíny v závorkách
        for b in blocks:
            if b['lang'] != 'cs':
                continue
            if 'text' in b:
                b['text'] = bracket_terms(b['text'], starred)
            for key in ('polozky', 'radky'):
                if key in b:
                    b[key] = [bracket_terms(x, starred) for x in b[key]]
        # párování: kotvy = nadpisy a obrázky
        out, warn = [], []
        de_run, cs_run = [], []

        def segment_pairs(de_run, cs_run):
            """Uvnitř úseku: nadpisy párovat podle pořadí, odstavce mezi nimi Gale–Church."""
            res = []
            dh = [k for k, b in enumerate(de_run) if b['typ'] == 'nadpis']
            ch = [k for k, b in enumerate(cs_run) if b['typ'] == 'nadpis']
            if len(dh) != len(ch):
                warn.append(f'nesouhlasí počet nadpisů DE {len(dh)} / CS {len(ch)}')
                # nadpisy navíc ber jako odstavce
                if len(dh) > len(ch):
                    for k in dh[len(ch):]:
                        de_run[k] = dict(de_run[k], typ='odstavec')
                    dh = dh[:len(ch)]
                else:
                    for k in ch[len(dh):]:
                        cs_run[k] = dict(cs_run[k], typ='odstavec')
                    ch = ch[:len(dh)]
            bd = [-1] + dh + [len(de_run)]
            bc = [-1] + ch + [len(cs_run)]
            for s in range(len(bd) - 1):
                if s > 0:
                    hd, hc = de_run[bd[s]], cs_run[bc[s]]
                    res.append(dict(typ='nadpis', uroven=min(hd['uroven'], 3), de=hd['text'], cs=hc['text']))
                    res += [dict(typ='obrazek', soubor=f) for f in hd.get('img_after', [])]
                dseg = de_run[bd[s] + 1:bd[s + 1]]
                cseg = cs_run[bc[s] + 1:bc[s + 1]]
                if not dseg and not cseg:
                    continue
                if not cseg:
                    for b in dseg:
                        v, t = merge([b])
                        res.append(dict(typ=t, de=v, cs=None))
                        res += [dict(typ='obrazek', soubor=f) for f in b.get('img_after', [])]
                    continue
                if not dseg:
                    for b in cseg:
                        v, t = merge([b])
                        res.append(dict(typ=t, de=None, cs=v))
                    continue
                if len(dseg) == len(cseg):
                    pairs = [([k], [k]) for k in range(len(dseg))]
                else:
                    pairs = gale_church(dseg, cseg)
                    warn.append(f'proporcionální párování {len(dseg)} DE : {len(cseg)} CS')
                for di, ci in pairs:
                    dv, dt = merge([dseg[k] for k in di]) if di else (None, None)
                    cv, ct = merge([cseg[k] for k in ci]) if ci else (None, None)
                    typ = dt or ct
                    if dt and ct and dt != ct:
                        typ = 'odstavec'
                        if isinstance(dv, list): dv = '\n'.join('- ' + x for x in dv)
                        if isinstance(cv, list): cv = '\n'.join('- ' + x for x in cv)
                    pair = dict(typ=typ, de=dv, cs=cv)
                    if len(di) != 1 or len(ci) != 1:
                        pair['zarovnat'] = True
                    res.append(pair)
                    for k in di:
                        res += [dict(typ='obrazek', soubor=f) for f in dseg[k].get('img_after', [])]
            return res

        state = None
        lead_imgs = []
        for b in blocks + [dict(typ='konec', lang='konec')]:
            if b['typ'] == 'obrazek':
                fn = images.get(b['obrazek'], b['obrazek'])
                if de_run:
                    de_run[-1].setdefault('img_after', []).append(fn)
                elif out:
                    out.append(dict(typ='obrazek', soubor=fn))
                else:
                    lead_imgs.append(fn)
                continue
            if b['typ'] == 'konec':
                if de_run or cs_run:
                    out += segment_pairs(de_run, cs_run)
                break
            if b['lang'] == 'de':
                if state == 'cs':  # nový úsek DE po českém
                    out += segment_pairs(de_run, cs_run)
                    de_run, cs_run = [], []
                de_run.append(b)
                state = 'de'
            else:
                cs_run.append(b)
                state = 'cs'
        if lead_imgs:
            k = 1 if out and out[0]['typ'] == 'nadpis' else 0
            out[k:k] = [dict(typ='obrazek', soubor=f) for f in lead_imgs]

        # pokračování odstavců přes hranici strany („…“)
        for blk in out:
            for key in ('de', 'cs'):
                v = blk.get(key)
                if isinstance(v, str):
                    v2 = re.sub(r'^\.\.\.\s*|^…\s*', '', v)
                    v2 = re.sub(r'\s*(\.\.\.|…)$', '', v2) if key == 'cs' else v2
                    blk[key] = v2
        if out:
            first, lastb = out[0], out[-1]
        stav = 'chybi_preklad' if all(not b.get('cs') for b in out if b['typ'] != 'obrazek') else 'prelozeno'
        if not out:
            stav = 'chybi_original'
        if stav == 'prelozeno' and any(b.get('de') and not b.get('cs') for b in out):
            stav = 'castecne'
        page = dict(
            id=p['id'],
            list=('titulní list' if p['id'] == 'titul' else _roman_label(p['num'])),
            strana=('recto' if not p['verso'] else 'verso'),
            sken=(1 if p['id'] == 'titul' else canvas(p['num'], p['verso'])),
            stav=stav, overeno_clovekem=False,
            bloky=out,
        )
        if notes:
            page['poznamky'] = [dict(n=k + 1, text=t) for k, t in enumerate(notes)]
        out_pages.append(page)
        if warn:
            report.append(f"{p['id']}: " + '; '.join(warn))

    # chybějící strany (v dokumentu nejsou vůbec): doplnit prázdné
    have = {p['id'] for p in out_pages}
    for num in range(1, 123):
        if num in (39, 59, 69):
            continue
        for verso in (False, True):
            pid = page_id(num, verso)
            if pid not in have:
                out_pages.append(dict(id=pid, list=_roman_label(num), strana='verso' if verso else 'recto',
                                      sken=canvas(num, verso), stav='chybi_original', overeno_clovekem=False, bloky=[]))
    # předsádka: věnování a předmluva (v pracovním překladu chybí)
    for pid, lbl, sk in (('venovani-1', 'věnování', 3), ('venovani-2', 'věnování', 4),
                         ('predmluva-1', 'předmluva', 5), ('predmluva-2', 'předmluva', 6)):
        out_pages.append(dict(id=pid, list=lbl, strana='recto' if sk % 2 else 'verso', sken=sk,
                              stav='chybi_original', overeno_clovekem=False, bloky=[]))
    front = ['titul', 'venovani-1', 'venovani-2', 'predmluva-1', 'predmluva-2']
    out_pages.sort(key=lambda p: front.index(p['id']) - 10 if p['id'] in front else int(p['id'][:3]) * 2 + (p['id'][3] == 'v'))
    for p in out_pages:
        dump(p, KNIHA / 'strany' / f"{p['id']}.yaml")
    (KNIHA / 'zdroje' / 'import_report.txt').write_text('\n'.join(report), encoding='utf-8')
    (KNIHA / 'zdroje' / 'hvezdickove_terminy.json').write_text(
        json.dumps(starred.most_common(), ensure_ascii=False, indent=0), encoding='utf-8')
    st = Counter(p['stav'] for p in out_pages)
    print('stran:', len(out_pages), dict(st))
    print('varování:', len(report), '| hvězdičkových termínů:', len(starred), '| obrázků:', len(images))


def _roman_label(n):
    vals = [(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IIII'), (1, 'I')]
    s = ''
    for v, r in vals:
        while n >= v:
            s += r; n -= v
    return s


class Dumper(yaml.SafeDumper):
    pass


def _str(dumper, s):
    if '\n' in s or len(s) > 70:
        return dumper.represent_scalar('tag:yaml.org,2002:str', s, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', s)


Dumper.add_representer(str, _str)


def dump(obj, path):
    # literal style nesnese koncové mezery
    def fix(o):
        if isinstance(o, dict):
            return {k: fix(v) for k, v in o.items()}
        if isinstance(o, list):
            return [fix(v) for v in o]
        if isinstance(o, str):
            return '\n'.join(x.rstrip() for x in o.split('\n')).strip()
        return o
    path.write_text(yaml.dump(fix(obj), Dumper=Dumper, allow_unicode=True, sort_keys=False, width=10_000), encoding='utf-8')


if __name__ == '__main__':
    main()
