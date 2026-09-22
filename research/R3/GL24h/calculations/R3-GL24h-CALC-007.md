---
calculation_id: R3-GL24h-CALC-007
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data: R3-GL24h-III-PO-S-SC-11-C-RES-004, R3-GL24h-III-PO-S-SC-44-C-RES-004
    (Anfangssteifigkeit je Scherfuge, Column-Seite, 1×1 bzw. 4×4); zur
    Plausibilitätsprüfung zusätzlich R3-GL24h-III-PO-S-SC-11-C-RES-001,
    R3-GL24h-III-PO-S-SC-44-C-RES-001 (Tragfähigkeit, dieselben Serien)
  assumptions: R3-GL24h-ASS-003
method: >
  Kalibrierung des Gruppenineffizienz-Exponenten α (R3-GL24h-ASS-003) aus
  den Column-seitigen (Lasche an Stütze) Push-Out-Steifigkeiten für 1×1
  (c_1 = 8,571 kN/mm, RES-004) und 4×4 (c_16 = 104,973 kN/mm, RES-004,
  4 Spalten × 4 Reihen). Mit dem Modell c_16 = n_Spalten · c_1 · n_Reihen^α
  (n_Spalten = 4 konstant, n_Reihen = 4) ergibt sich α = 0,807. Hochrechnung
  auf die reale Gruppe mit n_Reihen = 8 (4×8 = 32 Schrauben, eine
  Laschenseite): c_32 = 4 · c_1 · 8^α ≈ 183,68 kN/mm.

  Plausibilitätsprüfung (nicht Teil des Ergebnisses): dieselbe Herleitung
  mit den Tragfähigkeitswerten derselben Serien (F_1 = 10,745 kN,
  F_16 = 164,527 kN) ergibt einen eigenen Exponenten α_F = 0,968
  (deutlich näher an 1, d. h. geringere Gruppenineffizienz bei der
  Tragfähigkeit als bei der Anfangssteifigkeit — plausibel, da sich
  ungleiche Lastanteile zwischen den Reihen bei duktiler Laststeigerung
  nahe der Traglast eher ausgleichen können als im elastischen
  Anfangsbereich). Die damit hochgerechnete Tragfähigkeit F_32 ≈ 321,9 kN
  weicht nur ≈2,2 % von dem unabhängig (mit einem anderen, linearen
  n_ef=0,9n-Modell) ermittelten R3-GL24h-CALC-006-Wert (329,054 kN) ab —
  als Bestätigung, dass das Potenzgesetz-Modell (ASS-003) grundsätzlich
  plausible Ergebnisse liefert, nicht als eigenständiges Ergebnis dieser
  Berechnung.
equations: >
  α = ln(c_16 / (n_Spalten · c_1)) / ln(n_Reihen,4x4),  mit n_Spalten=4,
  n_Reihen,4x4=4

  c_32 = n_Spalten · c_1 · n_Reihen,4x8^α,  mit n_Reihen,4x8=8

  (Plausibilitätsprüfung, analog mit F statt c:
  α_F = ln(F_16/(4·F_1))/ln4;  F_32 = 4·F_1·8^α_F)
result:
  quantity: Extrapolierte ASSY-Schraubengruppen-Anfangssteifigkeit
    c_ax+br,par (Column-Seite, Lasche an Stütze, faserparallel) einer
    realen 4×8-Gruppe (32 Schrauben, eine Laschenseite), aus 1×1- und
    4×4-Push-Out-Steifigkeiten hochgerechnet
  value: 183.68
  unit: kN/mm
  original_value:
  original_unit:
source_file:
certainty: CALCULATED
superseded_by:
---

**Zwischenergebnis α = 0,807** (Column-Seite, aus c_1/c_16): entspricht
einer effektiven Reihenanzahl n_ef,Reihen(8) = 8^0,807 ≈ 5,36 (statt
linear 8) bzw. n_ef,Reihen(4) = 4 (exakte Reproduktion des 4×4-Messwerts,
da α direkt daraus kalibriert wurde).

**Ausdrücklich nur Column-Seite (c_ax+br,par):** Die Beam-Seite
(c_ax+br,perp) ist von diesem Ergebnis NICHT erfasst — siehe
R3-GL24h-ASS-003 für die Begründung (fehlende verwertbare 4×4-Daten,
Nutzerentscheidung gegen Übertragung des gleichen α, andere
Faserrichtung im Hauptbauteil). Die Beam-seitige Hochrechnung wird
gesondert behandelt (Stand 2026-09-22: noch offen).

Noch nicht in die Zugpfad-Gesamtsteifigkeitskette (c_t,sleeve,
R3-GL24h-CALC-001–005) eingebunden — das erfordert zusätzlich die
Beam-seitige Hochrechnung sowie c_c,0 (Holzstauchung unter der
Stahlplatte, noch offen).
