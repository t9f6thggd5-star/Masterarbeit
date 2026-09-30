---
decision_id: COMMON-COMMON-DEC-010
scope:
  connection: COMMON
  material: COMMON
type: DECISION
question: >
  Welcher Schubmodul wird für die Verstärkungsplatten aus Bau-Furniersperrholz
  Buche (BFU-BU nach DIN EN 636) im Schubfeld der Rahmenecken angesetzt?
decision: >
  G_v = 520 N/mm² (Schubmodul quer zur Plattenebene, Scheibenschub) nach
  DIN EN 12369-2:2011-09, Abschn. 6.3, Tab. 4, Zeile ρ_w,mean = 700 kg/m³
  (Buche, nächstgelegener unterer Tabellenwert). Der Tabellenwert ist ein
  5-%-Quantil (Anhang B, Gl. B.1) und wird bewusst ohne Umrechnung auf einen
  Mittelwert verwendet (sichere Seite). Gilt für alle Anschlüsse; je Anschluss
  gehen nur Plattendicke t_P und Plattenmaße ein: c_v,P = G_v · t_P · h_P / l_v.
reason: >
  Nutzerentscheidung (Chat, 2026-09-30), Herleitung vom Nutzer, Zahlen von Claude
  an der Norm geprüft (Tab. 4, S. 11: G_v = 520, f_v = 6,9, G_r = 82,
  f_r = 1,1 N/mm²). Schubwerte hängen nach 6.3 nur von der Rohdichte der
  Holzart ab, nicht von Dicke, Lagenanzahl oder F-/E-Klasse. Anwendungsbereich
  (Abschn. 1): mindestens 5 Lagen und 6 mm Gesamtdicke. R3 (5-lagig, 15 mm je
  Seite, GL24h und GL75) liegt im Anwendungsbereich; R2 (GL24h 4-lagig 12 mm,
  GL75 3-lagig 9 mm je Seite) liegt außerhalb, dort wird der Wert als Näherung
  verwendet (Nutzerentscheidung).
alternatives_considered: >
  G_v,mean ≈ 520/0,84 ≈ 620 N/mm² (Faktor 0,84 aus 6.2, dort nur für die
  E-Klassen angegeben, Übertragung auf G_v; verworfen zugunsten der sicheren
  Seite); bisher 500 N/mm² mit Verweis auf die KLH-ETA (Brettsperrholz, anderes
  Material; ersetzt).
date: "2026-09-30"
superseded_by:
---

Nicht geprüft, weil nicht im Quellenbestand: ρ_mean Buche ≈ 720 kg/m³ (LWF
Wissen 86 nach Grosser & Teetz 1998), DIN 1052-1:1988, DIN EN 12369-2:2025-11.
Offen: Leistungserklärung des Plattenherstellers (für R2 außerhalb des
Anwendungsbereichs maßgebend).
