# 2. revize – Solms 1559, dávka „kniha5-A“ (`5-titul`, `5-001r`–`5-012r`, skeny 435–459)

Revize podle `zdroje/ZADANI_REVIZE2.md` (plynulost „středně“, Oberst = plukovník, Fendlin u pěchoty = praporec).
Struktura bloků, `sken`, `id`, `stav: zkontrolovano` a `overeno_clovekem: false` beze změny. Sousedé `4-023v`
a `5-012v` jen čteni.

Ověření: `python -I nastroje/over_strany.py knihy/solms-1559 5-titul 5-001r … 5-012r --prisne`
→ **23 stran, 0 chyb, 0 varování**.

Skeny BSB IIIF staženy u sporných míst: 441, 442, 445, 447, 452, 454, 455, 456 (včetně výřezů v plném rozlišení), 457, 459.

## 1. Opravy originálu (`de`) podle skenu

| Strana | Bylo | Nyní | Pozn. |
|---|---|---|---|
| všechny | `vñ`, `dañ`, `wañ`, `mañ`, `Doñen`, `Persoñ`, `eiñ`, `võ` | `vnd`, `dann`, `wann`, `mann`, `Donnen`, `Person`, `ein`, `von` | rozepsání zkratek podle § 2 pravidel |
| `5-003r`, `5-005r`, `5-008v` | `Hölzer`, `hölzen`, `hölzern`, `hölze` … | `Höltzer`, `höltzen`, `höltzern`, `höltze` … | tisk má všude *tz* (OCR „Hölker“) |
| `5-003r` | `bisz halben`; `die ronde des Thurns` (2×); `ligenden ronden` | `biß halben`; `rönde`; `rönden` | |
| `5-003r` | `mit Puluer gefast worden`; `oder gefast ist`; `fürgesatz/`; `dz ein man darin` | `gesatzt worden`; `gesatzt ist`; `fürgesatzt/`; `dz ein mann darinn` | |
| `5-003v` | `gleichs falsz` | `gleichs falß` | |
| `5-005r` | `so fer?`; `verdaressen`; `Kreutzgraben miet 4.`; `Runden dinglin`; `verigelt`; `den Donen` | `so ferr`; `verdarressen`; `mit 4.`; `Ründen dinglin`; `verrigelt`; `den Donnen` | nová pozn. k *verdarressen* |
| `5-006r` | `vil find von stätten`; `zufürt` | `vil sind von`; `zufert` | „find“ byla chyba OCR, ne tisku – pozn. přepsána |
| `5-007r` | `don oder fasz` | `don oder faß` | |
| `5-008v` | `Zeughausß`, `Blasßbalg` | `Zeughauß`, `Blaßbalg` | |
| `5-009v`, `5-010r` | `Vogelszberger` (4×) | `Vogelßberger` | |
| `5-010v` | `Caspar Salzburger`, `Jörg Aschauer`, `Jacob Fur`, `Hanß Meter`, `fur ein lehen` | `Saltzburger`, `Asthauer`, `Fux`, `Meier`, `für ein lehen` | výřez ve 2800 px: tisk má zřetelně *Aſthauer* (tisková chyba za *Aschawer*), *Fux* (= *Fuchs*), *Meier* |
| `5-012r` | `wannes`; `darzu angenommen`; `zu den obengemelten` | `wann es`; `darzů`; `zů` | |

Ověřeno a ponecháno: `mit den kurtzen vier Büchsen` (`5-003v`, tisk), `Krafft` za *Grafft* (`5-008r`, nová pozn.),
`geschicht`, `bescheibung` (`5-006r`), `Summa 51.` (`5-010v`, zřetelně), `Summa 101.` (`5-009v`), `ziegen`, `Hilt` (`5-012r`),
kustody `Hanß`, `Bernhart`, `Die` a signatura `B`, `C`.

## 2. Tabulky rejstříku (`5-009v`–`5-011r`) – kontrola řádek po řádku

Všechna jména a čísla směn porovnána se skeny 454–457. Kromě oprav výše vše sedí. Přepočty (1 fl. = 15 bacenů):
- `5-009v`: levý sloupec 18 jmen = 100 směn ✓. Pravý sloupec nahoře (15 jmen) má jen 66 směn – **nové zjištění**: 66 + 35 směn sedmi
  rubačů z levého sloupce dole = přesně 101 ✓; devět rubačů vpravo dole (50) + *Vogelßberger* (6) = 56 ✓. Pozn. 2 a 3 přepsány.
- `5-010r`: 56 × 6 = 22 fl. 6 b. ✓; 12 × 5 = 4 fl. ✓; 13 × 6 = 5 fl. 3 b. ✓; výdaje za svíčky atd. = 13 fl. 2 b. + 32 fl. = 45 fl. 2 b.
  proti tištěným 45 fl. 5 b. (tištěná hodnota však sedí do součtu 150 fl. 10 b.) – pozn. ponechána.
- `5-010v`: tištěné „51“ nesouhlasí se jmény (20 + 34 = 54), peníze 13 fl. 10 b. = 41 směn = 34 + 7; skupina *Veit Weiner*–*Paul Fermer*
  (27 směn) nemá vlastní součet; 17 × 2 = 34 ✓ – pozn. 1 přepsána.
- `5-011r`: 111 fl. 6 b. vychází jen při 1 sluneční koruně = 23 bacenů (kurz vyplývá ze součtu, pozn. upřesněna); 149 fl.,
  299 fl. 10 b. a 165 fl. ✓.

## 3. Hlavní změny překladu

Terminologie sjednocena s glosářem v celé dávce:
- *Batzen/batz* → **bacen** (dříve „batz“): „po 5 bacenech“, „33 zlatých 5 bacenů“, „8½ bacenu“.
- *Schuh/schůh/Schůch* → **stopa** (dříve „střevíc“); *werckschůhe* ponecháno „dílenský střevíc“ (heslo `werkstrevice`).
- *Artolorei* → **dělostřelectvo**, *Artolorei Meister* → „mistr dělostřelectva“, *General Artolorei* → „generál dělostřelectva“ (dříve „artilerie“).
- *Schantz/Schantzen* → **šance** (dříve „zákop“); *Festung/Befestung* → „pevnost/opevnění“ s českým slovem (dříve holé `{Festung}`, `{Befestung}`, `{Wall}`).
- *Lantzknechten* → **lancknechty** (dříve zakázané „landsknechty“), *Fendlin* (pěchota) → **praporce** (dříve „korouhve“) – `5-001v`.
- *Obersten vber die Knappen* → „plukovníkovi nad horníky“ (dříve „nejvyššímu“) – `5-011r`.
- *Hutleut* → „důlní dozorci“, *Geding* → „úkolové dílo“, *Focher* → „[muži u] větrných měchů“, *Item* v tabulkách → „Dále“.

Po stranách (výběr):
- `5-titul`: „Jak se má {Festung} podkopávat“ → „Jak se má pevnost {Festung} podkopávat“.
- `5-001r`: rozdělena souvětí; „mistra artilerie {Artholorei}“ → „mistra dělostřelectva“; *Zeugdiener vnd wartter* → „zbrojním služebníkům {Zeugdiener} a správcům {wartter}“ (dříve „dozorcům zbrojnice“).
- `5-001v`: **posun významu** „mám ona zmeškání i zkoušky na svědomí“ → „mám ona zdržení i zkoušky dobře v paměti“ (*in gutem gewissen* = v dobré znalosti);
  *ordene zů oder ab … ein sollichen platz* → „aby se jim ve zbrojnici vyhradilo místo [ve stavu], přidáním či ubráním jiných“; *Anschaffer* → „předáci“.
- `5-003r`: „15 střevíců“ → „15 stop“; „zápalný žlab“ → „zápalný kanálek“; věty rozděleny.
- `5-003v`: „z krátkých ohnivých ručnic {vier Büchsen}“ → „ze čtyř krátkých pušek {Büchsen}“; pozn. přepsána (Feuerbüchsen jen nejistá domněnka).
- `5-004r`, `5-006r`: odstraněno neodůvodněné tykání („nedostaneš“, „kde chceš odpalovat“) → neosobní vazby.
- `5-005r`: „jak jest vidět v dlouhé hradbě s patrovým dřevem“ → „jak je vidět na dlouhém úseku hradby“ (*maurn stock*); nová pozn. k *verdarressen*.
- `5-006r`: *belegt sie* → „obránci se sevřou“; *Festen* → „pevnost“.
- `5-008r`: měch – srozumitelnější popis funkce záklopek; *kasten* = „žlab“ jednotně s `5-008v`; nová pozn. *Krafft* = *Grafft*.
- `5-009r`: „před Métami“; *gedingt* → „úkolově smlouval“; pozn. 1 opravena (přesmyčka „Orduung“ není ve 3. odstavci).
- `5-011r`: *Summa summarum* bez složených závorek; „jest přijat“ → „byl přijat … od samého Jeho Císařského Veličenstva“.
- `5-011v`: „Dva dozorce má člověk mít, kteří jsou…“ → „Je třeba mít dva důlní dozorce, kteří budou…“; „jeho rozkaz“ → „jeho povinnost {beuelch}“.
- `5-012r`: nadpis „Tažení velikého knížete, jemuž se říká Moskevský“; rozdělení souvětí; konec strany upraven na „který by byl v jednotných“ tak, aby navazoval na `5-012v` („válečných zvyklostech a v dobré zbroji“, *in einem Kriegßgebrauch*).
- `5-004v`: popis „značka rytce?“ → „snad značka rytce“.

## 4. Sporná místa k rozhodnutí

1. `5-010v` *Jörg Asthauer* – tisk má zřetelně *Aſthauer*; ponecháno podle tisku (dřívější revize opravovala na *Aschauer*). Případně sjednotit na *Aschawer* jen v `cs`.
2. `5-010r` *vmb ein Ziegel wasser zu heben* – „okov k vytahování vody“; *Ziegel* (cihla?) nedává smysl, snad *Zuber/Kübel* – ponecháno.
3. `5-011r` *vier Focher haben gemacht … 13. schichten* – *Focher* je jinde větrací měch (heslo `vetrny-mech`), zde zjevně obsluha; přeloženo „[muži u] větrných měchů {Focher}“.
4. *Knecht* v hornickém rejstříku = důlní čeledín (pomocník), ne voják; `{Knecht}` ale odkazuje na heslo `knecht` s vojenským výkladem.
5. `5-012v` (mimo dávku): „100 korouhví {Fendlin} německé pěchoty“ – podle rozhodnutí má být „praporců“.
6. `5-010r` záhlaví *Zuffer leut.*, *Hut leut.* – bez `{…}`, jinak validátor hlásí nepoměr délek krátkých bloků.

## 5. Návrhy do glosáře (glosář needitován)

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| `bacen` (varianta) | bacen | + `batz`, `batz.` | miry | tvar z rejstříku 5. knihy |
| `zlaty` (varianta) | zlatý | + `flo.` | miry | |
| `stopa` (varianta) | stopa | + `schůhe` | miry | |
| `werkstrevice` | **dílenská stopa** (návrh přejmenovat) | werckschůhe | miry | sjednotit se `stopa` (Schuh = stopa) |
| `slunecni-koruna` (varianta) | sluneční koruna | + `sonnen kronen` | miry | z rejstříku vychází 1 koruna = 23 bacenů |
| `dulni-dozorce` (varianta) | důlní dozorce | + `Hut leut` | velitele | |
| `val` (varianta) | val | + `wel`, `wällen`, `wäl` | opevneni | |
| `pevnost` (varianta) | pevnost | + `befestung`, `befestunge`, `Festen` | opevneni | |
| `prikop` (varianta) | příkop | + `greben` | opevneni | |
| `podkopova-chodba` (varianta) | podkopová chodba | + `graff`, `Graff`, `Krafft` | opevneni | |
| `vetrny-mech` (pozn.) | větrný měch | Focher | delostrelectvo | doplnit: v `5-011r` i obsluha měchů |
| `soudek` (nové) | soudek | Don, Donnen, donnen | delostrelectvo | soudek prachu do nálože |
| `tram-zaver` (nové) | trám (k zahrazení nálože) | drem, Dremlin | opevneni | příčné trámy zahrazující komoru |
| `dulni-celedin` (nové) | důlní čeledín | Knecht (v hornickém rejstříku) | jednotky | pomocník, vyváží a čistí; nezaměňovat s knechtem-vojákem |
| `pridavac` (nové) | přidavač | Zuffer leut | jednotky | pomocný horník |
| `predak-dulni` (nové) | předák | Anschaffer | velitele | hornický předák přidělující práci |
| `zbrojni-spravce` (varianta) | zbrojní správce | + `wartter` | delostrelectvo | |
| `dela` (oprava) | děla | odstranit `vier Büchsen` | delostrelectvo | zde jde o ruční pušky, ne děla |
