# Phase 4 FEA — Setup, Conditions & Results Summary (v2 — Corrected Baseline)
**Project:** SS316 Nozzle Feasibility · Pc=2MPa · Tc=800K · Rt=15mm · ε=4 · t=4mm
**Date:** 2026-05-06 · **Updated:** 2026-05-07 (Phase 5 reconciliation) · **Solver:** ANSYS 2026 R1 Student · **Model:** 2D Axisymmetric

**Note:** This document is superseded by `Phase5_FEA_v3.md` as a result of a data integrity correction. The v2 baseline FEA was solved against a stale CFD wall temperature export that did not propagate downstream after CFD re-run. v2 numbers in this document remain accurate as a record of what was solved at that time; v3 contains corrected and updated values for FoS. **Do not quote v2 numbers in the engineering report or external deliverables.**


---

## 1. Workbench Schematic

| System | Role | Status |
|---|---|---|
| F — Geometry | 2D axisymmetric surface body (SpaceClaim) | ✓ Shared |
| G — Steady-State Thermal | Inner wall T_aw via Imported Load + outer convection | ✓ Solved |
| H — Static Structural | Imported pressure + imported body temperature + displacement | ✓ Solved |
| I — External Data — Temperature | Static temperature CSV from Fluent | ✓ Linked to G |
| J — External Data — Pressure | Static pressure CSV from Fluent | ✓ Linked to H |

**Architecture (NEW in v2):** External Data systems (I, J) are dragged into the schematic and linked via Workbench connections, rather than imported directly through Mechanical's Imported Load dialog. Column mappings, unit handling, and sign multipliers become persistent project state visible in the schematic.

**Links:**
- I Setup → G Setup (temperature → thermal)
- J Setup → H Setup (pressure → structural)
- G Solution → H Setup (nodal temperature transfer — pink link)
- F Geometry → G and H (shared)

---

## 2. Geometry

| Parameter | Value |
|---|---|
| Type | 2D surface body — wall cross-section |
| Wall thickness | 4 mm |
| Throat radius (inner) | 15 mm |
| Exit radius (inner) | ~30 mm |
| Nozzle length | ~190 mm |
| Orientation | Y = axial, X = radial (Mechanical axisymmetric convention) |
| Analysis type | 2D — Axisymmetric |

---

## 3. Material — SS316 (Temperature-Dependent)

Reference temperature for thermal expansion: **20 °C (293.15 K)**, set consistently across Engineering Data, Mechanical body, and Environment Temperature (clears v1 reference temperature warning).

**Thermal expansion α — densified to 7 points in v2** (was 4 in v1) to reduce interpolation error and reinforce the reference temperature warning fix:

| Temperature (°C) | 20 | 100 | 200 | 300 | 400 | 500 | 600 |
|---|---|---|---|---|---|---|---|
| α (×10⁻⁶/K) | 16.00 | 16.25 | 16.50 | 17.00 | 17.50 | 18.00 | 18.50 |

All other properties unchanged from v1 (4-point table):

| Property | 20°C | 200°C | 400°C | 600°C | Unit |
|---|---|---|---|---|---|
| Young's Modulus E | 200 | 186 | 172 | 152 | GPa |
| Yield Strength σ_y | 310 | 263 | 238 | 195 | MPa |
| UTS σ_u | 621 | 553 | 496 | 399 | MPa |
| Thermal Conductivity k | 14.0 | 16.0 | 18.6 | 21.5 | W/m·K |
| Density ρ | 7950 | 7880 | 7801 | 7713 | kg/m³ |
| Poisson's Ratio ν | 0.30 | 0.30 | 0.30 | 0.30 | — |

Sources: BS EN 10088-1, SSINA Tables 1 & 5, INCO Publication 2980. The 7-point α series is a linear interpolation between the original BS EN 10088-1 anchor values at 20 / 200 / 400 / 600 °C.

---

## 4. Mesh (Mesh 1 — Phase 5 Convergence Study Baseline)

License-compliant per ANSYS_Student_License_Limits.md. Re-meshed in Phase 5 for consistency with Mesh 2 and Mesh 3 (see Section 13).

| Setting | Value |
|---|---|
| Sheet Body Method (active) | Quadrilateral Dominant |
| Mesh Sizing | Medium |
| Edge Sizing (inner/outer wall) | 0.5 mm |
| Face Sizing (body) | 1.5 mm |
| Throat Sizing (inner/outer wall) | 0.3 mm |
| Edge Sizing (inlet/outlet thickness) | 4 divisions |
| Virtual Topology | Not applied |
| Smoothing | High |
| **Nodes** | **8,196** |
| **Elements** | **2,489** |
| **Combined** | **10,685** |
| Min Element Quality | 0.674 |
| Avg Element Quality | 0.933 |
| Std Deviation | 0.0432 |

**Note on the re-mesh:** The original Mesh 1 used Adaptive sizing with the global Prime Quad Dominant default (4,829 nodes / 1,338 elements / min quality 0.326). For the Phase 5 convergence study, all three meshes must use the same active mesher engine for the comparison to be valid. Mesh 1 was rebuilt with Quadrilateral Dominant Method (active, unsuppressed) and Medium global sizing to match Mesh 2 and Mesh 3. The local sizing values (0.5 / 1.5 / 0.3 / 4 divisions) were preserved — only the engine and global sizing setting changed. Node count and quality both improved as a side effect; the QoI values changed by < 1%, leaving the engineering conclusion unchanged. Original Adaptive baseline retained in commit history.

**Note on virtual topology:** Not applied. With re-meshed min quality at 0.674, the original Phase 4 v1 motivation for considering virtual topology (poor 0.326 quality) is no longer relevant.

---

## 5. Boundary Conditions

### 5.1 Steady-State Thermal (G)

| BC | Type | Scope | Value |
|---|---|---|---|
| Imported Temperature | Temperature | Inner wall (named selection: `inner_wall_section`) | 768.58–809 K (from CFD T_adiabatic-wall) |
| Convection | Convection | Outer wall | **h = 1×10⁻⁵ W/mm²·K (= 10 W/m²·K)**, T_∞ = 300 K |

**Critical correction:** v1 used `h = 10 W/mm²·K` = 10⁷ W/m²·K (6 orders of magnitude too high). Diagnosed via Biot number check, corrected to natural-convection value. See Section 10.

### 5.2 Static Structural (H)

| BC | Type | Scope | Value |
|---|---|---|---|
| Imported Pressure | Pressure | Inner wall (`inner_wall_section`) | −0.039–1.898 MPa |
| Imported Body Temperature | Thermal Condition | All Bodies | Nodal T from G Solution |
| Displacement | Displacement | Inlet thickness outer-wall vertex | Y = 0 (constrained); X = Free |

**Why the displacement BC is at a single vertex with Y=0, X=Free:** Static structural FEA requires every body to be kinematically determinate against rigid body motion. In 2D axisymmetric, the axisymmetric formulation eliminates radial drift around the symmetry axis, leaving only axial translation as a rigid body mode that must be manually constrained. Y=0 at the inlet vertex eliminates that mode without introducing artificial radial constraint — the wall remains free to thermally expand radially. The inlet vertex was chosen to keep the resulting constraint singularity as far as possible from the throat (the region of interest for the engineering question). The singularity is a known consequence and is empirically demonstrated as such in Phase 5 (Section 13).

---

## 6. CFD Handoff — Imported BC Distributions

| Location | T_aw | Static Pressure |
|---|---|---|
| Chamber (inlet) | ~800–803 K | ~1.898 MPa (Max) |
| Throat | **810 K (Max)** | ~1.06 MPa |
| Exit | ~768.58 K (Min) | ~0.06 MPa (−0.039 at wall edge — BC artefact) |

---

## 7. Imported Load Mapping — Verification (NEW in v2)

Spatial spot-check before solving — caught the v1 mirror error in Phase 4 attempt 1.

| Quantity | Location | CFD value | Mapped value | Match |
|---|---|---|---|---|
| Pressure | Chamber wall | ~1.9 MPa flat | Max = 1.898 MPa on chamber | ✓ |
| Pressure | Exit | ~0 to −0.04 MPa | Min = −0.039 MPa at exit | ✓ |
| Temperature | Throat | ~810 K | Max = 809 K at throat | ✓ |
| Temperature | Exit | ~768 K | Min = 768.58 K at exit | ✓ |

---

## 8. Results — Mesh 1 Corrected Baseline

### 8.1 Summary

| Quantity | Value | Location |
|---|---|---|
| **Throat von Mises (probe)** | **5.1924 MPa** | Throat inner wall vertex |
| Max von Mises (global) | 267.06 MPa | Inlet vertex — constraint singularity |
| Max total deformation | 1.7161 mm | Exit end (free end) |
| Max / Min thermal strain | 9.37×10⁻³ / 8.60×10⁻³ | Throat / Exit |
| T_throat | 804.38 K | Throat |
| Through-wall ΔT at throat | 2.12 K | 804.96 K (inner) → 802.84 K (outer) |

### 8.2 V1 → V2 Comparison

| Quantity | V1 (broken) | V2 (corrected) | Change |
|---|---|---|---|
| Through-wall ΔT at throat | 504 K | 2.12 K | −99.6% |
| Throat σ_vM | 1051 MPa | **5.19 MPa** | −99.5% |
| Global max σ_vM | 1702.9 MPa | 267.06 MPa | −84.3% |
| Max total deformation | 0.805 mm | 1.7161 mm | +113% |

### 8.3 Factor of Safety

Convert throat temperature from Kelvin to Celsius:

$$T_{throat,C} = T_{throat} - 273.15 = 804.38 - 273.15 = 531.23 \text{ °C}$$

Interpolate σ_y from Engineering Data:

$$\sigma_{y,531.23} = \sigma_{y,400} + (\sigma_{y,600} - \sigma_{y,400}) \times \frac{T_{throat,C} - 400}{600 - 400}$$

$$\sigma_{y,531.23°C} = 238 - (238-195) \times \frac{531.23-400}{600-400} = 209.79 \text{ MPa}$$

$$\text{FoS} = \frac{209.79}{5.1924} = \mathbf{40.4}$$

**SS316 does not yield at the throat under steady-state operation. ~40× margin against yield.** Mesh-converged FoS at Mesh 3 is 41.3 (see Section 13).

### 8.4 Pre-Solve Sanity Checks (Validation)

Both checks computed analytically before solving and verified against FEA result:

| Check | Analytical | FEA | Deviation |
|---|---|---|---|
| Through-wall ΔT (Bi = h·t/k = 0.0022 ≪ 0.1, expect ~1–2 K) | ~1 K | 2.12 K | within range |
| Free axial expansion (α·ΔT·L = 17.5×10⁻⁶ × 511 × 190 mm) | 1.70 mm | 1.7161 mm | 0.9% |

### 8.5 Stress Decomposition — Throat (corrected physics)

With wall near-isothermal (Bi = 0.0022):

| Component | Magnitude | Notes |
|---|---|---|
| Pressure hoop stress (Pc·r/t at throat) | ~7.5 MPa | Dominant |
| Through-wall thermal gradient | ~quasi-zero | Wall is thermally lumped |
| Axial pressure end-cap | ~3.75 MPa | Minor |
| Differential axial expansion (~40 K over 190 mm) | <5 MPa | Minor |

Pressure hoop is now the dominant stress contributor — chamber-wall band shows 21.2 MPa = Pc · 42.4 mm / 4 mm, consistent with Pc·r/t hoop calc.

---

## 9. Engineering Conclusion

Under steady-state operation (Pc = 2 MPa, Tc = 800 K, uncooled, natural convection):

1. **SS316 does not fail by yield.** Throat σ_vM ≈ 5 MPa vs σ_y(531°C) ≈ 210 MPa, FoS ≈ 40 at Mesh 1, **41.3 at converged Mesh 3** (see Section 13).
2. **Wall is essentially isothermal at T_aw** (Bi = 0.0022). Uncooled SS316 in still air cannot dissipate heat fast enough to develop a meaningful through-wall gradient at steady state.
3. **Active design constraint shifts from yield to creep.** Wall sits at ~800 K = 531 °C, above the SS316 creep threshold of ~410 °C (= 0.4·T_melt). Time-dependent creep, not yield, is the limiting failure mode for sustained operation.
4. **Bulk axial thermal expansion** is 1.72 mm over 190 mm. Affects joint/mount/seal design but is not itself a structural failure.
5. **Project framing answer:** Uncooled SS316 is **viable for short-duration prototype/ground-test firings** at this operating point on yield grounds. For sustained operation, creep analysis (Larson-Miller, ASME II-D allowable stresses) is required and recommended as future work. Aligns with IJIRSET 2019 SS316 thruster precedent (prototype) and ArianeGroup's use of Haynes 25 for flight-qualified hardware (where creep + cycle life dominate).
6. **Mesh independence demonstrated in Phase 5.** The FoS conclusion is not mesh-dependent — see Section 13.

---

## 10. Changelog v1 → v2

Three independent BC errors corrected, plus supporting fixes. Each row: symptom → root cause → fix → verification.

### 10.1 Critical fixes

| # | Issue | Symptom | Root cause | Fix | Verification |
|---|---|---|---|---|---|
| C1 | Convection BC units | Through-wall ΔT = 504 K, throat σ_vM = 1051 MPa, FoS = 0.20 | Active unit system uses W/mm²·K for film coefficient. Entered `10` evaluated to 10⁷ W/m²·K — 6 orders too high | Replaced `10` with `1×10⁻⁵` W/mm²·K (= 10 W/m²·K) | Bi = 0.0022 → predicted ΔT ~1–2 K. FEA result: 2.12 K ✓ |
| C2 | BC spatial mirror | Imported pressure showed Max at exit, Min at chamber — opposite of CFD | CFD axial coordinate sign opposite to FEA Y convention. Direct mapping placed chamber values on exit nodes | Applied **−1 multiplier on Y coordinate** column in External Data Properties for both files | Spatial spot-check: chamber red, exit blue on pressure ✓ |
| C3 | Temperature column mapping | Temperature CSV imported but all columns read "Not Used" — no data bound to FEA mesh | Column type assignments not bound during initial External Data setup | Assigned columns to Node Number, X Coordinate, Y Coordinate, Temperature | Imported temperature visible on inner wall in Mechanical tree ✓ |

### 10.2 Supporting fixes

| # | Issue | Fix |
|---|---|---|
| S1 | CSV header row triggering "invalid data line 1" warning | Set "Start Import at Line" = 2 in External Data |
| S2 | Coordinate values in metres but column type set to mm | Either changed column type to (m), or applied ×1000 multiplier |
| S3 | Reference temperature mismatch (Engineering Data 20 °C vs Mechanical default 22 °C) | Set all three locations (Engineering Data α reference / body Ref T / Environment T) to 20 °C |
| S4 | Stale `external_load_data.xml` cache after BC edits | Re-read Data Files → Update External Data → Refresh downstream → re-import loads |
| S5 | Sparse α data (4 points, 20/200/400/600 °C) flagged in reference-temperature warning | Densified α to 7 points (20/100/200/300/400/500/600 °C) by linear interpolation along the BS EN 10088-1 trend. Reduces internal interpolation error; reinforces S3 fix |

### 10.3 Architecture improvements

| # | Change | Benefit |
|---|---|---|
| A1 | External Data systems linked via Workbench connections (vs direct Mechanical import) | Column mappings, units, sign multipliers visible in schematic and persistent across project reopens |
| A2 | Mandatory pre-solve BC verification gate added (Section 12.2) | Order-of-magnitude analytical checks before each solve catch BC errors before they propagate |

---

## 11. Known Limitations

| Limitation | Impact | Mitigation |
|---|---|---|
| Inlet vertex constraint singularity | Global max σ_vM (267 MPa at Mesh 1, diverges with refinement) is non-physical | Use throat probe (5.19 MPa); Phase 5 confirmed divergence empirically — see Section 13 |
| Outer wall h = 10 W/m²·K | Conservative — assumes still air | Real test stand may have additional convection from exhaust plume |
| Adiabatic wall CFD → T_aw | Neglects wall conduction in CFD | Bi = 0.0022 confirms wall conduction would not change gas-side T_aw — standard one-way FSI is appropriate |
| Negative pressure at exit edge (−0.039 MPa) | Negligible — 2% of peak pressure | Numerical BC artefact, not bulk flow error |
| 2D axisymmetric — no 3D effects | Ignores asymmetric loads | Valid for axisymmetric geometry; license-driven decision |
| **No creep model** | Wall above SS316 creep threshold (~410 °C) | **Active scope boundary.** FoS = 40 against yield is not the binding limit. Creep flagged as required future work |
| One-way FSI only | No structural deformation feedback into CFD | Standard for preliminary analysis |

---

## 12. Phase 5 — Mesh Convergence Plan (superseded)

Phase 5 is **complete**. The original plan in this section has been superseded by the executed study documented in `Phase5_Convergence_Study.md`. Section 13 below summarises the outcome.

### 12.1 Mandatory Pre-Solve BC Verification Gate (retained)

Added in response to v1 BC failures. Applied before each Phase 5 solve:

1. Imported Loads spatially spot-checked (chamber red, exit blue on pressure; throat hot, exit cold on temperature)
2. Convection BC value AND units re-confirmed in details panel
3. Reference temperatures consistent across Engineering Data / body / environment (all 20 °C)
4. Order-of-magnitude analytical estimates computed:
   - Biot number → expected through-wall ΔT
   - α·ΔT·L → expected free thermal expansion
   - Pc·r/t → expected hoop stress
5. Post-solve: results compared against pre-solve estimates. Any deviation > 2× triggers root-cause investigation before proceeding.

---

## 13. Phase 5 Convergence Study — Outcome Summary

Full details in `Phase5_Convergence_Study.md`. Reproduced here for cross-reference.

### 13.1 Three-mesh study

| Metric | Mesh 1 | Mesh 2 | Mesh 3 |
|---|---|---|---|
| Combined nodes + elements | 10,685 | 16,527 | 21,565 |
| Min element quality | 0.674 | 0.619 | 0.632 |
| Linear refinement ratio | — | 1.24 | 1.14 |

All three meshes used identical method (Quadrilateral Dominant), identical global sizing (Medium), and identical BCs. Only local element sizing varied between meshes.

### 13.2 QoI convergence results

| QoI | Mesh 1 | Mesh 2 | Mesh 3 | M1→M2 | M2→M3 | Verdict |
|---|---|---|---|---|---|---|
| σ_vM,throat (MPa) | 5.1924 | 5.0321 | 5.0773 | −3.09% | +0.89% | ✓ Converged |
| T_throat (K) | 804.38 | 804.38 | 804.38 | 0% | 0% | ✓ Converged |
| ΔT_throat (K) | 2.12 | 2.11 | 2.10 | −0.47% | −0.47% | ✓ Converged |
| δ_exit (mm) | 1.7161 | 1.7161 | 1.7163 | 0% | +0.012% | ✓ Converged |
| σ_vM,global (MPa) | 267.06 | 352.61 | 430.57 | +32.03% | +22.11% | ✓ Diverges (singularity confirmed) |

### 13.3 Mesh-converged FoS

At Mesh 3:

$$\text{FoS}_{converged} = \frac{\sigma_{y,531°C}}{\sigma_{vM,throat,M3}} = \frac{209.78}{5.0773} = 41.3$$

Within 2% of the Mesh 1 baseline (40.4), confirming mesh independence. The σ_vM,global divergence empirically validates excluding the constraint singularity from the FoS calculation.

---
