---
decision_id: R1-GL24h-DEC-011
scope:
  connection: R1
  material: GL24h
type: DECISION
question: >
  Wie werden die Last-Verschiebungs-Kurven der Zugversuche I-T-S-SD-28-1 bis -3
  aufbereitet, um die Verdrehung der Rahmenecke bei Höchstlast nichtlinear
  (Variante 3) statt nur linear mit C_rot,tot zu bestimmen?
decision: >
  (1) Hüllkurve je Gruppe (oben/unten, 6 Kurven): Erstbelastung bis F04
  (= Höchstwert der Erstbelastung, wie im Auswerteblatt), Entlastungs-/
  Wiederbelastungsschleife nach EN 26891 entfällt, ab Wiederbelastung auf F04
  weiter bis F_max. (2) Anfangsschlupf je Kurve nach EN 26891 abziehen
  (v0 = v01 − F01/K_i); er geht nicht in die Steifigkeit ein, wird für die
  Verdrehung aber getrennt ausgewiesen (+2·v0/z). (3) Mittelkurve durch
  Mitteln der Sekantensteifigkeiten je Kraftstufe (K(F) = Mittel F/v_i(F),
  v(F) = F/K(F)), damit das Mittel im Fenster 0,1–0,4·F_est mit
  K_ser = 279,52 kN/mm übereinstimmt. (4) Spanne von M_R aus den
  Einzelhöchstlasten mit ausweisen.
reason: >
  Entscheidungen des Nutzers am 2026-09-26: Hüllkurve (1) zugestimmt;
  Anfangsschlupf laut Betreuung nicht in der Steifigkeit, für die Verdrehung
  aber relevant (2); Mittelung der Steifigkeiten statt der Wege für
  Konsistenz mit dem Auswerteblatt (3), zunächst Mittelkurve aus allen 6
  Gruppen mit Vermerk der M_R-Spanne (4).
alternatives_considered: >
  Mittelung der Wege je Kraftstufe (ergab 269,1 statt 279,5 kN/mm im Fenster,
  verworfen); Einzelkurven statt Mittelkurve (vorerst nicht); Wiederbelastungs-
  steifigkeit K_e statt K_ser (offen, R1-COMMON-OPQ-008).
date: "2026-09-26"
---

Umsetzung: Skript `R1_GL24h_Mittelkurve_Mphi.py` im externen Quellenordner
unter R1/GL24h/calculations/ (siehe R1-GL24h-CALC-010). Die Schleife bei
0,4·F_est: EN 26891 schreibt Belasten bis 0,4·F_est, Entlasten auf
0,1·F_est und Wiederbelasten vor; Ent- und Wiederbelastung verlaufen steiler
(K_e), die Hüllkurve lässt diese Schleife weg. K_e geht nicht in die Kurve
ein; der Ast oberhalb F04 stammt aber aus dem bereits einmal
wiederbelasteten Prüfkörper.
