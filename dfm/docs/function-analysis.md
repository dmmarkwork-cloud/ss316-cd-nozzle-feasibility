# Function Analysis: Why Each Geometric Control Exists

Every geometric control on the drawings is justified here before it is drawn.

**Governing rule:** every feature control frame (FCF) traces to a row in §7. A control with no function does not go on the drawing.

**Feeds:** the datum scheme and the FCF schedule. Interface mechanics (fit class, fastener math, cross-part stack) live in [`interface-control-plan.md`](interface-control-plan.md); this file references them, it does not repeat them.

> **Claim Tier**
> - **T1** verified against the frozen analysis
> - **T2** derivable/reproducible
> - **T3** engineering judgment, stated as such
> - **T4** strategy, never on the drawing

| FCF | Control | Value | Tier | § |
|---|---|---|---|---|
| 1 | Internal contour, profile of a surface → A\|B | 0.2 | surface T1 / value T3 | 3, 7 |
| 2 | Throat wall, dimension + tol, CTQ | 4 +0.3/0 | value T1 / band T3 | 4, 7 |
| 3 | Seal face, flatness + Ra | 0.05, Ra 3.2 to 6.3 µm | T3 | 2, 7 |
| 4 | Pilot Ø, size, Rule #1 envelope | H7/g6 | T1 | 5, 7 |
| 5 | Bolt pattern, position at MMC → A\|B | ⌀0.9 Ⓜ | T2 | 1, 7 |
| 6 | Throat-to-mount, total runout → A\|B | 0.05 | surface T1 / value T3 | 3, 7 |
| 7 | Pilot squareness, both parts → A | 0.05 | T3 | 7 |
| 8 | Flange outboard face, Part 2 → A | 0.05 | T3 | 7 |
| n/a | Datum frame | A = seal face, B = pilot, no C | T3 | 5 |

---

## 1. How does the nozzle mount? (A-01)

**Decision:** bolted flange, **8 × M8** on a **Ø128** bolt circle, flange piloted on the nozzle body (two parts per **A-06**). Standard small-thruster practice.

- Fastener: **8 × M8 A286 (ASTM A453 Gr 660)** on the Ø128 bolt circle. Position tolerance **⌀0.9 Ⓜ → A|B**.
- Fit and fastener condition: [`interface-control-plan.md`](interface-control-plan.md) §2 (H7/g6 pilot) and §4 (floating fastener, $T = H - F$).

**Tier:** T3, assumed design. No mount exists in the parent analysis. Recorded as A-01.

## 2. What must seal?

**Function:** the mating face carries the gasket that seals the gas path at the joint. Sealing needs a **flat** face with a controlled **surface finish**. A rough or dished face leaks.

- Control: **flatness** on the mating face plus a **surface-texture (Ra)** callout.
- **Gasket (T3):** soft flat **flexible graphite**, reinforced grade. It survives the hot section, conforms to machined faces at low seating load, and is cheap and replaceable. That matches the frequent-disassembly basis of the floating-fastener call (A-08). BOM line only, not drawn. Full spec in [`gasket-spec.md`](gasket-spec.md).
- **Surface finish (T2):** Ra **3.2–6.3 µm (125–250 µin)**, the standard gasket-contact-face range. Soft graphite seals without a fine finish; it needs surface "tooth" to grip. Cited to ASME B46.1 (S5).

**Datum consequence:** the flange face is the functional seat, so it is **primary datum A**.

## 3. What must align?

**Function:** the throat axis must stay concentric with the mount axis so thrust acts through the intended line. Misalignment causes thrust-vector cant.

ASME Y14.5-2018 **removed concentricity**. The honest substitutes are runout, position of an axis, or a datum-referenced profile.

**Decision: total runout of the internal contour → A|B, ⌰ 0.05.** Kept alongside profile 0.2; the two do distinct jobs. Value **T3**, surface **T1**.

### Why runout and not composite profile

The requirement is a coaxiality budget. Total runout controls coaxiality directly:

$$\text{TIR } 0.05 \;\Rightarrow\; e_{\text{runout}} = 0.025 \text{ mm radial} \;\Rightarrow\; e_{\text{WC}} = 0.0345 + 0.025 = 0.060 \text{ mm} \;\le\; 0.10 \;\;(1.68\times)$$

Composite profile does not. Per Y14.5-2018 §11.6 its lower tier refines *orientation and form* only, so location stays at the upper tier. `⌓ 0.2 | 0.05 A|B` leaves the throat offset at ±0.1 mm radial and the stack fails:

$$e_{\text{WC}}^{\text{composite}} = 0.0345 + 0.100 = 0.135 \text{ mm} \;>\; 0.10 \text{ mm}$$

### Why keep both profile 0.2 and runout 0.05 (backed by external reviews)

They do distinct jobs. **Profile 0.2 → A|B** controls contour *shape* against the frozen coordinate table, which is aerodynamic performance. **Runout 0.05 → A|B** adds the tight *coaxiality* the stack needs, which profile 0.2 (±0.1 radial) alone does not give.

A single profile 0.05 would also close the stack, but it over-controls the whole contour form when only the throat needs coaxiality. Runout gets it with cheap spin-fixture inspection.

**Rejected, position of a throat axis:** the throat is a contour, not a clean feature of size, so a derived axis is ill-defined.

## 4. What is thermally and structurally critical? (the CTQ)

**CTQ = throat wall thickness, t = 4.00 mm.**

> **IMPORTANT:** The throat wall is critical-to-quality because it sets the pressure-boundary **minimum-material condition**, must survive **creep** at the ~530 °C throat operating point for the firing duration, and carries the **manufacturing minimum thickness**. Per the parent sensitivity study: *"wall-thickness selection at this operating point is not yield-governed … it IS governed by creep life, manufacturing minimums, and weight."*

**Control:** dimension plus tolerance, flagged **CTQ**, note basis = creep life + pressure-boundary MMC + manufacturing minimum. **(T1)**: traces to the frozen analysis.


## 5. Functional datum scheme

Full derivation and over-constraint logic in [`interface-control-plan.md`](interface-control-plan.md) §3.

- **Datum A, mating/seal face** (primary): the functional seat, controls tilt. Chosen because the sealing function references it.
- **Datum B, pilot diameter** (secondary): centres the part, the locator for the alignment function.
- **Datum C** (tertiary): **not used.** The nozzle is axisymmetric in function and the 8-hole pattern is non-indexed, so a clocking datum would add constraint no function needs.

**Why not locate on the bolt pattern:** the pilot locates, the bolts clamp through clearance holes at MMC. Locating on both is over-constraint.

## 6. Traceability

| Feature | Control | Traces to | Tier |
|---|---|---|---|
| Internal contour | Profile of a surface → A\|B | Frozen CFD-validated geometry (A-03) | T1 |
| Throat wall thickness | Dimension + tol, CTQ | Frozen FEA sensitivity study | T1 |
| Mating/seal face | Flatness + Ra | Assumed design | T3 |
| Pilot diameter | Size H7/g6 → datum B | Assumed design; fit values T1 | T3 |
| Bolt pattern | Position ⌀0.9 Ⓜ → A\|B | Assumed design; hole size T1 | T3 |
| Throat-to-mount alignment | Total runout → A\|B | Surface T1 / value T3 | mixed |
| Flange outboard face | Parallelism → A | Assumed design | T3 |

## 7. FCF to function map

Every control on the issued sheets appears here.

| # | Feature | FCF | Function it protects | Datum ref | Source / tier |
|---|---|---|---|---|---|
| 1 | Internal contour | Profile of a surface **0.2** | Aerodynamic performance, validated geometry | A\|B | A-03 / surface T1, value T3 |
| 2 | Throat wall | Dimension + tol **4 +0.3/0** (CTQ) | Creep life + pressure-boundary min-material + mfg min | n/a | Sensitivity study / value T1, band T3 |
| 3 | Seal face | Flatness **0.05** + Ra 3.2–6.3 | Gasket seal at the joint | n/a (form) | S5 / T3 |
| 4 | Pilot Ø | Size **H7/g6** (Rule #1 envelope) | Centres the flange | this *is* datum B | S4 / T1 |
| 5 | Bolt pattern | Position **⌀0.9 Ⓜ** | Clamp, assembles without binding | A\|B | S4 / hole T1, position T2 |
| 6 | Throat-to-mount | Total runout **⌰ 0.05** | Thrust-axis alignment | A\|B | surface T1 / value T3 |
| 7 | Pilot squareness (both parts) | **⊥ 0.05 → A** | Keeps datum B square to the seat, so the pilot centres without tilting the joint | A | S1 / T3 |
| 8 | Flange outboard face (Part 2) | **∥ 0.05 → A** | Keeps the external mounting face parallel to the sealed joint, so bolting to the chamber does not cock the joint open | A | S1 / T3 |

## Sources

- **S1** ASME Y14.5-2018:
    - FCF language, datum rules, Rule #1
    - removal of concentricity; §11.6 composite profile
- **S4** ISO 286-2 / ISO 273:
    - pilot fit class and clearance-hole size
- **S5** ASME B46.1:
    - surface-texture callouts
- **S11** frozen geometry and FEA:
    - [`Geometry_Freeze_Disposition.md`](../../docs/Geometry_Freeze_Disposition.md)
    - [`Phase5b_Sensitivity_Study.md`](../../docs/Phase5b_Sensitivity_Study.md)
