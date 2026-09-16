---
result_id: R2-GL75-II-T-B-BR-22-RES-003
scope:
  connection: R2
  material: GL75
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: R2-GL75-II-T-B-BR-22-RES-002
n: 6
method: >
  Direkt übernommen aus `R2/COMMON/calculations/2026-06_05_Auswertung_
  Steifigkeiten_Bonded-inRods.xlsx`, Blatt "Überblick", Zelle B95
  ("Mean Anfangssteifigkeit", Versuchsserie "II-T-B-BR-22"), gemäß
  R2-COMMON-DEC-003. Wert ist rechnerisch identisch zur Poolung der
  beiden in RES-002 dokumentierten Teilmittelwerte ("oben" = 742,347
  kN/mm, "unten" = 1.496,644 kN/mm, je n=3): (742,347+1.496,644)/2 =
  1.119,496 kN/mm.
result:
  quantity: Anfangssteifigkeit K_ser einer eingeklebten 2×2-M16-Gewindestangengruppe (gepoolter Mittelwert oben+unten, GL75)
  value: 1119.496
  unit: kN/mm
  original_value: 1119.4956608355833
  original_unit: kN/mm
certainty: MEASURED
---

Kein neuer Rohdatenwert — direkte Übernahme aus der Primärquelle
(Zelle B95 des "Überblick"-Blatts) gemäß R2-COMMON-DEC-003.

Wichtiger Vorbehalt (siehe RES-002): die zugrunde liegende Messreihe
zeigt die mit Abstand größte Streuung aller vier Gruppen — insbesondere
Prüfkörper 2 mit einem extremen Ausreißer bei "unten" (2.554,30 kN/mm,
Verhältnis oben/unten nur 23,55 %). Dieser gepoolte Mittelwert ist
entsprechend mit besonderer Vorsicht zu verwenden, nicht als eng
gesicherter charakteristischer Wert (CLAUDE.md Abschnitt 15). Für GL75
existiert aktuell noch keine Zugseiten-Steifigkeitskette im Excel
(R2-GL75-OPQ-001) — dieser Wert liegt für eine künftige Kette bereit,
ist aber noch nirgends eingesetzt.
