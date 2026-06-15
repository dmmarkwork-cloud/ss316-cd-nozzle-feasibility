# Phase 5 Convergence Study
**Project:** SS316 Nozzle Feasibility · Pc=2MPa · Tc=800K · Rt=15mm · ε=4 · t=4mm
**Date:** 2026-05-07 · **Solver:** ANSYS 2026 R1 Student · **Model:** 2D Axisymmetric

**Note:** This document is superseded by `Phase5_Convergence_Study_v2`. The convergence study methodoloy, mesh design, and probe strategy are correct and re-used in v2. The QoI values and FoS calculation were computed agains the stale upstream CFD temperature data; the corrected values are in v2. `Use v2 numbers in the engineering report`.

---

## 1. Methodology

### 1.1 Study type

Simple three-mesh trend study. Not formal Grid Convergence Index (GCI) per Celik 2008. The data collected is sufficient to compute GCI as post-processing if required, with the caveat that the linear refinement ratios (1.24 between M1→M2, 1.14 between M2→M3) are tighter than the r ≥ 1.3 typically recommended for Richardson extrapolation. Stated as a limitation in the report rather than treated as a flaw.

### 1.2 Controlled variables (identical across all three meshes)

| Setting | Value |
|---|---|
| Mesh Sizing | Medium |
| Method (active) | Quadrilateral Dominant |
| Element Order | Quadratic |
| Free Face Mesh Type | Quad/Tri |
| Smoothing | High |
| Boundary conditions | Imported pressure and imported temperature from CFD, h = 1×10⁻⁵ W/mm²·K convection, Y = 0 (constrained) and X = free vertex displacement |
| Reference temperature | 20 °C across Engineering Data, body, and environment |

The only variable changing between meshes is element size, applied through local sizing controls.

### 1.3 Probe strategy

All QoI sampled at **vertex-scoped named selections**, not node IDs. Vertex scoping ensures the same physical location is sampled across all three meshes; node IDs would shift between mesh generations and invalidate the comparison. Through-wall ΔT uses a Construction Geometry Path between two coplanar points (same Y, X separated by wall thickness), not two separate point probes — the inner and outer wall vertices are not at the same axial position due to the parallel wall offset, so direct point-probe subtraction would be sampling different axial stations.

---

## 2. Mesh Statistics

| Metric | Mesh 1 | Mesh 2 | Mesh 3 |
|---|---|---|---|
| Body sizing | 1.5 mm | 1.1 mm | 0.90 mm |
| Wall edge sizing | 0.5 mm | 0.36 mm | 0.30 mm |
| Throat curve sizing | 0.3 mm | 0.21 mm | 0.18 mm |
| Thickness divisions | 4 | 6 | 7 |
| Nodes | 8,196 | 12,609 | 16,413 |
| Elements | 2,489 | 3,918 | 5,152 |
| **Combined** | **10,685** | **16,527** | **21,565** |
| Min element quality | 0.674 | 0.619 | 0.632 |
| Avg element quality | 0.933 | 0.919 | 0.921 |
| Std deviation | 0.0432 | 0.0488 | 0.0491 |
| Element types | Tri6 + Quad8 | Tri6 + Quad8 | Tri6 + Quad8 |

### 2.1 Refinement ratios

$$r_{12} = \sqrt{\frac{16527}{10685}} = 1.24$$

$$r_{23} = \sqrt{\frac{21565}{16527}} = 1.14$$


### 2.2 Quality stability across the study

Min element quality stays in the 0.62–0.67 band across all three meshes, with average quality essentially flat at 0.92–0.93. Stable mesh quality across refinement levels means any change in QoI is attributable to element size, not to the mesher producing degraded elements at finer sizings — a necessary precondition for a valid convergence study.

---

## 3. Quantities of Interest

| # | Quantity | Symbol | Probe location | Expected behaviour |
|---|---|---|---|---|
| 1 | Throat inner wall σ_vM | σ_vM,throat | `probe_throat_inner` vertex | Asymptotic — primary metric |
| 2 | Throat inner wall T | T_throat | `probe_throat_inner` vertex | Asymptotic — validates thermal field |
| 3 | Through-wall ΔT at throat | ΔT_throat | `path_throat_throughwall` (T at 0 mm − T at ≈ 4 mm) | Asymptotic — drives gradient stress |
| 4 | Max total deformation at exit | δ_exit | `probe_exit_corner` vertex | Asymptotic — global compliance |
| 5 | Global max σ_vM | σ_vM,global | Whole-model maximum | **Diverges** — singularity confirmation |

---

## 4. Results

### 4.1 Raw QoI values

| QoI | Mesh 1 | Mesh 2 | Mesh 3 | Units |
|---|---|---|---|---|
| σ_vM,throat | 5.1924 | 5.0321 | 5.0773 | MPa |
| T_throat | 804.38 | 804.38 | 804.38 | K |
| ΔT_throat | 2.12 | 2.11 | 2.10 | K |
| δ_exit | 1.7161 | 1.7161 | 1.7163 | mm |
| σ_vM,global | 267.06 | 352.61 | 430.57 | MPa |

### 4.2 Percentage change between meshes

Each step's percentage change is normalised to the previous mesh (not always to Mesh 1):

$$\text{pc}_{12} = \frac{X_{M2} - X_{M1}}{X_{M1}} \times 100 \quad ; \quad \text{pc}_{23} = \frac{X_{M3} - X_{M2}}{X_{M2}} \times 100$$

| QoI | M1→M2 | M2→M3 | Convergence criterion (< 5%) |
|---|---|---|---|
| σ_vM,throat | −3.09% | +0.89% | ✓ Converged |
| T_throat | 0% | 0% | ✓ Converged |
| ΔT_throat | −0.47% | −0.47% | ✓ Converged |
| δ_exit | 0% | +0.012% | ✓ Converged |
| σ_vM,global | +32.03% | +22.11% | ✓ Diverges (expected) |

### 4.3 Interpretation

Four QoIs show clean convergence. σ_vM,throat oscillates within a ±0.16 MPa band around ~5.07 MPa — this is mesh discretisation noise, not a trend, and the magnitude is engineering-irrelevant given the FoS margin established in Section 5. T_throat is identical to two decimal places across all three meshes, confirming the thermal field is fully resolved at coarse-mesh resolution. ΔT_throat decreases monotonically by 0.01 K per refinement step, converging toward the analytical estimate of ~1–2 K from Bi = 0.0022. δ_exit shows mesh-independent free thermal expansion at 1.716 mm, matching the analytical α·ΔT·L estimate to within 1%.

The fifth QoI, σ_vM,global, climbs from 267 → 353 → 431 MPa across the three meshes — a +32% then +22% jump. This is the expected behaviour of a constraint singularity at the inlet vertex where the Y=0 displacement BC is applied. Each refinement level resolves more of the singular field, driving the local stress higher without converging. The divergence is the positive control for the study: it confirms the mesher is correctly resolving stress gradients (otherwise the singularity wouldn't appear at all), and empirically justifies excluding the global max from the FoS calculation in favour of the throat probe.

---

## 5. Factor of Safety at Converged Mesh 3

### 5.1 Yield strength interpolation

SS316 yield strength data (SSINA Table 1 / Nickel Institute brochure 9004):

$$\sigma_y(400°C) = 238 \text{ MPa} \quad ; \quad \sigma_y(600°C) = 195 \text{ MPa}$$

Throat temperature in converting from Kelving to Celsius:

$$T_{throat,C} = T_{throat,M3} - 273.15 = 804.38 - 273.15 = 531.23 \text{ °C}$$

Linear interpolation:

$$\sigma_{y,throat} = \sigma_{y,400} + (\sigma_{y,600} - \sigma_{y,400}) \times \frac{T_{throat,C} - 400}{600 - 400}$$

$$\sigma_{y,throat} = 238 + (195 - 238) \times \frac{531.23 - 400}{200} = 238 - 43 \times 0.6562 = 209.78 \text{ MPa}$$

### 5.2 Factor of Safety

$$\text{FoS} = \frac{\sigma_{y,throat}}{\sigma_{vM,throat,M3}} = \frac{209.78}{5.0773} = 41.32$$

---

## 6. Engineering Conclusion

With mesh independence demonstrated for σ_vM,throat, T_throat, ΔT_throat, and δ_exit, and with σ_vM,global confirmed as a constraint singularity rather than a real stress, the Phase 4 conclusion is supported by Phase 5 results:

- Throat von Mises stress: **5.08 ± 0.08 MPa** (mesh-independent)
- Throat temperature: **804.38 K (531.2 °C)** (mesh-independent)
- Through-wall ΔT: **2.10 K** (matches analytical Bi-based estimate)
- Exit thermal expansion: **1.716 mm** (matches α·ΔT·L estimate within 1%)
- **Factor of safety against yield at throat: 41.3**

Under steady-state operation at Pc = 2 MPa, Tc = 800 K, with natural convection on the outer wall, **uncooled SS316 is not yield-limited at the throat**. The active failure mode shifts to creep, since the wall sits at 531 °C, above the SS316 creep threshold of approximately 410 °C (= 0.4 × T_melt). Time-dependent creep analysis (Larson-Miller, ASME II-D allowable stresses) is required to establish the binding limit for sustained operation, and is correctly scoped as future work.

This conclusion is consistent with the IJIRSET 2019 SS316 thruster precedent (prototype hardware) and with ArianeGroup's use of Haynes 25 for flight-qualified hardware (where creep and cycle life dominate). SS316 is viable for short-duration prototype or ground-test firings at this operating point on yield grounds.

---

## 7. Limitations

| Limitation | Impact |
|---|---|
| Linear refinement ratios (1.24, 1.14) below typical GCI threshold (1.3) | Prevents formal Richardson extrapolation; trend study only |
| Three meshes is the minimum for asymptotic trend confirmation | More meshes would tighten uncertainty bounds but are constrained by the 32k license cap on the upper end |
| σ_vM,global divergence is not formally extrapolated to mesh-converged limit | Acceptable — global max is a singularity, not a quantity of engineering interest |
| Constraint singularity at inlet vertex is geometric, not physical | Real mounting hardware (flange, weld, clamp) would distribute the load across a finite area and produce a finite, lower stress |
| No creep model | Wall above SS316 creep threshold; FoS of 41 against yield is not the binding limit for sustained operation |

---

## 8. Files Generated

- `phase5_convergence.ipynb` — Jupyter handcalcs notebook with all calculations and plots
- `phase5_convergence.pdf` — exported PDF (File → Save and Export Notebook As → PDF_NoInput)
- Three plots: σ_throat dual-panel (mesh independence + distance from yield), ΔT_throat convergence, σ_global divergence (log scale)