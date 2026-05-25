# Phase 4 FEA — Setup, Conditions & Results Summary (v3 — Data Integrity Correction)
**Project:** SS316 Nozzle Feasibility · Pc=2MPa · Tc=800K · Rt=15mm · ε=4 · t=4mm
**Date:** 2026-05-10 · **Solver:** ANSYS 2026 R1 Student · **Model:** 2D Axisymmetric

Supersedes `Phase4_FEA_Summary_v2.md`. The v2 baseline FEA was solved against a stale CFD wall temperature export that remained in the External Data system after a CFD case re-run (Phase 3 Issue 5 lineage). The downstream Mechanical solve never received the updated upstream data because the External Data → Steady-State Thermal stream was not pushed after the source-file radio button was switched. This document records the diagnosis, the corrected solve, and the resulting QoI shifts. Engineering conclusions are unchanged.


---

## 1. Trigger — How the Stale Data Was Caught

During the Phase 5b sensitivity study setup at t = 3 mm, the Imported Temperature in Mechanical showed a Min source value of **790.29 K** instead of the v2 baseline-recorded 768.58 K. Cross-checking the Fluent CSV directly revealed only one node — at the exit edge (X = +56.72 mm) — differed between the two source files (805.72 K vs 767.85 K). The remaining 526 of 528 nodes were byte-identical.

The 38 K difference at the single edge node was sufficient to shift the mapped temperature field across the FEA mesh enough to change the throat probe stress by ~3%. The bulk wall temperature mean shift was 0.80 K with 1.84 K standard deviation across all nodes — small in absolute terms, but systematic and traceable to a defined upstream data event.

---

## 2. Root Cause

| Step | What happened |
|---|---|
| 1 | Original Phase 3 v2 CFD case + data was saved, validated, and exported (`wall_temperature_v2.xy`). |
| 2 | Case file was lost before Phase 4 began (Phase 3 Issue 5). CFD was re-run from the v2 mesh to reproduce the converged state. |
| 3 | Re-run produced a slightly different exit-edge node value (767.85 K vs the lost 805.72 K reference). All other nodes matched within solver noise (< 0.2 K). |
| 4 | Phase 4 v2 External Data system was set up. The CSV file was placed in the External Data location, but the source-file radio button selection in Workbench retained the earlier (pre-re-run) export path. |
| 5 | The "Update Stream Components" command was not invoked after the radio button toggle. Mechanical kept solving against the cached pre-re-run data through Phase 4 v2 baseline solve and all three Phase 5 mesh studies. |
| 6 | Phase 5b sensitivity setup forced a fresh External Data link, exposing the discrepancy in the Imported Temperature legend. |

---

## 3. Architectural Lesson — Pre-Solve Gate Update

The Phase 4 v2 pre-solve verification gate (Section 12.2 of the v2 document) checked imported load *spatial distribution* (chamber red, exit blue) but not *upstream freshness*. A spatially correct import can still be reading a stale file. The gate is updated for v3 with a freshness check.

### 3.1 v3 Pre-Solve Gate (additions in **bold**)

1. Imported Loads spatially spot-checked (chamber red, exit blue on pressure; throat hot, exit cold on temperature)
2. **Imported Loads numerical Min/Max recorded against expected baseline (v2 baseline: T 768.58–809 K, P −0.039 to 1.898 MPa). Any deviation >0.5 K or >0.005 MPa triggers upstream freshness check before solving.**
3. **External Data Setup cell right-clicked → "Update" before each fresh solve, then top-toolbar "Update Project" invoked to propagate downstream. Verified by Setup cell green-tick state.**
4. Convection BC value AND units re-confirmed in details panel
5. Reference temperatures consistent across Engineering Data / body / environment (all 20 °C)
6. Order-of-magnitude analytical estimates computed (Bi → ΔT, α·ΔT·L → δ, P·r/t → σ)
7. Post-solve: results compared against pre-solve estimates. Any deviation > 2× triggers root-cause investigation before proceeding.

### 3.2 Architecture improvement A3

| # | Change | Benefit |
|---|---|---|
| A3 | Imported Load Min/Max recorded as a versioned baseline value in this document, checked at every solve | Catches stale upstream propagation that v2 architecture (External Data via schematic links) did not detect on its own |

A1 (External Data via schematic links) and A2 (analytical pre-solve estimates) were necessary but not sufficient. A3 closes the remaining gap.

---

## 4. Corrected Imported Load Baseline (v3)

| Quantity | v2 recorded | v3 corrected | Δ |
|---|---|---|---|
| Imported Temperature Min | 768.58 K | 767.85 K | −0.73 K |
| Imported Temperature Max | 809.00 K | 808.17 K | −0.83 K |
| Imported Pressure Min | −0.039 MPa | −0.039 MPa | unchanged |
| Imported Pressure Max | 1.898 MPa | 1.898 MPa | unchanged |
| Source file (temperature) | `static temperature testing for FEA` | `wall_static_temperature_final.csv` (current re-run state) | re-linked |
| Source file (pressure) | `static pressure testing for FEA.csv` | `wall_static_pressure_final.csv` | unchanged |

Pressure import was unaffected. The stale-data issue was confined to the temperature stream.

---

## 5. Corrected Phase 5 Convergence Results

Re-run of all three meshes with corrected External Data link. See `Phase5_Convergence_Study_v2.md` for the full study; QoI table reproduced here for cross-reference.

### 5.1 QoI table (v3 corrected vs v2 recorded)

| QoI | v2 Mesh 1 | v3 Mesh 1 | v2 Mesh 2 | v3 Mesh 2 | v2 Mesh 3 | v3 Mesh 3 | Units |
|---|---|---|---|---|---|---|---|
| σ_vM,throat | 5.1924 | 5.0308 | 5.0321 | 4.8725 | 5.0773 | 4.9171 | MPa |
| σ_vM,global (singularity) | 267.06 | 267.06 | 352.61 | 352.62 | 430.57 | 430.58 | MPa |
| T_throat | 804.38 | 804.38 | 804.38 | 803.59 | 804.38 | 803.59 | K |
| ΔT_throat | 2.12 | 2.12 | 2.11 | 2.10 | 2.10 | 2.10 | K |
| δ_exit | 1.7161 | 1.7148 | 1.7161 | 1.7149 | 1.7163 | 1.7150 | mm |

### 5.2 Magnitude and direction of changes

- **σ_vM,throat:** systematic −3.1% across all three meshes. 
- **σ_vM,global:** unchanged to <0.1%. The singularity is constraint-driven, not thermally driven, so insensitive to the temperature field correction.
- **T_throat:** Mesh 1 unchanged at 804.38 K; Mesh 2 and Mesh 3 shifted to 803.59 K (−0.79 K). Within solver tolerance.
- **ΔT_throat:** essentially unchanged. Through-wall ΔT is governed by Bi, not absolute T_aw level.
- **δ_exit:** systematic −0.06% across all meshes. Exit deformation is dominated by α·ΔT·L integrated along the wall; small reduction consistent with cooler exit-edge load.

### 5.3 Convergence verdict

Convergence pattern is unchanged. 
    M1 → M2 step is −3.17% on σ_vM,throat;
    M2 → M3 step is +0.92%. Both within the same envelope as v2 (−3.09% / +0.89%). Mesh independence conclusion holds.

---

## 6. Updated Factor of Safety

Yield strength interpolation is unchanged (depends only on T_throat, which moved by 0.8 K). Throat T at 803.59 K = 530.44 °C → σ_y(530.44 °C) = 209.95 MPa.

$$\text{FoS}_{v3} = \frac{\sigma_{y,throat}}{\sigma_{vM,throat,M3}} = \frac{209.95}{4.9171} = 42.70$$

| | v2 | v3 |
|---|---|---|
| FoS at converged Mesh 3 | 41.3 | **42.7** |

Direction: marginally safer (+3.4%). Engineering interpretation unchanged — yield is not the binding constraint, creep is.

---

## 7. Engineering Conclusion (v3)

Unchanged from v2. Uncooled SS316 is not yield-limited at this operating point. The wall sits at 530 °C, above the SS316 creep threshold of approximately 410 °C. Time-dependent creep analysis is required to establish the binding limit. SS316 is viable for short-duration prototype or ground-test firings on yield grounds.

The data integrity correction shifted FoS by +3% — engineering conclusion not sensitive to the correction at this margin. This is itself a useful finding: it confirms that for FoS values of order 40+, ~1 K wall temperature noise in the imported load is well below the threshold of engineering significance. For lower FoS regimes (e.g., the t = 5 mm case in Phase 5b at FoS = 33.9), the same noise would be a larger relative contributor to uncertainty.

---

## 8. Updated Limitations Table

Adds L11 to the v2 limitations:

| # | Limitation | Impact | Mitigation |
|---|---|---|---|
| L1–L10 | Per Phase 4 v2 Section 11 | unchanged | unchanged |
| L11 | Imported Load freshness — single-node CFD export variability between re-runs | ~3% on throat stress, ~3% on FoS | A3 architecture: Min/Max baseline values now recorded and checked pre-solve |

---

## 9. File Trail

| File | Purpose |
|---|---|
| `Phase4_FEA_Summary.md` | Original v1 — broken solve (3 BC errors) |
| `Phase4_FEA_Summary_v2.md` | v2 baseline — corrected BCs, stale upstream data |
| `Phase4_FEA_Summary_v3.md` | **This document — data integrity correction + freshness gate** |
| `Phase5_Convergence_Study.md` | Original Phase 5 (against v2 stale data) |
| `Phase5_Convergence_Study_v2.md` | Phase 5 re-run with corrected loads |
| `Phase5b_Sensitivity_Study.md` | Wall thickness sensitivity (t = 3, 4, 5 mm) using corrected loads |

---

## 10. Closing Note on Audit Trail

The v1 → v2 → v3 progression of this document is the deliverable, not the final v3 numbers in isolation. Each version corresponds to a class of failure mode caught:

- v1 → v2: BC unit and mapping errors (caught by Biot number sanity check)
- v2 → v3: Stale upstream data despite correct BC setup (caught by sensitivity study cross-check)

The pre-solve verification gate has been extended at each step. A4-class failures — whatever they will turn out to be — will likely require A3 to be extended further. This is the expected pattern for a project of this complexity and is documented as such rather than papered over.
