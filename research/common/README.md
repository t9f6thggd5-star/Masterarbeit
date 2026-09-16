# research/common/

Forschungsstand, der nicht auf eine einzelne Verbindung oder ein einzelnes
Material beschränkt ist.

- `methods/` — übergreifende Methodik (z. B. Auswertungsverfahren, die für
  alle Versuchsreihen gelten).
- `assumptions/` — Annahmen, die für alle Verbindungen/Materialien gelten.
- `decisions/` — methodische Entscheidungen mit übergreifender Wirkung.
- `open_questions/` — offene, noch ungeklärte Forschungsfragen.
- `experimental_results/` — Versuchsergebnisse, die keiner einzelnen
  Rahmenecke zugeordnet sind, sondern verbindungsübergreifend als
  Baseline gelten (`scope.connection: COMMON`), z. B. die
  Push-Out-Grundserien 1×1 (Stabdübel/Holzdübel), die für R1/R2/R3
  gemeinsam als Referenz dienen. Wie bei allen `research/`-Einträgen
  bleibt `scope.material` (GL24h/GL75) weiterhin getrennt (CLAUDE.md
  Abschnitt 4) — nur die Verbindung ist hier COMMON, nicht das Material.
