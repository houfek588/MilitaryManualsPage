# 2. revize – Solms 1559, dávka kniha3-C (3-025v … 3-037r, skeny 302–325)

Rozsah: 24 stran (3-025v, 3-026r … 3-037r). Sousedé 3-025r a 3-037v jen čteny (návaznost vět sedí).
Postup podle `zdroje/ZADANI_REVIZE2.md` (plynulost „středně“). Struktura bloků, `sken`, `id` a `overeno_clovekem: false` beze změny.
`over_strany.py --prisne`: **0 chyb**, 3 varování (`fein` = „pěkně“ na 3-027v, 3-034v, 3-037r – planý poplach, nelze opravit).

## Hlavní obecné změny
- **Kalky ve výčtech dělostřelectva** (3-025v–3-027r): „váží na železe 72 centů“ → „váží 72 centů železa“; „drží na svém vlastním kovu 240 centů“ → „váží samy o sobě 240 centů“; „Tolikéž prachu činí…“ → „Na stejné množství prachu je třeba…“ / „Stejně tolik prachu váží také…“. Pozn.: soused 3-025r (dávka B) ještě používá „na železe“ – sjednotit.
- Dlouhá souvětí rozdělena (zvl. 3-027v, 3-029r, 3-029v, 3-030r, 3-030v, 3-031r, 3-031v, 3-032r/v, 3-033r/v, 3-035r/v, 3-036r, 3-037r); hranice stran (`pokracovani`) zachovány.
- Terminologie: Büchsen Puluer = „střelný prach“ (sjednoceno s dávkou 3-D), Feurpfeil = „zápalný šíp“ (+ `{Feurpfeiln}` na 3-036v), Kreidenschoß = „výstřel (jako) polní znamení“ podle glosáře (ne „signální výstřel“), däff = „zápalná lázeň / zápalný potah“, pöck = „zvedací kozy“, Kolen/Schwefel doplněny `{}` (3-034r). Odstraněno zavádějící `{Regiment}` (3-030v, význam „zařazení/uspořádání“, ne „pluk“).

## Opravy věcných chyb překladu (před → po)
- 3-028r: *sampt jren ladungen* „spolu s jejich lafetami“ → „spolu s jejich náložemi“.
- 3-028r: *lassen vberhaupt* „vcelku úkolem“ → „za paušální cenu“; *Keyserliche Maiestat* → „Jeho císařské Veličenstvo“; poznámka: zakázka Karla V. (ne „Ferdinanda I. / Karla V.“).
- 3-026v: *derhalben solchs den Rossen souil erschwenglicher* „aby to koně tím snáze zvládli“ → „protože je to pro koně o to namáhavější“.
- 3-026v: *bedörffen … an jren selbst zeug 120 centner* „potřebuje na svém vlastním kovu“ → „je zapotřebí 120 centů samotného kovu“.
- 3-027v: *anzeigend / sie schiessen auch …* „ukazují je a … střílejí“ → „jak tvrdí, … Také z nich … střílejí“; „předimenzované obludy“ (přidané) → „přerostlého děla“.
- 3-025v: *darunder auch einer … mit beschloßner truhen* (vztaženo ke koulím) → jeden z vozů má mít zavřenou truhlu.
- 3-031r: *klein puluer* „drobný střelný prach“ → „malou nálož prachu“; *Instrument … nit gewaltig* → „přístroje nic nezmohou“.
- 3-031v/3-032r: *das halb | teil in das Erdrich gesenckt* – opraven přerušený výklad („polovina [moždíře] je zapuštěna do země a druhá polovina vyhozena namísto šancovních košů“).
- 3-033r: konec věty *vnd so er die menge … gebraucht hat* (dříve nesrozumitelné „než jich bylo víc, znovu jej nasypal“) → „má-li [puškař pytlíků] víc, naplní vyprázdněný pytlík znovu dřív, než spotřebuje ostatní“; věta o zbytcích váčku (3-032v/3-033r) přeložena jako příčina, ne účel.
- 3-034r: přidané „dobrá náplň“ → „náplň“; *ein halbs Saltz* → „půl [libry] soli“.
- 3-036r: *möge außlauffen* „mohlo téct ven“ → „[lázeň] zatekla do dutin“.
- 3-037r: *hirten teil* „třetím či čtvrtým dílem“ → „čtvrtým dílem“ + poznámka; *zochen oder wiegen* → „knoty“.

## Opravy `de` podle skenu (BSB IIIF, staženy skeny 302, 303, 305–307, 310, 312, 313, 315, 317–319, 321, 323, 325)
- **3-028r: `26. Züg.` → `72. Züg.`** – předchozí kontrola chybně „opravila“ tisk; sken jasně má *72* (OCR četlo správně). Poznámka přepsána: tisková chyba předlohy, podle souhrnu na l. 27r je kladkostrojů 26.
- **3-031r: `im stůllen ligen` → `im stillen ligen`** – tisk má *stillen* (tisková chyba za *stülen*); poznámka přepsána (dříve tvrdila, že jde o chybu OCR).
- **3-033v: `sindt` → `findt`** – v tisku je jasně *f* s příčkou; zrušena nepravdivá poznámka o „sazečské záměně“.
- 3-036r: `auff däffen oder schmemen` → `auß däffen oder schmemen`; poznámka upravena.
- 3-033r: `Tonnen` → `Donnen` (tisk). 3-030v: `erfordert` → `erfortert` (tisk). 3-029v: doplněna virgule `geret / ist`.
- 3-025v: `pock` → `pöck`, `stucks`/`stuck` → `stücks`/`stück`, `am gewicht` → `an gewicht`; 3-027r: `zugehörig` → `zugehörige`; 3-027v: `schmucken` → `schmücken`; 3-031r: `falsch` → `falschs`, `auszulernen` → `außzulernen`; 3-037r: `Hirten` → `hirten`.
- Ověřeno beze změny: 3-025v *20. Centner* (tisková chyba za 200), 3-026r *133. kugeln*, 3-027r *1800* a *Plechebüchsen 40*, 3-027v *stonst*, *vortheilt*, *bedurfft*, 3-029v *nit an lange Leger*, 3-030v *ob die sollen*, 3-031r záhlaví *32* (místo 31), 3-032r *Möser*, *war*, 3-035r *schrieben*, *für die schnallen*, *Büchen*, 3-036r *geuierts*, *schmem*.
- Hranice stran ověřeny: *schwei-|ben* (3-026v/27r), *schies-|sen* (3-029v/30r), *Pul-|uer* (3-032v/33r), *geschri-|ben* (3-034v/35r), *sprin-|gete* (3-035v/36r), *la-|den* (3-036r/36v) – celé slovo vždy na straně, kde končí. *darunder/* na konci 3-034r je kustod.

## Poznámky
- Zrušeny poznámky duplikující glosář: 3-028v (Sturmwagen), 3-032v (Kardetsche), 3-034r (Gloriet), 3-034v (däff); čísla přečíslována.
- Poznámka o *Ein halb Kugel* přesunuta z 3-035r na 3-034v (kde výraz stojí).
- Nové: 3-037r n. 1 (*stecklin* asi za *secklin*); 3-027r n. 1 zpřesněna (*schweiben* = *Scheiben*, srov. l. 28r).

## Sporná místa k rozhodnutí
1. 3-028r *thůn die 72. Züg* – v textu ponecháno 72 dle tisku (s poznámkou). Alternativa: emendovat na 26 v `cs`.
2. 3-037r *mit einem hirten teil eines weisen hartzs* – „čtvrtým dílem“ (virten) vs. „třetím“ (dritten). Zvoleno „čtvrtým“.
3. 3-037r *vmb das stecklin herumb* – „kolem váčku“ (emendace *secklin*) vs. „kolem dříku“. Zvolen váček.
4. 3-030r *aber wils also zurichten daruorn* – „předem“ vs. „vpředu (před městem)“. Ponecháno „předem“.
5. 3-037r *durchgehenden beschloßnen scheiben* – přeloženo „průchozími uzavřenými deskami“ (dříve „okovanými obručemi“); přesný technický smysl nejistý.
6. 3-029r *mit einem geringen kosten / mit dem grossen Geschütz in kurtzer zeit* – ponecháno doslovně „s velkými děly“ s poznámkou.
7. Úroveň nadpisu *Volgt ein ander Rüstung von Feurwerck* (3-037r) je `2` stejně jako *Von Feurwerck*; v tisku stejná sazba jako nadpisy úrovně 3 – zvážit `uroven: 3`.

## Návrhy do glosáře (needitováno)
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| delovy-kladkostroj (doplnit de) | dělostřelecký kladkostroj | Züg, Zug, Zügen | delostrelectvo | v kn. 3 běžná podoba *Züg* bez odkazu |
| polovicni-falkonet | poloviční falkonet | halb Falconetlin, halbe Falconetlein | delostrelectvo | cca 2 centy, osazován na útočné vozy (3 ks na vůz) |
| plechova-nadoba (doplnit de) | plechová nádoba na prach | Plechnerbüchsen | delostrelectvo | varianta z 3-025v |
| zvedaci-koza (doplnit de) | zvedací koza | pöck | delostrelectvo | tvar z 3-025v |
| zapalovaci-trubicka | zápalná trubička | Rör, Rörn, Rörlin | delostrelectvo | železná/plechová trubička se zápalnou hmotou v ohnivé a tříštivé kouli |
| tristiva-koule | tříštivá koule | springende kugeln | delostrelectvo | dutá koule plněná prachem, vybuchne po dopadu |
| kozeny-pytlik | kožený pytlík na nálož | ledern Seck, lederen secklein | delostrelectvo | odměřená nálož pro rychlé nabíjení moždíře |
| stolice (doplnit de) | stolice | stülen, stüln, stül | delostrelectvo | tvary z 3-031r/3-032v |
