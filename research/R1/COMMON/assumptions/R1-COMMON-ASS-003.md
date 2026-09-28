---
assumption_id: R1-COMMON-ASS-003
scope:
  connection: R1
  material: COMMON
type: ASSUMPTION
statement: >
  Geometrie des R1-Rahmeneckversuchs (Einbau Konfiguration 1) für die
  Umrechnung von Eckverdrehung Φ auf Maschinenkraft F und Maschinenweg u_M:
  symmetrischer Rahmen mit Gehrung, Schenkelneigung α = 36°,
  Querschnittshöhe h = 800 mm, Schenkellänge 4,00 m (entlang Außenkante),
  Gesamtbreite 6,472 m, Bolzenabstand der Fußgelenke 4,065 m, äußere
  Spitze 2842 mm über der Zylinderachse. Bezugspunkt der Ecke ist der
  Schnittpunkt der Schwerachsen (h_m), er liegt h / (2·cos α) = 494,4 mm
  unter der äußeren Spitze. Hebelarm der Kolbenkraft um die Ecke:
  a = 2842 − 494,4 = 2347,6 mm.
reason: >
  Benötigt für die Übersichtstabelle F_est / Φ / u_M (COMMON-COMMON-DEC-008).
  Die Kolbenkraft wirkt horizontal auf Höhe der Zylinderachse (Höhe 0 der
  Skizze), daher ist der Hebelarm der vertikale Abstand Zylinderachse bis h_m.
basis: >
  PLAN-Einbau-Konfiguration1 (Skizze, Maße 4,00 m, 80 cm, 4,065 m, 6,472 m,
  2842 mm, 35 cm). α = 36° und Einheit cm für "80" vom Nutzer angegeben
  (Chat, 2026-09-28). Bezugspunkt h_m vom Nutzer bestätigt (2026-09-28).
supported_by: PLAN-Einbau-Konfiguration1
contradicted_by:
certainty: ASSUMED
superseded_by:
---

**Herleitung (2026-09-28):**
- Auf der Symmetrieachse schneidet ein Schenkel der Höhe h mit Neigung α
  die vertikale Strecke h / cos α = 800 / cos 36° = 988,9 mm heraus
  (äußere Spitze bis innerer Eckpunkt, h_i). Der Nutzer hatte ≈ 988,78 mm
  angegeben; das ist dieser innere Eckpunkt, nicht die Mitte.
- Schwerachsen-Schnittpunkt h_m: h / (2·cos α) = 494,4 mm unter der Spitze.
- Hebelarm: 2842 − 494,4 = 2347,6 mm.

**Konsistenzprüfung:** 4,00 m · cos 36° · 2 = 6,472 m = bemaßte
Gesamtbreite ✓ (bestätigt α = 36° und dass die Schenkellänge entlang der
Außenkante bemaßt ist).

**Weitere Angaben aus der Skizze bzw. vom Nutzer (2026-09-28):**
- Der Kolben zieht sich im Versuch zusammen, geprüft wird ein
  schließendes Moment (Zugseite außen, Druckseite innen).
- 35 cm ist der Kolbenweg; ob Gesamthub oder Resthub, ist unbekannt
  (COMMON-COMMON-OPQ-004).

Die Skizze gilt nur für R1. R2 und R3 haben eine andere Geometrie
(R2-COMMON-ASS-007, R3-COMMON-ASS-001).
