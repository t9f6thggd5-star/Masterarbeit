---
open_question_id: R1-COMMON-OPQ-003
scope:
  connection: R1
  material: COMMON
status: OPEN
question: >
  Wo waren die Wegaufnehmer (LVDT) der Zugversuche "I-T-S-SD-28-1/2/3"
  (GL24h) und "I-T-B-SD-28-1/2/3" (GL75) befestigt (Bezugspunkte an
  Stahlblech und Holz, Abstand zur Dübelgruppe), und steckt damit der
  Holzanteil c_br,par (Sprödversagen, Querkraft parallel zur Faser) im
  gemessenen Schlupf, oder nur c_v,f (Dübelabscheren)?
context: >
  Aufgenommen im Zusammenhang mit der Ableitung der Zugpfad-Federsteifigkeit
  aus den Versuchsdaten (2026-09-21). Federmodell (vom Nutzer als Abbildung
  im Chat geliefert, nicht im Quellenordner abgelegt): Zugpfad je Bauteil
  (Träger, Stütze) mit c_v,f,rot, c_v,f und c_br,par in Reihe; Träger- und
  Stützenseite ebenfalls in Reihe, Faserrichtung bei beiden gleich;
  Stahlblech als starr angesetzt und nicht im Modell enthalten.
  Der gemessene Schlupf der Blätter (Spalten I "OBEN" und J "UNTEN",
  jeweils Mittel aus VO/HO bzw. VU/HU; Zuordnung V/H = vorn/hinten
  vermutet, nicht bestätigt) ist die Relativverschiebung zwischen den
  beiden Bezugspunkten des Wegaufnehmers. Liegt der Holz-Bezugspunkt nahe
  an der Dübelgruppe, erfasst der Versuch im Wesentlichen c_v,f; liegt er
  weiter entfernt, geht ein Teil der Holzverformung (c_br,par) in den
  Messwert ein. Die Bezugspunkte sind bisher nicht dokumentiert.
  Arbeitsannahme (Nutzer, 2026-09-21): c_br,par steckt im Versuchswert
  mit drin; c_v,f und c_br,par werden daher zusammengefasst als eine Feder
  je Dübelgruppe angesetzt und nicht getrennt ausgewiesen.
related_sources:
options_considered: >
  (a) Arbeitsannahme beibehalten: gemessene Steifigkeit als
  zusammengefasste Feder c_v,f + c_br,par, c_br,par im Modell nicht
  zusätzlich ansetzen (Vermeidung von Doppelzählung); (b) falls die
  Bezugspunkte nur die Dübelzone erfassen: c_v,f aus dem Versuch, c_br,par
  separat ermitteln (Quelle noch offen). Zu klären anhand von Skizze,
  Foto oder Versuchsbericht des Messaufbaus.
date_opened: "2026-09-21"
date_resolved:
resolution:
---

Aufgenommen auf Wunsch des Nutzers (2026-09-21). Solange die Bezugspunkte
nicht geklärt sind, gilt die Arbeitsannahme (a); daraus abgeleitete Werte
sind entsprechend als vorläufig zu kennzeichnen.
