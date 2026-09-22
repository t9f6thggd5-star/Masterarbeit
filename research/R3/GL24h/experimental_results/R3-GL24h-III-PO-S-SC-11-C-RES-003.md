---
result_id: R3-GL24h-III-PO-S-SC-11-C-RES-003
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: R3-GL24h-III-PO-S-SC-11-C-RES-002
n: 6
method: >
  Poolung der in R3-GL24h-III-PO-S-SC-11-C-RES-002 dokumentierten
  K_ser-Einzelwerte aus LINKS (VL+HL) und RECHTS (VR+HR) zu einem
  gemeinsamen Stichprobenmittel. Begründung: LINKS und RECHTS sind laut
  Nutzerbestätigung (Chat, 2026-09-22) zwei unabhängige Verbindungen,
  nicht zwei Messstellenpaare derselben einen Verbindung
  (R3-GL24h-DEC-012).
result:
  quantity: >
    Anfangssteifigkeit K_ser einer einzelnen ASSY-Schraube (Lasche an
    Column, gepoolter Mittelwert LINKS+RECHTS, GL24h)
  value: 17.142
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
superseded_by: R3-GL24h-III-PO-S-SC-11-C-RES-004
---

Einzelwerte (kN/mm, aus RES-002): LINKS [20,71; 16,21; 17,76], RECHTS
[19,42; 13,57; 15,18].

```
Mittelwert = (20,71+16,21+17,76+19,42+13,57+15,18)/6 = 17,142 kN/mm
StabW (n-1) = 2,675 kN/mm, VarK = 15,6 %
```

Rein rechnerische Poolung bereits in RES-002 dokumentierter Einzelwerte,
keine neue Rohdatenquelle.

**Update (2026-09-22, R3-GL24h-DEC-013):** Dieser Wert ist um Faktor 2
zu hoch — die zugrunde liegenden K_ser-Werte basieren auf der
ungeteilten Gesamtkraft des symmetrischen Doppelscher-Prüfkörpers, nicht
auf der Kraft je Scherfuge (analog zur bereits etablierten Fmax,SF =
Fmax,ges/2-Konvention). Korrigierter Wert (8,571 kN/mm): siehe
R3-GL24h-III-PO-S-SC-11-C-RES-004.
