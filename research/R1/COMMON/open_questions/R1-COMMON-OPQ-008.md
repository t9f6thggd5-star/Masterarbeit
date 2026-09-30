---
open_question_id: R1-COMMON-OPQ-008
scope:
  connection: R1
  material: COMMON
status: OPEN
question: >
  Ist für das Federmodell die Steifigkeit der Erstbelastung (K_ser,
  0,1–0,4·F_est) oder die Wiederbelastungssteifigkeit K_e maßgebend? Und wird
  der Anfangsschlupf bei der Verdrehung und dem Maschinenweg bei Höchstlast
  berücksichtigt?
context: >
  GL24h: K_ser = 279,52 kN/mm, K_e = 734,17 kN/mm je 2×8-Gruppe (Faktor
  2,6). Projektweit gilt bisher K_ser (COMMON-COMMON-DEC-006). Die Vorgabe
  der Betreuung (Lastfenster 0,1/0,4·F_est wegen Hysterese, linear-elastisch,
  kein Anfangsschlupf) lässt beide Lesarten zu. Anfangsschlupf im Mittel
  0,28 mm je Gruppe, entspricht ≈ 1,0 mrad Eckverdrehung
  (R1-GL24h-CALC-010); vorerst getrennt ausgewiesen (R1-GL24h-DEC-011).
related_sources:
options_considered:
date_opened: "2026-09-26"
date_resolved:
resolution:
---

**Korrektur (2026-09-30):** Nicht Teil der E-Mail an die Betreuung vom
2026-09-26 (diese enthielt nur die Fragen zu Tragfähigkeit/Gruppendrehung,
c_br,par und Hebelarm, siehe R1-COMMON-OPQ-005/006/007).

**Update (2026-09-30), Nutzerentscheidung:** Der Anfangsschlupf wird bei Φ
und u_M mitgerechnet. Ob K_ser oder K_e verwendet wird, wird
situationsbedingt festgelegt; für die Hüllkurve (monotone Erstbelastung)
ist die Erstbelastungskurve maßgebend. Status bleibt OPEN für die
situationsbedingte Wahl K_ser/K_e.
