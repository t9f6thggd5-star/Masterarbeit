---
result_id: R3-GL24h-III-PO-S-WD-36-RES-003
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: R3-GL24h-III-PO-S-WD-36-RES-002
n: 6
method: >
  Poolung der in R3-GL24h-III-PO-S-WD-36-RES-002 dokumentierten
  K_ser-Einzelwerte aus LINKS (VL+HL) und RECHTS (VR+HR) zu einem
  gemeinsamen Stichprobenmittel. Begründung: LINKS und RECHTS sind laut
  Nutzerbestätigung (Chat, 2026-09-22) zwei unabhängige Verbindungen,
  nicht zwei Messstellenpaare derselben einen Verbindung
  (R3-GL24h-DEC-012).
result:
  quantity: >
    Anfangssteifigkeit K_ser einer 3×6-Holzdübelgruppe (gepoolter
    Mittelwert LINKS+RECHTS, GL24h)
  value: 74.228
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
superseded_by: R3-GL24h-III-PO-S-WD-36-RES-004
---

Einzelwerte (kN/mm, aus RES-002): LINKS [67,87; 74,56; 84,97], RECHTS
[65,90; 75,63; 76,44].

```
Mittelwert = (67,87+74,56+84,97+65,90+75,63+76,44)/6 = 74,228 kN/mm
StabW (n-1) = 6,814 kN/mm, VarK = 9,2 %
```

Rein rechnerische Poolung bereits in RES-002 dokumentierter Einzelwerte,
keine neue Rohdatenquelle. Geringste Streuung der bisherigen R3-Push-Out-
Serien (VarK 9,2 %).

**Update (2026-09-22, R3-GL24h-DEC-013):** Dieser Wert ist um Faktor 2
zu hoch — die zugrunde liegenden K_ser-Werte basieren auf der
ungeteilten Gesamtkraft des symmetrischen Doppelscher-Prüfkörpers, nicht
auf der Kraft je Scherfuge (analog zur bereits etablierten Fmax,SF =
Fmax,ges/2-Konvention). Korrigierter Wert (37,114 kN/mm): siehe
R3-GL24h-III-PO-S-WD-36-RES-004.
