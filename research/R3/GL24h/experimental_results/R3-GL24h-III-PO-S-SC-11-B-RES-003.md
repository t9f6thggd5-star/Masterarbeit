---
result_id: R3-GL24h-III-PO-S-SC-11-B-RES-003
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: R3-GL24h-III-PO-S-SC-11-B-RES-002
n: 6
method: >
  Poolung der in R3-GL24h-III-PO-S-SC-11-B-RES-002 dokumentierten
  K_ser-Einzelwerte aus LINKS (VL+HL) und RECHTS (VR+HR) zu einem
  gemeinsamen Stichprobenmittel. Begründung: LINKS und RECHTS sind laut
  Nutzerbestätigung (Chat, 2026-09-22) zwei unabhängige Verbindungen,
  nicht zwei Messstellenpaare derselben einen Verbindung
  (R3-GL24h-DEC-012).
result:
  quantity: >
    Anfangssteifigkeit K_ser einer einzelnen ASSY-Schraube (Lasche an
    Beam, gepoolter Mittelwert LINKS+RECHTS, GL24h)
  value: 13.762
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
superseded_by: R3-GL24h-III-PO-S-SC-11-B-RES-004
---

Einzelwerte (kN/mm, aus RES-002): LINKS [14,93; 16,56; 11,43], RECHTS
[12,27; 13,85; 13,53].

```
Mittelwert = (14,93+16,56+11,43+12,27+13,85+13,53)/6 = 13,762 kN/mm
StabW (n-1) = 1,840 kN/mm, VarK = 13,4 %
```

Rein rechnerische Poolung bereits in RES-002 dokumentierter Einzelwerte,
keine neue Rohdatenquelle. Deutlich niedrigere Steifigkeit als die
Lasche-an-Column-Serie (SC-11-C, 17,142 kN/mm) — Beam- und Column-Seite
werden hier bewusst getrennt geführt, nicht gemittelt (unterschiedliche
Anschlussgeometrie).

**Update (2026-09-22, R3-GL24h-DEC-013):** Dieser Wert ist um Faktor 2
zu hoch — die zugrunde liegenden K_ser-Werte basieren auf der
ungeteilten Gesamtkraft des symmetrischen Doppelscher-Prüfkörpers, nicht
auf der Kraft je Scherfuge (analog zur bereits etablierten Fmax,SF =
Fmax,ges/2-Konvention). Korrigierter Wert (6,881 kN/mm): siehe
R3-GL24h-III-PO-S-SC-11-B-RES-004.
