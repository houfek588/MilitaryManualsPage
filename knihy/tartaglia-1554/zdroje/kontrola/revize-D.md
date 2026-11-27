# Revize – dávka D (skeny 67–88, strany 034r–044v)

Stav: všech 22 stran `stav: zkontrolovano`, `overeno_clovekem: false` (žádná strana nebyla ověřena člověkem).
`python -I nastroje/over_strany.py knihy/tartaglia-1554 034r … 044v --prisne` → 22 stran, 0 chyb, 0 varování.

Úplnost `de` jsem porovnal s OCR strojově (difflib), takže chybějící věty nejsou. Odchylky jsou jen v tabulkách, kde OCR čte sloupce v jiném pořadí. Ve skenu jsem znovu ověřil:
- tabulky receptur č. 1–23 (039r, 039v, 040r),
- popisky úseček na 035v a 036r,
- sporná čtení na 034v, 040v a 041r,
- všechny obrazce (drevorez-70, 71, 85, 86, 87, 87b, 88, 88b, 88c).

Párování bloků s tiskem odpovídá. Hranice stran sedí: *al|quanto* je na 035r, *sen|za* na 036r. Slovo „fermata“ dole na 044v je kustoda a patří na 045r.

## Změny podle stran

| strana | změny |
|---|---|
| 034r | Přestylizována věta o autorech, kteří pravidlo nepochopili. Zkrácena poznámka o prstech (opakovala glosář). V pozn. 3 „otázka“ → „dotaz“. |
| 034v | Sjednocení „v předchozí otázce“ → „v předchozím dotazu“ (4×). „Že je tomu tak, dokládá jeho závěr…“ místo neobratné vazby. |
| 035r | „otázka“ → „dotaz“ (2×). Oslovení „Převážený“ → „Velectěný“ (honorandissimo). |
| 035v | **Opraven popis obrázku**: úsečky se doprava neprodlužují plynule; poloviny průměrů jsou kratší a pak opět rostou. Přepočty rotul → libry ověřeny, všechny sedí. |
| 036r | Upřesněn popis obrázku (poslední úsečka pro 1½ rotulu je opět delší). Chyba tisku u 8 rotulů („e un terzo“ místo ⅔) potvrzena. |
| 036v | Plynulejší závěr věty („nic, co se zhotovuje z hmoty…“). „Kdo by je chtěl…“ → „Chcete-li je však…“ (věrněji, je to oslovení adresáta). |
| 037r | Nadpis sjednocen s knihami I, II a VI: „Třetí kniha … Niccola Tartaglii“. „Kamenná sůl“ dána do uvozovek a doplněna nová pozn. 6 (sal petroso = sal petrae → Salpeter, nejde o halit). Zkrácena pozn. o Tadinovi. |
| 037v | Názvy ledku v uvozovkách („hořlavá sůl“, „kamenná sůl“, „sal praticha“) – oprava pádové vazby. Plynulejší „Je tedy dobře možné…“. |
| 038r | „chytí plamenem“ → „chytí plamen“, „ve velké míře“ → „ve velkém množství“, „skončeme“. |
| 038v | „na autoritu Cornazzanovu“ → „na základě Cornazzanova svědectví“. „ordine e proportione“ → „podle takového předpisu a poměru“ (jednotně s *ordine* = předpis). |
| 039r | Stylistika. Tabulka č. 1–4 ověřena ve skenu. |
| 039v | Tabulka č. 5–19 ověřena ve skenu. Pozn. 2 doplněna o propočet (6 dílů = ¾, 8 dílů = ⅘ ledku) a „v šesté otázce“ → „v šestém dotazu“. |
| 040r | Tabulka č. 20–23 ověřena. „živé důvody“ → „pádné důvody“. Přestylizována převorova replika. |
| 040v | „(v nepříliš dávné době)“, „skončeme“. Zlomky 1/3, 3/7, 5/8, 12/17, 9/14, 2/3 ověřeny výpočtem. |
| 041r | V `de` obnovena tisková chyba „uuo“ (= uno) podle skenu a zmíněna v poznámce. Stylistika závěrečné repliky. |
| 041v | „v 11. otázce“ → „v 11. dotazu“ (3× včetně poznámky). *ogni specie di artegliaria* → „každý druh děla“. Doplněno „[mistra]“ u člověka z Arzenálu. |
| 042r | *fromento* → „pšenice“ (bylo „zrní“, což se pletlo se „zrněním“). Přestylizována věta o prosbě v Arzenálu. |
| 042v | „zrní“ → „pšenice“ (3×). *inescar* → „k podsypání {inescar} toho malého otvoru“. |
| 043r | Nadpis „Čtvrtá kniha … Niccola Tartaglii“. V poznámce „otázky“ → „dotazy“. |
| 043v | *piu che bislonga* → „výrazně podlouhlý“ (bylo doslovné „víc než podlouhlý“). Plynulejší dotaz hraběte. Výpočty ověřeny (14² = 196, 187² = 34 969, zbytky 4 a 31). |
| 044r | Bez změn textu, ověřeny obrazce 87 a 87b a míry 63 × 27 stop. |
| 044v | „v této otázce“ → „v tomto dotazu“. Popisy obrazců 88, 88b (chybějící koncové „o“) a 88c ověřeny ve skenu. |

Opravy podle druhu (přibližně):
- 14× terminologie a sjednocení („otázka“ → „dotaz“, nadpisy knih, předpis),
- 7× věcné a významové opravy (pšenice, druh děla, výrazně podlouhlý, oslovení, uvozovky u názvů, tvar „Chcete-li“, „[mistra]“),
- 3× popisy obrázků (035v, 036r) a nová poznámka (037r),
- 1× oprava `de` podle skenu (041r „uuo“),
- asi 15× stylistika.

## Rozhodnutá sporná místa ze zprávy překladatele

- **Nadpisy dotazů**: dávka už měla formát „Devátý dotaz, který položil …“ podle ZADANI_REVIZE. V textu a poznámkách jsem sjednotil všechny zbylé „otázky“ na „dotaz“.
- **039v, předpis č. 19 – 6 × 8 dílů ledku**: ve skenu je v tabulce jasně „parti 6.“, v textu na 039r „parti.8.“. Ponecháno podle tisku s poznámkou. Rozhodnout, které číslo je chybné, nelze; na závěru 6. dotazu to nic nemění.
- **cazza** → „nabíjecí lžíce {cazza}“ ponecháno. Hledací výraz hesla *nabijak* (`\blžíc\w*`) odkaz zachytí. Viz návrh do glosáře.
- **Vaše Důstojnost** pro *Vostra Reuerentia / quella* u převora ponecháno; tak to dělá i zbytek knihy (047v, 065r…).
- **ordine** = „předpis“ ponecháno a dotaženo i na 038v („podle takového předpisu“).
- **sal praticha, suboido**: ponecháno s poznámkou, lepší výklad jsem nenašel.

## Zůstává sporné (k rozhodnutí člověkem)

1. **036v, poměr železa a kamene.** Tisk uvádí „quasi come da 15 à 38“ a „come 38 à 15“, tedy kámen ≈ 0,39 železa. S údajem „olovo : kámen = 4 : 1“ a „olovo : železo = 30 : 19“ to dává 0,40, takže je to vnitřně v pořádku a ponecháno bez poznámky.
2. **034v, pozn. 4 – Tartagliova věcná chyba** („asi osmina, o něco méně“ prstu pro 6 liber; správně ≈ 0,21). Ponecháno; poznámka to vysvětluje.
3. **037v, „sal praticha“** – nepřeloženo. Návrh: ponechat, případně „sal pratica“ = „praktická (užívaná) sůl“.
4. **040r, „suboido“** – CS „zvlhlé“. Snad benátské *sboìo / imbevuto*; ověřit v benátském slovníku (Boerio).
5. **041v, „moschetti“** – CS „muškety“ s poznámkou. V tomto kontextu jde spíš o lehká otočná děla (moschetto da posta) než o pozdější mušketu. Zvážit „mušketóny“ nebo ponechat.

## Návrhy do glosáře

| id | cs | it (de) | kategorie | pozn. |
|---|---|---|---|---|
| predpis-prachu | předpis (receptura prachu) | ordine, ordini | delostrelectvo | Poměr ledku, síry a uhlí; Tartaglia uvádí 23 předpisů (039r–040r). |
| prachovnice | prachovnice | fiasca, fiasche, fiaschettino | zbrane | S dávkovací trubičkou (canoncino); malá prachovnička na podsypávací prach. |
| davkovaci-trubicka | dávkovací trubička | canoncino | zbrane | Měrka na hrdle prachovnice (042v). |
| podsypani | podsypání (zápalu) | inescar, inescare | delostrelectvo | Nasypání jemného prachu do zápalného otvoru (busettino). |
| prapor | prapor | bandera, bandiera | jednotky | Stojí uprostřed druhé části pochodového sledu, ve čtvercovém šiku pak ve středu (044r). |
| balista | balista | balista, Balista | zbrane | Antický vrhací stroj; otvor hlavice (forame del capitello) je modul (034v–035r). |
| moschetto | mušketa | moschetto, moschetti | zbrane | Viz sporné místo 5. |
| arsenal | Arzenál (benátský) | Arsenale, arsenale | mista | Státní loděnice a zbrojnice v Benátkách. |
| trojclenka | trojčlenka | regola del tre | mereni | 034r. |
| treti-odmocnina | třetí odmocnina | radice cuba | mereni | Doplnit k heslu *odmocnina* (034r–035r). |

Úpravy stávajících hesel:
- **unce**: přidat délkovou unci (*onze di misura* = 1/12 stopy) a tvar *onze*.
- **stopa**: přidat tvar *pie*. Normalizace ho na *piede* nenapojí.
- **nabiják**: rozlišit lžíci (*cazza, cucchiara*) a pěch (*calcatore*). Nebo nové heslo „nabíjecí lžíce“.
- **zrnění prachu**: pozn. „jemný pro ručnice, hrubý pro děla“ je v rozporu s 041v–042v. Podle Tartaglii se zrní **jen** jemný prach do ručnic a arkebuz, hrubý dělový prach se nezrní. Doplnit tvary *ingranire, granita*.
- **prach**: tvar *poluere delle artegliarie* se napojí přes *poluere*, to je v pořádku.

## Osoby a místa pro rejstřík

- **Osoby**:
  - Giulio Savorgnan (Sauorgnano)
  - Giovanni Antonio (Zanantonio) Rusconi
  - Gian Giacomo dell’Acaya (Iacomo di Achaia)
  - Gabriele Tadino da Martinengo (převor z Barletty)
  - Hieronimo, podvelitel dělostřelců na Kypru
  - hrabě Hieronimo da Piagnano
  - Vitruvius, Avicenna, Serapion, Dioskúridés, Plinius, Matteo Silvatico (Pandette)
  - Antonio Cornazzano, Archimédés, Roberto Valturio, Cesare Cesariano, Vegetius
- **Místa**: Lecce (Lezze), Benátky (Arzenál), Kypr (Cipri), Barletta, Syrakusy, Piagnano.
