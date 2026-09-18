---
calculation_id: R2-GL75-CALC-011
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data: R2-GL75-II-T-B-BR-22-RES-003
  assumptions: R2-COMMON-DEC-003
method: >
  Gesamt-Zugseitensteifigkeit `c_T` als Serienschaltung dreier Federn,
  strukturell identisch zur GL24h-Kette (R2-GL24h-CALC-021,
  R2-GL24h-INT-001): Stangengruppe (4 Gewindestangen), Querdruck unter
  der Ankerplatte (`c_c,90`, Zugseite), Schubfeld (`c_v,ges`). Für die
  Stangengruppe wird direkt der gepoolte Messwert angesetzt (gemäß
  R2-COMMON-DEC-003), statt zunächst einen rein rechnerischen FprEN-Wert
  zu bilden und später zu ersetzen (wie bei GL24h, CALC-002→014) — für
  GL75 gibt es ohnehin keinen ASSY-Verstärkungsschritt, der eine
  Zwischenversion nötig gemacht hätte.
equations: 'Serienfeder: 1/c_T = 1/c_Stangen,4x + 1/c_c,90 + 1/c_v,ges.'
result:
  quantity: Gesamt-Zugseitensteifigkeit c_T, GL75
  value: 70.831
  unit: kN/mm
  original_value: 70831.3
  original_unit: N/mm
source_file:
certainty: CALCULATED
superseded_by:
---

**Eingangswerte:**
- `c_Stangen,4x = 1.119,496 kN/mm` — gepoolter K_ser-Messwert, n=6
  (R2-GL75-II-T-B-BR-22-RES-003, gemäß R2-COMMON-DEC-003 direkt aus
  Blatt "Überblick" der Steifigkeiten-Auswertungsdatei übernommen).
  **Vorbehalt:** dort selbst als "mit Vorsicht zu verwenden" markiert
  (deutlicher Ausreißer bei einem Prüfkörper, Verhältnis oben/unten nur
  ≈23 %) — dieser Vorbehalt gilt direkt auch für `c_T` hier.
- `c_c,90 = 158,021 kN/mm` (Zugseite, unverstärkt, R2-GL75-CALC-009).
- `c_v,ges = 145 kN/mm` (R2-GL75-CALC-010).

**Rechnung:**

```
1/c_T = 1/1.119,496 + 1/158,021 + 1/145
      = 0,0008933 + 0,0063283 + 0,0068966
      = 0,0141181
c_T   = 70,831 kN/mm
```

**Plausibilitätshinweis:** Wie bei GL24h (R2-GL24h-INT-001) dominiert
die weichste Feder die Serienschaltung — hier `c_v,ges=145 kN/mm`, nicht
die (durch den hohen Messwert extrem steife) Stangengruppe. Der
`c_T`-Wert liegt bei `70,831 kN/mm` deutlich über dem GL24h-Pendant
(`53,300 kN/mm`, ASSY-verstärkt, R2-GL24h-CALC-021) — konsistent mit dem
durchgängig höheren `E_90,mean`/`G_mean` von BauBuche und dem Umstand,
dass GL75 keine Verstärkung braucht, um dennoch steifer zu sein.

**Status:** Löst R2-GL75-OPQ-001 (erste vollständige
Zugseiten-Steifigkeitskette für GL75 liegt jetzt vor). Beruht auf dem
mit Vorsicht zu verwendenden Stangengruppen-Messwert (s. o.) sowie auf
der noch nicht mit der Betreuerin abgestimmten `G_r,mean=500 N/mm²`-
Annahme (R2-COMMON-ASS-003, materialunabhängig, bisher nur als
Nutzer-Annahme dokumentiert, kein eigener OPQ-Eintrag dafür bisher).
Mit `c_T` und `c_C` (R2-GL75-CALC-008, `165,545 kN/mm`) sowie `z=560mm`
(fix, R2-COMMON-ASS-006) ist jetzt auch `S_j,ini(GL75)` nach
R2-COMMON-HYP-001 berechenbar — noch nicht durchgeführt.
