# Templates

Diese Vorlagen sind die Grundlage für alle strukturierten Einträge im
Repository. Kopiere die passende Datei in den richtigen Zielordner unter
`research/` oder `wiki/` (bzw. bei `experiment_metadata.md` in den
externen Quellenordner, siehe CLAUDE.md Abschnitt 1), benenne sie nach dem
ID-Schema aus `schema.yaml` (`<CONNECTION>-<MATERIAL>-<CATEGORY>-<NUMBER>`)
und fülle das YAML-Frontmatter aus. Nicht benötigte Felder leer lassen
statt zu löschen, damit das Schema über alle Einträge hinweg konsistent
bleibt.

| Datei | Zielordner (Beispiel) |
|---|---|
| `experiment_metadata.md` | externer Quellenordner: `R1/GL24h/experiments/full_connection/<ID>/metadata.md` |
| `raw_measurement.md` | `research/R1/GL24h/experiment_processing/` |
| `processed_data.md` | `research/R1/GL24h/experiment_processing/` |
| `experimental_result.md` | `research/R1/GL24h/experimental_results/` |
| `calculation.md` | `research/R1/GL24h/calculations/` |
| `assumption.md` | `research/R1/GL24h/assumptions/` (oder `research/common/assumptions/`) |
| `hypothesis.md` | `research/R1/GL24h/hypotheses/` |
| `interpretation.md` | `research/R1/GL24h/interpretations/` |
| `conclusion.md` | `research/R1/GL24h/conclusions/` |
| `decision.md` | `research/R1/GL24h/decisions/` (oder `research/common/decisions/`) |
| `claim.md` | `wiki/.../` — für einzelne, quellenbezogene Aussagen |

Siehe CLAUDE.md für die inhaltlichen Regeln und `schema.yaml` für alle
erlaubten Werte.
