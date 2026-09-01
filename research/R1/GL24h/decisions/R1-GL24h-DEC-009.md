---
decision_id: R1-GL24h-DEC-009
scope:
  connection: R1
  material: GL24h
type: DECISION
question: >
  Ist der Betrag der relativen Translation zwischen den beiden geneigten
  Dübelgruppen automatisch die Rahmeneckenrotation φ?
decision: >
  Nein — der Betrag der relativen Translation zwischen den beiden
  geneigten Dübelgruppen ist nicht automatisch die Rahmeneckenrotation.
reason: >
  Eine reine Translation ändert nicht notwendigerweise die
  Bauteilausrichtung/-rotation.
alternatives_considered: >
  Vektor-Relativverschiebung via Kosinussatz bei 108° direkt als
  Rahmeneckenrotation interpretieren — verworfen.
date: "UNKNOWN (chat-2, seq 068-070; kein genaues Datum überliefert)"
---

Übernommen aus chat-2, DECISIONS.md D13. Konsequenz: die kinematische
Abbildung von lokalem Schlupf auf φ muss vor dem Fortfahren hergeleitet
werden — siehe R1-GL24h-HYP-001 und R1-GL24h-OPQ-002.

Die in der Excel-Datei (Zelle C92, "Umrechnung mit 108° Öffnungswinkel")
berechnete Vektor-Distanz Δu_ges ≈ 5.517 mm (siehe R1-GL24h-CALC-006) ist
ein Beispiel für genau diese noch unzureichende Vektor-Distanz-Rechnung,
nicht für die tatsächliche Rotation.
