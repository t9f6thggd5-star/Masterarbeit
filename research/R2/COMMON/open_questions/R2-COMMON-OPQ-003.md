---
open_question_id: R2-COMMON-OPQ-003
scope:
  connection: R2
  material: COMMON
status: RESOLVED
question: >
  Ist eine statistisch konsistente, reine Mittelwert-Tragfähigkeit für die
  ASSY-Schrauben (Ausziehen, Knicken) überhaupt abbildbar, wenn die
  einzige verfügbare Quelle (ETA-11/0190) nur charakteristische
  Schraubenkennwerte liefert?
context: >
  Der aktuelle Ansatz verwendet mittlere Holzkennwerte, aber
  charakteristische ETA-Schraubenkennwerte, bei `γ = 1`. Das Setzen von
  `γ = 1` macht einen charakteristischen Wert nicht zu einem Mittelwert
  (`f_k ≠ f_mean`) — das Ergebnis ist ein experimentnahes Hybridmodell,
  keine echte statistische Mittelwertrechnung.
related_sources: ETA-11-0190-2026
options_considered: >
  (a) Hybridmodell explizit als solches kennzeichnen (aktueller Stand);
  (b) Hersteller-/Versuchs-Mittelwertdaten für `f_ax,mean`, `f_y,mean`
  beschaffen, falls ein vollständig konsistentes Mittelwertmodell
  benötigt wird.
date_opened: "2026-09-01"
date_resolved: "2026-09-30"
resolution: >
  Geschlossen (Nutzer, 2026-09-30): für die Tragfähigkeit nicht maßgebend, weil die Gewindestangen (Zugversuchsmittel 285,77 kN) vor
  Querdruck und Schrauben versagen (Excel C97 = MIN(L16;L87;H87)).
---

Übernommen aus chat-3, OPEN_QUESTIONS.md Punkt 3 und KNOWLEDGE.md
Abschnitt 13. Betrifft aktuell konkret die Schraubenwerte im
GL24h-Verstärkungsblock (`f_y,k = 900 N/mm²`, `f_w,k`, siehe
R2-GL24h-CALC-006/CALC-007); relevant für GL75, sobald dort ggf. eine
eigene ASSY-Verstärkung modelliert wird (siehe R2-GL75-OPQ-002).
