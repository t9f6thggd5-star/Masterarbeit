---
claim_id: R2-COMMON-CLAIM-021
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Verifikation des mechanischen Modells (Abschnitt 6.6) an den beiden
    Versuchskörpern zur Bruchlast: bei Versuchskörper 1 (unverstärkt,
    F_u=164.8kN) sagt das Modell rechnerisch sowohl das Versagen der
    Druckzone (σ_c,i=15.1 > 11.3 N/mm² zulässig) als auch ausreichende
    Tragreserven der Gewindestangen (Interaktionsnachweis Gl. 6.58:
    Ausnutzung 0.57<1) korrekt voraus — deckt sich mit dem beobachteten
    Druckzonenversagen. Bei Versuchskörper 2 (verstärkt, F_u=303.9kN)
    sagt das Modell korrekt das Versagen der Gewindestangenverklebung
    voraus (Interaktionsnachweis Gl. 6.85: Ausnutzung 1.57>1, Versagen),
    während sowohl Kontaktzone als auch Schlitzblech-Stabdübelverbindung
    noch Tragreserven hatten. Konkretes Zahlenbeispiel zur Kraftteilung
    zwischen Kontakt und Verstärkung nach "Option 1" aus
    R2-COMMON-CLAIM-019 (Aufteilung nach Tragfähigkeitsverhältnis, da
    Kontaktsteifigkeit nicht eindeutig bestimmbar): Tragfähigkeit
    Kontaktzone F_r,c,i,1=361.6kN vs. Tragfähigkeit Schlitzblech
    (16 Stabdübel, 2 Reihen) F_r,c,i,2=355.2kN → nahezu hälftige
    Aufteilung, 50.5% Kontakt zu 49.5% Schlitzblech (Gl. 6.87). Bei
    Körper 1 tragen die äußeren Zugstangen (nach der 40%-Höhen-Regel,
    siehe R2-COMMON-CLAIM-017) rechnerisch 60% der Gesamtzugkraft, exakt
    übereinstimmend mit dem in Abschnitt 5.6.5 gemessenen Wert (siehe
    R2-COMMON-CLAIM-016).
  source: Lippert2002
  pages: "159-168"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Bestätigt, dass Lipperts Modell (Kapitel 6, siehe R2-COMMON-CLAIM-
017/018/019/020) in sich konsistent ist und die beobachteten
Versagensmechanismen der beiden Versuchskörper korrekt vorhersagt —
ein Hinweis auf die grundsätzliche Verlässlichkeit des Modellansatzes
innerhalb des untersuchten Parameterbereichs (16×70cm² BS16h, M20).
Für R2 selbst keine neue Erkenntnis über die bereits dokumentierten
Modellbausteine hinaus (CLAIM-017 bis -020), sondern deren
Verifikationsnachweis. Das 50.5%/49.5%-Zahlenbeispiel ist NICHT direkt
auf R2 übertragbar (andere Geometrie/Verbindungsmittel), zeigt aber,
wie "Option 1" aus CLAIM-019 in der Praxis rechnerisch angewendet wird
— relevant als methodisches Vorbild für R2-COMMON-OPQ-008, falls dort
eine tragfähigkeitsbasierte Kraftaufteilung zwischen Kontakt und
Querdruckverstärkung angesetzt werden soll.
