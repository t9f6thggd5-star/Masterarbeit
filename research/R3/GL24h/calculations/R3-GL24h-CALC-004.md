---
calculation_id: R3-GL24h-CALC-004
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: DIN-EN-1993-1-8-2025, DIN-EN-1993-1-8-NA-2026
  literature:
  experimental_data:
  assumptions: >
    Gewindestange M20 (A_s = 245 mm², Spannungsquerschnitt), Dehnlänge
    L_b = 1660 mm, Stahl E_s = 210000 N/mm².
method: >
  Axiale Dehnsteifigkeit der Gewindestange (Zug), berechnet als
  Steifigkeitskoeffizient k_t nach DIN EN 1993-1-8:2025-04, Anhang A.13.2,
  Gl. (A.40) (k_t = 1,6·A_s/L_b, nicht vorgespannte Schraubenreihe,
  Schrauben mit Zugbeanspruchung; L_b nach Tabelle 8.2; entspricht k_10
  in DIN EN 1993-1-8:2010-12, Tab. 6.11), multipliziert mit dem
  Stahl-E-Modul E_s, um vom Steifigkeitskoeffizienten auf die
  tatsächliche Federsteifigkeit zu kommen: c_t = E_s·k_t = E_s·1,6·A_s/L_b.
  Herleitung am 2026-09-22 vollständig nachvollzogen (siehe Update unten) —
  ursprünglich als nicht nachvollziehbar markiert.
equations: >
  c_t = E_s · 1,6 · A_s / L_b [N/mm]
  = 210000 · 1,6 · 245 / 1660
  = 49590,36 N/mm ≈ 49,59 kN/mm
result:
  quantity: Axiale Steifigkeit der Gewindestange
  value: 49.59
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl.
  Holzlaschen.xlsx, Sheet "Rahmenecke GL24h SD" Zelle H71 bzw. Sheet
  "Rahmenecke GL24h HD" Zelle I69 (beide 49,59036144578313 ≈ 49,59,
  Zellwert per openpyxl verifiziert); Stand August 2026 trotz Dateiname
  vom 08.02.2026. **Korrigiert 2026-09-22:** die tatsächliche Formelzelle
  ist "Rahmenecke GL24h SD" I83 bzw. "Rahmenecke GL24h HD" I73 (Label
  "c_t"), nicht H71/I69 wie ursprünglich notiert — Zeilenverschiebung
  vermutlich durch spätere Bearbeitung der Quelldatei nach der
  ursprünglichen Übernahme. Beide Zellen enthalten dieselbe Formel
  `=((1.6*A_s)/L_b*E_s)*10^-3` und ergeben denselben Wert 49,59036...
  kN/mm — der übernommene Zahlenwert war also stets korrekt, nur die
  dokumentierte Zellreferenz war veraltet.
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-1, KNOWLEDGE.md ("c_t=49.59 kN/mm").

**Nachvollziehbarkeit (ursprünglich, bis 2026-09-22):** die konkrete
Herleitung (Gewindestangen-Querschnitt, freie Länge, Stahl-E-Modul) war
in den übernommenen Chat-Dateien nicht enthalten — nur das Endergebnis
war überliefert. Als Endergebnis übernommen, nicht eigenständig
nachgerechnet.

**Update (2026-09-22):** Herleitung jetzt vollständig nachvollzogen durch
direkte Prüfung der Formelzellen in der Quelldatei (siehe Nutzerhinweis
auf DIN EN 1993-1-8 Tab. 6.11, k_10 = 1,6·A_s/L_b für Schrauben auf Zug).
Eingangswerte aus der Quelldatei: Gewindestange M20, A_s = 245 mm²
(Spannungsquerschnitt), L_b = 1660 mm (Dehnlänge), E_s = 210000 N/mm².
c_t = E_s·1,6·A_s/L_b = 210000·1,6·245/1660 = 49590,36 N/mm = 49,59 kN/mm
— exakte Übereinstimmung mit dem bisherigen Wert. Damit ist CALC-004 nun
vollständig nachvollziehbar (siehe `equations`-Feld oben) statt nur als
Endergebnis übernommen.

**Update (2026-09-25, Quellenangabe auf aktuelle Normfassung umgestellt):**
Der Normverweis bezog sich ursprünglich auf DIN EN 1993-1-8:2010-12,
Tab. 6.11 (`k_10`). Diese Fassung ist durch DIN EN 1993-1-8:2025-04
ersetzt (Quelle `DIN-EN-1993-1-8-2025`, Nationaler Anhang
`DIN-EN-1993-1-8-NA-2026`); die 2010er-Fassung war nie in
`bibliography/sources.yaml` registriert und liegt nicht mehr im
Quellenordner. In der Fassung 2025-04 steht dieselbe Formel in
Anhang A.13.2, Gl. (A.40), jetzt mit dem Symbol `k_t` (für eine nicht
vorgespannte Schraubenreihe, Kategorie D; für vorgespannte Schrauben
Gl. (A.41) `k_t = ∞`); die Dehnlänge `L_b` ist in Tabelle 8.2 definiert.
Der Nationale Anhang 2026-04 enthält zu A.13.2 keine abweichende
Festlegung. Formel und Eingangswerte sind unverändert, das Ergebnis
(49,59 kN/mm) bleibt gültig — deshalb reine Korrektur der Quellenangabe,
kein neuer Eintrag mit `superseded_by`. Der Nutzerhinweis oben ("Tab.
6.11, k_10") bleibt als historischer Wortlaut stehen.
