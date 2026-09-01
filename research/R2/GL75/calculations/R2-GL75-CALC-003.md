---
calculation_id: R2-GL75-CALC-003
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data:
  assumptions:
method: >
  Aufnehmbares Moment am Rahmeneck-Innenknoten aus dem inneren Hebelarm
  `z` und der für GL75 maßgebenden Zug-/Druckkomponente: `M_max =
  F_maßgebend · z`. Für GL75 wird als maßgebende Komponente die
  Gewindestangen-Zugtragfähigkeit (Versuchsmittel) eingesetzt, nicht die
  (deutlich höhere) unverstärkte Querdrucktragfähigkeit.
equations: M = F·z (Kräftepaar-Modell, kein FprEN-Gleichungsverweis im Excel angegeben).
result:
  quantity: Aufnehmbares Moment M_max, GL75 (maßgebende Komponente Gewindestangenzug)
  value: 162.962
  unit: kNm
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL75 SD", Zellen G74-I87 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01)
certainty: CALCULATED
superseded_by:
---

Eigenständig aus der R2-Excel-Datei erschlossen (nicht in chat-3
besprochen, siehe R2-COMMON-OPQ-008).

**Kette:** innerer Hebelarm `z=560 mm` (I77/I79, identisch zu GL24h),
maßgebende Zug-/Druckkomponente `I85=291,003 kN` (entspricht exakt dem
Gewindestangen-Zugversuchsmittel `II-T-B-BR-22`, siehe
R2-GL75-II-T-B-BR-22-RES-001 — NICHT der unverstärkten
Querdrucktragfähigkeit `1.031,65 kN` aus R2-GL75-CALC-002), `M_max =
291,003×0,560 = 162,962 kNm` (I87).

**Zum Vergleich GL24h vs. GL75 (siehe auch R2-GL24h-CALC-008):** Bei
GL24h wird die (kleinere) verstärkte Querdrucktragfähigkeit
(`248,85 kN`) als maßgebend gesetzt, bei GL75 die (kleinere)
Gewindestangen-Zugtragfähigkeit (`291,00 kN`, da die unverstärkte
Querdrucktragfähigkeit von GL75 mit `1.031,65 kN` weit darüber liegt und
für GL75 im Excel ohnehin keine ASSY-Verstärkung modelliert ist, siehe
R2-GL75-OPQ-002). Der bemessungskritische Versagensmechanismus
verschiebt sich damit materialabhängig von Querdruckversagen (GL24h) zu
Gewindestangen-Zugversagen (GL75) — eine plausible Folge der massiv
höheren Querdruckfestigkeit von BauBuche. Diese Einordnung ist eine
eigene Interpretation (Claude) auf Basis der Zellwerte, noch nicht vom
Forschenden bestätigt.

Nachgelagert im selben Block: "Zylinderkraft"-Abschnitt (Hebelarm 3,03 m,
`V_ed je Seite=38,03 kN`, `Z_ed,ges=53,78 kN`, Zellen I94-I96) — wie bei
GL24h vermutlich eine Rückrechnung auf die Prüfstands-Aktuatorkraft,
nicht in chat-3 erläutert (siehe R2-COMMON-OPQ-008).
