---
decision_id: R2-GL24h-DEC-001
scope:
  connection: R2
  material: GL24h
type: DECISION
question: >
  Welche Länge wird für die elastische Dehnungssteifigkeit der freien
  Gewindestange (`c_t`) angesetzt?
decision: >
  Es wird die freie Stangenlänge bis zum Beginn der Verklebungszone
  verwendet (nicht die gesamte Stangenlänge inkl. eingeklebtem Bereich).
reason: >
  Nur der nicht verklebte Stangenabschnitt dehnt sich wie ein freier
  Stahlstab; der eingeklebte Teil wird separat über die
  Verbund-Steifigkeit `c_ax,f,par` erfasst (Doppelzählung sonst).
alternatives_considered: Gesamte Stangenlänge inkl. Einklebebereich (verworfen).
date: "UNKNOWN (chat-3, seq 055-070; kein genaues Datum überliefert)"
---

Übernommen aus chat-3, DECISIONS.md "Seq 055-070 — Free rod length".
Ergebnis: `c_t,1 = 40.950 N/mm = 40,95 kN/mm` (R2-Excel, Sheet "Rahmenecke
GL24h SD", Zelle C120), Eingang in die Stangen-Steifigkeitskette
(R2-GL24h-CALC-002).
