---
decision_id: COMMON-COMMON-DEC-003
scope:
  connection: COMMON
  material: COMMON
type: DECISION
question: >
  In welche Phasen gliedert sich die Masterarbeit laut offizieller
  Aufgabenstellung, und was ist in der aktuellen Phase 2 zu leisten?
decision: >
  Fünf Phasen laut Original: Phase 1 = Vorstudie (Problemstellung/
  Forschungsfragen, Literaturrecherche zur Komponentenmethode,
  Einarbeitung in die drei Rahmeneckanschlüsse und die bereits
  vorliegenden Komponenten-Versuchsdaten). Phase 2 = rechnerische
  Vorbemessung der drei Rahmeneckanschlüsse (maßgebende Tragfähigkeiten/
  Steifigkeiten, Identifikation der Grundkomponenten) und darauf
  aufbauende Versuchsplanung (erwartete Last-/Verformungsbereiche).
  Phase 3 = Auswertung der bereits durchgeführten Komponentenversuche
  (Kennwerte + statistische Streuung) und Entwicklung von Federmodellen
  für die drei Anschlüsse auf Basis dieser realen Kennwerte. Phase 4 =
  Anwendung der Federmodelle zur rechnerischen Ermittlung der
  Momenten-Rotationskurven, Bewertung des Einflusses der
  Grundkomponenten und der Eingangsstreuung, Abgleich mit vorliegenden
  Rahmenecken-Versuchsergebnissen. Phase 5 = Schlussdarstellung
  (schriftlicher/bildlicher Bericht, Zwischen- und Schlusspräsentation).
  Die Bearbeitung befindet sich aktuell in Phase 2; ein vollständiges,
  kalibriertes Federmodell ist planmäßig erst ab Phase 3 vorgesehen.
reason: >
  Explizite Struktur der offiziellen Masterarbeits-Aufgabenstellung.
alternatives_considered: >
  Das vollständige Federmodell (z. B. das für R1 in Dokument1.pdf
  skizzierte Netz aus c_v,f, c_v,f,rot, c_c,0, c_br,par) bereits in Phase 2
  aufbauen und kalibrieren — verworfen, siehe R1-COMMON-DEC-001.
date: "2026-07-15 (Ausgabedatum der Aufgabenstellung, siehe MA-Aufgabenstellung-Maucher-2026)"
---

Ursprünglich aus chat-2, KNOWLEDGE.md ("Master thesis structure") und
DECISIONS.md D08 ("Interpretation of thesis phases") übernommen; am
2026-09-01 vollständig gegen das inzwischen im externen Quellenordner
abgelegte Original geprüft und entsprechend präzisiert (siehe
`MA-Aufgabenstellung-Maucher-2026`). Diese Phasenstruktur ist
projektweit gültig (nicht auf R1 beschränkt) und wird deshalb — anders
als die R1-spezifischen Entscheidungen aus demselben Chat — unter
COMMON/COMMON geführt, analog zu COMMON-COMMON-DEC-001/002.

**Eckdaten der Aufgabenstellung** (gegen das Original verifiziert,
Quelle `MA-Aufgabenstellung-Maucher-2026`):
- Titel: „Untersuchung der Komponentenmethode im Holzbau am Beispiel
  momententragfähiger Rahmeneckanschlüsse"
- Bearbeiter: Lukas Maucher, Matrikel-Nr. 3380882
- Ausgabe: 15.07.2026; Abgabe: 14.01.2027
- Betreuer: Prof. Dr. Markus Knobloch, Lea Buchholz
- Studiengang: Master Bauingenieurwesen, Universität Stuttgart, Institut
  für Konstruktion und Entwurf
- Drei Anschlussvarianten: Schlitzblech + Stabdübel (R1); eingeklebte
  Gewindestangen (R2); seitlich angeschraubte Holzlaschen (R3)
- Eingebettet in das Forschungsprojekt "HIP_2685085" (im Dokument nicht
  weiter spezifiziert), das ein Versuchsprogramm zu allen drei
  Rahmeneckanschlüssen und deren Grundkomponenten bereitstellt

**Verifikationshinweis:** Diese Angaben stammen jetzt aus einer eigenen
Sichtung von `MA_Aufgabenstellung_Maucher.pdf` (per PDF-Lesetool, Stand
2026-09-01) und decken sich mit der ursprünglich aus chat-2 übernommenen
Wiedergabe — keine inhaltlichen Abweichungen festgestellt, lediglich
Ergänzungen (Bearbeiter, Matrikel-Nr., Forschungsprojekt-Referenz,
vollständige Phase-1/5-Beschreibung). Löst COMMON-COMMON-OPQ-002
(siehe dort, status: RESOLVED).
