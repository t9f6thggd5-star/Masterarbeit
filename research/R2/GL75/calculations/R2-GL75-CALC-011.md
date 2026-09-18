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
  Gesamt-Zugseitensteifigkeit `c_T` als Serienschaltung von vier Federn,
  strukturell identisch zur GL24h-Kette (R2-GL24h-CALC-021,
  R2-GL24h-INT-001): Stangengruppe (4 Gewindestangen), Steifigkeit der
  Ankerplatte selbst (`c_t,ep`, im Excel als starr angenommen, siehe
  Update unten), Querdruck unter der Ankerplatte (`c_c,90`, Zugseite),
  Schubfeld (`c_v,ges`). Für die Stangengruppe wird direkt der gepoolte
  Messwert angesetzt (gemäß R2-COMMON-DEC-003), statt zunächst einen
  rein rechnerischen FprEN-Wert zu bilden und später zu ersetzen (wie
  bei GL24h, CALC-002→014) — für GL75 gibt es ohnehin keinen
  ASSY-Verstärkungsschritt, der eine Zwischenversion nötig gemacht
  hätte.
equations: >
  Serienfeder: 1/c_T = 1/c_Stangen,4x + 1/c_t,ep + 1/c_c,90 +
  1/c_v,ges.
result:
  quantity: Gesamt-Zugseitensteifigkeit c_T, GL75
  value: 70.831
  unit: kN/mm
  original_value: 70831.3
  original_unit: N/mm
source_file: >
  **Update (2026-09-18):** Der Nutzer hat den vollständigen
  Zugseiten-Rechenweg jetzt auch im R2-Excel ergänzt — Sheet
  "Rahmenecke GL75 SD", Block K51:M84. `M55` (c_Stangen,4x,
  `=N16`, Wert `1.119,5`, Verweis in N55 "siehe M16 Auswertung
  Anfangssteifigkeit"), `M58` (c_t,ep, Stahlplatten-Nachgiebigkeit,
  Wert `1E+99`, Notiz N58 "Annahme wird vernachlässigt" — Platte also
  bewusst als starr angenommen, nicht Teil der ursprünglich hier
  dokumentierten 3-Feder-Kette, numerisch aber irrelevant), `M61`
  (c_c,90, R2-GL75-CALC-009), `M80` (c_v,ges, R2-GL75-CALC-010), `M84`
  (c_T gesamt, `=(1/M55+1/M58+1/M61+1/M80)^-1`, Excel-Wert
  `70,83175417853643`) — per openpyxl geprüft. Kleine Abweichung zum
  hier verwendeten `c_Stangen,4x=1.119,496` (R2-GL75-II-T-B-BR-22-RES-003):
  Excel referenziert stattdessen `N16=1.119,5` (gerundeter Wert
  derselben Prüfserie, in diesem Blatt hinterlegt) — Differenz
  `<0,01 kN/mm`, praktisch bedeutungslos. Der Excel-Wert `70,83175`
  rundet exakt auf `70,832 kN/mm` (drei Nachkommastellen); der hier
  dokumentierte Wert `70,831` stammt aus der Handrechnung mit dem
  RES-003-Rohwert und wird beibehalten, da beide Werte praktisch
  identisch sind (Differenz `<0,001 kN/mm`, <0,002 %) und die
  Handrechnung nachvollziehbar bleibt.
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
- `c_t,ep = ∞` (Stahlplatten-Nachgiebigkeit, im Excel bewusst
  vernachlässigt/als starr angenommen, s. o.) — trägt nicht zur
  Nachgiebigkeit bei, daher hier ursprünglich nicht als eigene Feder
  geführt.
- `c_c,90 = 158,021 kN/mm` (Zugseite, unverstärkt, R2-GL75-CALC-009).
- `c_v,ges = 145 kN/mm` (R2-GL75-CALC-010).

**Rechnung:**

```
1/c_T = 1/1.119,496 + 1/158,021 + 1/145
      = 0,0008933 + 0,0063283 + 0,0068966
      = 0,0141181
c_T   = 70,831 kN/mm
```

(Der vernachlässigbare `c_t,ep`-Term entfällt hier, da `1/∞=0`.)

**Plausibilitätshinweis:** Wie bei GL24h (R2-GL24h-INT-001) dominiert
die weichste Feder die Serienschaltung — hier `c_v,ges=145 kN/mm`, nicht
die (durch den hohen Messwert extrem steife) Stangengruppe. Der
`c_T`-Wert liegt bei `70,831 kN/mm` deutlich über dem GL24h-Pendant
(`53,300 kN/mm`, ASSY-verstärkt, R2-GL24h-CALC-021) — konsistent mit dem
durchgängig höheren `E_90,mean`/`G_mean` von BauBuche und dem Umstand,
dass GL75 keine Verstärkung braucht, um dennoch steifer zu sein.

**Status:** Löst R2-GL75-OPQ-001 (erste vollständige
Zugseiten-Steifigkeitskette für GL75 liegt jetzt vor, seit 2026-09-18
auch als eigener Block im R2-Excel nachgebildet, s. o.). Beruht auf dem
mit Vorsicht zu verwendenden Stangengruppen-Messwert (s. o.) sowie auf
der noch nicht mit der Betreuerin abgestimmten `G_r,mean=500 N/mm²`-
Annahme (R2-COMMON-ASS-003, materialunabhängig — jetzt mit
Excel-dokumentierter Quellenangabe "KLH ETA Scheibenbeanspruchung",
siehe R2-GL75-CALC-010). Mit `c_T` und `c_C` (R2-GL75-CALC-008,
`165,545 kN/mm`) sowie `z=560mm` (fix, R2-COMMON-ASS-006) ist
`S_j,ini(GL75)` nach R2-COMMON-HYP-001 berechnet, siehe
R2-GL75-CALC-012 (inzwischen ebenfalls im R2-Excel nachgebildet,
Zelle I89).
