# 2. revize – Solms 1559, dávka „6-A“ (`6-titul`, `6-001r` – `6-009r`, skeny 491–509)

Revize podle `zdroje/ZADANI_REVIZE2.md` (vč. oddílu o knihách 6–9) a zprávy překladatele `preklad-6-A.md`.
Sousedé `5-026v` a `6-009v` jen čteni; návaznost `5-026v` → `6-titul` (konec 5. knihy, titul 6. knihy) i `6-009r` → `6-009v`
(oddíl 10 Josta von Velten) sedí. U všech 18 stran nastaveno `stav: zkontrolovano`; `overeno_clovekem: false`, `sken`, `id`
a struktura bloků beze změny.

Ověření: `python -I nastroje/over_strany.py knihy/solms-1559 6-titul 6-001r … 6-009r --prisne` → **18 stran, 0 chyb, 1 varování**.
Varování `6-002r blok 4` (foll/ift/fein) je plané: tisk má skutečně *an die fein an vnd ab zu fürn* (= Feind), vysvětleno v poznámce.

Skeny staženy z BSB IIIF (`bsb00085168_00491`–`_00509`, 1400 px) a prohlédnuty všechny; výřezy v plném rozlišení:
495 (*solchen seinen Ritmeistern*), 506 (oddíly 5 a 8, pravý sloupec se součty), 507 (záhlaví *Hauptman Andres Pflůg*, oddíly 9–13).

## 1. Opravy originálu (`de`)

| Strana | Bylo | Nyní | Pozn. |
|---|---|---|---|
| `6-001v` | `aber damit einer solliche Ordnung` | `aber darmit einer solliche Ordnung` | tisk *darmit* |

Jinak přepis souhlasí se skenem. Ověřeno a ponecháno: iniciály *ES* (493) a *AN* (498); *VErzeichnuß* (501) má jen zvětšené V,
ne zdobnou iniciálu – zápis ponechán; *Mutiplication*, *Mintzenberg*, *Breischs*/*Brieschs*, *Krießrathe*, *wie voglt*,
*Deiweil*, *nach verung*, *Verstengigen*, *in er Musterung*, *oberstersten*, *gedagchten*, *guden*, *3516, o.*; marginálie „1000“ (494).
*Hauptman Andres Pflůg* (507): písmeno po *Haup-* má v tisku tvar blízký *k* („Haupkman“), kustoda na 506 však zní *Haupt.* – ponecháno.

## 2. Tabulky a součty (přepočteno ze skenů)
- `6-001v`: tabulka čtverců 1–32 souhlasí.
- `6-002v`: žold 24 / 12 / 6 / 24 zl. souhlasí.
- `6-007r`: součet strany 62 / 5 / 5 / 7 sedí s položkami (vč. 9 koní knížecích úředníků).
- `6-007v`: výřez potvrzuje tisk *Kürisser 11, Drosser 9, Wagen ½* (oddíl 5) a *Drosser 6* (oddíl 8); součet levého sloupce
  63 / 3 / 5 / ½ odpovídá jen při hodnotách 1 / 1 / 1 a 4½ vozu – poznámka překladatele je správná. Celkové sumy
  (166 × 12 = 1992; 8 × 12 = 96; 14 × 6 = 84; 15 × 24 = 360; 16; celkem 2548 zl.) sedí; příplatky 6 + 4 + 6 = 16.
- `6-008r`: 52 / 6 / 4 / 4 a 33 / 5 / 2½ / 2½ sedí.
- `6-008v`: součet oddílů 9–14 z položek 51 / 7 / 4½ / 4½, tisk 52 / 7 / 3½ / 4½ – rozpor potvrzen výřezem (Otto von Ebeleuben
  7 koní, trénní ½); ostatní součty (51/1/4/4, 54/0/4/4½, 46/3/3/2½) sedí.
- `6-009r`: 5/0/0/½ a celkové součty 293 / 22 / 21 / 22½ (s tištěnými mezisoučty) sedí; 293 × 12 = 3516, 22 × 12 = 264,
  21 × 6 = 126, 22½ × 24 = 540, celkem 4460 zl. **Oprava poznámky 1**: příplatky jsou v Pflůgově rejstříku zapsány jen čtyřikrát
  (oddíly 1, 4, 7, 10: 2 + 6 + 2 + 2 = 12 zl.), tisk uvádí 14 zl.; původní poznámka uváděla neexistující pátý záznam
  („2 + 2 + 6 + 2 + 2“). Cedule Bortzfelt 1–4: 51 / 2 / 4 sedí.

## 3. Změny překladu po stranách
- `6-titul`: „pánem v Breischs“ → „pánem **z** Breischs“ (sjednoceno s „pánem z Münzenbergu“). Popis dřevořezu souhlasí se skenem.
- `6-001r`: *auff jre Kost vnd Jarbesoldung* „na stravě a ročním služném“ → „na **vlastní** stravě a ročním služném“.
- `6-002r`: *solchen seinen Ritmeistern* a *auch soll der Ritmeister von einem pferd … ein halben gulden / tregt … zwölff vnd
  ein halben* přeloženo podle smyslu jako **rotmistr** (tisk ověřen výřezem: skutečně *Ritmeistern*). Důvod: ½ zl. × 25 koní
  = 12½ zl.; ve služebním listu Mořice Saského (`6-005v`) dostává rotmistr na 50 koní 25 zl., tj. také ½ zl. z koně, kdežto rytmistr
  má celý zlatý z koně (poslední odstavec `6-002r`). Poznámka 1 přepsána. Dále *sich in fortheil zu schicken* „obrátit ve svůj
  prospěch“ → „postavit do výhody“.
- `6-002v`: *mit gůten leuten vnd Reuttern gebraucht vnd geübt* „zběhlý ve vedení dobrých lidí“ → „zběhlý v [zacházení s] dobrými
  lidmi a jezdci“ (vedení v tisku není).
- `6-003r`: *ob jm vnd den seinen halten helffen vnd handthaben* „pomáhat jemu i jeho lidem [pořádek] držet a prosazovat“ → „stát
  při něm i při jeho lidech a pomáhat jim [pořádek] udržet“; *nach finantz* „podle fint“ → „kvůli fintám {finantz}“ (glosář `finta`).
- `6-003v`: „pán v Brieschs“ → „pán z Brieschs“; *meine günstige Herrn* „moji příznivci“ → „moji laskaví páni“.
- `6-004r`: *mehr dann tausent Pferdt … die Musterung hielten* „více koní, než kolik přehlídka připouští, totiž víc než tisíc“
  → „více než tisíc koní, kteří obstojí při přehlídce“ (posunutý význam).
- `6-004v`: „pán v Berchemu“ → „pán z Berchemu“ (text i poznámka); *angeborn Petschier* „zděděnou pečetí“ → „rodovou pečetí“;
  *wie Keis. Mai. die bestallung … gehalten haben* „Jeho císařské Veličenstvo dodrželo služební list“ → „platí služební list
  Jeho císařského Veličenstva podle svého obsahu na tisíc koní“.
- `6-005r`: *Vnder disen 1000. pferden sollen zwei / vnd den 200. schützen ein Fendlin* „Pod těmito 1000 koňmi … pod 200
  střelci“ → „U těchto 1000 koní … u 200 střelců“; *Fendrichs ampt* „praporečnický úřad“ → „korouhevnický úřad“ (rozhodnutí
  pro knihy 6–9: *Fendrich* u jízdy = korouhevník).
- `6-006v`: `{Velthauptman}` → `{obersten Velthauptman}` (celý termín k „nejvyšším polním hejtmanem“).
- `6-005v`, `6-006r`, `6-007r` – `6-009r`: překlad věrný a plynulý, bez věcných změn (kromě poznámky na `6-009r`).

Terminologie dávky odpovídá rozhodnutím: *Oberster* = plukovník, *Fendlin/Fanen* u jízdy = korouhev, *Durchleuchtig* = osvícený
(překladatelem zmiňované „jasný“ už v textu není), *Drosser/Droß* = trénní kůň, *Summa lat.* = součet strany,
*Gerüster pferd* = zbrojný kůň (v tabulkách plurál „zbrojní koně“), *Kriegßleut* = válečníci, *Justitien* = justice.

## 4. Sporná místa k rozhodnutí
1. **Rotmistr místo rytmistra** (`6-002r`, odst. 4) – DE *damit der Ritmeister solchen seinen Ritmeistern …; auch soll der
   Ritmeister von einem pferd … ein halben gulden* / CS „rytmistr s takovými svými rotmistry …; Také má rotmistr mít … z každého
   koně půl zlatého“. Překlad podle smyslu (viz výše), tisk ponechán v `de`, vysvětleno poznámkou. Kdyby měl být překlad doslovný,
   vrátit „rytmistry / rytmistr“.
2. **Nesouhlasné součty** (`6-007v` oddíly 5 a 8, `6-008v` oddíly 9–14, `6-009r` příplatky 12 vs. 14 zl.) – tisk ověřen výřezy,
   chyby jsou v sazbě předlohy; `de` i `cs` podle tisku, rozpor v poznámkách.
3. **„Vberleng / vberlengde (pferde)“** – „příplatek“ zůstává nejistý. Sazby 6 zl. na 3 koně a 4 zl. na 4 koně nejsou jednotné;
   „vberlengde Pferde“ (`6-009r`) by mohlo znamenat i koně „navíc“ (přespočetné). Ponecháno s poznámkou.
4. **„Hertzog Moritz von Sachssen / etc.“** (`6-003v`) – v tisku stejně velké písmo jako následující seznam, ale jako nadpis
   oddílu dává smysl; `uroven: 2` ponechána (podřízený nadpis instrukce `uroven: 3`).
5. **„Haupkman“** (`6-008r`) – viz oddíl 1; ponecháno *Hauptman*.

## 5. Návrhy do glosáře
Návrhy překladatele (`preklad-6-A.md`: kyrys, koni-zbroj, jezdecke-kopi, krunyr, podkovar, odjezdne, hejtmansky-zlaty,
prehlidkova-cedule, prirazek, soucet-strany, jednokony-rosser, platebni-poukazka, stuver, stara-vira) podporuji. Doplňuji:

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| puska | puška | Büchsen (u jízdy), Feurbüchsen, Büchse am sattel | zbrane | Jezdecká palná zbraň; heslo `dela` (Büchsen = děla) tu odkazuje mylně – zvážit rozlišení podle kontextu. |
| nejvyssi-polni-hejtman (doplnit tvary) | nejvyšší polní hejtman | Obersten Veldhauptleut, obersten Velthauptman, oberstersten Veldhauptman | velitele | Tvary z `6-006r`/`6-006v`. |
| korouhevnik (doplnit tvary) | korouhevník | Fendrichen (u jízdy) | velitele | Podle rozhodnutí pro knihy 6–9; heslo `prapornik` dnes odkazuje na praporečníka. |
| rumormistr | rumormistr | Romormeister | velitele | Na `6-005r` s platem 40 zl. měsíčně; ověřit, zda heslo už existuje pod jiným tvarem (Rumormeister). |
| ranhojic (doplnit tvar) | ranhojič | Wundtartz, Wundartz | velitele | `6-005r`, `6-009r`. |
| osobni-lekar | osobní lékař | Leibartz | osoby | `6-005r`. |
| prehlidkovy-rejstrik | přehlídkový rejstřík | Muster Register | zold | `6-007r`; srov. `prehlidkova-cedule`. |
| propousteci-prehlidka | propouštěcí přehlídka | abmusterung | zold | Přehlídka při propuštění (abdancken). |
| preplatek | přeplatek | vbersold | zold | Zvláštní plat nad žold (kaplan, vůdce, trubači; kyrysníci 12 zl.). |
