---
open_question_id: R1-COMMON-OPQ-005
scope:
  connection: R1
  material: COMMON
status: OPEN
question: >
  Wie werden im Zugpfad von R1 (a) die Komponente c_br,par und (b) die
  Verformung des Holzes zwischen den Dübelgruppen angesetzt, nachdem
  feststeht, dass der Versuchswert nur c_v,f enthält (R1-COMMON-OPQ-003)?
  Und (c): Welcher Messkanal der Druckversuche enthält die zusätzlich
  gemessene Gesamtverformung der Verbindung, und für welche Versuche
  liegt sie vor?
context: >
  (a) Im Komponentenkatalog Buchholz2025 (Tab. 1, Nr. 13) ist br,par
  "Brittle failure, lateral load parallel to grain" mit einer
  Tragfähigkeitsregel (FprEN 11.5), aber ohne Steifigkeitsangabe. Im
  Federmodell für R1 (Buchholz2025, Abb. und Gl. 2) steht c_br,par
  trotzdem in Reihe im Zugpfad. Wird c_br,par als starr angesetzt,
  bleiben c_t,tot = 279,52 kN/mm (GL24h) bzw. 727,74 kN/mm (GL75)
  unverändert. (b) Die Zugverformung des Holzes parallel zur Faser
  (Träger und Stütze zwischen Dübelgruppe und Rahmenecke) ist weder im
  Messwert noch im Federmodell enthalten; im Druckpfad gibt es dafür
  c_c,0, im Zugpfad kein Gegenstück. (c) Laut Betreuung wurde bei den
  Druckversuchen zusätzlich die Gesamtverformung gemessen; in der
  Push-Out-Auswertungsdatei sind nur Maschinenweg sowie VL/HL/VR/HR
  (Mittel vorn/hinten je Seite) erkennbar.
related_sources: Buchholz2025
options_considered: >
  (a1) c_br,par starr (Katalog ohne Steifigkeit), (a2) eigene
  Steifigkeitsabschätzung. (b1) Feder c_t,0 = E_0,mean·A/l ergänzen
  (Länge und Fläche festzulegen), (b2) als Modellgrenze benennen.
date_opened: "2026-09-25"
date_resolved:
resolution:
---

Entstanden aus der Rückmeldung der Betreuung zu R1-COMMON-OPQ-003
(2026-09-25).

**Update (2026-09-26), Arbeitsannahme zu (a):** c_br,par wird vorläufig
als starr angesetzt (Nutzerentscheidung). Die Frage bleibt als offener
Diskussionspunkt mit der Betreuung bestehen: Der Katalog Buchholz2025 gibt
für br,par nur eine Tragfähigkeitsregel an, das Federmodell (Gl. 2) führt
c_br,par aber zweimal in Reihe im Zugpfad. Mit c_br,par starr bleibt
c_t,tot = 279,52 kN/mm (GL24h) bzw. 727,74 kN/mm (GL75). (b) und (c) sind
unverändert offen. Siehe auch R1-COMMON-DEC-004.

**Update (2026-09-28), zu (b) Holzdehnung im Zugpfad:** Vom Nutzer
erneut als offene Frage aufgenommen: ob und wie die Zugverformung des
Holzes parallel zur Faser bei R1 zu berücksichtigen ist. Bezeichnung
vorläufig **c_t,0** (Zug parallel zur Faser, Gegenstück zu c_c,0 im
Druckpfad; nicht zu verwechseln mit c_t = Zugseite je Bauteil in
R1-COMMON-DEC-004 und mit c_t = freie Stangendehnung bei R2).
Ansatz c_t,0 = E_0,mean · A / l_eff je Bauteil, in Reihe mit c_v,f.
Offen: (i) mitwirkende Fläche A (Holzbreite 2 × 72 mm, mitwirkende Höhe);
(ii) Länge l_eff ≈ ½ · Gruppenlänge + Abstand letzter Dübel bis Gehrung
(Plan PLAN-2685085-001-V1/V2); (iii) Doppelzählung: der Messwert c_v,f
wird im Schwerpunkt der Dübelgruppe erfasst (R1-COMMON-OPQ-003), ein Teil
der Holzdehnung innerhalb der Gruppe ist ggf. schon enthalten — dann nur
Gruppenschwerpunkt bis Gehrung ansetzen.
Grobe Abschätzung (Claude, R1/GL24h, nicht im Excel): c_t,0 ≈ 800–2000 kN/mm
je Bauteil → C_rot,tot −11 % bis −21 %; zusammen mit nachgiebiger
Druckseite (c_c,tot = 1…5 · c_t,tot) −17 % bis −35 %, Φ bei M_R ≈
2,65–3,65 mrad statt 2,36 mrad.
