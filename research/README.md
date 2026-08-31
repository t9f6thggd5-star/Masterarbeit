# research/

Der aktuelle Arbeitsstand: alles, was aus den Quellen und eigenen
Versuchen/Berechnungen **abgeleitet** wird, aber noch nicht in die
verlinkte Wissensbasis (`wiki/`) übernommen bzw. dort weiterverdichtet
wurde. Inhalte hier sind Forschungsergebnisse, keine Quellen (siehe
CLAUDE.md Abschnitt 6).

- `common/` — methodische Grundlagen, Annahmen, Entscheidungen und offene
  Fragen, die für alle Verbindungen gelten.
- `thesis/` — Arbeitsstand der nicht-verbindungsspezifischen Kapitel
  (Abstract, Einleitung, Grundlagen, Stand der Technik, Methodik,
  Diskussion, Grenzen der Arbeit, Schluss, Ausblick, general), siehe
  `research/thesis/README.md`.
- `R1/`, `R2/`, `R3/` — jeweils identisch unterteilt in `GL24h/` und
  `GL75/`, darunter:
  - `experiment_processing/` — Verarbeitung von Rohmessdaten (`PROCESSED_DATA`)
  - `experimental_results/` — abgeleitete Versuchsergebnisse (`EXPERIMENTAL_RESULT`)
  - `calculations/` — eigene Berechnungen (`CALCULATION`)
  - `assumptions/` — verbindungsspezifische Annahmen (`ASSUMPTION`)
  - `hypotheses/` — Arbeitshypothesen (`HYPOTHESIS`)
  - `interpretations/` — Interpretationen von Ergebnissen (`INTERPRETATION`)
  - `conclusions/` — Schlussfolgerungen (`CONCLUSION`)
  - `decisions/` — methodische Entscheidungen (`DECISION`)
  - `current_state.md` — kurze, laufend aktualisierte Zusammenfassung des
    Bearbeitungsstands für diese Verbindung/dieses Material

Provisorische Annahmen/Hypothesen dürfen hier stehen, dürfen aber laut
CLAUDE.md Abschnitt 13 niemals als gesicherte Fakten dargestellt werden.
