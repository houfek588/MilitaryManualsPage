# Pravidla překladu a datového formátu

Platí pro všechny knihy v `knihy/` a pro oba agenty (`.claude/agents/prekladatel.md`, `.claude/agents/kontrola-prekladu.md`).
Konkrétní kniha může mít výjimky v `knihy/<kniha>/kniha.yaml` (pole `poznamky_k_prekladu`).

## 1. Jeden soubor = jedna strana tisku

`knihy/<kniha>/strany/<id>.yaml`, např. `018r.yaml` = list XVIII, líc (recto); `018v.yaml` = rub (verso).
Tisk číslovaný po listech (foliace): na líci je římské číslo, rub je bez čísla.

```yaml
id: 018r
list: XVIII            # číslo listu, jak je v tisku
strana: recto          # recto = líc (pravá strana dvojstrany), verso = rub (levá)
sken: 43               # pořadí skenu v digitalizaci (viz kniha.yaml → sken)
stav: zkontrolovano    # chybi_original | chybi_preklad | castecne | prelozeno | zkontrolovano
overeno_clovekem: false  # true = stranu prošel a schválil člověk (nastavuje JEN člověk, viz § 5)
# overeno_datum: '2026-11-13'   # doplní nástroj overeno_clovekem.py
# overeno_kdo: 'jméno'          # volitelné
bloky:
- typ: nadpis          # nadpis | odstavec | seznam | verse | obrazek | tabulka
  uroven: 2            # jen u nadpisu: 1 = kniha/hlavní část, 2 = kapitola, 3 = podkapitola
  de: Das ander Buch …
  cs: Druhá kniha …
- typ: odstavec
  pokracovani: true    # odstavec pokračuje z předchozí strany (první blok strany)
  de: |-
    …německý text…
  cs: |-
    …český překlad…[^1]
- typ: seznam          # de i cs jsou seznamy položek, stejný počet
  de: [Leutenandt., Kriegßräth]
  cs: ['poručík {Leutenandt}', 'váleční radové {Kriegßräth}']
- typ: verse           # verše: seznam řádků; počet řádků DE a CS by měl sedět
  de: [ … ]
  cs: [ … ]
- typ: tabulka         # řádky × sloupce
  de: [[…, …], …]
  cs: [[…, …], …]
- typ: obrazek
  soubor: obrazek4.png # v knihy/<kniha>/obrazky/
  popis: Krátký český popis vyobrazení (co je na dřevořezu / nákresu).
poznamky:              # poznámky překladatele k této straně
- n: 1
  text: Vysvětlení …
```

### Zrcadlové párování (nejdůležitější pravidlo)
- Každý blok obsahuje **německý originál a jeho český překlad, které si odpovídají 1 : 1**.
  Na webu stojí vedle sebe; když nesedí, sloupce se rozjedou.
- Členění řídí **tisk**: jeden odstavec tisku = jeden blok. Odstavec v tisku začíná nový řádek s odsazením,
  často slovem *Item*, *Zum ersten/andern…*, *So…*, nebo iniciálou. Český překlad rozděl/sluč přesně podle toho.
- Nadpisy jsou **kotvy**: nadpis je vždy samostatný blok, nikdy se neslučuje s textem.
- Odstavec přecházející na další stranu se rozdělí na hranici strany: konec patří na tuto stranu, pokračování
  na další stranu s `pokracovani: true`. Český text rozděl ve stejném místě věty (bez „…“).
- Řádková záhlaví tisku (*Das ander Buch.*, *Das Vierdt Buch*), čísla listů a kustody (*A ij*, slovo pod textem,
  které opakuje první slovo další strany) **nejsou text** – vynech je.
- Slovo rozdělené přes hranici stran (*erma-|nen*) patří celé na stranu, **kde končí** (tj. na následující).
- Svorky a marginálie ve výčtech (*gehören vnter den Profosen*) připoj k poslední položce skupiny: „… – gehören vnter den Profosen.“
- Ve výčtech úřadů je každá položka termín: `{…}` jen při prvním výskytu na stránce, opakovaně („jeho poručík“) bez závorky.
- **Dřevořezy a vyobrazení**, která jsou na skenu, ale nemají v datech blok `obrazek`, doplň jako blok na správné místo:
  `typ: obrazek`, `soubor: drevorez-<sken>.jpg` (NN = číslo skenu; druhý obrázek na téže straně `drevorez-<sken>b.jpg`)
  a `popis`. Soubor nevytvářej – výřez ze skenu doplní správce projektu.

## 2. Německý originál (`de`)
- Zachovej dobový pravopis tisku: *vnd, seyn, Kriegßvolck, jhm, auff, Profoß*. Nemodernizuj.
- **Oprav chyby OCR** podle smyslu a podle tisku: dlouhé *ſ* čtené jako *f* (*foll → soll, ift → ist, fein → sein*,
  ale *Fein(d)* zůstává), *ond → vnd*, *Herz → Herr* (zkratka *Herꝛ*), *k → tz* (*Geschük → Geschütz, ganken → gantzen*),
  *ß/ſs*, rozdělená slova přes konec řádku (*fürnem lichsten → fürnemlichsten*), *Xoffz → Roß* apod.
  Když si nejsi jistý, podívej se do skenu (viz § 6). Zjevnou tiskovou chybu originálu ponech.
- Lomítko */* je dobová čárka (virgule) – ponech ho.
- Znaky tisku jednotně: *å* (a s nadepsaným e) → *ä*; *ů* ponech; zkratky s nadtržením rozepiš (*vñ → vnd, gegē → gegen*);
  *ꝛc.* (OCR čte jako *rc.*, *2c.*, *2.*) → *etc.*; *Herꝛ* → *Herr*.
- `seznam` použij pro soupisy krátkých položek bez slovesa (výčty úřadů, sazebníky, inventáře); odstavce tisku
  s celými větami („Item ein Wagen, darauff man …“) ponech jako samostatné bloky `odstavec`.
- Iniciály, které OCR vynechává (*Ere, As*), doplň v podobě tisku – zdobná iniciála + velké druhé písmeno: *WEre, DAs, SEin*.
- *Item* na začátku odstavce překládej jednotně „Dále“.
- Odstraň zbytky formátování (`*`, `\`), zalomení řádků uvnitř odstavce a dělení slov.

## 3. Český překlad (`cs`)
- Věrný, ale **plynulý a čtivý**: spisovná současná čeština s lehkým dobovým zabarvením. Žádný doslovný
  „německý slovosled“, ale ani převyprávění. Dlouhá souvětí se lomítky smíš rozdělit na víc vět.
- Zachovej obsah úplně: nic nevypouštěj, nic nepřidávej. Doplněk nutný pro srozumitelnost dej do
  hranatých závorek: „má [uvážit], jaká města…“.
- **Terminologie podle `glosar.yaml`** (pole `cs`) – závazná. Termíny z rubriky `nepouzivat` nepoužívej.
- Původní termín uveď ve **složených závorkách** `{…}` v podobě z tisku, a to **při prvním výskytu na stránce**:
  „profous {Profoß}“. Dál na stránce už bez závorky. Web z {…} udělá odkaz do glosáře.
- `{…}` smíš dát i u odborného termínu, který v glosáři není (web ho zobrazí bez odkazu) – a navrhni ho do glosáře.
  **Vlastní jména do `{…}` nedávej**; původní podobu jména uveď případně v poznámce.
- Vlastní jména: ustálená česká podoba (Maxmilián, Titus Livius, Frankfurt nad Mohanem), u méně známých
  původní podoba.
- Čísla, míry a mince přelož přesně (žádné přepočty v textu; přepočet patří do poznámky).
- Oslovení a formule listin (*N.*, *E. F. G.*) překládej dobově: „N.“, „Vaše knížecí Milost“.
- Uvozovky „…“, pomlčka –, tři tečky …, nezlomitelné mezery netřeba.

## 4. Poznámky překladatele
- Archaické nebo sporné termíny, věcné nejasnosti, dobové reálie → poznámka `poznamky` + značka `[^n]` za slovem
  v `cs` (číslování od 1 na každé stránce).
- Když termín vysvětluje heslo glosáře (`pozn`), poznámku nepiš – web glosářovou poznámku zobrazí sám.
  Navrhni raději doplnění glosáře (viz zpráva agenta).
- Značka `{Termín}*` z pracovního překladu = „sem patří poznámka“: vyřeš ji (poznámka nebo heslo glosáře)
  a hvězdičku odstraň.
- Nákresy, tabulky a vyobrazení převeď do srozumitelné textové podoby: u `obrazek` napiš `popis`, tabulky
  jako `tabulka`, výpočty šiků jako seznam nebo tabulku.

## 5. Stav strany
`chybi_original` → `chybi_preklad` → `prelozeno` → `zkontrolovano`. Kontrolor po kontrole nastaví `zkontrolovano`.

`stav: zkontrolovano` znamená strojovou kontrolu (agent kontrola-prekladu). Ruční kontrolu člověkem
zaznamenává samostatné pole **`overeno_clovekem`**:
- `false` = stranu zatím ověřil jen stroj; `true` = stranu prošel a schválil člověk (+ `overeno_datum`, volitelně `overeno_kdo`).
- Nastavuje se příkazem `python -I nastroje/overeno_clovekem.py knihy/<kniha> 001r 001v` (rozsah `001r-010v`,
  jméno `--kdo "…"`, zrušení `--zrusit`, přehled `--prehled`).
- **Agenti (překladatel i kontrolor) toto pole nikdy nenastavují na `true` a nemažou ho.** Když agent na straně
  s `overeno_clovekem: true` provede věcnou změnu textu, nastaví `overeno_clovekem: false`, smaže `overeno_datum`
  a `overeno_kdo` a změnu uvede ve zprávě, aby ji člověk znovu ověřil.

## 6. Pomůcky
- `knihy/<kniha>/zdroje/ocr_bsb/NNNN.txt` – OCR skenu NNNN (číslo = `sken`), po řádcích. Na kontrolu úplnosti.
- Sken strany: `https://api.digitale-sammlungen.de/iiif/image/v2/bsb00045899_000NN/full/1400,/0/default.jpg`
  (NN = `sken`, doplněno na 5 číslic: `bsb00045899_00043`). Stáhni `curl -s -o <scratchpad>/s43.jpg <url>` a otevři
  nástrojem Read – použij jen při pochybnostech (čísla, termíny, nečitelné OCR).
- Kontrola souborů: `python -I nastroje/over_strany.py knihy/<kniha> 018r 018v …` (bez seznamu = všechny).
