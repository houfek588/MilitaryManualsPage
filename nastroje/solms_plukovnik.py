"""Solms: sjednocení překladu (rozhodnutí autora 2026-11-17).

1. Oberst / Oberster / Obersten (samostatně) = „plukovník“ – dříve střídavě „nejvyšší velitel“, „nejvyšší polní
   hejtman“, „představený“. Složeniny (Oberster Feldhauptman, Oberster Zeugmeister…) se nemění.
2. Fendlin / Fendlein u jízdy = „korouhev“ (u pěchoty zůstává „praporec“).

Použití: python -I nastroje/solms_plukovnik.py [--zkouska]
"""
import re, sys, pathlib, yaml
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from import_md import dump

sys.stdout.reconfigure(encoding='utf-8')
S = pathlib.Path(__file__).resolve().parent.parent / 'knihy' / 'solms-1559' / 'strany'
ZKOUSKA = '--zkouska' in sys.argv

# „nejvyšší velitel“ ve všech pádech → „plukovník“ (v knize se tak překládá výhradně samostatné Oberst/Oberster/Obersten)
VELITEL = [
    ('nejvyššího velitele', 'plukovníka'), ('nejvyššímu veliteli', 'plukovníkovi'), ('nejvyšším velitelem', 'plukovníkem'),
    ('nejvyšším veliteli', 'plukovníkovi'), ('nejvyšší velitelé', 'plukovníci'), ('nejvyšších velitelů', 'plukovníků'),
    ('nejvyšším velitelům', 'plukovníkům'), ('nejvyššími veliteli', 'plukovníky'), ('nejvyšších velitelích', 'plukovnících'),
    ('nejvyšší velitele', 'plukovníky'), ('nejvyšší velitel', 'plukovník'),
]
OBERST = r'\{Obe?r(?:i)?st(?:er|en)?\}'
# jiné dřívější překlady samostatného Oberst (jen se značkou)
JINE = [
    (r'nejvyššího polního hejtmana (' + OBERST + ')', r'plukovníka \1'),
    (r'nejvyššímu polnímu hejtmanovi (' + OBERST + ')', r'plukovníkovi \1'),
    (r'nějaký představený (' + OBERST + ')', r'nějaký plukovník \1'),
]
# Fendlin u jízdy → korouhev (strana, hledaný text, náhrada)
KOROUHEV = [
    ('1-010r', 'ani u svých praporců {Fendlin}', 'ani u svých korouhví {Fendlin}'),
    ('1-010v', 'pod jedním praporcem {Fendlein} nebo pod stem koní', 'pod jednou korouhví {Fendlein} nebo pod stem koní'),
    ('1-020r', 'se svým praporcem {Fendlein}[^1] a jezdci', 'se svou korouhví {Fendlein}[^1] a jezdci'),
    ('036v', 'z každého praporce má být vzat jeden, ať už u jízdy nebo u pěchoty',
     'z každé korouhve či praporce {Fendlin} má být vzat jeden, ať už u jízdy, nebo u pěchoty'),
]
POZN_1020R = ('V První knize užívá Solms místy výraz *Fendlein* (praporec) i pro jízdní oddíl, zatímco v Druhé knize jej vymezuje pro pěchotu a pro jízdu užívá výraz *Fahne* / *Fanen* (korouhev).',
              'Solms užívá v První knize výraz *Fendlein* (praporec) místy i pro jízdní oddíl; u jízdy jej překládáme „korouhev“, stejně jako *Fahne* / *Fanen* v Druhé knize.')


def velke(z, vzor):
    return z[0].upper() + z[1:] if vzor[0].isupper() else z


def uprav_text(s):
    n = 0
    for a, b in VELITEL:
        s, k = re.subn(r'\b' + a + r'\b', lambda m, b=b: velke(b, m.group(0)), s, flags=re.I)
        n += k
    for a, b in JINE:
        s, k = re.subn(a, b, s)
        n += k
    return s, n


celkem = 0
for f in sorted(S.glob('*.yaml')):
    pid = f.stem
    d = yaml.safe_load(f.read_text(encoding='utf-8'))
    n = 0
    for b in d.get('bloky') or []:
        cs = b.get('cs')
        if isinstance(cs, str):
            de = str(b.get('de') or '')
            if re.search(r'\bObe?r(?:i)?st', de):          # jen bloky, kde originál Obersta skutečně má
                cs, k = uprav_text(cs)
                n += k
            for p, a, z in KOROUHEV:
                if p == pid and a in cs:
                    cs = cs.replace(a, z)
                    n += 1
            b['cs'] = cs
    for p in d.get('poznamky') or []:
        if pid == '1-020r' and POZN_1020R[0] in str(p['text']):
            p['text'] = str(p['text']).replace(*POZN_1020R)
            n += 1
    if n:
        celkem += n
        print(f'{pid}: {n}')
        if not ZKOUSKA:
            dump(d, f)
print(f'— celkem {celkem} změn' + (' (zkouška)' if ZKOUSKA else ''))
