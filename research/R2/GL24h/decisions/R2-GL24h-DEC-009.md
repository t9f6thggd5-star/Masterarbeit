---
decision_id: R2-GL24h-DEC-009
scope:
  connection: R2
  material: GL24h
type: DECISION
question: >
  Sind die in der Excel-Datei "20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx" (Sheet "Rahmenecke GL24h SD", Zeilen 124-178,
  dort selbst mit "Steifigkeiten Zugseite (in Bearbeitung)" beschriftet)
  enthaltenen Handrechnungswerte — u. a. `c_t,1` (40.950 N/mm),
  `K_SLS,w`/`c_ax,f,par` (177.646,15 N/mm), `c_t,ep` (1e99) und `c_c,90`
  unverstärkt (100.866,36 N/mm, FprEN Gl. 9.31) — als gültige
  Eingangsgrößen bzw. als Vergleichsbasis (z. B. Soll-Ist-Abgleich gegen
  Versuchsergebnisse) zu verwenden?
decision: >
  Nein. Die Zeilen 124-178 sind eine händische, vom Nutzer selbst als
  "in Bearbeitung" gekennzeichnete Berechnung und haben vorerst keine
  Gültigkeit. Sie werden weder als Eingangsgröße für die
  Steifigkeitskette noch als Vergleichsbasis herangezogen — insbesondere
  nicht für einen Soll-Ist-Vergleich mit Versuchswerten. Maßgebend und zu
  verwenden sind stattdessen: (a) aus Versuchsergebnissen abgeleitete
  Steifigkeiten (z. B. R2-GL24h-II-T-S-BR-22-RES-003) und (b) die
  Bejtka-basierte Herleitung für die (ASSY-verstärkte) Querdrucksteifigkeit
  (R2-COMMON-CALC-001).
reason: >
  Nutzerangabe im Chat, 2026-09-22, wörtlich: "die zeieln 124 bis 178 sind
  eine händisch berechnung. vorerst habe sie keine gültigkeit und sollen
  auch nciht zu vergleichen herangezogen werden. die steifigkeiten welche
  aus den verscuhsergebnisse abgeleitet wurden bzw bejtka sind die
  maßgebenden und zu verwendenden."
alternatives_considered: >
  Keine — direkte Anweisung des Nutzers, keine Abwägung durch Claude.
date: "2026-09-22"
---

## Anlass

Ausgelöst durch eine Rückfrage des Nutzers zu R2-GL24h-HYP-001 ("ich habe
doch nirgends eine vollständige Rechnung nach FprEN — wie kommst du auf
diese Werte?"). Bei der Überprüfung fiel zusätzlich auf, dass die in
R2-GL24h-CALC-002/CALC-001 zitierte Datei ("...20260208...") unter diesem
Namen nicht mehr existiert — nur eine "20260109"-Version liegt vor, mit
um ca. 8 Zeilen verschobenen, inhaltlich aber identischen Werten. Diese
Zellverschiebung ist unabhängig von der eigentlichen Entscheidung hier
(Gültigkeit der Zeilen 124-178) und wird in den betroffenen
CALC-Einträgen separat korrigiert.

## Betroffene Einträge

- **R2-GL24h-CALC-001** (`c_c,90` unverstärkt, 100,866 kN/mm) — Quellzelle
  liegt innerhalb des jetzt ungültigen Bereichs (Zeile 149 der aktuellen
  Datei). Wird dort entsprechend vermerkt.
- **R2-GL24h-CALC-002** (`c_Zugpfade,ges`, 57,384 kN/mm, rein rechnerisch)
  — sämtliche Eingangswerte liegen im ungültigen Bereich. War bereits
  durch R2-GL24h-CALC-014 superseded; Vermerk wird trotzdem ergänzt.
- **R2-GL24h-CALC-014** — die dort dokumentierte Beobachtung "Faktor
  ≈6,48 zwischen Versuchswert und FprEN-Vorhersage" vergleicht gegen den
  jetzt ungültigen Wert (133,115 kN/mm, aus denselben Zeilen). Diese
  Beobachtung darf nicht mehr als fachliche Diskrepanz gewertet werden.
  Der dortige Versuchswert-basierte Kettenanteil selbst (862,531 kN/mm,
  RES-003) bleibt unberührt gültig.
- **R2-GL24h-HYP-001** — die gesamte Kandidatenliste möglicher Ursachen
  für den Faktor ≈6,48 setzte voraus, dass dieser Faktor eine reale,
  erklärungsbedürftige Diskrepanz ist. Diese Prämisse entfällt hiermit;
  der Eintrag wird entsprechend als vorerst gegenstandslos markiert
  (siehe dortiges Update), nicht gelöscht (CLAUDE.md Abschnitt 13).

## Nicht betroffen

**R2-GL24h-CALC-021** (aktueller `c_T`, 53,300 kN/mm) verwendet bereits
die Bejtka-basierte, ASSY-verstärkte Querdrucksteifigkeit
(R2-COMMON-CALC-001, 111,339 kN/mm), nicht den unverstärkten
Handrechnungswert aus den Zeilen 124-178. Damit bleiben R2-GL24h-CALC-021,
R2-GL24h-INT-001/-002, R2-GL24h-CALC-022 und der aktuelle
`S_j,ini`-Wert von dieser Entscheidung unberührt.

## Offen / Symmetrie-Hinweis

Diese Entscheidung bezieht sich ausschließlich auf Sheet "Rahmenecke
GL24h SD" der genannten Datei. Ob ein analoger Handrechnungs-Block auch
in "Rahmenecke GL24h HD" oder "Rahmenecke GL75 SD" derselben Datei
existiert und ebenfalls betroffen ist, wurde nicht geprüft und wird hier
nicht unterstellt (CLAUDE.md Abschnitt 3/4 — keine Übertragung ohne
Beleg) — bei Bedarf gesondert zu prüfen.
