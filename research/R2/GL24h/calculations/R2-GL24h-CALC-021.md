---
calculation_id: R2-GL24h-CALC-021
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: Bejtka-2005
  experimental_data: R2-GL24h-II-T-S-BR-22-RES-003
  assumptions:
method: >
  Serienschaltung der vier Komponenten des Zugpfads gemäß der in
  R2-COMMON-DEC-004 bestätigten Federmodell-Topologie (Fig. 7,
  FragiacomoBatchelar2012a, R2-COMMON-CLAIM-031): Stangengruppe
  (teilweise messwertbasiert, R2-GL24h-CALC-014), Ankerplatten-
  Biegesteifigkeit `c_t,ep` (vernachlässigt, =1e99), Querdruck-
  steifigkeit `c_c,90` und Schubfeld `c_v` (R2-GL24h-CALC-003):
  `1/c_T = 1/c_Stange,4x + 1/c_t,ep + 1/c_c,90 + 1/c_v`.

  Gegenüber R2-GL24h-CALC-015 (bisher aktueller Wert) wird hier
  erstmals der ASSY-VERSTÄRKTE Bejtka-Wert für `c_c,90`
  (111,339 kN/mm, Zugseite, A=1, R2-COMMON-CALC-001) statt des
  unverstärkten FprEN-Werts (100,866 kN/mm, R2-GL24h-CALC-001)
  eingesetzt.
equations: Serienfeder (1/c_1+1/c_2+1/c_3+1/c_4)^-1.
result:
  quantity: >
    Gesamt-Zugseitensteifigkeit c_T, GL24h (teilweise messwertbasiert,
    mit ASSY-verstärktem c_c,90)
  value: 53.300
  unit: kN/mm
  original_value: 53300.156
  original_unit: N/mm
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen L130-L131
  (per openpyxl mit data_only=True ausgelesen, Stand der abgelegten
  Datei am 2026-09-17)
certainty: CALCULATED
superseded_by:
---

**Eingangswerte (Zelle → Wert):** `L94` (c_Stange×4, II-T-S-BR-22,
Messwert) `= 862,53 kN/mm`, `L97` (c_t,ep) `= 1e99` (vernachlässigt),
`L108` (c_c,90,verstärkt, Zugseite, A=1) `= 111,339 kN/mm`
(R2-COMMON-CALC-001), `L127` (c_v, Schubfeld) `= 116,0 kN/mm`
(R2-GL24h-CALC-003).

**Rechnung:**

```
c_T = (1/862,53 + 1/1e99 + 1/111,339 + 1/116,0)^-1
    = (0,0011594 + 0 + 0,0089815 + 0,0086207)^-1
    = 53,300 kN/mm
```

Gegenüber R2-GL24h-CALC-015 (`50,776 kN/mm`, mit unverstärktem
`c_c,90`) ein Zuwachs von `≈+5,0 %` — deutlich kleiner als der
Zuwachs von `c_c,90` selbst (`+10,4 %`, siehe R2-COMMON-CALC-001),
wieder wegen der Serienfeder-Dominanz durch die inzwischen noch
weichere Komponente `c_v` (Schubfeld, `116,0 kN/mm`, jetzt die
weichste Einzelkomponente der Kette).

**Wichtiger Vorbehalt:** Dieser Wert setzt den ASSY-verstärkten
Bejtka-`c_c,90` als gültig voraus. Der Status dieses Werts ist gemäß
R2-COMMON-CALC-001 weiterhin **nicht offiziell mit der Betreuerin
abgestimmt** — insbesondere hängt er an der Modellgültigkeits-
bedingung (steife Kontaktplatte vorhanden, erfüllt) und an mehreren
unbelegten Bejtka-eigenen Annahmen (Faktor 0,7 in Gl. 63, `f_LA`
Gl. 68 mit `l_ef` als unabhängigem FE-Parameter). Der Nutzer hat den
Wert am 2026-09-17 in die Excel-Kette übernommen ("wir verwenden in
der Folge nur den verstärkten [Wert]") — dieser Eintrag dokumentiert
diese Übernahme wahrheitsgemäß, ändert aber nichts an der weiterhin
ausstehenden fachlichen Absicherung.

Ersetzt R2-GL24h-CALC-015 als aktuellen Wert für `c_T`; CALC-015
bleibt dokumentiert und ist über dessen `superseded_by`-Feld auf
diesen Eintrag verwiesen (CLAUDE.md Abschnitt 13). R2-GL24h-INT-001
(Interpretation der Serienfeder-Mechanik) basiert noch auf dem alten
Wert (`50,776 kN/mm`) und sollte bei Gelegenheit mit den neuen Zahlen
nachgezogen werden — die grundsätzliche Aussage (c_c,90/c_v dominieren
die Nachgiebigkeit, Stangengruppe fällt praktisch heraus) bleibt aber
qualitativ gültig, da c_v jetzt sogar noch dominanter ist.
