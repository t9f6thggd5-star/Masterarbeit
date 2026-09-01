---
claim_id: R2-COMMON-CLAIM-028
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Anfangsdrehsteifigkeit S_j,ini nach Komponentenmethode (Abschnitt
    2.5, Gl. 14-26): S_j,ini = z_eq²/(1/k_t+1/k_c) (Gl. 14, EN 1993-1-8),
    mit Einzelsteifigkeiten je Komponente: k_cc (Stütze Querdruck) =
    E_w,90,l·b_c·(2c+a+d_n)/h_c (Gl. 16); k_bc (Riegel Druck) =
    E_w,0·b_b·√(m_b·(m_b+e+c')) nach Tomasi u. a. (2008) (Gl. 17); k_cs
    (Stütze Schub) = G_w·A_c/z_eq = G_w·b_c·h_c/z_eq, klassische Kurz-
    stützen-Schubtheorie (Gl. 18); k_bt (Schraube Zug) = E_b·A_bt/l_bt
    (Gl. 19); k_srtb (Stahlkastenprofil Biegung) mit/ohne Prying-Kräfte
    nach EN 1993-1-8 (Gl. 20-21); k_srtc (Stahlkastenprofil Druck, ohne
    Steife) = 32·E_s·b_f·t_f³/h_srt³ — MIT Steife wird die Steifigkeit
    als UNENDLICH angenommen (Gl. 26, "assumed to be infinite"). WICHTIG
    — Steifigkeit der eingeklebten Gewindestange auf Zug k_grt, aus
    EN 1993-1-8 (dort als Ankerbolzen-Formel), Gl. 22-23: MIT
    Prying-Kräften k_grt=1.6·E_gr·A_gr/L_b; OHNE Prying-Kräfte
    k_grt=2.0·E_gr·A_gr/L_b — mit der "elongation length" L_b=α·U_gr
    (Gl. 24), wobei α ein von Tomasi u. a. (2008) vorgeschlagener,
    auf der Volkersen-Analyse (1938, einschnittige Klebeverbindung)
    basierender Koeffizient ist: α=[1/(45.8·E_w,0)+1/(45.8·E_w,0·√
    (E_gr/G_a·U_gr/A_gr,s·t_a))]^0.5 (Gl. 25). Analog wird k_gtt (Stahl-
    rohr auf Zug) nach derselben Methode bestimmt. Fazit der Autoren
    (Abschnitt 3.3, anhand Versuchsauswertung): die Anfangsdrehsteifig-
    keit des Gesamtanschlusses wird hauptsächlich von k_cc, k_cs und
    k_srtc bestimmt (relativ NIEDRIGE Werte), während k_grt/k_gtt
    (Gewindestangen/Stahlrohr auf Zug) SO HOCH sind, dass sie "als
    unendlich betrachtet werden können" — die Zugseite ist in diesem
    Verbindungstyp praktisch NICHT die Steifigkeits-bestimmende
    Komponente.
  source: YangLiuRen2016
  pages: "46-47"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

SEHR RELEVANT für R2s Zugstangen-Steifigkeit c_ax,f (siehe R2-COMMON-
CLAIM-006/008/012 zu Lipperts/Ehlbecks/Aichers z. T. stark streuenden
Werten): dies ist eine VIERTE, unabhängige Formel für die axiale
Steifigkeit eingeklebter Gewindestangen (k_grt nach EN 1993-1-8/
Volkersen-Ansatz über L_b statt direkt über die Einklebelänge l_g) —
methodisch grundverschieden von den DIN-V-ENV-1995-2- und Aicher(2001a)-
Ansätzen. Der QUALITATIVE Befund, dass die Gewindestangen-Zugsteifigkeit
in diesem Verbindungstyp so hoch ist, dass sie praktisch als "unendlich"
behandelt werden kann, ist eine interessante, aber NICHT unbesehen auf
R2 übertragbare Aussage — sie gilt für diese spezifische Geometrie
(Douglas-Fir-BSH GL36h, andere Abmessungen) und könnte für R2 (GL24h/
GL75, andere Stangenlänge/-anzahl) anders ausfallen. Ob k_cc/k_cs (die
hier als steifigkeitsbestimmend identifizierten Druckseiten-Komponenten)
strukturell den in R2-COMMON-OPQ-001 gesuchten Druckseiten-Federn
c_c,90/c_c,0 entsprechen, ist naheliegend, aber nicht verifiziert.
Formeln wurden nicht nachgerechnet oder auf R2 angewendet.
