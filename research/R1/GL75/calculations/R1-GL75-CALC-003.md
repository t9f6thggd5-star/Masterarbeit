---
calculation_id: R1-GL75-CALC-003
scope:
  connection: R1
  material: GL75
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions:
method: >
  Effektive Anzahl n_ef nach FprEN Tab. 11.10 (7) (LVL und GLVL) für die
  BauBuche/GL75-Variante des R1-Anschlusses (n_0=8, d=12mm,
  a=min(a_1; a_3,t)=80mm). Die Dicke t nach Tab. 11.10 (9) wird als
  t = min{2·t_1; 2·t_2} = 144mm angesetzt; das Stahl-Innenteil (12mm) geht
  nicht als t_ms ein. Diese Auslegung hat der Nutzer am 2026-09-21
  bestätigt (R1-GL75-OPQ-002, RESOLVED); sie ist eine Entscheidung des
  Nutzers, im FprEN-Normtext nicht ausdrücklich geregelt. Ersetzt
  R1-GL75-CALC-001 (t = t_ms = 12mm, n_ef = 3,927).
equations: >
  FprEN 1995-1-1:2024, Tab. 11.10 (7): n_ef = min{n_0; n_0^0,9 ·
  (t·a/(50·d²))^(1/4)}, mit (8) a = min{a_1; a_3,t} für n_0 ≥ 2 und (9)
  t = min{2·t_1; 2·t_2} (t_ms entfällt bei Stahl-Innenteil, siehe oben).
  Vergleich: DIN EN 1995-1-1 Gl. (8.34), siehe R1-GL75-CALC-002.
result:
  quantity: Effektive Anzahl n_ef (BauBuche/GL75, FprEN Tab. 11.10 (7), t=144mm)
  value: 7.308
  unit: "-"
  original_value: 7.308209423296034
  original_unit: "-"
source_file: >
  R1/COMMON/calculations/20260109_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL75 SD", Zellen C47/C52 (n_ef = 7,308209), C48 (t = 144mm,
  Formel =MIN(2*C12;2*C12)), C30/C72 (1254,159 kN); per openpyxl mit
  data_only=True ausgelesen, Stand der Datei am 2026-09-21 (vom Nutzer
  nach der Bestätigung angepasst)
certainty: CALCULATED
superseded_by:
---

**Ergebnis und Verwendung:** n_ef = 7,308 (C52). Mit F_D,k = 21,451 kN je
Scherfuge und Dübel (C69, Fließmoment aus den Biegeversuchen), n_90 = 4 und
m = 2 ergibt sich die Höchstlast F_est der 4×8-Gruppe zu 1254,16 kN
(C72, C30); je getesteter 2×8-Gruppe (n_90 = 2) 627,08 kN. Der Nutzer
bestätigte am 2026-09-21, dass n_ef = 7,31 der Wert ist, den er für F_est
verwendet.

**Abhängigkeit von t** (n_0 = 8, a = 80mm, d = 12mm; F je 2×8-Gruppe):

| t | n_ef | F (2×8) | F (4×8) |
|---|---|---|---|
| 12 mm (Blech als t_ms, frühere Auslegung, R1-GL75-CALC-001) | 3,927 | 336,9 kN | 673,8 kN |
| 24 mm | 4,670 | 400,7 kN | 801,3 kN |
| 72 mm (= t_1) | 6,145 | 527,3 kN | 1054,6 kN |
| 144 mm (= 2·t_1, bestätigt) | 7,308 | 627,1 kN | 1254,2 kN |
| DIN Gl. (8.34), nicht von t abhängig | 5,499 | 471,8 kN | 943,7 kN |

**Warum (7) hier über DIN liegt:** Beide Formeln enthalten n_0^0,9 = 6,50.
Der Wurzelterm ist bei DIN (a_1/(13d))^(1/4) = 0,846, bei FprEN (7) mit
t = 144mm (t·a/(50d²))^(1/4) = 1,125. Beide Formeln sind gleich, wenn
t ≈ 50·d/13 = 46mm (bei a = a_1); darüber liefert (7) mehr als DIN, darunter
weniger. Gedeckelt ist n_ef nur durch n_0 = 8 (erreicht bei t ≈ 207mm).
Die Herleitung der Formel (7) wurde in den Quellen nicht gefunden (siehe
R1-GL75-OPQ-002).

**Vergleich mit den Versuchen** I-T-B-SD-28-1 bis -3 (2×8; Höchstlasten laut
Excel, Zellen I2:I4 des Blattes "Rahmenecke GL75 SD"): F_max = 581,0 /
640,2 / 645,7 kN, Mittel 622,3 kN. Verhältnis F_max zu F_est (627,08 kN):
0,93 / 1,02 / 1,03, Mittel 0,99. Die Einordnung bleibt eingeschränkt: F_D,k
ist eine Schätzung mit Mittelwerten von Rohdichte und Fließmoment, und der
Versagensmodus der GL75-Versuche ist im Wiki nicht dokumentiert. War das
Stahlblech begrenzend (Nettoquerschnitt), sind die Versuchswerte nur eine
Untergrenze der Dübelgruppe.

**Stand im Excel (2026-09-21):** C48 = MIN(2*C12;2*C12) = 144mm (beide
Argumente gleich, t_ms/C7 geht nicht mehr ein); C47 = MIN(C50;C52) = 7,308;
C61 (mit normativem M_y,k, C59) = 833,2 kN. Nicht angepasst: die
Beschriftungen D47 und D72 nennen "Tab. 11.10 (6)", obwohl mit (7) gerechnet
wird; A96 "nef=5,5" und A97 "nef=3,93" stehen noch da, C96 und C97 sind
jetzt beide 1254,16 kN (C100 = C101 = 689,8 kNm); C98 (Versuche) =
I7·2 = 1244,54 kN, damit M_max aus Versuchen 684,5 kNm (C102). Das R2-Blatt
"Rahmenecke GL75 SD" (C48, n_0 = 3, a_1 = 85mm, n_ef = 2,31) setzt für GL75
dagegen die Zeile (6) an (anderer Anschluss, nicht geprüft; Querverweis,
gehört zu R2).
