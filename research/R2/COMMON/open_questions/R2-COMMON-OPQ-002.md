---
open_question_id: R2-COMMON-OPQ-002
scope:
  connection: R2
  material: COMMON
status: RESOLVED
question: >
  Welches Modell soll als primärer Vorbemessungs-Vergleichswert für die
  querdruckverstärkte Widerstandsseite dienen — das FprEN-2024-Modell
  (`≈248,85 kN` für GL24h, siehe R2-GL24h-CALC-006 — veraltet, siehe
  Update unten) oder das ETA/Würth-Vergleichsmodell (`≈356,3 kN`, altes
  `k_c,90 = 1,75`)?
context: >
  Je nach gewähltem Modell kann sich der maßgebende Versagensmodus
  zwischen Gewindestangen-Zugversagen und Querdruckversagen verschieben.
  chat-3 schlug vor, FprEN als primären Wert und ETA/Würth als
  Vergleichs-/Sensitivitätswert zu verwenden, ohne dass dies vom Nutzer
  abschließend bestätigt wurde.
related_sources:
options_considered: >
  (a) FprEN als primären Wert, ETA/Würth nur als Sensitivität (Vorschlag
  aus chat-3); (b) ETA/Würth als primären Wert; (c) beide Modelle
  gleichrangig nebeneinander im Bericht führen.
date_opened: "2026-09-01"
date_resolved: "2026-09-30"
resolution: >
  Geschlossen (Nutzer, 2026-09-30): für die Tragfähigkeit nicht maßgebend, weil die Gewindestangen (Zugversuchsmittel 285,77 kN) vor
  Querdruck und Schrauben versagen (Excel C97 = MIN(L16;L87;H87)).
---

Übernommen aus chat-3, OPEN_QUESTIONS.md Punkt 2 und DECISIONS.md "Seq
197-200 — Primary predesign value" (dort ausdrücklich als `[Proposal]`,
nicht als abgeschlossene Entscheidung markiert: "Status: active proposal;
user had not explicitly closed the issue with a final acceptance
statement"). Die ETA/Würth-Vergleichsrechnung selbst ist im aktuell
vorliegenden R2-Excel nicht als eigenes Berechnungsblatt auffindbar
(nur der FprEN-Pfad ist im Workbook abgebildet, siehe
R2-GL24h-CALC-005/006) — die in chat-3 genannten ETA/Würth-Zahlenwerte
(`≈356,3 kN` u. a.) sind daher bisher nicht unabhängig gegen die Excel-
Datei verifizierbar.

**Fehlerkorrektur (2026-09-22, Nutzerhinweis):** Der hier zitierte
FprEN-Wert `≈248,85 kN` (CALC-006) ist inzwischen durch die
`k_mat`-Korrektur überholt: aktuell `≈384,124 kN` (R2-GL24h-CALC-011,
Druckseite) bzw. `≈356,273 kN` (R2-GL24h-CALC-017, Zugseite) — beide
bereits am 2026-09-01/17 korrigiert, also schon zum Zeitpunkt dieser
Fragestellung veraltet zitiert. Die eigentliche methodische Frage
(FprEN als primärer Wert vs. ETA/Würth als Vergleichswert) bleibt davon
unberührt offen.
