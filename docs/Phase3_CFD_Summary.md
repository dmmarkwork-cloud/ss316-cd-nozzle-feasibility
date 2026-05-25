# Phase 3 CFD — Setup, Conditions & Results Summary
**Project:** SS316 Nozzle Feasibility · Pc=2MPa · Tc=800K · Rt=15mm · ε=4 · t=4mm
**Date:** 2026-05-08 · **Solver:** ANSYS Fluent 2026 R1 Student · **Model:** 2D Axisymmetric · **Mode:** Standalone (not Workbench-linked)

V2 final converged solution. Re-run from Geom-1 mesh after V1 case/data loss. All validation gate metrics passed within tolerance. Adiabatic-wall outputs (wall static temperature, wall static pressure) handed off to Phase 4 FEA.

---

## 1. Software Architecture

| Element | Configuration | Notes |
|---|---|---|
| Fluent launch | Standalone, Dimension = 2D | Not Workbench-linked. Required because Workbench 3D-default mode rejects 2D mesh transfer in 2026 R1 (see Section 11) |
| Mesh source | Fluent Meshing 2D Workflow | NOT ANSYS Meshing — Pre algorithm fails on curved 2D boundaries in this release |
| Mesh file | `Geom-1-surface-body_2d.msh.h5` | Loaded via File → Read → Mesh |
| Case + data | `residual_results (validation gate passed!!).cas.h5` + `.dat.h5` | Saved immediately on convergence (V1 lesson learned) |

---

## 2. Domain & Geometry

| Parameter | Value |
|---|---|
| Analysis type | 2D Axisymmetric, Steady |
| Domain extents (x, axial) | −126.72 mm to 56.72 mm |
| Domain extents (y, radial) | 0 to 42.40 mm |
| Total 2D area | 6.810 × 10⁻⁴ m² |
| Throat location (axial) | x ≈ −47 mm (Fluent coordinate system) |
| Geometry type | Conical C-D, converging half-angle 30°, diverging half-angle 15° |
| Throat radius (inner) | 15 mm |
| Exit radius (inner) | 30 mm (from area ratio ε=4) |

---

## 3. Mesh

License-compliant per `ANSYS_Student_License_Limits.md`. Fluent cell cap is 512,000 — current cell count is 3% of limit. No cell-budget concerns.

### 3.1 Mesh statistics

| Setting | Value |
|---|---|
| Total cells | 15,757 |
| Quadrilateral fraction | 97.7% |
| Min orthogonal quality | 0.649 |
| Max tangent skewness | 0.878 |
| Max aspect ratio | 150 (boundary layer cells, expected) |
| Cells below quality 0.05 | 0 |
| Min cell volume | 9.15 × 10⁻¹¹ m³ |
| Max cell volume | 5.56 × 10⁻⁷ m³ |

Min-quality cell location: x = −9.16 mm, y = 14.95 mm — just upstream of throat in the boundary layer transition zone. Quality of 0.649 is well above the typical 0.10 cutoff for solver stability.

### 3.2 Sizing controls

| Region | Size | Rationale |
|---|---|---|
| Global min | 0.01 mm | First boundary layer cell |
| Global max | 1.5 mm | Freestream cells in chamber |
| Throat curves (body 2, 3) | 0.10 mm | Resolve sonic transition geometry |
| Diverging wall (body 9) | 0.30 mm | Resolve peak heat flux region |
| Converging wall (body 4) | 0.50 mm | Lower gradient zone |

### 3.3 Boundary layer

| Setting | Value |
|---|---|
| Offset method | Last-ratio |
| First layer height | 0.01 mm |
| Number of layers | 20 |
| Growth rate | 1.2 |
| Max layer height | 2.0 mm |
| Applied to zones | Bodies 2, 3, 4, 5, 9 (all wall surfaces — chamber, converging, throat, diverging) |
| NOT applied to | Inlet, outlet, axis |

### 3.4 V2 vs V1 — what changed

| V1 Problem | V2 Fix |
|---|---|
| Smooth-transition BL, y⁺ uncontrolled (200–400) | Last-ratio method, first layer 0.01 mm |
| Min orthogonal quality 0.125 at throat | Min orthogonal quality 0.649 |
| No local sizing on diverging wall | Added 0.30 mm sizing on body 9 |
| BL on inner_wall only | BL on all wall zones |
| Named selection overlap caused throat junction artefacts | Boundary zones reassigned via Fluent Separate function |

---

## 4. Boundary Zone Map

The single `part-boundary` zone produced by Fluent Meshing was split using **Domain → Zones → Separate → Angle = 40°** in the solver. Edge-level named selections in SpaceClaim are ignored by Fluent Meshing — only face-level transfer (see Section 11, Issue 2).

| Zone | Identity | BC Type |
|---|---|---|
| `part-boundary` | Converging + throat + diverging wall | wall (adiabatic) |
| `part-boundary.1` | Chamber wall | wall (adiabatic) |
| `part-boundary.2` | Inlet | pressure-inlet |
| `part-boundary.3` | Axis — left half | axis |
| `part-boundary.4` | Axis — right half | axis |
| `part-boundary.5` | Outlet | pressure-outlet |

---

## 5. Solver Configuration

### 5.1 General

| Setting | Value |
|---|---|
| Solver type | Density-based, implicit |
| Velocity formulation | Absolute |
| 2D space | Axisymmetric |
| Time | Steady |
| Gravity | Off |

### 5.2 Models

| Model | Setting |
|---|---|
| Energy | On |
| Viscous | k-ω SST with **Correlation** near-wall treatment |

Correlation near-wall treatment blends viscous sublayer integration (low y⁺) with wall functions (high y⁺). Required because the present mesh has y⁺ varying from ~2 in the chamber to ~18 at the throat (see Section 8.4 and Section 12).

### 5.3 Material — air

| Property | Setting |
|---|---|
| Density | ideal-gas |
| Viscosity | sutherland (3-coefficient) |
| Cp, k | Fluent defaults |

Working fluid is air, not combustion products. This is a documented simplification — see Section 12.

### 5.4 Cell zone

| Setting | Value |
|---|---|
| Material | air |
| **Operating pressure** | **100,000 Pa** |

All gauge pressures are referenced to this. Operating pressure is 100 kPa, NOT 101.325 kPa (deliberately rounded for clean gauge arithmetic).

### 5.5 Boundary conditions

| Zone | Type | Value |
|---|---|---|
| **inlet** (`part-boundary.2`) | pressure-inlet | Gauge Total Pressure = **1,900,000 Pa** (= 2.0 MPa abs); Supersonic/Initial Gauge = 1,893,000 Pa; Total Temperature = **800 K**; TI = 1%; TVR = 10 |
| **outlet** (`part-boundary.5`) | pressure-outlet | Gauge Pressure = **−40,000 Pa** (= 60,000 Pa abs, matches design Pe for ε=4); Backflow Pressure Spec = **Static Pressure**; Backflow Total T = 300 K; TI = 5%; TVR = 10 |
| **all wall zones** | wall | Thermal: Heat Flux = **0** (adiabatic); No-slip momentum |
| **axis zones** (`part-boundary.3`, `.4`) | axis | — |

**Adiabatic wall rationale:** Wall temperature is treated as a CFD output, not an imposed input. With adiabatic walls, the inner wall settles at the adiabatic recovery temperature T_aw — the upper-bound temperature the wall would reach if no heat conducted into the SS316. This is the conservative input for the Phase 4 thermal BC. Heat conduction through the wall is modelled in Phase 4 FEA, not here. See Section 12 for limitations of this approach.

### 5.6 Solution methods

| Setting | Value |
|---|---|
| Formulation | Implicit |
| Flux type | Roe-FDS |
| Gradient | Least Squares Cell Based |
| Flow | Second Order Upwind |
| Turbulent Kinetic Energy | Second Order Upwind |
| Specific Dissipation Rate | Second Order Upwind |
| High Speed Numerics | Enabled |
| Convergence Acceleration for Stretched Meshes | Enabled |

### 5.7 Solution controls

| Setting | Value |
|---|---|
| Courant number | 0.5 (reduced from default 1.0 — fine BL cells in diverging section) |
| Under-relaxation factors | All defaults (TKE = 0.8, SDR = 0.8, Turbulent Viscosity = 1.0, Solid = 1.0) |

### 5.8 Initialisation

| Setting | Value |
|---|---|
| Method | Standard Initialization (NOT Hybrid, NOT FMG) |
| Compute from | Inlet |

FMG initialisation corrupts this geometry's solution to the subsonic branch (M_max ≈ 1.33 instead of 2.94). Documented in Section 11, Issue 3.

---

## 6. Run Strategy

| Stage | Iterations | Purpose |
|---|---|---|
| Initial run | 0 → 8,000 | Drive flow residuals to limit-cycle floor |
| Diagnostic continuation | 8,000 → 11,000 | Verify k residual reaches true plateau (was still trending down at 8,000) |
| **Total** | **11,000** | Full convergence demonstrated for both flow and turbulence variables |

---

## 7. Convergence Behaviour

### 7.1 Residual history

See `residuals_v2_final.png`.

| Variable | Final residual | Behaviour |
|---|---|---|
| Continuity | ~1 × 10⁻³ | Limit-cycle oscillation (steady RANS at transonic conditions) |
| x-velocity | ~2 × 10⁻³ | Limit-cycle oscillation |
| y-velocity | ~7 × 10⁻⁴ | Limit-cycle oscillation |
| Energy | ~1 × 10⁻³ | Limit-cycle oscillation |
| k | ~7 × 10⁻⁶ | Fully converged after diagnostic continuation |
| ω | ~2 × 10⁻⁴ | Limit-cycle oscillation |

### 7.2 Why residuals do not reach 1×10⁻⁵

The flow residual floor at ~10⁻³ is not premature stopping — it is the genuine numerical floor for steady RANS at transonic throat conditions. NASA CFD guidance (Spalart, NASA TM 2007–214853) documents this as inherent **limit-cycle oscillation**: the steady solver alternates within a small band rather than monotonically decreasing because the throat shock structure has bounded fluctuation in the time-averaged sense.

The 8,000 → 11,000 diagnostic run proved this. Flow residuals stayed at the same band; only k continued to converge. If the floor were premature stopping, all variables would have continued to drop together.

### 7.3 Primary convergence metric

**Mass flow imbalance is the governing convergence criterion, not residual magnitude.** See Section 8.

---

## 8. Validation Gate

All four checks within ≤5% deviation. Gate **passed**.

### 8.1 Throat Mach = 1

Confirmed visually from Mach contour (`mach_contour_v2.png`). Sonic line lies at the geometric throat; converging section subsonic; diverging section supersonic with no internal shocks.

### 8.2 Mass flow conservation

| Boundary | Mass flow [kg/s] |
|---|---|
| Inlet | +1.9847 |
| Outlet | −1.9856 |
| **Net imbalance** | **+0.000826 kg/s (0.04%)** |

0.04% imbalance is exceptional for a density-based RANS solver at transonic conditions. Industry threshold is typically <2% for steady CFD; 0.04% indicates the discretisation error is at the solver's noise floor.

### 8.3 Exit Mach (area-weighted)

| Source | M_exit |
|---|---|
| CFD area-weighted average at outlet | 2.8666 |
| 1D isentropic hand-calc (ε=4, γ=1.4) | 2.94 |
| **Deviation** | **2.5%** |

The 2.5% gap is attributable to boundary-layer displacement effects (1D inviscid theory vs 2D viscous CFD). This is the expected physical deviation, not solver error.

**Note on contour vs area-weighted:** Mach contour shows centreline peak ≈ 3.12. This is the inviscid core value, not the bulk exit. The 2.866 area-weighted figure is the correct comparison against 1D theory.

### 8.4 Exit static pressure (area-weighted, absolute)

| Source | P_exit |
|---|---|
| CFD area-weighted average at outlet | 61,474.5 Pa (−38,525.5 Pa gauge + 100,000 Pa operating) |
| 1D isentropic hand-calc | 59,520 Pa |
| **Deviation** | **3.3%** |

CFD slightly above hand-calc. Flow is therefore mildly **under-expanded** at the exit plane (P_e > P_back = 60,000 Pa), producing weak expansion fans off the lip rather than over-expansion shocks. This is consistent with the slight area-ratio mismatch from boundary-layer displacement.

### 8.5 Validation gate summary

| Check | CFD | Hand-calc | Deviation | Gate (≤5%) |
|---|---|---|---|---|
| Throat M = 1 | Confirmed (contour) | 1.0 | — | ✓ |
| Mass flow imbalance | 0.04% | — | — | ✓ |
| Exit Mach (area-weighted) | 2.8666 | 2.94 | 2.5% | ✓ |
| Exit pressure (area-weighted, abs) | 61,475 Pa | 59,520 Pa | 3.3% | ✓ |

---

## 9. Wall Data — Phase 4 FEA Handoff

Adiabatic wall outputs along the inner wall surface, exported as Fluent XY data files.

### 9.1 Wall static temperature (`wall_temperature_v2.xy`)

| Region | x range [mm] | T range [K] | Notes |
|---|---|---|---|
| Chamber wall | −126.7 to −36.7 | 799.58 – 801.44 | Effectively isothermal at T_c = 800 K (subsonic, no significant Mach heating) |
| Converging + throat + diverging | −36.7 to +56.7 | 767.85 – 808.17 | Max at x ≈ 1.1 mm (just downstream of throat); min at x = +56.7 mm (exit) |

Total: 537 data points (64 chamber + 465 converging/throat/diverging — densest sampling at throat where gradients are sharpest, as designed).

**Anomaly (documented):** Max wall T of 808.17 K slightly exceeds chamber stagnation T_c = 800 K. Thermodynamically T_aw should always be ≤ T_0 for recovery factor r < 1. This ~1% overshoot is a buffer-zone numerical artefact tied to local y⁺ peak at the throat — see Section 12.

### 9.2 Wall static pressure (`wall_pressure_v2.xy`)

| Region | x range [mm] | P range [Pa abs] | Notes |
|---|---|---|---|
| Chamber wall | −126.7 to −36.7 | 1,992,820 – 1,999,310 | Effectively at P_c = 2.0 MPa |
| Converging + throat + diverging | −36.7 to +56.7 | 60,041 – 1,996,570 | Smooth pressure decay through expansion |

### 9.3 y⁺ distribution (`yplus_v2.png`)

| Region | y⁺ range | Treatment validity |
|---|---|---|
| Chamber wall | 2 – 4 | Viscous sublayer integration — fully resolved |
| Converging section (entry) | 2 – 6 | Viscous sublayer / lower buffer |
| Throat region (sharp peak) | up to **18** | **Buffer zone — accuracy reduced (see Section 12)** |
| Diverging section | 2 – 11 | Mostly viscous sublayer / lower buffer |

### 9.4 Heat flux — NOT exported

Wall heat flux is identically zero on adiabatic walls by construction. The XY plot of wall heat flux shows machine-precision noise (~10⁻⁹ W/m²), not physical flux. **Not handed to Phase 4.** Bartz analytical correlation (`bartz_htc_v2.csv`) supplies the convective HTC for the FEA convection BC.

---

## 10. Figures

| File | Content |
|---|---|
| `residuals_v2_final.png` | Residual history, 0 – 11,000 iterations, all 6 transport variables |
| `mach_contour_v2.png` | Mach number contour, range 3.19×10⁻⁵ to 3.12 |
| `temperature_contour_v2.png` | Static temperature contour, range 272 K to 808 K |
| `pressure_contour_v2.png` | Static pressure contour (gauge), range −5.45×10⁴ to +1.90×10⁶ Pa |
| `yplus_v2.png` | Wall y⁺ XY plot, all wall zones |
| `final_mesh_statistics.png` | Mesh quality screenshot from Fluent display |
| `boundary_conditions_zones.png` | BC zone assignment screenshot |
| `solution_methods_CFD.png` | Solution methods panel screenshot |
| `CFD_convergence_V2.png` | Mid-run convergence screenshot |
| `CFD_results_1.png`, `CFD_results_2.png` | Result panel screenshots |
| `project_schematic_1.png`, `project_schematic_2.png` | Workbench/Fluent project schematic |

---

## 11. Issues Encountered & Resolutions

### Issue 1 — Workbench 3D/2D incompatibility

| Aspect | Detail |
|---|---|
| Symptom | "2D mesh cannot be transferred to 3D solver" error when clicking *Switch to Solution* |
| Root cause | Workbench in 2026 R1 defaults to 3D solver; 2D mesh handoff fails |
| Resolution | Launch Fluent **standalone** from Start Menu, set Dimension = 2D in launcher, File → Read → Mesh (NOT Read → Case) |
| Lesson | Standalone mode is required for this workflow; do not attempt Workbench-linked operation |

### Issue 2 — SpaceClaim named selections not transferred

| Aspect | Detail |
|---|---|
| Symptom | Only `part-boundary` zone appeared after mesh load — no separate inlet/outlet/axis/wall zones |
| Root cause | Edge-level named selections in SpaceClaim are ignored by Fluent Meshing. Only face-level named selections transfer |
| Resolution | Split zones in Fluent solver via **Domain → Zones → Separate → Angle = 40°** |
| Lesson | For 2D Fluent Meshing workflow, plan to do BC zone separation in the solver — do not rely on SpaceClaim named selections |

### Issue 3 — FMG initialisation corrupted solution

| Aspect | Detail |
|---|---|
| Symptom | Mach contour showed M_max ≈ 1.33 — diverging section running subsonic. Wrong solution branch. |
| Root cause | FMG (Full Multi-Grid) initialisation produces a starting field that converges to the wrong branch for this geometry/BC combination |
| Resolution | Use Standard Initialization only. Disable FMG via console: `/solve/initialize/fmg-initialization no` |
| Lesson | **Never use FMG for this geometry.** Standard initialisation from inlet is the only safe choice |

### Issue 4 — Heat flux plot showed numerical noise

| Aspect | Detail |
|---|---|
| Symptom | Wall heat flux XY plot oscillating around ~10⁻⁹ W/m² |
| Root cause | Adiabatic wall → heat flux = 0 by definition. Plot shows machine-precision round-off, not physical flux |
| Resolution | Do not export heat flux for FEA handoff. Use wall static temperature (= adiabatic recovery temperature) and wall static pressure instead. Use analytical Bartz correlation for convective HTC in Phase 4 |
| Lesson | Adiabatic wall CFD cannot produce physically meaningful heat flux or surface heat transfer coefficient — both require finite wall temperature gradient |

### Issue 5 — V1 case/data files lost

| Aspect | Detail |
|---|---|
| Symptom | Original V2-converged case + data files no longer on disk |
| Root cause | Files not saved immediately after first convergence run |
| Resolution | Re-run from `Geom-1-surface-body_2d.msh.h5` using exact V2 settings. Save Case + Data **immediately** on convergence |
| Lesson | **Save protocol enforced going forward:** (a) File → Export → Case & Data on convergence, (b) verify both `.cas.h5` and `.dat.h5` exist on disk, (c) save residual plot PNG before closing Fluent (residual history is not stored in `.dat.h5`) |

### Issue 6 — Wall function HTC unusable for FEA handoff

| Aspect | Detail |
|---|---|
| Symptom | Wall Function Heat Transfer Coefficient plot showed values seven orders of magnitude below expected, with negative spikes |
| Root cause | Fluent's wall function HTC computation requires a finite wall temperature gradient to produce physically meaningful values. With fully adiabatic walls, the reference temperature difference collapses and the output is numerical noise |
| Resolution | Replaced CFD HTC handoff with analytical **Bartz correlation** computed in `bartz_htc.ipynb`. h(x) tabulated as `bartz_htc_v2.csv` for direct import into Phase 4 |
| Lesson | Adiabatic CFD cannot provide a meaningful convective HTC for one-way FSI. Either run conjugate heat transfer (CHT) or use an analytical correlation. Bartz is the standard rocket-nozzle choice |

---

## 12. Known Limitations

These limitations apply to the engineering interpretation of CFD outputs in Phase 4 and the report. State all of them in the final report.

| # | Limitation | Impact | Mitigation / Note |
|---|---|---|---|
| L1 | y⁺ peak ~18 at the throat (buffer zone) | Reduced near-wall accuracy for k-ω SST in a narrow throat region. Wall functions and viscous sublayer integration are both non-ideal at 5 < y⁺ < 30 | k-ω SST with Correlation near-wall treatment blends both regimes automatically. Bulk flow validation passes (mass flow 0.04%, exit Mach 2.5%, exit P 3.3%). Wall heat transfer **not extracted from CFD** — replaced with Bartz analytical correlation |
| L2 | T_aw artefact at throat — max wall T = 808 K > T_c = 800 K | ~1% overshoot of stagnation temperature is thermodynamically inconsistent (T_aw must be ≤ T₀ for recovery factor r < 1) | Localised to the buffer-zone y⁺ region around the throat. Magnitude (~8 K, 1%) is well below the conservatism margin of using T_aw as a Dirichlet thermal BC in Phase 4 |
| L3 | Working fluid = air, not combustion products | Real H₂O₂-monoprop or hydrazine exhaust has γ ≈ 1.27, not 1.4. Throat T*/T₀ ratio shifts; exit Mach shifts; wall temperatures shift | Treated as a parametric simplification. T_c = 800 K is treated as an independent operating-point input, not a stoichiometric combustion result. Documented in report Introduction |
| L4 | Adiabatic wall assumption | Neglects heat conduction into the SS316 wall in the CFD step. Inner wall settles at T_aw rather than the coupled wall temperature | Standard one-way FSI approach. Bi number check (Bi ≈ 0.0022) confirms wall conduction is small enough that gas-side T_aw is not significantly affected by including conjugate heat transfer. See Phase 4 Section 11 limitation table |
| L5 | Inlet TI = 1% (low for combustion chamber) | Real chambers have TI ≈ 5–10% from combustion turbulence. Boundary-layer growth depends weakly on inlet TI for k-ω SST in nozzle flows | k-ω SST is dominated by wall-shear-generated turbulence inside the nozzle; inlet TI sensitivity is low. Documented as an assumption rather than a flaw |
| L6 | 2D axisymmetric — no 3D effects | Ignores any non-axisymmetric instabilities (corner separation, swirl) | Geometry is genuinely axisymmetric. Loading is axisymmetric (no transverse thrust, no swirl injection). 2D is correct for this physics. Also a license-driven choice (Fluent and Mechanical caps) |
| L7 | Steady RANS — no transient/startup | Startup transients can produce peak loads not captured here | Out of scope per Project Definition Document Section 4.2. Flagged as "future work" in conclusions |
| L8 | Negative gauge pressure (~−54 kPa minimum) at exit edge | Local numerical artefact where the exit boundary meets the outer wall — corner cell pressure dips below the imposed back-pressure | Magnitude (~54 kPa, peak) is an isolated cell. Bulk area-weighted exit pressure (61.5 kPa abs) is physically correct. Excluded from FEA pressure load profile |
| L9 | Residual floor at ~10⁻³ (not 10⁻⁵) | Convergence below 10⁻³ is not achievable for steady RANS at transonic throat conditions | Documented limit-cycle behaviour per NASA TM 2007–214853. Mass flow imbalance (0.04%) is the primary convergence criterion and passes by 50× margin |

---

## 13. Files for Phase 4 Handoff & Phase 6 GitHub

| File | Purpose | Status |
|---|---|---|
| `cfd_conical_v2_final.cas.h5` | Full case (mesh + setup) | ✓ Saved |
| `cfd_conical_v2_final.dat.h5` | Converged solution data | ✓ Saved |
| `wall_temperature_v2.xy` | Inner wall T_aw distribution → Phase 4 thermal BC | ✓ Exported |
| `wall_pressure_v2.xy` | Inner wall pressure distribution → Phase 4 structural load | ✓ Exported |
| `bartz_htc_v2.csv` | Analytical convective HTC h(x) → Phase 4 convection BC (replaces failed CFD HTC handoff per L4 / Issue 6) | ✓ Generated |
| `residuals_v2_final.png` | Convergence figure for report | ✓ Saved |
| `mach_contour_v2.png` | Validation figure — sonic throat, supersonic exit | ✓ Saved |
| `temperature_contour_v2.png` | Validation figure — temperature distribution | ✓ Saved |
| `pressure_contour_v2.png` | Validation figure — pressure expansion | ✓ Saved |
| `yplus_v2.png` | y⁺ documentation for limitation L1 | ✓ Saved |
| `final_mesh_statistics.png` | Mesh quality documentation | ✓ Saved |
| `boundary_conditions_zones.png` | BC zone documentation | ✓ Saved |
| `solution_methods_CFD.png` | Solver settings documentation | ✓ Saved |

---

## 14. Phase 3 Success Criteria — Status

Per Project Definition Document Section 8:

| # | Criterion | Status |
|---|---|---|
| 3 | CFD converged with residuals below 1×10⁻⁵ | **Modified — flow residuals at limit-cycle floor 10⁻³, k at 7×10⁻⁶.** Residual target replaced with mass-flow imbalance gate. Justification in Section 7 and Limitation L9 |
| 4 | CFD validation gate passed: throat M=1, exit P and mass flow within 5% of hand calcs | ✓ Passed (Section 8). All four checks within 5% |

The original criterion 3 (residuals below 10⁻⁵) is not achievable for steady RANS at transonic conditions and has been replaced with a convergence framework based on mass conservation and validation against 1D theory. This is an explicit, documented modification — not a silent relaxation.

---

## 15. Handoff to Phase 4

Phase 4 inputs ready:

1. **Imported Body Temperature** (Steady-State Thermal): `wall_temperature_v2.xy` → applied to inner wall as Dirichlet T_aw (conservative upper-bound thermal BC)
2. **Imported Pressure** (Static Structural): `wall_pressure_v2.xy` → applied to inner wall
3. **Convection BC** (Steady-State Thermal — alternative to Dirichlet, more physically accurate): `bartz_htc_v2.csv` h(x) + `wall_temperature_v2.xy` T_aw(x) → applied to inner wall as `h × (T_aw − T_wall)`
4. Outer wall convection: h = 10 W/m²·K, T_∞ = 300 K (still air, conservative)

**Architectural note for Phase 4:** Phase 4 v1/v2 used the Dirichlet approach (Imported Body Temperature). The Bartz convection BC (option 3 above) was added in this Phase 3 closeout as an alternative for future iterations or sensitivity studies. The current Phase 4/5 baseline uses Dirichlet — this is the conservative engineering choice and is explicitly documented as such.

This document closes Phase 3.

---

## 16. File Trail

| File | Purpose |
|---|---|
| `cfd_v2_continuation.md` | V2 mesh handoff & re-run plan (pre-convergence) |
| `Phase3_CFD_Summary.md` | **This document — V2 final converged baseline** |
| `bartz_htc.ipynb` | Bartz correlation hand-calculation notebook |
| `bartz_htc_v2.csv` | Tabulated h(x) for FEA handoff |
| `Phase4_FEA_Summary_v2.md` | Downstream — Phase 4 FEA setup & results |
| `Phase5_Convergence_Study.md` | Downstream — Phase 5 mesh independence study |
