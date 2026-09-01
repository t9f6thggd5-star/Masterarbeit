---
hypothesis_id: R1-GL24h-HYP-001
scope:
  connection: R1
  material: GL24h
type: HYPOTHESIS
statement: >
  Die Rahmeneckenrotation φ des R1-Anschlusses (Schlitzblech + Stabdübel,
  Innenwinkel 108°) lässt sich aus den lokalen, zu den jeweiligen
  Stabachsen parallelen Dübelgruppen-Schlupfen über eine
  Starrkörper-/Kompatibilitätsbeziehung ableiten, die (1) lokale
  Koordinatensysteme beider Stäbe, (2) die Lage der
  Dübelgruppen-Schwerpunkte/Kontaktzonen und (3) die durch z=550mm
  getrennten Zug-/Druckresultierenden berücksichtigt — nicht durch
  skalare Addition der Schlupfwege (verworfen, R1-GL24h-DEC-008) und
  nicht durch die reine Vektor-Relativtranslation via Kosinussatz
  (unzureichend, R1-GL24h-DEC-009, R1-GL24h-CALC-006).
motivated_by: >
  R1-GL24h-DEC-009 (Vektor-Translation ist nicht automatisch Rotation);
  Ziel gemäß Aufgabenstellung (COMMON-COMMON-DEC-003) ist die Abschätzung
  erwarteter Last-/Verformungsbereiche für die Versuchsplanung
  (R1-GL24h-OPQ-001).
tested_by:
certainty: HYPOTHESIZED
authored_by: CLAUDE_DRAFT
reviewed: false
---

Übernommen aus chat-2, artifacts/VERFORMUNGSKONZEPT_GL24H.md ("Required
next derivation") sowie TASKS.md (N1, B2). Als `CLAUDE_DRAFT`/unreviewed
geführt, da nicht eindeutig überliefert ist, wieweit dieser
Lösungsansatz im Chat vom Forschenden selbst stammt oder von einer KI
vorgeschlagen wurde — siehe CLAUDE.md Abschnitt 14.

**Hinweis zur Abgrenzung:** Dies ist ein eigenständiges,
R1-spezifisches Verformungsmodell (Schlitzblech + Stabdübel,
108°-Rahmengeometrie) und nicht identisch mit R3-GL24h-HYP-001 (Δ=Δ_Zug+
Δ_Druck-Modell für den seitlich verschraubten Holzlaschen-Anschluss von
R3) — beide Anschlusstypen benötigen wegen unterschiedlicher Geometrie
und Lastabtragung eigene Kompatibilitätsherleitungen.

**Erforderliche Herleitungsschritte** (aus chat-2, wörtlich übernommen und
übersetzt):
1. Lokale Koordinatensysteme beider Stäbe definieren.
2. Lage der Dübelgruppen-Schwerpunkte/Resultierenden bestimmen.
3. Die durch z=550mm getrennten Zug-/Druckresultierenden lokalisieren
   (siehe R1-GL24h-OPQ-003).
4. Translatorische Schlupfe an den relevanten Punkten ansetzen.
5. Die Kompatibilitätsbeziehung herleiten, die daraus φ liefert.

Erst danach sollen die aktuellen Schätzungen für u_el,S und u_0
(R1-GL24h-CALC-005) in Rahmeneckenrotation und anschließend in
Aktuatorweg umgerechnet werden (siehe R1-GL24h-OPQ-002, R1-GL24h-OPQ-010).

**Bereits verworfene Modellierungsansätze** (siehe R1-GL24h-DEC-008/009):
- Skalares Addieren der Schlupfwege beider geneigter Anschlussbereiche
  (verworfen).
- Reine Vektor-Relativverschiebung via Kosinussatz bei 108° direkt als
  Rahmeneckenrotation interpretieren (unzureichend, R1-GL24h-CALC-006).

**Akzeptanzkriterien** (aus chat-2, REQUIREMENTS.md → "Acceptance
criteria for current GL24h deformation precheck"): dominante
Verformungsmechanismen identifiziert; normative/theoretische
Steifigkeiten transparent verwendet (R1-GL24h-CALC-001–005); Lochspiel
und elastische Verformung getrennt (R1-GL24h-DEC-007); 108°-Geometrie
korrekt berücksichtigt; plausibler Verformungsbereich für den Versuch
abgeleitet; Annahmen und Grenzen explizit gekennzeichnet.
