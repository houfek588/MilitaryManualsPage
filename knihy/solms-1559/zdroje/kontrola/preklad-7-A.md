# Překlad 7-A – Solms 1559, Sedmá kniha (skeny 546–565)

Dávka: `7-erb-solms`, `7-titul`, `7-001r` – `7-009r` (19 stran; sken 548 = prázdný rub titulu, v edici není).
Všechny strany: `stav: prelozeno`, `overeno_clovekem: false`. Kontrola
`python -I nastroje/over_strany.py knihy/solms-1559 <19 stran> --prisne` → **0 chyb, 1 varování**
(7-003r: „fein“ – falešný poplach, tisk má skutečně *daß ers fein ordentlich … beschreib* „pěkně“).

Přepis podle skenů BSB (IIIF, 1600 px + výřezy), OCR jen jako výchozí text. Sousední strany 6-027r a 7-009v
jsou ještě kostry (`chybi_original`) – návaznost: 6-027r je jiná kniha (přehlídkový rejstřík), 7-009v začíná
novými (červenými) kartami, takže žádný odstavec nepřechází přes hranici dávky.

## Přehled stran
| Strana | Sken | Obsah |
|---|---|---|
| 7-erb-solms | 546 | nápis *Reinhart der Elter…* + erbovní dřevořez (popis) |
| 7-titul | 547 | titul *Das sibend Bůch ist Ein Kartenspiel…* (nadpis 1), odstavec o Hannibalovi a Scipionovi, císařský znak, tiráž *M. D. Lix.* |
| 7-001r | 549 | *Anfang des sibenden Buchs* (nadpis 2), úvod ke karetní hře – iniciála **IN** doplněna |
| 7-001v | 550 | dokončení věty (`pokracovani`), nadpisy *Veldzug auff zwei tausent Pferde…*, *Zehen tausent Knecht* (3), pochodový řád předvoje a jízdy; iniciály **ER**, **DIe** |
| 7-002r | 551 | pěchota, děla, vozová hradba; otázky hráče |
| 7-002v | 552 | psané karty, proč antická jména (`pokracovani`) |
| 7-003r | 553 | *Volgt noch ein weitterer Bericht…* (nadpis 3), iniciála **WAnn** |
| 7-003v | 554 | užití karet plukovníkem; nadpis 2 *Volgt ein Zugordnung…* (uvedení karet) |
| 7-004r | 555 | 8 černých obrazových karet (úřady) – obrázek + tabulka nápisů |
| 7-004v | 556 | 9 černých karet jízdy, čísla 100, 50 |
| 7-005r | 557 | 8 černých karet (střelci, děla, vozy, lodní most, moždíř) – bez nápisů |
| 7-005v | 558 | 4 černé karty pěchoty + vlepený textový odstavec *Dise hernachuolgende…*; **nově přidán blok `obrazek` `drevorez-558.jpg` – soubor neexistuje, výřez musí doplnit správce** |
| 7-006r | 559 | 8 textových karet (Hannibal, Himilkón, Hasdrubal, Syfax, Karthalo, Magón, Filip Makedonský, Jugurtha) – tabulka |
| 7-006v | 560 | 8 textových karet (rytmistři Juba, Bocchus, Micipsa, Hiempsal, Saburra; šarfmece, kartouny) |
| 7-007r | 561 | 8 textových karet (kulveriny, falkonety, lodní mosty, vozy) + odstavec *Volgt hernach das gegentheil von den Römern/ mit roter Farb* |
| 7-007v | 562 | 8 červených obrazových karet (Římané, úřady) – tabulka nápisů |
| 7-008r | 563 | 9 červených karet jízdy, čísla 100, 50, 25 |
| 7-008v | 564 | 8 červených karet (střelci, děla, vozy) – bez nápisů |
| 7-009r | 565 | červené karty pěchoty, písmena A, B; bloky drobných střelců |

Karty: podle rozhodnutí autora vždy blok `obrazek` s popisem jednotlivých karet (číslováno po řádcích zleva
doprava) + `typ: tabulka` se sloupci *číslo karty | nápis* (DE) a *číslo karty | překlad* (CS); strany bez nápisů
mají jen obrázek s popisem.

## Nejistá čtení ze skenu
- 7-001v, ř. 2: *Vnd wil* – rozmazáno, čteno podle smyslu (poznámka).
- 7-001r: *auff das vortheil hafftigst* – konec slova pod *s* nejasný (zda *-igs* s nadepsaným *t*); přepsáno *hafftigst*.
- 7-004v karta 9: místo čísla jen skvrna (červený protějšek má „25“); 7-008r karta 6: číslice „1“ v „100“ poškozená.
- 7-006r karta 7: *Capitan der Justitien* – písmena poškozená (*Capi tander*).
- 7-007v: zkratky *EDEL MĀ*, *CAPITĀ* rozepsány.

## Sporná místa (DE + CS + důvod)
1. **7-002r, 4. odstavec** – *Die andern 4000. Knecht sollen bei dem gewaltigen hauffen oder mittelzug ziehen/ der auch 1500. pferde auff der lincken seiten…* téměř opakuje předchozí odstavec (opět „levá strana“); v exempláři orámováno červenou tužkou. Přeloženo doslova, v poznámce možná chyba tisku (snad pravá strana). Také *aller zu gehörte gehn* – nesrozumitelné, přeloženo „se vším příslušenstvím“.
2. **7-001v** – součet koní 100 + 200 + 100 + 1500 + 70 = 1970, tisk uvádí 2000 (poznámka).
3. **7-002v** – *wann er dann ein grosser Ampt bekeme/ würds jn verdiessen* – *verdiessen* = tisková chyba za *verdriessen*; doplněn podmět „[jiný]“.
4. **7-titul** – *Veldoberster* přeloženo „polní plukovník“ (podle rozhodnutí *Oberst = plukovník*); u Hannibala a Scipiona by se věcně hodilo „vrchní polní velitel“ – k rozhodnutí.
5. **Tiskové chyby ponechané v DE** (s poznámkou): *Carnelius* (Cornelius), *Knech* (Knecht), *veldhaptman*, *Juiorta* (Jugurta), *Ritmeiser*, *fünffhunhert*.
6. **7-003v** – *wo/ auff/ neben/ oder wem er ziehen soll* → „kde, za kým, vedle koho nebo s kým“; *auff* chápáno jako „následovat za“.
7. **7-001v** – *der Knecht Forirer* → „furýra knechtů {Forirer}“; *den zeug oder Artolorei meister* → „zbrojmistra neboli mistra dělostřelectva“.

## Návrhy hesel do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| karetni-hra | karetní hra | Kartenspiel, Kriegßkarten | sluzba | Solmsova výuková „válečná karetní hra“ (7. kniha) |
| polni-plukovnik | polní plukovník | Veldoberster, Veltoberster, Veldöbersten | velitele | vrchní velitel vojska v poli; zatím podle pravidla *Oberst = plukovník* |
| hlavni-houf | hlavní houf | gewaltig Hauff, gewaltigen hauffen, mittelzug | jednotky | hlavní (střední) voj pochodového řádu |
| pochodovy-rad | pochodový řád | Zugordnung, zug ordnung | sluzba | sestava vojska na pochodu |
| vybrani-knechti | vybraní knechti | außgeschossen Knecht | jednotky | = ztracený houf |
| strelecka-korouhev | střelecká korouhev | schützen Fan | jednotky | korouhev jízdních střelců |
| predni-hlidka | přední / zadní hlídka | vorwart, nachwart, vorwacht | sluzba | hlídky předvoje a zadního voje |
| markytanski-vuz | markytánský vůz | Marcatantenwagen, Macatanten wagen | zbrane | doplnit k heslu markytán |
| delostrelecky-vuz | dělostřelecký vůz | Artoloreiwagen | delostrelectvo | |
| kara | kára | Karn, karn | zbrane | dvoukolový vozík na prach a koule |
| slechtic-delostrelectva | šlechtic dělostřelectva | Edelman der Artolorei | velitele | úřad v dělostřelectvu (karty) |
| kapitan-delostrelectva | kapitán dělostřelectva | Capitan der Artolorey | velitele | |
| mistr-delostrelectva | (nejvyšší) mistr dělostřelectva | Artoloreimeister, Artolorei meister | velitele | ztotožněn se zbrojmistrem (*zeug oder Artolorei meister*) |
| vuz-vozove-hradby | vůz vozové hradby | Wagenburgwagen, Rüstwagen | opevneni | |
| dvorska-celed | dvorská čeleď / služebníci | Hoffgesind, Hoffdiener | osoby | družina velitele |
| generalni-vachmistr | generální vachmistr | General Wachtmeister | velitele | |
| ctvrtecni-kulverina | (doplnit tvar) | quartirschlangen | delostrelectvo | doplnit do existujícího hesla |
| falkonet | (doplnit tvar) | Falconetlin | delostrelectvo | doplnit do existujícího hesla |
| munice | (doplnit tvar) | Monition wagen | delostrelectvo | |
| osoby | Himilkón, Hasdrubal, Syfax, Karthalo, Magón, Filip V. Makedonský, Juba I., Bocchus, Micipsa, Hiempsal, Saburra, Hannibal | Himilco, Astrubal, Syphax, Cartalo, Mago, Philippus Macidonie Rex, Juba, Pochus, Micipsa, Hiemsalem, Sabura, Hannibal | osoby | jména na kartách; Jugurtha a Scipio už v glosáři (doplnit tvary *Juiorta*, *Carnelius Scipio*) |

## Pomocné soubory
Skeny a výřezy jen ve scratchpadu `p7a/` (mimo projekt).
