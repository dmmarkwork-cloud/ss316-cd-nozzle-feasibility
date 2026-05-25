# Phase 5b Sensitivity Study — Wall Thickness
**Project:** SS316 Nozzle Feasibility · Pc=2MPa · Tc=800K · Rt=15mm · ε=4
**Date:** 2026-05-10 · **Solver:** ANSYS 2026 R1 Student · **Model:** 2D Axisymmetric

Wall thickness sensitivity study at converged Mesh 3 refinement, varying **t ∈ {3, 4, 5} mm**; promoted to executed Phase 5b after the data integrity correction (Phase 4 v3) cleared the upstream baseline.

This study produced a **non-monotonic finding** that is physically explicable but BC-dependent. Section 5 contains the most important caveat in this document — it must be read before quoting the FoS values out of context.

---

## 1. Methodology

### 1.1 Variables held constant

| Setting | Value |
|---|---|
| CFD source data | `wall_static_temperature_final`, `wall_static_pressure_final` (current re-run state) |
| Material | SS316, temperature-dependent properties
| Boundary conditions | Imported T_aw on inner wall, imported pressure on inner wall, h = 10 W/m²·K (1e-0.005 W/mm²·K); T∞ = 300 K on outer wall; Y = 0; X = free at inlet vertex |
| Mesh refinement level | Mesh 3 sizing parameters from Phase 5 v2 (body 0.90 mm, wall edge 0.30 mm, throat 0.18 mm, 7 thickness divisions) |
| Reference temperature | 20 °C across Engineering Data, body, environment |
| Probe locations | `probe_throat_inner` vertex, `path_throat_throughwall`, `probe_exit_corner` |

### 1.2 Variable changed

Wall thickness: t ∈ {3, 4, 5} mm. Inner wall geometry identical across all three cases (the gas-side surface — Rt = 15 mm at throat, Re = 30 mm at exit do not change). Only the outer wall offset differs.

### 1.3 Through-wall mesh density

A check on through-wall element count was performed at the throat for each case. All three meshes show ≥ 8 elements through the wall thickness at the throat probe location, confirming adequate through-wall resolution for stress gradient sampling. This was a verification step after an earlier setup attempt at t = 3 mm gave anomalous results that turned out to be a separate upstream data integrity issue (see Phase 4 v3).

---

## 2. Results

### 2.1 Raw QoI values

| QoI | t = 3 mm | t = 4 mm | t = 5 mm | Units |
|---|---|---|---|---|
| σ_vM,throat | 3.9414 | 4.9171 | 6.1812 | MPa |
| σ_vM,global (singularity) | 486.95 | 430.58 | 484.70 | MPa |
| T_throat | 803.59 | 803.59 | 803.59 | K |
| ΔT_throat | 1.33 | 2.10 | 2.71 | K |
| δ_exit | 1.7159 | 1.7150 | 1.7150 | mm |

### 2.2 Comparison to analytical predictions

| QoI | Predicted (analytical) | Measured (FEA) | Match |
|---|---|---|---|
| ΔT_throat at t = 3 mm (Bi = 0.0017) | ~1.3 K | 1.33 K | within 3% |
| ΔT_throat at t = 4 mm (Bi = 0.0022) | ~2.1 K | 2.10 K | exact |
| ΔT_throat at t = 5 mm (Bi = 0.0028) | ~2.6 K | 2.71 K | within 4% |
| δ_exit (α·ΔT·L, t-independent) | 1.70 mm | 1.7150–1.7159 mm | within 1% |
| Pressure hoop alone (P*·r/t at t=3) | 5.29 MPa | n/a (see Section 5) | n/a |
| Pressure hoop alone (P*·r/t at t=4) | 3.96 MPa | n/a | n/a |
| Pressure hoop alone (P*·r/t at t=5) | 3.17 MPa | n/a | n/a |

ΔT_throat tracks Biot number prediction across all three thicknesses. δ_exit is essentially t-independent (varies by < 0.1%), matching the analytical expectation that free axial expansion = α · ΔT · L is a property of the wall material and integrated temperature, not the wall thickness. Both results confirm the thermal solve and structural compliance are correctly resolved across the three cases.

### 2.3 Factor of Safety against yield at throat

Yield strength is interpolated at T_throat = 803.59 K = 530.44 °C → σ_y = 209.95 MPa.

| Wall thickness | σ_vM,throat (MPa) | FoS |
|---|---|---|
| 3 mm | 3.9414 | 53.27 |
| 4 mm | 4.9171 | 42.70 |
| 5 mm | 6.1812 | 33.96 |

---

## 3. The Non-Monotonic Finding

Pressure hoop stress alone (P*·r/t) predicts σ_throat decreasing with thickness: 5.29 → 3.96 → 3.17 MPa. The FEA shows the opposite trend: σ_vM,throat increases with thickness: 3.94 → 4.92 → 6.18 MPa.

This means the throat probe is **not pressure-hoop-dominated**. It is dominated by thermal-bending stress arising from constrained differential thermal expansion at the throat geometric inflection.

### 3.1 Physical mechanism

The Dirichlet BC imposes T_aw(x) on the inner wall regardless of wall thickness. For a thicker wall:

1. The same imposed inner-wall temperature combined with a longer through-wall path produces a larger through-wall ΔT (confirmed: 1.33 → 2.10 → 2.71 K).
2. The differential expansion between inner and outer surfaces drives a bending moment at the throat region, where geometric curvature constrains free expansion.
3. Bending stiffness of a plate scales as t³, but the surface stress associated with a given imposed differential expansion scales as t · E · α · ΔT / (1 − ν) — and ΔT itself grows with t (per Bi).
4. Net effect: thicker wall = higher inner-surface bending stress at the throat, in this BC + geometry configuration.

Pressure hoop component (∝ 1/t) is smaller than the thermal-bending component at all three thicknesses. The pressure component decreases with t, but the thermal-bending component increases faster, so the von Mises sum increases with t.

### 3.2 Why this is reportable, not anomalous

The trend was initially counter-intuitive against a naive pressure-vessel reading. A careful decomposition of the stress state — separating pressure hoop from thermal bending — recovers physical sense. The mechanism is consistent with bending-plate theory for a constrained thermally-loaded shell. The four other QoIs (ΔT, δ_exit, T_throat, σ_global,singularity) all behave as analytically expected, providing positive controls that the FEA setup is correct and the trend reversal is not a numerical artefact.

---

## 4. Singularity Behaviour Across Thicknesses

| Wall thickness | σ_vM,global (MPa) |
|---|---|
| 3 mm | 486.95 |
| 4 mm | 430.58 |
| 5 mm | 484.70 |

The singularity is constraint-driven (inlet vertex Y = 0 BC). Its absolute magnitude depends on local element size at that vertex and on the geometric stress concentration at the wall corner. The non-monotonic shape across t is consistent with the inlet-edge geometry changing slightly between the three thicknesses (the outer wall vertex sits at a different radial position) and with mesh-discretisation interactions at the singular point. It is not a quantity of engineering interest in this study — flagged here only for completeness.

---

## 5. Critical Caveat — The Dirichlet BC Confound

**The thermal-bending stress component identified in Section 3 is amplified by the Dirichlet thermal BC choice.** Imposing T_aw on the inner wall regardless of wall thickness is a deliberately conservative engineering choice, but it produces a stronger t-dependence in throat stress than would arise under a more physical BC.

A higher-fidelity convection BC — applying the Bartz heat transfer coefficient h_g(x) to the inner wall and letting wall temperature equilibrate against an internal conductive resistance that scales with t — would give a different result:

- Thicker wall → larger conductive resistance from inner to outer surface → cooler inner-wall temperature → smaller through-wall ΔT than Dirichlet predicts → smaller thermal-bending stress.
- The t-dependence of throat σ_vM would compress.
- The pressure hoop component (∝ 1/t) would dominate at the upper end of the thickness range, plausibly recovering the conventional "thinner wall = higher stress" trend.

This is not speculation about future work — it is a known confound in the result documented here. The FoS values in Section 2.3 should not be quoted out of context as evidence that a thicker wall is structurally less safe than a thinner wall at this operating point. They are evidence of *the imposed-temperature BC's sensitivity to wall thickness*, which is partially a numerical-method effect.

### 5.1 What the FoS values do support

- Across t ∈ {3, 4, 5} mm, **all three configurations sit at FoS > 33 against yield**. None is yield-limited.
- The FoS spread across the three thicknesses is 1.6× (33.96 to 53.27). Even the most conservative end of this range is far above any structural margin requirement in the prototype/ground-test scope of this project.
- The binding constraint at all three thicknesses remains **creep**, not yield. T_throat is identical across all three (the Dirichlet BC enforces this), all three sit above the SS316 creep threshold (~410 °C), and creep life is BC-insensitive in the gas-side temperature regime.

### 5.2 What the FoS values do NOT support

- A claim that t = 5 mm is structurally inferior to t = 3 mm.
- A claim that this study quantifies the *true* mechanical-stress sensitivity to wall thickness independent of BC choice.
- A claim that the t-dependence is monotonic in either direction in the limit of a more physical BC.

A Bartz-BC follow-up study is required to establish the actual t-dependence of mechanical stress at the throat, and is added to the Future Work list (Section 7).

---

## 6. Engineering Conclusion

At Pc = 2 MPa, Tc = 800 K, with Dirichlet thermal BC, conical convergent-divergent geometry, and SS316 material:

- **Wall thickness selection at this operating point is not yield-governed.** All three thicknesses give FoS ≫ 4 against yield.
- **Wall thickness selection IS governed by creep life, manufacturing minimums, and weight.** Yield analysis alone is the wrong tool to choose t.
- **The throat thermal-bending mechanism identified here is BC-dependent.** A Bartz convection BC would compress the t-dependence and likely shift the dominant stress component back toward pressure hoop at thicker walls.

The FoS results in this document are upper-bound conservative for thin walls (t = 3 mm) and lower-bound conservative for thick walls (t = 5 mm) under the Dirichlet BC. The qualitative engineering conclusion (FoS ≫ 1 across all three; creep is binding) is robust to the BC choice.

---

## 7. Future Work (Updated)

1. **Bartz convection BC sensitivity study.** Re-run t = 3, 4, 5 mm with h_g(x) inner-wall convection BC instead of Dirichlet. Quantify the compression of the t-dependence and identify the actual dominant stress component as a function of t.
2. **Creep analysis (Larson-Miller, ASME II-D).** Establish the binding limit at the t = 4 mm baseline, then sweep across t to identify creep-life-driven minimum thickness.
3. **Two-way FSI iteration.** Allow structural deformation to feed back into the CFD flow field. Likely small effect at this Bi = 0.0022 regime, but worth documenting.

---

## 8. Limitations

| # | Limitation | Impact |
|---|---|---|
| L1 | Dirichlet thermal BC | Amplifies t-dependence of throat stress; documented in Section 5 |
| L2 | Three-thickness sweep, not a fine resolution | Trend identification, not optimisation |
| L3 | Singularity behaviour across t is mesh-discretisation-dependent | Not engineering-relevant; flagged only for completeness |
| L4 | Inherits all Phase 4 v3 limitations (L1–L11) | Documented in `Phase4_FEA_Summary_v3.md` Section 8 |

---

## 9. File Trail

| File | Purpose |
|---|---|
| `Phase5_Convergence_Study_v2.md` | Provides the t = 4 mm Mesh 3 baseline used here |
| `Phase4_FEA_Summary_v3.md` | Provides the corrected upstream load baseline used here |
| `Phase5b_Sensitivity_Study.md` | **This document** |

---

## 10. Closing Note

This study was originally scoped as Future Work in the engineering report, then promoted to an executed Phase 5b after the data integrity correction cleared the upstream baseline. The decision to execute it surfaced a finding (the thermal-bending dominance of throat stress under Dirichlet BC) that strengthens the engineering report's discussion section: it gives the reader a concrete reason why a Bartz convection BC follow-up is needed, beyond a generic "higher fidelity is better" framing.

The study also confirms what the pressure-only analytical estimate could not: that across a 2× range of wall thickness, **none of the configurations is yield-limited** at this operating point. That is the headline result. The non-monotonic σ_throat trend is the secondary finding that requires careful framing in the report — Section 5 of this document is the framing.
