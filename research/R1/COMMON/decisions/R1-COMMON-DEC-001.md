---
decision_id: R1-COMMON-DEC-001
scope:
  connection: R1
  material: COMMON
type: DECISION
question: >
  Soll das aus "Dokument1.pdf" übernommene Federmodell für den
  R1-Anschlusstyp (Schlitzblech + Stabdübel) bereits in Phase 2
  aufgebaut/kalibriert werden?
decision: >
  Nein. Das Federmodell (Komponenten c_v,f, c_v,f,rot, c_c,0, c_br,par)
  wird in Phase 2 nur zur Identifikation der wahrscheinlich dominanten
  Verformungsmechanismen herangezogen, nicht als vollständiges,
  kalibriertes Berechnungsmodell aufgebaut. Der vollständige Aufbau und
  die Kalibrierung erfolgen erst in Phase 3, nachdem reale Eingangsgrößen
  aus den Komponentenversuchen vorliegen.
reason: >
  Konsistent mit der Phasenstruktur der Aufgabenstellung (siehe
  COMMON-COMMON-DEC-003); ein bereits kalibriertes Modell vor Auswertung
  der Komponentenversuche würde die vorgesehene Methodik umkehren.
alternatives_considered: >
  Vollständiges Federnetz (c_v,f, c_v,f,rot, c_c,0, c_br,par) bereits jetzt
  entwickeln/kalibrieren — verworfen.
date: "UNKNOWN (chat-2, seq 041-050; kein genaues Datum überliefert)"
---

Übernommen aus chat-2, DECISIONS.md D09 sowie
artifacts/FEDERMODELL_REFERENZ.md. Gilt materialunabhängig für R1
(Nutzerentscheidung vom 2026-09-01), da die Modelltopologie den
R1-Anschlusstyp als solchen beschreibt, unabhängig davon ob GL24h oder
GL75 verwendet wird.

**Inhalt der Referenzabbildung** ("Dokument1.pdf" — "Frame corner joint
type I with slotted-in steel plate and dowel-type fasteners" mit
zugehörigem Federmodell):
- `c_v,f` — translatorische Feder, Abscheren der stiftförmigen
  Verbindungsmittel
- `c_v,f,rot` — Rotationseffekt der Dübelgruppe
- `c_c,0` — Holzdruck parallel zur Faser
- `c_br,par` — Sprödbruch-Komponente bei Querlast parallel zur Faser

**Verifikationsvorbehalt:** "Dokument1.pdf" selbst liegt aktuell nicht im
externen Quellenordner vor — siehe R1-COMMON-OPQ-001.
