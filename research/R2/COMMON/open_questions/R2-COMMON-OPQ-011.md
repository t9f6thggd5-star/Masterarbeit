---
open_question_id: R2-COMMON-OPQ-011
scope:
  connection: R2
  material: COMMON
status: OPEN
question: >
  Ist der Modellierungsansatz für c_c,0 (axiale Druck-Steifigkeit des
  Holzes parallel zur Faser in der Druckzone) korrekt — insbesondere
  die angesetzte Bezugslänge l=240mm (Plattentiefe in Kraftrichtung,
  Saint-Venant-artige Analogie zu h_ef bei c_c,90) sowie die Fläche
  A=Plattenfläche (160×240mm, unabhängig von der noch offenen
  Druckzonenhöhe h_d)?
context: >
  FprEN 1995-1-1:2024 enthält (Kapitel 9, geprüft am 2026-09-17) keine
  Formel für Druckverformung parallel zur Faser — nur 9.4
  "Compressive deformation perpendicular to grain" (Gl. 9.31). Es gibt
  also keine Normvorgabe für c_c,0, im Gegensatz zu c_c,90. Der
  angesetzte Ansatz c_c,0=E_0,mean·A/l (Hookesches Gesetz, homogener
  Ersatzstab) sowie insbesondere die Wahl von l=240mm sind eine eigene
  Modellierungsannahme (Analogieschluss zu h_ef, kein Normbezug, keine
  Literaturquelle) — siehe R2-GL24h-CALC-019. Der Nutzer hat der
  Fläche A=Plattenfläche und der Länge l=240mm im Chat vom 2026-09-17
  zugestimmt, möchte den Ansatz aber vor endgültiger Übernahme noch
  mit der Betreuerin absichern.
related_sources:
options_considered: >
  (1) l=240mm, Plattentiefe in Kraftrichtung (aktuell angesetzt,
  Saint-Venant-Analogie zu h_ef); (2) l=Druckzonenhöhe h_d (noch nicht
  bestimmt, R2-COMMON-OPQ-006, würde c_c,0 zusätzlich von dieser noch
  offenen Größe abhängig machen); (3) andere Bezugslänge (z. B.
  Trägerbreite/-tiefe), bisher nicht weiter verfolgt.
date_opened: "2026-09-17"
date_resolved:
resolution:
---

Übernommen aus der Chat-Diskussion vom 2026-09-17 zur Herleitung von
`c_c,0`. Betrifft `R2-GL24h-CALC-019` (und künftig die analoge
GL75-Berechnung, sobald für GL75 eine Druckseiten-Steifigkeitskette
aufgestellt wird). Materialunabhängig geführt, da die Wahl von `A`
und `l` primär von der Rahmeneck-Konstruktion (Ankerplattengeometrie),
nicht vom Holzwerkstoff abhängt — analog zu R2-COMMON-OPQ-001/DEC-002.

**Für die nächste Besprechung mit der Betreuerin vorzulegen:** ob der
Saint-Venant-artige Analogieschluss (Bezugslänge in der Größenordnung
der belasteten Plattenabmessung, hier 240mm) für die axiale Richtung
methodisch vertretbar ist, oder ob stattdessen die Druckzonenhöhe
`h_d` (sobald über R2-COMMON-OPQ-006 bestimmt) oder ein anderer Ansatz
verwendet werden sollte.
