---
decision_id: R2-GL24h-DEC-008
scope:
  connection: R2
  material: GL24h
type: DECISION
question: >
  Soll die einseitige Lastausbreitung in der Zugseiten-Steifigkeitskette
  (`c_c,90`, siehe R2-GL24h-CALC-001/002) ebenfalls auf beidseitige
  Lastausbreitung umgestellt werden — analog zur Korrektur der
  unverstärkten und verstärkten Querdrucktragfähigkeit unter der
  Ankerplatte (R2-GL24h-CALC-010/011)?
decision: >
  Nein. Die einseitige Lastausbreitung in der Zugseiten-Steifigkeitskette
  (`c_c,90`, R2-GL24h-CALC-001/002) bleibt unverändert bestehen und wird
  nicht auf beidseitig umgestellt.
reason: >
  Bei dieser Komponente liegt die Stahlplatte direkt am Trägerrand, sodass
  sich die Lastausbreitung geometrisch nur in eine Richtung ausbilden
  kann — anders als bei der Querdrucktragfähigkeit unter der
  Ankerplatte (R2-GL24h-CALC-010/011), wo eine beidseitige Ausbreitung
  möglich ist. Angabe des Nutzers, 2026-09-01.
alternatives_considered: >
  Umstellung auf beidseitige Lastausbreitung analog zu
  R2-GL24h-CALC-010/011 — verworfen, da die reale Randbedingung
  (Stahlplatte am Trägerrand) eine beidseitige Ausbreitung an dieser
  Stelle nicht zulässt.
date: "2026-09-01"
---

Dokumentiert die explizite Entscheidung des Nutzers, die in
R2-GL24h-CALC-010 (Nächste-Schritte-Hinweis) aufgeworfene Folgefrage
("Ist die einseitige Lastausbreitung auch in der Zugseiten-Kette zu
korrigieren?") für `c_c,90` in R2-GL24h-CALC-001/002 **nicht** analog
zur Querdruckkorrektur unter der Ankerplatte umzustellen — im Gegensatz
zur dortigen Situation liegt bei dieser Komponente eine echte
randnahe/einseitige Lastausbreitungsgeometrie vor (Stahlplatte direkt am
Trägerrand), nicht ein bloßer Excel-Fehler. R2-GL24h-CALC-001/002 bleiben
damit inhaltlich unverändert gültig; kein `superseded_by`-Verweis nötig.
