---
result_id: R3-GL24h-III-PO-S-SC-11-C-RES-004
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  R3-GL24h-III-PO-S-SC-11-C-RES-003, korrigiert nach R3-GL24h-DEC-013
  (Halbierung: die in der Auswertungsdatei tabellierten K_ser-Werte
  basieren auf der ungeteilten Gesamtkraft des symmetrischen
  Doppelscher-Prüfkörpers, nicht auf der Kraft je Scherfuge).
n: 6
method: >
  Wie R3-GL24h-III-PO-S-SC-11-C-RES-003 (Poolung LINKS+RECHTS, n=6),
  zusätzlich jeder Einzelwert durch 2 geteilt (R3-GL24h-DEC-013).
  Halbierung vor der Poolung ist rechnerisch identisch zur Halbierung
  des bereits gepoolten RES-003-Mittelwerts (lineare Operation).
result:
  quantity: >
    Anfangssteifigkeit K_ser einer einzelnen ASSY-Schraube, je Scherfuge
    (Lasche an Column, gepoolter Mittelwert LINKS+RECHTS, GL24h)
  value: 8.571
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
superseded_by:
---

Einzelwerte je Scherfuge (kN/mm, RES-002-Werte /2): LINKS
[10,355; 8,105; 8,880], RECHTS [9,710; 6,785; 7,590].

```
Mittelwert = 17,142 / 2 = 8,571 kN/mm
StabW (n-1) = 2,675 / 2 = 1,338 kN/mm, VarK = 15,6 % (unverändert, da
Mittelwert und StabW mit demselben Faktor skalieren)
```

Siehe R3-GL24h-DEC-013 zur Begründung der Halbierung (symmetrischer
Doppelscher-Prüfkörper, Fmax,SF = Fmax,ges/2-Konvention analog auf K_ser
angewendet). Wird als Basiswert für den Gruppeneffizienz-Vergleich mit
SC-44-C (RES-004) herangezogen.
