"""Lavater: označí v překladu odkazy na mědirytiny značkou [[tab-NN|text]] (proklik na stranu s tabulí).

Lavater čísluje mědirytiny ve dvou řadách:
  - První díl (pevnost) a výklad cizích slov: „das 1./2. Kupffer(blat)“ = tab-01 / tab-02.
  - Třetí díl (šiky, str. 101–112): „blat I–VI“ = tab-07 … tab-12 (tab-04–06 jsou listy cvičení III–V).
Skript je idempotentní (již označená místa přeskočí). Použití:
  python -I nastroje/odkazy_rytiny.py            # provede změny
  python -I nastroje/odkazy_rytiny.py --zkouska  # jen vypíše, co by změnil
"""
import re, sys, pathlib
import yaml
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from import_md import dump

S = pathlib.Path(__file__).resolve().parent.parent / 'knihy' / 'lavater-1651' / 'strany'
ZKOUSKA = '--zkouska' in sys.argv
NEOZNACENO = r'(?<![\[|])'          # mimo již existující [[…|…]]

# Třetí díl: pořadové číslo listu se šiky → tabule (list I = tab-07)
RADA3 = {'prvn': 'tab-07', 'druh': 'tab-08', 'třet': 'tab-09', 'čtvrt': 'tab-10', 'pát': 'tab-11', 'šest': 'tab-12',
         '11.': 'tab-08'}   # „das 11. Kupfferblat“ = tisková chyba místo II. (viz pozn. na str. 103)
RX3 = re.compile(NEOZNACENO + r'\b((?:výše (?:uvedenou|zmíněn\w*) )?(prvn\w*|druh\w*|třetí|čtvrt\w*|pát\w*|šest\w*|11\.) mědirytin\w*)')
RX_VYKLAD = re.compile(NEOZNACENO + r'\b(([12])\. mědirytin\w*)')
RX_TAB = re.compile(NEOZNACENO + r'\b(tab-(\d\d))\b(?!\])')

# ruční místa: (strana, hledaný text, náhrada)
RUCNE = [
    ('101', 'na výše zmíněné mědirytině', 'na [[tab-08|výše zmíněné mědirytině]]'),
    ('110', 'jak ukazuje velké číslo I[^3]', 'jak ukazuje [[tab-12|velké číslo I]][^3]'),
    ('vazba', 'I. První mědirytina {Kupfferblat}', 'I. [[tab-01|První mědirytina]] {Kupfferblat}'),
    ('vazba', 'malý přistřižený list s věží', '[[tab-03|malý přistřižený list s věží]]'),
    ('vazba', 'druhý malý list s kůlovými ploty', '[[tab-02|druhý malý list]] s kůlovými ploty'),
    ('vazba', 'II. Cvičení {Exercitium} s mušketou', 'II. [[tab-04|Cvičení]] {Exercitium} s mušketou'),
    ('vazba', 'druhé, s píkami', '[[tab-05|druhé]], s píkami'),
    ('vazba', 'třetí, se štíty', '[[tab-06|třetí]], se štíty'),
    ('vazba', 'III. Přistřižený list o zdvojování', 'III. [[tab-07|Přistřižený list o zdvojování]]'),
    ('slovnicek-2', '1. První a druhá mědirytina', '1. [[tab-01|První]] a [[tab-02|druhá]] mědirytina'),
    ('slovnicek-2', 's mušketami před 1. stranu, s píkou a se štítem', '[[tab-04|s mušketami]] před 1. stranu, [[tab-05|s píkou]] a [[tab-06|se štítem]]'),
    ('slovnicek-2', '3. Sedmá mědirytina', '3. [[tab-07|Sedmá mědirytina]]'),
    ('errata', 'vyobrazeno na mědirytině', 'vyobrazeno [[tab-05|na mědirytině]]'),
]


def rada3(m):
    return f'[[{RADA3[next(k for k in RADA3 if m.group(2).lower().startswith(k))]}|{m.group(1)}]]'


def uprav(s, fce):
    if isinstance(s, list):
        return [uprav(x, fce) for x in s]
    return fce(s) if isinstance(s, str) else s


celkem = 0
for f in sorted(S.glob('*.yaml')):
    pid = f.stem
    d = yaml.safe_load(f.read_text(encoding='utf-8'))
    puvodni = yaml.dump(d, allow_unicode=True)
    fce = []
    if re.fullmatch(r'1(0[1-9]|1[0-2])', pid):
        fce.append(lambda s: RX3.sub(rada3, s))
    if pid.startswith('vyklad-'):
        fce.append(lambda s: RX_VYKLAD.sub(lambda m: f'[[tab-0{m.group(2)}|{m.group(1)}]]', s))
    for p, a, b in RUCNE:
        if p == pid:
            fce.append(lambda s, a=a, b=b: s.replace(a, b) if b not in s else s)
    for b in d.get('bloky') or []:
        for g in fce:
            b['cs'] = uprav(b.get('cs'), g)
        if b.get('popis'):   # odkazy „tab-NN“ v popisech tabulí
            b['popis'] = RX_TAB.sub(lambda m: f'[[{m.group(1)}|{m.group(1)}]]' if m.group(1) != pid else m.group(1), b['popis'])
    for n in d.get('poznamky') or []:
        n['text'] = RX_TAB.sub(lambda m: f'[[{m.group(1)}|{m.group(1)}]]', str(n['text']))
    nove = yaml.dump(d, allow_unicode=True)
    if nove != puvodni:
        k = len(re.findall(r'\[\[', nove)) - len(re.findall(r'\[\[', puvodni))
        celkem += k
        print(f'{pid}: +{k}')
        if not ZKOUSKA:
            dump(d, f)
print(f'— celkem {celkem} odkazů' + (' (zkouška, nic nezapsáno)' if ZKOUSKA else ''))
