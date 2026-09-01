---
hypothesis_id: R3-GL24h-HYP-001
scope:
  connection: R3
  material: GL24h
type: HYPOTHESIS
statement: >
  Die Gesamtverformung der Verbindung lässt sich als Δ = Δ_Zug + Δ_Druck
  darstellen, mit φ ≈ Δ/z und Rotationssteifigkeit C_rot = M/φ. Δ_Zug
  ergibt sich additiv aus Gewindestangen-Dehnung, axialer
  Holzlaschen-Verformung und ASSY-Schlupf/axialer Verformung; Δ_Druck aus
  Holz-Lager-/Kontaktverformung. Holz-Schubverformung wird nur bei
  nachgewiesener Relevanz ergänzt (siehe R3-GL24h-OPQ-012). Erforderliche
  Modellvarianten: ohne Vorspannung, mit zugseitiger Vorspannung, ohne
  direkten Seitenlaschen-Kontakt, mit garantiertem Kontakt (Sensitivität).
motivated_by: >
  R3-GL24h-DEC-009 (Übergang von Tragfähigkeits-Vorbemessung zu
  Verformungsabschätzung); Ziel ist laut REQUIREMENTS.md die Ausgabe von
  relativer Öffnung, Rotation und Rotationssteifigkeit.
tested_by:
certainty: HYPOTHESIZED
authored_by: CLAUDE_DRAFT
reviewed: false
---

Übernommen aus chat-1, artifacts/current-deformation-model-outline.md
("Status: Proposal; not yet numerically completed") sowie KNOWLEDGE.md
("Deformation framework"). Als `CLAUDE_DRAFT`/unreviewed geführt, da nicht
eindeutig überliefert ist, wieweit dieser Modellrahmen im Chat vom
Forschenden selbst stammt oder von einer KI vorgeschlagen wurde — siehe
CLAUDE.md Abschnitt 14.

**Zentrale Nebenbedingung (aus dem Ursprungsmaterial wörtlich
übernommen):** "do not count the same physical compliance twice" — direkt
relevant für R3-GL24h-OPQ-006 (Kombination von ASSY-Abstützung,
Holz-Axialverformung und ASSY-Schlupf ohne Doppelzählung), welche noch
ungeklärt ist.

**Bereits verworfene Modellierungsansätze** (aus chat-1,
REQUIREMENTS.md → "Rejected/superseded", zur Vermeidung erneuter
Fehlversuche hier dokumentiert):
- Willkürliches Verkürzen von L_eff allein aufgrund vorhandenen direkten
  Druckkontakts (verworfen).
- Verteilte ASSY-Schrauben als einzelne Punktfeder plus vollständig
  unabhängige 800-mm-Holzfeder ohne Prüfung auf Doppelzählung (verworfen).
- Vollständiges c_t,sleeve direkt mit nur einer partiellen
  Gegen-Steifigkeit in einem VDI-artigen Lastanteilsausdruck vermischt
  (überholt/verworfen, siehe R3-GL24h-OPQ-010).

**Akzeptanzkriterium** (aus chat-1, REQUIREMENTS.md → "[Proposal]
Acceptance"): klarer Kraftfluss, nachvollziehbare Steifigkeiten und
Einheiten, keine Doppelzählung; Ausgabe: relative Öffnung, Rotation und
Rotationssteifigkeit.
