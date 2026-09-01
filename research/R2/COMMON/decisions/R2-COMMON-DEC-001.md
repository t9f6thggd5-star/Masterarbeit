---
decision_id: R2-COMMON-DEC-001
scope:
  connection: R2
  material: COMMON
type: DECISION
question: >
  Auf welcher Norm-Basis wird die Querdruck-Festigkeitsverifikation der
  R2-Rahmenecke (Holzdruck 90° unter der Stahl-Ankerplatte) geführt?
decision: >
  Umstellung der Querdruck-Festigkeitsverifikation von der älteren
  DIN-EN-1995-1-1-Logik (u. a. altes `k_c,90 = 1,75`) auf FprEN
  1995-1-1:2024 als aktuelle Berechnungsgrundlage, sowohl für die
  unverstärkte als auch die ASSY-verstärkte Querdruckprüfung.
reason: >
  Hält die Vorbemessung auf dem aktuellen Normenstand; die alte
  DIN-EN-1995-Logik dient nur noch als Vergleichs-/Sensitivitätsrechnung
  (ETA/Würth-Vergleich, siehe R2-GL24h-DEC-007).
alternatives_considered: >
  Bei der DIN-EN-1995-1-1/Würth-Berechnungsvorlage bleiben (verworfen als
  primäres Modell, aber als Vergleichswert beibehalten).
date: "UNKNOWN (chat-3, seq 150-160; kein genaues Datum überliefert)"
---

Übernommen aus chat-3, DECISIONS.md "Seq 150-160 — Update cross-grain
strength to FprEN". Gilt für R2 materialunabhängig, da sowohl die
GL24h- als auch die GL75-Querdruckrechnung im R2-Excel (Sheets
"Rahmenecke GL24h SD" und "Rahmenecke GL75 SD") dieselbe FprEN-Gleichung
(Gl. 8.5/8.7, Tab. 8.1) referenzieren.
