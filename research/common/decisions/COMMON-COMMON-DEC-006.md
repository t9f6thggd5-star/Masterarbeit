---
decision_id: COMMON-COMMON-DEC-006
scope:
  connection: COMMON
  material: COMMON
type: DECISION
question: >
  Wird für die Eingangsgrößen der Federn der Komponentenmethode (und
  damit für die daraus kombinierte Anfangsrotationssteifigkeit `S_j,ini`)
  die Anfangssteifigkeit (`K_ser`, DIN-EN-26891-Erstbelastung) oder die
  Wiederbelastungssteifigkeit (`K_e`) angesetzt?
decision: >
  Vorläufig wird durchgängig die Anfangssteifigkeit `K_ser` angesetzt,
  nicht `K_e`. Gilt projektweit (R1/R2/R3), für alle Federn der
  Komponentenmethode und damit für die daraus kombinierte
  Anfangsrotationssteifigkeit `S_j,ini` — nicht nur für die bereits in
  R2-COMMON-DEC-003 geregelte Zellzuordnung der Stangengruppen-`K_ser`-
  Werte (jene Entscheidung legt nur fest, *welcher* `K_ser`-Wert/welche
  Poolung angesetzt wird, nicht *dass* `K_ser` statt `K_e` verwendet
  wird — diese Entscheidung ergänzt sie insofern, ersetzt sie nicht).
reason: >
  Nutzerentscheidung (Chat, 2026-09-22), ohne weitere fachliche
  Begründung angegeben. Ausdrücklich als vorläufig ("vorerst")
  bezeichnet.
alternatives_considered: >
  Wiederbelastungssteifigkeit `K_e` — in den Auswertungstabellen der
  BR-Zugversuche durchgängig mit erfasst (`K_e` liegt dort in allen vier
  Versuchsserien II-T-B-BR-11/22 und II-T-S-BR-11/22 etwas über `K_ser`,
  Blatt "Überblick" der Datei `2026-06_05_Auswertung_Steifigkeiten_
  Bonded-inRods.xlsx`) — nicht gewählt.
date: "2026-09-22"
---

Kontext: Im Gespräch wurde festgestellt, dass in der BR-Zugversuchs-
Auswertung neben `K_ser` (Erstbelastung) auch `K_e` (Wiederbelastung)
ausgewertet vorliegt und `K_e` durchgängig etwas über `K_ser` liegt
(Kommentar in der Datei: vermutlich Imperfektionen bei Erstbelastung).
Für die Verwendung als Eingangsgröße der Federn — und damit für die
Anfangsrotationssteifigkeit `S_j,ini` im Sinne von DIN EN 1993-1-8:2025-04,
Anhang B.4.1(4), Gl. (B.6) (Quelle `DIN-EN-1993-1-8-2025`; in der Fassung
2010-12 Abschnitt 6.3.1)
bzw. deren Analogon im Holzbau — ist definitionsgemäß die
Anfangs-/Erstbelastungssteifigkeit maßgebend; diese Entscheidung macht
das jetzt auch für dieses Projekt explizit und einheitlich, statt es
implizit aus der bisherigen Zellauswahl (R2-COMMON-DEC-003) abzuleiten.

Betrifft alle bisher aufgestellten Steifigkeitsketten mit `K_ser`-Werten
aus den BR-Versuchen, u. a. `R2-GL24h-II-T-S-BR-22-RES-003`,
`R2-GL24h-II-T-S-BR-11-RES-003`, `R2-GL75-II-T-B-BR-11-RES-003`,
`R2-GL75-II-T-B-BR-22-RES-003` — dort wurde ohnehin bereits `K_ser`
verwendet, diese Entscheidung bestätigt das jetzt ausdrücklich als
projektweite Festlegung statt als Einzelfallwahl.

Als "vorerst" gekennzeichnet: kann revidiert werden, z. B. falls sich
im weiteren Verlauf (Phase 4, Vergleich mit Rahmenecken-Gesamtversuchen)
zeigt, dass `K_e` für bestimmte Fragestellungen (etwa wiederholte
Belastung) der passendere Wert wäre.
