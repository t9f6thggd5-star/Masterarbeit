---
calculation_id: R3-GL24h-CALC-015
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: Buchholz2025
  experimental_data: R3-GL24h-III-PO-S-SC-44-C-RES-004, R3-GL24h-III-PO-S-SC-11-C-RES-004, R3-GL24h-III-PO-S-SC-44-B-RES-001
  assumptions: R3-GL24h-ASS-003, R3-GL24h-ASS-004
method: >
  Empfindlichkeit der Zugkette gegenüber dem Prüfkörper III-PO-S-SC-44-C-2
  (R3-GL24h-OPQ-023): Die Kette R3-GL24h-CALC-007 (α, c32,Column) →
  R3-GL24h-CALC-010 (c16,Beam) → c32,Beam → R3-GL24h-CALC-013 (c_t,sleeve)
  → R3-GL24h-CALC-014 (c_t,tot) wird ohne 44-C-2 neu gerechnet. C-2 wird
  dabei konsequent in beiden Lastfenstern ausgeschlossen (Normfenster
  0,1–0,4 · F_est für K_C,norm und Fenster 10–20 % F_est für K_C,10–20).
  Alle übrigen Eingänge unverändert (c_1,Column = 8,571 kN/mm; K_B,10–20 aus
  44-B-1 = 67,02 kN/mm; c_t = 30,994; c_H,Lasche = 298,438;
  c_v = 156,174 kN/mm).
  Zusätzlich Ausreißerprüfung nach Dixon mit n = 3 Prüfkörpern (die
  Ursache der geringen Steifigkeit betrifft beide Seiten von C-2 gleich,
  daher Prüfkörper und nicht Seiten als Stichprobe).
equations: >
  K_C,norm je Scherfuge (Überblick B40:C42 / 2): C-1 112,93/136,59;
  C-2 78,29/80,94; C-3 99,45/121,66 kN/mm.
  Mit C-2: K_C,norm = 104,97 (n = 6, VK 22 %), K_C,10–20 = 89,29;
  ohne C-2: K_C,norm = 117,65 (n = 4, VK 13 %), K_C,10–20 = (106,8 + 105,0)/2
  = 105,9 kN/mm.
  α = ln(K_C,norm/(4·c_1))/ln 4: 0,807 bzw. 0,890;
  c32,Column = 4·c_1·8^α: 183,68 bzw. 217,95 kN/mm (+19 %);
  c16,Beam = 67,02 · K_C,norm/K_C,10–20: 78,79 bzw. 74,46 kN/mm (−5 %);
  c32,Beam = c16,Beam · 2^α: 137,87 bzw. 137,93 kN/mm (±0);
  1/c_t,sleeve = 1/30,994 + 1/c32,Column + 1/c32,Beam + 2/298,438:
  19,36 bzw. 19,68 kN/mm (+1,7 %);
  c_t,tot = 1/(1/(2·c_t,sleeve) + 1/156,174): 31,02 bzw. 31,44 kN/mm (+1,4 %).
  Dixon Q (n = 3): Normfenster, Mittel je Prüfkörper 124,76/79,61/110,55 →
  Q = (110,55 − 79,61)/(124,76 − 79,61) = 0,685; Fenster 10–20 %
  106,8/56,0/105,0 → Q = 0,965. Kritische Werte n = 3: 0,941 (90 %),
  0,970 (95 %) (Standardtabelle Dixon-Test, Quelle nicht im Quellenbestand
  registriert).
result:
  quantity: Gesamtsteifigkeit der Zugseite c_t,tot ohne Prüfkörper III-PO-S-SC-44-C-2 (Empfindlichkeit zu R3-GL24h-CALC-014)
  value: 31.44
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  Gerechnet im Chat 2026-09-30 (Python) aus den Werten im Blatt "Überblick"
  von common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx und
  den Fensterwerten aus R3-GL24h-CALC-010; nicht im Excel umgesetzt.
certainty: CALCULATED
superseded_by:
---

Empfindlichkeitsrechnung, ersetzt keinen Hauptwert. Hauptwerte bleiben
R3-GL24h-CALC-007/010/013/014 mit allen drei Prüfkörpern (Nutzerentscheidung
2026-09-30, R3-GL24h-OPQ-023).

Ergebnis: C-2 verschiebt die mittlere Gruppensteifigkeit der Stützenseite
deutlich (K_C,norm −11 %, c32,Column −16 % gegenüber der Variante ohne C-2),
die Zugkette aber kaum (c_t,tot −1,4 %). Gründe: Bei c32,Beam heben sich
kleineres c16,Beam und größeres α auf; c32,Column hat nur ≈ 9–11 % Anteil an
1/c_t,sleeve, die Gewindestange 62–64 %.

Beitrag zur Parameterstudie laut Aufgabenstellung (Streuung der
Komponenten-Eingangswerte); zusammen mit der Spanne c32,Beam 130–147 kN/mm
(R3-GL24h-DEC-015) weiterführen. n = 3 Prüfkörper je Serie; statistisch ist
C-2 nicht als Ausreißer nachweisbar (CLAUDE.md Abschnitt 15).

**Hinweis (2026-09-30):** Gerechnet mit c_v = 156,17 kN/mm (R3-GL24h-CALC-012,
inzwischen ersetzt). Mit c_v = 131,13 kN/mm (R3-GL24h-CALC-017): c_t,tot ohne 44-C-2
≈ 30,28 statt 29,89 kN/mm (+1,3 %); die Aussage (Einfluss von C-2 gering) bleibt.
