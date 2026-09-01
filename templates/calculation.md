---
calculation_id:           # <CONNECTION>-<MATERIAL>-CALC-<NUMMER>
scope:
  connection:              # R1 | R2 | R3
  material:                # GL24h | GL75
type: CALCULATION
inputs:
  normative_sources:       # ID(s) aus bibliography/sources.yaml
  literature:              # ID(s) aus bibliography/sources.yaml
  experimental_data:       # ID(s) aus research/.../experimental_results/
  assumptions:             # ID(s) aus research/.../assumptions/
method:
equations:
result:
  quantity:
  value:
  unit:                    # gemäß schema.yaml -> unit_convention
  original_value:          # nur falls ein verwendeter Eingangswert in einer anderen Einheit vorlag
  original_unit:
source_file:                # Pfad zur zugrundeliegenden Berechnungsdatei (z. B. Excel) im externen
                            # Quellenordner, falls vorhanden — keine sources.yaml-ID, da die Datei
                            # selbst laufend weiterbearbeitet wird und kein unveränderliches
                            # Original ist (siehe CLAUDE.md Abschnitt 9/13). Version/Datum mit
                            # angeben (z. B. Dateiname mit Datum), damit klar bleibt, welcher Stand
                            # dieser Eintrag wiedergibt.
certainty: CALCULATED    # siehe schema.yaml -> certainty
superseded_by:             # ID der neueren Berechnung, falls diese hier durch eine überarbeitete
                            # Version (z. B. der Exceltabelle) überholt ist (siehe Abschnitt 13)
---

Herleitung / Nachvollziehbarkeit der Berechnung. Nicht als normative
Aussage formulieren — es ist eine eigene Berechnung (siehe CLAUDE.md
Abschnitt 9).
