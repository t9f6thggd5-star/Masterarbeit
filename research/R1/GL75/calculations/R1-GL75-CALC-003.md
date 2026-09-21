---
calculation_id: R1-GL75-CALC-003
scope:
  connection: R1
  material: GL75
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024, DIN-EN-1995-1-1-2010
  literature:
  experimental_data:
  assumptions:
method: >
  Sensitivität der effektiven Anzahl n_ef nach FprEN Tab. 11.10 (7)
  (LVL und GLVL) für die BauBuche/GL75-Variante des R1-Anschlusses
  (n_0=8, d=12mm, a=min(a_1; a_3,t)=80mm) in Abhängigkeit von der
  Dicke t nach Tab. 11.10 (9). Variante A: t = t_ms = 12mm (Stahlblech als
  Innenteil, wie im Blatt und in R1-GL75-CALC-001). Variante B (dieser
  Eintrag, Hauptwert): t = min{2·t_1; 2·t_2} = 144mm, das
  Stahl-Innenteil wird nicht als t_ms angesetzt. Welche Variante gilt, ist
  offen (R1-GL75-OPQ-002); B ist die Lesart von Claude
  (CLAUDE_DRAFT), nicht vom Nutzer bestätigt.
equations: >
  FprEN 1995-1-1:2024, Tab. 11.10 (7): n_ef = min{n_0; n_0^0,9 ·
  (t·a/(50·d²))^(1/4)}, mit (8) a = min{a_1; a_3,t} für n_0 ≥ 2 und (9)
  t = min{2·t_1; 2·t_2; t_ms} bei zweischnittigen Verbindungen. Vergleich:
  DIN EN 1995-1-1 Gl. (8.34), siehe R1-GL75-CALC-002.
result:
  quantity: Effektive Anzahl n_ef (BauBuche/GL75, FprEN Tab. 11.10 (7), Variante B, t=144mm)
  value: 7.308
  unit: "-"
  original_value: 7.308209423296034
  original_unit: "-"
source_file: >
  Eigene Nachrechnung (Claude, 2026-09-21) mit den Eingaben aus
  R1/COMMON/calculations/20260109_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL75 SD" (C12 = 72mm, C7 = 6mm als halbe Blechdicke, C22,
  C25-C27, C69 = 21,451 kN); Variante A entspricht C52 = 3,9266.
certainty: CALCULATED
superseded_by:
---

Rechnung ist für beide Varianten gegen die Excel-Zelle C52 (Variante A,
3,9266) nachvollzogen; Variante B ändert nur t von 12mm auf 144mm.

**Abhängigkeit von t** (n_0 = 8, a = 80mm, d = 12mm; F je 2×8-Gruppe mit
F_D,k = 21,451 kN je Scherfuge und Dübel (C69), n_90 = 2, m = 2):

| t | n_ef | F (2×8) | F (4×8) |
|---|---|---|---|
| 12 mm (Blech, Variante A, Blatt C52/C72) | 3,927 | 336,9 kN | 673,8 kN |
| 24 mm | 4,670 | 400,7 kN | 801,3 kN |
| 72 mm (= t_1) | 6,145 | 527,3 kN | 1054,6 kN |
| 144 mm (= 2·t_1, Variante B) | 7,308 | 627,1 kN | 1254,2 kN |
| DIN Gl. (8.34), nicht von t abhängig | 5,499 | 471,8 kN | 943,7 kN |

**Warum B über DIN liegt:** Beide Formeln enthalten n_0^0,9 = 6,50. Der
Wurzelterm ist bei DIN (a_1/(13d))^(1/4) = 0,846, bei FprEN (7) mit
t = 144mm (t·a/(50d²))^(1/4) = 1,125. Beide Formeln sind gleich, wenn
t ≈ 50·d/13 = 46mm (bei a = a_1); darüber liefert (7) mehr als DIN, darunter
weniger. Gedeckelt ist n_ef nur durch n_0 = 8 (erreicht bei t ≈ 207mm).
Die Herleitung der Formel (7) wurde in den Quellen nicht gefunden (siehe
R1-GL75-OPQ-002).

**Vergleich mit den Versuchen** I-T-B-SD-28-1 bis -3 (2×8, Höchstlasten aus
den Rohdaten von Claude ausgelesen, nicht als Versuchsergebnis im Wiki
abgelegt): F_max = 579,7 / 639,7 / 644,5 kN, Mittel 621,3 kN. Die
Einordnung ist nicht eindeutig: F_D,k ist eine Schätzung mit Mittelwerten
von Rohdichte und Fließmoment, und der Versagensmodus der GL75-Versuche ist
im Wiki nicht dokumentiert. War das Stahlblech begrenzend (Nettoquerschnitt),
sind die Versuchswerte nur eine Untergrenze der Dübelgruppe und
unterscheiden die Varianten nicht.

**Folge für die Excel:** Bei Variante B läge die FprEN-Tragfähigkeit
(C72-Ersatz) über der DIN-Tragfähigkeit (C71/C30, 943,7 kN); die
Beschriftungen "kleineres n_ef" (A101) und "nef=3,93" (A97) träfen nicht
mehr zu. Die Beschriftungen D47 und D72 nennen "Tab. 11.10 (6)", obwohl mit
(7) gerechnet wird. Im R2-Blatt "Rahmenecke GL75 SD" (C48, n_0 = 3,
a_1 = 85mm, n_ef = 2,31) wird für GL75 dagegen die Zeile (6) angesetzt
(anderer Anschluss, nicht geprüft; Querverweis, gehört zu R2).
