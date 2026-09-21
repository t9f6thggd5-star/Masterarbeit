---
decision_id: R1-GL24h-DEC-010
scope:
  connection: R1
  material: GL24h
type: DECISION
question: >
  Welche Steifigkeit K_ser je Stabdübel (Ø12, zweischnittig, Stahl-Holz,
  GL24h) wird für die Drehfeder C_rot,v,f der Dübelgruppen nach
  Buchholz2025 Gl. (4) angesetzt: der Normwert oder der aus den
  Gruppenversuchen abgeleitete effektive Wert c_T / 32?
decision: >
  Es wird der Normwert verwendet: K_ser,Dübel = 17,96 kN/mm nach FprEN
  1995-1-1:2024, Tab. 11.12 (ρ_m^1,5 · d / 23 mit ρ_m = 420 kg/m³, d = 12 mm
  ergibt 4,49 kN/mm je Scherfläche; doppelt für Stahl-Holz nach
  11.3.8.2 (5), mal m = 2 Scherfugen). Damit ist C_rot,v,f = K_ser,Dübel ·
  I_p = 17,96 kN/mm · 1.175.200 mm² = 21.111 kNm/rad je 4×8-Gruppe
  (a_1 = 80 mm, a_2 = 50 mm, Ursprung im Gruppenschwerpunkt).
reason: >
  Buchholz2025 Gl. (4) nennt K_ser nach FprEN Tab. 11.12 je
  Verbindungsmittel. Der aus den Gruppenversuchen abgeleitete Wert
  c_T / 32 = 17,47 kN/mm ist kein Einzeldübelwert (enthält Gruppenwirkung,
  gegebenenfalls Holz- und Blechverformung zwischen den Messpunkten und
  Lochspiel im Lastfenster; siehe R1-GL24h-OPQ-013) und weicht nur um 2,8 %
  vom Normwert ab. Für GL24h Ø12 liegt kein Einzeldübelversuch vor.
alternatives_considered: >
  (a) c_T / 32 = 17,47 kN/mm (Versuch, kein Reihendeckel; C_rot,v,f =
  20.531 kNm/rad); (b) c_T / 12 = 23,29 kN/mm (Versuch mit
  Reihendeckel min{n_0; 6} nach Gl. 11.26; C_rot,v,f = 27.374 kNm/rad,
  +33 %). Beide nicht gewählt; (a) dient als Gegenprobe.
date: "2026-09-21"
---

Entscheidung des Nutzers am 2026-09-21 ("dann machen wir K_ser nach Norm"),
nachdem R1-GL24h-OPQ-013 die Herleitung von c_T / 32 und die Reihenregel
aus Gl. (11.26) geklärt hatte. Die Translationsfeder c_T = 559,04 kN/mm
bleibt die gemessene Gruppensteifigkeit und ist von dieser Entscheidung
nicht betroffen. Offen bleiben die Kombination der vier Drehfedern
(Gl. 5 wörtlich oder physikalisch mit Träger/Stütze in Reihe) und die
Umsetzung im Blatt "Rahmenecke GL24h SD"
(I18 ist noch der Platzhalter 1E+99). Die Druckgruppe ist laut Nutzer
(2026-09-21) geometrisch identisch mit der Zuggruppe (4×8, a_1 = 80 mm,
a_2 = 50 mm), sodass alle vier Gruppen dasselbe C_rot,v,f haben. Wovon der
Normwert selbst abhängt (ρ_mean, Versuchsbelege), steht in R1-GL24h-OPQ-014.
