---
calculation_id: R3-GL24h-CALC-008
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data: R3-GL24h-III-PO-S-SC-11-B-RES-004, R3-GL24h-III-PO-S-SC-11-C-RES-004,
    R3-GL24h-III-PO-S-SC-44-C-RES-004
  assumptions: R3-GL24h-ASS-004
method: >
  Hochrechnung der ASSY-Schraubengruppen-Anfangssteifigkeit
  c_ax+br,perp (Beam-Seite, Lasche am Träger) für 4×4 (16 Schrauben)
  und die reale 4×8-Gruppe (32 Schrauben, eine Laschenseite), indem
  die entsprechenden Column-seitigen Werte (c16,Column aus RES-004,
  c32,Column aus R3-GL24h-CALC-007) mit dem konstanten Verhältnis
  c1,Beam/c1,Column = 6,881/8,571 = 0,8028 (R3-GL24h-ASS-004)
  skaliert werden.
equations: >
  Verhältnis: r = c1,Beam / c1,Column = 6,881 / 8,571 = 0,80282

  c16,Beam = c16,Column · r = 104,973 · 0,80282 = 84,275 kN/mm

  c32,Beam = c32,Column · r = 183,684 · 0,80282 = 147,466 kN/mm
  (c32,Column = 183,684 kN/mm aus R3-GL24h-CALC-007)
result:
  quantity: Extrapolierte ASSY-Schraubengruppen-Anfangssteifigkeit
    c_ax+br,perp (Beam-Seite, Lasche am Träger, faserparallel im
    Beam-Bezugssystem) einer realen 4×8-Gruppe (32 Schrauben, eine
    Laschenseite), über das konstante Beam/Column-Verhältnis aus dem
    Column-seitigen Hochrechnungswert (CALC-007) abgeleitet
  value: 147.466
  unit: kN/mm
  original_value:
  original_unit:
source_file:
certainty: CALCULATED
superseded_by:
---

**Zwischenergebnis c16,Beam (4×4) = 84,275 kN/mm** — zum Vergleich mit
einer künftigen, tatsächlich verwertbaren Messung dieser Konfiguration
(sollte eine solche verfügbar werden, siehe R3-GL24h-ASS-004).

**Ausdrücklich als vorläufige Schätzung gekennzeichnet:** Dieses
Ergebnis beruht vollständig auf der in R3-GL24h-ASS-004 dokumentierten
Vereinfachung (faserrichtungsunabhängige Gruppeneffizienz) und nicht
auf einer eigenen empirischen oder normativen Bestimmung des Beam-
seitigen Gruppeneffekts — eine solche war trotz Prüfung mehrerer
Ansätze (Exponent-Übertragung, Kreuzverhältnis-Methode, normative
n_ef-Formel, Literaturrecherche) nicht möglich. Certainty entsprechend
mit Vorbehalt zu lesen (die Rechenschritte selbst sind exakt, die
zugrunde liegende Annahme jedoch ASSUMED, nicht MEASURED).

Damit liegen jetzt für beide Seiten der ASSY-Schraubengruppe
Hochrechnungswerte auf 4×8 vor:

| Seite | c_32 [kN/mm] | Grundlage |
|---|---|---|
| Column (c_ax+br,par) | 183,684 | R3-GL24h-CALC-007, aus Push-Out-Daten kalibriertes α |
| Beam (c_ax+br,perp) | 147,466 | dieses CALC-008, über Beam/Column-Verhältnis abgeleitet |

Noch nicht in die Zugpfad-Gesamtsteifigkeitskette (c_t,sleeve,
R3-GL24h-CALC-001–005) eingebunden — dafür fehlt weiterhin c_c,0
(Holzstauchung unter der Stahlplatte, noch offen).
