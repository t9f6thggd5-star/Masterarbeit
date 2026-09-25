---
interpretation_id: R3-GL24h-INT-001
scope:
  connection: R3
  material: GL24h
type: INTERPRETATION
based_on:
  experimental_results: R3-GL24h-III-PO-S-SC-44-B-RES-001, R3-GL24h-CALC-009
  observations: >
    Kraft-Weg-Kurve III-PO-S-SC-44-B-1 (Blatt "III-PO-S-SC-44-B-1" der
    Push-Out-Auswertungsdatei): Maschinenkurve flacht ab ≈ 50 kN ab,
    Plateau ab ≈ 80 kN, danach langsamer Anstieg bis 93,97 kN ohne
    spröden Abfall; die lokalen Wegaufnehmer (VL+HL, VR+HR) verlaufen
    bis ≈ 80 kN nahezu linear und nehmen danach kaum noch zu, während
    der Maschinenweg bis 20,4 mm weiterläuft. Nutzeraussage 2026-09-25:
    PK2 und PK3 der Serie sind durch Querdruck im Mittelholz versagt
    (keine Messdaten).
interpretation: >
  Das Versagen von III-PO-S-SC-44-B-1 ist sehr wahrscheinlich
  Querdruckversagen des Mittelholzes an der Lasteinleitung (Kopffläche
  160 × 160 mm, Last quer zur Faser), nicht Querzugversagen (so noch am
  2026-09-22 vermerkt) und nicht Versagen der Schraubengruppe. Stützend:
  (1) duktiler Kurvenverlauf mit Plateau und Verdichtungsanstieg statt
  sprödem Abfall; (2) Plateau (≈ 80–83 kN) nahe am rechnerischen
  Querdruckwiderstand mit Mittelwert (84,88 kN, CALC-009); (3) die
  Verformung findet außerhalb der Messstrecke der lokalen Wegaufnehmer
  statt; (4) gleicher Mechanismus laut Nutzer bei PK2/PK3. Folge:
  F_max = 93,97 kN (47,3 kN je Scherfuge) ist keine Tragfähigkeit der
  Schraubengruppe, sondern eine Untergrenze. Der Versuchsaufbau
  (R-Variante ohne Querdruckverstärkung der Lasteinleitung) konnte die
  Schraubengruppe bei F_est = 290 kN konstruktionsbedingt nicht zum
  Versagen bringen. Einschränkung: n = 1 mit Kurve.
certainty: INTERPRETED
superseded_by:
authored_by: CLAUDE_DRAFT
reviewed: false
---

Vermutung Querdruck stammt vom Forschenden (Chat 2026-09-25); die
Begründung (1)–(3) und der Abgleich mit CALC-009 sind von Claude
ergänzt und noch nicht geprüft (CLAUDE.md Abschnitt 14).

Ob die lokale Steifigkeit unterhalb des Querdruckbeginns (≈ 50–64 kN)
als Steifigkeit der Beam-seitigen Schraubengruppe verwendbar ist, wird
gesondert untersucht (Rekonstruktion, siehe R3-GL24h-OPQ-022) und ist
nicht Teil dieser Interpretation.
