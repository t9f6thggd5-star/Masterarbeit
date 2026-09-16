---
result_id: R2-GL75-II-T-B-BR-11-RES-003
scope:
  connection: R2
  material: GL75
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: R2-GL75-II-T-B-BR-11-RES-002
n: 6
method: >
  Direkt übernommen aus `R2/COMMON/calculations/2026-06_05_Auswertung_
  Steifigkeiten_Bonded-inRods.xlsx`, Blatt "Überblick", Zelle B94
  ("Mean Anfangssteifigkeit", Versuchsserie "II-T-B-BR-11"), gemäß
  R2-COMMON-DEC-003. Wert ist rechnerisch identisch zur Poolung der
  beiden in RES-002 dokumentierten Teilmittelwerte ("oben" = 225,442
  kN/mm, "unten" = 227,751 kN/mm, je n=3): (225,442+227,751)/2 =
  226,596 kN/mm. Ob "oben"/"unten" hier — wie für GL24h vom Nutzer
  bestätigt (siehe R2-GL24h-II-T-S-BR-11-RES-002, Update) — ebenfalls
  zwei separate, unabhängig eingeklebte Klebefugen sind, wurde für die
  GL75-Serien nicht gesondert nachgefragt, aber als naheliegend
  angenommen (identischer Versuchsaufbau lt. Blatt "Überblick").
result:
  quantity: Anfangssteifigkeit K_ser einer eingeklebten Einzelstange (gepoolter Mittelwert oben+unten, GL75)
  value: 226.596
  unit: kN/mm
  original_value: 226.59626030700176
  original_unit: kN/mm
certainty: MEASURED
---

Kein neuer Rohdatenwert — direkte Übernahme aus der Primärquelle
(Zelle B94 des "Überblick"-Blatts) gemäß R2-COMMON-DEC-003. Für GL75
existiert aktuell noch keine Zugseiten-Steifigkeitskette im Excel
(R2-GL75-OPQ-001) — dieser Wert liegt für eine künftige Kette bereit,
ist aber noch nirgends eingesetzt. Nahezu identisch zum GL24h-Wert
derselben Serie (203,303 kN/mm, R2-GL24h-II-T-S-BR-11-RES-003) — bereits
in RES-002 als Beobachtung vermerkt, dass diese Kenngröße primär vom
Stahl/der Verklebung, nicht vom umgebenden Holzwerkstoff abzuhängen
scheint.
