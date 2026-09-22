---
calculation_id: R2-GL24h-CALC-001
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions:
method: >
  FprEN-Querdruckverformungsmodell unter der 160×240 mm-Ankerplatte:
  `c_c,90 = 2·E_90,mean / (h_ef·(1/A + 1/A_ef))`, mit
  Lastausbreitung unter 45° über die effektive Höhe `h_ef=min(0,4h;140)`.
equations: FprEN 1995-1-1:2024, Gl. 9.31; Lastausbreitung nach Tab. 8.2/Gl. 8.11.
result:
  quantity: Querdrucksteifigkeit unter der gemeinsamen Ankerplatte, GL24h
  value: 100.866
  unit: kN/mm
  original_value: 100866.359
  original_unit: N/mm
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx (Update 2026-09-22: einzige unter diesem
  Dateistamm noch vorhandene Version; der ursprünglich zitierte
  Dateiname "...20260208..." existiert nicht mehr, Werte identisch,
  Zeilen um ca. 8 verschoben), Sheet "Rahmenecke GL24h SD", Zelle C149
  (ursprünglich C141 zitiert; per openpyxl mit data_only=True erneut
  ausgelesen und verifiziert am 2026-09-22)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-3 (KNOWLEDGE.md Abschnitt 5, FORMULAS.md Abschnitt 8)
und unabhängig gegen die reale Excel-Datei verifiziert.

**Eingangswerte** (Zelle → Wert): `E_90,mean=300 N/mm²`
(GL24h, Holzkennwerte-Blatt), `h_ef=140 mm` (C134, Gl. 8.11),
Lastausbreitungswinkel `α=45°` (C135, Tab. 8.2), `Δl=140 mm` (C136),
`b_90,c=160 mm` (C137), `l_ef=380 mm` (C138), `A_Stahlplatte=38.400 mm²`
(C139), `A_ef=60.800 mm²` (C140).

Eingang in die Stangen-Steifigkeitskette: unter der Annahme
gleichmäßiger Lastaufteilung auf vier Stangen (R2-COMMON-ASS-002) ergibt
sich der äquivalente Wert je Stange als `c_c,90 / 4 ≈ 25,2 kN/mm`, siehe
R2-GL24h-CALC-002.

**Update (2026-09-22, R2-GL24h-DEC-009):** Die Quellzelle dieses Werts
liegt innerhalb des Excel-Bereichs "Steifigkeiten Zugseite (in
Bearbeitung)" (Zeilen 124-178, Sheet "Rahmenecke GL24h SD"), den der
Nutzer als händische, vorerst ungültige Berechnung gekennzeichnet hat —
weder als Eingangsgröße noch als Vergleichsbasis zu verwenden (siehe
R2-GL24h-DEC-009). Dieser Eintrag (unverstärktes `c_c,90=100,866 kN/mm`)
gilt damit vorerst nicht als belastbarer Wert. Für die tatsächlich
verwendete, ASSY-verstärkte Querdrucksteifigkeit gilt stattdessen die
Bejtka-basierte Herleitung R2-COMMON-CALC-001 (111,339 kN/mm) — bereits
seit R2-GL24h-CALC-021 die maßgebende Größe in der `c_T`-Kette,
unberührt von diesem Update.
