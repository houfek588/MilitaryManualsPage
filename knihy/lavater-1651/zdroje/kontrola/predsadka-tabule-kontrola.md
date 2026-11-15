# Kontrola L-K1 – předsádka, výklad, slovníček, básně, errata, mědirytiny (druhé čtení)

Strany: titul, vazba, venovani, predmluva-1…3, vyklad-1…4, slovnicek-1…2, basne-1…4, errata; popisy frontispis, tab-01 … tab-12.
Všech 30 stran: `stav: zkontrolovano`, `overeno_clovekem: false` (žádná nebyla ověřena člověkem).
`over_strany.py --prisne`: 0 chyb, 1 varování (slovnicek-2, blok 29 „Secours – vyproštění [obležených]“ – krátké heslo, poměr délek je v pořádku).
Pole `de` jsem skriptem znovu porovnal s `zdroje/dta/NNNN.txt`: shoda, jen *waa-|re* a *wel-|chem* přesunuté na stranu, kde slovo končí, a „rc.“ → „etc.“.

## 1. Přehled stran

| Strana | Zásadní změny |
|---|---|
| titul | beze změn (překlad v pořádku) |
| vazba | „blat“ překládáno „strana“ (dříve „list“), stejně jako ve výkladu a v errata; odstraněny zdvojené odkazy „[str. N, ř. M]“ za položkami, které totéž uvádějí v textu; **pozn. 1 opravena věcně**: výtisk HAB není svázán podle pokynu ze slovníčku, jak tvrdila původní poznámka – tab-01…06 jsou vpředu před s. 1, tab-07…12 mezi s. 80 a 81 (sken 114 → 116–125 → 127) |
| venovani | Quartierhauptleuhten: „čtvrťoví hejtmani“ → **obvodní hejtmani** (glosář); poznámka zkrácena |
| predmluva-1, -2 | beze změn |
| predmluva-3 | „Spříseženství“ → **Spříseženstvo** (glosář); poznámka zkrácena, značka přesunuta k datu |
| vyklad-1 | Real → **královská pevnost** (glosář, `{Real}` místo `{Hauptschantz}`); „vnější/vnitřní polygon“ → **mnohoúhelník** (glosář); poznámka o contregarde vypuštěna (je v glosáři, heslo val) |
| vyklad-2 | Affterstreych: „druhotná flanka“ → **zadní obrana** (glosář), i v hesle Streychlinien a v pozn.; `{defenslinien}` → `{beständige defenslinien}` (odkaz do glosáře); glosa „[boky, podpaží…]“ → „[bok, plece, ramena…]“ (Achsel = rameno, ne podpaží); nová pozn. 4: číslice 2 je na rytině rytá jako „z“ |
| vyklad-3 | „středový úhel“ → **úhel středu**; „obchozí cesta“ → **obchůzková cesta**; eskarpa jako cílový termín hesla; **nová pozn. 7** (písmena 2. mědirytiny) a u Batterey doplněno „[na rytině baterie fig. F a H]“; poznámky zkráceny tam, kde je vykládá glosář |
| vyklad-4 | „nášlapné bodce“ → **nášlapní ježci** (glosář); u Stagketen, Palissaden, Sturmhäspel, Fußängel, Schantzkörb, Schützenkörblein doplněno skutečné písmeno rytiny v [ ] + společná pozn. 2; **nová pozn. 5** (Approches – „3. Kupffer fig. B“ neexistuje), **nová pozn. 7** (Reduct – „fig. E“ na tab-01 není); `{Corps degarde}` odkazuje na strážnici; Breche: „bruch des Wals“ ponecháno v originále s glosou jako ostatní synonyma; vypuštěny poznámky dublující glosář (kleště, protiaproše, zákop, reduta, střelecké košíky) |
| slovnicek-1 | Capitain des armes, Cannonier, Cartusen, Collonell, Cornet, Controlleurs, Commiß, Fourrage, Garnison, Gouverneur, Granaden, Ingenieur, Matrosen, Marquitanter, Mineurs, Major dostaly `{…}` (odkaz do glosáře); Corporal – „rotmistr {Rottmeister}“ + pozn., že v překladu je Corporal jednotně desátník; „Flanckieren – „stírat“ … palbou z děl“; vypuštěny pozn. ke konstáblovi a majorovi (glosář) |
| slovnicek-2 | Secours / Secondieren → **vyproštění / vyprostit** (glosář vyprosteni); odkazy `{…}` u Picquenier, Quartier, Rondache, Sergeant, Sorties, Vivres, Voluntaire; vypuštěny pozn. k pikenýrovi a seržantovi (glosář) |
| basne-1 | „jasně je poznáváme“ → „jasně se mu učíme“ (lehrnen) |
| basne-2 | 1. verš: „hledíte si doby“ → „řídíte se dobou“ (bequemt euch den Zeiten) |
| basne-3 | „Jaké ozdoby…“ → „Jaké dary zvláště / duch pana Werdmüllera od vysokého nebe má“; „při té hře“ → „už zakusili boj“ (Schimpff ironicky = boj, srov. s. 114); poznámky upraveny |
| basne-4 | beze změn |
| errata | „list“ → „strana“; odkazy [str., ř.] ponechány jen u „tamtéž/téže strany“; Targe: „terč“ → **štít** (glosář); „rondela“ → „rondel“ |
| frontispis | „palcát s hroty“ → **kropáč** (ověřeno na obrázku: koule s hroty na násadě v trofeji vlevo nahoře) |
| tab-01 | „hrot bašty“ → špice bašty, „zadní flanky“ → zadní obrana, „záseky“ → retranšement; „Výklad … v předmluvě“ → v předsádce; číslice 2 = „z“; doplněno, že fig. E na rytině není; poloha ve výtisku |
| tab-02 | odkaz na doplněná písmena ve výkladu (ověřeno na obrázku – popis rytiny sedí) |
| tab-01…07 | nespisovné „se vazbí“ → „se má vevázat“ |
| tab-11, tab-12 | „kornet/kornetách“ (nejasné skloňování, glosář má kornet = praporečník i jednotka) → „jízdní kompanie“ |
| tab-03…10 | jinak beze změn; terminologie popisů odpovídá glosáři |

## 2. Posouzení sporných míst z překladatelských zpráv

- **preklad-predsadka:** návrh přejmenovat `list: předmluva` – už je „věnování (předmluva)“, ponecháno. Chyby DTA (Seribenten, Angeschen, Exccutionen, Historta, Gebilff, Zü, Waaffens-kunft, zalgebunden) správně ponechány v `de` a přeloženy podle smyslu. Výklad „flüssig“, „Blech“, „Practic“ přijímám jako pravděpodobný (viz níže). Návrh hesla „čtvrťový hejtman“ je překonán – glosář má `obvodni-hejtman`, sjednoceno.
- **preklad-vyklad:** „blat“ = strana – souhlasím (ověřeno např. s. 9, 12, 21); sjednotil jsem i vazbu a errata. „ii“ (snad 11), „Bollwerckspunet“, „a ngle“, „anglc“, „Carbes“ – ponecháno v de, v poznámkách. „nášlapné bodce“ zamítnuto ve prospěch glosáře (nášlapný ježek; ježek-šik má jiné heslo a odkaz). Corporal/Rottmeister – řešeno poznámkou, termín desátník zůstává.
- **preklad-tabule:** nesoulad písmen tab-02 jsem ověřil na obrázku (B kůlový plot, C palisády, D kozlice, E koše s dělem a košíky, F předprseň z košů, G koš, H baterie, I fronta, K aproše, L ježci) – souhlasí s popisem; poznámky doplněny na vyklad-3 a vyklad-4. Fig. E na tab-01 skutečně chybí. Ostatní body (tab-10 „VII“ místo „III“, číslování švadron, tab-04 přibližné přiřazení postav) jsou v popisech dostatečně uvedeny.

## 3. Sporná místa k rozhodnutí člověkem

| Strana | DE | CS (navrženo / ponecháno) | Proč sporné |
|---|---|---|---|
| vyklad-2 | „Groß Streychwinckel/ angle flanquant exterieur, angle de tenaille … mit 9. bezeichnet“ | velký obranný úhel; pozn.: odkaz „mit 9“ přesně neodpovídá | 9 je na fig. A špice bašty; úhel podle s. 3–4 leží proti středu kurtiny. Buď chyba tisku, nebo Lavater míní jiný úhel – ověřit na rytině ve vyšším rozlišení (DTA 1600px je pro fig. A nedostatečné). |
| vyklad-4 | „Approches … das 3. Kupffer. fig. B. mit 2. vnd 5.“ | ponecháno + pozn. 5 | Snad tisková chyba za „1. Kupffer“ (tam fig. B = reduta na konci aproše fig. K). |
| vyklad-4 | „Reduct … das 1. Kupffer. fig B. vnd fig. E. mit 9.“ | ponecháno + pozn. 7 | Fig. E na tab-01 není. |
| vyklad-3/-4 | písmena 2. mědirytiny | doplněno „[na rytině fig. …]“ | Rozhodnout, zda tento způsob (hranaté závorky v textu) vyhovuje, nebo stačí poznámka. |
| slovnicek-1 | „Corporal, Rottmeister.“ | „{Corporal} – rotmistr {Rottmeister}“ | Věrné Lavaterovi, ale v rozporu s konvencí Corporal = desátník; řešeno poznámkou. |
| slovnicek-1 | „Capitain des armes, Rüst oder Gewehrmeister.“ | „správce zbroje neboli zbraní“ | Obě glosy = jeden úřad (správce zbraní); „správce zbroje“ by šlo nahradit jen „správce zbraní“. |
| slovnicek-2 | „Particular, Gemein.“ | „obyčejný“ | Smysl nejistý (soukromý / obecný). |
| basne-2 | „Der Tiguriner Fälde / Fürwar auch flüssig sind“ | „Pole Tigurinů / jsou věru také plodná“ | flüssig = hojný, výnosný? |
| basne-3 | „Gleichwol ohn Joch vnd Blech“ | „bez jařma a pilířů“ | Blech nejasné. |
| basne-3 | „Was Zierden auch vorab / Des Herr’n Werdmüllers Sinn vom hohen Himmel hab“ | „Jaké dary zvláště / duch pana Werdmüllera od vysokého nebe má“ | Výklad „nebem dané nadání“ je můj návrh; alternativně narážka na astronomické přístroje. |
| vazba | „in der mitte des halben Thars“ | „uprostřed poloviny brány“ | Thars = Thors; branka uprostřed jednoho křídla vrat (s. 9). |

## 4. Návrhy do glosáře

| id | cs | de (doplnit) | kategorie | pozn |
|---|---|---|---|---|
| pika | píka | Spiessen | zbrane | `{Spiessen}` (vazba) teď odkazuje na **dlouhé kopí** (tvar je v hesle dlouhe-kopi); u Lavatera Spieß = píka – zvážit přesun tvaru nebo pozn. |
| obvodni-hejtman | obvodní hejtman | Quartier-Hauptleuth už má | velitele | Strana 081 (mimo dávku) překládá „kvartýrní hejtmani“ – sjednotit. |
| kornet | kornet | – | velitele | Ujasnit český tvar pro jednotku (korneta, ž.) vs. důstojníka (kornet, m.); s. 109 překládá Cornet jako „korouhev“. |
| zakladni-sik | základní šik | Fundamentsordnung | jednotky | (je) – OK |
| landschaft | venkov, venkovský kraj | Landschafft | mista | Curyšské poddanské venkovské území (proti Statt); v titulu a predmluva-2 v `{…}` bez odkazu. |
| mediryt | mědirytina | Kupffer, Kupfferblat, Kupffer-riß, Kupffer-rissen | (obecné) | Odkazy „Kupffer“, „fig.“ v celé knize. |
| cviceni | cvičení | Exercitium, Exereitien | jednotky | Cvičení se zbraní; dnes `{Exercitium}` bez odkazu (vazba, errata, slovnicek-2). |
| zdvojovani | zdvojování | Dopplierung, dopplieren | jednotky | s. 84–91, tab-07. |
| auditor | auditor | Auditeur | pravo | Vojenský soudce pluku (slovnicek-1, pozn. 2). |
| lancepasade | podrotmistr (lancepasáda) | Lancepasade, Vnder-Rottmeister | velitele | Franc. anspessade, zástupce desátníka. |
| podperny-tram | podpěrný trám | Vndersätzbaum, Vndersätzbäum | opevneni | errata k s. 116. |
| maly-polomer / velky-polomer | malý / velký poloměr | klein halbe Diameter, groß halb Diameter, Semi-Diameter polygoni interioris/exterioris | opevneni | vyklad-3; dnes bez odkazu. |
| vnitrni-polygon | vnitřní mnohoúhelník | Interieur polygone | opevneni | Spojnice bodů hrdla; doplnit k vnějšímu mnohoúhelníku. |
| uhel-ramene | úhel ramene | + espaule? | opevneni | Lavater řadí espaule k flance – ponechat u flanky, jen pozn. |

**Osoby a místa** (na stranách dávky; vše už v glosáři): Lavater, Bodmer, Vegetius, Eberhard, Brändli, Ardüser, Meyer, Werder, Holzhalb, Körner, Werdmüller, Curych, Spříseženstvo, Švédsko, Limmat, Rýn. Chybí: **Tigurini / Tigurum** (mista; humanistické jméno Curyšanů, basne-2), **Mojžíš, Amalek, Izrael** (biblické, basne-4), **Mars** (basne-1, -2), **J. W. S.** a **G. M.** (neurčení autoři básní), **Samuel Marolois** (heslo je, ale jen de „Maralois“ – doplnit „Marolois“).

## 5. Mimo dávku (needitováno)
- 081: „kvartýrní hejtmani {Quartier-Hauptleuth}“ → podle glosáře „obvodní hejtmani“.
- 109: „kompanie {Compagnie} čili korouhev {Cornet}“ – sjednotit s heslem kornet.
