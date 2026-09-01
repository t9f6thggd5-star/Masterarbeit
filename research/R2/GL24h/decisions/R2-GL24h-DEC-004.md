---
decision_id: R2-GL24h-DEC-004
scope:
  connection: R2
  material: GL24h
type: DECISION
question: >
  Wie wird die querdruckverstärkte (ASSY-Schrauben) Widerstandsseite
  berechnet — als eigenständige FprEN-Gleichung oder als Summe aus
  unverstärktem Widerstand und Schraubenanteil?
decision: >
  Es wird die dedizierte FprEN-Gleichung für die verstärkte
  Querdrucktragfähigkeit (Gl. 8.12) verwendet, nicht "unverstärkter
  Widerstand + Schraubenanteil".
reason: >
  Die verstärkte Gleichung hat einen eigenen Holzanteil-Term und einen
  zweiten Versagensmodus (Ebene der Schraubenspitze); eine einfache
  Summe würde günstige Lastausbreitungseffekte doppelt berücksichtigen.
alternatives_considered: >
  Unverstärkter FprEN-Widerstand (`≈224,29 kN`) plus 9×Schraubenanteil
  addieren — ausdrücklich verworfen (chat-3, REQUIREMENTS.md, "Rejected
  or superseded approaches").
date: "UNKNOWN (chat-3, seq 168-175; kein genaues Datum überliefert)"
---

Übernommen aus chat-3, DECISIONS.md "Seq 168-175 — Reinforced FprEN
model". Umgesetzt in R2-GL24h-CALC-006: Holzanteil `≈143,24 kN`
(Excel-Zelle H104) + Schraubenanteil `9×11,73 kN = 105,61 kN`
(Zelle H105) → `F_R1 ≈ 248,85 kN` (Zelle H106), zweiter Modus
`F_R2 ≈ 413,79 kN` (Zelle H107), maßgebend `F_c,90 ≈ 248,85 kN`
(Zelle H109, Gl. 8.12).
