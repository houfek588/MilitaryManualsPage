# Zadání: přepis a překlad Šesté až Deváté knihy Solmse (2026-11-18)

Strany Šesté až Deváté knihy jsou založené jako kostry (`stav: chybi_original`, prázdné `bloky`) skriptem
`nastroje/solms_kostry_6_9.py`. Úkolem je u každé strany **přepsat německý originál** (OCR + sken) a **přeložit ho**.
Platí `PRAVIDLA_PREKLADU.md`, `zdroje/ZADANI_AGENTUM.md` (pravidla přepisu tisku Solmse) a rozhodnutí v
`zdroje/ZADANI_REVIZE2.md` (plynulost „středně“, terminologie). Glosář `glosar.yaml` je závazný.

## Přehled knih
| Kniha | Skeny | Obsah |
|---|---|---|
| 6 | 491–545 | *Das sechst Bůch* – přehlídka (Musterung) jízdy a pěchoty podle služebních listů Mořice Saského a markraběte Albrechta Braniborského za Karla V. (1544): pravidla přehlídky, přehlídkové rejstříky (jména rytmistrů a jezdců, počty koní, vozů, žold v zlatých a bacenech) |
| 7 | 546–584 | *Das sibend Bůch* – „Kartenspiel“: karetní hra s vojenskými úřady, oddíly, děly a vozy; Hannibal proti Scipionovi; dřevořezy karet s nápisy, výčty a výklad hry; ležení a vozová hradba |
| 8 | 585–616 | *Das acht Bůch* – jak obsadit město či městečko válečným lidem a zásobit ho proviantem a municí; výpočty zásob; obrazová strana 610 |
| 9 | 617–681 | *Borgundische Kriegsordnung* – Burgundský válečný řád (dle Filipa Klévského / *Arbor militiae*): předmluva, články, řád ležení a pochodu; 681 = erbovní list na konci svazku |

## Foliace a id stran
Liché skeny = líc (r), sudé = rub (v). `6-001r` = sken 493, `7-001r` = 549, `8-001r` = 589, `9-001r` = 621;
titulní listy `6-titul`, `7-titul`, `8-titul`, `9-titul`; erby `7-erb-solms`, `8-erb-solms`, `9-erb-solms`, `9-erb-konec`.
Pole `id`, `list`, `strana`, `sken` neměň. Prázdné strany (492, 548, 584, 586, 588, 618, 620) v edici nejsou.

## Postup u každé strany
1. **Originál (`de`)**: výchozí je OCR `zdroje/ocr_bsb/NNNN.txt` (NNNN = sken, 4 číslice). OCR je u těchto knih
   špatné (fraktura, červený tisk, tabulky) – **každou stranu porovnej se skenem**:
   `curl -s -o <tvoje-podsložka-scratchpadu>/sNNN.jpg "https://api.digitale-sammlungen.de/iiif/image/v2/bsb00085168_<NNNNN>/full/1600,/0/default.jpg"`
   (NNNNN = sken na 5 číslic) a otevři nástrojem Read; drobné písmo si zvětši výřezem
   (`…/bsb00085168_<NNNNN>/<x>,<y>,<w>,<h>/1200,/0/default.jpg`). Dobový pravopis zachovej, zkratky rozepiš
   (vñ → vnd, mañ → mann, ꝛc. → etc.), vynech živé záhlaví (*Das sechst Bůch*, *Von Muster Registern*), čísla listů,
   signatury a kustody; slovo rozdělené přes hranici stran patří celé na stranu, kde končí.
2. **Bloky**: nadpisy (`uroven` 1 = titul knihy, 2 = hlavní oddíl, 3 = pododdíl), odstavce 1 : 1 podle sazby,
   `pokracovani: true` u odstavce přecházejícího z předchozí strany.
   - **Rejstříky a výpočty** (6. kniha – jména, koně, vozy, peníze; 8. kniha – zásoby) jako `typ: tabulka` se stejným
     počtem řádků v `de` i `cs`, sloupce jako v tisku; jména osob a míst nepřekládej (v `cs` ponech, případně
     doplň dnešní podobu v poznámce), čísla a mince přesně (fl. = zlatý, batzen = bacen, kr. = krejcar).
   - **Obrázkové strany** mají připravený blok `obrazek` (`obrazky/drevorez-<sken>.jpg`): doplň `popis` (co obraz
     ukazuje). U **karet Sedmé knihy** přepiš a přelož všechny nápisy na kartách – buď do `popis`, nebo jako
     `typ: tabulka` (sloupce: nápis na kartě | překlad), aby byly prohledávatelné; text strany mimo karty (záhlaví,
     výklad) patří do běžných bloků.
   - Titulní list: nadpis `uroven: 1` s celým titulem, pak odstavce, obrázek, tiráž (*Gedruckt…*) – viz `5-titul`.
   - Erbová strana: odstavec s nápisem (*Reinhart der Elter…*) + obrázek – viz `4-erb-solms`.
3. **Překlad (`cs`)**: věrně a plynule („středně“ – dlouhá souvětí dělit, přirozený slovosled, dobový tón listin a
   služebních listů ponechat). Závazně: *Oberst / Oberster / Obersten* = **plukovník**; *Fendlin* u jízdy = **korouhev**,
   u pěchoty **praporec**; *Kriegßleut* = **válečníci**; *Maiestat* = **Veličenstvo**; *Ritmeister* = rytmistr;
   *Musterung* = přehlídka, *Musterherr* = přehlídkový komisař, *Muster Register* = přehlídkový rejstřík;
   *Feurpfeil* = zápalný šíp; *Büchsenpulver* = střelný prach. `{Termín z tisku}` při prvním výskytu na stránce.
   Kde glosář chybí, zvol překlad, drž ho v celé dávce a navrhni heslo ve zprávě (glosář needituj).
4. **Poznámky**: reálie (osoby, místa, události 1544 – tažení proti Francii, Saint-Dizier; Filip Klévský…),
   nejasná místa a tiskové chyby. Neopakuj výklad glosáře.
5. **Stav**: `stav: prelozeno`, `overeno_clovekem: false`.

## Výstup
- Edituj jen strany své dávky; stranu před a za dávkou jen čti (návaznost).
- Pomocné skripty a skeny jen ve **vlastní podsložce scratchpadu** (např. `p6a/`) – sdílené soubory přepisují jiní agenti.
- Po dokončení: `python -I nastroje/over_strany.py knihy/solms-1559 <id …> --prisne` – 0 chyb.
- Zprávu ulož do `knihy/solms-1559/zdroje/kontrola/preklad-<dávka>.md`: přehled stran, nejistá čtení ze skenu,
  sporná místa (DE + CS + důvod), návrhy hesel (id, cs, de, kategorie, pozn). Do odpovědi vrať shrnutí do 12 řádků.
