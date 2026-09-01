---
open_question_id: R2-COMMON-OPQ-008
scope:
  connection: R2
  material: COMMON
status: OPEN
question: >
  Welche Rolle spielen vier Excel-Inhalte, die in chat-3 nicht besprochen
  wurden, im tatsächlichen R2-Versuchs-/Rechenkonzept: (1) der
  vollständige Stabdübel-Johansen-Nachweis ("Tragfähigkeit Stabdübel",
  Spalten A-D je Blatt), (2) der Block "Tragfähigkeit Stütze auf Zug"
  (FprEN Fig. 11.38, Zellen F/G43-52 bzw. G43-52), (3) der Abschnitt
  "innerer Hebelarm Rahmeneck"/"maximales Moment"/"Zylinderkraft" (Zellen
  F/G113-133 bzw. G74-96), und (4) die beiden Vorspannungs-Arbeitsblätter
  "VSP GL24h "/"VSP GL75 " (enthalten `#DIV/0!`/`#REF!`-Fehler,
  referenzieren ASSY-Schraubengruppen und eine Annahme
  "L_eff=450 mm, F/8 je Schraube")?
context: >
  Der Nutzer hat entschieden (2026-09-01), reale Versuchsdaten aus diesen
  Blöcken direkt als Versuchsergebnisse (RES) zu übernehmen (siehe
  R2-GL24h-II-PO-S-SD-34-RES-001 u. a.), die Blöcke selbst aber vorerst
  nur als offene Frage zu dokumentieren, statt sie als vollständige
  eigene Berechnungen (CALC) auszuarbeiten, solange ihr Zweck im
  R2-Gesamtkonzept ungeklärt ist. Auffällig: der Stabdübel-Nachweis
  taucht in einem Excel auf, das eigentlich die eingeklebte-
  Gewindestangen-Verbindung (R2) behandelt — möglich wäre, dass er eine
  Hilfskonstruktion/Prüfstands-Lagerung (z. B. Anschluss der Probe an ein
  Widerlager) statt der eigentlichen R2-Rahmenecke selbst beschreibt; dies
  ist aber nicht bestätigt. Die Bezeichnungen der Versuchsreihen
  unterscheiden sich zudem zwischen den Blättern ("SD" auf Blatt
  "...GL24h SD", aber "WD" in der zugehörigen Push-Out-Versuchsreihen-ID
  auf Blatt "...GL24h HD") — auch diese Kürzel sind nicht dokumentiert.
  Der Block "Stütze auf Zug" könnte eine Blockscher-/Sprödbruchprüfung
  der Gewindestangengruppe nach FprEN Fig. 11.38 sein (Eingaben `a=88mm`,
  `b=80mm`, `A_ef=7040mm²` passen zu diesem Modelltyp), ist aber ebenfalls
  nicht im Chat erläutert. Die "VSP"-Blätter sind strukturell ähnlich zur
  R3-Annahme "F/8 je Schraube" (siehe R3-GL24h-ASS-002), aber in R2 nicht
  einmal ansatzweise im Chat erwähnt.
related_sources:
options_considered: >
  (a) Nur dokumentieren und auf Klärung durch den Nutzer warten (gewählt);
  (b) eigene Interpretation als CALC-Einträge ausformulieren (verworfen,
  da Zweck ungeklärt — Gefahr einer erfundenen Interpretation, siehe
  CLAUDE.md Abschnitt 19).
date_opened: "2026-09-01"
date_resolved:
resolution:
---

Eigener Fund (Claude) beim Cross-Check der R2-Excel-Datei
(`R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
Gewindestangen.xlsx`, Sheets "Rahmenecke GL24h SD/HD", "Rahmenecke GL75
SD", Stand 2026-09-01) gegen chat-3 — keiner dieser vier Blöcke wird in
SUMMARY.md, STATE.md, DECISIONS.md, KNOWLEDGE.md, TASKS.md oder
OPEN_QUESTIONS.md von chat-3 erwähnt. Rein rechnerisch sind alle vier
Blöcke in sich nachvollziehbar (Formeln/Normverweise vorhanden), nur ihr
Platz im Gesamtkonzept der R2-Verbindung ist offen.
