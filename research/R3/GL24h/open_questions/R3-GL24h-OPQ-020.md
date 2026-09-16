---
open_question_id: R3-GL24h-OPQ-020
scope:
  connection: R3
  material: GL24h
status: OPEN
question: >
  Warum ist Prüfkörper 1 der Serie III-PO-S-SD-36 (Push-Out, Stabdübel,
  3×6) in der Auswertungsdatei als "entfällt" markiert, mit Steifigkeit
  "nv" (nicht verwertbar), obwohl ein Fmax-Wert (35,525 kN pro
  Scherfuge) vorhanden ist — und ist dieser Fmax-Wert trotzdem
  verwendbar?
context: >
  Quelle: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_
  FINAL.xlsx`, Blatt "Überblick", Zeile "III-PO-S-SD-36-1". Der
  Fmax-Wert von PK1 (35,525 kN) weicht stark von PK2/PK3 (65,42 kN /
  68,695 kN) ab — weniger als halb so groß. Dokumentiert (ohne weitere
  Interpretation) in R3-GL24h-III-PO-S-SD-36-RES-001 (Fmax, n=3 inkl.
  PK1) und R3-GL24h-III-PO-S-SD-36-RES-002 (Steifigkeit, n=2 exkl. PK1).
related_sources:
options_considered: >
  (1) Prüfabbruch oder Fehlmessung bei PK1 — Fmax-Wert wäre dann
  ebenfalls fraglich, nicht nur die Steifigkeit. (2) Realer, abweichender
  Versagensmechanismus bei PK1 (z. B. vorzeitiges Versagen) — Fmax-Wert
  dann prinzipiell gültig, aber nicht direkt mit PK2/3 vergleichbar. Beide
  Optionen bewusst nicht entschieden (CLAUDE.md Abschnitt 4).
date_opened: "2026-09-16"
date_resolved:
resolution:
---

Aufgefallen beim Einpflegen der Push-Out-Steifigkeitsauswertung ins
Wiki/`research/` am 2026-09-16. Der Mittelwert in
R3-GL24h-III-PO-S-SD-36-RES-001 (56,547 kN) schließt PK1 derzeit mit
ein — sollte sich herausstellen, dass PK1 ungültig ist, muss dieser
RES-Eintrag korrigiert werden (alter Eintrag nicht löschen, sondern
`superseded_by` setzen, CLAUDE.md Abschnitt 13).
