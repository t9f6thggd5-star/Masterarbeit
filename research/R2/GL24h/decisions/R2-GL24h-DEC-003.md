---
decision_id: R2-GL24h-DEC-003
scope:
  connection: R2
  material: GL24h
type: DECISION
question: >
  Nach welcher FprEN-Materialklasse wird die unverstärkte
  Querdruckfestigkeit von GL24h verifiziert?
decision: >
  GL24h wird als SWB (Solid Wood-Based) klassifiziert; für den
  unverstärkten Fall A wird `k_mat = 1,4` angesetzt.
reason: >
  Konventionelles Brettschichtholz fällt unter die SWB-Klassifikation
  der FprEN 1995-1-1:2024.
alternatives_considered:
date: "UNKNOWN (chat-3, seq 160-168; kein genaues Datum überliefert)"
---

Übernommen aus chat-3, DECISIONS.md "Seq 160-168 — SWB / k_mat". Ergebnis:
unverstärkte FprEN-Querdrucktragfähigkeit `F_v,R ≈ 224,29 kN`
(R2-GL24h-CALC-005).

**Wichtiger Vorbehalt:** Diese Entscheidung gilt ausdrücklich nur für
GL24h. chat-3 selbst hatte die SWB-Klassifikation testweise auch auf GL75
angewendet ("GL24h (and GL75 if it is GL)") — das ist durch
COMMON-COMMON-DEC-004 inzwischen widerlegt: GL75 ist als BauBuche/hardwood
GLVL zu behandeln, nicht als SWB. Ob der bestehende
Querdruck-Festigkeitsnachweis im R2-Excel für GL75 dieselben `k_mat`/
`k_c,90`-Werte trotzdem unverändert übernehmen darf, ist offen — siehe
R2-GL75-OPQ-003.
