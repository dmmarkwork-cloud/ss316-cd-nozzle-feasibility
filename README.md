# Thermal and Structural Feasibility of an Uncooled SS316 Conical Convergent-Divergent Nozzle


Multiphysics analysis of an uncooled stainless-steel converging-diverging nozzle. The study answers a single question: **can SS316 survive the combined thermal and pressure loading at the design operating point?**

The short answer is *yes against yield, not against creep.*

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
*Nozzle half-section dimensions (mm). Throat radius 15, exit radius 30 (ε = 4); 14.8° conical divergent half-angle. The convergent side is not a simple cone; it is a straight taper from the chamber blends into the throat through an R22.5 arc, so it has no single half-angle. 4 mm wall.*

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
| Geometry | Conical C-D | 14.8° divergent half-angle; convergent side is a straight taper blended into the throat by an R22.5 arc |
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

## Scoping & limitations

Stated up front because they affect how the results should be read:

- **No creep model.** The active scope boundary: yield is not the binding limit for sustained operation, and creep is flagged as required future work.
- **Steady-state only.** No transient startup/shutdown or thermal-fatigue/cyclic loading; startup transients can produce higher peak loads than the steady operating point analyzed here. The short-duration-firing conclusion does not cover cyclic life.
- **One-way FSI only.** No structural deformation feedback into CFD. Standard for preliminary analysis at this fidelity.
- **Adiabatic-wall CFD → imposed T_aw on FEA.** Conservative; credits no wall-side conduction or radiation relief.
- **2D axisymmetric.** No asymmetric loads. Acceptable for axisymmetric geometry and required by the license cell cap.
- **Outer-wall convection h = 10 W/m²·K.** Still-air natural convection; conservative for a test stand where exhaust-plume entrainment would add convective relief.

---

## Repository structure

```
C-D-Nozzle/
├── README.md                          # This file
├── docs/
│   ├── ss316_properties.md
│   ├── Phase3_CFD_Summary.md
│   ├── Phase4_FEA_Summary_v2.md
│   ├── Phase4_FEA_Summary_v3.md
│   ├── Phase5_Convergence_Study_v2.md
│   └── Phase5b_Sensitivity_Study.md

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
