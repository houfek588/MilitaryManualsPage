# 2. revize – dávka „predsadka“ (`titul`, `citaty`, `predmluva-01`–`predmluva-14`)

Skeny 3–18 nově staženy z e-rara IIIF (`2050511 + sken`) a porovnány s `de`; sporná slova ověřena na výřezech
v plném rozlišení. Kontext: `001` (jen čteno). Všechny strany `stav: zkontrolovano`, `overeno_clovekem: false`.
`python -I nastroje/over_strany.py knihy/bern-1615 titul citaty predmluva-01 … predmluva-14 --prisne` → **16 stran, 0 chyb, 0 varování**.

## 1. Opravy originálu (`de`) podle skenu

| Strana | Před → po | Pozn. |
|---|---|---|
| `titul` | `Landschafft` → `Landtschafft` | tisk |
| `citaty` | `Duo` → `DVo` | iniciála podle pravidel § 2 |
| `predmluva-01` | `Wir` → `WIR` | iniciála |
| `predmluva-02` | `ir wesen` → `jr wesen`, `ihres Standts` → `jhres Standts` | tisk |
| `predmluva-03` | `ihre Indisposition` → `jhre Indisposition` | tisk |
| `predmluva-04` | `ihrer hochen` → `jhrer hochen`, `ihre Lendern` → `jhre Lendern` | tisk |
| `predmluva-06` | `fürsehen` → `fürsechen`, `fertigen` → `fehrtigen` (tisk `fehꝛ-|tigen`), `erkennet/ vnnd` → `erkennet: vnnd` | 1. revize tisk „normalizovala“ |
| `predmluva-12` | `besehen` → `besechen` (tisk `besechē`), `am 26. cap.` → `am 26 cap.` | tisk |
| `predmluva-14` | **`Zugenden` → `Tugenden`** | tisk má jasně `Tugenden` (výřez skenu 18), „tisková chyba“ z 1. revize neexistuje – poznámka zrušena. **`SPORNA_MISTA.md` (odrážka `predmluva-14`) je tedy neplatná.** |

Ověřeno a ponecháno: `kunst/` na `predmluva-12` (tisk opravdu `kunst`, sazečská chyba za `gunst` – poznámka), `Monarchey`,
`Vigetius`, kustody `WIR`, `Vnder-`, `Solda-`, `Die`, `de exci-` (na skenu 17 je `de exci-` jen kustod, `de excidio` celé na sk. 18), `Das`.

## 2. Hlavní změny překladu po stranách

- **`titul`**: nadpis „…průvodce vojenským výcvikem a manévry“ → „Stručný přehled a návod k válečnému cvičení {Kriegs Exercitij} a výcviku“ (*Anleitung* = návod, *Vbung* ≠ manévry). Odstavec nyní věta s velkým písmenem: „Takto stručně sestavený k užitku a potřebě chvalitebné republiky Bern, jejích měst i venkova {Landtschafft}. A shodně s [řádem] osvíceného, vysoce urozeného knížete…, upravený a uspořádaný.“
- **`citaty`**: zpřesněny překlady – „Vojenská statečnost převyšuje…“ → „Vojenská zdatnost předčí…“ (jednotně *virtus* = zdatnost); „Nerozvážně si počínat v bitevním šiku… podobného šelmám“ → „Bezhlavě se vrhat do bitevního šiku a potýkat se s nepřítelem zblízka je cosi surového a podobného divé zvěři.“ Poznámky upozorňují, že citáty jsou volné/zkrácené (Polybios není doslovný; Pro Murena IX, 22; De off. I, 23, 81).
- **`predmluva-01`** (úřední řeč): „vzkazujeme všem a každému světskému [úředníku]“ → „vzkazujeme všem vůbec i každému zvlášť ze světského stavu“; „náš milostivý a příznivý pozdrav“ → „své milostivé a příznivé pozdravení“; „těm, kdo podléhají správě“ → „všem, kdo jsou poddáni správě naší vlády“. Úřady ponechány podle glosáře. Poznámky přepsány: 1 = šultys (dva střídající se šultysové; rychtáři poddanských měst Thun, Burgdorf), 2 = Malá a Velká rada, 3 = správa venkova (guvernér jen v Aigle/Älen, kasteláni ve Frutigenu a Simmentalu – vypuštěn chybný Saanen, který byl zemským fojtstvím; výslovně, že Freyweibel/Weibel nejsou vojenské hodnosti), nová 4 = *Hindersessen* (podsedci bez měšťanského práva).
- **`predmluva-02`**: „nejhlavnější základy“ → „nejpřednější základy, na nichž stojí…“; Římané: „kteří byli ze všech republik… tou nejhlavnější“ → „jejichž republika byla ze všech… ta nejpřednější“; konec „Proto tedy měli ve zvyku“ → „Proto se u nich také ujal tento zvyk:“ (navazuje „totiž že…“).
- **`predmluva-03`**: opraven smysl – *dieselben … verderben lassen* a *ihre Indisposition* se vztahují k disciplíně (fem.), ne k žaludku: „…aby [disciplínu] snad z nedbalosti a lehkomyslnosti, a protože by včas nepostřehli její nevolnost a nemoc, nenechali od základu zchátrat a docela zahynout“; *anordnungen* = zřízení.
- **`predmluva-04`**: „nebeských hvězd i zemí“ → „podle polohy a povahy podnebí[^1] i zemí“ + poznámka (*Himmelsgestirn*, nauka o podnebí a povaze vojáků, srov. Vegetius I, 2); věty rozděleny („vyžadovány? Z nich je třeba…“).
- **`predmluva-05`**: „učí toto poslední poučení … znakům“ → „poslední návod neboli nařízení učí pěti … znakům[^1]“ + poznámka k nejasným *Merckzeichen*; konec převeden na „…aby vládu, kterou jim svěřil Bůh Všemohoucí, mohli | s větším užitkem spravovat“.
- **`predmluva-06`**: „pečovat mohli“ → „spravovat“; „ušlechtilé“ → „úhledné válečné cvičení {Kriegsvbung}“; „tak k tomu, aby“ → „tak i v tom, že“ (správná vazba *als das sie … sich … befunden*).
- **`predmluva-07`**: věta převrácena podle smyslu: „…se vždy ukázali srdnatě a neohroženě ochotni odrazit ty, kdo by se odvážili potlačovat výkon jejich náboženství a svědomí“ (vypuštěno přidané „svobodného“; *verstossen* = odrazit, jednotně s `predmluva-08`); „[vyloží]“ → „[předvedou]“; „idea či zobrazení“ → „představa neboli vyobrazení“.
- **`predmluva-08`**: „vést zbraně řádně a se ctí“ → „řádně a vzhledně vládnout zbraněmi“ (*mit wolstand*); „Chceme tudíž“ → „Protož chceme“; „zapudit a pomoci potlačit“ → „pomoci odrazit a potlačit“; „v tom či onom“ → „tu či onde“.
- **`predmluva-09`**: viz sporné místo níže; „vysedávání doma v domech“ → „vysedávání doma“; *Item* → „Dále“; „četba takovýchto válečných spisů“ → „čtení o takových válečných věcech“.
- **`predmluva-10`**: opraven smysl *mit deß Feindes, so derselb anfallen wolte* → „s mocí nepřítele, který by ji chtěl napadnout“; *Gelegenheit … gewahr nemen* → „příležitosti … nepromarnila, nýbrž se jich … chopila“; „výše předložené důvody“ → „výše vznesené argumenty“.
- **`predmluva-11`**: „chována ve cti“ → „vážena“; „ti na ně vytáhli se zbraní v ruce a podrobili si je daněmi“ → „ti je ozbrojenou rukou přepadli a učinili poplatnými“; souvětí rozděleno.
- **`predmluva-12`**: přesunut odkaz na knihu („Král Uziáš (2. kniha Paralipomenon, 26. kapitola) měl…“ místo „měl ve 2. knize…“); poznámka k Sofér doplněna o znění Vulgáty (*Sopher principem exercitus, qui probabat tirones*), odkud „polní hejtman Sofér“; nová pozn. k Vegetiovi (tisk *Vigetius*); „správa věcí veřejných“ → „římské státní zřízení“.
- **`predmluva-13`**: „dbali na“ → „každý den věnovali výcviku…“; Theodorich: „Kde se válečnému umění předem neučí a necvičí, tam ve vážné chvíli a v nouzi chybí.“; „V úhrnu pak“ → „Zkrátka“. Poznámky ponechány (Platón, Seneca 18, 6, Cassiodorus Var. I, 40), upřesněny.
- **`predmluva-14`**: „nedosáhli náhodou, nýbrž skrze… ctnosti.[^2]“ → „nezískali štěstím, nýbrž svou skvělou válečnou disciplínou a ctnostmi“ (pozn. 2 zrušena, viz výše); „obecní zřízení“ → „státní zřízení“ (*Policey*); datace „Dáno v Bernu 12. dne měsíce srpna 1615.“; poznámka k Josephovi opravena na *Bellum Iudaicum* III, 5 dnešního číslování (ve starších vydáních kap. 6).

## 3. Sporná místa k rozhodnutí

| Strana | DE | CS | Rozhodnutí / důvod |
|---|---|---|---|
| `predmluva-09` | `wann man in einicher Person die Effecten verbringen/ vnd vollziehen sichet/ vnd hilffet` | „když člověk vlastní osobou[^1] vidí, jak se [válečné] činy provádějí a dovršují, a sám při tom pomáhá“ | **Rozhodnuto**: *einig* = sám, jediný (srov. *einig vnd allein* na `predmluva-08`), tedy „vlastní osobou, osobně“ (= *in eigner Person*); *Effecten* = skutečné válečné akce v protikladu k četbě. Dřívější „u někoho osobně“ neodpovídá kontextu (námitka praktiků proti knižnímu učení). Vysvětleno poznámkou. |
| `titul` | `Kurtzer Begriff vnd Anleitung Des Kriegs Exercitij vnd Vbung` | „Stručný přehled a návod k válečnému cvičení a výcviku“ | `kniha.yaml` → `nazev` má stále „…průvodce vojenským výcvikem a manévry“. Navrhuji sjednotit (`kniha.yaml` jsem needitoval). |
| `predmluva-05` | `die fünff aller fürnembsten vnd nutzlichsten Merckzeichen` | „pěti … znakům[^1]“ | Smysl „pěti znaků“ předmluva nevysvětluje; ponecháno doslovně s poznámkou. |
| `predmluva-01` | `Weiblen`, `Freyweiblen` | „šikovatelům“, „svobodným šikovatelům“ | Ponecháno podle glosáře/zadání, ale v civilní bernské správě jde o soudní/obecní zřízence (poslové, biřici), ne o vojenské hodnosti – vysvětleno pozn. 3. Zvážit vlastní heslo (viz níže). |
| `predmluva-04` | `in einem Kriege zu gebrauchen sey. Die dritte…` / začátek `erfordert werden/ dero dann…` | „vyžadovány? Z nich…“ | Řečnická otázka z `predmluva-03` nemá v tisku otazník; v češtině doplněn kvůli srozumitelnosti (jen interpunkce). |
| `SPORNA_MISTA.md` | `Zugenden` | – | Odrážku `predmluva-14` je třeba smazat/opravit (tisk má `Tugenden`). Odrážka `predmluva-09` je touto revizí vyřešena. |

## 4. Návrhy do glosáře

- `venkov`: doplnit tvar `Landtschafft` (titul; `norm_de` dělá `dt→t`, takže `Landtschafft` ≠ `Landschafft` a odkaz se nespáruje).
- `sikovatel` × bernský `Weibel`: buď v hesle `sikovatel` doplnit do `pozn` civilní význam (ve švýcarských městech soudní a obecní zřízenec, posel), nebo založit samostatné heslo `weibel-bern` (cs např. „biřic / soudní posel“) pro `Weiblen` a změnit překlad na `predmluva-01`. Totéž `svobodny-sikovatel` (`Freyweibel` = předsedající úředník zemského soudu).
- nové heslo `velitel` (`Befelchshaber`, `Befelchsleut`) – na `predmluva-07` přeloženo „velitelé“ bez `{…}`.
- `cviceni`: zvážit `cs` „válečné cvičení“ i pro `Kriegsvbung` (užito na `predmluva-06`, `-07`) – sedí, jen potvrdit.
