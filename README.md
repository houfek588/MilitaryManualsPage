# Vojenské manuály – dvojjazyčné edice

Digitální edice raně novověkých vojenských příruček: německý originál (podle skenu) a český překlad,
čtené vedle sebe, s poznámkami překladatele, věcným rejstříkem, odkazy na skeny a exportem do PDF.

Web je čistě statický (HTML + CSS + JS, data vložená jako `<script>`), takže:
- **offline**: sestav web (`python -I nastroje/build.py`) a otevři `docs/index.html` dvojklikem,
- **GitHub Pages**: web sestavuje a nasazuje GitHub Actions (`.github/workflows/pages.yml`) při každém pushi do `main`:
  zkontroluje data všech knih (`over_strany.py`; chyba = nenasadí se), spustí `build.py` a nasadí `docs/`.
  Nastavení repozitáře: Settings → Pages → Build and deployment → Source: **GitHub Actions**.
  Lokálně se `docs/` dál sestavuje příkazem `python -I nastroje/build.py` (náhled, offline použití).

## Struktura

```
PRAVIDLA_PREKLADU.md        pravidla překladu a popis datového formátu (závazné pro lidi i agenty)
PRIDANI_KNIHY.md            postup přidání nové knihy (podklady → import → glosář → agenti → build)
projekt.yaml                nastavení webu: autor, kontakt, skupina, sociální sítě, údaje pro podporu (dar), Google formulář „nahlásit chybu“ (formular)
knihy/
  fronsberger-1564/
    kniha.yaml              metadata knihy, zdroj skenů, pořadí předsádky, pokyny k překladu
    glosar.yaml             jednotná terminologie = věcný rejstřík (hesla, kategorie, poznámky)
    strany/<id>.yaml        ZDROJ PRAVDY: jedna strana tisku = jeden soubor (bloky DE ↔ CS, poznámky)
    obrazky/                vyobrazení z pracovního překladu + dřevořezy vyříznuté ze skenu (drevorez-<sken>.jpg)
    zdroje/                 OCR skenů (ocr_bsb/), IIIF manifest, zprávy z kontrol (kontrola/)
    SPORNA_MISTA.md         souhrn sporných míst překladu k rozhodnutí
nastroje/
  import_md.py              jednorázový import pracovního překladu z Google Docs (.md)
  migrace_sken_45899.py     jednorázový přechod na úplný sken (doplnění 3 vynechaných dvojstran)
  stahni_ocr_bsb.py         stažení OCR z digitale-sammlungen.de
  dta_strany.py             rozdělení přepisu Deutsches Textarchiv (TEI) po stranách → zdroje/dta/NNNN.txt
  import_lavater.py         jednorázový import pracovního překladu Lavatera (.md)
  import_bern.py            jednorázový import pracovního překladu Bernské příručky (.md)
  import_solms.py           jednorázový import a příprava stran Solmse (.md + hOCR BSB)
  over_strany.py            kontrola dat (struktura, párování, poznámky, terminologie)
  odkazy_rytiny.py          Lavater: označení odkazů na mědirytiny v překladu značkou [[tab-NN|text]]
  odkazy_strany.py          označení odkazů na čísla stran („Čti s. 5“) značkou [[id|text]] (knihy se stránkováním)
  normalizuj_zkratky.py     sjednocení přepisu zkratek tisku (ꝛc., vñ, …)
  overeno_clovekem.py       označení stran, které ručně ověřil člověk (pole overeno_clovekem)
  vyrez_drevorezy.py        výřez dřevořezů ze skenu přes IIIF (bloky obrazek se souborem drevorez-*.jpg)
  build.py                  sestavení webu do docs/
  web/                      šablony a aplikace (app.js, app.css, kniha.html, index.html, o-projektu.html, logo.png, payment_qr.png, fonts/)
docs/                       VYGENEROVANÝ web – není v gitu (.gitignore), sestavuje se lokálně i v GitHub Actions; needitovat ručně
.claude/agents/             specializovaní agenti: prekladatel, kontrola-prekladu
Fronsberger/                původní pracovní překlad (export z Google Docs) – archiv, už se needituje
```

## Proč YAML po stranách
- čitelný a editovatelný v libovolném editoru, dlouhé texty jako bloky `|-` (jeden odstavec = jeden řádek → přehledné diffy v Gitu),
- jedna strana tisku = jeden soubor → korektury bez zásahu do kódu, snadné dělení práce (shardy po 15–20 stranách),
- každý blok drží originál i překlad pohromadě → zrcadlové zobrazení se nerozjede.

## Postup práce
1. Korektura: uprav `knihy/<kniha>/strany/<id>.yaml` (nebo terminologii v `glosar.yaml`).
2. Kontrola: `python -I nastroje/over_strany.py knihy/fronsberger-1564 [id …]`
3. Ruční ověření: po přečtení a schválení strany `python -I nastroje/overeno_clovekem.py knihy/fronsberger-1564 001r-002v --kdo "jméno"`
   (`--zrusit` zruší, `--prehled` vypíše ověřené). `stav: zkontrolovano` = strojová kontrola, `overeno_clovekem: true` = ověřil člověk.
4. Sestavení webu: `python -I nastroje/build.py`
   Build trvá několik sekund a je deterministický: soubory nesou `?v=<otisk obsahu>`, takže prohlížeč stahuje znovu jen
   to, co se opravdu změnilo, a nezměněná kniha nevytvoří změnu v gitu. Rejstřík v `data.js` ukládá výskyty jako
   `[blok, začátek, konec]` a úryvky skládá prohlížeč; mapa tvarů obsahuje jen tvary z glosáře + výjimky, koncovky
   dopočítá `app.js` (`najdiHeslo`) stejným pravidlem jako `build.py` (`odvod_tvar`).
5. Náhled: otevři `docs/index.html`, nebo `python -m http.server 8766 --directory docs` a http://localhost:8766/

Nová kniha: vytvoř `knihy/<id>/` se stejnou strukturou (kniha.yaml, glosar.yaml, strany/) – build ji přidá do rozcestníku.
Podrobný postup krok za krokem včetně kontrolního seznamu: [PRIDANI_KNIHY.md](PRIDANI_KNIHY.md).
Pořadí stran určuje pole `sken` (číslo snímku). V `kniha.yaml` nastav `strankovani: folio` (fol. XII r) nebo `strany` (str. 12)
a údaje o skenech (`sken.url_strana`, `sken.url_obrazek` s {sken}/{sken4}/{sken5}/{sirka}, `sken.paticka`).

Knihy: `fronsberger-1564` (Fronsperger, Kriegs Ordnung vnd Regiment, sken BSB), `lavater-1651`
(Lavater, Kriegs-Büchlein, Curych 1651; německý text z přepisu Deutsches Textarchiv, CC BY-SA 4.0), `bern-1615`
(Město Bern, Kurtzer Begriff vnd Anleitung Des Kriegs Exercitij vnd Vbung, Bern 1615; sken UB Bern / e-rara)
`solms-1559` (Reinhard hrabě ze Solmsu, Kriegsbeschreibung – Das erst bis neundt Buch, Lich 1559; sken BSB)
`ott-1530` (Michael Ott von Echterdingen, Kriegsordnung, Augsburg kolem 1530; sken BSB bsb00089558)
a `wintzenberger-1588` (Daniel Wintzenberger, Beschreibung einer Kriegs-Ordnung, Drážďany 1588; sken BSB bsb00032546).

## Web
- čtení po **kapitolách** (`#/kap/<id>`) i po **stranách tisku** (`#/strana/018r`), šipky ← → listují,
- předěl strany uvnitř kapitoly: folio, číslo skenu, levá/pravá strana, odkaz na samostatnou stranu a na sken,
- přepínač **Originál / Jen překlad** (klávesa O), světlý/tmavý režim,
- **věcný rejstřík** (`#/rejstrik`) s ukázkami vět, odkazy na kapitolu i stranu; termíny v textu vedou do rejstříku,
- **odkazy na jiné strany** (značka `[[id strany|text]]`), např. z textu na tabuli s mědirytinou – s náhledem obrázku po najetí myší,
- **hledání** v překladu i originálu bez ohledu na diakritiku,
- **PDF** (`#/tisk`): výběr kapitol nebo rozsahu stran, jen překlad / originál + překlad, tisk přes „Uložit jako PDF“.

## Verzování webu
Číslo verze je v `projekt.yaml` (pole `verze`) a zobrazuje se v patičce všech stránek. Formát MAJOR.MINOR.PATCH,
první vydaná verze 1.0.0. Po změně verze spusť `python -I nastroje/build.py`.

| Číslo | Kdy zvýšit | Příklad |
|---|---|---|
| třetí (PATCH) | opravy překladu a drobné úpravy | 1.0.0 → 1.0.1 |
| druhé (MINOR) | nová funkce webu nebo větší část ověřená člověkem | 1.0.1 → 1.1.0 |
| první (MAJOR) | nová kniha nebo zásadní přestavba | 1.1.0 → 2.0.0 |

Při zvýšení vyššího čísla se nižší nulují (1.2.3 → 1.3.0 → 2.0.0).

## Zdroje
- Fronsperger, *Kriegs Ordnung vnd Regiment*, Frankfurt a. M. 1564 (VD16 F 3130). Sken: Bayerische Staatsbibliothek
  München, 2 Polon. 9#Beibd.1, [bsb00045899](https://www.digitale-sammlungen.de/de/view/bsb00045899) (úplný sken; starší digitalizace bsb10150061 a Google Books vynechávají listy XXXVIII v–XXXIX r, LVIII v–LIX r a LXVIII v–LXIX r) – rightsstatements.org NoC-NC 1.0.
  Tentýž exemplář je v [Google Books](https://books.google.cz/books?id=7aBMAAAAcAAJ).
- Město Bern (připisováno Valentinu Friderichovi), *Kurtzer Begriff vnd Anleitung Des Kriegs Exercitij vnd Vbung*, Bern (Abraham Weerli) 1615. Sken: Universitätsbibliothek Bern, `MUE Rar alt 559`, [e-rara 2050509](https://www.e-rara.ch/bes_1/content/titleinfo/2050509) / [DOI 10.3931/e-rara-7750](https://doi.org/10.3931/e-rara-7750) – Public Domain Mark.
- Reinhard Graf zu Solms, *Dises Buch vnd Kriegsbeschreibung ... Das erst bis fünfft Buch*, Lich 1559 (VD16 R 938). Sken: Bayerische Staatsbibliothek München, Rar. 986, [bsb00085168](https://www.digitale-sammlungen.de/de/view/bsb00085168) – rightsstatements.org NoC-NC 1.0.
