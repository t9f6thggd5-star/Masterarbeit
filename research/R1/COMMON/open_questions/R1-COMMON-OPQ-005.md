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
