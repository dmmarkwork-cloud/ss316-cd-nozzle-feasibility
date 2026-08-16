# Manufacturing Route and Material

How the two parts are made and from what: route selection, SS316 machinability practice, raw-stock sizing, distortion control, and the procurement-grade material line the drawing BOM and the RFQ both draw from.

> **Note:** Only the **grade** (S31600) and the **wall-thickness minimum** trace to the frozen analysis. The route, stock sizing and shop practice are **T3** grounded in the cited standards. They are not analysis-derived and are not claimed to be.

> **Claim Tier**
> - **T1** verified against the frozen analysis
> - **T2** derivable/reproducible
> - **T3** engineering judgment, stated as such
> - **T4** strategy, never on the drawing

| Item | Value | Tier | § |
|---|---|---|---|
| Route | Machining from wrought bar, 2-axis CNC turning + indexed drilling | T3 | 3 |
| Material | ASTM A479/A479M-25 Type 316 (UNS S31600), solution-annealed | T1 | 2.1 |
| Condition wording | "annealed" (A479), not "Condition A" (A276) | T1 | 2.2 |
| Annealed minima, room temperature | Tensile 515 MPa, yield 205 MPa, elong 30 %, RA 40 % | T1 | 2.1 |
| Sensitization window | 427 to 871 °C; throat runs ~530 °C | T1 | 2.3 |
| Duty scope | Short-duration / ground-test firing only | T1 | 2.3 |
| Raw stock | ⌀160 mm bar; Part 1 ~220 mm, Part 2 ~25 mm; buy ≈ 270 mm | T3 | 4 |
| Certification | EN 10204 Type 3.1 | T1 | 7 |
| Machining power | ~75 % of carbon-steel rating | T1 | 5 |
| Post-machining | Passivate per ASTM A967 | T3 | 5 |
| Thermal treatment | Full solution anneal ~1040 °C if needed; no 480 to 650 °C stress relief | T3 | 6 |
| CTQ for the shop | 4.00 mm is a protect-minimum floor | T2 / T3 | 6 |

---

## 1. Summary decisions

| # | Decision | Value | Tier |
|---|----------|-------|------|
| M-1 | Process route | **Machining from wrought bar**, 2-axis CNC turning + indexed drilling; one part = one bar | T3 (§3) |
| M-2 | Material, procurement grade | **Bar, stainless steel, ASTM A479/A479M Type 316 (UNS S31600), solution-annealed** | **T1** (§2) |
| M-3 | Condition wording | A479 designates **"annealed,"** not "Condition A" | **T1 finding** (§2.2) |
| M-4 | Service scope caveat | **Short-duration / ground-test firing only** | T1 (§2.3) |
| M-5 | Raw stock | Both parts from **⌀160 mm** A479 round bar; Part 1 ~220 mm, Part 2 ~25 mm cut length | T3 (§4) |
| M-6 | Distortion control | Rough → solution anneal **only if** distortion appears → finish. **No 480–650 °C stress relief**, it sensitizes 316 | T3 (§6) |

---

## 2. Material

### 2.1 Grade and specification

Procurement specification: **ASTM A479/A479M, Type 316, UNS S31600**, furnished **solution-annealed**. **T1.**

**Why A479 and not A276.** A479/A479M is *"Standard Specification for Stainless Steel Bars and Shapes for Use in Boilers and Other Pressure Vessels."* A276 is the general bar and shapes spec with no pressure-service intent. The nozzle wall **is** a pressure boundary, so the pressure-service bar spec is the correct call and A276 is dropped. The ASME Boiler and Pressure Vessel Code adopts this spec as **SA-479/SA-479M** in Section II, which is the same material family the package's other code references sit in.

**Grade identity matches the frozen analysis.** A479 Table 1 lists **S31600 / Type 316** at C 0.08 max, Cr 16.0–18.0, Ni 10.0–14.0, Mo 2.00–3.00, cleanly distinct from **316L (S31603, C 0.030 max)**. The frozen FEA used **316 / S31600**: its datasheet is headed S31600 and the hot yield of ~210 MPa at 530 °C matches 316, not 316L. **Drawing grade = analysis grade.** The two grades differ by roughly 10–15 % in yield, so this is not a bookkeeping detail.

**Certified minimums for annealed bar**, A479 Table 2: tensile **515 MPa (75 ksi)** min, yield **205 MPa (30 ksi)** min, elongation 30 %, reduction of area 40 %. These are the acceptance minimums the mill certificate must meet. They are *room-temperature* minima, not the 530 °C hot values used in the analysis.

### 2.2 Condition wording

A479's own condition column designates the austenitic supply condition as **"annealed,"** with strain-hardened levels as the cold-worked alternatives. **"Condition A" is ASTM A276's terminology for the same metallurgical state, not A479's.** Citing A276's label on an A479 line is a provenance mismatch a QA reviewer can flag, so the BOM reads:

> **Bar, stainless steel, ASTM A479/A479M-25 Type 316 (UNS S31600), solution-annealed condition** *(cite latest revision at order).*

The current active edition is **A479/A479M-25**. Scope, S31600 composition and annealed minima are edition-stable, and the EN 10204 3.1 mill certificate certifies to the edition current at order.

### 2.3 Service-temperature scope note

Standard 316 sits in the **427–871 °C carbide-precipitation (sensitization) window**, and the throat runs at **~530 °C**. Standard 316 is made defensible here **only** by scoping the duty to **short-duration, ground-test firing**. Sensitization is a time-at-temperature phenomenon, so a brief firing does not accumulate the grain-boundary chromium-carbide network that continuous service would.

- The **CDN-000 assembly BOM and the RFQ both carry** the qualifier: *"Short-duration / ground-test firing only. Not for continuous service in 427–871 °C."* Drawing note **N5** carries the first clause only, and takes the full qualifier at the next sheet issue.
- If sustained service were ever in scope the grade would change to **316L or 316Ti**, low-carbon or stabilized, not standard 316, and the material basis would have to be re-frozen.



## 3. Route selection: machining, casting or additive

**Selected: machining from wrought A479 bar.** Quantity basis is **1–5 prototype units** (**A-02**). The three options were weighed on the terms that actually decide a qty-1–5 pressure-boundary prototype: material-property basis, lead time, cost, and re-qualification burden against the frozen FEA.

| Route | Verdict | Reasoning |
|-------|---------|-----------|
| **Wrought bar + machining** | **SELECTED** | Certified, fully dense, near-isotropic pressure-boundary properties with an EN 10204 3.1 certificate, which is the S31600 annealed basis the FEA assumed. Shortest lead time and lowest cost at qty 1–5 for a turned axisymmetric part. **T1 basis / T3 selection.** |
| Sand or investment casting (CF8M ≈ cast 316) | Rejected | Pattern and mould tooling are uneconomic at qty 1–5. Cast structure carries porosity and lower, anisotropic properties on a pressure boundary, requiring re-qualification against the wrought FEA basis. **T3.** |
| Metal additive (L-PBF) | Rejected | Common AM stainless is **316L, not standard 316**, ~10–15 % lower yield, contradicting the frozen S31600 basis. Porosity and residual stress would need HIP plus full machining of every critical surface anyway, and the geometry has none of the internal channels or lattices AM exists to enable. **T3.** |

**Machined operations**, both parts, one setup family:

1. Face and rough-turn the OD and flange.
2. Bore and turn the internal C-D contour, the profile-controlled surface.
3. Turn the **spigot Ø92.80 g6** register on Part 1, or the recess and **register bore H7** on Part 2.
4. Face the gasket seat.
5. Index-drill the **8 × Ø9.0** bolt pattern.

Turning plus indexed drilling on a lathe with driven tools, or a mill-turn, covers the whole part. **No 5-axis and no special process is required.** **T3.**



## 4. Raw stock

The envelope drives the bar diameter, and the **flange OD Ø152** is the largest section on both parts.

| Part | Governing envelope | Stock | Cut length |
|------|--------------------|-------|-----------|
| **Part 1: Nozzle Body** | Flange OD **Ø152**; part overall, spigot tip to outlet, **203.19 mm** | **⌀160 mm** | **~220 mm** (203.19 + facing + parting/grip) |
| **Part 2, Mounting Flange** | Flange OD **Ø152**; thickness 15 mm + recess 4.5 | **⌀160 mm** | **~25 mm** |

**One bar diameter for both parts.** About 4 mm of radial cleanup on the Ø152 flange covers bar out-of-round and skin removal. A single diameter means **one bar, one heat, one mill certificate** covers the whole assembly, which is a QA simplification that also feeds the first-article and coupon plan. Buy one length of ≈ **270 mm** to yield both parts plus a test coupon from the same heat. **T3.**

**High material removal (acknowledged).** The body turns a Ø152 flange at the mount end but necks to the Ø84.8 contraction inlet with an internal C-D bore, so a large fraction of the billet becomes chip. That is inherent to machining a one-off from solid and is **accepted at qty 1–5**. It is the cost the route trades for a certified wrought pressure boundary.

**Hollow bar, not baseline.** SSINA notes hollow bar is attractive where ≥ 30 % of the centre is removed. The inlet bore qualifies, but the variable-section contour and the solid flange make a single hollow bar a poor fit. Held as a **supplier-discretion cost option**, not a spec requirement. **T3.**


## 5. SS316 machinability and shop practice

Standard 316 is **not a free-machining grade.** SSINA rates the 300-series austenitics as the **least machinable** of the common stainless family: gumminess plus a **rapid work-hardening rate**, worsened by **low thermal conductivity**, so heat concentrates at the cut.

The free-machining variants (303, 316F) buy machinability by adding sulfur or selenium, which degrades corrosion resistance, transverse ductility and weldability. That is unacceptable on a pressure boundary. So the part is made in **standard 316 and machinability is managed at the shop**:

- **Rigid setup.** Tooling and fixtures as rigid as possible, and minimise workpiece and tool overhang, because chatter drives the work-hardened glaze. Support the thin diverging section during finishing.
- **Positive feed, positive cuts, no dwelling.** Take a cut deep enough to get **under** the prior work-hardened layer. Avoid dwelling, interrupted cuts and a succession of thin skim passes: each glazes the surface and the next pass inherits a harder start.
- **Lower speeds.** Reduce cutting speed relative to carbon steel and trade speed for tool life.
- **Sharp tools, flood coolant.** Keep HSS or carbide tools sharp with a fine edge, and direct flood coolant at sufficient flow for both lubrication and heat removal. Carbide is preferred for the contour turning.
- **Power.** Expect higher cutting forces and run the machine to ~75 % of its carbon-steel power rating, not more.
- **Post-machining: passivate** (nitric acid, ASTM A967) to remove embedded free iron from tooling. This restores the chromium-oxide film on freshly cut surfaces and, with the graphite gasket, reduces the galvanic-pitting risk noted as R6 in [`gasket-spec.md`](gasket-spec.md).

All bullets above are SSINA guidance. Positive-rake tool geometry is standard austenitic practice (T3) and is not attributed to SSINA, whose wording is "positive feed / positive cuts."



## 6. Distortion and stress relief

The **4 mm** diverging-section wall is thin and distortion-prone, and austenitic bar can carry residual stress from bar production and from unbalanced roughing.

**Sequence:** rough-machine leaving finish stock → inspect for distortion → finish-machine in light, balanced passes. If distortion after roughing is unacceptable, interpose a **full solution anneal (~1040 °C plus rapid cool)** before finishing.

> **480–650 °C stress relief caveat.** That range sits inside the **427–871 °C sensitization window** and would precipitate chromium carbides, which is the exact degradation the §2.3 scope note exists to avoid. For 316 the only safe thermal treatment is a full solution anneal, not a low-temperature stress relief. At qty 1–5 with short-duration duty the **stress-relief-free strategy** (sharp tools, balanced stock removal, light finishing) is the primary path and solution anneal is the fallback. **T3.**

**What the CTQ means for the shop.** The throat wall is critical-to-quality on the basis of creep life at ~530 °C, the pressure-boundary minimum-material condition, and the manufacturing minimum, **not** on any stress-versus-thickness argument. For manufacturing that reduces to one instruction: the **4 mm is a protect-minimum floor.** Finish the thin section to hold `4 +0.3/0` without ever thinning below 4.0, which is what the light-finishing sequence above protects. **T2/T3.**



## 7. BOM material line

1.  **Bar, stainless steel, ASTM A479/A479M-25 Type 316 (UNS S31600), solution-annealed condition** *(cite latest revision at order).*
2. **Stock:** ⌀160 mm round bar.
3. **Certification:** EN 10204 Type 3.1 mill test report.
4. **Scope qualifier:** *Short-duration / ground-test firing only. Not for continuous service in 427–871 °C.*



## Sources

- **S6** ASTM A479/A479M, current edition **-25**:
    - *Standard Specification for Stainless Steel Bars and Shapes for Use in Boilers and Other Pressure Vessels*
    - §1.1 scope, §2.2 (SA-479 in ASME BPVC II), Table 1 (S31600 composition), Table 2 (annealed minima). **T1.**
- **S7** EN 10204 Type 3.1:
    - mill test certificate on the delivered heat
- **S9** SSINA:
    - *Stainless Steel for Machining* (General Guidelines, Good Shop Practices) and *Design Guidelines for the Selection and Use of Stainless Steel*
    - [ssina.com/education/fabrication](https://www.ssina.com/education/fabrication/) · [machining handbook](https://www.ssina.com/wp-content/uploads/2019/06/machining.pdf). **T1.**
- **S17** ASTM A967:
    - passivation treatment after machining
- **S11** grade and analysis basis:
    - [`ss316_properties.md`](../../docs/ss316_properties.md), S31600 and the sensitization window. **T1.**
