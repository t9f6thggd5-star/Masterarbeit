---
claim_id: R2-COMMON-CLAIM-002
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Experimentell aus Langzeitversuchen an vier Rahmenecken-Prüfkörpern
    (Glulam GL10 Radiata Pine, 315×90 mm, Gewindestangen Ø12 mm Grade
    8.8, jeweils zwei Geometrien × zwei Ausführungsarten) ermittelte
    elastische Rotationssteifigkeiten (Tab. 5, lineare Anpassung an die
    Momenten-Rotations-Kurve während der Belastungsrampe): "tensioned"
    (nur Zugstangen verklebt, Druckseite unverklebt, reine Kontaktpressung)
    1617–2276 kNm/rad; "fully epoxied" (alle Stangen über die gesamte
    Länge verklebt) 1656–1940 kNm/rad. Beide Ausführungsarten weisen laut
    Quelle ähnliche Rotationssteifigkeit auf ("both the tensioned and
    fully epoxied type joints have similar stiffness"). Die Joint-
    Rotation trug bei allen Prüfkörpern zu ca. 50 % der gesamten
    Kragarm-Durchbiegung bei.
  source: FragiacomoBatchelar2012b
  pages: "804, 808"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Realer Vergleichs-/Plausibilitätswert für eine spätere Gesamt-
Rotationssteifigkeit des R2-Federmodells — Geometrie/Material weichen
allerdings deutlich von R2 (GL24h/GL75, 4× M16) ab: kleinerer
Querschnitt (315×90 mm vs. R2 h=800 mm), andere Stangenanzahl/-
durchmesser (2× Ø12 mm je Prüfkörper vs. 4× M16 bei R2), New-Zealand-
Radiata-Pine-Brettschichtholz GL10 statt GL24h/GL75. Ein direkter
Zahlenvergleich mit den R2-Werten (c_T, c_c,90 etc.) ist daher nicht
ohne Weiteres zulässig — als Größenordnungs-/Plausibilitätscheck aber
möglicherweise nützlich, insbesondere weil die Konfiguration
"tensioned" (nur Zugseite verklebt) strukturell der R2-Verbindung
ähnelt (siehe auch R2-COMMON-CLAIM-003).

Wichtig für die Motivation der eigenen Herleitung: die Quelle stellt
explizit fest, dass zum Erhebungszeitpunkt kein allgemeines Verfahren
zur analytischen Steifigkeitsberechnung existierte (siehe
R2-COMMON-CLAIM-001) — diese Tabelle 5 ist rein experimentell, nicht
aus einem analytischen Federmodell hergeleitet.
