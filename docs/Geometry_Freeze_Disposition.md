# Geometry Freeze Disposition — SS316 Conical C-D Nozzle

**Purpose:** Establish the single frozen source of truth for the nozzle contour before the manufacturing/DFM package (Project A) is built on it, and formally disposition the deviations between the documented nominal geometry and the as-built CAD that was actually analyzed.

**Status:** FROZEN — as-built contour, use-as-is. See §4 for the disposition and §6 for the conditions.
**Compiled:** 2026-07-20
**Applies to:** `cad/conical_v1_sketch.SLDPRT`, `cad/conical_v1_sketch.STEP`, the CFD case (`cfd/case_data/residual_results.cas.h5`), and the FEA meshes (`fea/mesh*/`).

---

## 1. Why this note exists

Before freezing the geometry for drawing production, a documentation discrepancy on the converging half-angle had to be resolved (flagged in the Project A pre-execution review, item S3, and in the Geometry Workflow Record §10.1). On investigation the discrepancy was larger than a single wrong angle: the nominal design values stated in several documents, the coordinate table in the Geometry Workflow Record, and the as-built CAD were three different geometries.

Freezing a manufacturing drawing requires one authoritative contour. A profile-of-a-surface callout on the aerodynamic wall is only a true statement if it references the contour the analysis actually validated. This note records which contour that is, how it was verified, and how the deviation from the stated nominal is dispositioned.

---

## 2. What was verified, and how

The as-built contour was measured three independent ways and all three agree. This is direct measurement of the geometry files, not inference from documentation.

| Source | What was read | Method |
|---|---|---|
| `cad/conical_v1_sketch.STEP` | CARTESIAN_POINT, LINE, CIRCLE, TRIMMED_CURVE entities | Text parse of the STEP (AP214) file; angles/radii computed from the point and arc-center coordinates |
| `cfd/case_data/residual_results.cas.h5` | 15,951 mesh node coordinates; wall boundary = zone `convergin_throat_diverging` (465 nodes) | HDF5 read of `meshes/1/nodes/coords`; wall nodes extracted via the face→node connectivity |
| `fea/mesh2/mesh2_mesh_data.stl` | 34,762 mesh vertices | Binary STL parse; inner-wall contour = minimum radial coordinate per axial station |
| `cad/conical_v1_sketch.SLDPRT` | Converging taper angle, throat minimum radius | Opened and measured in SolidWorks — **confirmed by the author, 2026-07-20** |

**Cross-check result:** the CFD mesh wall matches the STEP contour to better than 0.1 µm in the throat-arc region; the FEA inner wall reaches the same 14.9420 mm minimum radius. The three analysis artifacts and the CAD describe the same contour. The concern that the May-4 STEP might be stale relative to the later SLDPRT is closed: the author has confirmed the SLDPRT reads the as-built values below.

*Claim tier: T1 (verified against primary source — the geometry files themselves).*

---

## 3. Frozen geometry — the as-built contour

| Feature | Value | Basis / tier |
|---|---|---|
| Converging straight taper half-angle | **47.43°** | Measured, all three sources. T1 |
| Diverging straight taper half-angle | **14.91°** | Measured, all three sources. T1 |
| Diverging throat-to-exit chord angle | 14.81° | Geometric (throat 15 mm → exit 30 mm over 56.72 mm axial). This is the "14.8°" quoted in the README. T2 |
| Throat minimum radius (as-built) | **14.942 mm at x ≈ −1.6 mm** | Measured, all three sources. T1 |
| Throat radius (nominal design intent) | 15.00 mm at x = 0 | Project Definition / hand calc. T1 |
| Upstream throat blend arc | R 22.50 mm (1.5 R_t) | Measured; matches convention. T1 |
| Downstream throat blend arc | R 5.73 mm (0.382 R_t) | Measured; matches convention. T1 |
| Chamber radius | 42.40 mm (R_t·√8) | Design. T1 |
| Exit radius | 30.00 mm (R_t·√ε) | Design. T1 |
| Wall thickness (baseline) | 4.00 mm, offset radially outward | Design. T1 |
| Wall thickness (sensitivity) | 3, 4, 5 mm | Phase 5b. T1 |

**The frozen drawing basic contour is defined by the CAD/STEP coordinate table, not by the stated half-angle parameters.** For an aerodynamic surface this is the correct authority — the surface is a defined contour, and a profile-of-a-surface tolerance is applied to it. The half-angle numbers are descriptive, not the controlling definition.

---

## 4. Deviation disposition

Two deviations exist between the documented nominal design and the as-built/analyzed contour. Both are dispositioned **use-as-is**. Reasoning below.

### 4.1 Converging half-angle: nominal 30° → as-built 47.43°

The 30° value appears in the Project Definition and (before correction) in `Phase3_CFD_Summary.md`. The as-built taper is 47.43°. The Geometry Workflow Record separately derived 45° from its own coordinate table (§2.4/§10.1); that table does not match the CAD (its converging-line/arc junction is at (−15.91, 21.59); the CAD has it at (−18.184, 22.221)), so its 45° figure was arithmetic on an incorrect table, not a measurement of the CAD.

**Disposition — use as-is.** The converging section of a C-D nozzle is entirely subsonic; its wall angle sets the chamber contraction profile, not the throat/supersonic performance that the analysis gates on. The CFD validation gate (area-Mach and isentropic checks) passed at the ~1–2.5 % level on this as-built geometry. A steeper contraction cone is aerodynamically benign here. No re-analysis is warranted; the deviation is a documentation error, now corrected, not a geometry defect.

*Note on convention:* the converging side is not a single cone — it is a straight 47.43° taper blended into the throat by the R22.5 arc. Describing it with a single half-angle is itself an approximation; the drawing controls it by the coordinate contour, not by an angle callout.

### 4.2 Throat minimum radius: nominal 15.00 mm at x = 0 → as-built 14.942 mm at x ≈ −1.6 mm

The two throat blend arcs are tangent to each other, but their common tangent point is tilted ~4.1° from the nozzle axis rather than lying at the axial throat plane. Consequently the true minimum flow radius is 14.942 mm and sits ~1.6 mm upstream of x = 0, instead of 15.00 mm exactly at x = 0.

**Quantitative impact (throat area):**

$$\frac{\Delta A}{A} = \left(\frac{14.942}{15.000}\right)^2 - 1 = -0.77\%$$

Assumptions: circular cross-section (axisymmetric); area governed by minimum radius. This is a straightforward geometric ratio, not a flow calculation.

**Disposition — use as-is.** A −0.77 % throat-area change is well inside the CFD validation band already accepted for this model (exit Mach agreement was within 2.5 %). Mass flow through a choked throat scales linearly with throat area, so the first-order effect on ṁ and thrust is likewise ≈ −0.77 % — below the fidelity of the present analysis and immaterial to the feasibility conclusion (FoS ≫ 1 against yield; creep-governed, not stress-governed). The offset originates in the arc-center placement of the original sketch; it is characteristic of the as-built part and is what was analyzed.

*Claim tier for both dispositions: the measurements are T1; the "use-as-is" engineering judgment is T3 (reasonable engineering judgment, stated as such). A formal mass-flow/thrust re-computation on the as-built contour would raise §4.2's impact statement to T2 but is not required for the feasibility scope.*

---

## 5. Governing-rule check (no re-analysis)

The project's standing rule is: *no re-analysis; if drawing work reveals an analysis problem, log it as an issue.* This disposition complies:

- Nothing here re-opens or re-runs the CFD or FEA. Reading the existing mesh and CAD files to identify which contour was analyzed is verification of the input, not re-analysis.
- The deviations are dispositioned against the **already-completed** validation results, not against a new run.
- The frozen contour for drawings is the analyzed contour, so the analysis→drawing traceability chain is preserved and honest.

If a future higher-fidelity study (e.g. the Bartz-BC follow-up already in Phase 5b future work) re-computes performance, the −0.77 % throat-area note in §4.2 should be revisited then — logged here as a known open item, not acted on now.

---

## 6. Freeze conditions and downstream actions

**Frozen for Project A drawing production:** the as-built CAD/STEP contour in §3, wall thickness t = 4.00 mm, maximum 3 parts.

Actions taken with this freeze:
1. `docs/Phase3_CFD_Summary.md` corrected: converging/diverging half-angles updated to as-built; the erroneous "throat at x ≈ −47 mm" entry corrected to x = 0.
2. `README.md` geometry caption and table corrected: converging taper stated as 47.43°; the 14.8° diverging figure identified as the throat-to-exit chord angle (vs the 14.91° straight-segment angle); throat nominal-vs-as-built noted.

Open items carried forward (not blocking the freeze):
- The Geometry Workflow Record §2.4 point table (in the Project A workspace) still contains the incorrect converging-line/arc junction coordinates and a 45° derivation; correct it there for internal consistency.
- Any Project Definition document that states 30° converging should be corrected to reference this disposition.
- The drawing's profile-of-a-surface tolerance zone (to be assigned in Project A Phase 4) should be checked against these deviations; the −0.058 mm throat-radius offset is within typical machining profile tolerances (~±0.05–0.1 mm class, to be confirmed against the chosen tolerance), whereas the converging-section nominal-vs-as-built gap reaches ~1.4 mm and therefore cannot be represented by drawing the clean nominal — the as-built contour must be the drawn basic geometry.

---

## 7. One-line summary

The nozzle is frozen on its **as-built, analysis-verified contour** (converging taper 47.43°, throat minimum 14.942 mm at x ≈ −1.6 mm, diverging 14.91°, t = 4 mm). The documented "30° / 15°" nominal was a paperwork error, now corrected. Both deviations from nominal are dispositioned use-as-is: the converging angle is subsonic and performance-irrelevant, and the −0.77 % throat-area offset is inside the accepted CFD validation band. No re-analysis performed or required.
