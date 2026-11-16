"""Označí v překladu, popisech obrázků a poznámkách odkazy na čísla stran („Čti s. 5 a 7“, „str. 58–59“,
„na 13. řádku 3. strany“) značkou [[id strany|číslo]] – na webu z nich je proklik.

Jen pro knihy se stránkováním (kniha.yaml: strankovani: strany); číslo se páruje s polem `list` strany.
Skript je idempotentní (již označená místa přeskočí). Použití:
  python -I nastroje/odkazy_strany.py knihy/lavater-1651             # provede změny
  python -I nastroje/odkazy_strany.py knihy/lavater-1651 --zkouska   # jen vypíše, co by změnil
"""
import re, sys, pathlib
import yaml
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from import_md import dump

args = [a for a in sys.argv[1:] if not a.startswith('--')]
ZKOUSKA = '--zkouska' in sys.argv
KNIHA = pathlib.Path(args[0])
# strany, kde čísla neodpovídají stránkování tohoto vydání (starší pokyn knihaři počítá strany po dílech)
VYNECHAT = {'slovnicek-2'}
# ruční doplnění: (strana, hledaný text, náhrada)
RUCNE = [('vazba', 'za 82. a', 'za [[082|82.]] a')]
MAX_ROZSAH = 10      # rozsahy delší než 10 stran (např. „strany 1–134“) nejsou odkaz na konkrétní místo

meta = yaml.safe_load((KNIHA / 'kniha.yaml').read_text(encoding='utf-8'))
assert meta.get('strankovani') == 'strany', 'skript je jen pro knihy se stránkováním (strankovani: strany)'
cislo = {}
for f in (KNIHA / 'strany').glob('*.yaml'):
    m = re.search(r"^list: '?(\d+)'?$", f.read_text(encoding='utf-8'), re.M)
    if m:
        cislo[int(m.group(1))] = f.stem

CISLA = r'\d+(?:–\d+)?(?:(?:, | a )\d+(?:–\d+)?)*'
RX_PRED = re.compile(r'\b(?:s\.|str\.|strana|strany|straně|stranu|stranách|stranám)\s+(' + CISLA + r')(?![\d.]\d)')
RX_ZA = re.compile(r'\b(\d+)\. (strany|stranu|straně)\b')
RX_ODKAZ = re.compile(r'(\[\[[^|\]]+\|[^\]]+\]\])')


def odkaz(n, text, pid):
    cil = cislo.get(int(n))
    return f'[[{cil}|{text}]]' if cil and cil != pid else text


def seznam(s, pid):
    def rozsah(m):
        a, b = m.group(1), m.group(2)
        if b and int(b) - int(a) > MAX_ROZSAH:
            return m.group(0)
        return odkaz(a, a, pid) + (('–' + odkaz(b, b, pid)) if b else '')
    return re.sub(r'(\d+)(?:–(\d+))?', rozsah, s)


def oznac(text, pid):
    if not isinstance(text, str):
        return text
    casti = RX_ODKAZ.split(text)            # existující odkazy nech být
    for i in range(0, len(casti), 2):
        s = casti[i]
        s = RX_PRED.sub(lambda m: m.group(0)[:m.start(1) - m.start(0)] + seznam(m.group(1), pid), s)
        s = RX_ZA.sub(lambda m: odkaz(m.group(1), m.group(0), pid), s)
        casti[i] = s
    return ''.join(casti)


def uprav(v, fce):
    if isinstance(v, list):
        return [uprav(x, fce) for x in v]
    return fce(v)


celkem = 0
for f in sorted((KNIHA / 'strany').glob('*.yaml')):
    pid = f.stem
    if pid in VYNECHAT:
        continue
    d = yaml.safe_load(f.read_text(encoding='utf-8'))
    pred = yaml.dump(d, allow_unicode=True)
    for b in d.get('bloky') or []:
        for pole in ('cs', 'popis'):
            if b.get(pole):
                b[pole] = uprav(b[pole], lambda s: oznac(s, pid))
                for p, a, z in RUCNE:
                    if p == pid:
                        b[pole] = uprav(b[pole], lambda s: s.replace(a, z) if isinstance(s, str) and z not in s else s)
    for n in d.get('poznamky') or []:
        n['text'] = oznac(str(n['text']), pid)
    po = yaml.dump(d, allow_unicode=True)
    if po != pred:
        k = po.count('[[') - pred.count('[[')
        celkem += k
        print(f'{pid}: +{k}')
        if not ZKOUSKA:
            dump(d, f)
print(f'— celkem {celkem} odkazů' + (' (zkouška, nic nezapsáno)' if ZKOUSKA else ''))
