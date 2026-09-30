---
decision_id: R3-COMMON-DEC-008
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Wie werden die Komponenten Sprödversagen parallel zur Faser (Katalog Nr. 13,
  br,par) und rechtwinklig zur Faser (Nr. 14, br,perp) nach Buchholz2025 bei R3
  in Steifigkeit und Tragfähigkeit behandelt?
decision: >
  Steifigkeit: c_br,par = c_br,perp = ∞ (wie bereits in R3-COMMON-DEC-005).
  Tragfähigkeit: br,par und br,perp werden als nicht maßgebend angenommen und
  vorerst nicht rechnerisch nachgewiesen; maßgebend bleibt die Gewindestange
  (R3-COMMON-DEC-003). Die Annahme ist in der schriftlichen Ausarbeitung zu
  begründen (R3-COMMON-OPQ-006).
reason: >
  Nutzerentscheidung (Chat, 2026-09-30). Buchholz2025 Tab. 1 (S. 1745) nennt
  für Nr. 13/14 nur eine Tragfähigkeitsregel (FprEN 1995-1-1:2024,
  Abschn. 11.5 bzw. 11.6), keine Steifigkeit; auch FprEN 11.5/11.6 enthalten
  nur Tragfähigkeitsregeln (S. 205–219). Die Komponenten stehen im Federmodell,
  weil es Tragfähigkeit und Steifigkeit gemeinsam abbildet; für die Steifigkeit
  sind sie wie c,p bei Buchholz2025 (S. 1746, "should be assumed to be
  infinite") faktisch starr. Deutung (von Claude vorgeschlagen, vom Nutzer im Chat
  mitgetragen): Sprödversagen ist ein Versagensmodus, kein eigener
  Verformungsmechanismus; die elastische Holzverformung im Gruppenbereich ist
  in K_ser der Push-Out-Versuche bzw. in c_H,Lasche enthalten (Abgrenzung
  offen, R3-COMMON-OPQ-003), eine eigene br-Feder würde doppelt zählen. Eine
  rechnerische Tragfähigkeit nach Norm würde laut Nutzer die Tragfähigkeit
  voraussichtlich stark unterschätzen (Bemessungswerte, 11.5 auf quer
  belastete Stifte zugeschnitten, keine Verstärkungswirkung der geneigten
  ASSY-Schrauben).
alternatives_considered: >
  Rechnerischer Nachweis nach FprEN 11.5/11.6 mit Bemessungswerten (verworfen,
  zu konservativ); Nachweis mit Mittelwerten gegen die Stangentragfähigkeit
  203 kN (GL24h) bzw. 293 kN (GL75) je Lasche oder Kalibrierung des
  Normmodells an den 4×4-Push-Out-Versuchen (vorerst nicht durchgeführt,
  mögliche Stütze der Begründung, siehe R3-COMMON-OPQ-006).
date: "2026-09-30"
superseded_by:
---

Gilt für GL24h und GL75. Präzisiert R3-COMMON-DEC-005 (dort c_br = ∞ nur für
die Steifigkeit festgelegt). Quellen: Buchholz2025 (Tab. 1, S. 1745; Text
S. 1746), FprEN-1995-1-1-2024 (Abschn. 11.5, 11.6, S. 205–219).
