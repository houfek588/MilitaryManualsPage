# Zpráva z překladu a vizuální revize – `knihy/solms-1559` (Kniha 1, Dávka 4: `1-030r`–`1-039v`)

Zpracováno všech **20 stran** závěrečné dávky První knihy (`1-030r`–`1-039v`, skeny `69`–`88`), včetně celostránkového dřevořezu rozmluvy Starého otce a Syna (`1-034v`, sken `78`) a závěrečné formule První knihy (`1-039v`, sken `88`). Všech 20 stran má nastaveno `stav: prelozeno` a `overeno_clovekem: false`.

Ověření skriptem `python -I nastroje/over_strany.py knihy/solms-1559 1-030r 1-030v 1-031r 1-031v 1-032r 1-032v 1-033r 1-033v 1-034r 1-034v 1-035r 1-035v 1-036r 1-036v 1-037r 1-037v 1-038r 1-038v 1-039r 1-039v --prisne`:
- **20 stran, 0 chyb, 0 varování**.

---

## 1. Přehled změn po stranách

| Strana | List | Sken | Bloky | Pozn. | Hlavní úpravy podle skenů a překlad |
|---|---|---:|---:|---:|---|
| `1-030r` | 30r | 69 | 4 | 1 | `pokracovani: true`, z `1-029v` připojeno celé `haben`, opravy OCR (`mdgen`, `auff chens`→`auffsehens`, `feken`→`setzen`, `Kriegsher ?`→`Kriegsherr`, `regick`→`regirt`, `lap`→`laß`), rozep. `vñ`, `personē`, `neñt`, odstraněna signatura `F`, pozn. k *Commissen*. |
| `1-030v` | 30v | 70 | 2 | 1 | Opravy OCR (`geſakt … zuuer heren`→`gesatzt … zuuerlieren`, `wöl`, `Herrn`, `darbet`→`darbei`), rozděleny 2 odstavce, odstraněn kustod `Kriegs=`, pozn. k *Doctorn noch langen Röcken*. |
| `1-031r` | 31r | 71 | 7 | 1 | `pokracovani: true`, opravy OCR (`Herzen`/`Herz`→`Herren`/`Herr`, `his`→`hitz`, `Lanthuolck`→`Lantßuolck`, `Artoloret`→`Artolorei`), odstraněny záhlaví, signatura `F ij`, rozděleno na 7 bloků; řešen rukopisný vpisek `wider)` nad 1. řádkem v poznámce 1. |
| `1-031v` | 31v | 72 | 5 | 1 | `pokracovani: true`, opravy OCR (`Volkkond`→`Volck vnd`, `mußbreuch`→`mißbreuch`, `disi`→`diß`, `icht`→`nicht`, `ein gang`→`ein gantz`, `seitlang`→`zeitlang`), odstraněn kustod `kriegen`, pozn. k *nicht zu regiren wissen vnd gern thůn* a *nich*. |
| `1-032r` | 32r | 73 | 4 | 1 | `pokracovani: true`, opravy OCR (`voz`→`vor`, `Kriegsfordnung`→`Kriegßordnung`, `darber`→`darbei`, `Colt`→`Solt`), doplněna chybějící lomítka `/`, slovo `vngehorsamer` přesunuto na `1-032v`, odstraněna signatura `F iij`, pozn. k *gehorsan*. |
| `1-032v` | 32v | 74 | 4 | 1 | `pokracovani: true`, připojeno celé `vngehorsamer`, opravy OCR (`fn förcht ond heb`→`jn förcht vnd lieb`, `baft`→`baß`, `Beuelchhleut`→`Beuelchsleut`, `gefaßten`→`gesetzten`), rozep. `eĩn`→`einen`, slovo `verstendigen` přesunuto na `1-033r`, pozn. k *leichfertiger*. |
| `1-033r` | 33r | 75 | 4 | 2 | `pokracovani: true`, připojeno celé `verstendigen`, opravy OCR (`orbittig`→`erbittig`, `Krieghleuten`→`Kriegßleuten`, `Musterplay`→`Musterplatz`, `Finank`→`Finantz`), odstraněna signatura `F iiij`, pozn. k *grauch* a *Kriegßuerstenden*. |
| `1-033v` | 33v | 76 | 5 | 0 | Doplněna ozdobná iniciála `I` (`ITem`), nadpis `uroven: 2` (`Antwort auff der Kriegsleut begern.`), opravy OCR (`imcht`→`nicht`, `Muſterug`→`Musterung`, `Krigfuolck`→`Krigßuolck`), odstraněn kustod `So` (OCR `60`). |
| `1-034r` | 34r | 77 | 2 | 1 | Opravy OCR (`eigen nützig`, `gefprech`→`gesprech`, `onderzicht`→`vnderricht`), nadpis `uroven: 2` pro rozmluvu Starého otce a Syna, odstraněn kustod `Alter`, pozn. k 24 úřadům Druhé knihy. |
| `1-034v` | 34v | 78 | 2 | 0 | Ponechán doprovodný blok popisků nad postavami (`Alter Vatter. Son.` → `Starý otec. Syn.`), doplněn podrobný popis dřevořezu `drevorez-078.jpg`. |
| `1-035r` | 35r | 79 | 10 | 2 | Doplněna ozdobná iniciála `L` (`LIeber`), nadpisy mluvčích `uroven: 3` (`Son.`, `Alter Vatter.`), opravy OCR (`Jeber`→`LIeber`, `inirerzeigt`→`mir erzeigt`, `helt`→`hett`, `mitleit`→`mir leit`, `Con`→`Son.`), odstraněn kustod `vnd`, pozn. k *sagt* a *freundtschafft*. |
| `1-035v` | 35v | 80 | 5 | 2 | `pokracovani: true`, opravy OCR (`mirgent`→`nirgent`, `grof`→`groß`, `Con`→`Son.`), rozděleno 5 bloků (promluvy s nadpisy `uroven: 3`), odstraněn kustod `Alter`, pozn. k *sein* a *vnderrichs*. |
| `1-036r` | 36r | 81 | 14 | 0 | Opravy OCR (`núk`→`nutz`, `1ch`→`ich`, `Batter`→`Vatter`, `wifit`→`wißt`, `oil`→`vil`, `freter`→`freier`), rozděleno 14 bloků (střídání mluvčích s `uroven: 3`), odstraněna signatura `G`. |
| `1-036v` | 36v | 82 | 5 | 1 | `pokracovani: true`, opravy OCR (`wirl`→`wirt`, `micht`→`nicht`, `auſprichten`→`außrichten`, `nißlichs`→`nützlichs`, `Heredein`→`Herr dein`, `Gon`→`Son.`), odstraněn kustod `Son.`, pozn. k přesmyčkám *wirts* a *kömpts*. |
| `1-037r` | 37r | 83 | 4 | 1 | Opravy OCR (`Con`→`Son.`, `anrdsten`→`anrüsten`, `than`→`thůn`, `Xegirungen`→`Regirungen`, doplněny kulaté závorky `(Gott hab lob)`), nadpis `Alter Vatter.` na konci strany jako `uroven: 3`, odstraněna signatura `G ij`, pozn. k *sein*. |
| `1-037v` | 37v | 84 | 3 | 1 | Promluva po nadpisu z `1-037r` (bez `pokracovani: true`), opravy OCR (`mut`→`mit`, `Feldmarschalek`→`Feldmarschalck`, `Artolorcimeister`→`Artoloreimeister`, `jhe`→`jhr`), odstraněn kustod `Des`, pozn. k *nichs*. |
| `1-038r` | 38r | 85 | 5 | 3 | Opravy OCR (`Aimpts`→`Ampts`, `Con`→`Son.`), doplněna lomítka `/`, odstraněn kustod `so` (OCR `٢٥`), poznámky k *Fundierungen*, přesmyčkám *kompts*/*sichts* a tvarům *dirtte*/*leren*. |
| `1-038v` | 38v | 86 | 7 | 1 | `pokracovani: true`, opravy OCR (`bet`→`bei`, `zuthin`→`zuthůn`, `fichts`→`sichst`, `besichts`→`besichst`, `Con`→`Son.`), nadpis `uroven: 2` (`Instruction vnd vnderricht...`), odstraněn kustod `Vor`, pozn. k *kömpts*. |
| `1-039r` | 39r | 87 | 2 | 1 | Doplněna ozdobná iniciála `V` (`VOr`), opravy OCR (`noten`→`nöten`, `rösten`→`rüsten`), doplněna lomítka `/`, odstraněn kustod `stellen.`, pozn. k druhému přikázání první desky Desatera. |
| `1-039v` | 39v | 88 | 7 | 1 | `pokracovani: true`, opravy OCR (`obel`→`vbel`, `obung`→`vbung`), ponechán závěrečný blok První knihy (`Ende des ersten Bůchs.` → `Konec první knihy.`), pozn. k *jhm warheit*. |

---

## 2. Významnější opravy OCR ověřené ze skenů (`s069.jpg`–`s088.jpg`)

- **Ozdobné iniciály**:
  - `1-033v` (`s076.jpg`): `Tem` → `ITem` (velké zdobené `I` + `Tem`).
  - `1-035r` (`s079.jpg`): `Jeber` → `LIeber` (velké zdobené `L` + `Ieber`).
  - `1-039r` (`s087.jpg`): `Or` → `VOr` (velké zdobené `V` + `Or`).
- **Záměny smyslu v OCR**:
  - `1-030r` (`s069.jpg`): `auff chens` → `auffsehens`; `feken` → `setzen`; `prer` → `jrer`; `Kriegsher ?` → `Kriegsherr`; `regick` → `regirt`; `lap` → `laß`.
  - `1-030v` (`s070.jpg`): `geſakt … zuuer heren` → `gesatzt … zuuerlieren` (zásadní obrat významu!); `darbet` → `darbei`; `zuhahen … set` → `zuhaben … sei`.
  - `1-031r` (`s071.jpg`): soustavná záměna `Herꝛ`/`Herꝛen` za `Herz`/`Herzen`; `his` → `hitz`; `Lanthuolck` → `Lantßuolck`; `Schakung` → `Schatzung`; `Artoloret` → `Artolorei`.
  - `1-031v` (`s072.jpg`): `Volkkond` → `Volck vnd`; `mußbreuch` → `mißbreuch`; `disi` → `diß`; `icht` → `nicht` (zásadní obrat významu!); `ein gang` → `ein gantz`; `seitlang` → `zeitlang`.
  - `1-032r` (`s073.jpg`): `voz` → `vor`; `Kriegsfordnung` → `Kriegßordnung`; `darber` → `darbei`; `Colt` → `Solt`.
  - `1-032v` (`s074.jpg`): `fn förcht ond heb` → `jn förcht vnd lieb`; `baft` → `baß`; `Beuelchhleut` → `Beuelchsleut`; `gefaßten` → `gesetzten`; `in ein Artickel` → ve skenu se zkracovací čárkou `eīn` → `einen Artickel`.
  - `1-033r` (`s075.jpg`): `orbittig` → `erbittig`; `Krieghleuten` → `Kriegßleuten`; `Musterplay` → `Musterplatz`; `Finank` → `Finantz`.
  - `1-033v` (`s076.jpg`): `imcht` → `nicht`; `Muſterug` → ve skenu se zkracovací čárkou `Muſterūg` → `Musterung`; `Krigfuolck` → `Krigßuolck`.
  - `1-035r` (`s079.jpg`): `inirerzeigt` → `mir erzeigt`; `helt` → `hett`; `mitleit` → `mir leit`; `Con .` → `Son.`.
  - `1-035v` (`s080.jpg`): `mirgent` → `nirgent`; `Xath` → `Rath`; `grof` → `groß`.
  - `1-036r` (`s081.jpg`): `núk` → `nutz`; `1ch` → `ich`; `Batter` → `Vatter`; `wifit` → `wißt`; `oil` → `vil`; `rickging` → `rück ging`; `freter` → `freier`.
  - `1-036v` (`s082.jpg`): `wirl` → `wirt`; `micht` → `nicht`; `auſprichten` → `außrichten`; `nißlichs` → `nützlichs`; `Heredein` → `Herr dein`; `Gon .` → `Son.`.
  - `1-037r` (`s083.jpg`): `anrdsten` → `anrüsten`; `than` → `thůn`; `Xegirungen` → `Regirungen`; závorka `>` → `)`.
  - `1-037v` (`s084.jpg`): `mut` → `mit`; `Feldmarschalek` → `Feldmarschalck`; `Artolorcimeister` → `Artoloreimeister`; `jhe` → `jhr`.
  - `1-038r` (`s085.jpg`): `Aimpts` → `Ampts`; kustod `٢٥` → `so`.
  - `1-038v` (`s086.jpg`): `zuthin` → `zuthůn`; `fichts` → `sichst`; `besichts` → `besichst`; `rúhe ists` → `růhe ist /`.
  - `1-039r` (`s087.jpg`): `noten` → `nöten`; `rösten` → `rüsten`.
- **Návaznost před začátkem dávky (`1-029v` → `1-030r`)**: V `1-029v.yaml` (mimo tuto dávku, ponecháno beze změny) zůstal na konci rozdělený začátek slova `ha` a kustod `ben`, zatímco celé slovo `haben` bylo v souladu s pravidly přeneseno na začátek `1-030r.yaml`. Doporučujeme při zpracování Dávky 3 konec `1-029v.yaml` upravit na `einen freien zugang`.

---

## 3. Sporná místa DE + CS k rozhodnutí

1. **`1-031r` (sken `71`) – tisková chyba `das ist einem Herren zurathen` a rukopisný vpisek `wider)`**:
   - **DE**: `Kriegßuolck ist / das ist einem Herren zurathen / dann es fert kein Herr wol damit`
   - **CS**: `válečným lidem {Kriegßuolck} – to pánovi [nelze] radit,[^1] neboť žádný pán s tím nepochodí dobře`
   - **Poznámka**: V tisku zjevně vypadl zápor *nit* nebo předpona *wider-*. Nad záhlavím `Von Kriegßregirung` přímo nad slovem `zurathen` dopsal starý čtenář rukou `wider)` (tj. *widerrathen* = odrazovat, zrazovat). V `de` je ponecháno tištěné znění, v `cs` význam opraven doplňkem v hranatých závorkách a vysvětlen v poznámce.
2. **`1-031v` – `die versehung nicht zu regiren wissen vnd gern thůn`**:
   - **CS**: `ale správu zastávat neumějí, a přece se k ní rádi mají.[^1]`
   - **Poznámka**: Možná interpretace elipsy záporu (*a neradi pracují*), případně kontrastu (*a přece se k ní rádi hlásí*). Vysvětleno v poznámce 1.
3. **`1-032r`, `1-032v`, `1-033r`, `1-035r`, `1-035v`, `1-036v`, `1-037r`, `1-037v`, `1-038r`, `1-038v`, `1-039v` – drobné tiskové odchylky**:
   - Zachovány v `de` a vysvětleny v poznámkách: `gehorsan` (`1-032r`), `leichfertiger` (`1-032v`), `grauch` a `Kriegßuerstenden` (`1-033r`), `sagt` (`1-035r`), `sein` za *bin* (`1-035v`, `1-037r`) a `vnderrichs` (`1-035v`), přesmyčky `wirts`/`kömpts`/`kompts`/`sichts`/`dirtte` (`1-036v`, `1-038r`, `1-038v`), `nichs` (`1-037v`), `jhm warheit` za *inn warheit* (`1-039v`).
4. **`1-038r` – `Fundierungen`**:
   - **DE**: `als auff die Wachten / Warten / Fundierungen / Scharmützel besichtigung zuthůn`
   - **CS**: `jako na stráže {Wachten}, hlídky, průzkumy,[^1] konat obhlídky šarvátek`
   - **Poznámka**: Slovo *Fundierungen* může být tiskařskou záměnou za *Futerungen* (pícování) či *Kundierungen* (výzvědy, průzkumy), případně jde o vyměřování a zakládání stanovišť/postavení. Přeloženo jako *průzkumy* s poznámkou.
5. **`1-039r` – `im andern Gebot der ersten Tafeln`**:
   - **CS**: `ve druhém přikázání první desky[^1]`
   - **Poznámka**: Odkaz na druhé přikázání Desatera podle tehdejšího luterského i katolického členění (nezneužívat Boží jméno nadarmo – Ex 20,7; Dt 5,11).

---

## 4. Návrhy do glosáře (`knihy/solms-1559/glosar.yaml`)

### A. Nové varianty ke stávajícím heslům
- `nejvyssi-polni-hejtman`: doplnit do `de`: `Kriegs Oberster`, `Kriegßobersten` (`1-037v`)
- `zbrojmistr`: doplnit do `de`: `Artoloreimeister` (`1-037v`, `1-038r`)
- `komis`: doplnit do `de`: `Commissen` (`1-030r`)
- `verejny-rad`: doplnit do `de`: `Polliceien` (`1-038r`)
- `pluk`: doplnit do `de`: `Regimenten` (`1-033v`)
- `zavazek`: doplnit do `de`: `pflicht` (`1-039r`)
- `zbroj`: doplnit do `de`: `rüstung` (`1-030v`, `1-031r`)
- `soud`: doplnit do `de`: `Justitien` je již v hesle; zvážit rozdělení/upřesnění, zda *Justitien* v obecném významu „spravedlnost / soudnictví“ nemá mít vlastní heslo `spravedlnost` (v edici `solms-1559` se překládá převážně jako `spravedlnost {Justitien}`).

### B. Návrhy nových hesel
```yaml
- id: zemsky-lid
  cs: zemský lid
  de:
  - Landtuolck
  - Lantßuolck
  - landtuolck
  kategorie: jednotky
  pozn: Domácí branná hotovost poddaných a obyvatel země (na rozdíl od najatých cizích žoldnéřů).

- id: berne
  cs: berně
  de:
  - Schatzung
  kategorie: zold
  pozn: Mimořádná zemská daň či válečný poplatek vybíraný od poddaných.

- id: polni-hlidka
  cs: hlídka
  de:
  - Warten
  kategorie: sluzba
  pozn: Pozorovací stanoviště nebo předsunutá polní hlídka (Warte).
```
