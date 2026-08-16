# Method and Assumption Register

How the package was produced, the rules it was held to, and every assumption it rests on.

**Goal:** convert the analyzed SS316 nozzle from an *analysis exercise* into a *fabricable engineering package*: GD&T drawings, tolerance stack-ups, a manufacturing route, an inspection plan, a BOM and a supplier RFQ.

---

## 1. Standing rules

1. **Provenance rule.** No dimension, tolerance, fit class or material value enters a drawing without a **source** and a **claim tier**.
2. **Claim tiers.**
    - **T1** verified against a primary source
    - **T2** derivable or reproducible on demand
    - **T3** standard engineering judgment, stated as such
    - **T4** strategy judgment, never appears in the deliverable
3. **Function rule.** GD&T is applied only where function demands it. Every feature control frame must answer: what function does this control protect?
4. **Visible-error rule.** External review was a hard gate on publication, not a polish step.

## 2. How the package was built

| Stage | Output | Where it lives |
|---|---|---|
| Freeze the geometry | One authoritative contour, hash-verified across STEP, CFD mesh and FEA mesh, with the nominal-vs-as-built deviations formally dispositioned | [`Geometry_Freeze_Disposition.md`](../../docs/Geometry_Freeze_Disposition.md) |
| Function analysis | Why each geometric control exists, before any is drawn | [`function-analysis.md`](function-analysis.md) |
| Interface and datum scheme | Fit class, fastener condition, datum reference frame, over-constraint logic | [`interface-control-plan.md`](interface-control-plan.md) |
| Joint design record | Every resolved joint decision with its source and tier | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) |
| Drawing data | Every value that goes on a sheet, sourced and tiered | [`drawing-data.md`](drawing-data.md) |
| Value register | Every as-designed value in one table, with its source and tier | [`value-register.md`](value-register.md) |
| Tolerance stack-ups | Three worst-case stacks: analysis-link, misalignment, axial engagement | [`stackup.md`](stackup.md) |
| Manufacturing route | Machining against casting against additive, material spec, shop practice | [`manufacturing.md`](manufacturing.md) |
| Gasket specification | Type, geometry, duty, factors, bolt loads | [`gasket-spec.md`](gasket-spec.md) |
| Inspection and procurement | CTQ verification, FAIR forms, RFQ | [`inspection-plan.md`](inspection-plan.md) · [`RFQ.md`](RFQ.md) |
| External review | Two platforms, four threads, point-by-point disposition | [`../revisions/cdn-drawing-revisions.md`](../revisions/cdn-drawing-revisions.md) |


## 3. Traceability

Only the **internal contour** and the **throat wall thickness** trace to the frozen analysis. The mount, bolt pattern, pilot, seal and datum scheme are **assumed design (T3)**: the parent project is 2-D axisymmetric and contains no mounting features.

"Traceable to the analysis" is claimed only for the contour and the wall thickness. Everything else is presented as engineering judgment, and where a judgment carries a number, the number carries a reason.

## 4. Assumption register

| ID | Assumption | Basis | Tier | Impact if wrong |
|----|-----------|-------|------|-----------------|
| A-01 | Bolted flange mount, 8 × M8 on Ø128 | Standard small-thruster practice | T3 | Datum scheme and stacks change |
| A-02 | Qty 1–5 prototype batch | Scope decision | T4 | Route selection changes at volume; worst-case stacks could move to statistical |
| A-03 | Geometry **FROZEN**: converging taper 47.43°, throat minimum 14.942 mm at x ≈ −1.6 (nominal Rt 15.00), diverging 14.91°, R22.50/R5.73 blends, t = 4.00 mm | CAD/STEP-verified, dispositioned use-as-is, deviations inside the CFD validation band | **T1** | CTQ values shift; any change requires a new freeze |
| A-05 | General tolerance = explicit title-block table, ASME style. ISO 2768-2/-mK not used | Sidesteps the withdrawn ISO 2768-2, superseded by ISO 22081:2021; cleanest for a Y14.5 package | T3 | Untoleranced dimensions uncontrolled |
| A-06 | Part set = **two parts**, nozzle body plus separate bolted mounting flange; gasket a BOM line | Interface competence needs one real machined-to-machined joint; minimal scope, 2 not 3 | T3 | Reverts to a single part via the degrade-gracefully rule |
| A-07 | Pilot register **H7/g6** locational clearance locates the flange, datum B | Centring plus hand assembly plus matched-CTE joint | T3 (values T1) | Loose degrades concentricity; interference is not serviceable |
| A-08 | Bolt pattern = **floating fastener**, position ⌀T at MMC, T = H − F | Simplest robust clamp; keeps threads out of the SS316 body on a frequently-disassembled prototype | T3 (formula T2) | Holes bind, or the pattern is over-toleranced |
| A-09 | **Two-datum A\|B** mating scheme, datum C only if clocking is proven necessary | Axisymmetric function, non-indexed 8-hole pattern; avoids a needless tertiary | T3 | Missing C if an indexed feature is later required |

## 5. Out of scope

Stated so a reviewer knows what is deliberately absent rather than overlooked.

- **No re-analysis.** The geometry is frozen from the corrected FEA project. If drawing work reveals an analysis problem it is logged as an issue, not fixed by reopening the analysis.
- **No thread specifications** beyond standard callouts, and **no weld symbols**: nothing in the assembly is welded.
- **No CAM or toolpath work.**
- **Cyclic life is not assessed.** The flange radial thermal gradient is identified as a low-cycle-fatigue question and deferred to the analysis repo as an explicit open item, not silently dropped.
