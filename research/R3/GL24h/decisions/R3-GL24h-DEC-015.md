---
decision_id: R3-GL24h-DEC-015
scope:
  connection: R3
  material: GL24h
type: DECISION
question: >
  Welcher Wert der Beam-seitigen ASSY-Schraubengruppe (32 Schrauben, eine
  Laschenseite) geht in die Zugpfadkette ein?
decision: >
  c32,Beam = 137,9 kN/mm (c16,Beam = 78,8 kN/mm je Scherfuge, Rekonstruktion
  aus III-PO-S-SC-44-B-1, R3-GL24h-CALC-010) als Hauptwert. Für die
  Parameterstudie wird die Spanne 130–147 kN/mm mitgeführt (untere Grenze
  mit 1×1-Fensterkorrektur, obere Grenze Faktor 0,8028 nach
  R3-GL24h-CALC-008).
reason: >
  Einziger Wert, der auf einer Messung an einer Beam-Gruppe mit 16 Schrauben
  beruht; braucht die wenigsten Zusatzannahmen (nur gleiche Kurvenform von
  Träger- und Stützenseite zwischen den Lastfenstern); liegt mittig in der
  Spanne. Einfluss auf die Zugpfadkette gering (c_t,sleeve ändert sich über
  die Spanne um etwa ±1 %). Nutzerentscheidung (Chat, 2026-09-28), im
  R3-Excel bereits übernommen (Sheet "Rahmenecke GL24h SD" M64, I116).
alternatives_considered: >
  147,5 kN/mm (Faktor 0,8028, ASS-004/CALC-008) — ohne Messung einer
  Beam-Mehrschraubengruppe; 129,7 kN/mm (mit 1×1-Fensterkorrektur) — nur als
  Empfindlichkeit, da 1×1- und 4×4-Kurven sich unterschiedlich versteifen und
  die 1×1-Werte stark streuen.
date: "2026-09-28"
superseded_by:
---

n = 1 bleibt die zentrale Einschränkung; R3-GL24h-OPQ-022 bleibt OPEN, bis
ein weiterer Beam-4×4-Versuch oder eine belastbare Methode vorliegt.
Erläuterung des Rechenwegs als Word-Dokument an den Nutzer übergeben
(R3_GL24h_Rekonstruktion_Steifigkeit_44B.docx, 2026-09-28).
