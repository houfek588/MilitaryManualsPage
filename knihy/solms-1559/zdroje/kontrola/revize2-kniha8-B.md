# 2. revize – Solms 1559, dávka 8-B (konec Osmé knihy, skeny 600–616)

Datum: 2026-11-19. Zadání: `zdroje/ZADANI_REVIZE2.md` (vč. oddílu o knihách 6–9), zpráva překladatele `kontrola/preklad-8-B.md`.
Rozsah: **8-006v … 8-014v** (17 stran). Sousedy 8-006r a 9-erb-solms jsem jen četl.
Všechny strany mají `stav: zkontrolovano` a `overeno_clovekem: false`.
`python -I nastroje/over_strany.py knihy/solms-1559 8-006v … 8-014v --prisne` → **17 stran, 0 chyb, 0 varování**.

Všech 17 stran jsem porovnal se skeny BSB (IIIF, šířka 1600 px, uloženy ve scratchpadu `r8b/`). Přepis `de` byl
velmi čistý, opravil jsem jen jedno místo. Těžiště revize bylo v plynulosti, ve vazbách a v návaznosti přes hranice stran.

## Hlavní změny po stranách

- **8-006v, 8-007r, 8-007v** – spojku tabulek jsem sjednotil s Druhou knihou (039v–040v): „Nebo lze vzít:“ → „nebo lze vzít:“.
  Všechna čísla v tabulkách odpovídají skenu. Součty jsem přepočítal podle vah (vůl 300, kráva 150, tele 36, skopec 30,
  ovce 20 liber) a všechny poznámky o tiskových chybách sedí.
- **8-007v** – poznámka 2 tvrdila, že Druhá kniha „také čte spojení ‚a‘“. Ve skutečnosti má Druhá kniha (040v)
  „fünff Kälber sechs Schaaff“ **bez** „oder“, kdežto tisk 8. knihy má „oder“. Opraveno takto: „… nikoli jedno nebo druhé. Druhá kniha má na tomto
  místě ‚fünff Kälber sechs Schaaff‘ bez ‚oder‘, tedy pět telat a šest ovcí.“
- **8-008r, 8-008v** (výpočty ovsa) – ve 13 + 2 výpočtech jsem zrušil řetězení s dvojím „a“: „to činí na váhu 84 centů a 58 korců a 4 měřice“ →
  „to činí na váhu 84 centů, což je 58 korců a 4 měřice“ (stejně jako v revidovaném 041v). Výpočty jsem ověřil (korec = 12 měřic, měřice = 12 liber).
- **8-008v** – „když se před vařením zase čistě vypere“ (o mase) → „když se před vařením znovu důkladně omyje“, dále drobná úprava interpunkce.
- **8-009r** – v *durch gifft / forcht / lieb / gunst oder haß* znamená *gifft* „dar, úplatek“, ne „jed“ (ustálená přísežná formule):
  „ať jedem, strachem, láskou…“ → „Nemám ji ani pro dary[^1], strach, lásku, přízeň či nenávist … dopustit do rukou žádného jiného pána“. K tomu nová poznámka.
  Dále „nechal si ji ve všem, jak se sluší, svěřenu“ → „ve všem, jak se sluší, ji měl ve své péči“, „svolat válečný lid, který má“ →
  „svolat všechen svůj válečný lid“ a „vyžaduje má velká potřeba“ → „vyžaduje naléhavá potřeba“.
- **8-009v** – nadpis „Obsah řádu, který je v posádce potřebný nejprve“ → „Obsah řádu, který je pro posádku nejprve zapotřebí“.
  Shoda: „je každému obrannému místu přidělena … děla“ → „jsou … přidělena … děla“. Dále „až budeme v díle“ (*im werck*) → „až dojde na věc“,
  „nezamýšlí“ (*nit gemůt*) → „nemíní“. Z *Regiment* = „řízení“ jsem odstranil `{Regiment}`, protože vedl na heslo `pluk` (viz sporná místa).
- **8-010r** – plukovníkova řeč začínající „Když jste tedy svolili…“ neměla uzavírací uvozovku. Uzavřel jsem ji na konci odstavce
  („… je všechno naše počínání marné.““), protože další články jsou ve 3. osobě. Další úpravy: „kolik je podle potřeby zapotřebí“ → „kolik je potřeba“,
  „(a nade vše bez Boha)“ → „(a především bez Boha)“ (*vnd Gott beuor*), „že toho máme podle výpočtu dobře dost“ → „takže toho podle výpočtu máme dostatek“.
- **8-010v** – „Proto má být tento článek trestán jako nejpřednější a první“ → „Proto má být rouhání prvním a nejpřednějším článkem, který se trestá“
  (*soll solches der fürnemblichst vnd erst Artickel sein zu straffen*). „Jak velkou zásobou se disponuje“ → „jakou zásobou je [posádka] opatřena“.
  „Má se mít i více takových kuchařů“ → „mají se mít i další polní kuchaři {Garköch}“. „Vydávají jídlo“ → „prodávají jídlo“ (*vmb den pfenning*).
  „Aby se držel jeho řádu {Regiment}“ → „aby se podřizoval jeho řízení“.
- **8-011r** – „aby zůstal ve svém pořádku“ (podmět nejasný) → „… a udržet svůj řád“ (podmětem je plukovník). Z věty o chlebu jsem vypustil přidané „i“
  a z „celý rozpočet“ přidané „celý“.
- **8-011v** – popis dřevořezu jsem ověřil proti obrázku (figury 20–25, číslice zrcadlově obrácené). Opraven tvar „se zápalnou slože“ → „složí“.
- **8-012r** – chybně pochopený podmět: *was nit auff den Letzen ist mit vmbfürn* jsou **lidé**, kteří nejsou na stanovištích, ne věci:
  „Co není na stanovištích, má s sebou vodit po obchůzce“ → „Ty, kdo nejsou na stanovištích {Letzen}, má brát s sebou na obchůzku“.
  „K tomu slouží slepé příkopy s ohněm…“ → „– například slepými příkopy s ohněm…“ (*als mit*). U nebozezu „jím“ → „skrz něj“.
  Z poznámky 2 jsem odstranil redakční zmínku o glosáři (patří do zprávy). Poznámka 3: „v tažení Karla V.“ → „(patrně ve vojsku Karla V.)“.
- **8-012v** – přes hranici stran se zdvojovalo slovo „kolíky“ („aby kolíky, až se do nich | kolíky zatlučou, vyšly…“). Opraveno na
  „zatlučou, vycházely křížem…“, `{Pfel}` jsem přesunul k dalšímu výskytu. Dále „jako dělají tesaři své kolíky“ → „jaké dělají tesaři na svých stahovacích kolících {Zugnägel}“
  a „dřevo podobné páčidlu na hřebíky {Nageleisen}“ → „dřevěný průbojník podobný vyrážeči hřebíků {Nageleisen}“.
- **8-013r / 8-013v** – zmínka o figurách 22 a 25 (*wie dise zwo Figurn eine mit 22. die ander mit 25. verzeichnet /* je v tisku na 613) byla v `cs`
  přesunutá na 8-013v. Vrátil jsem ji na 8-013r, takže zlom věty teď odpovídá tisku: „… jak tato dvě vyobrazení – jedno označené číslem 22, druhé číslem 25 –“ |
  „ukazují a vykládají: jak mají být soudky…“. Dále na 8-013r „pod dohledem“ → „bezpečně uložit“ (*verwart*) a „dokud v tom místě není celá jeho masa“ → „dokud tam není velké množství [nepřátel]“.
  Na 8-013v: „mají volné všechny strany, aby jimi bily ven“ → „mohou volně bít na všechny strany“, „nařízne se řečené cípy“ → „nařížnou se … cípy“ a „hrdlo …, kterým prochází“ → „jímž prochází“.
- **8-014r** – „ta kouli mocně roztrhne a ta bije“ → „… a bije kolem sebe do houfu“, „prach má volno“ → „prach má volný průchod“ (*hat das puluer lofft*).
- **8-014v** – beze změn textu (ověřeno ve skenu).

## Ověřená místa ze skenů
- 600–602: všechna čísla v tabulkách masa, „schlchachten“ (tisk, 600), „1315 Kälber“, „oder 3 Hämel 5 schaaff / od|der“ (602).
- 603: nadpis *Nůn volgt die Füterung …* je v tisku vysázen jako nadpis (úr. 3 sedí), iniciála **ES**, „gennt“.
- 604: závěrečný odstavec *Dise gemelte Ordnung …* je vysázen na střed jako závěr oddílu (blok `odstavec` je v pořádku).
- 605–606: „vorm eingang vnd verflichtung“, „befastung“, „mit den Harn“, „Beschatzung“ (tisk), iniciála **ERstlich**, slovo *Pul-|uer* přesunuto celé na 607 – správně.
- 607: tisk má i zde „Schauffelu“ (převrácené *n*) – v `de` je *Schauffeln*, jako na 609. Dvakrát „Zum fünfften“ – tisk.
- 609: „Befestuug“, „gůng“ – tisk; poslední slovo *thůn* je kustod a zároveň první slovo 611 (věta přechází přes obrazovou stranu 610).
- 613: tisk začíná malým **„helfft“** (pokračování věty z 612). V `de` bylo „Helfft“, **opraveno**. „Trachteten“, „lufft“, „Kalcktonnen“ – tisk.
- 614: „mit zweien Rören“ (tisk), „der Schuor“ (převrácené *n*, v `de` je *Schnor*).
- 615: „lettern Eimer“ (= lederne), „Fütternng“ (tisk, v `de` je *Fütterung*), „dön vō Zeug“.
- 616: „Ende des achten Bůchs.“ – shoda.

## Sporná místa k rozhodnutí
1. **Regiment = řízení/řád** (8-009v *einer Ordnung vnd Regiment*, *ein Regiment vnd Ordnung*; 8-010v *vnder seinem Regiment*): `{Regiment}` jsem
   odstranil, protože odkazoval na heslo `pluk`. Ke zvážení je samostatné heslo „řízení, řád (Regiment)“, nebo poznámka v hesle `pluk`.
2. **Creutzhaspel / Creutzhespel** (8-011v, 8-012r, 8-012v): glosářové heslo `navijak` obsahuje tvar *creutz Hespel*. Zde jde o křížového ježka.
   Doporučuji samostatné heslo (viz návrhy). V textu zůstává „křížový ježek {Creutzhespeln}“.
3. **Garkoch = „polní kuchař“** (glosář) v posádce města – ponecháno podle glosáře. Ke zvážení je „výdejní kuchař / kuchař pro mužstvo“.
   Glosář nemá tvary *Garköch*, *Garköchen* (8-010v, 8-011r).
4. **Spojka v tabulkách 8-006r** (dávka 8-A): na 8-006r je *Oder mag nemen.* v 1. řádku a `cs` „nebo lze vzít“ bez dvojtečky, v 8-B (podle tisku i Druhé knihy) je
   v prostředním řádku „nebo lze vzít:“. 8-006r jsem needitoval. Doporučuji sjednotit při revizi 8-A podle skenu 599.
5. **8-014r, odkaz na vyobrazení vrhacího stroje**, které v knize chybí. Poznámku překladatele jsem ponechal.
6. **gifft** (8-009r) vykládám jako „dar, úplatek“ (formule *Miet und Gaben*). Kdyby autor projektu preferoval doslovné „jed“, stačí vrátit původní znění.

## Návrhy do glosáře
Návrhy překladatele (`preklad-8-B.md`) podporuji beze změn (`krizovy-jezek`, `kolovy-tram`, `zataras`, `vlneny-pytel`, `pricna-zed`,
`slepy-prikop`, `parkan`, `trhaci-soudek`, `trhaci-koule`, `zlab`, `mistr-delostrelectva`, `prachovy-mlyn`, `zentourovy-mlyn`, `palec`, `metadlo`) a doplňuji:

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| polni-kuchar (doplnit tvary) | polní kuchař | Garköch, Garköchen | zold | plurálové tvary z 8-010v a 8-011r |
| rizeni | řízení, řád | Regiment (ve významu vláda, správa) | sluzba | odlišit od `pluk`; 8-009v, 8-010v |
| smolny-venec | smolný věnec | Bechring | delostrelectvo | plátěné „klobásy“ s pomalým prachem, stočené a namočené v síře a pryskyřici; házely se na útočníky (8-013v) |
| kozene-vedro | kožené vědro | lettern Eimer, Eimer | opevneni | hasičské vědro v posádce (8-014r) |
| navijak (úprava) | naviják | vyjmout *creutz Hespel* | delostrelectvo | kolize s křížovým ježkem |
