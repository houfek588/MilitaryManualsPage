# Zpráva ze zpracování a vizuální kontroly – `knihy/solms-1559`, Třetí kniha, Dávka 6 (`3-056r`–`3-067r`)

Zpracováno všech **23 závěrečných stran** Dávky 6 Třetí knihy Solmsova tisku (1559): `3-056r`–`3-067r` (skeny `363`–`385`). Všechny strany byly ověřeny proti staženým náhledům skenů (`s363.jpg`–`s385.jpg`, plus hraniční sken `s362.jpg`), rozděleny 1 : 1 podle sazby, doplněny o ozdobné iniciály, vyčištěny od chyb BSB OCR a netextových prvků (záhlaví *Das drit Buch.*, *Von der Artolorei.*, čísla listů, signatury `Kk iij`–`Ll iij`, kustody, čárové kódy a prosvítající text či kaňky jako `湯` na `s380.jpg`) a plynule přeloženy do češtiny podle `PRAVIDLA_PREKLADU.md` a `knihy/solms-1559/glosar.yaml`. Všech 23 stran má `stav: zkontrolovano` a `overeno_clovekem: false`.

Ověření skriptem `python -I nastroje/over_strany.py knihy/solms-1559 3-056r 3-056v 3-057r 3-057v 3-058r 3-058v 3-059r 3-059v 3-060r 3-060v 3-061r 3-061v 3-062r 3-062v 3-063r 3-063v 3-064r 3-064v 3-065r 3-065v 3-066r 3-066v 3-067r --prisne`:
- **23 stran, 0 chyb, 1 varování** (jediné varování na `3-059v`, blok 2: autentické dobové přídavné jméno *fein* ve spojení *so wirt er fein vnd gůt / oder fertig*, ověřeno na skenu `s370.jpg`).

---

## 1. Přehled stran, foliace a ukončení Třetí knihy

- **Foliace ve skenech (`s363.jpg`–`s385.jpg`)**:
  - Číslování listů `56` (`3-056r`) až `67` (`3-067r`) běží souvisle a bez přesmyček.
  - Na `3-061r` (`s373.jpg`) ověřeno ve skenu číslo `61` (OCR četlo `σε`), na `3-062r` (`s375.jpg`) je číslo `62` v horním pravém rohu v originále sotva znatelně otištěné (OCR jej vynechalo), na `3-066r` (`s383.jpg`) je čitelné `66` (OCR četlo `6`).
- **Hraniční přechod `3-055v` → `3-056r`**:
  - Rub `3-055v` (`s362.jpg`) končí tečkou (`denn laß wol trucken werden.`, kustod `Weiß`); `3-056r` začíná novým nadpisem `Weis Puluer sol man also machen.`, takže bez `pokracovani: true` a bez rozděleného slova přes hranici.
- **Závěr Třetí knihy (`3-067r`, sken `385`)**:
  - Kniha končí na posledním řádku líce listu `67` (`3-067r`) větou `…die Koln lenger zubehalten / das sie nit in dem Puluer verderben / so thů mañ ein wenig Atrament zun Koln / etc.` (bez závěrečného kolofonu *Ende des dritten Büchs.*). BSB OCR na posledním řádku zduplikovalo zkomolené slovo (`fothan verderben / fothaman`) a značku `ꝛc.` četlo jako `ca`.
  - Na rubu téhož listu `67v` (sken `386`) je již vytištěn erbovní frontispis Čtvrté knihy (*Reinhart der Elter / Graue zu Solms…*), v němž v průsvitu papíru prosvítá text z `3-067r`.

| Strana | List | Sken | Bloky | Pozn. | Hlavní obsah a úpravy |
|---|---|---:|---:|---:|---|
| `3-056r` | 56r | 363 | 14 | 7 | Barevné (bílý, červený, modrý, žlutý) a běžné střelné prachy; opravy iniciál, *Zendel*, *Spiciam Nardi*, *Widertat*, *Capillum veneris*, *Albram holtz*. |
| `3-056v` | 56v | 364 | 10 | 5 | Zesilování a záchrana zkaženého prachu; opravy *brenn*, *ein gebresten*, *Bilsensamen*, *redten*; slovo přes přelom `3-056v -> 3-057r`. |
| `3-057r` | 57r | 365 | 8 | 5 | Prach mistra Rüdigera z Heidelbergu, záchrana navlhlého prachu, prach pro dalekou ránu; oprava lékárnických symbolů `℥` a `ß`, *grimentlich*. |
| `3-057v` | 57v | 366 | 11 | 6 | Prach pro kamenometná děla a ručnice, zkouška prachu rozžhavenou železnou tyčkou v hluboké nádobě; oprava nadpisu `been putuer zustercken`. |
| `3-058r` | 58r | 367 | 13 | 5 | Silné prachy, prachy pro kamenná děla a ručnice, zápalný prach (*Zündtpuluer*); oprava *Quecksiber*, *eisern sindern*, *geleschten Kalch*. |
| `3-058v` | 58v | 368 | 9 | 5 | Složení prachů, rozdělení dávek, *silberschaum*, *braunstein*; odstranění falešných zlomků a úprava kustodů. |
| `3-059r` | 59r | 369 | 7 | 2 | Oddělování složek prachu (uhlí, síra, ledek); v nadpisu odstraněno zduplikované `ufscheiden.`, doplněny vynechané iniciály. |
| `3-059v` | 59v | 370 | 6 | 4 | Čištění nového a horského (*wilden / hartzepffig*) ledku; ověřeno *fein* (`s370.jpg`), opraveno *dickes*, *ES*, *gestehen*, *zwei theil ein*. |
| `3-060r` | 60r | 371 | 5 | 5 | Další způsoby čištění ledku; opraveno *Reitter* (OCR `Ketter`), *Brünnwasser* (`Grünwasser`), *Aceto distillato*, *anderweit*. |
| `3-060v` | 60v | 372 | 5 | 5 | Čištění surového ledku louhem a kamennou solí; opravy *Kalcus*, *Filtz oder Hut*, *saluiter*. |
| `3-061r` | 61r | 373 | 5 | 4 | Rychlé zprudčování ledku a rozlišování od soli; ověřeno folio `61`, opraveno *WIltu*, *alß ab*, *Ispontcum*, *Galitzenstein*. |
| `3-061v` | 61v | 374 | 7 | 3 | Další čištění již čištěného ledku; opraveno *rechten Salpeter*, *etli*. |
| `3-062r` | 62r | 375 | 5 | 4 | Zkouška ledku míchadlem (*Rürstab*, OCR `Xirstab*) a směs s *Sal Commune*; ověřena slabě otištěná číslice `62` v originále. |
| `3-062v` | 62v | 376 | 7 | 3 | Znalectví a zkoušky kupovaného benátského ledku; opraveno *protzelt* (`proßelt`), *salunien*/*Sal siluestrum*, *er treugt*. |
| `3-063r` | 63r | 377 | 7 | 3 | Kde hledat ledek, jak čistit v inných sudech/sklepech; odstraněn prosvítající řádek z rubu, doplněn řádek vynechaný v OCR. |
| `3-063v` | 63v | 378 | 7 | 6 | Výnosnost nástěnného ledku, příprava *Salutter preparatum*; opraveno *seil* (`seid`), *knutzig* (`knugig`), *giessen* (`greffen`). |
| `3-064r` | 64r | 379 | 5 | 3 | Dobývání ledku v tenkých hliněných hrncích (*Lutum Sapiencie*) a krystalizace v chladném sklepě se zaječí packou (*hasen fuß*). |
| `3-064v` | 64v | 380 | 7 | 4 | Přirozenost ledku (čtyři stupně kvalit, *Alandt* vs. *Saluiter*) a další čištění kamencem/skalicí; odstraněn šum `湯`. |
| `3-065r` | 65r | 381 | 10 | 3 | Vaření ledku se salmiakem a měděnkou (*Glaritzenstein*), zkoušky soli; zachována přesmyčka *Klach* (*Kalch*), odstraněn kustod `reinen`. |
| `3-065v` | 65v | 382 | 8 | 3 | Závěr oddělování ledku (`pokracovani: true`), hlavní oddíl `uroven: 2` o přípravě síry (*Schwefel*), iniciála `LEbendiger`, sirný olej; odstraněn kustod `tröpffeln/`. |
| `3-066r` | 66r | 383 | 13 | 2 | Dokončení destilačního sirného oleje (`pokracovani: true`), olej z vaječných žloutků, rýmované sirné svíce (`typ: verse` – 4 verše), síra se rtutí a sublimátem; odstraněn kustod `Nun`. |
| `3-066v` | 66v | 384 | 9 | 2 | Hlavní oddíl `uroven: 2` o pálení dřevěného uhlí (*Koln*), iniciála `WIlt du`, posilování atramentem (*Atrimentum*), uhlí z ubrusu do zápalného prachu; odstraněn kustod `mann`. |
| `3-067r` | 67r | 385 | 7 | 3 | Pálení uhlí v hrnci se sírou a hlínou (`pokracovani: true`), pálení velkého milíře uhlí s atramentem a závěr Třetí knihy (*etc.* místo `ca`). |

---

## 2. Významné opravy BSB OCR a poznámky k závěru 3. knihy

- **Ozdobné iniciály**: doplněny na `3-065v` (`LEbendiger` – šestirádková iniciála `L`) a `3-066v` (`WIlt du` – sedmirádková iniciála `W`), dále opraveny menší iniciály a záhlaví odstavců v `3-056r`–`3-067r` (`SO`, `NIm`, `ITem`, `WIltu`, `THů`, `ES`, `NEme`, `ZErlaß`).
- **Zásadní opravy čtení OCR ze skenů `s363.jpg`–`s385.jpg`**:
  - `3-056v`: *breñ* (OCR `brest`), *fer* (`fer ?`).
  - `3-057r`: lékárnické symboly `℥` (OCR `3.`) a `ß` (OCR `f`/`ff`).
  - `3-059v`: *dickes* (`dines`), *ES* (`FS`), *gestehen* (`gefichen`), *zwei theil ein* (`zwet thelein`).
  - `3-060r`: *Reitter* (`Ketter`), *Brünnwasser* (`Grünwasser`).
  - `3-061r`: *WIltu* (`MIltu`), *alß ab* (`alfab`), oprava folia `61` (`σε`).
  - `3-062r`: *Rürstab* (`Xirstab`).
  - `3-062v`: *protzelt* (`proßelt`), *wöllest* (`willest`).
  - `3-063r`: odstraněn neexistující řádek z prosvítajícího rubu a doplněn vynechaný řádek předpisu.
  - `3-063v`: *seil* (`seid`), *knutzig* (`knugig`), *that man* (`that most`), *giessen* (`greffen`).
  - `3-064v`: *Alandt* (`landt`), *harthebig* (`Harthebig`), *in drei theil Wasser* (`Notain bret`), *sieden* (`fidlich` → *sitlich*), odstraněn čínský znak OCR ze skvrny (`湯`).
  - `3-065r`: *Thů den* (`Huben`), *in einem lautter* (`launer`), *auf dem Feur anhebt zu sieden* (`zu sieben`), *Glaritzenstein* (`Glarikenstein`), *2. lb.* (`2.16.`), *vngeleschten Klach* (autentická přesmyčka v tisku ponechána v `de` s poznámkou).
  - `3-065v`: *Volgt wie mann* (`Volgt`), *LEbendiger* (`Ebendiger`), *2. pfundt* (`pfundtschwefel`), *einen verdeckten* (`verdeckten`).
  - `3-066r`: *Alentbick* (autentická podoba předlohy za *Alembick*), *Ein Fadn soll dadurch gezogen sein.* (`typ: verse`).
  - `3-066v`: *WIlt du* (`Ilt du`), *Scheider* (`Scheider darauß`), *Atrimentum* (ponechán dobový pravopis *Atrimentum*/*Atrament* v tisku).
  - `3-067r`: *Einkolen zubereiten zu molen* (`Einkolen zu bereiten`), *Eier Doterlin* (`Eier Doterim`), *ein kreiß eins schůhß tieff* (`Freizeins fchuyp`), *lesch nit mit wasser* (OCR `lesch mit mit wasser` – obrácený význam!), *dem Puluer verderben / so thů man ein wenig Atrament zun Koln / etc.* (OCR zduplikovalo `fothan verderben / fothaman` a četlo `ꝛc.` jako `ca`).
