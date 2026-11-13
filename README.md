# Vojenské manuály – dvojjazyčné edice

Digitální edice raně novověkých vojenských příruček: německý originál (podle skenu) a český překlad,
čtené vedle sebe, s poznámkami překladatele, věcným rejstříkem, odkazy na skeny a exportem do PDF.

Web je čistě statický (HTML + CSS + JS, data vložená jako `<script>`), takže:
- **offline**: otevři `docs/index.html` dvojklikem,
- **GitHub Pages**: Settings → Pages → *Deploy from a branch* → `main` / složka `/docs`.

## Struktura

```
PRAVIDLA_PREKLADU.md        pravidla překladu a popis datového formátu (závazné pro lidi i agenty)
projekt.yaml                nastavení webu: autor, kontakt, skupina, sociální sítě, údaje pro podporu (dar)
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
  over_strany.py            kontrola dat (struktura, párování, poznámky, terminologie)
  normalizuj_zkratky.py     sjednocení přepisu zkratek tisku (ꝛc., vñ, …)
  overeno_clovekem.py       označení stran, které ručně ověřil člověk (pole overeno_clovekem)
  vyrez_drevorezy.py        výřez dřevořezů ze skenu přes IIIF (bloky obrazek se souborem drevorez-*.jpg)
  build.py                  sestavení webu do docs/
  web/                      šablony a aplikace (app.js, app.css, kniha.html, index.html, o-projektu.html, logo.png, payment_qr.png, fonts/)
docs/                       VYGENEROVANÝ web (needitovat ručně – přepíše ho build.py)
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
5. Náhled: otevři `docs/index.html`, nebo `python -m http.server 8766 --directory docs` a http://localhost:8766/

Nová kniha: vytvoř `knihy/<id>/` se stejnou strukturou (kniha.yaml, glosar.yaml, strany/) – build ji přidá do rozcestníku.

## Web
- čtení po **kapitolách** (`#/kap/<id>`) i po **stranách tisku** (`#/strana/018r`), šipky ← → listují,
- předěl strany uvnitř kapitoly: folio, číslo skenu, levá/pravá strana, odkaz na samostatnou stranu a na sken,
- přepínač **Originál / Jen překlad** (klávesa O), světlý/tmavý režim,
- **věcný rejstřík** (`#/rejstrik`) s ukázkami vět, odkazy na kapitolu i stranu; termíny v textu vedou do rejstříku,
- **hledání** v překladu i originálu bez ohledu na diakritiku,
- **PDF** (`#/tisk`): výběr kapitol nebo rozsahu stran, jen překlad / originál + překlad, tisk přes „Uložit jako PDF“.

## Zdroje
- Fronsperger, *Kriegs Ordnung vnd Regiment*, Frankfurt a. M. 1564 (VD16 F 3130). Sken: Bayerische Staatsbibliothek
  München, 2 Polon. 9#Beibd.1, [bsb00045899](https://www.digitale-sammlungen.de/de/view/bsb00045899) (úplný sken; starší digitalizace bsb10150061 a Google Books vynechávají listy XXXVIII v–XXXIX r, LVIII v–LIX r a LXVIII v–LXIX r) – rightsstatements.org NoC-NC 1.0.
  Tentýž exemplář je v [Google Books](https://books.google.cz/books?id=7aBMAAAAcAAJ).
