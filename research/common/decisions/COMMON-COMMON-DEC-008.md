---
decision_id: COMMON-COMMON-DEC-008
scope:
  connection: COMMON
  material: COMMON
type: DECISION
question: >
  Wie wird die von der Betreuung gewünschte Übersicht (geschätzte
  Höchstlast F_est, Verdrehung Φ bei F_est, Maschinenweg u_M bei F_est für
  R1, R2, R3 je GL24h und GL75) für die Besprechung am 2026-09-30 definiert?
decision: >
  (1) F_est in der Übersicht ist die geschätzte Höchstlast der Maschine
  (Kolbenkraft F) im Rahmeneckversuch, nicht das F_est der
  Komponentenversuche (z. B. 480 kN bei R1/GL24h); beide werden in der
  Tabelle eindeutig unterschieden bezeichnet. (2) Die Momententragfähigkeit
  M_R wird vorerst nur über das Kräftepaar angesetzt (keine Tragreserve aus
  der Gruppendrehung, vgl. R1-COMMON-OPQ-007). (3) F_est = M_R / a mit dem
  Hebelarm a von der Zylinderachse zum Schwerachsen-Schnittpunkt h_m der
  Ecke. (4) u_M ist der horizontale Kolbenweg (Änderung des Abstands der
  Fußbolzen, in Richtung von F) und wird vorerst nur aus der
  Anschlussverdrehung gerechnet: u_M ≈ Φ · a (kleine Winkel).
  (5) Geprüft wird ein schließendes Moment (Kolben zieht sich zusammen).
reason: >
  Anforderung der Betreuung (vom Nutzer im Chat weitergegeben, 2026-09-28);
  Festlegungen (1)–(5) vom Nutzer im Chat, 2026-09-28. Geometrie je
  Anschluss: R1-COMMON-ASS-003 (a = 2347,6 mm), R2-COMMON-ASS-007 und
  R3-COMMON-ASS-001 (a = 3029,3 mm).
alternatives_considered: >
  F_est als Komponentenlast — nach Rückfrage verworfen (Nutzer-Korrektur,
  2026-09-28). u_M inkl. Biegung/Schub von Riegel und Stütze und
  Nachgiebigkeit der Auflager — vorerst zurückgestellt, Klärung in der
  nächsten Besprechung (COMMON-COMMON-OPQ-004). Bezugspunkt innerer
  Eckpunkt h_i — verworfen zugunsten h_m.
date: "2026-09-28"
superseded_by:
---

Vor dem Eintragen der M_R-Werte ist je Anschluss zu prüfen, dass das
Kräftepaar für das schließende Moment aufgestellt ist (Zugseite außen).
