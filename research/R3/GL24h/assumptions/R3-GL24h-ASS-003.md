---
assumption_id: R3-GL24h-ASS-003
scope:
  connection: R3
  material: GL24h
type: ASSUMPTION
statement: >
  Für die Hochrechnung der ASSY-Schraubengruppen-Anfangssteifigkeit
  (Push-Out, 1×1 → 4×4 → real 4×8) wird angenommen, dass die
  Gruppenineffizienz ausschließlich aus der Vervielfachung in
  Kraftrichtung ("Reihen", hintereinander) entsteht, während die
  Vervielfachung quer dazu ("Spalten", nebeneinander) linear ohne
  Abminderung wirkt. Modell: c(n_Spalten, n_Reihen) = n_Spalten · c_1 ·
  n_Reihen^α, mit c_1 = Einzelschrauben-Steifigkeit und α als
  empirisch zu kalibrierendem Exponenten (0 < α ≤ 1; α=1 entspräche
  keiner Gruppenineffizienz). Analog anwendbar auf die Tragfähigkeit
  F(n_Spalten, n_Reihen) = n_Spalten · F_1 · n_Reihen^α mit eigenem,
  im Allgemeinen abweichendem α_F.
reason: >
  Physikalische Vereinfachung (Nutzerentscheidung 2026-09-22): bei
  Schrauben nebeneinander (Spalten) teilt sich die Kraft näherungsweise
  gleichmäßig auf unabhängige Lastpfade auf; bei Schrauben hintereinander
  (Reihen) führt die endliche axiale Steifigkeit von Holzlasche und
  Gewindestange/Hauptbauteil zu ungleicher Lastverteilung zwischen den
  Reihen (ähnlich dem n_ef-Konzept für Nagel-/Schraubengruppen in
  EC5/ETA, dort allerdings nur für Tragfähigkeit und nicht als
  Potenzgesetz normiert) — dies wird hier für die Anfangssteifigkeit
  näherungsweise mit einem eigenen, aus den Push-Out-Versuchen
  kalibrierten Exponenten erfasst.
basis:
supported_by: R3-GL24h-CALC-007
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Eingeführt am 2026-09-22 im Zuge der Hochrechnung der Column-seitigen
(Lasche an Stütze, faserparallel) ASSY-Schraubengruppensteifigkeit von
den getesteten 16 Schrauben (4×4, `III-PO-S-SC-44-C`) auf die reale
32-Schrauben-Gruppe (4×8) im Zugpfad. Der Exponent α selbst ist nicht
Teil dieser Annahme, sondern wird in `R3-GL24h-CALC-007` aus den
vorliegenden Push-Out-Daten kalibriert.

**Geltungsbereich ausdrücklich nur Column-Seite (c_ax+br,par):** Für die
Beam-Seite (c_ax+br,perp, Lasche an Träger, faserparallel andere
Richtung im Hauptbauteil) fehlen verwertbare 4×4-Steifigkeitsdaten
vollständig (`III-PO-S-SC-44-B`, siehe R3-GL24h-OPQ-021) und auch der
dort einzig vorhandene Fmax-Einzelwert (n=1, 47,3 kN) gilt nach
Rücksprache mit dem Nutzer (2026-09-22) nicht als belastbare Datenbasis.
Der Nutzer hat eine direkte Übertragung des hier für die Column-Seite
kalibrierten α auf die Beam-Seite ausdrücklich abgelehnt ("nein ich
möchte nicht mit gleichem alpha rechnen", 2026-09-22), da sich die
Faserrichtung zwischen Column und Beam unterscheidet und keine
empirische Grundlage für die Übertragbarkeit besteht. Die Beam-seitige
Hochrechnung ist damit weiterhin offen und wird gesondert behandelt.
