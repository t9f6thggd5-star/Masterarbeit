---
open_question_id: R3-COMMON-OPQ-003
scope:
  connection: R3
  material: COMMON
status: OPEN
question: >
  Ist die Stauchung der Lasche im Bereich der Schraubengruppe (280 mm der
  L_eff = 450 mm) bereits im gemessenen K_ser der Push-Out-Versuche enthalten
  und wird damit doppelt gezählt?
context: >
  c_c,0 = c_H,Lasche = E_0·A_netto/L_eff mit L_eff = 170 mm (frei) + 280 mm
  (Lastabbau über 8 Reihen, ASS-002). Messen die Wegaufnehmer der Push-Out-
  Versuche die Relativverschiebung am Gruppenrand, steckt die Stauchung von
  Lasche und Mittelholz im Gruppenbereich schon in c_ax,v,f,α. Einfluss
  GL24h: c_H 298 (450 mm) bzw. 790 kN/mm (170 mm), c_t,sleeve 19,36 bzw.
  21,05 kN/mm (+9 %). Hängt an COMMON-COMMON-OPQ-003 (Messaufbau der
  Push-Out-Versuche).
related_sources: Buchholz2025
options_considered: >
  450 mm (weichere Annahme) vorerst beibehalten (Nutzerentscheidung
  2026-09-28). Im Excel c_H in freie Länge und Gruppenbereich aufteilen, um
  umschalten zu können.
date_opened: "2026-09-28"
date_resolved:
resolution:
---

Außerdem: Die Lastverteilung "jede Reihe F/8" (R3-GL24h-ASS-002) ist eine
Vereinfachung eines gekoppelten Problems (Verhältnis Laschen-/Schrauben-
steifigkeit, ähnlich Volkersen); real tragen die Endreihen mehr.

**Update (2026-09-30), Varianten der Laschenlänge (Claude, zur Besprechung):**
Geometrie laut Plan: 170 mm (Ankerplatte bis erste Reihe) + 7 × 80 + 70 mm
(letzte Reihe bis Stoßfuge). Mit Kontakt (R3-COMMON-DEC-011) wird die Lasche
auch auf der Druckseite gestaucht (70 mm + Gruppenbereich). Drei Ansätze
(GL24h, E_0·A_netto = 134 300 kN):
1. Verschiebung der letzten Reihe (bisher): Zug 450 mm (298 kN/mm), Druck
   350 mm (384 kN/mm).
2. Mittel der Reihenverschiebungen bei gleicher Reihenlast F/8 (passt
   energetisch zu R3-GL24h-ASS-002): Zug 345 mm (389 kN/mm), Druck 245 mm
   (548 kN/mm).
3. Nur freie Länge (falls die Push-Out-Wegmessung den Gruppenbereich schon
   enthält): Zug 170 mm (790 kN/mm), Druck 70 mm (1 919 kN/mm).
Überschlag S_j,ini nach dem Öffnen der Stoßfuge (mit Laschen auf der
Druckseite, Bettung konstant): 10 660 / 10 960 / 11 520 kNm/rad
(Spanne ≈ 8 %). Entscheidung mit dem Nutzer offen.


**Stand (2026-09-30, Nutzer):** Als offene Frage mitgenommen, noch keine
Entscheidung. Bis dahin rechnet die Excel weiter mit 450 mm (Zug); für die
Druckseite wird vorerst der gleiche Ansatz (Verschiebung der letzten Reihe,
350 mm) verwendet.

**Update (2026-09-30), Messaufbau Push-Out (Nutzer):** Bei den Push-Out-Versuchen
mit Schrauben sitzt der Wegaufnehmer mittig zwischen der 3. und 4.
Schraubenreihe (4×4-Serien). Er misst also die Relativverschiebung Lasche
gegen Mittelholz an einem Punkt innerhalb der Gruppe. Folgerung (Claude, zu
prüfen): K_ser enthält den Schlupf der Schrauben an dieser Stelle, aber nicht
die Stauchung von Lasche und Mittelholz über den Gruppenbereich. Ansatz 3
(nur freie Länge) scheidet damit aus; es bleibt die Wahl zwischen Ansatz 1
(450/350 mm) und Ansatz 2 (345/245 mm). Da die Messstelle nahe einem
Gruppenende liegt, wo der Schlupf bei nachgiebigen Bauteilen größer ist als
im Mittel (Volkersen-Effekt), ist das gemessene K_ser eher etwas kleiner als
eine auf den mittleren Schlupf bezogene Steifigkeit. Zusammen mit der
Annahme F/8 je Reihe passt Ansatz 2 folgerichtig; Ansatz 1 als weichere
Grenze. Offen: Lage des Wegaufnehmers bei den 1×1-Versuchen.

**Update (2026-09-30), 1×1-Versuche (Nutzer):** Der Wegaufnehmer saß 70 mm
unterhalb des Schraubenkopfs. Bei 80 mm Laschendicke und 45° Neigung kreuzt
die Schraube die Scherfuge etwa 80 mm vom Kopf entfernt (Claude); die
Messstelle liegt also nahe dem Durchgang der Schraube durch die Fuge und
misst den örtlichen Schlupf. 1×1 und 4×4 messen damit vergleichbar an der
Schraube; die Hochrechnung 16 → 32 (R3-GL24h-CALC-007) bleibt davon
unberührt. Laut Foto III-PO-S-SC-44-C1 (Deutung Claude, vom Nutzer nicht
bestätigt): Gehäuse mit einer Halterung am Mittelholz befestigt, Taster auf einem Winkel an der
Lasche; Halterung und Lochblech des Winkels etwa 10 cm höhenversetzt, dadurch geht die
unterschiedliche Dehnung beider Hölzer auf dieser Strecke mit ein (grob
5–7 % des Messwerts bei 0,4 · F_est, kleine Stellschraube).
