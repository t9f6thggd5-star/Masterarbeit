---
result_id: R2-GL24h-II-T-S-BR-11-RES-003
scope:
  connection: R2
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: R2-GL24h-II-T-S-BR-11-RES-002
n: 6
method: >
  Direkt übernommen aus `R2/COMMON/calculations/2026-06_05_Auswertung_
  Steifigkeiten_Bonded-inRods.xlsx`, Blatt "Überblick", Zelle B96
  ("Mean Anfangssteifigkeit", Versuchsserie "II-T-S-BR-11"), gemäß
  R2-COMMON-DEC-003. Wert ist rechnerisch identisch zur Poolung der
  beiden in RES-002 dokumentierten Teilmittelwerte ("oben" = 205,360
  kN/mm, "unten" = 201,246 kN/mm, je n=3): (205,360+201,246)/2 =
  203,303 kN/mm.
result:
  quantity: Anfangssteifigkeit K_ser einer eingeklebten Einzelstange (gepoolter Mittelwert oben+unten, GL24h)
  value: 203.303
  unit: kN/mm
  original_value: 203.30293172195255
  original_unit: kN/mm
certainty: MEASURED
---

Kein neuer Rohdatenwert — direkte Übernahme aus der Primärquelle
(Zelle B96 des "Überblick"-Blatts) gemäß R2-COMMON-DEC-003, unabhängig
gegengerechnet gegen die Poolung der RES-002-Teilmittelwerte (siehe
`method`). Die in RES-002 dokumentierte Streuung zwischen den drei
Prüfkörpern bleibt bestehen und wird hier nicht reduziert.

Bisher nicht in eine Steifigkeitskette eingesetzt — der Nutzer hat
entschieden, für die R2/GL24h-Zugseiten-Kette ausschließlich auf die
BR-22-Ergebnisse (vier Stangen) zurückzugreifen, siehe
R2-GL24h-II-T-S-BR-22-RES-003 und R2-GL24h-CALC-014.
