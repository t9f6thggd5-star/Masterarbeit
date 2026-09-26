---
calculation_id: R1-GL24h-CALC-009
scope:
  connection: R1
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature: Buchholz2025
  experimental_data:
  assumptions: R1-COMMON-ASS-001, R1-COMMON-ASS-002
method: >
  Anfangsrotationssteifigkeit der Rahmenecke nach dem Federmodell
  Buchholz2025 Gl. (1)–(5) (R1-COMMON-DEC-004). Zugseite je Bauteil
  c_t = c_v,f und c_br,par in Reihe, Träger und Stütze in Reihe
  (Gl. 2); c_v,f = gemessene 4×8-Gruppensteifigkeit (2 · K_ser des
  2×8-Zugversuchs), c_br,par vorläufig starr (R1-COMMON-OPQ-005).
  Druckseite vorläufig starr (R1-COMMON-ASS-002, Platzhalter 1E+99 für
  c_v,f und c_c,0). Schlitzblech starr (R1-COMMON-DEC-003). Kräftepaar
  nach Gl. (3) mit z = 550 mm, dazu vier Drehfedern C_rot,v,f nach
  Gl. (4)/(5) mit K_ser nach FprEN Tab. 11.12 (R1-GL24h-DEC-010).
equations: >
  c_t = 1/(1/c_v,f + 1/c_br,par); c_t,tot = 1/(1/c_t + 1/c_t);
  c_c,tot = 1/(1/c_v,f + 1/c_c,0 + 1/c_c,0 + 1/c_v,f);
  C_rot,t+c = z²/(1/c_t,tot + 1/c_c,tot); C_rot,v,f = I_p · K_ser;
  C_rot,tot = C_rot,t+c + 4 · C_rot,v,f.
result:
  quantity: Anfangsrotationssteifigkeit C_rot,tot der Rahmenecke R1 (GL24h)
  value: 168996.9
  unit: kNm/rad
  original_value:
  original_unit:
source_file: >
  R1/COMMON/calculations/20260109_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet "Rahmenecke GL24h SD", Stand 2026-09-26 (vom Nutzer
  angelegt, per openpyxl mit data_only=True/False geprüft, Datei-mtime
  1790430683000): I15 c_br,par = 1E+99, I18 c_v,f = 559,04 kN/mm (=J7*2),
  I21 c_t = 559,04 kN/mm, I24 c_t,tot = 279,52 kN/mm (=1/(1/I21+1/I21)),
  N15/N18 c_v,f/c_c,0 Druck = 1E+99, N21 c_c,tot = 2,5E+98, N27 C_rot,t+c
  = 84.554,8 kNm/rad (=C101^2/(1/I24+1/N21)*10^-3, C101 = z = 550 mm),
  I27 K_ser = 17,963 kN/mm, I37 I_p = 1.175.200 mm², I40 C_rot,v,f =
  21.110,5 kNm/rad, N29 C_rot,tot = 168.996,9 kNm/rad (=N27+4*I40).
certainty: CALCULATED
superseded_by:
---

**Rechnung:**

```
c_t,tot   = 1/(1/559,04 + 1/559,04)          = 279,52 kN/mm
C_rot,t+c = 550² · 279,52 · 10⁻³              = 84.554,8 kNm/rad
C_rot,v,f = 1.175.200 · 17,963 · 10⁻³         = 21.110,5 kNm/rad
C_rot,tot = 84.554,8 + 4 · 21.110,5            = 168.996,9 kNm/rad
```

Kräftepaar und Drehfedern tragen je etwa die Hälfte bei.

**Vorläufig, abhängig von:** c_br,par starr (R1-COMMON-OPQ-005),
Druckseite starr bis zur Auswertung der Druckversuche (R1-COMMON-ASS-002;
obere Grenze der Steifigkeit), z = 550 mm auch bei Kontaktpressung
(R1-COMMON-OPQ-006), K_ser für die Drehfeder Normwert oder Versuchswert
c_v,f/32 = 17,47 kN/mm (offen, R1-GL24h-DEC-010; Σ C_rot,v,f −2,8 %),
Zugverformung des Holzes nicht enthalten (R1-COMMON-OPQ-005 (b)).
