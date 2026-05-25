# Phase 5 Convergence Study (v2 — Corrected Upstream Loads)
**Project:** SS316 Nozzle Feasibility · Pc=2MPa · Tc=800K · Rt=15mm · ε=4 · t=4mm
**Date:** 2026-05-10 · **Solver:** ANSYS 2026 R1 Student · **Model:** 2D Axisymmetric

Supersedes `Phase5_Convergence_Study.md`. The original Phase 5 was solved against a stale CFD wall temperature export. All three meshes have been re-run with the corrected External Data link. Methodology, mesh statistics, and probe strategy are unchanged from the v1 study; only the solved values change.

---

## 1. What Changed from v1

| Item | v1 (original) | v2 (corrected) |
|---|---|---|
| CFD wall temperature source | stale export (805.72 K at exit edge) | current re-run state (767.85 K at exit edge) |
| External Data freshness check | not performed | performed before each solve |
| Methodology | three-mesh trend study | unchanged |
| Mesh statistics (M1, M2, M3) | unchanged | unchanged |
| Probe strategy (vertex-scoped named selections) | unchanged | unchanged |
| Controlled variables | unchanged | unchanged |

Mesh statistics and methodology are documented in `Phase5_Convergence_Study.md` Sections 1–3 and are not repeated here.

---

## 2. Corrected QoI Results

### 2.1 Raw values

| QoI | Mesh 1 | Mesh 2 | Mesh 3 | Units |
|---|---|---|---|---|
| σ_vM,throat | 5.0308 | 4.8725 | 4.9171 | MPa |
| T_throat | 804.38 | 803.59 | 803.59 | K |
| ΔT_throat | 2.12 | 2.10 | 2.10 | K |
| δ_exit | 1.7148 | 1.7149 | 1.7150 | mm |
| σ_vM,global | 267.06 | 352.62 | 430.58 | MPa |

### 2.2 Percentage change between meshes

| QoI | M1→M2 | M2→M3 | Convergence (< 5%) |
|---|---|---|---|
| σ_vM,throat | −3.15% | +0.92% | ✓ Converged |
| T_throat | −0.10% | 0% | ✓ Converged |
| ΔT_throat | −0.94% | 0% | ✓ Converged |
| δ_exit | +0.006% | +0.006% | ✓ Converged |
| σ_vM,global | +32.04% | +22.10% | ✓ Diverges (singularity confirmed) |

### 2.3 Comparison against v1

| QoI | v1 Mesh 3 | v2 Mesh 3 | Δ |
|---|---|---|---|
| σ_vM,throat | 5.0773 MPa | 4.9171 MPa | −3.16% |
| T_throat | 804.38 K | 803.59 K | −0.79 K |
| ΔT_throat | 2.10 K | 2.10 K | unchanged |
| δ_exit | 1.7163 mm | 1.7150 mm | −0.08% |
| σ_vM,global | 430.57 MPa | 430.58 MPa | <0.01% |

The σ_vM,throat shift is systematic across all three meshes (~3.1% in the same direction), confirming the change is driven by the corrected thermal load rather than mesh-dependent solver noise. Singularity result (σ_vM,global) is unchanged because the singularity is constraint-driven, not thermally driven.

---

## 3. Convergence Verdict

Mesh independence demonstrated for all four engineering QoIs. The σ_vM,throat M2 → M3 step is +0.92%, well within the < 5% gate. T_throat, ΔT_throat, and δ_exit are mesh-independent to within solver noise. σ_vM,global continues to diverge as expected for a constraint singularity.

The convergence pattern is qualitatively identical to v1. The data integrity correction shifted absolute values but not the convergence character.

---

## 4. Updated Factor of Safety

### 4.1 Yield strength interpolation

T_throat at converged Mesh 3 = 803.59 K = 530.44 °C.

$$\sigma_y(530.44°C) = 238 + (195 - 238) \times \frac{530.44 - 400}{600 - 400} = 238 - 43 \times 0.6522 = 209.95 \text{ MPa}$$

(v1 value: 209.78 MPa at 531.23 °C. The 0.79 K shift in T_throat moved σ_y by 0.17 MPa.)

### 4.2 Factor of Safety

$$\text{FoS} = \frac{\sigma_{y,throat}}{\sigma_{vM,throat,M3}} = \frac{209.95}{4.9171} = 42.70$$

(v1 FoS = 41.32.)

### 4.3 Mesh sensitivity of FoS

Computing FoS at each mesh against the same σ_y:

| Mesh | σ_vM,throat (MPa) | FoS |
|---|---|---|
| Mesh 1 | 5.0308 | 41.73 |
| Mesh 2 | 4.8725 | 43.09 |
| Mesh 3 | 4.9171 | 42.70 |

FoS spread across the three meshes is 1.4 (3.3%), comparable to v1's 1.3 (3.2%). Mesh independence of the FoS conclusion confirmed.

---

## 5. Engineering Conclusion (Unchanged from v1)

With mesh independence demonstrated, the corrected results give:

- Throat von Mises stress: **4.92 ± 0.10 MPa** (mesh-independent)
- Throat temperature: **803.59 K (530.4 °C)**
- Through-wall ΔT: **2.10 K** (matches Bi-based analytical estimate)
- Exit thermal expansion: **1.7150 mm** (matches α·ΔT·L within 1%)
- **Factor of safety against yield at throat: 42.7**

Uncooled SS316 is not yield-limited at the throat. The active failure mode is creep, since the wall sits at 530 °C, above the SS316 creep threshold of approximately 410 °C. Time-dependent creep analysis is required to establish the binding limit and is correctly scoped as future work.

The 3% downward shift in σ_vM,throat from v1 is an artefact of correcting the stale upstream temperature data, not a change in physical understanding. For a FoS of 42, ~1 K of wall-temperature noise is engineering-irrelevant. This is a useful sanity check on the v1 conclusion: the FoS conclusion was robust enough to survive a 3% upstream data correction.

---

## 6. Limitations (Unchanged from v1)

| Limitation | Impact |
|---|---|
| Linear refinement ratios (1.24, 1.14) below typical GCI threshold (1.3) | Prevents formal Richardson extrapolation; trend study only |
| Three meshes is the minimum for asymptotic trend confirmation | Constrained by 32k license cap on the upper end |
| σ_vM,global divergence is not formally extrapolated | Acceptable — global max is a singularity, not engineering-relevant |
| Constraint singularity at inlet vertex | Real mounting hardware would distribute load and produce a finite, lower stress |
| No creep model | Wall above SS316 creep threshold; FoS of 42 against yield is not the binding limit |

Phase 4 v3 limitation L11 (Imported Load freshness — single-node CFD export variability) added at the project level but does not change the within-study convergence conclusion of this document.

---

## 7. Files Generated

| File | Purpose |
|---|---|
| `Phase5_Convergence_Study.md` | Original v1 — solved against stale upstream temperature |
| `Phase5_Convergence_Study_v2.md` | **This document — re-run with corrected loads** |
| `phase5_convergence.ipynb` | Jupyter handcalcs notebook (FoS interpolation values updated to v2) |
| `phase5_convergence.pdf` | Exported PDF (regenerate with v2 numbers before report submission) |

---

## 8. Closing Note

The convergence study itself was correctly designed and executed in v1. The error was not in the methodology, the mesh design, the probe strategy, or the convergence interpretation — all of those carry through unchanged. The error was in trusting that the upstream External Data link was current. v2 documents what changes when that assumption is verified rather than assumed.

This is consistent with the v1 → v2 progression of Phase 4 (where the BC setup was correct in form but wrong in unit/sign). The pattern across both phases: methodology has been consistently sound; setup hygiene has been the recurring failure mode. The v3 pre-solve gate (Phase 4 v3 Section 3) addresses this systemically going forward.
