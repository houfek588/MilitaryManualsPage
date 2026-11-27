# Překlad – dávka E (skeny 89–110, strany 045r–055v)

Všech 22 stran má `stav: prelozeno` a `overeno_clovekem: false`. `over_strany.py --prisne` hlásí 0 chyb a 2 varování (falešný poplach: „fia“ = „krát“ v násobení, 046r a 055r).
Každou stranu jsem porovnal se skenem a čísla v obrazcích jsem si zvětšil výřezem.

## Obsah
- **045r–046r (kniha IV, Quesito II–III, hrabě Hieronimo da Piagnano):** pochodový sled, který lze rychle převést na čtvercový šik. Je to třetina odmocniny počtu mužů v řadě, rozdělená do tří částí; jsou rozebrány zbytky 1 a 2 při dělení třemi (příklady 100, 121, 3969, 5776, 2809, 4000). Quesito III ukazuje pravidlo pro šik podobný šiku o 1000 mužích s 49 muži v čele (příklad 3500 → 91 mužů v řadě, 38 do hloubky, zbývá 42).
- **046v (Q. IV, vrchní šikovatel vévody z Urbina):** šik čtvercový co do plochy (7 × 3 stopy na muže podle Vegetia, dělitel 21; příklad 3600 → 91).
- **046v–050r (Q. V–IX, převor Gabriel Tadino):** klín (řada lichých čísel 1, 3, 5 …), nůžky, útok klínu na šik čtvercový co do plochy, pila (4 zuby po 25 mužích a podpůrný šik 144 mužů po 36) a kosočtverec (320 mužů).
- **050r–050v (Q. X):** rohatý šik ze 300 mužů (dva čtverce po 100 jako rohy a uprostřed šik čtvercový co do plochy).
- **051r–051v (Q. XI):** jak po zásahu dělostřelectvem přesunout prázdná místa z čela do týlu (příklad 144 mužů, 12 padlých).
- **052r–053r (Q. XII):** jak čtverec obrácením mužů šikmo přeměnit v klín (25 písmen a–ꝯ).
- **053r–054r (Q. XIII):** rozhovor o síle Turka, o dělostřelectvu, o vzpomínce na Rhodos a o tom, co dokáže umění proti přírodě. Konec knihy IV.
- **054v–055v (kniha V, Q. I, Richard Wentworth):** stavba buzoly – plechový kotouč, osm větrů, dělení na 360 nebo 72 dílů, střelka, skleněné víčko a dva druhy dioptry.

## Ověřeno ve skenu / nejistá čtení
- 046r: „auanzara .122.“ – prostřední číslice je slitá. Čtu 122 (8403 − 91² = 122), OCR má „12“.
- 051r/051v: konec 051r „subito debb…“ zasahuje do vazby. Zapsal jsem „debba“, protože 051v začíná „à longare i passi“.
- 049r: obrazec pily s podpůrným šikem má pod hroty zřetelně jen 4 souvislé řady (základna a 3 podpůrné řady), text vyžaduje 5 (144 : 36 = 4 podpůrné řady). Uvedeno v `popis`.
- 048r: obrazec – v šiku vlevo počítám 6 řad po 15 tečkách a jednu osamocenou tečku, ne 100 mužů. U čela jsou písmena b, a, c.
- 052r/052v: poslední znak abecedy je zkratka ꝯ (con).
- 055v: končí „…sia de tal“, slovo „grandezza“ je celé na 056r (dohoda s dávkou F).

## Sporná místa a chyby předlohy (v `de` ponechány, vysvětleny v poznámkách)
- 050r: „pigliarne quelli fanti .19. che ui manca“ – správně je 9. Překlad drží tisk („19“) a poznámka věc vysvětluje.
- 050r, Převorova replika: „fanti desnoue … cento settantanoue“ – správně 16 a 176. Výsledných 55 sedí jen se 176. V textu je ponecháno podle tisku.
- 050r: „primo rhombo“ místo „primo cuneo“.
- 050v: „gia fatta in forma quadra di gente“ u prostředního šiku, který je ve skutečnosti „quadra di terreno“. Dále tisková chyba „qustea“.
- 046r: „bttaglia“. 052v: „cal figura“ a „se approssimata“.
- 052v: tvrzení „il doppio del solito“ – úhlopříčka je ve skutečnosti √2krát delší, ne dvojnásobná.
- 048v a 052v: „di sotto appare“, obrazec je však nad textem nebo na protější straně.
- 045r: „par che disdicano assai“ přeloženo „vypadají dost nevhodně“ (disdire = nehodit se, nesluší).
- 053v: „haueriano persa la scrimia“ přeloženo „ztratili svou zdatnost“ (scrimia = šerm, obratnost).

## Terminologie, kterou jsem v dávce držel
- battaglia / ordinanza = šik
- quadra di gente = čtvercový co do mužstva
- quadra di terreno = čtvercový co do plochy
- fila = řada; „fila per longo“ = řada po délce
- per testa = v čele
- fanti = pěšáci
- Sargente = šikovatel; sargente maggiore = vrchní šikovatel
- cuneo = klín, forfice = nůžky, serra = pila, rhombo = kosočtverec, corni = rohy
- radice (propinqua) = (nejbližší) odmocnina
- bossolo = buzola, dioptra / trasguardo = dioptra / průzor, lancetta / lanzetta = střelka, calamita = magnetovec, armilla = obruč, scatolina = pouzdro (podle dávky F)
- Oslovení: Převor = „Vaše Důstojnost“ (V.R.), jinak „Vaše Milost“ (V.S.).
- Mluvčí: **Hrabě Hieronimo.**, **Šikovatel.**, **Převor.**, **Richard.** (podle dávky F)
- Nadpisy quesit: „Otázka první/druhá…, kterou položil …“. Dávka F používá „Druhý dotaz, který položil …“ – formu je třeba sjednotit při revizi.

## Návrhy do glosáře
- id `sik`: přidat do `de` tvary battaglia, battaglie.
- id `rota`: zvážit cs „řada“ (Tartaglia počítá „fanti per fila“ = muži vedle sebe).
- `klin` – cs klín; de cuneo, cunei, forma cunea; kategorie jednotky; pozn.: trojúhelníkový šik z řad 1, 3, 5 …; ze čtvercového počtu mužů vychází beze zbytku.
- `nuzky` – cs nůžky; de forfice; jednotky; pozn.: dva spojené klíny proti klínu (Vegetiova forfex).
- `pila` – cs pila; de serra, sega; jednotky; pozn.: řada klínů („zubů“) vedle sebe, případně s podpůrným šikem.
- `kosoctverec` – cs kosočtverec; de rhombo, figura rhombica; jednotky.
- `rohaty-sik` – cs rohatý šik; de battaglia cornuta, corni; jednotky.
- `sikovatel` – cs šikovatel; de sargente, sergente, sargente maggiore; velitele; pozn.: staví pěchotu do šiku.
- `quadra-di-gente` – cs čtvercový co do mužstva / co do plochy; de quadra di gente, quadra di terreno; jednotky; pozn.: stejný počet řad a mužů v řadě × čtverec půdy (pěšák zabírá 3 × 7 stop).
- `dioptra` – cs dioptra; de dioptra, trasguardo; mereni; pozn.: otočné zaměřovací rameno s destičkami s dírkou.
- `strelka` – cs střelka; de lancetta, lanzetta; mereni.
- `magnetovec` – cs magnetovec; de calamita; mereni.
- `vitr` – cs vítr (směr růžice); de uento, uenti; mereni; pozn.: 8 větrů – Tramontana, Greco, Levante, Sirocco, Ostro, Garbino, Ponente, Maestro.
- `stupen` – cs stupeň; de grado, gradi; mereni.
- `arkebuzir`: doplnit tvar archibuseri.

## Osoby a místa pro rejstřík
- Hieronimo da Piagnano (hrabě)
- vrchní šikovatel vévody z Urbina
- Gabriele Tadino da Martinengo, rytíř rhodský a převor barlettský
- Vegetius
- Eukleidés
- Giovanni Battista della Valle („el uallo“)
- Turek (Selim I.)
- Sofi (šáh Ismáíl I.) – bitva u Čaldiránu 1514
- Rhodos – obléhání 1522
- Ptolemaios (Geografie, chorografie)
- Richard Wentworth (Richardo Ventuorth)
- Anglie
- Německo („Alamagna“, kompasové sluneční hodiny)
- Barletta
