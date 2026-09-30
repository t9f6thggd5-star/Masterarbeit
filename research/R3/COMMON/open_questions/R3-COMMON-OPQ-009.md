---
open_question_id: R3-COMMON-OPQ-009
scope:
  connection: R3
  material: COMMON
status: OPEN
question: >
  Werden die Rotationsfedern der ASSY-Schraubengruppen C_v,f,rot
  (Buchholz2025 Gl. (4)/(5), C_rot,v,f = I_p · K_ser, parallel zu C_rot,t+c
  addiert) für R3 angesetzt, und mit welchem K_ser?
context: >
  Im Federmodell von Buchholz2025 (Bild 5) für Typ III enthalten, im
  bisherigen R3-Modell nicht (R3-GL24h-CALC-019 "ohne C_v,f,rot"; Abgleich in
  R3-COMMON-DEC-014). Größenordnung (Claude, 2026-09-30, grob): 4×8-Gruppe
  mit Schraubenlagen laut Plan (Querabstände ±30,5/±60,5 mm, Reihen ±40 …
  ±280 mm) I_p ≈ 1,15·10⁶ mm² je Gruppe; mit K ≈ 8,6 kN/mm je Schraube
  (1×1-Push-Out Stütze, axial und lateral gemischt) ≈ 9 800 kNm/rad je Gruppe,
  also in der Größenordnung von S_j,ini selbst. Ob die Gruppendrehung
  überhaupt wirkt, hängt davon ab, ob die Lasche über die Stoßfuge ein Moment
  übertragen kann (mit Kontakt eher ja, ohne Kontakt nein) und wie steif die
  45°-Schrauben quer zur Laschenachse sind (dort rein lateral, deutlich
  weicher als in Lastrichtung). Gilt für GL24h und GL75.
related_sources: Buchholz2025
options_considered: >
  (a) weglassen (bisher, auf der sicheren Seite weich); (b) nach Buchholz mit
  I_p · K_ser je Gruppe, K_ser lateral nach FprEN Tab. 11.12; (c) als
  Stellschraube für den Versuchsvergleich.
date_opened: "2026-09-30"
date_resolved:
resolution:
---
