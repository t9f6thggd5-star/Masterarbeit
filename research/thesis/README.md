# research/thesis/

Der aktuelle Arbeitsstand für die nicht-verbindungsspezifischen Kapitel
der Arbeit. Anders als `research/common/` (übergreifende Methodik/
Annahmen, die technisch für R1/R2/R3 gelten) geht es hier um die
eigentliche Kapitelarbeit der Masterarbeit selbst. Die zugrundeliegenden
Quellen liegen unabhängig vom Kapitel im externen Quellenordner (`common/`,
siehe CLAUDE.md Abschnitt 1) — es gibt dort keine eigene `thesis/`-Kategorie,
weil dieselbe Quelle oft in mehreren Kapiteln zitiert wird.

Kapitel, in der Reihenfolge, in der sie in der Arbeit vorkommen würden:

- `abstract/` — Kurzfassung/Abstract.
- `introduction/` — Motivation, Problemstellung, Forschungsfragen, Zielsetzung.
- `fundamentals/` — Grundlagen: Begriffe, Basistheorie, die zum Verständnis
  der Arbeit nötig sind (abzugrenzen von `state_of_the_art/`, das den
  aktuellen Forschungs-/Normungsstand behandelt, nicht die Grundlagen).
- `state_of_the_art/` — Aufarbeitung des Forschungsstands als eigenes Kapitel.
- `methodology/` — Begründung des Forschungsdesigns der gesamten Arbeit
  (warum drei Verbindungen, warum diese Materialien, warum diese
  Versuchsebenen kombiniert) — nicht zu verwechseln mit den technischen
  Methoden selbst in `research/common/methods/`.
- `discussion/` — Gesamtdiskussion über alle drei Verbindungen hinweg.
- `limitations/` — Grenzen der Arbeit.
- `conclusion/` — Schlussfolgerungen/Fazit der gesamten Arbeit; baut auf
  `wiki/cross_connection/overall_conclusions/` auf, ist aber die
  eigentliche Kapiteltextarbeit, nicht die technische Synthese selbst.
- `outlook/` — Ausblick, offene Fragen für künftige Forschung.
- `general/` — Sammelordner für Inhalte, die noch keinem der obigen
  Kapitel eindeutig zuzuordnen sind, oder für später hinzukommende Kapitel
  (z. B. ein eigenes Anhang-Kapitel).

Es gelten dieselben Regeln wie in `research/common/` und
`research/R1|R2|R3/` (siehe CLAUDE.md): Annahmen/Entwürfe bleiben
nachvollziehbar, Claude-Vorschläge werden als `CLAUDE_DRAFT` markiert
(Abschnitt 14), bis du sie bestätigst.
