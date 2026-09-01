---
decision_id: R1-GL24h-DEC-004
scope:
  connection: R1
  material: GL24h
type: DECISION
question: >
  Darf der Gruppen-Tragfähigkeitsfaktor "2" für die zweischnittige
  Johansen-Tragfähigkeit unhinterfragt angesetzt werden?
decision: >
  Nein — der Faktor wird nicht pauschal angesetzt; die genaue normative
  Interpretation ist vor jeder abschließenden Gesamttragfähigkeit explizit
  zu begründen.
reason: >
  Frühere Antworten widersprachen sich darüber, ob Gl. 11.14 je Scherfuge
  gilt und wie dies mit dem zweischnittigen Mechanismus kombiniert wird.
alternatives_considered:
date: "UNKNOWN (chat-2, seq 001-015; kein genaues Datum überliefert)"
---

Übernommen aus chat-2, DECISIONS.md D04 (dort mit Status "unresolved"
geführt — die zugrunde liegende technische Frage ist weiterhin offen,
siehe R1-GL24h-OPQ-006; diese Entscheidung selbst ("nicht unhinterfragt
ansetzen, sondern begründen") ist jedoch aktiv/umgesetzt).

**Beobachtung aus der Excel-Datei:** In
`R1/COMMON/calculations/20260208_Berechnung_Rahmenecke_SB+SD.xlsx`, Sheet
"Rahmenecke GL24h SD", wird in Zelle C57 eine Gesamttragfähigkeit
F_D,k,ges ≈ 494.77 kN ausgewiesen. Diese lässt sich rechnerisch aus den
Zellwerten als F_D,k(Modus f, C55 = 11.247 kN) × n_ef (C45 = 5.4989) ×
n_90 (C22 = 4) × m (C6 = 2) ≈ 494.77 kN rekonstruieren (siehe
R1-GL24h-CALC-003) — d. h. der Faktor "m = 2" scheint dort bereits korrekt
in die effektive Gesamtanzahl eingerechnet zu sein. Da in der Datei selbst
keine sichtbare Formel (nur der Zellwert) vorliegt, ist dies eine eigene
Rekonstruktion und wird nicht als abschließende Bestätigung gewertet —
siehe R1-GL24h-OPQ-006 für die weiterhin offene Verifikation.
