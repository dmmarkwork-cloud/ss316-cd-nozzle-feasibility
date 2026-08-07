# Phase 4 FEA: Setup, Conditions and Results Summary (v2, Corrected Baseline)
**Project:** SS316 Nozzle Feasibility · Pc=2MPa · Tc=800K · Rt=15mm · ε=4 · t=4mm
**Date:** 2026-05-06 · **Updated:** 2026-05-07 (Phase 5 reconciliation) · **Solver:** ANSYS 2026 R1 Student · **Model:** 2D Axisymmetric

Supersedes Phase4_FEA_Summary.md. Three independent BC errors in v1 were identified and corrected; see Section 10. Mesh and result values were updated post-Phase 5 for consistency with the convergence study baseline; see Section 13.

---

## 1. Workbench Schematic

| System | Role | Status |
|---|---|---|
| F: Geometry | 2D axisymmetric surface body (SpaceClaim) | ✓ Shared |
| G: Steady-State Thermal | Inner wall T_aw via Imported Load + outer convection | ✓ Solved |
| H: Static Structural | Imported pressure + imported body temperature + displacement | ✓ Solved |
| I: External Data, Temperature | Static temperature CSV from Fluent | ✓ Linked to G |
| J: External Data, Pressure | Static pressure CSV from Fluent | ✓ Linked to H |

**Architecture (NEW in v2):** External Data systems (I, J) are dragged into the schematic and linked via Workbench connections, rather than imported directly through Mechanical's Imported Load dialog. Column mappings, unit handling, and sign multipliers become persistent project state visible in the schematic.

**Links:**
- I Setup → G Setup (temperature → thermal)
- J Setup → H Setup (pressure → structural)
- G Solution → H Setup (nodal temperature transfer, pink link)
- F Geometry → G and H (shared)

---

## 2. Geometry

| Parameter | Value |
|---|---|
| Type | 2D surface body, wall cross-section |
| Wall thickness | 4 mm |
| Throat radius (inner) | 15 mm |
| Exit radius (inner) | ~30 mm |
| Nozzle length | 183.44 mm |
| Orientation | Y = axial, X = radial (Mechanical axisymmetric convention) |
| Analysis type | 2D Axisymmetric |

---

## 3. Material: SS316 (Temperature-Dependent)

Reference temperature for thermal expansion: **20 °C (293.15 K)**, set consistently across Engineering Data, Mechanical body, and Environment Temperature (clears v1 reference temperature warning).

**Thermal expansion α, densified to 7 points in v2** (was 4 in v1) to reduce interpolation error and reinforce the reference temperature warning fix:

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
| Poisson's Ratio ν | 0.30 | 0.30 | 0.30 | 0.30 | n/a |

Sources: BS EN 10088-1, SSINA Tables 1 & 5, INCO Publication 2980. The 7-point α series is a linear interpolation between the original BS EN 10088-1 anchor values at 20 / 200 / 400 / 600 °C.

---

## 4. Mesh (Mesh 1: Phase 5 Convergence Study Baseline)

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

**Note on the re-mesh:** The original Mesh 1 used Adaptive sizing with the global Prime Quad Dominant default (4,829 nodes / 1,338 elements / min quality 0.326). For the Phase 5 convergence study, all three meshes must use the same active mesher engine for the comparison to be valid. Mesh 1 was rebuilt with Quadrilateral Dominant Method (active, unsuppressed) and Medium global sizing to match Mesh 2 and Mesh 3. The local sizing values (0.5 / 1.5 / 0.3 / 4 divisions) were preserved; only the engine and global sizing setting changed. Node count and quality both improved as a side effect; the QoI values changed by < 1%, leaving the engineering conclusion unchanged. Original Adaptive baseline retained in commit history.

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

**Why the displacement BC is at a single vertex with Y=0, X=Free:** Static structural FEA requires every body to be kinematically determinate against rigid body motion. In 2D axisymmetric, the axisymmetric formulation eliminates radial drift around the symmetry axis, leaving only axial translation as a rigid body mode that must be manually constrained. Y=0 at the inlet vertex eliminates that mode without introducing artificial radial constraint: the wall remains free to thermally expand radially. The inlet vertex was chosen to keep the resulting constraint singularity as far as possible from the throat (the region of interest for the engineering question). The singularity is a known consequence and is empirically demonstrated as such in Phase 5 (Section 13).

---

## 6. CFD Handoff: Imported BC Distributions

| Location | T_aw | Static Pressure |
|---|---|---|
| Chamber (inlet) | ~800–803 K | ~1.898 MPa (Max) |
| Throat | **810 K (Max)** | ~1.06 MPa |
| Exit | ~768.58 K (Min) | ~0.06 MPa (−0.039 at wall edge; BC artefact) |

---

## 7. Imported Load Mapping: Verification (NEW in v2)

Spatial spot-check before solving; caught the v1 mirror error in Phase 4 attempt 1.

| Quantity | Location | CFD value | Mapped value | Match |
|---|---|---|---|---|
| Pressure | Chamber wall | ~1.9 MPa flat | Max = 1.898 MPa on chamber | ✓ |
| Pressure | Exit | ~0 to −0.04 MPa | Min = −0.039 MPa at exit | ✓ |
| Temperature | Throat | ~810 K | Max = 809 K at throat | ✓ |
| Temperature | Exit | ~768 K | Min = 768.58 K at exit | ✓ |

---

## 8. Results: Mesh 1 Corrected Baseline

### 8.1 Summary

| Quantity | Value | Location |
|---|---|---|
| **Throat von Mises (probe)** | **5.1924 MPa** | Throat inner wall vertex |
| Max von Mises (global) | 267.06 MPa | Inlet vertex; constraint singularity |
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
| Through-wall ΔT (small because outer-wall film resistance dominates heat path; expect ~1–2 K) | ~1 K | 2.12 K | within range |
| Free axial expansion (α·ΔT·L = 17.1×10⁻⁶ × 511 × 183.44 mm) | 1.60 mm | 1.7161 mm | 6.6% |

Notes on the inputs:
- **L = 183.44 mm** is the actual nozzle length (corrected from the earlier 190 mm placeholder).
- **α = 17.1×10⁻⁶ /K** is the *mean* thermal expansion coefficient between the 20 °C reference and the ~531 °C wall temperature, not the value at any single temperature. This is the correct quantity for free expansion over a temperature rise, since the wall expands across the whole range it heats through. (For reference, the table value at 400 °C is 17.5 and at 531 °C is ~18.16; the mean over the range is lower because it includes the cooler near-reference behaviour.)
- The ~6.6% deviation is expected for an order-of-magnitude gate. The analytical estimate assumes uniform free expansion of a straight bar, while the FEA includes the curved wall profile and the small differential expansion along the nozzle. The estimate lands at the right magnitude, which is its purpose.

### 8.5 Stress Decomposition: Throat (corrected physics)

Dominant component resolved by separating the contributors at t = 4 mm and cross-checking against the Phase 5b wall-thickness sweep (see note below):

| Component | Magnitude | Notes |
|---|---|---|
| Through-wall thermal-bending (E·α·ΔT / [2(1−ν)], ΔT ≈ 2.1 K) | ~4.3–4.8 MPa | **Dominant** |
| Pressure hoop stress (P*·r/t at throat) | ~3.96 MPa | Secondary |
| Axial pressure end-cap | ~3.75 MPa | Minor |
| Differential axial expansion (~40 K over 183.44 mm) | <5 MPa | Minor |

**Throat stress is thermal-bending-dominated, not pressure-hoop-dominated.** This is established by the Phase 5b thickness sweep: FEA throat σ_vM *rises* with wall thickness (3.94 → 4.92 → 6.18 MPa across t = 3/4/5 mm), the opposite of the pressure-hoop trend (P*·r/t = 5.29 → 3.96 → 3.17 MPa, ∝ 1/t). A rising trend can only come from the thermal-bending term, whose driver ΔT grows with t. The hand-calc agrees: thermal-bending ≈ 4.3 MPa exceeds pressure hoop 3.96 MPa at t = 4 mm, and the two combine to the FEA total von Mises of 4.92 MPa (Mesh 3) / 5.19 MPa (Mesh 1). The earlier "~7.5 MPa pressure-hoop, dominant" entry was wrong on both counts: 7.5 MPa exceeds the FEA total (impossible for a single component), and the correct hoop value is 3.96 MPa.

For contrast, the *chamber* band (not the throat) is pressure-hoop-dominated: it shows ~21.2 MPa = P_c · 42.4 mm / 4 mm, consistent with the P·r/t hoop calc at the larger chamber radius and near-zero local ΔT. The dominant mechanism differs by location: hoop in the chamber, thermal-bending at the throat.

---

## 9. Engineering Conclusion

Under steady-state operation (Pc = 2 MPa, Tc = 800 K, uncooled, natural convection):

1. **SS316 does not fail by yield.** Throat σ_vM ≈ 5 MPa vs σ_y(531°C) ≈ 210 MPa, FoS ≈ 40 at Mesh 1, **41.3 at converged Mesh 3** (see Section 13).
2. **Wall is essentially isothermal at T_aw.** The outer wall is modelled with a low natural-convection coefficient (10 W/m²·K), so it sheds almost no heat; the through-wall heat flux is therefore tiny and only a small gradient (~2 K) develops. Uncooled SS316 in still air cannot dissipate heat fast enough to develop a meaningful through-wall gradient at steady state.
3. **Active design constraint shifts from yield to creep.** Wall sits at ~800 K = 531 °C, above the SS316 creep threshold of ~410 °C (= 0.4·T_melt). Time-dependent creep, not yield, is the limiting failure mode for sustained operation.
4. **Bulk axial thermal expansion** is 1.72 mm over 183.44 mm. Affects joint/mount/seal design but is not itself a structural failure.
5. **Project framing answer:** Uncooled SS316 is **viable for short-duration prototype/ground-test firings** at this operating point on yield grounds. For sustained operation, creep analysis (Larson-Miller, ASME II-D allowable stresses) is required and recommended as future work. Aligns with IJIRSET 2019 SS316 thruster precedent (prototype) and ArianeGroup's use of Haynes 25 for flight-qualified hardware (where creep + cycle life dominate).
6. **Mesh independence demonstrated in Phase 5.** The FoS conclusion is not mesh-dependent; see Section 13.

---

## 10. Changelog v1 → v2

Three independent BC errors corrected, plus supporting fixes. Each row: symptom → root cause → fix → verification.

### 10.1 Critical fixes

| # | Issue | Symptom | Root cause | Fix | Verification |
|---|---|---|---|---|---|
| C1 | Convection BC units | Through-wall ΔT = 504 K, throat σ_vM = 1051 MPa, FoS = 0.20 | Active unit system uses W/mm²·K for film coefficient. Entered `10` evaluated to 10⁷ W/m²·K, 6 orders too high | Replaced `10` with `1×10⁻⁵` W/mm²·K (= 10 W/m²·K) | Bi = 0.0022 → predicted ΔT ~1–2 K. FEA result: 2.12 K ✓ |
| C2 | BC spatial mirror | Imported pressure showed Max at exit, Min at chamber, opposite of CFD | CFD axial coordinate sign opposite to FEA Y convention. Direct mapping placed chamber values on exit nodes | Applied **−1 multiplier on Y coordinate** column in External Data Properties for both files | Spatial spot-check: chamber red, exit blue on pressure ✓ |
| C3 | Temperature column mapping | Temperature CSV imported but all columns read "Not Used"; no data bound to FEA mesh | Column type assignments not bound during initial External Data setup | Assigned columns to Node Number, X Coordinate, Y Coordinate, Temperature | Imported temperature visible on inner wall in Mechanical tree ✓ |

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
| Inlet vertex constraint singularity | Global max σ_vM (267 MPa at Mesh 1, diverges with refinement) is non-physical | Use throat probe (5.19 MPa); Phase 5 confirmed divergence empirically (see Section 13) |
| Outer wall h = 10 W/m²·K | Conservative; assumes still air | Real test stand may have additional convection from exhaust plume |
| Adiabatic wall CFD → T_aw | Neglects wall conduction in CFD | The outer wall is near-adiabatic (h = 10 W/m²·K), so through-wall heat flux is small and gas-side T_aw is not significantly affected by neglecting conjugate heat transfer, so standard one-way FSI is appropriate. (Note: a gas-side Biot number using the Bartz coefficient is ≈ 0.6, not negligible; the justification rests on the low outer-wall heat flux, not on a lumped wall.) |
| Negative pressure at exit edge (−0.039 MPa) | Negligible; 2% of peak pressure | Numerical BC artefact, not bulk flow error |
| 2D axisymmetric, no 3D effects | Ignores asymmetric loads | Valid for axisymmetric geometry; license-driven decision |
| **No creep model** | Wall above SS316 creep threshold (~410 °C) | **Active scope boundary.** FoS = 40 against yield is not the binding limit. Creep flagged as required future work |
| One-way FSI only | No structural deformation feedback into CFD | Standard for preliminary analysis |

---

## 12. File Trail

| File | Purpose |
|---|---|
| Phase4_FEA_Summary.md | Original v1; broken solve (3 BC errors) |
| Phase4_FEA_Summary_v2.md | This document; corrected v2 baseline + Phase 5 reconciliation |
| Phase5_Convergence_Study.md | Standalone Phase 5 deliverable |
| phase5_convergence.ipynb | Jupyter handcalcs notebook with calculations and plots |
| phase5_convergence.pdf | Exported notebook PDF for portfolio submission |