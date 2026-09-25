---
decision_id: R3-GL24h-DEC-014
scope:
  connection: R3
  material: GL24h
type: DECISION
question: >
  Welches Lastfenster gilt als Hauptwert für die Rekonstruktion der
  Steifigkeit der Beam-seitigen 4×4-Schraubengruppe aus der Erstbelastung
  von III-PO-S-SC-44-B-1, dessen Normfenster 0,1–0,4 · F_est (29–116 kN)
  wegen Querdruckversagens des Mittelholzes bei 94 kN nicht erreicht wurde?
decision: >
  Hauptwert ist das Lastfenster 10–20 % F_est (29–58 kN). Die Lastfenster
  3–13 % F_est (10–40 % von F_max,Versuch) und 10–28 % F_est (29–80 kN)
  werden als Vergleich weitergeführt.
reason: >
  Nach der Rückmeldung der Betreuung (vom Nutzer im Chat weitergegeben,
  2026-09-25, zu R1-COMMON-OPQ-004) wird die Steifigkeit im auf F_est
  bezogenen Lastfenster ausgewertet, im linear-elastischen Bereich und
  ohne Anfangsschlupf; eine geringere Höchstlast aus einem anderen
  Versagensmodus steht nicht in direktem Zusammenhang mit der Steifigkeit.
  Das Lastfenster 10–20 % F_est ist das einzige der drei, das (1) wie die
  Norm bei 0,1 · F_est beginnt, (2) vollständig vor dem Querdruckbeginn im
  Mittelholz (≈ 50–64 kN) liegt und damit linear-elastisch ist und (3) den
  Anfangsschlupf ausschließt. 3–13 % F_est liegt im Bereich des
  Anfangsschlupfs (an den 1×1-Serien ist die Trägerseite dort deutlich
  weicher als im Normfenster); 10–28 % F_est reicht bereits in den Bereich,
  in dem das Mittelholz nachgibt. Die einzige verbleibende Abweichung zur
  Norm ist die obere Grenze (20 statt 40 % F_est).
alternatives_considered: >
  Lastfenster 3–13 % F_est (EN 26891 sinngemäß mit F_est := F_max) —
  enthält Anfangsschlupf, F_max folgt aus einem anderen Versagensmodus.
  Lastfenster 10–28 % F_est — schon im Bereich des Querdrucks.
date: "2026-09-25"
superseded_by:
---

Ergebnis siehe R3-GL24h-CALC-010. Welcher Wert in die Zugpfadkette geht
(Faktor 0,8028 nach ASS-004/CALC-008 oder die Rekonstruktion), ist damit
noch nicht entschieden (R3-GL24h-OPQ-022).
