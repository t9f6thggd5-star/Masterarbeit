---
decision_id: R3-COMMON-DEC-009
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Wie wird die Druckseite von R3 im Federmodell abgebildet (Komponenten,
  Kontaktfläche, Lastausbreitung, Lage der Nulllinie)?
decision: >
  Variante ohne Druckkontakt der Laschen: Die gesamte Druckkraft wird über
  den Kontakt Riegel/Stütze übertragen; keine Querdruckverstärkung.
  Komponenten nach Buchholz2025 Gl. (6) in Reihe: c_c,90 (Riegel, Nr. 4) und
  c_c,0 (Stütze, Nr. 3). Keine fest definierte Kontaktfläche: dreieckförmige
  Pressung, Länge x der Druckzone aus dem Gleichgewicht Zug = Druck
  (gerissener Querschnitt, Zustand nach dem Öffnen der Fuge):
  c_t,tot·(d − x) = ½·k·b·x², z = d − x/3, S_j,ini = c_t,tot·(d − x)·(d − x/3),
  mit d = Abstand Zugkraft zum inneren Stützenrand, b = Kontaktbreite.
  Riegel: c_c,90 nach FprEN 1995-1-1:2024 Gl. (9.31) mit A = b·x,
  Lastausbreitung beidseitig unter 45° parallel zur Faser (Tab. 8.2),
  A_ef = b·(x + 2·h_ef), h_ef = min(0,4·h; 140 mm) nach Gl. (8.11).
  Stütze: c_c,0 = E_0,mean·b·x/l_0 ohne Lastausbreitung (Faser in
  Kraftrichtung), l_0 = x (analog R2-GL24h-CALC-019, Nutzerentscheidung
  2026-09-30; gestützt durch ScheibmairQuenneville2014), damit
  c_c,0 = E_0,mean·b.
  Bettung k = c_c,tot/(b·x) (mittlere Bettung), Iteration über x.
reason: >
  Nutzerentscheidungen (Chat, 2026-09-30): kein Druckkontakt der Laschen,
  keine Querdruckverstärkung, Vorgehen wie bei R2 (R2-GL24h-CALC-001/019/020,
  R2-COMMON-DEC-004); anders als bei R2 (Stahlplatte, R2-COMMON-DEC-002)
  liegt der Riegel ohne definierte Kontaktfläche auf der Stütze auf, die
  Druckzonenlänge hängt vom Steifigkeitsverhältnis ab (R3-COMMON-OPQ-001,
  Option b); in der Stütze keine Ausbreitung, weil die Druckkraft parallel
  zur Faser wirkt; im Riegel Ausbreitung beidseitig unter 45°.
  Buchholz2025 Tab. 1 (S. 1744) nennt für Nr. 3/4 als Steifigkeitsquelle nur
  EN 338:2016 / EN 14080:2013, also nur E-Moduln (DIN EN 14080:2013,
  Tab. 5, S. 27: GL 24h E_0,g,mean = 11 500, E_90,g,mean = 300 N/mm²), keine
  Geometrie der Feder. h_ef nach Gl. (8.11) ist ein Vorschlag von Claude
  (wie R2), vom Nutzer noch nicht ausdrücklich bestätigt.
alternatives_considered: >
  Feste Druckzone 400 mm mit Gl. (9.31) für A = 160 × 400 mm (verworfen,
  keine definierte Kontaktfläche); Riegel ohne Ausbreitung (untere Grenze,
  als Vergleich); h_ef = 280 mm nach Gl. (8.10) (Empfindlichkeit); volle
  Riegelhöhe als h_ef (sehr weich, nicht normgestützt).
date: "2026-09-30"
superseded_by:
---

Gilt für GL24h und GL75 (GL75 mit eigenen Kennwerten, noch nicht gerechnet).
Ergebnis GL24h: R3-GL24h-CALC-016.

**Gültigkeitsbereich:** Zustand nach dem Öffnen der Fuge an der Zugseite.
Die Vorspannung der zugseitigen Stangen drückt die Fuge außen unter der
Stangenlinie vor (Kraftfluss Stange → Laschenhälften → ASSY → Riegel/Stütze
→ Kontaktfuge, vom Nutzer bestätigt 2026-09-30); davor ändert sich die
Kontaktzone mit dem Moment, siehe R3-COMMON-OPQ-007.

**Literaturbezug (SOURCE_CLAIM):** ScheibmairQuenneville2014 modelliert die
Druckseite des "Quick Connect" (Anschlusstyp von R3) ebenso: Ebenbleiben der
Querschnitte, dreieckige Druckzone der Länge λ (Gl. 24–26, S. 04013022-5),
Stauchung bezogen auf λ, σ = E_timber·Δ_C/λ (Gl. 27–30), C = E_timber·Δ_T·λ·b/
(2(d − λ)) (Gl. 31), Nulllinie aus T = C, geschlossen λ = 2·k_system·g/
(E_timber·b + 2·k_system) (Gl. 36, S. 04013022-6). Das entspricht l_0 = x.
Unterschiede: dort ein einziges E_timber ohne Richtung und ohne h_ef; hier
Aufteilung in c_c,0 (Stütze, wie dort) und c_c,90 (Riegel, FprEN Gl. 9.31);
Fall Holz auf Holz dort nur mit "both beam and column parts … must be
accounted for" beschrieben (S. 04013022-6); Versuche dort mit LVL,
Übertragung auf GL24h nicht belegt.

**Einschränkungen:** Gl. (9.31) setzt gleichmäßige Pressung voraus, hier
ist sie dreieckig und zur Nulllinie hin null; die Ausbreitung zur
Nulllinie hin wirkt real schwächer, "beidseitig" überschätzt c_c,90 etwas
(untere Grenze: ohne Ausbreitung). Für den Hebelarm z der
Momententragfähigkeit M_R gilt bis zur Entscheidung des Nutzers weiter
R3-COMMON-DEC-004 (586,7 mm); mit z aus der Nulllinie wären es ≈ 634 mm.
