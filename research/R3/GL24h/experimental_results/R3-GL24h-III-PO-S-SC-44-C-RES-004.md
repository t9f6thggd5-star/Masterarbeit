---
result_id: R3-GL24h-III-PO-S-SC-44-C-RES-004
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  R3-GL24h-III-PO-S-SC-44-C-RES-003, korrigiert nach R3-GL24h-DEC-013
  (Halbierung: die in der Auswertungsdatei tabellierten K_ser-Werte
  basieren auf der ungeteilten Gesamtkraft des symmetrischen
  Doppelscher-Prüfkörpers, nicht auf der Kraft je Scherfuge).
n: 6
method: >
  Wie R3-GL24h-III-PO-S-SC-44-C-RES-003 (Poolung LINKS+RECHTS, n=6),
  zusätzlich jeder Einzelwert durch 2 geteilt (R3-GL24h-DEC-013).
  Halbierung vor der Poolung ist rechnerisch identisch zur Halbierung
  des bereits gepoolten RES-003-Mittelwerts (lineare Operation).
result:
  quantity: >
    Anfangssteifigkeit K_ser einer 4×4-ASSY-Schraubengruppe (16
    Schrauben), je Scherfuge (Lasche an Column, gepoolter Mittelwert
    LINKS+RECHTS, GL24h)
  value: 104.973
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
superseded_by:
---

Einzelwerte je Scherfuge (kN/mm, RES-002-Werte /2): LINKS
[112,925; 78,285; 99,445], RECHTS [136,590; 80,935; 121,655].

```
Mittelwert = 209,945 / 2 = 104,973 kN/mm
StabW (n-1) = 46,146 / 2 = 23,073 kN/mm, VarK = 22,0 % (unverändert, da
Mittelwert und StabW mit demselben Faktor skalieren)
```

Siehe R3-GL24h-DEC-013 zur Begründung der Halbierung (symmetrischer
Doppelscher-Prüfkörper, Fmax,SF = Fmax,ges/2-Konvention analog auf K_ser
angewendet). Deutliche Streuung zwischen den Prüfkörpern bleibt bestehen
(VarK 22,0 %) — als Eingangsgröße mit Vorsicht zu verwenden, nicht als
eng gesicherter charakteristischer Wert (CLAUDE.md Abschnitt 15).

Zum Vergleich (Gruppeneffekt, nicht weiter interpretiert): 16 × die
gepoolte Einzelschrauben-Steifigkeit derselben Lasche-an-Column-Serie,
je Scherfuge (R3-GL24h-III-PO-S-SC-11-C-RES-004, 8,571 kN/mm) ergäbe
rechnerisch 137,13 kN/mm — die gemessene Gruppensteifigkeit
(104,973 kN/mm) liegt darunter (Gruppeneffizienz ≈ 76,5 %, unverändert
gegenüber RES-003, da beide Seiten des Vergleichs mit demselben Faktor
skalieren).
