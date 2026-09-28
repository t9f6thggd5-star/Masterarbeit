---
decision_id: R2-COMMON-DEC-005
scope:
  connection: R2
  material: COMMON
type: DECISION
question: >
  Welcher Anfangsschlupf φ_S wird für R2 (GL24h und GL75) in der
  Übersichtstabelle (COMMON-COMMON-DEC-008) angesetzt?
decision: >
  φ_S = 0 für R2/GL24h und R2/GL75.
reason: >
  Auswertung der Zugversuche II-T-S-BR-22-1 bis -3 (GL24h) und
  II-T-B-BR-22-1 bis -3 (GL75), je 6 Kurven (oben/unten), nach
  v0 = v01 − F01/K_ser (EN 26891; K_ser = Sekante F01–F04, Zellen M21/S21):
  GL24h v0 = 0,036 / −0,053 / −0,006 / 0,006 / −0,014 / 0,027 mm,
  Mittel −0,001 mm; GL75 v0 = −0,037 / −0,005 / 0,047 / −0,028 /
  −0,036 / 0,004 mm, Mittel −0,009 mm. Die Werte streuen um null
  (negativer Schlupf ist physikalisch nicht möglich), liegen im Bereich
  der Messauflösung und sind mit eingeklebten Stangen ohne Lochspiel
  plausibel. Nutzerentscheidung (Chat, 2026-09-28). Schlupf aus dem
  Setzen der Ankerplatte vorerst nicht angesetzt (R2-COMMON-ASS-007,
  R2-COMMON-OPQ-012).
alternatives_considered: >
  Mittelwerte direkt ansetzen (negativ, physikalisch nicht sinnvoll);
  Betrag als Obergrenze ansetzen (≤ 0,05 mm → φ_S ≤ 0,09 mrad mit
  φ_S = v0/z, z = 560 mm; vernachlässigbar gegenüber φ_el ≈ 10–13 mrad).
date: "2026-09-28"
superseded_by:
---

**Prüfung der Auswertungsdatei** `R2/COMMON/calculations/2026-06_05_Auswertung_Steifigkeiten_Bonded-inRods.xlsx`
nach COMMON-COMMON-DEC-007 (Claude, 2026-09-28), Blätter BR-22 GL24h und GL75:

- Spalten I = (03+04)/2 („oben“) und J = (01+02)/2 („unten“): Formel in allen
  Zeilen aller 6 Blätter korrekt.
- Zeiger V11–V16 (F01, F04, F14, F11, F21, F24) sitzen richtig, höchstens eine
  Zeile daneben (ohne Einfluss).
- K_ser = M21/S21, Mittel der 6 Kurven: GL24h 862,53 kN/mm (= R2-GL24h-II-T-S-BR-22-RES-003),
  GL75 1119,50 kN/mm.
- Rohdichte der Vergleichsformeln (AF14) richtig: 420 bzw. 800 kg/m³.
- F_est = 260 kN in allen Blättern (GL24h und GL75), F_max 282–291 kN; gegen das
  Prüfprogramm noch abzugleichen.
- F_max (M6) ist von Hand eingetragen und liegt 0,4–1,0 kN über dem Maximum der
  Kraftspalte (gleiches Muster wie bei R1).
- Die Verschiebungen im Lastfenster sind sehr klein (v04 = 0,01–0,28 mm), mehrere
  v01 negativ; die große Streuung von K_ser (GL24h 419–1440, GL75 484–2554 kN/mm)
  ist damit mindestens teilweise durch die Messauflösung erklärbar.
