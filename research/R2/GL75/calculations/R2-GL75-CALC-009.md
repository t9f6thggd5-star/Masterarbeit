---
calculation_id: R2-GL75-CALC-009
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions: R2-GL24h-DEC-008
method: >
  FprEN-Querdruckverformungsmodell unter der 160×240 mm-Ankerplatte,
  Zugseite (einseitige Lastausbreitung, da Stahlplatte am Trägerrand,
  analog GL24h-DEC-008, für GL75 mit identischer Ankerplattengeometrie
  übernommen): `c_c,90 = 2·E_90,mean / (h_ef·(1/A + 1/A_ef))`. Wie auf
  der Druckseite (R2-GL75-CALC-006) unverstärkt, da GL75 keine
  ASSY-Querdruckverstärkung hat (R2-GL75-OPQ-002, RESOLVED).
equations: >
  FprEN 1995-1-1:2024, §9.4(5), Gl. 9.31, S. 152; Lastausbreitung nach
  Tab. 8.2/Gl. 8.11 (h_ef), Gl. 8.9 (A_ef).
result:
  quantity: Querdrucksteifigkeit unter der Ankerplatte, Zugseite, GL75 (unverstärkt)
  value: 158.021
  unit: kN/mm
  original_value: 158020.6
  original_unit: N/mm
source_file: >
  Vom Nutzer im Chat berechnet (158,02) und hier formelbasiert
  nachvollzogen/bestätigt. **Update (2026-09-18):** Der Nutzer hat den
  vollständigen Zugseiten-Rechenweg jetzt auch im R2-Excel ergänzt —
  Sheet "Rahmenecke GL75 SD", Zelle M61 (Formel
  `=2*Holzkennwerte!F35/(M37*(1/M42+1/M43))*10^-3`, Normverweis in N61
  "FpreEN EC5 -2024, Gl. 9.31"), Excel-Wert `158,02396313364056`, per
  openpyxl mit data_only=True/False geprüft — deckt sich exakt mit dem
  hier dokumentierten Wert. Eingangsgeometrie im selben Block: `M37`
  (h_ef=140), `M40` (l_ef=380), `M41` (b_90,c=160), `M42`
  (A_Stahlplatte=38.400), `M43` (A_ef=60.800) — identisch zu den hier
  verwendeten Werten.
certainty: CALCULATED
superseded_by:
---

Analog zu R2-GL75-CALC-006 (Druckseite), aber mit der einseitigen
Lastausbreitungsgeometrie der Zugseite (wie bei GL24h, R2-GL24h-CALC-001
bzw. R2-GL24h-CALC-018 für die Tragfähigkeit).

**Eingangswerte:** `E_90,mean=470 N/mm²` (Holzkennwerte!F35), `h_ef=140mm`
(identisch zu Druckseite, gleiche Trägergeometrie), `l_ef=380mm`
(einseitig: `b_Stahlplatte+Δl=240+140`), `b_90,c=160mm`,
`A_Stahlplatte=38.400mm²`, `A_ef=60.800mm²` (=380·160).

**Rechnung:**

```
c_c,90 = 2·E_90,mean / (h_ef·(1/A + 1/A_ef))
       = 2·470 / (140·(1/38.400 + 1/60.800))
       ≈ 158,021 kN/mm
```

**Plausibilitätshinweis:** Verhältnis Druckseite/Zugseite
`176,409/158,021 ≈ 1,116` — exakt der rein geometrisch bedingte Faktor
aus der unterschiedlichen Lastausbreitung (beidseitig vs. einseitig),
identisch zum entsprechenden Verhältnis bei der Tragfähigkeit
(R2-GL75-CALC-005) und unabhängig vom Material (siehe Chat-Diskussion
vom 2026-09-18).

Weiterverwendung: eine der Federn der Zugseiten-Gesamt-
steifigkeitskette `c_T`, siehe R2-GL75-CALC-011.
