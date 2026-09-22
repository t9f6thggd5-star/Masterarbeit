---
result_id: R3-GL24h-III-PO-S-SC-44-C-RES-003
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: R3-GL24h-III-PO-S-SC-44-C-RES-002
n: 6
method: >
  Poolung der in R3-GL24h-III-PO-S-SC-44-C-RES-002 dokumentierten
  K_ser-Einzelwerte aus LINKS (VL+HL) und RECHTS (VR+HR) zu einem
  gemeinsamen Stichprobenmittel. Begründung: LINKS und RECHTS sind laut
  Nutzerbestätigung (Chat, 2026-09-22) zwei unabhängige Verbindungen,
  nicht zwei Messstellenpaare derselben einen Verbindung
  (R3-GL24h-DEC-012).
result:
  quantity: >
    Anfangssteifigkeit K_ser einer 4×4-ASSY-Schraubengruppe (16 Schrauben,
    Lasche an Column, gepoolter Mittelwert LINKS+RECHTS, GL24h)
  value: 209.945
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
superseded_by: R3-GL24h-III-PO-S-SC-44-C-RES-004
---

Einzelwerte (kN/mm, aus RES-002): LINKS [225,85; 156,57; 198,89], RECHTS
[273,18; 161,87; 243,31].

```
Mittelwert = (225,85+156,57+198,89+273,18+161,87+243,31)/6 = 209,945 kN/mm
StabW (n-1) = 46,146 kN/mm, VarK = 22,0 %
```

Rein rechnerische Poolung bereits in RES-002 dokumentierter Einzelwerte,
keine neue Rohdatenquelle. Deutliche Streuung zwischen den Prüfkörpern
bleibt bestehen (VarK 22,0 %) — als Eingangsgröße mit Vorsicht zu
verwenden, nicht als eng gesicherter charakteristischer Wert (CLAUDE.md
Abschnitt 15).

Zum Vergleich (Gruppeneffekt, nicht weiter interpretiert): 16 × die
gepoolte Einzelschrauben-Steifigkeit derselben Lasche-an-Column-Serie
(R3-GL24h-III-PO-S-SC-11-C-RES-003, 17,142 kN/mm) ergäbe rechnerisch
274,3 kN/mm — die gemessene Gruppensteifigkeit (209,945 kN/mm) liegt
darunter (Gruppeneffizienz ≈ 76,5 %).

**Update (2026-09-22, R3-GL24h-DEC-013):** Dieser Wert ist um Faktor 2
zu hoch — die zugrunde liegenden K_ser-Werte basieren auf der
ungeteilten Gesamtkraft des symmetrischen Doppelscher-Prüfkörpers, nicht
auf der Kraft je Scherfuge (analog zur bereits etablierten Fmax,SF =
Fmax,ges/2-Konvention). Korrigierter Wert (104,973 kN/mm): siehe
R3-GL24h-III-PO-S-SC-44-C-RES-004.
