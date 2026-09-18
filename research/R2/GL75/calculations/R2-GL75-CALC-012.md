---
calculation_id: R2-GL75-CALC-012
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources:
  literature: FragiacomoBatchelar2012a
  experimental_data:
  assumptions: R2-COMMON-ASS-006
method: >
  Anwendung der in R2-COMMON-HYP-001 (noch `CLAUDE_DRAFT`,
  `reviewed: false`) hergeleiteten Kombinationsformel
  `S_j,ini = z²/(1/c_T+1/c_C)` auf die für GL75 vollständig vorliegende
  Zugseiten-Gesamtsteifigkeit `c_T` (R2-GL75-CALC-011) und
  Druckseiten-Gesamtsteifigkeit `c_C` (R2-GL75-CALC-008), analog zum
  GL24h-Pendant (R2-GL24h-CALC-022). Der Hebelarm `z=560mm` ist
  materialunabhängig (identischer Excel-Zahlenwert in allen drei
  Blättern, siehe R2-GL24h-CALC-022 und R2-COMMON-ASS-006 für die
  inzwischen dokumentierte geometrische Herkunft: mittiger
  Kraftangriff in der 160×240mm-Stahlplatte, `z=800-2·(240/2)=560mm`).
equations: >
  S_j,ini = z²/(1/c_T + 1/c_C), siehe R2-COMMON-HYP-001 für die
  Herleitung.
result:
  quantity: Anfangsrotationssteifigkeit S_j,ini der Rahmenecke, GL75
  value: 15556.5
  unit: kNm/rad
  original_value: 15556508000
  original_unit: N*mm/rad
source_file: >
  Abgeleitet aus R2-GL75-CALC-008 (c_C), R2-GL75-CALC-011 (c_T) und dem
  materialunabhängigen Excel-Zahlenwert z=560mm (siehe R2-GL24h-CALC-022
  für die Fundstelle, R2-COMMON-ASS-006 für die Herkunftserklärung). Vom
  Nutzer unabhängig im Chat berechnet (15.556,61) und hier
  formelbasiert nachvollzogen/bestätigt (2026-09-18).
certainty: CALCULATED
superseded_by:
---

**Eingangswerte:** `c_T = 70,831 kN/mm` (R2-GL75-CALC-011),
`c_C = 165,545 kN/mm` (R2-GL75-CALC-008), `z = 560 mm`
(materialunabhängig, R2-COMMON-ASS-006).

**Rechnung:**

```
c_eq = (1/c_T + 1/c_C)^-1 = (1/70,831 + 1/165,545)^-1 = 49,606 kN/mm
S_j,ini = z² · c_eq = 560² mm² · 49,606 kN/mm = 15.556.508 kN·mm
        = 15.556,5 kNm/rad
```

Nutzer-Ergebnis (unabhängig gerechnet): `15.556,61 kNm/rad` — Abweichung
`≈0,1 kNm/rad` (<0,001 %), im Rahmen üblicher Rundung der
Zwischenwerte `c_T`/`c_C` auf drei Nachkommastellen. Beide Werte
bestätigen sich gegenseitig.

**Vergleich mit GL24h:** `S_j,ini(GL75) ≈ 15.556,5 kNm/rad` liegt rund
`24 %` über dem GL24h-Pendant (`12.540,8 kNm/rad`, R2-GL24h-CALC-022,
ASSY-verstärkt). Konsistent damit, dass sowohl `c_T` (`70,831` vs.
`53,300 kN/mm`) als auch `c_C` (`165,545` vs. `160,137 kN/mm`) für GL75
höher liegen als die entsprechenden — teils ASSY-verstärkten —
GL24h-Werte, obwohl GL75 gänzlich unverstärkt ist (kein ASSY,
R2-GL75-OPQ-002 RESOLVED): das deutlich höhere `E_90,mean`/`G_mean`
von BauBuche kompensiert den fehlenden Verstärkungsschritt vollständig.

**Status:** Erste vollständige Anfangsrotationssteifigkeit der
Rahmenecke R2/GL75. Beruht — wie das GL24h-Pendant R2-GL24h-CALC-022 —
auf zwei noch offenen/unbestätigten Punkten: (1) der
Kombinationsformel selbst (R2-COMMON-HYP-001, `CLAUDE_DRAFT`,
`reviewed: false`), (2) der Anwendung desselben Hebelarms `z=560mm` auf
die Steifigkeits- statt nur die Tragfähigkeitskette (R2-COMMON-OPQ-006
bleibt `OPEN`). Zusätzlich erbt dieser Wert alle bereits in
R2-GL75-CALC-008/011 dokumentierten Vorbehalte: `c_c,0`-
Modellierungsannahme `l=240mm` (R2-COMMON-OPQ-011, `certainty:
ASSUMED`), der mit Vorsicht zu verwendende Stangengruppen-Messwert
(deutlicher Ausreißer, R2-GL75-II-T-B-BR-22-RES-003) sowie die
materialunabhängige, noch nicht mit der Betreuerin abgestimmte
`G_r,mean=500 N/mm²`-Annahme (R2-COMMON-ASS-003) für die
Sperrholzverstärkung im Schubfeld. Als laufende Arbeitsthese zu
behandeln, nicht als bestätigtes Endergebnis.
