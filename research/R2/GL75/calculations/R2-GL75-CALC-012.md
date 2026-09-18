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
  value: 15556.61
  unit: kNm/rad
  original_value: 15556612793.72842
  original_unit: N*mm/rad
source_file: >
  **Update (2026-09-18):** Der Nutzer hat die vollständige Kombination
  jetzt auch im R2-Excel ergänzt — Sheet "Rahmenecke GL75 SD", Zelle
  I89 (Formel `=C86^2/(1/M84+1/I70)*10^-3`, Einheit `kNm/rad` in H89),
  Excel-Wert `15.556,61279372842`, per openpyxl mit
  data_only=True/False geprüft. `C86` ist die Zelle "innerer Hebelarm
  z" (=C84="Abstand Zugkraft zu Druckkraft"=560mm) — **korrigiert eine
  frühere Fehlangabe**: R2-GL24h-CALC-022 hatte für dieses Blatt
  fälschlich die Zellen "I54/I56" als Fundstelle von `z` genannt; die
  tatsächliche Fundstelle ist `C84`/`C86` (siehe auch die dortige
  Korrektur). `M84`=`c_T` (R2-GL75-CALC-011, Excel-Wert
  `70,83175417853643`), `I70`=`c_C` (R2-GL75-CALC-008, Excel-Wert
  `165,54460235863317`). Der Excel-Wert deckt sich exakt mit dem vom
  Nutzer unabhängig im Chat berechneten Ergebnis (`15.556,61`) — die
  vorherige Version dieses Eintrags hatte auf Basis der im Wiki auf
  drei Nachkommastellen gerundeten `c_T`/`c_C`-Werte nur `≈15.556,5`
  ermittelt; mit der jetzt vorliegenden Excel-Fundstelle wird der
  präzisere, formal referenzierte Wert `15.556,61` übernommen.
certainty: CALCULATED
superseded_by:
---

**Eingangswerte (Excel-exakt):** `c_T = 70,83175 kN/mm` (M84,
R2-GL75-CALC-011), `c_C = 165,54460 kN/mm` (I70, R2-GL75-CALC-008),
`z = 560 mm` (C86, materialunabhängig, R2-COMMON-ASS-006).

**Rechnung (Excel, Zelle I89):**

```
S_j,ini = z² / (1/c_T + 1/c_C)
        = 560² / (1/70,83175 + 1/165,54460)
        = 15.556,613 kNm/rad
```

Mit den im Wiki auf drei Nachkommastellen gerundeten Eingangswerten
(`c_T=70,831`, `c_C=165,545`) ergibt die Handrechnung `≈15.556,5
kNm/rad` — die minimale Differenz (`≈0,1 kNm/rad`, `<0,001 %`) ist
reine Rundungspropagation aus der Zwischenwert-Rundung und bestätigt
den Excel-Wert (siehe Chat-Diskussion vom 2026-09-18: Sensitivität von
`S_j,ini` gegenüber Rundung von `c_T`/`c_C` liegt bei `≈154` bzw.
`≈28 kNm/rad` pro `kN/mm`).

**Vergleich mit GL24h:** `S_j,ini(GL75) = 15.556,61 kNm/rad` liegt rund
`24 %` über dem GL24h-Pendant (`12.540,8 kNm/rad`, R2-GL24h-CALC-022,
ASSY-verstärkt). Konsistent damit, dass sowohl `c_T` (`70,832` vs.
`53,300 kN/mm`) als auch `c_C` (`165,545` vs. `160,137 kN/mm`) für GL75
höher liegen als die entsprechenden — teils ASSY-verstärkten —
GL24h-Werte, obwohl GL75 gänzlich unverstärkt ist (kein ASSY,
R2-GL75-OPQ-002 RESOLVED): das deutlich höhere `E_90,mean`/`G_mean`
von BauBuche kompensiert den fehlenden Verstärkungsschritt vollständig.

**Status:** Erste vollständige Anfangsrotationssteifigkeit der
Rahmenecke R2/GL75, jetzt sowohl im Wiki als auch als eigener Block im
R2-Excel dokumentiert (Zelle I89 — Achtung: die Zeilenbeschriftung in
A89 lautet dort irrtümlich "maximales Moment", ein reines
Excel-Beschriftungsversehen ohne Auswirkung auf die Formel/den Wert,
dem Nutzer zur Info). Beruht — wie das GL24h-Pendant R2-GL24h-CALC-022
— auf zwei noch offenen/unbestätigten Punkten: (1) der
Kombinationsformel selbst (R2-COMMON-HYP-001, `CLAUDE_DRAFT`,
`reviewed: false`), (2) der Anwendung desselben Hebelarms `z=560mm` auf
die Steifigkeits- statt nur die Tragfähigkeitskette (R2-COMMON-OPQ-006
bleibt `OPEN`). Zusätzlich erbt dieser Wert alle bereits in
R2-GL75-CALC-008/011 dokumentierten Vorbehalte: `c_c,0`-
Modellierungsannahme `l=240mm` (R2-COMMON-OPQ-011, `certainty:
ASSUMED`), der mit Vorsicht zu verwendende Stangengruppen-Messwert
(deutlicher Ausreißer, R2-GL75-II-T-B-BR-22-RES-003) sowie die
materialunabhängige, noch nicht mit der Betreuerin abgestimmte
`G_r,mean=500 N/mm²`-Annahme (R2-COMMON-ASS-003, jetzt mit
Excel-Quellenangabe "KLH ETA Scheibenbeanspruchung"). Als laufende
Arbeitsthese zu behandeln, nicht als bestätigtes Endergebnis.
