---
calculation_id: R1-GL75-CALC-005
scope:
  connection: R1
  material: GL75
type: CALCULATION
inputs:
  normative_sources:
  literature: Buchholz2025
  experimental_data:
  assumptions:
method: >
  Gesamtsteifigkeit des Zugpfads c_t,tot nach Buchholz2025 Gl. (2) wie in
  R1-GL24h-CALC-008: c_v,f und c_br,par zu einer gemessenen Feder c_T je
  Bauteil zusammengefasst (R1-COMMON-OPQ-003), Träger und Stütze in Reihe,
  c_T = 2 · mittleres K_ser der getesteten 2×8-Gruppe (Zugversuche
  I-T-B-SD-28-1 bis -3).
equations: >
  c_T = 2 · 727,74 = 1455,48 kN/mm; c_t,tot = 1 / (1/c_T + 1/c_T) = c_T / 2.
result:
  quantity: Zugpfad-Gesamtsteifigkeit c_t,tot (GL75)
  value: 727.74
  unit: kN/mm
source_file: >
  R1/COMMON/calculations/20260109_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL75 SD", Zellen J7 (727,74 kN/mm, vom Nutzer korrigiert; früher
  734,17, siehe R1-COMMON-OPQ-002) und I15 (c_T = J7*2 = 1455,48 kN/mm); Stand
  der Datei am 2026-09-21. Die Zelle I21 (c_t,ges) verweist dort noch auf
  leere Zellen (`=I29+2*I37`); vorgesehen ist `=1/(1/I15+1/I15)`.
certainty: CALCULATED
superseded_by:
---

**Vorläufig:** Die GL75-Gruppenversuche sind mit F_est = 800 kN ausgewertet
(Fenster 80 bis 320 kN); die gemessenen Höchstlasten liegen bei 581 bis
646 kN, die Auswertung mit F_est = 627,08 kN je 2×8-Gruppe
(R1-GL75-CALC-003) steht aus (R1-COMMON-OPQ-004). Ebenfalls offen ist die
Messbasis der Wegaufnehmer (R1-COMMON-OPQ-003). Die Drehfedern gehen nicht in
c_t,tot ein, siehe R1-GL75-CALC-004; die Druckseite (c_c,tot) fehlt, die obere
Grenze von C_rot,t+c ist z² · c_t,tot = 220.141 kNm/rad mit z = 550 mm (R1-GL24h-OPQ-003).

**Update (2026-09-25):** R1-COMMON-OPQ-004 ist geklärt: Das Lastfenster mit
F_est = 800 kN ist richtig, die Auswertung mit 627,08 kN entfällt, c_T und
c_t,tot bleiben unverändert. R1-COMMON-OPQ-003 ist geklärt: Der Messwert
entspricht c_v,f, die Holzverformung ist nicht enthalten (Begründung in
`method` überholt, siehe R1-GL24h-CALC-008). Offen bleibt R1-COMMON-OPQ-005
(c_br,par starr? Zugverformung des Holzes?).

**Update (2026-09-26):** Der Nutzer hat im Excel c_v,f und c_br,par
getrennt (Blatt neu gegliedert, Zellen jetzt: I15 c_br,par = 1E+99, I18 c_v,f = 1.455,48 kN/mm (=J7*2), I21 c_t = 1/(1/I15+1/I18), I24 c_t,tot = 1/(1/I21+1/I21) = 727,74 kN/mm). Die frühere
Zusammenfassung zu einer Feder c_T entfällt; c_T heißt im Blatt jetzt
c_t (Zugseite je Bauteil). Zahlenwert unverändert, weiter vorläufig
(c_br,par starr, R1-COMMON-OPQ-005). Weiterverwendet in
R1-GL75-CALC-006.
