# Thermal and Structural Feasibility of an Uncooled SS316 Conical Convergent-Divergent Nozzle and DFM Package


Multiphysics analysis of an uncooled stainless-steel converging-diverging nozzle. The study answers a single question: **can SS316 survive the combined thermal and pressure loading at the design operating point?**

The short answer is *yes against yield, not against creep.*

[Download Full Report (PDF)](https://github.com/dmmarkwork-cloud/ss316-cd-nozzle-feasibility/blob/main/report/ss316_cd_nozzle_report.pdf)

---

## Headline result

| Metric | Value | Source |
|---|---|---|
| Throat von Mises stress (mesh-converged) | **4.92 MPa** | Phase 5, Mesh 3 |
| SS316 yield strength at 530 °C (interpolated) | ~210 MPa | SSINA Table 1 / Nickel Institute 9004 |
| **Factor of safety against yield** | **42.7** | Phase 5 |
| Through-wall ΔT at throat | 2.1 K | Phase 4 |
| Free axial thermal expansion | 1.72 mm over 183 mm | Phase 4 |

![Mach number contour from the converged Fluent solution](cfd/figures/mach_contour_v2.png)
*Mach number contour, converged Fluent solution. Area-weighted exit Mach 2.87 vs hand-calc 2.94, within 2.5% (validation gate passed).*

![Nozzle half-section dimensions](cad/cad_dimensions.png)
*Nozzle half-section dimensions (mm). Throat radius 15 (nominal; as-built minimum 14.942 at −0.77 % area — see Geometry Freeze Disposition), exit radius 30 (ε = 4). Divergent side: 14.8° throat-to-exit chord angle (the straight diverging segment itself is 14.91°). Convergent side: a straight 47.43° taper from the chamber blended into the throat through an R22.5 arc. 4 mm wall.*

![Workflow part 1](workbench/project_schematic_part1.png)
![Workflow part 2](workbench/project_schematic_part2.png)
*Six-phase workflow with explicit validation gates between phases.*

![Von Mises stress contour at Mesh 3](fea/mesh3/von_mises_throat.png)
*Throat von Mises stress = 4.92 MPa at Mesh 3 (mesh-converged), yielding FoS = 42.7 against SS316 yield at ~530 °C. The red region at the inlet vertex is the constraint singularity, empirically confirmed as non-physical by mesh-refinement divergence in Phase 5, and excluded from the FoS calculation.*

**The binding failure mode is not yield.** With wall temperature at ~530 °C — above the SS316 creep onset of ~410 °C, sustained operation is creep-limited, not stress-limited. SS316 is viable for short-duration prototype/ground-test firings at this operating point. Sustained operation requires a creep analysis that is out of scope here.

---

## Operating point

| Parameter | Value | Notes |
|---|---|---|
| Chamber pressure, P_c | 2 MPa | Working air, γ = 1.4 |
| Chamber temperature, T_c | 800 K | Within SS316 continuous-service limit (925 °C, oxidizing) |
| Exit pressure, P_e | 0.1 MPa | Sea-level design |
| Throat radius, R_t | 15 mm | |
| Area ratio, A_e/A_t | 4 | |
| Contraction ratio, A_c/A_t | 8 | From M_inlet ≤ 0.1 constraint (min ≥ 5.9) |
| Wall thickness, t | 4 mm | Baseline; sensitivity at 3/4/5 mm |
| Geometry | Conical C-D | Diverging straight taper 14.91° half-angle (14.8° throat-to-exit chord); converging straight taper 47.43° half-angle, blended into the throat by an R22.5 arc. As-built, verified from CAD/STEP — see `docs/Geometry_Freeze_Disposition.md` |
| Material | SS316 | Uncooled, temperature-dependent properties |

Material precedent: the IJIRSET 2019 H₂O₂ monopropellant thruster (Deif et al.) uses SS316 in a similar uncooled configuration. Conditions differ (lower chamber pressure, smaller throat, pulsed, different working fluid), so it supports material precedent only.

---

## Tools & environment

| Phase | Tool | Notes |
|---|---|---|
| Hand calculations | Jupyter + handcalcs | Symbolic → numeric trace |
| CAD geometry | SolidWorks → SpaceClaim | 2D axisymmetric surface body |
| CFD | ANSYS Fluent 2026 | 2D axisymmetric, k-ω SST |
| FEA | ANSYS Mechanical 2026 | Steady-state thermal + static structural |
| Mesh | Fluent Meshing (CFD), Mechanical (FEA) | Combined node+element ≤ 32k ||

License is the ANSYS 2026 R1 Student release (valid through March 2027). The 32k node+element cap drove the 2D-axisymmetric choice throughout.

---

## Analysis workflow

Six phases, each gated by validation against the previous phase.

| # | Phase | Status | Deliverable |
|---|---|---|---|
| 1 | Hand calculations (isentropic, area-Mach, T_aw) | Complete | `notebooks/cd-nozzle-handcalc-checkpoint.ipynb` |
| 2 | SolidWorks geometry (2D axisymmetric profile, 4 mm wall offset) | Complete | `cad/conical_v1_sketch.SLDPRT` |
| 3 | CFD — ANSYS Fluent, 2D axisymmetric, k-ω SST (incl. CFD/hand-calc validation gate, §4.4) | Complete | `docs/Phase3_CFD_Summary.md` |
| 4 | FEA — one-way FSI → ANSYS Mechanical thermal-structural | Complete | `docs/Phase4_FEA_Summary_v3.md` |
| 5 | Mesh convergence study | Complete | `docs/Phase5_Convergence_Study_v2.md`, `notebooks/convergence_study_handcalc-checkpoint.ipynb` |
| 6 | Wall-thickness sensitivity study | Complete | `docs/Phase5b_Sensitivity_Study.md`, `notebooks/wall_thickness_sensitivity-checkpoint.ipynb` |

The one-way FSI uses Fluent wall outputs (static temperature, static pressure) mapped onto the FEA mesh through ANSYS Workbench **External Data systems**.

---

## Key findings

1. **Yield is not the binding failure mode.** FoS ≈ 42.7 against yield at the throat, mesh-converged. Time-dependent creep is the limiting mode for sustained operation.
2. **The wall is near-isothermal** through the thickness (~2 K through-wall ΔT at the throat). In still air, the outer wall cannot shed heat fast enough to develop a meaningful gradient. **The dominant stress contributor is thermal-bending, not pressure hoop**; a reversal of the naïve thin-wall expectation, confirmed by the thickness sensitivity study.
3. **Mesh convergence is demonstrated** by a three-mesh trend study. The throat von Mises probe is stable to <1% between Mesh 2 and Mesh 3 (4.87 MPa → 4.92 MPa). Global max von Mises diverges with refinement, empirically confirming the inlet-vertex constraint as a singularity rather than a physical hot spot.
4. **Three independent boundary-condition errors** were caught and corrected during Phase 4 — most consequentially, a convection coefficient 6 orders of magnitude too high from a W/mm²·K vs W/m²·K unit mismatch in Mechanical. The pre-solve verification gate added in response to these errors is documented in `docs/Phase4_FEA_Summary_v2.md`

---
## The Design for Manufacturing (DFM) Package

The feasibility result above is only useful if the part can be made and inspected. The analysis is therefore carried into a **fabricable engineering package**: a GD&T'd, toleranced drawing set for the inlet joint, tolerance stack-ups that close against the frozen FEA geometry, a machining route, an inspection plan, a BOM, and a mock supplier RFQ.

**Scope** is a short-duration, ground-test prototype, quantities 1 to 5. Drawing set is ASME Y14.5-2018, first-angle, A2, issued Revision C (2026-08-13).




![Exploded view of the inlet joint assembly](dfm/images/exploded-view.png)
*Inlet-joint assembly (CDN-000). Nozzle body, flexible-graphite gasket, mounting flange, 8 x M8 A286 floating fasteners.*

| Sheet | Part | Key controls |
|---|---|---|
| [CDN-001](dfm/drawing/CDN-001.pdf) | C-D Nozzle Body | frozen internal contour by surface profile 0.2 A\|B + total runout 0.05 A\|B; throat wall **4 +0.3/0 (CTQ)**; pilot Ø92.80 g6 |
| [CDN-002](dfm/drawing/CDN-002.pdf) | Mounting Flange | register bore Ø92.80 H7 with ⊥0.05 A; seat flatness 0.05 |
| [CDN-000](dfm/drawing/CDN-000.pdf) | Inlet-joint Assembly | ballooned BOM, interface notes, bolt torque 6.8 N·m cold |


### Four main decisions that carry this package

1. **Pilot locates, bolts clamp.** A single Ø92.80 H7/g6 locational-clearance fit centres the flange (Datum B); the 8 x M8 fasteners float and only clamp, positioned at MMC.
2. **The CTQ is the throat wall, and it is not a yield argument.** The 4 +0.3/0 band comes from creep life at ~530 °C, pressure-boundary minimum material, and machining minimum. The sensitivity study confirms the whole band is structurally free (FoS ≈ 40 across it), which is exactly why the tolerance had to be justified on other grounds.
3. **The stacks close, with margin.** Worst-case 1-D concentricity 0.060 mm against a 0.10 mm limit (1.68x); the bolt pattern assembles at strict MMC with no reliance on bonus tolerance.
4. **Every value is traceable.** Each dimension, tolerance and fit is tied to a source and a claim tier in the [value register](dfm/docs/value-register.md) and [`SOURCES.md`](dfm/sources/SOURCES.md), down to the gasket bolt load taken from ASME BPVC VIII-1 Mandatory Appendix 2.

The package closes out with an inspection plan (including UT through-wall at the CTQ) and mock AS9102B FAIR forms for all three sheets.

**Full package: [`dfm/README-dfm.md`](dfm/README-dfm.md)**

---


## Scoping & limitations

Stated up front because they affect how the results should be read:

- **No creep model.** The active scope boundary: yield is not the binding limit for sustained operation, and creep is flagged as required future work.
- **Steady-state only.** No transient startup/shutdown or thermal-fatigue/cyclic loading; startup transients can produce higher peak loads than the steady operating point analyzed here. The short-duration-firing conclusion does not cover cyclic life.
  - *Specific open instance (L12, 2026-08-12, from the DFM package):* the **inlet-flange radial thermal gradient** drives **low-cycle fatigue at the bore/fillet** (cyclic, distinct from the throat-wall creep above). First-order check (`Project_A/docs/phase4/thermal-gradient-calc.md`): elastic below ΔT ≈ 120 °C; actual ΔT unrun (needs a thermal model or test thermocouple, then a shakedown/LCF check). See FEA Summary v3 §8, L12.
- **One-way FSI only.** No structural deformation feedback into CFD. Standard for preliminary analysis at this fidelity.
- **Adiabatic-wall CFD → imposed T_aw on FEA.** Conservative; credits no wall-side conduction or radiation relief.
- **2D axisymmetric.** No asymmetric loads. Acceptable for axisymmetric geometry and required by the license cell cap.
- **Outer-wall convection h = 10 W/m²·K.** Still-air natural convection; conservative for a test stand where exhaust-plume entrainment would add convective relief.

---

## Repository structure

```
C-D-Nozzle/
├── README.md                                           # This file
├── docs/
│   ├── ss316_properties.md
│   ├── Geometry_Freeze_Disposition.md                  # Frozen as-built contour + deviation disposition
│   ├── Phase3_CFD_Summary.md
│   ├── Phase4_FEA_Summary_v2.md
│   ├── Phase4_FEA_Summary_v3.md
│   ├── Phase5_Convergence_Study_v2.md
│   └── Phase5b_Sensitivity_Study.md
├──dfm/
|   ├── calculations                                    # gasket loads, stack-up analysis and plot
|   ├── docs                                            # drawing data, specs, plans, records,  registers, decisions
|   ├── drawing                                         # official drawing sheets; CDN-000, CDN-001, CDN-002
|   ├── fair                                            # first article inspection request forms
|   ├── images                                          # isometric, inspection, and clash views
|   ├── revisions                                       # drawing sheet revision block records
|   ├── sources                                         # package source ledger (standards, materials, methods)
|   └── README-dfm.md                                   # DFM package summary
├── notebooks/
│   ├── cd-nozzle-handcalc-checkpoint.ipynb             # Phase 1
│   ├── convergence_study_handcalc-checkpoint.ipynb     # Phase 5
│   └── wall_thickness_sensitivity-checkpoint.ipynb     # Phase 6
├── cad/
│   ├── cad_dimensions.png
│   ├── conical_v1_sketch.SLDPRT                        # SolidWorks source 2D/3D
│   ├── conical_v1_sketch.STEP                  
│   ├── conical_v2_spaceclaim.sketch.scdocx             # SpaceClaim geometry
│   ├── inlet_side.png                       
│   ├── isometric.png                           
│   ├── outlet_side.png                        
│   └── right_side.png                          
├── cfd/
│   ├── case_data/                                      # CFD Fluent data and setup
│   ├── figures/                                        # results, plots, contours
│   ├── exports/                                        # wall_temperature_v2.xy, wall_pressure_v2.xy, BC, and loads
│   └── mesh/                                           # Mesh data
├── fea/
│   ├── mesh1/                                          # Solved figures (von Mises, ΔT, deformation) and Mechanical data in mesh 1
│   ├── mesh2/                                          # Solved figures (von Mises, ΔT, deformation) and Mechanical data in mesh 2
│   └── mesh3/                                          # Solved figures (von Mises, ΔT, deformation) and Mechanical data in mesh 3
├── workbench/
    ├── project_schematic_part1.png                     # Analysis workflow
    └── project_schematic_part2.png
└── report/
    └── ss316_nozzle_report.pdf                         # Comprehensive report of the project
```

---

## Related work

- **`gas-vessel-fea`** — prior portfolio piece. Pressure vessel mesh convergence study; same methodological framework applied to a simpler geometry.

---


## Author
Mark Lorenz Yamanaka · Tsukuba · 2026
