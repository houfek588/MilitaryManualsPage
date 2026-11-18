# 2. revize – Druhá kniha, dávka F (073v … 087v, skeny 222–248)

Rozsah: 27 stran (073v–076v, 078r–087v; list 77 tisk přeskakuje), konec Druhé knihy: nižší úřady pěchoty
(šikovatelé, vůdci, furýři, šikovatelé trénu), kat, služební list jezdců, služební list plukovníka lancknechtů
(Bemelberg 1536), artikulní list lancknechtů, Řád posádky a Soudní řád lancknechtů. Sousedé `073r`
a `3-erb-solms` jen čteny; návaznost sedí. Plynulost „středně“ podle `ZADANI_REVIZE2.md`: souvětí dělena v rámci bloků,
struktura bloků, `sken`, `id`, `stav` a `overeno_clovekem: false` beze změny, všechny přechody `pokracovani: true`
(079v, 081v, 082r, 082v, 084r, 085r, 085v, 086r, 086v) dál sedí s tiskem.

Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 073v … 087v --prisne` → **27 stran, 0 chyb, 0 varování**.

## Opravy `de` podle skenů (BSB IIIF)

| strana | bylo | tisk (sken) | pozn. |
|---|---|---|---|
| 078v | auff fünfftig pferdt | **fünfftzig** | OCR vynechalo *tz* (s230) |
| 081r | den Hauptleuten angezeigt | **angezeiget** | s235 |
| 083v | mit nottwendigem geschütz | **notwendigem** | s240 |
| 087r | Gerichtsordnung der Lantsknecht | **Lantskneckt** | s247, tisková podoba jako na 079r; doplněno do pozn. 1 |

Ověřeno beze změny: *darein nicht gehen oder stehen* (081r), *Schroten/ Schmidten/ Salbeter* (083v),
*Hauptleut.* jako druhý menší řádek pod nadpisem 087r, iniciála *W* místo *E* v „ES sollen“ (087r, pozn. 2),
*Rotmeisters ambs*, *Schimdt*, *Fecken* (078v), *weinger* (078r).

## Hlavní změny překladu po stranách

- **074r** – *gemein Man* „prostý lid“ → „obec“ (glosář `obec`; jde o shromáždění mužstva, ne o civilisty);
  věta o nižších šikovatelích přestavěna; pozn. 1 (*Weibels Weibel*) vypuštěna – opakovala glosář `nizsi-sikovatele`
  a obsahovala neověřený údaj o „deseti“ polních šikovatelích. „přičleněných a vybíhajících střelcích“ → „o rozestavení…“.
- **074v** – popis dřevořezu opraven podle obrázku: „ukazuje k seřazeným houfům pěchoty s píkami“ (na obrázku nejsou)
  → ukazuje před sebe, v pozadí krajina s městečkem; monogram v pravém dolním rohu, ne „pod pařezem“.
- **075r** – „sesazováni prostým lidem“ → „obec sesazuje / dosazuje“; pořadí ubytování srozumitelně.
- **076r** – „ženy i holomky“ → „nevěstky a pacholky {Hurn vnd Bůben}“ (glosář `nevestky-a-chlapci`), pozn. 1 vypuštěna;
  „využívá je až na kůži“ → „plně je využije“ + nová pozn. k rčení *nach der haut*; závěrečná věta v 1. osobě autora.
- **076v** – popis: odstraněn neověřitelný „odznak s vyobrazením šibenice“, doplněny sovy s myšmi, svazky provazů,
  postavy přesněji (pomocníci „patrně kat a žalářník, případně profousovi pacholci“).
- **078r** – *ob einem ein pferde an den Feinden schadhafftig wurde* → „Utrpí-li někomu kůň u nepřátel škodu…
  jako dar a odškodnění“; dělení vět; pozn. 1 opravena (*weinger* je přesmyčka, ne vypuštěné písmeno).
- **078v** – *mit denselben geledigt* „s nimi vykoupen“ → „za ně vyměněni“; *nach seinem nutz schetzen* „ocenit“ →
  „vymoci si výkupné“; *auff dieselb Malstat* → „až do návratu na totéž shromaždiště“.
- **079r** – spor řeší „vynést výrok a rozhodnout polní maršálek“ (místo „spočívat na výroku“); ručení měst N. nebo N.
  přeloženo srozumitelně; „píci… kdekoli ji tam najdou“.
- **079v** – *gemeine Hauptleut* „řadoví hejtmani“ → „všichni hejtmani“; *auff weiter Bestallung* → „na základě dalšího
  služebního listu {Bestallung}“ (glosář `sluzebni-list`, dříve „služební smlouva“).
- **080r** – *gegen den feinden oder von den feinden* „proti nepřátelům, či od nepřátel“ → „směrem k nepříteli, či od něho“;
  *Kriegsman* „voják“ → „válečník“ (shodně s 085r a s rozhodnutím *Kriegßleut* = válečníci); „jeden či více lidí…
  má či mají“ → „ať jeden, či více“.
- **080v** – *wie jm der Monat seins dienst begreifft* → „ať je v měsíci své služby kdekoli“; věta o dezerci zjednodušena;
  zákaz tábořit v kostelech jako samostatná věta.
- **081r** – „vcházet či postávat“ → „vstupovat či se tam usazovat“; „probodnout“ → „bodnout do něj“.
- **081v** – chybný zápor: „nesmí… začínat vzpoury… a také s nimi hrát“ → „ani s nimi hrát“; *friede nemen* „vyhlásit mír“
  → „vyžádat mír“, *nicht friede geben* „mír nezachoval“ → „mír neslíbil“.
- **082r** – „neradit a nenapomáhat“ (dvojí totéž) → „neradit a nenavádět“, *vortheil* = „lest“; *vor oder durch zeucht*.
- **082v** – `{Ordnung}` u „válečného obyčeje a řádu“ odstraněn (heslo *šik* nesedí); *an leib vnd leben* „na hrdle“ →
  „na těle“; hra „jen o hotové peníze“; závěrečné ustanovení srozumitelně („má to být na plukovnících“).
- **083r** – *Kriegsübungen* „válečná cvičení“ → „válečné činnosti“; úvod „je namístě co nejstručněji pojednat“;
  „nevěstky a chlapce“ → „nevěstky a pacholky“ (glosář); výčet proviantu v genitivu.
- **083v–086r** – *Kriegsuerstendigen* „váleční znalci“ → „znalci válečnictví {…}“ (glosář `znalec-valecnictvi`),
  *Kriegserfarnen* → „ve válce zkušení muži“ (odlišeno od *Kriegsleut* = válečníci). 083v: věta o zákazu plýtvání
  prachem přestavěna; mlýny „o které nemůže přijít“. 084r: *bei leib vnd leben* „na hrdle“ → „na těle“.
  084v: „pevné pravidlo“ → „obšírně psát“ (*statlich*). 085r: dvojžoldnéři „několik před půlnocí a několik po ní“;
  *zum sturm ordnen* → „k odražení útoku“; *platz* „volné prostranství“ → „místo [k postavení obránců]“ (odkaz na 084v);
  z pozn. 2 vypuštěn výklad *schlahende feuer* (je v glosáři `traskavy-ohen`). 085v: dlouhé souvětí rozděleno,
  `{hauffen}` u „vtrhnout v houfu“ odstraněn. 086r: přidané „jeden“ u počtu příkopů odstraněno, „někdy i dvakrát či
  třikrát“; *Justitie* „spravedlivé soudnictví“ → „dobrou spravedlnost {Justitie}“ (rozhodnutí autora).
- **086v** – „pevné bránění a tuhé držení se“ → „jak se pevně bránit a houževnatě držet“; závěr („byť jen skromně přislíbit“).
- **087r** – *so sich vor versprechen* → „které si ustanoví řečníka“ (podle *verfürsprechen*, srov. Fronsberger), pozn. 3
  upravena; pozn. 1 k „Hauptleut.“ přepsána podle skenu; předvolání ke svědectví a úschova u rychtáře srozumitelně.
- **087v** – „prostý lid“ → „obec {gemeinen Mans}“; „to jde dokola“ → „to se střídá dokola“; závěrečné ustanovení
  o článcích sjednoceno s 082v.

Beze změny ponechány (po kontrole): 073v, 075v (popisy dřevořezů sedí s obrázky).

## Sporná místa k rozhodnutí

1. **083v** *Schroten/ Schmidten/ Salbeter* – „Schmidten“ ve výčtu materiálů (tisk potvrzen). Ponecháno „kováři“
   (srov. *Schmiden* u stavitele téže strany); možné i „kovářské zboží / kovárny“.
2. **079r** *des Obersten Hauptmans vnd Beuelchabers* – bez virgulí; přeloženo jako jedna osoba „nejvyššího hejtmana
   a velitele“. Alternativa „plukovníka, hejtmana a velitele“.
3. **084v** *an dem nechsten 4. Artickel vor disem* – pozn. 1 čte „4. odstavec před tímto“; možné i „4 předchozí články“.
4. **087r** „Hauptleut.“ – pokračování titulu, nebo samostatné záhlaví? Struktura ponechána (samostatný nadpis `uroven: 3`).
5. **Sjednocení *gemein Man* napříč knihou** – v této dávce „obec“ (podle glosáře); jinde v Druhé knize (013r, 035r, 044r,
   064v) zůstává „prostý lid“ – doporučuji sjednotit v dávkách A–E.
6. **076r** *gebrauch sie nach der haut* – výklad „naplno, důkladně“ vs. „podle jejich povahy“ (pozn. 1).

## Návrhy do glosáře

| id | cs | de (doplnit) | kategorie | pozn |
|---|---|---|---|---|
| justice | justice (spravedlnost) | + `Justitie` | pravo | varianta z 086r |
| znalec-valecnictvi | znalec válečnictví | + `Kriegsuerstendige` | velitele | varianta z 085r |
| obec | obec | + `gemein Man`, `gemeinen man`, `gemeinen Mans` | jednotky | Solmsovy podoby (074r, 075r, 087v) |
| nevestky-a-chlapci | nevěstky a pacholci | + `Hurn vnd Bůben` | sluzba | 076r |
| soudni-misto | soudní místo | (pozn.) | pravo | u jízdy (078v) *Malstat* = přehlídkové shromaždiště; doplnit do pozn. |
| ve-valce-zkuseni (nové) | ve válce zkušení muži | Kriegserfarnen, Kriegßerfarnen | velitele | odlišit od *Kriegsleut* (válečníci) a *Kriegsuerstendigen* |
| stavitel (nové) | stavitel | Bawmeister, Bawmeistern | opevneni | stavitel opevnění v posádce (083v–086v) |
| quastitor (nové) | zákopník | Quastitor, Quastitorn | opevneni | z it. *guastatore*; nebo přidat k heslu `zakopnik` |
