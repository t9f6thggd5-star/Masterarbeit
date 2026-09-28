---
assumption_id: R3-COMMON-ASS-001
scope:
  connection: R3
  material: COMMON
type: ASSUMPTION
statement: >
  Geometrie des R3-Rahmeneckversuchs (Einbau Konfiguration 2/3) für die
  Umrechnung von Eckverdrehung Φ auf Maschinenkraft F und Maschinenweg u_M:
  symmetrischer Rahmen, Stütze und Riegel im 90°-Winkel (je 45° zur
  Horizontalen), keine Gehrung, Querschnittshöhe h = 800 mm, Schenkellänge
  4,80 m (entlang Außenkante), Gesamtbreite 6,788 m, Bolzenabstand der
  Fußgelenke 4,065 m, äußere Ecke 3595 mm über der Zylinderachse.
  Bezugspunkt der Ecke ist der Schnittpunkt der Schwerachsen (h_m), er
  liegt h / (2·cos 45°) = 565,7 mm unter der äußeren Ecke. Hebelarm der
  Kolbenkraft um die Ecke: a = 3595 − 565,7 = 3029,3 mm.
reason: >
  Benötigt für die Übersichtstabelle F_est / Φ / u_M (COMMON-COMMON-DEC-008).
  Die Kolbenkraft wirkt horizontal auf Höhe der Zylinderachse (Höhe 0 der
  Skizze), daher ist der Hebelarm der vertikale Abstand Zylinderachse bis h_m.
basis: >
  PLAN-Einbau-Konfiguration2-3-R3 (Skizze, Maße 4,80 m, 80 cm, 4,065 m, 6,788 m, 3595 mm, 35 cm).
  Einheit cm für "80", 90°-Winkel ohne Gehrung und Bezugspunkt h_m vom
  Nutzer angegeben bzw. bestätigt (Chat, 2026-09-28).
supported_by: PLAN-Einbau-Konfiguration2-3-R3
contradicted_by:
certainty: ASSUMED
superseded_by:
---

**Herleitung (2026-09-28):**
- Äußere Ecke bis innerer Eckpunkt: h / cos 45° = 1131,4 mm (Nutzerangabe
  ≈ 1131,22 mm entspricht diesem inneren Eckpunkt, nicht der Mitte).
- Schwerachsen-Schnittpunkt h_m: h / (2·cos 45°) = 565,7 mm unter der Ecke.
- Hebelarm: 3595 − 565,7 = 3029,3 mm.

**Konsistenzprüfung:** 4,80 m · cos 45° · 2 = 6,788 m = bemaßte
Gesamtbreite ✓.

**Weitere Angaben (Nutzer, 2026-09-28):** Der Kolben zieht sich zusammen,
geprüft wird ein schließendes Moment (Zugseite außen, Druckseite innen).
35 cm ist der Kolbenweg; Gesamt- oder Resthub unbekannt
(COMMON-COMMON-OPQ-004).

R2 und R3 verwenden laut Nutzer exakt dieselbe Einbauskizze; der Eintrag
wird wegen der strukturellen Trennung der Anschlüsse (CLAUDE.md Abschnitt 3)
je Anschluss geführt. Vergleiche R1-COMMON-ASS-003, R2-COMMON-ASS-007.
