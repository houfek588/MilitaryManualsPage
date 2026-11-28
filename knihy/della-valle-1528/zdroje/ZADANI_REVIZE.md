# Zadání korektury – Battista della Valle, Vallo (Benátky 1528)

Platí `PRAVIDLA_PREKLADU.md`, `zdroje/ZADANI_AGENTUM.md` (hlavně **ORIGINÁL JE ITALSKY** a přepis ze skenu) a
`kniha.yaml` → `poznamky_k_prekladu`. Všech 158 stran je ve stavu `prelozeno` (přepis ze skenu + překlad od sedmi
překladatelů, zprávy `zdroje/kontrola/preklad-A…G.md`). Cílem je **korektura překladu jako celku**: věrnost
italskému originálu, plynulost („středně“) a jednotnost napříč knihou.

## Sjednocení napříč knihou (závazné)
- Vojsko: *milite* = voják, *militia* = vojenství / válečné řemeslo, *capitano* = kapitán, *colonello* = plukovník,
  *sergente / sargente* = šikovatel, *caporale* = desátník, *alfiere* = praporečník, *bandera* = prapor,
  *lanze spezate* = „lance spezzate“ (ponech italsky, glosář vysvětluje), *fantaria* = pěchota, *huomo d'arme* = kyrysník,
  *cauallo leggiero* = lehký jezdec, *scopettero* = ručničář, *scopetto* = ručnice, *archibuso* = arkebuza,
  *picca* = píka (muži = pikenýři), *guardia* = stráž, *sopra guardia* = vrchní stráž (obchůzka), *nome* = heslo,
  *scolta* = hlídka.
- Šiky: *battaglione* = bataillon, *battaglia* = šik (v boji „útok“ / „bitva“ podle smyslu), *filaro / filare* = řada,
  *piaza* = prostranství (v šiku), *fronte* = čelo, *schino* = týl, *fianco* = bok, *ala* = křídlo, *lunetta* =
  půlměsíc, *triangolo* = trojúhelník, *quadrangolo* = čtyřúhelník, *forfece* = nůžky, *scorpione* = štír,
  *spicolo* = hrot. Číselné řady nad obrazci (např. „o.4.5.25.“) přepiš podle tisku a vyklad ponech v poznámce
  podle šifry z kap. XLI (050r); „5“ v řadách = písmeno p. (partire).
- Opevnění a dobývání: *bastione* = bašta, *riparo* = záštita, *gabione* = koš, *candonera* = střílna, *trenciera* =
  zákop, *caua* = mina, *scala* = žebřík, *ponte* = most, *argano* = rumpál, *modello* = stroj, *chiaue* = kotva,
  *terra / cità* = město.
- Oheň: *artificio de fuoco* = ohňostrojná (zápalná) zbraň, *tromba de fuoco* = ohnivá trouba, *pignata* = ohnivý
  hrnec, *mistura* = zápalná směs, *stoppino* = doutnák, *salnitro / salmitro* = ledek, *polvere* = prach.
- Kniha IV (čest a souboj): *disfida / desfida* = výzva (k souboji), *cartello* = vyzývací list, *actore* = vyzyvatel,
  *reo / desfidato* = vyzvaný, *padrino* = sekundant, *mentita* = obvinění ze lži („lžeš“), *iniuria* = urážka,
  *querela / lite* = spor, *caualiero* = rytíř, *campo franco / steccato* = kolbiště, *ad tutta oltranza* = na smrt,
  *pingere / depingere* = potupně vymalovat, *reportatore* = donašeč, *poltrone* = zbabělec, *traditore* = zrádce.
- Nadpisy: kniha = úroveň 1, kapitola = 2 („Jak udělat bataillon o třech stech pikách. Kapitola XVI.“ – číslo kapitoly
  podle tisku, římskými číslicemi). Chyby v číslování kapitol (XXVIII dvakrát, chybějící XXX a XXXII, „Ca.XI.“ za XL)
  ponech podle tisku s poznámkou.

## Na co se zaměřit
- Porovnej každý blok `cs` s italským `de`; **italský přepis ověř ve skenu** (překladatelé četli ze skenu, ale mohli
  se splést – hlavně čísla, zkratky a slabě otištěná místa). Hranice stran: slovo rozdělené přes stranu patří na
  stranu, kde končí.
- Plynulost: rozděl přetížená souvětí; zachovej tón praktické vojenské příručky (a v knize IV právnického kodexu cti).
- `{…}` jen u věcných termínů v italské podobě z tisku, při prvním výskytu na stránce; u obecných slov (campo, terra,
  testa, corda…) závorky odstraň, pokud nejde o termín. Glosář `glosar.yaml` je závazný.
- Obrázky: výřezy `obrazky/drevorez-*.jpg` otevři a ověř, že `popis` odpovídá (počty řad a mužů, nápisy).
- Poznámky: zpřesnit, zbytečné vypustit, neopakovat glosář. Sporná místa ze zpráv překladatelů rozhodni, kde to jde.
- Neměň `overeno_clovekem` (zůstává `false`). Po kontrole `stav: zkontrolovano`. Ukládej stranu po straně.
- Na konci `python -I nastroje/over_strany.py knihy/della-valle-1528 <tvoje strany> --prisne` (0 chyb) a zpráva
  `zdroje/kontrola/revize-<dávka>.md` (co jsi změnil, rozhodnutá a dál sporná místa, návrhy do glosáře).
