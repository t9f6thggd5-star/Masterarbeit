---
calculation_id: R3-GL24h-CALC-016
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature: Buchholz2025, ScheibmairQuenneville2014
  experimental_data:
  assumptions: >
    R3-COMMON-DEC-009 (Modell Druckseite, Nulllinie aus Gleichgewicht,
    Zustand nach dem Öffnen der Fuge, ohne Vorspannung); c_t,tot = 31,023 kN/mm
    (R3-GL24h-CALC-014); d = 720 mm (Abstand Zugkraft zum inneren
    Stützenrand, Excel "Rahmenecke GL24h SD" C79); b = 160 mm (I95);
    h = 800 mm; E_90,mean = 300, E_0,mean = 11 500 N/mm² (Holzkennwerte
    D35/D34 = DIN EN 14080:2013 Tab. 5).
method: >
  Druckseite nach R3-COMMON-DEC-009: c_c,90 = 2·E_90,mean/(h_ef·(1/A + 1/A_ef))
  (FprEN Gl. 9.31, S. 153) mit A = b·x, A_ef = b·(x + 2·h_ef), h_ef =
  min(0,4·800; 140) = 140 mm (Gl. 8.11, S. 88; 45° nach Tab. 8.2, S. 87);
  c_c,0 = E_0,mean·b·x/x = E_0,mean·b (l_0 = x wie ScheibmairQuenneville2014
  Gl. 27–30); c_c,tot = (1/c_c,90 + 1/c_c,0)⁻¹
  (Buchholz2025 Gl. 6); k = c_c,tot/(b·x); x aus c_t,tot·(d − x) = ½·k·b·x²,
  iteriert bis zur Konvergenz; z = d − x/3; S_j,ini = c_t,tot·(d − x)·z.
equations: >
  Konvergiert: x = 256,8 mm; A = 41 095 mm², A_ef = 85 895 mm²;
  c_c,90 = 2·300/(140·(1/41 095 + 1/85 895)) = 119,13 kN/mm;
  c_c,0 = 11 500·160 = 1 840 kN/mm; c_c,tot = 111,88 kN/mm;
  k = 2,723 N/mm³; Kontrolle T/φ = C/φ = 14,37·10⁶ N/rad;
  z = 720 − 256,8/3 = 634,4 mm;
  S_j,ini = 31 023 · (720 − 256,8) · 634,4 = 9,115·10⁹ Nmm/rad.
result:
  quantity: Anfangsrotationssteifigkeit S_j,ini R3/GL24h nach dem Öffnen der Fuge (ohne Vorspannung, ohne C_v,f,rot)
  value: 9115
  unit: kNm/rad
  original_value:
  original_unit:
source_file: >
  Gerechnet im Chat 2026-09-30 (Python); Eingangswerte aus
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl. Holzlaschen.xlsx
  (Stand 2026-09-30). Im Excel umgesetzt 2026-09-30 (Struktur vom Nutzer,
  vervollständigt von Claude): Sheet "Rahmenecke GL24h SD", Eingänge
  I160–I165, Iteration G168:N177 (10 Zeilen, Start x = 400 mm), Ergebnisse
  I179 (x), I182 (c_c,tot), I183 (z), I184 (S_j,ini), Kontrolle I185/I186;
  per LibreOffice nachgerechnet, Werte identisch.
certainty: CALCULATED
superseded_by:
---

**Zwischenergebnisse:** x = 256,8 mm, c_c,tot = 111,88 kN/mm, z = 634,4 mm.

**Empfindlichkeit:**

| Variante | x [mm] | c_c,tot [kN/mm] | z [mm] | S_j,ini [kNm/rad] |
|---|---|---|---|---|
| Hauptwert (h_ef = 140, beidseitig 45°) | 256,8 | 111,9 | 634,4 | 9 115 |
| Riegel ohne Ausbreitung (untere Grenze) | 287,2 | 93,5 | 624,3 | 8 381 |
| h_ef = 280 mm (Gl. 8.10), beidseitig | 320,8 | 77,2 | 613,1 | 7 594 |
| l_0 = 400 mm fest statt l_0 = x | ≈ 260 | ≈ 109,5 | ≈ 633 | ≈ 9 030 |
| zum Vergleich: x = 400 mm fest (bisher), z = 586,7 | 400 | 157,9 | 586,7 | ≈ 8 920 |
| Druckseite starr | – | ∞ | 720 | – |

**Iteration (Start x = 400 mm):** 400,0 → 266,9 → 257,7 → 256,9 → 256,8 mm
(c_c,90 172,7 → 123,0 → 119,5 → 119,2 → 119,1 kN/mm).

**Vorbehalte:** gilt nur nach dem Öffnen der Fuge (Vorspannung,
R3-COMMON-OPQ-007); Gl. (9.31) für gleichmäßige Pressung angewendet auf
dreieckige Pressung (R3-COMMON-DEC-009); h_ef = 140 mm noch nicht
ausdrücklich bestätigt; C_v,f,rot nicht angesetzt (R3-COMMON-DEC-005);
Zugseite mit den Vorbehalten von R3-GL24h-CALC-013/014 (n = 1 Riegelseite).
