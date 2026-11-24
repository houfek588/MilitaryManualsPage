# Zadání korektury – Wintzenberger, Beschreibung einer Kriegs-Ordnung (Drážďany 1588)

Platí `PRAVIDLA_PREKLADU.md`, `zdroje/ZADANI_AGENTUM.md` a `kniha.yaml` → `poznamky_k_prekladu`. Strany jsou ve stavu
`prelozeno` (přepis z OCR BSB + překlad od pěti překladatelů, zprávy `zdroje/kontrola/preklad-A…E.md`). Cílem je
**korektura překladu jako celku**: věrnost, plynulost („středně“ – přirozená čeština, ale bez přepisování stylu)
a jednotnost napříč knihou.

## Sjednocení napříč knihou (závazné)
- *Obrister / Oberster / Oberst* = plukovník; jde-li o velitele celého vojska (rady v Prvním dílu, „zu einem Obersten
  erwehlen“), „vrchní velitel“ (odkaz zůstává `{Oberste}`). *oberster Hauptman* = nejvyšší hejtman, *Oberster
  Feldhauptman* = nejvyšší polní hejtman, *KriegsOberster* = válečný plukovník, *Oberste Feldherr* = válečný pán.
- *Kriegsleute* = válečníci, *Kriegsvolck* = válečný lid, *Fenlein* = praporec (u jízdy korouhev), *Fenrich* =
  praporečník, *Feldwebel* = šikovatel, *Leutenampt* = poručík, *Fürer* = vůdce, *Fuhrirer / Vorehrer* = furýr,
  *Befehlsleute / Befehlshaber* = velitelé, *Zeugmeister* = zbrojmistr, *Büchsenmeister* = puškař, *Geschützmeister* =
  dělmistr, *Artalerey* = dělostřelectvo, *Leuffer* = běžci, *fauler hauffen* = líný houf, *gewaltiger hauffen* = hlavní
  houf, *treffen* = střetnutí, *Gegentheil* = protivník, *Potentat* = mocnář, *Flecken* = městečko, *Ringkragen* =
  nákrčník, *Kronen* = koruny, *Vbersoldt* = přeplatek, *erste Blat* = první list.
- *Regiment* jako správa = zřízení, jako útvar = pluk. *Item* = „Dále“ bez dvojtečky (už sjednoceno).
- Soud: *Schultheis* = rychtář, *Richter* (přísedící soudu) = přísedící, *Malefitzrecht* = hrdelní právo, *lange Spies
  Recht* = právo dlouhých pík, *ausweisung* = nález, *Vrtheil* = rozsudek, *Vorsprecher / Redener* = řečník, *Peen* =
  pokuta, *Gerichtswebel* = soudní šikovatel, *Profos* = profous, *Nachrichter* = kat.
- Panovnické tituly: *Key: May: / Röm: Key: May:* = „Jeho (římské) císařské Veličenstvo“ ve správném pádě (např.
  „Jeho římského císařského Veličenstva“, „Jeho Veličenstvu“) – nahraď všechna „Majestát/Majestátu“ (jsou i chybně
  skloňovaná, např. nadpis na `030r`). *Capitulation* = smlouva (ne kapitulace).
- Dvojice `014v`/`015r` (skeny 32–33) je opakovaný snímek `030v`/`031r`: překlad i přepis musí zůstat **totožný**
  (změny v jedné dvojici proveď i ve druhé; obě v dávce C).
- Nadpisy: úroveň 1 = titul, věnování, obsah, První díl, Druhý díl ([26] r); úroveň 2 = kapitoly (pochodový řád,
  ležení, služební list, artikulní list, lodní řád, hrdelní právo, právo dlouhých pík…); úroveň 3 = drobné oddíly,
  otázky a odpovědi soudu.

## Na co se zaměřit
- Porovnej každý blok `cs` s `de` (posuny významu, zápory, slovesné vazby, čísla, částky v tabulkách). Sporná čtení `de`
  ověř ve skenu (návod v `ZADANI_AGENTUM.md`; IIIF `https://api.digitale-sammlungen.de/iiif/image/v2/bsb00032546_000NN/full/1600,/0/default.jpg`).
- Plynulost: rozdělit přetížená souvětí, přirozený slovosled, méně opakování; zachovat tón rad, řádů a přísah.
- Termíny ve složených závorkách `{…}` musí odpovídat tvaru v `de`; nové termíny označ jen u věcně důležitých slov.
- Poznámky: zpřesnit, zbytečné vypustit, neopakovat glosář. Sporná místa ze zpráv překladatelů rozhodni, kde to jde.
- Neměň `overeno_clovekem` (zůstává `false`). Po kontrole `stav: zkontrolovano`. Ukládej stranu po straně.
- Na konci spusť `python -I nastroje/over_strany.py knihy/wintzenberger-1588 <tvoje strany> --prisne` (0 chyb) a napiš
  zprávu `zdroje/kontrola/revize-<dávka>.md` (co jsi změnil, rozhodnutá a dál sporná místa, návrhy do glosáře).
