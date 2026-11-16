"""Rozdělí TEI přepis z Deutsches Textarchiv (DTA) po stranách (snímcích) do zdroje/dta/NNNN.txt.

Použití: python -I nastroje/dta_strany.py knihy/lavater-1651 zdroje/lavater_dta.xml

Výstup na stranu (NNNN = číslo snímku, odpovídá poli `sken`):
  první řádek „# strana N“ (je-li číslovaná), pak odstavce oddělené prázdným řádkem;
  nadpisy začínají „## “, položky seznamů „- “, řádky tabulek „| … |“, marginálie „[Marg.: …]“,
  obrázky „[obrázek]“. Živá záhlaví, kustody, signatury a čísla stran (fw) se vynechávají.
Text se normalizuje stejně jako v edici (funkce `normalizuj`): ſ→s, uͤ→ü, ꝛ→r, m̃→mm, ñ→nn; pravopis zůstává.
"""
import re, sys, pathlib, unicodedata
import xml.etree.ElementTree as ET

TEI = '{http://www.tei-c.org/ns/1.0}'


def normalizuj(t):
    """Typografické znaky starého tisku → běžná písmena (pravopis beze změny)."""
    t = t.replace('ſ', 's').replace('ꝛ', 'r').replace('ʒ', 'z')
    t = unicodedata.normalize('NFD', t)
    t = re.sub(r'([aouAOU])ͤ', lambda m: {'a': 'ä', 'o': 'ö', 'u': 'ü', 'A': 'Ä', 'O': 'Ö', 'U': 'Ü'}[m.group(1)], t)
    t = re.sub(r'([mn])̃', r'\1\1', t)          # m̃ → mm, ñ → nn
    t = t.replace('ͤ', '').replace('̃', '')  # zbylé nadepsané e / vlnovky
    t = unicodedata.normalize('NFC', t)
    t = t.replace('’', '’')
    return t


class Strany:
    def __init__(self):
        self.strany = {}      # facs -> seznam bloků (str)
        self.cisla = {}       # facs -> n
        self.facs = None
        self.buf = []         # rozpracovaný blok (části textu)
        self.prefix = ''

    def novy_blok(self, prefix=''):
        self.konec_bloku()
        self.prefix = prefix

    def konec_bloku(self):
        t = ''.join(self.buf)
        t = re.sub(r'[-¬]\s*\n\s*(?=[a-zäöüßſꝛ])', '', t)  # dělení slov na konci řádku (i před dlouhým ſ)
        t = re.sub(r'\s+', ' ', t).strip()
        if t and self.facs:
            self.strany.setdefault(self.facs, []).append(self.prefix + normalizuj(t))
        self.buf, self.prefix = [], ''

    def text(self, t):
        if t:
            self.buf.append(t)


def chod(el, S, v_hlave=False):
    tag = el.tag.replace(TEI, '')
    if tag == 'pb':
        S.konec_bloku()
        S.facs = el.get('facs', '').lstrip('#f')
        if el.get('n'):
            S.cisla[S.facs] = el.get('n')
        S.text(el.tail)
        return
    if tag in ('fw',):              # živé záhlaví, kustody, signatury
        S.text(el.tail)
        return
    if tag == 'lb':
        S.text('\n')
        S.text(el.tail)
        return
    if tag == 'figure':
        S.novy_blok(); S.buf = ['[obrázek]']; S.konec_bloku()
        S.text(el.tail)
        return
    if tag == 'choice':             # opravy a rozvedené zkratky: corr / expan / reg
        vyber = None
        for pref in ('corr', 'expan', 'reg'):
            vyber = el.find(TEI + pref)
            if vyber is not None:
                break
        if vyber is None and len(el):
            vyber = el[0]
        if vyber is not None:
            S.text(''.join(vyber.itertext()))
        S.text(el.tail)
        return
    if tag == 'note':
        S.text(' [Marg.: ' + re.sub(r'\s+', ' ', ''.join(el.itertext())).strip() + '] ')
        S.text(el.tail)
        return
    blokove = {'head': '## ', 'p': '', 'item': '- ', 'row': '| ', 'l': '', 'byline': '', 'dateline': '', 'closer': '',
               'salute': '', 'signed': '', 'trailer': '', 'docTitle': '', 'titlePart': '', 'docImprint': '', 'argument': ''}
    je_blok = tag in blokove
    if je_blok:
        S.novy_blok(blokove[tag])
    S.text(el.text)
    for ch in el:
        if ch.tag.replace(TEI, '') == 'cell':
            S.text(''.join(ch.itertext()).strip() + ' | ')
            S.text(ch.tail)
        else:
            chod(ch, S)
    if je_blok:
        S.konec_bloku()
    S.text(el.tail)


def main():
    kniha = pathlib.Path(sys.argv[1])
    tei = ET.parse(kniha / sys.argv[2]).getroot()
    text = tei.find(TEI + 'text')
    S = Strany()
    chod(text, S)
    S.konec_bloku()
    out = kniha / 'zdroje' / 'dta'
    out.mkdir(parents=True, exist_ok=True)
    for facs, bloky in sorted(S.strany.items()):
        hlavicka = f'# strana {S.cisla[facs]}\n\n' if facs in S.cisla else ''
        (out / f'{facs}.txt').write_text(hlavicka + '\n\n'.join(bloky) + '\n', encoding='utf-8')
    print(len(S.strany), 'stran s textem;', len(S.cisla), 'číslovaných')


if __name__ == '__main__':
    main()
