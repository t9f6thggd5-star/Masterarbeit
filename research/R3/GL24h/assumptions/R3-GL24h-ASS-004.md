---
assumption_id: R3-GL24h-ASS-004
scope:
  connection: R3
  material: GL24h
type: ASSUMPTION
statement: >
  Das Verhältnis der Einzelschrauben-Anfangssteifigkeit Beam/Column
  (c1,Beam/c1,Column = 6,881/8,571 = 0,8028, aus den 1×1-Push-Out-Werten)
  wird als bei jeder Schraubenanzahl der ASSY-Schraubengruppe konstant
  angenommen — also auch für die 4×4- und die reale 4×8-Gruppe:
  c_n,Beam = c_n,Column · (c1,Beam/c1,Column). Äquivalent dazu: der in
  R3-GL24h-ASS-003 eingeführte Gruppenineffizienz-Exponent α wird
  implizit als faserrichtungsunabhängig (gleich für Beam und Column)
  behandelt — beide Formulierungen führen rechnerisch zum exakt
  gleichen Ergebnis (Nachweis siehe Diskussion 2026-09-22).
reason: >
  Für die Beam-Seite liegen keine verwertbaren 4×4-Steifigkeitsdaten vor
  (III-PO-S-SC-44-B: PK2/PK3 ohne jede Messkurve, PK1 mit Steifigkeit
  manuell als "nv" markiert — Ursache laut Nutzerhinweis 2026-09-22
  Querzugversagen im Holz [korrigiert 2026-09-25: Querdruck im
  Mittelholz, siehe R3-GL24h-INT-001], d. h. ein anderer Versagensmechanismus als
  die ASSY-Schraubengruppen-Steifigkeit selbst; siehe R3-GL24h-OPQ-021).
  Auch der einzige Fmax-Wert dieser Serie (n=1, 47,3 kN) gilt aus
  demselben Grund nicht als belastbare Datenbasis für eine indirekte
  Ableitung (Nutzerentscheidung 2026-09-22, siehe verworfene
  Kreuzverhältnis-Methode unten). Eine unabhängige, empirische oder
  normative Bestimmung des Beam-seitigen Gruppeneffekts war trotz
  Prüfung mehrerer Ansätze nicht möglich:
  - Übertragung des Column-kalibrierten Potenzgesetz-Exponenten α
    (R3-GL24h-ASS-003) — vom Nutzer verworfen, da die Faserrichtung
    zwischen Beam und Column wechselt und keine empirische Grundlage
    für die Übertragbarkeit besteht.
  - Kreuzverhältnis-Schätzung über das Beam/Column-Tragfähigkeits-
    verhältnis (Verschiebungsfaktor-Methode) — verworfen, da sie
    vollständig vom einzigen, nicht belastbaren 44-B-Fmax-Wert abhängt.
  - Normative n_ef-Formel (FprEN 1995-1-1 Tab. 11.10(6), im Push-Out-
    Workbook für die Column-Seite mit n_ef≈12,48 hinterlegt) — diese
    Formel ist grundsätzlich faserrichtungsunabhängig, liefert also
    zwangsläufig dasselbe Verhältnis wie diese Annahme hier (siehe
    Diskussion 2026-09-22: jedes Modell mit einer gemeinsamen,
    faserrichtungsunabhängigen Gruppenfunktion führt auf dasselbe
    Beam/Column-Verhältnis).
  - Literaturrecherche (2026-09-22): keine verwertbare, validierte
    Formel für die Steifigkeits-Gruppeneffizienz axial beanspruchter
    Schraubenreihen in Abhängigkeit vom Faserwinkel gefunden.
    Stamatopoulos & Malo (2017, "Withdrawal of pairs of threaded rods
    with small edge distances and spacings") zeigen zwar, dass der
    Tragfähigkeits-Gruppeneffekt bei Gewindestangenpaaren tatsächlich
    vom Faserwinkel abhängt (n_ef zwischen 1,72 und 1,94 je nach
    Winkel 15°–90°) — das bestätigt physikalisch, dass diese Annahme
    hier eine echte Vereinfachung ist, liefert aber keine direkt
    anwendbare Formel für unseren Fall.
  Diese Annahme ist damit eine bewusste, vorläufige Vereinfachung
  (Nutzerentscheidung 2026-09-22), keine abgesicherte Methode.
basis: R3-GL24h-ASS-003, R3-GL24h-III-PO-S-SC-11-B-RES-004, R3-GL24h-III-PO-S-SC-11-C-RES-004
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Eingeführt am 2026-09-22 als pragmatischer Ersatz, nachdem sowohl die
direkte α-Übertragung als auch die Kreuzverhältnis-Methode verworfen
wurden bzw. sich als nicht robust erwiesen. Sollte künftig eine
belastbare Beam-seitige Gruppen-Steifigkeitsmessung (neuer Push-Out-
Versuch III-PO-S-SC-44-B mit auswertbaren Prüfkörpern) verfügbar
werden, ist diese Annahme durch den Messwert zu ersetzen und diese
Annahme entsprechend als `superseded_by` zu kennzeichnen.
