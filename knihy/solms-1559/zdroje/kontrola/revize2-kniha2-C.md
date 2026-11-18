# 2. revize – Druhá kniha, dávka C (024r … 038r)

Rozsah: 25 stran (skeny 139–163): konec výkladu o ústupu a obléhání (024r), dřevořezy polního maršálka (024v)
a nejvyššího zbrojmistra (027v), úřad polního maršálka a podmaršálka (025r–027r), úřad nejvyššího zbrojmistra
(028r–029v), nejvyššího poručíka (031r–031v), plukovníka nade všemi profousy (031v–032v), nejvyššího proviantního
pána (032v–036r) a začátek Řádu komisu s výpočty chleba (036r–038r). Sousedé 023v a 038v jen čteny; navázání vět
přes hranice stran (023v→024r, 038r→038v) sedí.

Plynulost „středně“ podle `ZADANI_REVIZE2.md`: dlouhá souvětí dělena na věty uvnitř bloků, struktura bloků, `sken`,
`id`, `stav: zkontrolovano` a `overeno_clovekem: false` beze změny. Všechny přechody `pokracovani: true`
(024r, 026v, 027r, 029r, 031v, 034v, 035r, 035v, 036r, 036v, 037r) znovu sladěny s místem zlomu v originálu.

Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 024r … 038r --prisne` → **25 stran, 0 chyb, 0 varování**.

## Opravy `de` podle skenů

| strana | bylo | tisk (sken) | pozn. |
|---|---|---|---|
| 026v | jre lastierung thun | **thůn** | |
| 029r | Bickel vnd Axten | **Axsen** | sken 149 |
| 034v | gleich vnd vnpartheiß vnd klag | **gleich on vnpartheiß vnd klag** | přesmyčka tisku, nová pozn. 1 |
| 034v | ein eigen Prouiantmeister | **einn eigen** (*eiñ*) | podle konvence knihy |

Ověřeno beze změny (skeny 139, 141, 144, 147, 149, 151, 153, 156, 161; OCR u 162): *kundthafftigen nachtheil*,
*thůts* (024r); dvojitá virgule *nach //*, *Kriegsmanner* (025r); *von jnen lassen*, *bescheidigung*, *enttrint*
(028r); *butzen*, *streimaß*, *schurtzer* (029r); *biß zů den Finden* (031r, tisková chyba, nová pozn. 2);
iniciála *FVr* → *FUr* (032r); *das holt* (034v); *fünff vnd zwentzig hundert Brot* s rukopisnou opravou „35“
na okraji (037r); *drei metzen* (037v, OCR). Výpočty na 037r–038r přepočítány (90 chlebů z achtelu, 8 měřic na
achtel): sedí kromě dvou již poznamenaných tiskových chyb (2500 místo 3500; 1066 místo 1666 achtelů).

## Hlavní změny překladu po stranách

- **024r** – rozdělena souvětí; *gegen Leger* → „protiležením {gegen Leger}“; *obersten Hauptman* = „nejvyššího
  hejtmana {obersten Hauptman}“ (dříve „vrchního hejtmana {Hauptman}“); „že je … vyhladoví“ → „že obránce …
  vyhladoví“; formule předání korouhve plynuleji. Poznámka o *Memorial* zkrácena.
- **025r** – doplněno {Oberster} u „plukovníkem nad předvojovou korouhví“; „vystrojených“ → „vyzbrojených“;
  „na výšině nad ležením“ → „stát nad ležením“; věty rozděleny.
- **025v** – „znalci vojenství“ → „znalci válečnictví {Kriegsuerstendigen}“; *Wacht vnd Quartier meister* =
  „vachmistr a kvartýrmistr {Wacht vnd Quartier meister}“ (dříve „vachmistr {Wacht}“); „místo poplachu“ →
  „poplachové shromaždiště“; **opraven význam** *mehr leut dann dem Obersten* („více lidí než plukovníkovi“,
  dříve „a to plukovníka“), nová pozn. 1; *zů seiner notturfft* = „pro svou potřebu“ (dříve „nad svou potřebu“).
- **026r** – *Mustermeister* = „přehlídkový mistr“ (dříve „přehlídkový komisař“, odporovalo glosáři);
  *Quartier vnd Wachtmeister* s {…}; *Zetel* = „písemné soupisy“; „měřicí“ → „měřidlo“ (kolize s měřicí = *Metzen*);
  vypuštěny pozn. o *Compaßbriff* a *Mustermeister* (opakovaly glosář), zůstala pozn. o *Wahtmeister*.
- **026v** – odstraněn pracovní artefakt „na bílém praporu -> na bílé korouhvi“; *Artlereimeister* = „zbrojmistr“
  (glosář, dříve „mistr dělostřelectva“); *Justitie* = „justici {Justitie}“ (dříve „soudní moc“); *stat, ampt vnd
  Regiment* = „postavení, úřad i velení“ (odstraněn chybný odkaz {Regiment} → pluk, {Regiment} nyní u „plukem
  knechtů“); *von Reichs wegen* = „jménem Říše“; dlouhý blok rozdělen na 9 vět.
- **027r** – „který jezdce … bere do vazby“ (nejasný podmět) → „Profous bere jezdce …“; *Trosser buben* =
  „trénní pacholci“; „nevyvolali útěk“ → „nedali se na útěk“; pozn. o *Meutzkopff* zkrácena na výklad
  *für sich hudeln* (zbytek je v glosáři).
- **028r** – „Zbrojmistři požadují, že každé městečko … má válečný pán vykoupit“ → „žádají, aby u každého městečka
  … válečný pán od nich vykoupil“; *Regierer* = „dozorce šancířů“; *raumen* = „upravovat“ (dříve navíc „hloubili
  šance“); *preiß gemacht* = „dán v plen“ (dříve „vydán napospas“), pozn. 3 nově vysvětluje psanectví místo odkazu
  na glosář; zkráceny pozn. 1, 2, 4.
- **028v** – *doppel, einfach, halb hacken* → {hacken} u celého výčtu; „znalci vojenství“ → „znalci válečnictví“;
  „vyplatí se to levně“ → „je to přesto laciné“; ostřelování rozděleno na 3 věty.
- **029r** – „ti v posádce … v jedné významné posádce“ → „obránci … v jedné významné pevnosti“; *Stück innror* =
  „vývrt se rozdírá“; zkráceny pozn. 1–3 (*butzen*, *streimaß*, *schurtzer* mají hesla v glosáři).
- **029v** – „znalci válečnictví {Kriegsuerstendigen}“, doplněno {Oberst}; *durch sich selbst oder andere* =
  „sami nebo prostřednictvím jiných“; „přehlédnout při přehlídce“ → „sám přehlédnout {mustern}“.
- **031r** – {obersten Leutenants} v nadpisu (odkaz na heslo *nejvyšší poručík*); „pobít doprovod proviantu“ →
  „přepadnout dopravu proviantu“; nová pozn. 2 (*Finden*).
- **031v** – nadpis *Volget der Oberst vber alle Prouosen* = „Následuje plukovník {Oberst} nade všemi profousy“
  (rozhodnutí autora: *Oberst* = plukovník; dříve „nejvyšší nad všemi profousy“); *Justitien* = „justici“;
  vypuštěna pozn. o *Pollicei* (glosář `verejny-rad`).
- **032r–032v** – osm článků profouse plynuleji; *Henckern* = „katům“ ponecháno; 10. článek rozdělen na 6 vět.
- **034r** – anakolutický úvod rozdělen na samostatné věty; „Takový pán [pověřený proviantem]“ → „Tito pověřenci“;
  odstraněn chybný odkaz {kundtschafft} (zde „svědci“, ne zvěd); *die zwei vnnd vier pfundt behalten* =
  „dvou- a čtyřliberní chleby uschovat“ (viz sporná místa).
- **034v** – blok rozdělen na 16 vět; „ustavit nad tím pekaře“ → „určit k tomu pekaře“; „nikoli z komisu“
  zřetelně vztaženo k pekařům; nové pozn. 1 (*on vnpartheiß*) a 2 (*das holt*).
- **035r–035v** – „vyvolá nevrlost v houfu“ → „nevoli“; „tak si jej pán udrží“ (nejasné *jej*) → „udrží vojáky“;
  „jízdní hlídkový houf“ → „hlídkující houf“ (*jízdní* nebylo v textu); „pán války“ → „válečný pán“; *jhre … Wapen*
  = „jejich erby“ (dříve „své erby“), pozn. 2 upravena; *verehrung* u úplatků profousů bez {…} (heslo *čestný dar*
  zde nesedí).
- **036r** – *Justitie* = „spravedlnost {Justitie}“ (navazuje na 035v); „pro Dunaj“ → „po Dunaji“; úvod Řádu
  komisu rozdělen na věty; doplněna tečka v nadpisu „Řád komisu.“
- **036v** – „rozdělit proviantmistry na sto tisíc mužů“ → „rozvrhnout, kolik proviantmistrů má být na sto tisíc
  mužů“; *Lermen* zde = „rozruch“ (ne poplach); 1. osoba autora zachována.
- **037r–038r** – výpočty sjednoceny („na žitě to činí“, „váhou“), trojčlenka s {Regel De Tri}; vypuštěny pozn.
  o *Achtel* a *Metzen* (opakovaly glosář), zbylé poznámky přečíslovány; *mit dem namen verwandelt* = „liší se i
  názvem“, *nicht vnderschiedtlich* = „bez rozdílu“ (dříve „nikoli odlišně“).
- **024v, 027v** – popisy dřevořezů zkontrolovány, beze změny.

## Sporná místa k rozhodnutí

1. **025v** *dem Feldmarschalck mehr leut / dann dem Obersten vber die Knecht / oder andere sampt dem Zeugmeister
   zů ordenen* – CS: „přidělit polnímu maršálkovi více lidí než plukovníkovi nad knechty nebo jiným spolu se
   zbrojmistrem“. Důvod: *dann* = „než“ (dativ), možné je i „přidělit mu navíc plukovníka…“ (pozn. 1).
2. **034r** *So das brot also auff das gewicht gebacken wirdt / die zwei vnnd vier pfundt behalten* – CS: „mají se ty
   dvou- a čtyřliberní chleby uschovat“ (jako vzorky). Alternativa: „a udrží si váhu dvou a čtyř liber“.
3. **028r** *von jnen lassen* (ověřeno ve skenu) – překládáno „vykoupit“ podle *lösen* v posledním odstavci a na
   28v; alternativa „jim ponechat“ (pozn. 4).
4. **034v** *wann mann das holt* – „kdy se [chléb] odváží“; alternativa *holtz* = dřevo na pečení (pozn. 2).
5. **035v** *darinn jhre / oder hohen Graden Wapen* – „jejich erby“ (tamních pánů) vs. „jeho erby“ (válečného pána).
6. **031v** nadpis *der Oberst vber alle Prouosen* – nyní „plukovník nade všemi profousy“ podle rozhodnutí
   *Oberst = plukovník*; věcně jde o nejvyššího profouse (srov. *Oberster Feldprofoß*). Ponecháno podle zadání.

## Návrhy do glosáře

- `kundtschafft` (význam „svědectví, přítomnost svědků“, 034r) – heslo `zved` má *kundschafft* v `de`; navrhuji
  z `zved` *kundschafft* vyřadit nebo v `pozn` uvést, že *Kundschaft* znamená také „zprávy, výzvědy“ a „svědectví“.
- id `trojclenka`, cs: trojčlenka, de: [Regel De Tri, Regel de Tri], kategorie: miry, pozn: Dobové pravidlo tří
  (*regula de tri*) k přepočtu dávek chleba a měr.
- id `rozruch`, cs: rozruch, de: [Lermen] – jen jako poznámka k heslu `poplach`: *Lermen* u Solmse někdy znamená
  „tumult, rozruch“ (036v), ne vyhlášený poplach.
- `cestny-dar` (*verehrung*): doplnit do `pozn`, že v souvislosti s profousy a markytány (035v) jde o úplatek.
- `dozorce` (*Regierer*): heslo vyhovuje; `hejtman` – zvážit složeninu *oberster Hauptman* = „nejvyšší hejtman“ (024r).
