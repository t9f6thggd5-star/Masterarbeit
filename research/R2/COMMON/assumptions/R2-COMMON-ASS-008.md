---
assumption_id: R2-COMMON-ASS-008
scope:
  connection: R2
  material: COMMON
type: ASSUMPTION
statement: >
  Das Setzen bzw. Anpressen der Stahl-Ankerplatte auf das Holz (Zug- und
  Druckseite) erzeugt vorerst keinen Anfangsschlupf. Der Anfangsschlupf der
  Zugseite wird nur aus der eingeklebten Gewindestangengruppe angesetzt.
  Auf der Zugseite liegt dabei genau eine Stangengruppe in Reihe (4× M16 als
  zwei parallele Stangenpaare einer Gruppe), also φ_S = v0 / z.
reason: >
  Nutzerangaben (Chat, 2026-09-28): Bestätigung "2 parallele Stangenpaare in
  einer Gruppe"; Ankerplatte vorerst ohne Schlupf, Frage bleibt offen
  (R2-COMMON-OPQ-012). Die Zugseitenkette (R2-GL24h-CALC-021) enthält die
  Stangengruppe einmal (c_Stange,4x aus den 2×2-Zugversuchen BR-22).
basis: Nutzer, 2026-09-28
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Präzisiert die Formulierung "2 je Zugpfad" in R2-COMMON-ASS-002: gemeint
sind zwei parallele Stangenpaare derselben Gruppe, nicht zwei Gruppen in
Reihe.

**Ergänzung (2026-09-28), keine Vorspannung:** Laut Nutzer werden die
Muttern an der Ankerplatte nur festgedreht, nicht vorgespannt. Eine
Vorspannung der Stangen wird daher nicht angesetzt. (Buchholz2025, Abschn.
4.3, beschreibt die Stangen als nur in die Stütze eingeklebt, im Riegel frei
durch leicht größere Bohrungen geführt und oben mit Muttern gegen eine
Stahlplatte angezogen.)

**Hinweis zur ID (2026-09-28):** Dieser Eintrag wurde zunächst versehentlich
unter der bereits vergebenen ID R2-COMMON-ASS-007 (Versuchsgeometrie
Konfiguration 2/3) angelegt und hat diese Datei überschrieben. Die
Geometrie-Annahme wurde unter R2-COMMON-ASS-007 wiederhergestellt; dieser
Inhalt führt jetzt die ID R2-COMMON-ASS-008.
