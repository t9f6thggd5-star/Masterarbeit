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

