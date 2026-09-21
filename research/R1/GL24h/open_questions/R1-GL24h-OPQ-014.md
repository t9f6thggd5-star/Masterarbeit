---
open_question_id: R1-GL24h-OPQ-014
scope:
  connection: R1
  material: GL24h
status: OPEN
question: >
  Wird K_ser,Dübel für GL24h Ø12 (Stahl-Holz, zweischnittig) nach FprEN
  1995-1-1 Tab. 11.12 nur rechnerisch aus der mittleren Rohdichte ρ_mean
  (420 kg/m³) und dem Durchmesser bestimmt, oder gibt es Versuche an
  Einzeldübeln, die den Normwert 17,96 kN/mm für dieses Material und diesen
  Durchmesser belegen oder korrigieren?
context: >
  Anlass (Nutzer, 2026-09-21): Nach R1-GL24h-DEC-010 geht K_ser,Dübel =
  17,96 kN/mm nach Norm in die Drehfeder C_rot,v,f ein (21.111 kNm/rad je
  4×8-Gruppe). Der Nutzer will festhalten, worauf dieser Normwert beruht.
  Was die Norm sagt: FprEN 1995-1-1:2024, Tab. 11.12 Zeile (1) gibt für
  Stabdübel K_SLS,v,i = ρ_mean^1,5 · d / 23 [N/mm] je Scherfläche und
  Verbindungsmittel an, mit ρ_mean als Mittelwert der Rohdichte in kg/m³ und
  d in mm; bei unterschiedlichen Rohdichten der beiden Bauteile gilt das
  geometrische Mittel (Gl. 11.27), bei Stahl-Holz wird der Wert verdoppelt
  (11.3.8.2 (5)). Die Norm nennt keine Versuchsgrundlage. Ein Lochspiel ist
  laut Fußnote a nur bei Bolzen gesondert zu addieren, für Stabdübel steht
  dazu nichts in der Tabelle (im Projekt getrennt geführt, R1-GL24h-DEC-007).
  Eingangswert Rohdichte: Das Blatt "Rahmenecke GL24h SD" (Zelle C5) und
  "Holzkennwerte" (D21) führen ρ_mean = 420 kg/m³ für GL24h (charakteristisch
  385 kg/m³, D11), aus den Tabellenwerten, nicht aus gemessenen Rohdichten der
  Prüfkörper der Zugversuche I-T-S-SD-28; gemessene Prüfkörperrohdichten
  wurden in den gesichteten Dateien nicht gefunden. K_ser ist proportional zu
  ρ^1,5: ρ = 385 kg/m³ ergibt 15,77 kN/mm (minus 12 %, C_rot,v,f 18.527
  kNm/rad); plus/minus 10 % Rohdichte ergeben plus 15 % bzw. minus 15 %.
  Was die Literatur dazu sagt (Gauss2024, Diss.): (1) Abschn. 2.3.7 (nach
  Jockwer und Jorissen): Der Ursprung der Formel im Eurocode 5 (dieselbe wie
  in FprEN Tab. 11.12) ist unklar, sie beruht auf vereinfachten Annahmen; die
  Rohdichte hat geringen Einfluss auf die Anschlusssteifigkeit, der
  Durchmesser mehr als in der Norm berücksichtigt. (2) Abschn. 3.4.5.7:
  Datenbank von Einzeldübel-Anschlussversuchen (eigene Versuche, Sandhaas
  2012, Brühl 2020, Bejtka 2005) mit sehr großer Streuung (bis Faktor 5 je
  Durchmesser); die Normwerte liegen tendenziell im unteren Drittel der
  Versuchswerte; ein Durchmesserexponent 1,9 (K_ser,EC5,mod = 2 · ρ_m^1,5 ·
  d^1,9 / 230) passt besser. (3) Kap. 3.3: Bettungsversuche an GL24h Ø12, 16
  und 20 mm (0° und 90°) mit k_ser je Bettungsfläche in N/mm/mm²; im Mittel
  sinkt k_ser für Ø16 um 6 % und für Ø20 um 18 % gegenüber Ø12; die
  Umrechnung auf die Steifigkeit eines Stabdübels ist nicht durchgeführt.
  (4) Gauß zitiert außerdem, dass Brühl (2020) die nach EC5 berechneten
  K_ser von Stabdübeln deutlich größer als die gemessenen fand; das steht im
  Widerspruch zu (2) und ist ungeklärt.
  Was im Projekt an Versuchen vorliegt: (a) die Gruppenversuche
  I-T-S-SD-28 (2×8, GL24h): 279,52 kN/mm, effektiv 17,47 kN/mm je Dübel,
  97 % des Normwerts, aber Gruppenwert (R1-GL24h-OPQ-013); (b) die
  Einzeldübelversuche HO-SD8 (Ø8, ρ_m = 800 kg/m³, Hartholz): 21,1 kN/mm,
  etwa 0,67 · Normwert, für GL24h Ø12 nicht übertragbar; (c) der IGF-Bericht
  20625 N enthält nach Claudes Durchsicht Einzeldübelversuche mit d = 12,
  16 und 20 mm, darunter GL24h; er ist nicht in bibliography/sources.yaml
  geführt und nicht ausgewertet.
related_sources: FprEN-1995-1-1-2024, Gauss2024, Buchholz2025
options_considered: >
  (a) Normwert 17,96 kN/mm mit ρ_mean = 420 kg/m³ beibehalten (Stand nach
  R1-GL24h-DEC-010); (b) mit der gemessenen Rohdichte der Prüfkörper
  rechnen, falls diese dokumentiert ist; (c) Einzeldübelversuche aus der
  Literatur (Gauss2024 Kap. 3.4.5.7, IGF-Bericht 20625 N) für GL24h Ø12
  auswerten und K_ser,Dübel daraus ableiten, den Normwert dann als Gegenprobe
  führen; (d) Sensitivität ausweisen (Rohdichte 385 bis 420 kg/m³, Streuung
  der Versuchswerte, Durchmesserexponent). Zu klären durch den Nutzer.
date_opened: "2026-09-21"
date_resolved:
resolution:
---

Aufgenommen auf Wunsch des Nutzers (2026-09-21). Bis zur Klärung gilt
R1-GL24h-DEC-010 (Normwert 17,96 kN/mm); daraus abgeleitete Werte
(C_rot,v,f) sind als abhängig von dieser Annahme zu kennzeichnen.
