---
decision_id: R1-COMMON-DEC-004
scope:
  connection: R1
  material: COMMON
type: DECISION
question: >
  Nach welchem Federmodell wird die Anfangsrotationssteifigkeit der
  R1-Rahmenecke (Schlitzblech + Stabdübel) berechnet, und wie werden die
  vier Drehfedern C_rot,v,f der Dübelgruppen kombiniert?
decision: >
  Es wird das Federmodell nach Buchholz2025, Abschn. 4.2, Gl. (1) bis (5)
  verwendet: c_c,tot = 1/(1/c_v,f + 1/c_c,0 + 1/c_c,0 + 1/c_v,f),
  c_t,tot = 1/(1/c_v,f + 1/c_br,par + 1/c_br,par + 1/c_v,f),
  C_rot,t+c = z²/(1/c_t,tot + 1/c_c,tot), C_rot,v,f = I_p · K_ser und
  C_rot,tot = C_rot,t+c + Σ C_rot,v,f,i, mit Summe über die vier
  Dübelgruppen (Träger/Stütze, Zug-/Druckzone).
reason: >
  Entscheidung des Nutzers (2026-09-26, "wir folgen dem Federmodell nach
  Buchholz"). Referenzmodell der Betreuung für den R1-Anschlusstyp
  (vgl. R1-COMMON-DEC-001).
alternatives_considered: >
  (a) Drehfedern von Träger- und Stützengruppe in Reihe (physikalische
  Lesart, R1-GL24h-CALC-007). (b) Polares Modell je Bauteil (Kräftepaar und
  Gruppendrehung um die Mitte zwischen Zug- und Druckgruppe, Träger und
  Stütze in Reihe; Claude-Entwurf in der Übersichtstabelle vom 2026-09-26,
  S_j,ini = 62.808 kNm/rad für GL24h). Beide nicht gewählt.
date: "2026-09-26"
---

**Stand der Eingangsgrößen (2026-09-26):**
- c_v,f Zugzone: gemessene Gruppensteifigkeit c_T (R1-GL24h-CALC-008,
  R1-GL75-CALC-005; laut Betreuung reine c_v,f, R1-COMMON-OPQ-003).
- c_br,par: vorläufig starr (Arbeitsannahme des Nutzers, offener
  Diskussionspunkt, R1-COMMON-OPQ-005).
- Schlitzblech: starr (R1-COMMON-DEC-003).
- c_v,f Druckzone und c_c,0: noch offen (R1-GL24h-OPQ-008,
  R1-COMMON-OPQ-005 (c)).
- C_rot,v,f je Gruppe: R1-GL24h-CALC-007 bzw. R1-GL75-CALC-004
  (K_ser nach R1-GL24h-DEC-010 bzw. R1-GL75-DEC-001).

**Lesart der Abbildung (Nutzer, 2026-09-26):** In Abb. 3 sind die
Drehfedern C_v,f,rot zwar in der Kette der Zug- bzw. Druckzone gezeichnet,
aber durch die Knotenpunkte von den Translationsfedern getrennt; sie
wirken auf den Verdrehungsfreiheitsgrad, nicht auf die Verschiebung. Der
Satz im Fließtext (S. 1746, "also connected in series") steht damit nicht
im Widerspruch zu Gl. (5). Gerechnet wird nach Gl. (5): vier Drehfedern
(Träger/Stütze × Zug-/Druckzone) je C_rot,v,f, summiert; für GL24h
4 · 21.111 = 84.444 kNm/rad (Nutzer bestätigt 2026-09-26).

**Hinweis (Claude, nicht entschieden):** In c_t,tot/c_c,tot liegen Träger-
und Stützengruppe in Reihe, in Gl. (5) erfährt dagegen jede Gruppe die
volle Eckverdrehung. Bei starrem Blech gilt kinematisch φ = θ_Träger +
θ_Stütze; konsequent in Reihe gerechnet ergäbe sich für GL24h nur einmal
C_rot,v,f statt viermal (≈ 63.000 statt ≈ 127.000 kNm/rad bei
c_c,tot = c_t,tot). Kann bei Bedarf mit der Betreuung (Mitautorin)
angesprochen werden.
