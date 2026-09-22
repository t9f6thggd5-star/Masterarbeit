---
calculation_id: R1-GL24h-CALC-008
scope:
  connection: R1
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: Buchholz2025
  experimental_data:
  assumptions:
method: >
  Gesamtsteifigkeit des Zugpfads c_t,tot nach Buchholz2025 Gl. (2)
  (Reihenschaltung der Komponenten). c_v,f und c_br,par werden nach der
  Arbeitsannahme des Nutzers (R1-COMMON-OPQ-003) zu einer gemessenen Feder c_T
  je Bauteil zusammengefasst; Träger und Stütze liegen in Reihe und haben
  dieselbe Gruppe. c_T ist die 4×8-Gruppe, also das Doppelte der getesteten
  2×8-Gruppe (mittleres K_ser der Zugversuche I-T-S-SD-28-1 bis -3).
equations: >
  c_t,tot = 1 / (1/c_v,f + 1/c_br,par + 1/c_br,par + 1/c_v,f) mit
  c_v,f + c_br,par zusammengefasst zu c_T: c_t,tot = 1 / (1/c_T + 1/c_T) =
  c_T / 2; c_T = 2 · 279,52 = 559,04 kN/mm.
result:
  quantity: Zugpfad-Gesamtsteifigkeit c_t,tot (GL24h)
  value: 279.52
  unit: kN/mm
source_file: >
  R1/COMMON/calculations/20260109_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL24h SD", Zellen J7 (K_ser Mittel, 279,52 kN/mm), I15 (c_T =
  J7*2 = 559,04 kN/mm); Stand der Datei am 2026-09-21. Die Zelle I36
  (c_t,ges) enthält dort noch `=I42+2*#REF!` (defekt); vorgesehen ist
  `=1/(1/I15+1/I15)`. Der Verweis in J36 auf "FprEN Gl. 9.31" trifft nicht zu
  (Gl. 9.31 ist die Druckverformung quer zur Faser w_SLS,z).
certainty: CALCULATED
superseded_by:
---

Die Drehfedern C_rot,v,f gehen nicht in c_t,tot ein (Gl. 2 enthält sie nicht),
sondern über Buchholz2025 Gl. (5); siehe R1-GL24h-CALC-007.

**Vorläufig:** c_T hängt am Lastfenster der K_ser-Auswertung (F_est =
480 kN; mit 313,6 kN wäre das Mittel 238 kN/mm und damit c_t,tot etwa
238 kN/mm, R1-COMMON-OPQ-004) und an der Messbasis der Wegaufnehmer, die
festlegt, ob c_br,par im Messwert steckt (R1-COMMON-OPQ-003).

**Druckseite offen:** Für c_c,tot (Gl. 1) fehlen c_v,f der Druckgruppe und
c_c,0; Versuche liegen nicht vor. Ohne c_c,tot liegt C_rot,t+c zwischen
42.277 kNm/rad (c_c,tot = c_t,tot) und 84.555 kNm/rad (Druckseite starr) mit
z = 550 mm (Abstand der resultierenden Zug- und Druckkraft, R1-GL24h-OPQ-003).
