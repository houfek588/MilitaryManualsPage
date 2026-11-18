# 2. revize – První kniha, dávka D (1-031r … 1-039v)

Rozsah: 18 stran (skeny 71–88), konec První knihy: závěr výkladu o válečné správě, „Odpověď na žádost
vojáků“, rozmluva Starého otce se Synem a instrukce pro mladíka. Soused před dávkou `1-030v` jen čten
(navazující věta „…který předtím, jak bylo řečeno, nebyl / válečným lidem“ sedí).
Plynulost „středně“ podle `ZADANI_REVIZE2.md`: souvětí řetězená přes `/ so / vnd / dann` dělena na věty
v rámci bloků, struktura bloků, `sken`, `id` a `overeno_clovekem: false` beze změny; všechny přechody
`pokracovani: true` (031r, 031v, 032r, 032v, 033r, 035v, 036v, 038v, 039v) dál sedí s originálem.
Všech 18 skenů staženo z BSB IIIF a porovnáno s `de` řádek po řádku.

Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 1-031r … 1-039v --prisne` → **0 chyb, 0 varování**.

## Opravy `de` podle skenů (dobový pravopis tisku)

| strana | bylo | tisk (sken) | pozn. |
|---|---|---|---|
| 1-032v | Beuelchsleut | **Beuelchßleut** | |
| 1-032v | gesetzten Obrigkeit | **gesatzten** | |
| 1-033r | willig vnnd erbittig | **vrbittig** | dobová podoba *erbietig* |
| 1-033v | auff der Musterung | **Musterug** | tisková chyba, nová pozn. 1 |
| 1-033v | angehört | **angehort** | |
| 1-035r | freundtschafft / gehört | **freundschafft / gehort** | |
| 1-035r | es ist mir leit | **mit leit** | tisková chyba za *mir*, nová pozn. 3 |
| 1-035v | gehört hab / zu widerrathen | **gehort / zu wider rathen** | |
| 1-036r | jrs versteht | **verstehe** | nová pozn. 1 |
| 1-036v | tüglich | **tüglch** | tisková chyba, doplněno do pozn. 1 |
| 1-037r | sachen vnd handel / anrüsten | **händel / anrösten** | nová pozn. 1 (*anrösten* = *anrüsten*) |
| 1-037v | Beuelchsleut / solltest | **Beuelchßleut / soltest** | |
| 1-038r | leren kan (2. výskyt lernen) / gehört | **leren / gehort** | |
| 1-038v | sichst / besichst | **sichts / besichts** | přesmyčky tisku, pozn. 1 rozšířena |
| 1-039r | Gottsförchtig / Gottslesterer / rüsten | **Gottßförchtig / Gottßlesterer / rösten** | nová pozn. 2 |
| 1-039v | ein grossen behalt | **einen** (*eiñ*) | |

Ověřeno beze změny: rukopisný vpisek *wider)* nad záhlavím 031r (pozn. 1), *Lantßuolck* (031r),
*nich anderst* (031v), *gehorsan* (032r), *leichfertiger* (032v), *grauch*, *Kriegßuerstenden* (033r),
*sitter der zeit* (035r), *auffrichtigst* (036r), *wirts / kömpts* (036v), *nichs* (037v), *dirtte*,
*Fundierungen*, *kompts / sichts* (038r), kustoda *stellen.* na 039r (039v správně začíná *stellen. Er soll…*
v témže odstavci), iniciály *ITem* (033v), *LIeber* (035r), *VOr* (039r). Úrovně nadpisů ponechány
(v 1. knize jsou oddílové nadpisy jednotně `uroven: 2`, repliky Son./Alter Vatter. `uroven: 3`).

## Hlavní změny překladu po stranách

- **1-031r** – rozdělena dlouhá souvětí; přesnější „pole po nich zůstane obnažené“ (*wirt ein Feld von jnen
  entblöst*), „země zůstávají zalidněné“ (*bleiben die land besetzt*, dříve „obsazeny“). Blok 6 přestavěn:
  „Svůj zemský lid ať šetří k tomu, aby dodával peníze a proviant a doprovázel je…“. Poznámka zkrácena.
- **1-031v** – „ti nejsou míněni v tom, že by pán neměl…“ → „Na ty se nevztahuje, co bylo řečeno o tom, že pán
  nemá používat svůj zemský lid; tím je míněn obecný válečný lid…“; „věšet na krk“ → „přidělovat“;
  poslední blok (*Dieweil dann von der Kriegßordnung…*) přeložen srozumitelně. Pozn. 1 zjednodušena.
- **1-032r** – rozpletena věta navazující z 031v („chceme-li ovšem zase / válčit tak… K tomu se válečných věcí
  musejí znovu ujmout čestní a rozumní vojáci…“); *Kriegßuerstendigen* → „znalců válečnictví“ podle glosáře
  (`znalec-valecnictvi`) s `{…}`; *ist das Kriegßuolck… damit gefangen* → „je tím sám od sebe [ke kázni] zavázán“.
- **1-032v** – *Gott gebe was Nation es seien* chybně „dej Bůh, ať jsou z jakéhokoli národa“ → „ať jde o kterýkoli
  národ“; `{Regiment}` u významu „řád, zřízení“ odstraněn (odkazoval by na heslo *pluk*), místo něj pozn. 2;
  `{hauffen}` u *zum hauffen gebracht* odstraněn („k vojsku“, heslo *šik* nesedí); blok 3 jako předpoklad
  („Dejme tomu, že by služební list…“), na nějž odpovídá blok 4.
- **1-033r** – rozdělena věta s podmínkou vojáků („Avšak s podmínkou, že…“), *gleich allen Nationen* = „stejně pro
  všechny národy“, *billichkeit* = „slušnost“; *Kriegßuerstenden* → „znalci válečnictví“.
- **1-033v** – „dobrou spravedlivou mírou a rozvahou“ → „slušným a spravedlivým postupem a s rozvahou“;
  odpověď komisařů rozdělena na věty, „vezme na přetřes“ → „projedná“.
- **1-034r** – závěrečný odstavec výkladu rozdělen na 7 vět, zachována 1. osoba autora („Nechci však…“,
  „Chci jen věrně podat zprávu…“).
- **1-034v** – popis dřevořezu přepsán podle skenu: dřívější popis (stařec „pozdviženou levou rukou poučuje“,
  mladík „ruku na starcově rameni“, „úzké nohavice“) neodpovídal; nově oděv, baret s pery, nabírané
  a prostřihované rukávy a kalhoty, krátké meče, spára mezi dvěma štočky.
- **1-035r** – rozmluva zpřirozena („Mohu-li vám to nějak oplatit…“, „co ti nepřístálo“); nová pozn. 3
  (*mit leit*) a 4 (*zu forderen*).
- **1-035v** – „cizí tovaryši“ → „cizí mládenci“, „dobří jinoši“ → „dobří mládenci“; rada Starého otce
  rozdělena na věty.
- **1-036r** – „nešel bych na pouhou soukromou výpravu či prostou sběř“ → „nešel bych na výpravu jednoho muže
  ani do nahodilého srocení“; „válečná akce“ (anachronismus) → „nějaká válka“; *frei* = „otevřeně“.
- **1-036v** – řeč k pánovi rozčleněna na věty; „pouhým řadovým… jako obyčejný člověk“ → „prostým vojákem…
  jako prostý voják“ (*ein gemeiner*).
- **1-037r** – vyprávění Syna rozděleno; nepřímá řeč pána („Mám si prý rozmyslet…“); pořadí poznámek
  srovnáno s textem.
- **1-037v** – `{hauffen}` u *gemeinen hauffen* („obecný houf“ = dav, chátra) odstraněn; *dich leiden vnd
  züchtigen müssen* = „snášet strádání i tresty“.
- **1-038r** – „má první srážku s nepřáteli“ → „jako první naráží na nepřítele“; doplněno `{Scharmützel}`
  a `{Ordnung}` (šik); *der erst… auß dem Leger vnd der letst darinn* → „musí z ležení vytáhnout první
  a zůstat v něm poslední“; pozn. 1 (*Fundierungen*) upřesněna.
- **1-038v, 1-039r, 1-039v** – rozdělení vět, přirozenější slovosled; v 039r rouhač jako jasný podmět
  („rouhač není o nic moudřejší…“), závěrečná řečnická otázka samostatně.

## Sporná místa k rozhodnutí

1. **1-031r, *das ist einem Herren zurathen*** – v tisku chybí zápor; překlad „[nelze] radit“ podle smyslu
   a dobového vpisku *wider)*. Ponecháno s poznámkou.
2. **1-035r, *als zu dem da ich zu forderen vnnd gůt vnderweisung vnd Rath bei gefunden hab*** – čteno jako
   *Förderung* („podporu, dobré poučení a radu“); alternativa *zuvorderst* („především“). Pozn. 4.
3. **1-038r, *Fundierungen*** – nejasné; přeloženo „průzkumy“ (pozn. 1 uvádí *Futerungen* / *Kundierungen*).
4. **1-038r, *er můß der erst wann mann zeucht auß dem Leger / vnd der letst darinn sein*** – vyloženo „musí
   z ležení vytáhnout první a zůstat v něm poslední“; možné i „poslední, kdo do něj vstoupí“.
5. **1-037v, *das wart bei disem*** – přeloženo „a toho se pak drž“ (*warten* = věnovat se, setrvat).
6. **1-032v / 1-033v / 1-036v, *Oberster / Obersten*** – kde jde o vrchního velitele celého vojska, ponecháno
   „nejvyšší velitel {Oberster}“ (glosář odkazuje na *plukovník*); v 033v *die Obersten von allen Regimenten*
   = „plukovníci“; v 038r/038v *Obersten* = *Kriegs Oberster* = „nejvyšší polní hejtman“ (glosář má
   *Kriegs Oberster* u hesla `nejvyssi-polni-hejtman`).

## Návrhy do glosáře

| id | cs | de | kategorie | pozn. |
|---|---|---|---|---|
| `valecny-lid` (doplnit) / nové `vojak` | voják (válečník) | Kriegßleut, Kriegßleuten, Kriegsleut | velitele / jednotky | *Kriegßleut* je v 1. knize překládáno střídavě „vojáci“ (tato dávka) a „válečníci“ (starší dávky), heslo `valecny-lid` má cs „válečný lid“. Doporučuji samostatné heslo s jednotnou volbou (návrh: „vojáci“). |
| `soud` (doplnit pozn.) | spravedlnost / justice | Justitien | pravo | *Justitien* je v knize „spravedlnost“ i „justice“, nikdy „soud“; heslo `soud` s cs „soud“ nesedí. Návrh: samostatné heslo `justice` (cs „spravedlnost, justice“). |
| `valecna-sprava` | válečná správa | Kriegßregirung, Kriegßregierung, Kriegsregierung, Kriegßregierungen | sluzba | častý pojem 1. knihy, v glosáři chybí. |
| `znalec-valecnictvi` (doplnit de) | znalec válečnictví | Kriegßuerstendigen, Kriegßuerstenden | osoby | doplnit tvary z 032r a 033r. |
| `verejny-rad` (doplnit de) | veřejný řád | Polliceien | – | tvar z 038r. |
| `sik` (pozn.) | – | hauffen | – | upozornit, že *gemeiner hauffen* / *zum hauffen bringen* znamená dav, resp. vojsko, nikoli šik. |
| `pluk` (pozn.) | – | Regiment | – | *Regiment* v 1. knize často = „řád, zřízení, vláda“ (1-032v), nikoli pluk. |
