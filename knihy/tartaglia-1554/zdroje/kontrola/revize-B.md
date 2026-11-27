# Revize – dávka B: listy 12r–22v (skeny 23–44), První kniha, dotazy III (konec) – XVII

Všech 22 stran má `stav: zkontrolovano`, `overeno_clovekem: false` (nikde nebylo `true`).
`python -I nastroje/over_strany.py knihy/tartaglia-1554 012r … 022v --prisne` → 22 stran, 0 chyb, 0 varování.

Překlad od dávky B byl kvalitní: italský text je úplný (poměr délky `de` k OCR 1,00–1,04 na všech stranách,
rozdíl dávají rozepsané zkratky), párování replik a nadpisů odpovídá tisku a hraniční slova (sup|poneremo, tira|re,
Vrbi|no, de|ue) jsou na správné straně. Ve skenu jsem namátkou ověřil sporná čtení (12r „& con tanta“, 12v
„uostre inuentioni“ / „uostre ragioni“, 18v a 19r všechna čísla v seznamu děl, 18v „iire“ = lire). Text `de` jsem
neměnil. Opravy se týkají hlavně plynulosti a jednotnosti, věcné posuny byly jen drobné.

## Přehled změn
| Strana | Změna |
|---|---|
| 012r | „když se z ní střílí s předkem zdviženým“ → „střílí-li se s hlavní vpředu poněkud zdviženou“ (*quella* = kolubrina, ne koule); pozn. 2 zpřesněna (odkaz na listy 10v–11v, „dotaz“ místo „quesito“) |
| 012v | *ragioni naturali* = „přírodní důvody“ (ne „přirozené“); pozn. 2 „dotazy IV–XVII“ |
| 013r | *attrattiuo* – odstraněno kalkované „stává se sacím / sací vada“ → „nasává stále víc“, „nedostatek, totiž sání“; „a možná i víc“ → „i s přebytkem“ |
| 013v | *satisfatto* = „uspokojil“ (ne „vyhověl“); *tiro longo* = „delší dostřel“ |
| 014r | „přírodními důvody“ (sjednoceno) |
| 014v | nová pozn. 2: v tisku neuzavřená závorka za „El secondo proposito“ |
| 015r | beze změny textu |
| 015v | `popis` drevorez-30 zpřesněn (obrazec patří k výkladu na 15r, přední mířidlo D, oko mířiče) |
| 016r | „pochopí (z přirozeného rozumu)“ → „pochopí přirozeným rozumem“ |
| 016v | *scarsetta* = „kratší“ (ne „skrovnější“) |
| 017r | přestavěna toporná věta „o kolik nekonečně mnoha způsoby…“; *dignita* = „čest“ (ne „hodnost“) |
| 017v | *incontrano* (lišty) = „srovnají“, ne „přiloží“ |
| 018r | *medicar quel tal effetto* = „napravovat vadu“ (ne „léčit účinek“); převorova replika o kolubrinách uhlazena; „mohlo stát“ → „by se mohlo stát“ (podmiňovací *potria*) |
| 018v | nová pozn. 2 k nejasnému „ne azzo una notta“ |
| 019r | Nicolòova replika uhlazena; pozn. 3 (kortald) zkrácena o spekulaci (moždíř/houfnice) |
| 019v | „Posuďte tedy, zda to časem nebude mnoho znamenat“; „přírodními důvody určit“; pozn. 2 o Tadinově stáří zkrácena na ověřitelné („převor se zmiňuje o nemoci; zemřel 1543“) |
| 020r–021r | beze změny textu |
| 021v | „střední mezi mezi“ → „střední hranici mezi“; *el passa l'hora da cena* = „hodina večeře už minula“ |
| 022r | *offende* = „působí větší škodu“ (ne „ubližuje“); *da banda à banda* = „skrz naskrz“ |
| 022v | *balle scarsette* = „poněkud menší koule“; „zapálilo by se jim to ústím“ → „zapálila by se ústím“ |

Ověřeno: všechny obrázky (drevorez-24, 28, 28b, 30–34) – popisy odpovídají výřezům (písmena, nápisy LINEA VISVALE /
TRANSITO DELLA BALLA). Na drevorez-28 prosvítá zrcadlově text z rubu („QVESITO SETTIMO…“) – to je průsvit, ne nápis.
Aritmetika 18r ověřena (2/3 z 20 liber = 13 liber 4 unce, 4/5 = 16 liber, rozdíl 2 libry 8 uncí při 12 uncích na libru).

## Rozhodnutá sporná místa ze zprávy preklad-B
- **Návaznost 11v → 12r**: 011v končí „… tím činí“, 012r začíná „svůj pohyb méně zakřiveným.“ – navazuje, ponecháno.
- **Drobné tiskové chyby** (*siamo* 16r, *Sacri la* 18v, *poportionale* 20r, *dabole* 21r, *ballo* 22r, *in in* 15v,
  *in eguali* 12v) – ponechány v `de` bez poznámky, smysl je jednoznačný a překlad je správný. Poznámky mají jen místa,
  kde by čtenář mohl zaváhat (*toccata* 15r, *.o.* 16v, *duendoli* 18r, *azzo* 18v, mezera v sazbě 19r, *come si sa me
  si sa* 22r, neuzavřená závorka 14v).
- **bocca** – glosář už má heslo `usti` (ústí; „bocca neznamená ráži“), návrh překladatele je tím vyřízen.
- **transito / uiaggio / tramito** = dráha / cesta – ponecháno („dráha čili cesta“), odpovídá glosáři `draha`.
- **„tirar de mira“** = „střílet podle mířidel“, „dostřel podle mířidel“ (16v–17r) – ponecháno s poznámkou na 16v.
- **ragion(i) naturale/i** sjednoceno: „přírodní důvody“ (12v, 14r, 19v); „per ragion naturale“ v úvodu výkladu
  ponecháno „z přirozeného rozumu“ / „přirozeným rozumem“ (16r, 22r), kde jde o zdravý úsudek.

## Dál sporná místa (k rozhodnutí člověkem)
- **012r** „in tal obliquo uerso“ (vévoda o vodorovném výstřelu) – přeloženo doslova „v tomto šikmém směru“; Tartaglia
  zřejmě míní „šikmý vůči svislici“ (každý směr kromě svislého). Návrh: ponechat, případně „v tomto ne svislém směru“.
- **013r/021r** *essalatione uentosa / uentosita* = „větrný výpar / větrnost“ – shodné s 23r, ale pro čtenáře neprůhledné.
  Návrh na celou knihu: heslo glosáře „větrný výpar (plyny z hořícího prachu)“.
- **022v** *dischiodare* = „odtlouci“ – novotvar k „zatlouci“; alternativa „uvolnit zatlučené dělo“.
- **018v** *ne azzo una notta* – čtení ověřené ve skenu, tvar nejasný (snad nářeční „gh'ho“ / „ne ho“).

## Návrhy do glosáře
| id | cs | it (tvary z tisku) | kategorie | pozn |
|---|---|---|---|---|
| vetrny-vypar | větrný výpar | essalatione uentosa, essalation uentosa, essalatione aerea, uentosita | delostrelectvo | plyny z hořícího prachu, které podle Tartaglii ženou kouli |
| prachova-stopa | prachová stopa | sementella, sementelle | delostrelectvo | nasypaná dráha prachu k zapálení zdálky (21v, 22v) |
| aspid | aspid | aspide, Aspidi | delostrelectvo | lehké dělo kolem 12 liber (18v) |
| passavolante | passavolante | passauolante, Passauolante | delostrelectvo | dlouhé dělo malé až střední ráže (19r) |
| kortald | kortald | cortaldo, cortaldi | delostrelectvo | krátké těžké dělo na kamenné koule (19r) |
| unce (doplnit) | unce | onze | miry | benátský tvar k heslu `unce` (18r) |
| libra (doplnit) | libra lehká / těžká | lira alla sottile / alla grossa | miry | benátská libbra sottile ≈ 0,30 kg, grossa ≈ 0,48 kg (19v) |
| zatlouci (doplnit) | zatlučení / odtlučení | dischiodar, dischiodare, deschiodare, inchiodatura | delostrelectvo | doplnit tvary k heslu `zatlouci` (22v) |
| prirozeny-pohyb / draha | – | tramito (už v `draha`) | – | beze změny |

## Osoby a místa
- **Gabriele (Gabriel) Tadino da Martinengo** († 1543), johanita (rytíř rhodský), převor v Barlettě, velitel
  dělostřelectva Karla V.; tazatel dotazů IV–XVII.
- **Francesco Maria I. della Rovere** († 1538), vévoda z Urbina (14r „padre di questo“ – otec Guidobalda II.).
- Místa: Pesaro (12v), Barletta (12v, 19v), Rhodos (12v), Benátky (19v – benátská míra).
- Dílo: *Nova scientia* (1537) – 3. a 4. věta 1. knihy (12r, 22r); Eukleidés – pátý postulát (14v).
