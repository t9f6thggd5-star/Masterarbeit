---
result_id: R3-GL24h-III-PO-S-SD-36-RES-003
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: R3-GL24h-III-PO-S-SD-36-RES-002
n: 4
method: >
  Poolung der in R3-GL24h-III-PO-S-SD-36-RES-002 dokumentierten
  K_ser-Einzelwerte aus LINKS (VL+HL) und RECHTS (VR+HR) zu einem
  gemeinsamen Stichprobenmittel. Begründung: LINKS und RECHTS sind laut
  Nutzerbestätigung (Chat, 2026-09-22) zwei unabhängige Verbindungen,
  nicht zwei Messstellenpaare derselben einen Verbindung
  (R3-GL24h-DEC-012). **n=4 statt 6:** Prüfkörper 1 ist als 'nv' (nicht
  verwertbar) markiert und bleibt ausgeschlossen (siehe RES-001/RES-002),
  daher nur Prüfkörper 2+3 × LINKS/RECHTS = 4 Werte.
result:
  quantity: >
    Anfangssteifigkeit K_ser einer 3×6-Stabdübelgruppe (gepoolter
    Mittelwert LINKS+RECHTS, Prüfkörper 2+3, GL24h)
  value: 60.695
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
superseded_by: R3-GL24h-III-PO-S-SD-36-RES-004
---

Einzelwerte (kN/mm, aus RES-002, nur PK2+PK3): LINKS [63,14; 69,62],
RECHTS [47,51; 62,51].

```
Mittelwert = (63,14+69,62+47,51+62,51)/4 = 60,695 kN/mm
StabW (n-1) = 9,359 kN/mm, VarK = 15,4 %
```

Rein rechnerische Poolung bereits in RES-002 dokumentierter Einzelwerte,
keine neue Rohdatenquelle. n=4 ist eine kleine Stichprobe; der Mittelwert
wird deshalb ausdrücklich nicht als charakteristischer/typischer Wert
dargestellt (CLAUDE.md Abschnitt 15).

**Update (2026-09-22, R3-GL24h-DEC-013):** Dieser Wert ist um Faktor 2
zu hoch — die zugrunde liegenden K_ser-Werte basieren auf der
ungeteilten Gesamtkraft des symmetrischen Doppelscher-Prüfkörpers, nicht
auf der Kraft je Scherfuge (analog zur bereits etablierten Fmax,SF =
Fmax,ges/2-Konvention). Korrigierter Wert (30,348 kN/mm): siehe
R3-GL24h-III-PO-S-SD-36-RES-004.
