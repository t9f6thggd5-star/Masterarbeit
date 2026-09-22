---
result_id: R3-GL24h-III-PO-S-SD-36-RES-004
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  R3-GL24h-III-PO-S-SD-36-RES-003, korrigiert nach R3-GL24h-DEC-013
  (Halbierung: die in der Auswertungsdatei tabellierten K_ser-Werte
  basieren auf der ungeteilten Gesamtkraft des symmetrischen
  Doppelscher-Prüfkörpers, nicht auf der Kraft je Scherfuge).
n: 4
method: >
  Wie R3-GL24h-III-PO-S-SD-36-RES-003 (Poolung LINKS+RECHTS, n=4,
  Prüfkörper 1 weiterhin ausgeschlossen), zusätzlich jeder Einzelwert
  durch 2 geteilt (R3-GL24h-DEC-013). Halbierung vor der Poolung ist
  rechnerisch identisch zur Halbierung des bereits gepoolten
  RES-003-Mittelwerts (lineare Operation).
result:
  quantity: >
    Anfangssteifigkeit K_ser einer 3×6-Stabdübelgruppe, je Scherfuge
    (gepoolter Mittelwert LINKS+RECHTS, Prüfkörper 2+3, GL24h)
  value: 30.348
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
superseded_by:
---

Einzelwerte je Scherfuge (kN/mm, RES-002-Werte /2, nur PK2+PK3): LINKS
[31,570; 34,810], RECHTS [23,755; 31,255].

```
Mittelwert = 60,695 / 2 = 30,348 kN/mm (genauer 30,3475)
StabW (n-1) = 9,359 / 2 = 4,680 kN/mm, VarK = 15,4 % (unverändert, da
Mittelwert und StabW mit demselben Faktor skalieren)
```

Siehe R3-GL24h-DEC-013 zur Begründung der Halbierung (symmetrischer
Doppelscher-Prüfkörper, Fmax,SF = Fmax,ges/2-Konvention analog auf K_ser
angewendet). n=4 bleibt eine kleine Stichprobe; der Mittelwert wird
weiterhin ausdrücklich nicht als charakteristischer/typischer Wert
dargestellt (CLAUDE.md Abschnitt 15).
