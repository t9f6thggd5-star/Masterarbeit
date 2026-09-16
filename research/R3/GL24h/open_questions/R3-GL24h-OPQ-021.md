---
open_question_id: R3-GL24h-OPQ-021
scope:
  connection: R3
  material: GL24h
status: OPEN
question: >
  Warum liegen für die Serie III-PO-S-SC-44-B (Push-Out, Schraube,
  Lasche am Riegel, 4×4) nur für Prüfkörper 1 Werte vor (Fmax=47,3 kN,
  Steifigkeit "nv"), während Prüfkörper 2 und 3 in der Auswertungsdatei
  vollständig leer sind ("-" in allen Spalten, Stand "entfällt")? Wurden
  PK2/3 nie durchgeführt, oder ist nur die Auswertung nicht eingetragen?
context: >
  Quelle: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_
  FINAL.xlsx`, Blatt "Überblick", Zeilen "III-PO-S-SC-44-B-1/2/3".
  Dokumentiert (ohne weitere Interpretation, n=1) in
  R3-GL24h-III-PO-S-SC-44-B-RES-001. Zum Vergleich: die Lasche-an-
  Column-Variante derselben 4×4-Anordnung (III-PO-S-SC-44-C) hat alle
  3 Prüfkörper vollständig (siehe R3-GL24h-III-PO-S-SC-44-C-RES-001/002)
  — ein Beam/Column-Vergleich für die 44er-Anordnung ist deshalb aktuell
  nicht sinnvoll möglich.
related_sources:
options_considered:
date_opened: "2026-09-16"
date_resolved:
resolution:
---

Aufgefallen beim Einpflegen der Push-Out-Steifigkeitsauswertung ins
Wiki/`research/` am 2026-09-16. Der einzige vorhandene Fmax-Wert (PK1,
47,3 kN) wird gemäß CLAUDE.md Abschnitt 15 ausdrücklich als
Einzelbefund behandelt, nicht als charakteristischer Wert der Serie.
