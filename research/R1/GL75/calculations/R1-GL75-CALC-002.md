---
calculation_id: R1-GL75-CALC-002
scope:
  connection: R1
  material: GL75
type: CALCULATION
inputs:
  normative_sources: DIN-EN-1995-1-1-2010, ETA-14-0354-2026
  literature: Gauss2024
  experimental_data:
  assumptions:
method: >
  Effektive Anzahl n_ef der Stabdübel je Reihe in Faserrichtung nach
  DIN EN 1995-1-1 (Eurocode 5 mit A1:2008) für die BauBuche/GL75-Variante
  des R1-Anschlusses, mit n_0=8, d=12mm und a_1=80mm. Dient als
  Gegenüberstellung zur FprEN-Regel (R1-GL75-CALC-001 und -003). Die
  DIN-Formel enthält weder eine Materialunterscheidung noch die
  Bauteildicke; für Stabdübel gilt sie nach 8.6(1) über 8.5.1.1(4).
equations: >
  DIN EN 1995-1-1:2010-12, Gl. (8.34):
  n_ef = min{n; n^0,9 · (a_1/(13·d))^(1/4)}
  (Kraft in Faserrichtung; Gl. (8.35) ist dagegen der Fall rechtwinklig
  zur Faser mit n_ef = n)
result:
  quantity: Effektive Anzahl n_ef (BauBuche/GL75, DIN EN 1995-1-1 Gl. 8.34)
  value: 5.499
  unit: "-"
  original_value: 5.4988558557348375
  original_unit: "-"
source_file: >
  R1/COMMON/calculations/20260109_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL75 SD", Zelle C51 (per openpyxl mit data_only=True
  ausgelesen, Stand der Datei am 2026-09-21)
certainty: CALCULATED
superseded_by:
---

Am 2026-09-21 mit dem Nutzer geprüft; Nutzer hat bestätigt, dass die
Formel im Blatt (C51, Beschriftung "DIN EN 1995 Gl. 8.34") stimmt.

**Nachrechnung:** 8^0,9 · (80/(13·12))^(1/4) = 6,499 · 0,846 = 5,4989.
Formel gegen den Normtext geprüft (DIN EN 1995-1-1:2010-12, 8.5.1.1(4),
Gl. (8.34)); dieselbe Formel gibt Gauß (Gauss2024, Gl. 2-8) mit Verweis
auf Jorissen (1998) wieder.

**Abstände:** a_1 = 80mm ≥ (3+2|cos α|)·d = 60mm; a_3,t = 183mm ≥
max(7d; 80mm) = 84mm (Tabelle 8.5, Stabdübel); a_2 = 50mm ≥ 3d = 36mm
(a_2 laut Nutzer 2026-09-21 wie bei der getesteten Gruppe).

**Anwendbarkeit auf BauBuche:** Die DIN-Formel kennt keine Materialklasse.
Die ETA-14/0354 (Anhang 3, PDF-Seite 17) sieht für Verbindungsmittel in
Träger BauBuche vor: "Die Berechnung der Verbindungsmittel kann gemäß
EN 1995-1-1 erfolgen" (Lochleibungsfestigkeit bei d ≥ 8mm in den
Schmalflächen mit Faktor 0,8) und enthält keine eigene n_ef-Regel. Die
materialspezifische Zeile für LVL/GLVL steht erst im FprEN-Entwurf
(Tab. 11.10 (7), siehe R1-GL75-CALC-001/-003). Ob die Dübel in den
Schmalflächen liegen und der Faktor 0,8 im Blatt berücksichtigt ist, wurde
nicht geprüft.

**Verwendung im Blatt:** C71 (F_D,k,ges = C51·C24·C69·C6 = 943,66 kN)
speist über C30 die Höchstlast F_est der Versuchsblätter (halbiert für die
getestete 2×8-Gruppe: 471,83 kN). C72 rechnet mit dem FprEN-Wert
(C52 = 3,93; 673,84 kN). Die Gegenüberstellung DIN gegen prEN ist vom
Nutzer so gewollt (Bestätigung 2026-09-21); kein Widerspruch zu
R1-GL75-CALC-001.

**Hinweis Quellenangabe:** R1-GL24h-CALC-001 und R1-GL75-CALC-001 nennen
als Quelldatei "20260208_Berechnung_Rahmenecke_SB+SD.xlsx". Im
Quellenordner liegt die Datei unter "20260109_Berechnung_Rahmenecke_SB+SD.xlsx"
(so hier angegeben); ungeklärt, ob es zwei Fassungen gibt oder der Name
in den älteren Einträgen abweicht. Die dort genannten Zellbezüge (z. B.
C23-C26, C45/C50) entsprechen nicht mehr dem Stand des Blattes
(n_ef: C47 bis C52).
