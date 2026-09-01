---
decision_id: R1-GL24h-DEC-003
scope:
  connection: R1
  material: GL24h
type: DECISION
question: >
  Wie werden die Bauteile in der Johansen-Gleichung (Gl. 11.14) für den
  R1-Anschluss (Holz-Schlitzblech-Holz, zweischnittig) nummeriert?
decision: >
  Bauteil 1 = äußeres Holz (Seitenteil), Bauteil 2 = inneres Stahlblech.
reason: >
  Quellnotation und Geometrie des Anschlusses.
alternatives_considered:
date: "UNKNOWN (chat-2, seq 001-010; kein genaues Datum überliefert)"
---

Übernommen aus chat-2, DECISIONS.md D03. Konsequenz:
f_{h,1,k} = Lochleibungsfestigkeit Holz, f_{h,2,k} = Lochleibungsfestigkeit
Stahl; die für den Johansen-Mechanismus wirksame innere Lochleibungstiefe
entspricht der halben Stahlblechdicke. Für die Geometrie 72 | 12 | 72 mm
ergibt sich damit eine wirksame innere Einbindetiefe von 12/2 = 6 mm —
bestätigt durch die Excel-Datei (Zelle C7, "Stahl - Mittelteil: t_h,2
12mm" = 6, siehe R1-GL24h-CALC-001).
