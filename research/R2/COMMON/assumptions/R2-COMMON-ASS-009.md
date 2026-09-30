---
assumption_id: R2-COMMON-ASS-009
scope:
  connection: R2
  material: COMMON
type: ASSUMPTION
statement: >
  Messbasis der Gewindestangen-Zugversuche BR-22 (und BR-11): Der
  Wegaufnehmer ist seitlich am Holz 3 cm unterhalb der Hirnholzkante
  befestigt; seine Messspitze liegt auf einem Metallblech-Anschlag, der
  etwa 3 cm über der Hirnholzkante an den Stangen befestigt ist
  (Messlänge insgesamt ≈ 6 cm). Gemessen wird damit die Verschiebung der
  Stangengruppe relativ zum Holz am Stangenaustritt: im Wesentlichen der
  Verbund-/Auszugsweg (c_ax,f,par) zuzüglich der Stangendehnung über ≈ 30 mm
  und einer vernachlässigbaren Holzverformung. Nicht enthalten sind der
  Querdruck unter der Ankerplatte (c_c,90), das Schubfeld (c_v) und die
  Dehnung der freien Stangenlänge in der Rahmenecke (c_t).
reason: >
  Versuchsskizze und Angaben des Nutzers (Chat, 2026-09-28). Klärt für R2 die
  nach der Betreuungs-Rückmeldung vom 2026-09-25 offene Frage, ob im
  Messwert Holzanteile enthalten sind: c_c,90 und c_v werden nicht doppelt
  gezählt; die freie Stangendehnung ist dagegen getrennt anzusetzen.
basis: Skizze des Versuchsaufbaus (vom Nutzer im Chat bereitgestellt, nicht im Quellenordner registriert), Nutzer 2026-09-28
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Folge: In der messwertbasierten Zugseitenkette wird die freie Stangendehnung
c_t = 4 · E_s·A_s / l_frei mit l_frei = l_t − 30 mm = 770 mm ergänzt (die
30 mm über der Hirnholzkante sind im Messwert enthalten), siehe
R2-GL24h-CALC-024 und R2-GL75-CALC-013. Keine Übertragung auf R1/R3 ohne
eigene Prüfung (CLAUDE.md Abschnitt 4).
