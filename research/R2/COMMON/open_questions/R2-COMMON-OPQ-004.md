---
open_question_id: R2-COMMON-OPQ-004
scope:
  connection: R2
  material: COMMON
status: RESOLVED
question: >
  Soll der Schub-Korrekturbeiwert `κ = 1` (siehe R2-COMMON-ASS-004) durch
  `κ = 5/6` oder einen literatur-/FE-kalibrierten Wert ersetzt werden?
context: >
  Beeinflusst die Schubfeldsteifigkeit `c_v` und damit die gesamte
  Zugseiten-Steifigkeit `c_T`; der quantitative Effekt auf die
  Gesamt-Rotationssteifigkeit der Rahmenecke ist noch nicht ermittelt.
related_sources:
options_considered: κ = 1 (aktuell) vs. κ = 5/6 vs. FE-kalibrierter Wert.
date_opened: "2026-09-01"
date_resolved: "2026-09-30"
resolution: >
  κ = 1 bleibt (Nutzer, 2026-09-30). Begründung: Im Schubfeld der Ecke wird
  die Kraft an den Rändern eingeleitet, der Schub ist näherungsweise gleichmäßig;
  analog zum Stützenstegfeld im Stahlbau (DIN EN 1993-1-8:2025-04, A.4.2,
  Gl. (A.13), S. 150: k_wp = 0,38·A_wp/(β·z), mit 0,38·E ≈ G, ohne Abminderung).
  κ = 5/6 gilt für die Schubverformung von Timoshenko-Balken mit
  Rechteckquerschnitt (vgl. FprEN 1995-1-1:2024, Anhang C, Gl. (C.9), S. 320).
---

Übernommen aus chat-3, OPEN_QUESTIONS.md Punkt 6 und TASKS.md "P3 — Shear
correction sensitivity".
