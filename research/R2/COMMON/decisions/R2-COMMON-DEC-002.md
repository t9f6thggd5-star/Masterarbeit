---
decision_id: R2-COMMON-DEC-002
scope:
  connection: R2
  material: COMMON
type: DECISION
question: >
  Wie ist die Druckzone am Rahmeneck-Innenknoten anzusetzen (rechteckige
  vs. dreieckige Pressungsverteilung), und wo liegt der resultierende
  Kraftangriffspunkt/Hebelarm? (löst R2-COMMON-OPQ-001)
decision: >
  Die Druckzone wird als RECHTECKIG angesetzt (konstante
  Pressungsverteilung über die Druckzonenhöhe, keine Abminderung durch
  einen Plastizierungs- oder Dreiecksfaktor). Der Hebelarm z wird mittig
  in der Druckzone angesetzt, d. h. der Kraftangriffspunkt der
  Druckresultierenden liegt in der Mitte der rechteckigen Druckzonenfläche.
reason: >
  Festlegung durch die Betreuerin in der Besprechung vom 2026-09-04.
alternatives_considered: >
  Dreieckige Pressungsverteilung mit einem Plastizierungsfaktor,
  methodisches Vorbild bei Lippert (2002, h_d ≈ 0,4·h_z, siehe
  R2-COMMON-OPQ-001 und wiki/R2/COMMON/literature/R2-COMMON-CLAIM-018.md)
  — nicht gewählt.
date: "2026-09-04"
---

Löst R2-COMMON-OPQ-001 (Druckzonenlänge/-verteilung am
Rahmeneck-Innenknoten). Festlegung durch die Betreuerin in der
Besprechung vom 2026-09-04; dem Nutzer (Lukas) am 2026-09-16 im Chat
mitgeteilt und hier entsprechend nachgetragen.

Materialunabhängig geführt (R2/COMMON), da die Wahl der
Druckverteilungsform und die Lage des Kraftangriffspunkts primär von der
Rahmeneck-Konstruktion (Ankerplatte, Kontaktgeometrie), nicht vom
verwendeten Holzwerkstoff (GL24h/GL75) abhängt — analog zu
R2-COMMON-OPQ-001 selbst.

**Was diese Entscheidung festlegt und was nicht:** Festgelegt sind Form
(rechteckig statt dreieckig) und Lage des Kraftangriffspunkts (Mitte der
Druckzonenfläche). NICHT festgelegt ist die konkrete Höhe/Ausdehnung der
rechteckigen Druckzone selbst (Betrag von h_d) — deren Bestimmung ist ein
nachfolgender Berechnungsschritt (`c_c,90`, `c_c,0`), der durch diese
Entscheidung erst freigegeben wird, siehe R2-COMMON-OPQ-006 (Kombination
von Zug- und Druckseiten-Steifigkeit zur vollständigen Rotationssteifigkeit
der Rahmenecke).
