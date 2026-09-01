---
decision_id: R2-GL24h-DEC-006
scope:
  connection: R2
  material: GL24h
type: DECISION
question: >
  Welcher Ausziehfestigkeits-/Knickwert wird je ASSY-Verstärkungsschraube
  für die Bemessung angesetzt?
decision: >
  Der produktspezifische ETA-Wert `f_y,k = 900 N/mm²` (ETA-11/0190) wird
  für die Schrauben-Knicktragfähigkeit verwendet; die daraus berechnete
  Knicktragfähigkeit `F_c = 11,73 kN` je Schraube wird als maßgebend
  festgelegt (Knicken governiert vor Ausziehen).
reason: >
  `F_c = 11,73 kN` (Knicken) < `F_w,k ≈ 73,55 kN` (Ausziehen nach FprEN
  generischem Modell) — Knicken ist der kritische Versagensmodus je
  Schraube.
alternatives_considered:
date: "UNKNOWN (chat-3, seq 182-188; kein genaues Datum überliefert)"
---

Übernommen aus chat-3, DECISIONS.md "Seq 182-188 — Screw buckling". Gegen
R2-Excel verifiziert: `f_y,k=900` (Zelle H75, Quelle "ETA 11/0190"),
Knicktragfähigkeit `F_c=11,734 kN` (Zelle H103, FprEN Gl. 11.5), siehe
Herleitungskette in R2-GL24h-CALC-007. Ausziehwiderstand `F_w,k≈73,55 kN`
in Zelle H94 (FprEN Gl. 11.3).
