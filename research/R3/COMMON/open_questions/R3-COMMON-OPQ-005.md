---
open_question_id: R3-COMMON-OPQ-005
scope:
  connection: R3
  material: COMMON
status: RESOLVED
question: >
  Ist das einfache Schubfeldmodell c_v = G·b·h_v/l_v (Holz + Platten
  parallel) für R3 ausreichend, insbesondere weil die Verstärkungsplatten
  (l = 460 mm) kürzer sind als das Holzfeld (800 mm)?
context: >
  Rechenweg aus R2 übernommen (R3-COMMON-DEC-007). Die Parallelschaltung
  nimmt gleiche Verformung von Holz und Platte an; eine kürzere Platte
  überbrückt nur einen Teil des Feldes, das Ergebnis ist eher zu steif. Anteil
  der Platten klein (2 · 26 von 156 kN/mm GL24h). G_P = 500 N/mm² ist eine
  Annahme ("KLH ETA Scheibenbeanspruchung", Quelle nicht registriert). Für
  Holz gibt es keine Katalogformel (Nr. 5 nennt nur G nach EN 14080); im
  Stahlbau genauer k_1 = 0,38·A_vc/(β·z) mit Übertragungsparameter β.
  Gilt sinngemäß auch für R2.
related_sources: Buchholz2025
options_considered: >
  Vorerst einfaches Modell (Nutzerentscheidung 2026-09-28).
date_opened: "2026-09-28"
date_resolved: "2026-09-30"
resolution: >
  Für die Vorbemessung festgelegt (Nutzer, 2026-09-30, nach
  COMMON-COMMON-DEC-011): einfaches Modell wie bisher, c_v = G_H·b·h_v/l_v +
  2·G_P·t_P·h_v/l_P mit κ = 1, G_P = 520 N/mm², eine 15-mm-Platte je Seite
  (R3-GL24h-CALC-017: 131,13 kN/mm). Beim Vergleich mit den Globalversuchen
  als Stellschraube prüfen (Alternativen siehe unten).
---

**Alternativen (Claude, 2026-09-30, für den Versuchsvergleich):** Werte GL24h,
c_t,tot bisher 29,89 kN/mm.
1. Feld in Längsrichtung teilen: Abschnitt mit Platten (460 mm, Holz + Platten
   parallel) und ohne Platten (340 mm, nur Holz) in Reihe:
   c_v = 1/(1/208,0 + 1/244,7) = 112,4 kN/mm (−14 %), c_t,tot ≈ 28,80 kN/mm
   (−3,6 %). Kinematisch folgerichtiger als die bisherige Addition, gleicher
   Aufwand; setzt voraus, dass die 460 mm in Richtung der Feldlänge liegen.
2. Hebelarm z statt l_v im Nenner (R3-COMMON-OPQ-008, Stahlbau DIN EN
   1993-1-8:2025-04 A.4.2 Gl. (A.13) mit Übertragungsparameter β): mit
   z = 635,7 mm c_v = 165,0 kN/mm, c_t,tot ≈ 31,36 kN/mm (+4,9 %); mit
   Variante 1 kombiniert 141,5 kN/mm bzw. 30,40 kN/mm.
3. Verbund Platte/Holz: Sind die Platten geschraubt statt geklebt, wirkt der
   Schlupf der Verbindungsmittel in Reihe zur Platte, der Plattenanteil wird
   kleiner (Grenze: nur Holz, c_v = 104 kN/mm, c_t,tot ≈ 28,21 kN/mm, −5,6 %).
4. FE-Modell des Eckfelds (Scheibe, orthotropes Holz, Platten, Verbindung):
   genauestes Verfahren, erfasst ungleichmäßigen Schub und Biegung im Feld;
   hoher Aufwand, eher zur Kalibrierung nach den Versuchen.
Der Einfluss auf c_t,tot liegt damit etwa zwischen −6 % und +5 %.
