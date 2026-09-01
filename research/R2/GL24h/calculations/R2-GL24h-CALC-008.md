---
calculation_id: R2-GL24h-CALC-008
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data:
  assumptions:
method: >
  Aufnehmbares Moment am Rahmeneck-Innenknoten aus dem inneren Hebelarm
  `z` (Abstand Zug- zu Druckkraftresultierende) und der maßgebenden
  Zug-/Druckkomponente der Verbindung: `M_max = F_maßgebend · z`.
equations: M = F·z (Kräftepaar-Modell, kein FprEN-Gleichungsverweis im Excel angegeben).
result:
  quantity: Aufnehmbares Moment M_max, GL24h (maßgebende Komponente Querdruck verstärkt)
  value: 139.354
  unit: kNm
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen F113-H133 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01)
certainty: CALCULATED
superseded_by: R2-GL24h-CALC-012
---

Eigenständig aus der R2-Excel-Datei erschlossen (nicht in chat-3
diskutiert) — Zweck/Herleitung dieses Blocks ("innerer Hebelarm
Rahmeneck"/"maximales Moment"/"Zylinderkraft") ist nicht durch chat-3
belegt, siehe R2-COMMON-OPQ-008. Die reine Rechenkette ist jedoch
nachvollziehbar und wird hier dokumentiert.

**Kette:** innerer Hebelarm `z=560 mm` (H116/H118, "Abstand Zugkraft zu
Druckkraft"), maßgebende Zug-/Druckkomponente `H123=248,846 kN`
(entspricht exakt der verstärkten Querdrucktragfähigkeit aus
R2-GL24h-CALC-006, Zelle H109 — nicht dem Gewindestangen-Zugversuchs-
mittel), `M_max = 248,846×0,560 = 139,354 kNm` (H125).

**Bemerkenswert:** Für GL75 wird an derselben Stelle im Excel die
Gewindestangen-Zugtragfähigkeit (`291,00 kN`) statt der
Querdrucktragfähigkeit als maßgebende Komponente eingesetzt (siehe
R2-GL75-CALC-003) — d. h. die Excel-Datei wählt je Material offenbar den
jeweils kleineren der beiden Widerstände (Querdruck vs.
Gewindestangenzug) als "maßgebende Komponente". Für GL24h ist das der
Querdruckwiderstand (`248,85 kN < 285,77 kN`
Zugversuchsmittel), für GL75 der Gewindestangenzug
(`291,00 kN < 1.031,65 kN` unverstärkter Querdruckwiderstand) — der
maßgebende Versagensmechanismus verschiebt sich also materialabhängig.
Diese Beobachtung ist eine eigene Interpretation (Claude) auf Basis der
Zellwerte, nicht aus chat-3 übernommen, und noch nicht vom Forschenden
bestätigt.

Nachgelagert im selben Excel-Block: "Zylinderkraft"-Abschnitt (Hebelarm
3,03 m, `V_ed je Seite=32,52 kN`, `Z_ed,ges=45,99 kN`, Zellen H131-H133)
— vermutlich eine Rückrechnung auf die erforderliche Prüfstands-
Aktuatorkraft, aber ebenfalls nicht in chat-3 erläutert (siehe
R2-COMMON-OPQ-008).

**Korrektur (2026-09-01):** Der hier verwendete Wert `H109=248,846 kN`
wurde in R2-GL24h-CALC-011 korrigiert (`k_mat`-Fehler, richtig:
`384,124 kN`). Dadurch ändert sich auch, welcher der drei
MIN-Kandidaten (`H40`, `H52`, `H109`) für `H123` maßgebend wird — siehe
R2-GL24h-CALC-012 für die korrigierte Kette und den resultierenden
Wechsel der maßgebenden Komponente (Querdruck verstärkt →
Gewindestangen-Zugversuchsmittel).
