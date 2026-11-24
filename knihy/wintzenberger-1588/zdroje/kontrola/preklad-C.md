# Překlad – dávka C (skeny 49–70 a 32–33)

Strany: `023r`–`033v` (skeny 49–70) a `014v`, `015r` (skeny 32–33). Všech 24 stran má `stav: prelozeno`,
`overeno_clovekem: false`. `python -I nastroje/over_strany.py knihy/wintzenberger-1588 <24 stran> --prisne`
→ 0 chyb, 0 varování. Každá strana byla porovnána se skenem (1600 px, sporná místa ve výřezu).
Sousední skeny 48 a 71 jsem jen četl kvůli návaznosti: `023r` začíná slovem „geschrey“ (rozděleným „ge-|schrey“, celé
patří na `023r`), `033v` končí uzavřeným 30. artikulem, 31. artikul začíná na skenu 71.

## Obsah
- **023r–023v (konec pochodového a bitevního řádu):** varování před „pokřikem“ o slunci a větru; jak postavit děla
  a jízdu podle pole a podle síly nepřítele (děla na obě strany, jízda vně děl). Návod platí pro vojsko „obyčejného knížete“
  o 10 000 pěších a 1500 koních. Dále noční ležení u vody a dříví, bdělé stráže a spolehlivé zprávy.
- **024r – Jak se utábořit před městy:** oběhnutí města, šarvátka, prohlídka, 2–4 dny ostřelování, rychlý útok;
  nepodaří-li se, odtáhnout. Příklad Francouzů.
- **024v–025v – Jak dobrým řádem udržet město:** kvartýry na hradbách, střídání polovin, záložní šik na prostranství,
  velitelé úseků, kněží a ženy u hašení požárů, soupis a příděl zásob. Závěrečná prosba autora a „Ende des Ersten Theils“
  s vinětou.
- **026r:** titul Druhého dílu a jeho obsah (I. služební a artikulní list Karla V., II. lodní řád, III. hrdelní právo
  a právo dlouhých pík).
- **026v–030r – Služební list Karla V. (1543):** pověření vévody z Alby naverbovat pluk o 12 praporcích po 400 mužích;
  plukovníkem je J. B. z Lodronu, hejtmanem a nejvyšším poručíkem F. z Arca. Následuje stav plukovníka, stav vysokých
  úřadů (tabulky) a instrukce přehlídkovému komisaři: kdo smí projít přehlídkou, přeplatky, první list, pacholata
  a podvody se jmény.
- **030r–033v – Artikulní list (art. 1–30):** přísaha, poslušnost, žold 4 zl. na měsíc o 30 dnech, zběhnutí, ochrana
  žen a kostelů, rouhání, dobytí města místo útočného žoldu, kořist, útěk z boje, poplach, výpalné, mlýny, rozmluvy
  s nepřítelem, dvojí zápis, obec bez svolení, stráže, proviant, cizí národy, jízda v ležení, přísaha na 6 měsíců,
  žold 3 koruny a příplatek hákovničářům.

## Skeny 32–33 (strany 014v, 015r) – důležité zjištění
Zadání předpokládalo, že jde o týž text v odlišné sazbě. **Porovnáním skenů jsem zjistil, že nejde o jinou sazbu, ale
o tutéž fyzickou dvojstranu [30] v – [31] r vyfotografovanou dvakrát:**
- shodné zalomení všech řádků, rozpal i kustody („erleub-“, „seines“);
- shodně poškozené litery (např. „Ste?ten“ v 9. artikulu, zalomené „tüglichsten“);
- **shodné ruční inkoustové značky na okraji** (háček u 3. artikulu na skenu 32/64, u 7. artikulu na skenu 33/65)
  – ve výřezech se kryjí tvarem i polohou vůči textu;
- signatura líce je na skenech 33 i 65 „H iij“ (stejná litera H jako na skenu 61, odlišná od D na skenech 29 a 31).
  List [15] r by nesl „D iij“.
Rozdíly mezi soubory OCR 0032/0033 a 0064/0065 („ist“ na zvláštním řádku, „4. Zum“, „9.“) jsou jen šum OCR.
Ve skenech se liší jen expozice a ořez (posun asi 20 px).

**Odchylky sazby: žádné.** Přepis `de` stran 014v/015r je proto shodný s 030v/031r. Překlad je převzat beze změny
a na obou stranách je poznámka 1, která to vysvětluje a odkazuje na 030v/031r. První blok 014v nemá
`pokracovani` (nenavazuje na 014r), první blok 015r ho má (navazuje na 014v).
**Návrh:** v `kniha.yaml` (`strany_poznamka`) opravit „odlišně vysázený“. Jde o chybu digitalizace: místo dvojstrany
[14] v–[15] r (pokračování pochodového řádu mezi „oder wie“ na skenu 31 a soupisem munice na skenu 34) byla podruhé
nasnímána dvojstrana [30] v–[31] r. Zda list [14]/[15] fyzicky chybí i v exempláři, ze skenů určit nelze
(v exempláři je pravděpodobně přítomen).
Kdyby se později měnil překlad 030v/031r, je třeba stejnou změnu provést i v 014v/015r.

## Místa ověřená ve skenu / tiskové chyby (ponechány v `de`)
- 024r „wenn man **daraor** kömpt“ – ve výřezu zřetelně „daraor“ (za „daruor“); poznámka.
- 023v „durch angeben **besser** kundschafft“ – tisk „besser“, smysl žádá „böser“; přeloženo doslova s poznámkou.
- 026r „alldo **vrehalten**“ (za „verhalten“).
- 027r „obristen **Leutenapmt**“ (přesmyk za „Leutenampt“).
- 027v „wenn wir jhrer **lenger** notdürfftig sein“ – chybí „nicht“; v překladu doplněno [už] … nepotřebovali.
- 028v „Summa Summarum / aller dieser Soldt **vnd vnd** Vbersoldt“ a „Geschehen **instruction** auff Musterung
  **instruction**“ – porušená sazba (chybí datum, nadpis instrukce vsazen do textu); v překladu rozčleněno.
- 028r tabulka: 8 jízdních koní „auff eines 10. fl. thut 80. fl.“ (OCR „so“), součet stavu plukovníka v tisku **600 zl.**,
  ačkoli položky dávají **640 zl.** – ponecháno, vysvětleno poznámkou.
- 028v čísla: „Item **10.** Feldwebel / einem jeden **3.** Vber sold / thut **120.** fl.“ (výřez), Steckenknechte **48** zl.,
  celkem **468** zl. (sedí s položkami).
- OCR skenu 62 zdvojuje slova („auff auff“, „nachfolgender nachfolgender“, „Trummelschlagern Trummelschlagern“,
  „sol fol der der Feldweibel Feldweit“) – v tisku nic zdvojeno není, přepsáno podle skenu.
- Fraktura H čtená OCR jako D (Dauptman, Derren, Doltz, Deuser, Darnisch, Dacken) a V jako D (Vehste, Vheste)
  – opraveno všude. Čísla artikulů 12, 13, 15 (OCR „13“, „13“, chybějící „15“) opravena podle skenu.
- 030v „auff **Zug** vnd Wacht“ (bez přehlásky, ověřeno výřezem).

## Sporná místa (DE – CS – důvod)
- 023r „Ist aber das Fusuolck zu starck / **diesem hauffen**“ – „je-li však na tento houf příliš silná jeho pěchota“ –
  dativ „diesem hauffen“ syntakticky visí; chápu ho jako „na náš houf“.
- 024v „ein jetzlicher soll auch sein **Geschütz** … auff der Vehste bey sich haben“ – „zbraň“ – zde zjevně palná zbraň
  jednotlivce, nikoli dělo.
- 025r „das man **Quartiermeister** mache / achte“ – „kvartýrmistři – osm“ – nejde o kvartýrmistra ležení, ale
  o velitele úseků hradeb; poznámka.
- 027r „als **Hauptman vnd obristen Leutenapmt**“ – „jako hejtmana a nejvyššího poručíka“ – z věty neplyne, kdo
  zastává který úřad; artikulní list jmenuje Lodrona plukovníkem a Arca „jrer May: Hauptman“.
- 027r „für **jhren oder derselbigen vermügen** wol bezalet werden“ – „podle své či jejich možnosti“ – nejasné.
- 028v „Angeber vnsers Deudschen Kriegesuolcks“ – „zapisovatel {Angeber}“ – snad „Annehmer“ (verbíř).
- 028v „gen **Reinhausen**“ – nejisté místo (snad Rheinhausen u Speyeru).
- 029r „auch sol er **die gebunden** / vnd sonderlich die Wunten cassiren“ – „obvázané a zvláště raněné“.
- 029v „Fürer / **Vorehrer** / beyden Weibeln“ – „vůdce, furýr“ – „Vorehrer“ chápu jako „Forierer“.
- 029v „Im ersten Blat sol der Feldweibel 1. Soldt / vnd **im andern des Obristen Stadt 3. Soldt**“ – přeloženo doslova,
  smysl nejistý; „mit wie viel **schulden** dieselben möchten **zu endern gestalt** werden“ – vykládáno jako „kolika
  žoldy by mohli být uspokojeni“.
- 031v art. 9–10: „sein Monat seines diensts begreifft / aus vnd angehen“ – „měsíc … skončit a [nový] začít“ (náhrada
  útočného žoldu); art. 10 je v tisku syntakticky porušený, přeloženo podle smyslu.
- 031v art. 11 „die Besetzten vnd **Beschüldigten** bey der sicherung bleiben lassen“ – snad „Beschädigten“.
- 033v art. 29 „jhrer May: **nöthlich** zu dienen“ – „podle potřeby“ (snad za „redlich“).
- 033v art. 30 „sie sollen auch schuldig sein / mit dieser Bezahlung …“ – chybí sloveso, doplněno „[spokojit se]“.
- 026v nadpis „zu **Maron im Etzschlande**“ – „v Maronu v Adižsku“; Maron = nejspíš Meran (Merano).

## Návrhy do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| prvni-list | první list | erste Blat, ersten Blat, ersten Blats | zold | Prima plana – první list přehlídkového rejstříku praporce se jmény hejtmana, praporečníka, šikovatelů a dalších úředníků s vyšším žoldem. |
| koruna | koruna | Kronen, Krone, Cronen | miry | Zlatá koruna (zvl. francouzská sluneční); ve 32. artikulu za 23 bacenů. Případně přidat tvary do hesla `slunecni-koruna`. |
| lehengeld | záloha na žold | Lehengeldt | zold | Peníze vyplacené předem jako půjčka (Lehen) na žold, odečítané při řádné výplatě. Pozor na kolizi s heslem `zaloha` (Halt = skrytý oddíl). |
| instrukce | instrukce | instruction | sluzba | Písemný pokyn válečného pána komisaři (zde k přehlídce). |
| rinkkragen | nákrčník | Rinckkragen, Ringkragen | zbrane | Plátový nákrčník; spolu s pancéřovými rukávy a šturmhaubou výstroj na 6 zl. žoldu. |
| sturmhaube | šturmhauba | Sturmhauben, Sturmhaube | zbrane | Otevřená přilba (burgundka). |
| pancerove-rukavy | pancéřové rukávy | Pantzerermeln | zbrane | Kroužkové rukávy nošené ke kabátci nebo zbroji. |
| hofmistr | hofmistr | Hoffemeister | velitele | Vrchní dvorský úředník (mayordomo mayor) – titul vévody z Alby. |
| sarvatka (doplnit) | šarvátka | Scharmützel | – | tvar „Scharmützel“ už v hesle je, bez změny |
| obec (doplnit) | obec | gemein (shromáždění) | – | doplnit do pozn.: „kein gemein halten“ = nekonat shromáždění obce bez plukovníka (art. 21). |
| stav (doplnit) | stav | Stadt | – | do `de` doplnit tvar „Stadt“ (velké S; „Stadt eines Obristen“, „Stadt der hohen Empter“). |
| vypalne (doplnit) | výpalné | Brantschetzen | – | tvar už v hesle je jako „Brantschatzen“; doplnit „Brantschetzen“. |
| hakovnice (doplnit) | hákovnice | Hackenschützen | – | v překladu „střelci z hákovnic“; zvážit samostatné heslo `hakovnicar`. |
| vehste | opevnění, hradba | Vehste, Vheste, Vehsten | opevneni | Feste – hradby a opevnění města (024v–025r). |

## Osoby a místa pro rejstřík
- Karel V., římský císař (026v, 030r a dál) – heslo `karel-v`.
- Fernando Álvarez de Toledo, 3. vévoda z Alby („Duca de Alba“) – 027r.
- Johann Baptist (Giovanni Battista) hrabě z Lodronu („Johan Baptista Graffen zu Ladron“) – 027r, 030r.
- Felix hrabě z Arca („Graffen Felix von Arch“) – 027r, 030r.
- Maron im Etzschlande (Meran?, Adižsko) – 026v, 030r.
- Reinhausen (shromaždiště) – 028v.
- Itálie (cíl pluku) – 027v, 028r; Kastilie (původ peněz, 31. artikul na skenu 71 – mimo dávku).
- Francouzi („Der Frantzos“) – 024r.

## Obrázky (bloky doplněny, soubory dodá správce)
`drevorez-54.jpg` (oválná viněta, 025v), `drevorez-55.jpg` (ozdobná lišta, 026r), `drevorez-56.jpg` (portrét
„Karla V.“ v rámu, 026v), `drevorez-63.jpg` (lišta před artikulním listem, 030r).
