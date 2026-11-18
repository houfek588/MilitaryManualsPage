# 2. revize – Solms 1559, První kniha, dávka B (`1-011r`–`1-020v`)

Rozsah: 20 stran (skeny 31–50), sousedé `1-010v` a `1-021r` jen čteni. Řídil jsem se zadáním `ZADANI_REVIZE2.md`: plynulost „středně“, věrnost a terminologie podle glosáře. Struktura bloků, `id`, `sken`, `stav: zkontrolovano` a `overeno_clovekem: false` zůstaly beze změny.
Skeny jsem stáhl z BSB IIIF (`bsb00085168_000NN`, 1400 px).

Ověření: `python -I nastroje/over_strany.py knihy/solms-1559 1-011r … 1-020v --prisne` → **20 stran, 0 chyb, 0 varování**.

## 1. Hlavní změny po stranách

| Strana | Změny |
|---|---|
| `1-011r` | Opraven posunutý význam: *mit allen Emptern darinnen beschlossen* „žold …, jenž je v něm zahrnut“ → „žold se všemi úřady, které jsou v něm zahrnuty“. Výklad o komisařích jsem rozdělil do tří vět a opravil podmět: komisaři plní rozkaz *jejich* pána (pána jezdců), jezdci mají naopak táhnout pokojně a platit. *in vnd durch der Freundtlandt* → „do země přátel a skrze ni“. *vnbilliche bezallung oder vberlast* → „nespravedlivě zaplacen nebo utiskován“ (dříve „bezpráví při placení nebo násilí“). |
| `1-011v` | Dlouhé souvětí o přehlídce jsem rozdělil do osmi vět. *die Pferdt fürn vnd vnter jhrem Sattel haben* „vedou koně a mají lidi pod svým sedlem“ → „přivádějí koně a mají je pod vlastním sedlem“. Rozbitou vazbu „vyslechli jste již dříve pánův úmysl, o čemž nelze pochybovat, že se…“ jsem nahradil větou „vyslechli jste již předtím vůli válečného pána, a není pochyb, že se podle ní budete umět zachovat“. |
| `1-012r` | 1. blok rozdělen do vět („volní žoldnéři“ místo „svobodní“). Odstraněna poznámka 1: opakovala heslo glosáře `jednokony-jezdec` a doplňovala jen informaci o OCR. Proviantní odstavce přeformulovány („podle úředního ocenění“ místo „podle úřední taxy“ za *nach der schatzung*). Formuli přísahy jsem ponechal. |
| `1-012v` | *im Regiment ziehen*: odstraněno zavádějící `{Regiment}` (web by ho odkázal na heslo „pluk“) a doplněna poznámka 1 (Regiment = správa, kázeň). Velký odstavec o válečné radě rozdělen do sedmi vět s nepřímou řečí pána. Konec strany přeformulován, aby navazoval na `1-013r` („To vše jim chce přikázat jako mužům válečným a | rytířským…“). Poznámky přečíslovány. |
| `1-013r` | Návaznost z `1-012v` opravena. Přehlednější slovosled a rozdělené věty ve všech blocích, *wie vor zu dem ernstlichsten* → „jako předtím co nejvážněji“. Opraven způsob: „Zmíněná vrchnost tedy obešle“ → „Tato vrchnost má pak obeslat“ (*soll*). |
| `1-013v` | Dlouhý blok rozdělen do vět. Pravidlo o soudu žalovaného jsem přeložil srozumitelně: „aby se nepřely o to, který národ má jít k druhému … strana žalobcova musí jít tam, kde je žalovaný“. Odstraněny poznámky k *Sudler* a *Auditores*, protože jen opakovaly glosář. Poznámka k *Jstitien* přečíslována na 3. |
| `1-014r` | *finantz vnd schinderei* → „fintu a vydírání“. Nejasné *für ein Regiment zu nemen geordnet* → „ustanovilo ji jako jeho vládu“ + nová poznámka 1. Rétorické otázky jsem rozdělil do vět. Přidaný výklad „co by si o tom lidé pomysleli“ jsem nahradil věrným „co tím vlastně sledují“ (*was sie darmit haben wolten*). |
| `1-014v` | Plukovní soudy by byly „jejich sluhy a poddanými“ (dříve chybně „sami … jejich čeledíni“). Odstraněno zavádějící `{Knecht}` a `{Regiment}`, doplněno `{Reuter recht}`. Rozděleno do vět, rétorická otázka o 24–30 přísedících přeložena jako otázka. Soudní formule přeformulována: „když se ustavují, vyhlašují se ve jménu válečného pána a zahajují, zapovídají či vymezují“. |
| `1-015r` | *mit grundt abzunemen* → „lze s dobrým důvodem usoudit“ (dříve „z gruntu prohlédnout“). *Damit aber diser sach mag abzuhelffen sein* → „Aby se však ta věc rozhodla“ (ironická zkouška doktorů). Na konci strany úprava návaznosti („neboť jsou | spolu užiteční při poradách“). |
| `1-015v` | *gleich vorgenomen* → „zavést … stejně pro všechny“ (dříve „ihned“). Úvod článku o rouhání rozdělen do vět; *vnd ich 24. Artickel … gestelt hab* → „Sepsal jsem sice 24 trestních článků, ale…“. Upraveno „se mnou, tehdejším polním maršálkem“. |
| `1-016r` | **Oprava `de` podle skenu:** `auff ein stuk` → `auff einen stutz` (tisk *eiñ stutz*), `gluck/vngluck` → `glück/vnglück` (4×, přehláska ve skenu zřetelná). Poznámka 3 o „stuk“ zrušena, poznámka 1 opravena (*erschweren* ≈ *erschwören* – „přísahou vymoci“). V češtině opraveno „ke zlehkomyslnění sebe sama“, „nadarmo se rozhněvává“ (mylně zvratné → „popouzí k hněvu“). Nepřímou řeč polního hejtmana jsem rozdělil a opravil vazbu *daß sie jm dazu wolten behilfflich sein* (prosba hejtmana, ne podmínka autora). |
| `1-016v` | Rozdělení vět. *trützlich fleissen* → „vzdorovitě pokračoval“. *darüber gehalten* → „pevně při nich stáli“ (dříve „drželi nad nimi ochrannou ruku“). Nová poznámka 1 k *auffhebung … seiner Göttlichen gnaden* (rouhavé dovolávání se Kristových ran). Poznámka k Desateru přečíslována na 2. |
| `1-017r` | Vypuštěno přidané „malé“ (děti) a „jen“ (druhá deska), zbytečné „tělem i duší“ (*an seinem leib*) nahrazeno slovem „vskutku“. Úvaha o Otčenáši a závěrečné souvětí rozděleny do vět. |
| `1-017v` | Popis dřevořezu po prohlédnutí `drevorez-044.jpg` zpřesněn: „uťaté ruce“ → „probodené ruce, srdce a nohy (pět ran Kristových)“, doplněn klobouk s péry. |
| `1-018r` | *mehr auß angenommenem fleiß dann leichtfertigkeit* „ze strojené zpupnosti“ → „spíše schválně a z navyklé horlivosti než z lehkomyslnosti“. Opravena vazba „aby do nás vlil … upevnění naší víry“ → „prosit o upevnění naší víry a o to, aby do nás vlil … lásku“. Rozdělení vět, konec strany navazuje na `1-018v` („zaslíbil své modle | oběť a dary“). Odkaz v poznámce 1 nyní zní `[[1-017v|dřevořez na protější straně]]`. |
| `1-018v` | Přeformulována věta o pohanech a křesťanech (dříve neobratné „u pohanů … bylo jméno … ctěno“). Sjednoceno „synové Izraele“. Citát ze Siracha dán do uvozovek přes hranici strany. |
| `1-019r` | **`de`:** `vngluck` → `vnglück` (sken). Nadpis: „s výkladem jim stanovených trestů“ → „s výkladem trestů, které jsou za ně stanoveny“. Čl. 4: *Prouiantpletzen* podle glosáře „proviantní tržiště“. Doplněna koncová uvozovka citátu. |
| `1-019v` | Čl. 9: *weitter dann das rauhe futer* jsem přiřadil ke správnému členu („Kdo by vzal víc než hrubou píci…, má být postaven před soud“). Čl. 6: *so ins Leger gehörig* se vztahuje k proviantu. Čl. 13: „vyobcován“ → „vykázán“. Čl. 12: „výstřel polního znamení“ → „signální výstřel“. |
| `1-020r` | Číslování článků sjednoceno s `1-019r`/`1-019v` („Za čtrnácté, …“ místo dvojtečky). Čl. 15: „bez dovolení svého rytmistra“ (*von seinem Ritmeister on erlaubnuß*). Čl. 17: slovosled (soud „z jízdy i pěchoty“), *das jm soll geschriben werden* → „má mu to být písemně oznámeno“. |
| `1-020v` | Čl. 19: *dem Kriegßherrn zu nachtheil seinem Ritmeister oder Obrigkeit* → „ke škodě válečného pána, svého rytmistra nebo vrchnosti“ (dříve „proti svému rytmistrovi“). Čl. 24 rozdělen, závěrečné odstavce přeformulovány. *auffruhr* podle glosáře „vzpoury“ (dříve „bouře“). |

## 2. Místa ověřená ve skenech

- s31 (`1-011r`): `das maň` = *mann*, `Regirung der Justitien`, `Commissarien` – `de` souhlasí.
- s36 (`1-013v`): tiskové chyby *Parth* a *Jstitien* jsou skutečně v tisku. Poznámky jsem ponechal.
- s41 (`1-016r`): *auff eiñ stutz* (OCR „ein stuk“) a *glück, vnglück* s přehláskou (OCR „gluck“) → **opraveno v `de`**. *schendt-lichen* je správně. *nach … nach* je tisková podoba (poznámka 2 platí).
- s47 (`1-019r`): *vnglück* s přehláskou → opraveno. *gestraff* je tisková chyba (poznámka 3 platí). Iniciála *ERstlich* a *Prouiantpletzen* souhlasí.
- s50 (`1-020v`): *puncken*, *Fendlin* a *zurechtfertigen* souhlasí s tiskem.
- Dřevořez `drevorez-044.jpg`: signatura *SEBASTIAN . H.* a celá ikonografie odpovídají popisu.

## 3. Sporná místa k rozhodnutí

1. **`1-014r`** – *vnd für ein Regiment zu nemen geordnet*. Nově „ustanovilo ji jako jeho vládu“ s poznámkou. Lze číst i „a nařídilo [ji] brát za pluk“, tedy justice jako znak samostatného pluku. Doporučuji ověřit znalcem.
2. **`1-016r`** – *darmit erschweren*. Vykládám ho jako *erschwören* („přísahou vymoci“). Možná je to i tisková chyba za *erwerben* („získat“); smysl se tím nemění.
3. **`1-016v`** – *mit auffhebung vnd vbel gedencken seiner Göttlichen gnaden vnd leidens*. Překlad zní „v klení vytahujeme a zle o nich mluvíme“. *auffheben* může znamenat i „vyčítat“.
4. **`1-018v`** – *so offt sein Königliche Kron … verzuckt*. Doplnění „kdykoli [je zaslechl]“ je výklad; v tisku chybí, při jaké příležitosti král korunu smekal.
5. **`1-019v` čl. 6** – *die Prouiant vorm Leger oder andern ortten so ins Leger gehörig*. Vztažnou větu vztahuji k proviantu („který patří do ležení“); může se vztahovat i k místům.
6. **Termín *Justitien*.** V celé dávce je přeložen jako „justice“ (správa soudnictví), glosář ho vede pod heslem `soud`. Ponechal jsem „justice“, protože Solms rozlišuje *Justitien* (soudní správu národa či pluku) a *Gericht* (konkrétní soud). Navrhuji samostatné heslo (viz níže).
7. **Termín *Oberster / Oberst* bez přívlastku** (`1-014v`, `1-015r`, `1-020r`). Je přeložen jako „nejvyšší velitel“, ale `{…}` odkazuje na heslo `plukovnik`. Glosář na tento význam upozorňuje, odkaz ale může mást.

## 4. Návrhy do glosáře

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| `justice` (nové) | justice | Justitien, Justitia, Justitica, Jstitien | pravo | Soudní správa (soudní moc) pluku či národa; Solms ji odlišuje od jednotlivého soudu (*Gericht*). Nyní pod `soud`. |
| `soud` (doplnit) | soud | Reuter recht | pravo | Varianta *Reuter recht* (`1-014v`); v glosáři je jen *Reutter Recht*. |
| `sluzebni-list` (doplnit) | služební list | bestallungen | – | Malá varianta z `1-012r`. |
| `prisaha` (doplnit) | přísaha | eidt | – | Varianta z `1-011v`, `1-014r`. |
| `tazeni` (doplnit) | tažení | feldzuge | – | Varianta z `1-011v`. |
| `pice` (doplnit) | píce | fůterung, futer | zold | Varianty z `1-019v` (*rauhe futer* = hrubá píce). |
| `artikulni-list` (doplnit) | artikulní list | Artickelbrieffs | pravo | Genitiv z `1-014r`. |
| `regiment-sprava` (nové, volitelné) | správa, vláda | Regiment (ve smyslu vláda) | velitele | Odlišit od `pluk`: *im Regiment ziehen*, *gůtes Regiment*, *Kriegs Regiment*. |
