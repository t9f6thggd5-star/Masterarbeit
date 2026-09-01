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
| `open_question.md` | `research/common/open_questions/` — auch für R1/R2/R3-spezifische Fragen; der Scope steht im Frontmatter (`scope.connection`), nicht im Ordner (es gibt keinen separaten `open_questions/`-Unterordner je Verbindung) |
| `claim.md` | `wiki/.../` — für einzelne, quellenbezogene Aussagen |
| `current_state.md` | `research/R1/GL24h/current_state.md` (genau eine Datei je Verbindung/Material, kein ID-Schema — siehe Datei selbst) |

Siehe CLAUDE.md für die inhaltlichen Regeln und `schema.yaml` für alle
erlaubten Werte.

## Index und Lint

`scripts/build_index.py` und `scripts/lint.py` lesen alle Einträge unter
`research/` und `wiki/` anhand ihres YAML-Frontmatters und erzeugen daraus
automatisch `_index/catalog.yaml`, `_index/INDEX.md` und
`_index/lint_report.md`. Beide Dateien in `_index/` sind reine
Ausgabedateien — nie von Hand bearbeiten, sondern nach jeder Änderung neu
erzeugen:

```
python3 scripts/build_index.py
python3 scripts/lint.py
```

`lint.py` prüft u. a. die R1/R2/R3-Symmetrie (CLAUDE.md Abschnitt 3),
doppelte oder scope-widersprüchliche IDs, Pflichtfelder je Eintragstyp,
kontrolliertes Vokabular gegen `schema.yaml` (CLAUDE.md Regel 12) und ob
ein unreviewter `CLAUDE_DRAFT`-Eintrag anderswo zitiert wird (CLAUDE.md
Abschnitt 14). Siehe `_index/README.md` für Details.
