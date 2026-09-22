---
result_id: R3-GL24h-III-PO-S-WD-36-RES-004
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  R3-GL24h-III-PO-S-WD-36-RES-003, korrigiert nach R3-GL24h-DEC-013
  (Halbierung: die in der Auswertungsdatei tabellierten K_ser-Werte
  basieren auf der ungeteilten Gesamtkraft des symmetrischen
  Doppelscher-Prüfkörpers, nicht auf der Kraft je Scherfuge).
n: 6
method: >
  Wie R3-GL24h-III-PO-S-WD-36-RES-003 (Poolung LINKS+RECHTS, n=6),
  zusätzlich jeder Einzelwert durch 2 geteilt (R3-GL24h-DEC-013).
  Halbierung vor der Poolung ist rechnerisch identisch zur Halbierung
  des bereits gepoolten RES-003-Mittelwerts (lineare Operation).
result:
  quantity: >
    Anfangssteifigkeit K_ser einer 3×6-Holzdübelgruppe, je Scherfuge
    (gepoolter Mittelwert LINKS+RECHTS, GL24h)
  value: 37.114
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
superseded_by:
---

Einzelwerte je Scherfuge (kN/mm, RES-002-Werte /2): LINKS
[33,935; 37,280; 42,485], RECHTS [32,950; 37,815; 38,220].

```
Mittelwert = 74,228 / 2 = 37,114 kN/mm
StabW (n-1) = 6,814 / 2 = 3,407 kN/mm, VarK = 9,2 % (unverändert, da
Mittelwert und StabW mit demselben Faktor skalieren)
```

Siehe R3-GL24h-DEC-013 zur Begründung der Halbierung (symmetrischer
Doppelscher-Prüfkörper, Fmax,SF = Fmax,ges/2-Konvention analog auf K_ser
angewendet). Geringste Streuung der bisherigen R3-Push-Out-Serien
(VarK 9,2 %) bleibt gegenüber den anderen Serien unverändert bestehen.
