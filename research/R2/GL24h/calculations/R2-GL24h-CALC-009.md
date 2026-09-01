---
calculation_id: R2-GL24h-CALC-009
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
  Johansen-Tragfähigkeit eines zweischnittigen Stabdübelanschlusses
  (d=12mm, S235, 3 Reihen × 4 Stabdübel = 12 Stück, a_1=70mm), auf
  demselben Excel-Blatt wie die eigentliche R2-Gewindestangen-Berechnung,
  aber mit unklarem Bezug zur eigentlichen R2-Rahmenecke (siehe
  R2-COMMON-OPQ-008 — möglich, aber nicht bestätigt: Prüfstands-/
  Widerlager-Anschluss statt der R2-Verbindung selbst). Zwei
  Fließmoment-Basen: normativ (FprEN Tab. 11.7(2)) und aus eigenem
  Stabdübel-Biegeversuch (Mittelwert).
equations: >
  FprEN 1995-1-1:2024, Gl. 11.14 (a-f) für die Einzeltragfähigkeit je
  Scherfuge/Stabdübel; Gl. 11.15 (β); Tab. 11.6 (28)-(30)
  (f_h,1,k/f_h,2,k/k_90/k_mat); Tab. 11.10 (6) (n_ef).
result:
  quantity: Gruppen-Tragfähigkeit F_D,k,ges (governierende Basis, normatives M_y,k)
  value: 78.720
  unit: kN
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen A34-A67 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01)
certainty: CALCULATED
superseded_by:
---

Eigenständig aus der R2-Excel-Datei erschlossen — dieser Block wird in
chat-3 an keiner Stelle erwähnt (siehe R2-COMMON-OPQ-008 für die offene
Frage nach seiner Rolle im R2-Gesamtkonzept). Die reine Rechenkette ist
jedoch vollständig nachvollziehbar und wird hier dokumentiert, um sie
nicht durch Weglassen zu verlieren.

**Normative Basis** (`M_y,k=69.070,88 Nmm`, C36, FprEN Tab. 11.7(2)):
Modi a-f ergeben C49-C54 (19,016 / 29,095 / 9,898 / 8,051 / 10,189 /
7,247 kN), governierend Modus f mit `F_D,k=7,247 kN` je Verbindungsmittel
(C55), `n_ef=2,850` (C45/C47, Tab. 11.10(6)), Gruppentragfähigkeit
`F_D,k,ges=61,965 kN` (C57).

**Basis aus Stabdübel-Biegeversuch** (`M_y,mean=156.989 Nmm`, C37):
Modi a-f ergeben C59-C64, governierend Modus d mit `F_D,k=9,207 kN`
(C62/C65), `F_D,k,ges=78,720 kN` (C67) — dieser Wert ist der hier als
Hauptergebnis dokumentierte, da er der "Höchstlast F_est" in Zeile 27
(`78,720 kN`) entspricht und damit offenbar als rechnerischer
Vergleichswert zur realen Versuchsreihe diente.

**Vergleich mit realer Versuchsreihe** `II-PO-S-SD-34` (n=3, Mittelwert
`68,715 kN`, siehe R2-GL24h-II-PO-S-SD-34-RES-001): niedriger als beide
rechnerischen Werte. Anmerkung in der Excel-Datei (Zelle D72):
"Querdruckversagen war maßgeblich" — d. h. die Versuchskörper versagten
laut Herstellerangabe durch Querdruckversagen des Holzes, nicht durch
klassisches Stabdübel-/Johansen-Versagen, was die Diskrepanz zur
rein rechnerischen Johansen-Tragfähigkeit erklären könnte.
