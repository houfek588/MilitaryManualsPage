"""Sjednotí přepis zkratek tisku v německém textu (pole de) podle PRAVIDLA_PREKLADU.md § 2.

  ꝛc. / rc. / 2c. → etc.     vñ → vnd     jiné ñ → nn (Wañ → Wann)     Herꝛ → Herr
Použití: python -I nastroje/normalizuj_zkratky.py knihy/<kniha> <id> [<id> …]
Upravuje jen zadané strany (ať se nekříží s rozpracovanou prací agentů). Vypíše změny.
"""
import re, sys, pathlib, yaml
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from import_md import dump  # stejný formát YAML


def norm(s):
    s = re.sub(r'(?<![\w])(ꝛc|rc|2c)\.', 'etc.', s)
    s = re.sub(r'\bvñ\b', 'vnd', s)
    s = s.replace('ñ', 'nn').replace('Herꝛ', 'Herr').replace('ꝛ', 'r')
    return s


def walk(v):
    if isinstance(v, str):
        return norm(v)
    if isinstance(v, list):
        return [walk(x) for x in v]
    return v


def main():
    kniha = pathlib.Path(sys.argv[1])
    sys.stdout.reconfigure(encoding='utf-8')
    for pid in sys.argv[2:]:
        f = kniha / 'strany' / f'{pid}.yaml'
        d = yaml.safe_load(f.read_text(encoding='utf-8'))
        n = 0
        for b in d.get('bloky') or []:
            if b.get('de') is not None:
                nove = walk(b['de'])
                if nove != b['de']:
                    n += 1
                    b['de'] = nove
        if n:
            dump(d, f)
            print(f'{pid}: upraveno {n} bloků')


if __name__ == '__main__':
    main()
