---
decision_id: R3-COMMON-DEC-005
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Wie wird die Zugseite von R3 im Federmodell aufgebaut und welche
  Komponenten des Katalogs Buchholz2025 werden wie angesetzt?
decision: >
  Zugseite nach Buchholz2025, Gl. (11) und (12), Federmodell Typ III
  (Bild 5), Variante ohne Druckkontakt:
  1/c_t,sleeve = 1/c_t + 2/c_c,ep + 1/c_ax,v,f,α,Col + 1/c_ax,v,f,α,Beam
  + 1/c_br,par + 1/c_br,perp + 2/c_c,0;
  c_t,tot = 1/(1/(2·c_t,sleeve) + 1/c_v).
  Zuordnung: c_t = Gewindestange (R3-COMMON-DEC-006);
  c_c,ep (Nr. 15, Platte auf Hirnholz) = ∞;
  c_br,par (Nr. 13) und c_br,perp (Nr. 14) = ∞;
  c_c,0 (Nr. 3) = c_H,Lasche = E_0,mean·A_netto/L_eff mit L_eff = 450 mm
  (Deutung (a): Stauchung der Lasche parallel zur Faser);
  c_ax,v,f,α (Nr. 11) seitenspezifisch aus den Push-Out-Versuchen
  (Stütze R3-GL24h-CALC-007, Riegel R3-GL24h-DEC-015);
  zwei Laschen (vorne/hinten) parallel; Schubfeld c_v (Nr. 5) in Reihe
  (R3-COMMON-DEC-007). Rotationsfedern C_v,f,rot und Vorspannung vorerst
  nicht angesetzt.
reason: >
  Nutzerentscheidungen im Chat 2026-09-28. c_c,ep: die Platte deckt die volle
  Nettofläche A_netto der Lasche ab (gleiche Fläche wie im Pressungsnachweis,
  Excel "VSP GL24h ohne Druckkontakt" C6), eine eigene Feder würde denselben
  Holzbereich doppelt zählen; das Einsetzen der Platte wird als Schlupf offen
  gehalten (R3-COMMON-OPQ-002). c_br: im Katalog nur Tragfähigkeitsregel
  (FprEN 11.5/11.6), keine Steifigkeit; als Versagensmodus weiter
  nachzuweisen. c_c,0 = c_H: in der Variante ohne Druckkontakt berühren sich
  die Laschenhälften nicht, physikalisch bleibt nur die Laschenstauchung
  (Deutung von Buchholz Bild 5 offen, R3-COMMON-OPQ-004). L_eff = 450 mm
  (weichere Annahme; mögliche Doppelzählung der 280 mm im Gruppenbereich
  offen, R3-COMMON-OPQ-003). C_v,f,rot weggelassen: parallel geschaltet,
  Weglassen liegt auf der sicheren Seite. Vorspannung wird behandelt, wenn
  Zug- und Druckkette stehen.
alternatives_considered: >
  Bisherige Excel-Formel 1/c_t,sleeve = 1/c_t + 2/c_ASSY,S + 2/c_H mit dem
  normativen Einheitswert c_ASSY,S = 199,15 kN/mm (FprEN Gl. 11.29,
  R3-GL24h-CALC-003) — ersetzt durch seitenspezifische Versuchswerte; der
  Normwert bleibt im Excel als Vergleich stehen (Nutzerentscheidung).
  c_H mit 170 mm (nur freie Länge) — nur als Empfindlichkeit (+9 % auf
  c_t,sleeve).
date: "2026-09-28"
superseded_by:
---

Gilt für GL24h und GL75. Ergebnis GL24h: R3-GL24h-CALC-013 (c_t,sleeve)
und R3-GL24h-CALC-014 (c_t,tot). GL75: c_ax,v,f,α fehlt noch
(R3-GL75-OPQ-002).

Im Excel (Sheet "Rahmenecke GL24h SD", Block "Steifigkeit Zugseite mit
Versuchsergebnissen", I96 ff.) sind die Bezeichnungen noch anzupassen:
I101 "c_c,ep Stahlplatte" und I104 "c_c,0 Kontakt Platte/Hirnholz"
beschreiben zusammen die Katalogkomponente c,ep; c_c,0 nach Buchholz ist
c_H,Lasche (ab G120).
