# Překlad předsádky – dávka L-T1 (titul … errata)

Strany: titul (sken 3), vazba (4), venovani (5), predmluva-1 až -3 (6–8), basne-1 až -4 (15–18), errata (181).
Všechny strany: stav `prelozeno`, `overeno_clovekem: false`. `over_strany.py --prisne`: 0 chyb, 0 varování.
Pole `de` je strojově porovnané s `zdroje/dta/NNNN.txt` a obsahově se shoduje. Jediné úpravy: „rc.“ → „etc.“, slova rozdělená přes stránku
(*waa-|re*, *wel-|chem*) jsem podle pravidel přesunul na stranu, kde slovo končí.

## Obsah
- **titul** – titulní list: „Válečná knížka, to jest důkladný návod k válečnictví…“, obsah díla, druhé vydání, autor hejtman H. C. Lavater,
  tisk J. J. Bodmer, Curych 1651.
- **vazba** – stránka obsahuje tři části:
  1. pokyn knihaři, kam vevázat mědirytiny;
  2. kratší seznam tiskových chyb (ERRATA, 9 položek s odkazy na strany);
  3. motto z Vegetia (3. kniha, předmluva) a dvojverší o míru.
- **venovani + predmluva-1…3** – věnování purkmistrům, tajným a válečným radům a čtvrťovým hejtmanům města a venkova Curychu.
  Ve věnování autor vysvětluje, proč je nutné být připraven na válku i v míru a že knížku napsal v souvislosti s novým opevněním
  Curychu. Je datováno 22. 6. 1644 a podepsáno „Hans Conrad Lavater, hejtman“.
  **Pozor:** strany „predmluva-1…3“ nejsou samostatná předmluva, jsou to jen pokračování věnování (na skenech 6–8 není žádný nadpis).
  Pole `list: předmluva` jsem neměnil, navrhuji ho přepsat na „věnování“.
- **basne-1** – „Nově uvitý vavřínový věnec“ (12 veršů, podepsal J. W. S., datováno 22. 6. 1644).
- **basne-2 až basne-4** – „Básnické úvahy“ (podepsal G. M.). Báseň chválí curyšské vynálezce: kožená děla (Eberhard, Brändli), Ardüserovu
  geometrii, rozkládací železné dělo (Meyer), zlacené mosazné pistole (Werder), Holzhalbův most bez pilířů, Körnerův vodní stroj
  a Werdmüllera. Končí přáním, aby válečné umění zůstalo jen věděním, a narážkou na Mojžíše a Amaleka (Ex 17).
  Verše jsou spárované 1 : 1 (28 + 36 + 24), překlad je nerýmovaný.
- **errata** – „Chyby, které je v tomto díle třeba opravit“: 13 oprav a poznámka NB. Každá položka má odkaz [str. N, ř. M].

## Ověření ve skenu (DTA 800px)
- Sken 37 (str. 3): čísla řádků v seznamech chyb se počítají **bez živého záhlaví a nadpisů**. „36. schuh“ je 13. řádek textu.
- Sken 52 (str. 18): „12. schuh“ (míra prutu) je na 28. řádku, ne na 2. řádku. Údaj v errata je zřejmě chybný.
- Sken 55 (str. 21): vynechaná věta patří k výpočtu na ř. 22–24 (obvod 3750 stop / 1875 mužů = 2 stopy na muže).
- Sken 46 (str. 12): „werden“ není na 7. řádku textu, nejblíže je na 6. řádku. Odkaz je nejistý.
- Sken 130 (str. 84): tento výtisk už obsahuje opravené znění (bod 17 o řemenu rondely i cvičení s terčem) a řádky
  o „Exercitium der Spieß“ v něm nejsou.
  **Hypotéza:** seznam na skenu 181 se týká staršího stavu sazby (patrně 1. vyd. 1644) a do vydání 1651 byl převzat beze změny.
  Platný seznam pro 1651 je pravděpodobně kratší seznam ERRATA na straně vazba.
- Ostatní odkazy jsem ověřil podle textu stran:
  - str. 52–53: „Saintinellen“;
  - str. 116: „vnd Ersätzbäumen“;
  - str. 120: „rüffen“ a „Reyenweis“;
  - str. 121: „ersten Theil“;
  - str. 99: „zween Corporal“;
  - str. 9: „in der mitte des Thors“.
- Skeny 3, 4, 5 a 181: kontrola členění (titul, adresa věnování jako nadpis, errata jako jeden odstavec s visícím odsazením).
  V datech jsem errata rozdělil na položky typu `seznam`, aby šlo ke každé připojit odkaz. Text DE se tím nemění.

## Sporná místa
- Přepis DTA má zřejmé chyby. Podle zadání jsem je v `de` ponechal a do `cs` přeložil správný smysl:
  - *Seribenten* (tisk: Scribenten), *Angeschen* (Angesehen), *Exccutionen* (Executionen);
  - *Historta* (Historia), *Gebilff* (Gehilff), *Zü* (Zů), *Waaffens-kunft* (-kunst), *zalgebunden* (zal gebunden).
  Návrh: nahlásit je DTA, případně opravit podle skenu.
- basne-2: „Der Tiguriner Fälde / Fürwar auch flüssig sind“ – „pole Tigurinů jsou věru také plodná“. *flüssig* chápu jako „hojný, výnosný“.
- basne-2: „die nicht auß Schweden her / Zü vns erst kommen sind: von vns hineyn vil mehr“ – „ta děla nepřišla ze Švédska teprve
  k nám, nýbrž mnohem spíš od nás tam“. Básník tvrdí, že kožená děla vznikla v Curychu dřív než ve Švédsku.
- basne-3: „Gleichwol ohn Joch vnd Blech“ – „bez jařma a pilířů“. Slovo *Blech* je nejasné (kování? tisková chyba?).
- basne-3: „Was Zierden auch vorab / Des Herr’n Werdmüllers Sinn vom hohen Himmel hab“ – „jaké ozdoby duch pana Werdmüllera
  z vysokého nebe má“. Není jasné, ke kterému dílu Werdmüllera se verš vztahuje.
- basne-3: „bey dem Schimpff nicht all gewesen“ – „ne všichni byli při té hře“. *Schimpf* = hra/zápas, tady nejspíš skutečný boj.
- basne-4: „Weil nicht ein jeder Mann der Practic hie begäret“ – „že ne každý muž tu po praxi touží“. Výklad smyslu je v poznámce.
- vazba: „in der mitte des halben Thars“ – „uprostřed poloviny brány“ (Thars = Thors, branka v jednom křídle vrat?).
- titul a predmluva-2: *Landschafft* – „venkovský kraj“, tj. curyšské venkovské poddanské území (je v poznámce).

## Návrhy do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| ctvrtovy-hejtman | čtvrťový hejtman | Quartierhauptmann, Quartierhauptleuhten | velitele | Velitel milice jednoho vojenského obvodu (Quartier) curyšského venkova. |
| rondela | rondela | Rondelle, Rondellen, Rondache | zbrane | Kulatý štít pěšáka (rondache); cvičení „mit der Rondellen vnd Spieß/Dägen“. |
| terc | terč | Targe, Schilt | zbrane | Štít (pěchotní), v cvičení se štítem a kordem. |
| mediryt | mědirytina | Kupffer, Kupfferblat, Kupffer-riß | – (obecné) | Tabule s vyobrazením; v textu odkazy „Kupffer“, „fig.“. |
| zastup | zástup | Reyen | jednotky | Podélná řada šiku (file); proti „řada {Glied}“ (rank). V tisku užíváno důsledně. |
| zdvojovani | zdvojování | Dopplierung, dopplieren | jednotky | Zdvojení řad nebo zástupů v šiku. |
| cviceni | cvičení | Exercitium | sluzba | Cvičení se zbraní (mušketa, píka, štít). |
| sentinela | stráž, hlídka | Sentinelle, Sentinell, Saintinell | sluzba | Cizí slovo pro stálou stráž (Schildwacht); v tisku i chybné „Saintinell“. |
| podperny-tram | podpěrný trám | Vndersätzbaum | opevneni | Podkládací trám (oprava v errata k str. 116). |
| landschaft | venkov, venkovský kraj | Landschafft | mista | Curyšské poddanské venkovské území (proti Statt). |
| spriseženstvi | Spříseženství | Eydgnoschafft | mista | Švýcarské spříseženství. |

## Osoby a místa pro rejstřík
- **Osoby:**
  - Hans Conrad Lavater (autor, hejtman); Johann Jacob Bodmer (tiskař, Curych);
  - Vegetius (Epitoma rei militaris); J. W. S. a G. M. (neurčení autoři básní);
  - mistr Eberhard a jeho pomocník Brändli (kožená děla); Johann Ardüser (1585–1665, matematik, pevnostní inženýr);
  - Meyer (kovář, železné dělo); Felix Werder (1591–1673, puškař, zlacené pistole – identifikace překladatele);
  - Holzhalb (stavitel mostu); cechmistr Körner (vodní stroj); Werdmüller (patrně Hans Georg Werdmüller, inženýr opevnění);
  - biblické postavy: Mojžíš, Amalek, Izrael; Mars.
- **Místa:** Curych (město a venkov), Spříseženství, Švédsko, řeka Limmat, Rýn, Tigurini/Tigurum.
