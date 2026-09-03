# Gasket Specification: Inlet Joint Seal

One consolidated spec for the inlet-joint gasket, so the model, the drawing BOM and the RFQ all draw from one source.

**Item:** CDN-000 BOM item 5. **Confirmed part: SGL SIGRAFLEX APX2 HOCHDRUCK V15011W3.**

> **Claim Tier**
> - **T1** verified against the frozen analysis
> - **T2** derivable/reproducible
> - **T3** engineering judgment, stated as such
> - **T4** strategy, never on the drawing

| Item | Value | Tier | § |
|---|---|---|---|
| Grade | SIGRAFLEX APX2 HOCHDRUCK V15011W3, inhibited reinforced graphite | T2 | 1 |
| Dimensions | Ø92.8 ID × Ø112.8 OD × 1.5 mm free, plain ring | T2 | 2 |
| Compressed, seated | ~1.0 to 1.1 mm | T2 | 2 |
| Effective width (b), reaction diameter (G) | 5.0 mm, 102.8 mm | T2 | 2, 6 |
| Seat temperature | ~527 °C in air, confined | T1 | 3 |
| Governing temperature limit | 580 °C, datasheet maximum | T2 | 4 |
| Seat finish | Ra 3.2 to 6.3 µm, serrated, not lapped | T2 | 5 |
| Bolt-load method | ASME BPVC VIII-1 App. 2, eq (1) and (2) | T1 | 6 |
| Gasket factors | m = 2.5, y = 3000 psi (20.7 N/mm²) | T2 | 6 |
| Operating load Wm1 | 32.74 kN | T2 | 6 |
| Seating load Wm2 | 33.40 kN, governs | T2 | 6 |
| Seating stress delivered | 20.7 N/mm² over 1615 mm² | T2 | 6 |
| Re-torque | 5.7 kN/bolt (6.8 N·m) before every firing | T3 | 7 |
| Open residuals | 527 °C air rating, binding design m/y | n/a | 9 |

---

## 1. Type and selection

A soft flat **ring gasket** cut from **reinforced flexible graphite**, in an **oxidation- and corrosion-inhibited** grade, with a stainless insert.

**Why graphite (Path A), chosen over a metal C-ring (Path B).** It seals at low seating load, conforms to a machined face, survives the hot section, and is a cheap **replaceable consumable**. It also follows premeditated package scope of frequent-disassembly, floating-fastener design. **Path B** was rejected as a larger redesign, finer seat finish plus a machined groove plus different seating factors, disproportionate to a short-duration prototype. Path B remains the documented upgrade path if ever the project needs a sealed-for-life joint. **(T3)**

**Confirmed grade: SGL SIGRAFLEX APX2 HOCHDRUCK V15011W3**, 1.5 mm. Multilayer build: 0.5 mm APX2 oxidation-resistant flexible-graphite foils plus 0.05 mm 316L stainless foils, adhesive-free. Carries both an oxidation inhibitor and a passive corrosion inhibitor per ASTM F2168-13. The reinforcement is **smooth 316L foil**, which the spec allows alongside tanged. **T2, datasheet.**

**There are equivalents if APX2 HOCHDRUCK is unavailable**: GraFoil, SIGRAFLEX UNIVERSAL. Note that UNIVERSAL publishes EN 13555 parameters only and would need ASME-format m/y from the manufacturer before it could drop into the Appendix-2 calculation.

## 2. Dimensions

| Parameter | Value | Basis · tier |
|---|---|---|
| Inside diameter | **Ø92.8** full-seat (see §2a) | T2 |
| Outside diameter | **Ø112.8** | gasket-seat band outer · T2 |
| Thickness, free | **1.5 mm** (1/16″) | design · T3 |
| Thickness, compressed and seated | **~1.0–1.1 mm** | compressibility 37 % (ASTM F36) · T2 |
| Effective seating width, **b** | **5.0 mm** | ASME App-2, flat facing · T2 |
| Reaction (mean) diameter, **G** | **102.8 mm** | · T2 |
| Form | **Plain annular ring, no bolt holes** | OD Ø112.8 sits inside the Ø128 bolt circle, so it is a ring gasket, not full-face · T2 |

The machined **flat seat** on the parts is **Ø92.8 → Ø112.8**, 10 mm radial, coplanar to the Ø152 OD with no raised step. Only the **gasket footprint** has two options.

### 2a. Footprint options: full seat vs. fillet-cleared

The real soft-graphite gasket is cut to the **full 10 mm machined seat** and conforms over the R1.5 spigot/seat corner fillet. That is **Option A**, the design and procurement intent and the **bolt-sizing basis**. In the CAD assembly the ring is pulled in to Ø95.8 so it sits on the flat and avoids a corner clash. That is **Option B**, a modelling convenience. Both are valid; the loads differ by a few percent, always in the safe direction.

| | **Option A, full seat** *(design / procurement / sizing)* | **Option B, fillet-cleared** *(CAD model)* |
|---|---|---|
| Gasket ID | **Ø92.8** | Ø95.8 (Ø92.8 + 1.5 on radius, clears the R1.5 fillet) |
| Gasket OD | Ø112.8 | Ø112.8 |
| Radial footprint | 10 mm | 8.5 mm |
| Effective seating width, **b** | 5.0 mm | 4.25 mm |
| Reaction diameter,  **G** | 102.8 mm | 104.3 mm |
| Wm1 operating | 32.7 kN | 31.0 kN |
| Wm2 seating | **33.4 kN** *(governs)* | 28.8 kN |

**Selected**: **Option A** for bolt sizing and the flange load path. It is the conservative, real-gasket case. **Option B's** small inner-corner pocket sits on the gas side of the seal and is intended: two clean face contacts, no clash.

## 3. Operating Duty

| Condition | Value | Tier |
|---|---|---|
| Seat temperature | **~527 °C** (≈ 800 K) | T1 |
| Working medium | **Air**, γ = 1.4 | T1 |
| Chamber pressure | **2 MPa** | T1 |
| Scope | **Short-duration / ground-test firing only** | T1 |
| Seat exposure | **Confined**, only the inner edge sees the gas | T2 |

## 4. Temperature Caveat (one of the limitations)

This is the tightest margin in the joint.

The seat runs at **527 °C**. Four air ratings circulate in gasket literature and they describe different things, so only one governs here:

| Figure | Describes | Governs? |
|---|---|---|
| ~450 °C | **Bare, uninhibited** graphite in air | No, wrong material |
| ~510–525 °C | **Generic inhibited-grade** guidance, not tied to a product | No, superseded by the datasheet |
| **580 °C** | **APX2 HOCHDRUCK datasheet maximum**, the confirmed product | **Yes** |
| ~600 °C | **Confined-service** limit, edges only exposed, this joint's geometry | Yes, as the service condition |

Against the governing datasheet the seat is **below** the 580 °C maximum and **below** the ~600 °C confined limit, but **above** the datasheet's **"consult the manufacturer above 480 °C"** qualifier. That clause, not the temperature, is why a residual is carried in §9.

The margin rests on three conditions: the seat is confined with only the inner edge exposed, the firing is short-duration ground test only, and the gasket is a replaceable consumable inspected for inner-edge recession at teardown. Inhibited grades lose **≤ 2 %/h even at 670 °C** against up to 40 %/h for plain foil, so recession is slow and inspectable. **(T2/T3)**

**Open residual:** a one-line manufacturer confirmation of 527 °C service in confined air. It does not change the bolt sizing.

## 5. Mating-Seat Requirements

**Ra 3.2–6.3 µm, serrated / stock finish, NOT lapped.** Soft graphite needs a tooth-like surface to grip; a lapped seat weeps. Called out on CDN-001 and CDN-002 per ASME B46.1. Recorded as decision **C-4** in [`inlet-joint-design-record.md`](inlet-joint-design-record.md). **T2.**

> **Note** the distinction the drawing has to carry: **flat** is the seat *geometry*, **serrated** is the seat *finish*. They are not alternatives.

## 6. Gasket Factors and Bolt Loads

**Method, T1**, verified verbatim against ASME BPVC VIII-1 (2021) Mandatory Appendix 2, eq (1) and (2):

$$W_{m1} = 0.785\,G^2 P + 2b\pi G m P \qquad\text{(operating)}$$
$$W_{m2} = \pi b G y \qquad\text{(seating)}$$

Effective width and reaction diameter per Table 2-5.2, flat gasket sketch 1a/1b: $b_0 = N/2 = 5.0$ mm, and since $b_0 \le 6$ mm, $b = b_0$ and $G$ = mean diameter.

**Factors, T2**, from the APX2 HOCHDRUCK V15011W3 datasheet, **ASTM columns**: **m = 2.5, y = 3000 psi (20.7 N/mm²)**.

**Design loads, Option A:**

$$W_{m1} = 0.785(102.8)^2(2.0) + 2(5.0)\pi(102.8)(2.5)(2.0) = 16.59 + 16.15 = \mathbf{32.74 \text{ kN}}$$
$$W_{m2} = \pi(5.0)(102.8)(20.68) = \mathbf{33.40 \text{ kN}}$$
$$W_{\text{gov}} = \max(W_{m1}, W_{m2}) = \mathbf{33.4 \text{ kN}} \quad\text{seating governs, because } y \text{ is high}$$

Within the **35 kN grade-robust envelope**, so a gasket substitution among qualifying products cannot invalidate the bolt sizing.

**Seating stress check.** Delivered stress over the effective area $\pi G b$ = 1615 mm² is **20.7 N/mm²**, inside the datasheet window (minimum assembly 20, maximum 270 at 20 °C, 210 at 300 °C). Seated, not crushed. **T2.**

Reproduced by [`gasket_loads.py`](../calculations/gasket_loads.py).



### Why the factors are datasheet-sourced, not code-tabulated

Flexible graphite is not in ASME Table 2-5.1; that is the asbestos-era table, and its nearest row (mineral fiber with binder) is a different material at a different seating stress. Values of m and y are product- and thickness-specific rather than grade-independent: real reinforced-graphite products range across 2.0/2000, 2.6/2500 and 2.5/3000. The factors above therefore come from the confirmed product's datasheet, and the bolts are sized to a 35 kN envelope rather than to one vendor's number.

## 7. Handling, life and risks

| # | Item | Requirement |
|---|---|---|
| n/a | **Consumable** | Renew at each disassembly. Re-torque on reassembly: graphite consolidates, so preload relaxation is the managed loss path, not the metal. |
| R1 | Inner-edge oxidation | Life-limiting, not sudden. Inhibited grade + consumable replacement + teardown inspection of recession. |
| R3 | Preload relaxation | Managed by the re-torque protocol below plus replacement. Datasheet: residual stress ≥ 45/50 N/mm², 90 % retained after 16 h at 300 °C per **DIN 52913**; hot creep < 3 %. **T2, at 300 °C.** |
| R6 | Galvanic couple, graphite to SS316 | Graphite is **cathodic** to SS316, so with moisture it can pit the flange faces. Specify a corrosion-inhibited grade **and keep the joint dry between tests.** |

**Re-torque protocol (T3).** Re-torque all 8 bolts to assembly preload **$F_0 \approx 5.7$ kN/bolt before every firing**, verify residual, and **replace the gasket at each teardown**:

$$T = k F_0 d = 0.15 \times 5700 \text{ N} \times 0.008 \text{ m} = 6.84 \approx \mathbf{6.8 \text{ N·m} \;(60 \text{ lbf·in})} \text{ cold}$$

at a nickel-anti-seize $k \approx 0.15$. This is the CDN-000 note N1 torque.

The protocol bounds accumulated relaxation to a **single short firing**, minutes against the datasheet's 16-hour test, and the heating-induced metal tightening (+2.6 to +10.5 kN/bolt) works in the sealing direction and further offsets it.


## 8. BOM Callout: CDN-000 Item 5

Gasket, reinforced flexible graphite, oxidation- and corrosion-inhibited, 316L SS multilayer reinforcement; ring type, Ø92.8 ID × Ø112.8 OD × 1.5 mm. Confirmed part: SGL SIGRAFLEX APX2 HOCHDRUCK V15011W3 (or equivalent publishing ASME m/y and rated for the service temperature). **Replaceable consumable.**

## 9. Open residuals

Both reduce to one manufacturer enquiry. Neither changes the bolt sizing, and both are stated rather than hidden.

| Item | Status |
|---|---|
| **527 °C air rating** | Datasheet maximum is 580 °C with oxidation ≤ 2 %/h at 670 °C, but it says "consult manufacturer above 480 °C." Confined-air service at 527 °C needs a one-line confirmation. |
| **Binding design values** | The published m/y are "typical, non-binding; contact technical sales for design." Adequate for a portfolio package at T2; obtain binding values for real procurement. |

---

## Sources

- **S13** method:
    - ASME BPVC VIII-1 (2021) Mandatory Appendix 2, §2-5 eq (1)/(2), Tables 2-5.1 and 2-5.2, verified against a licensed copy (**T1**, cited by identifier; code scans are not committed to this repo)
- **S13** factors:
    - SGL SIGRAFLEX APX2 HOCHDRUCK datasheet, grade V15011W3, ASTM columns m = 2.5 / y = 3000 psi (**T2**)
    - [SIGRAFLEX APX2 datasheet](https://www.sglcarbon.com/pdf/SGL-Datasheet-SIGRAFLEX-APX2-APX-BP-B-SHL-N-Foil-US.pdf)
    - [SGL SIGRAFLEX gasket sheets](https://www.sglcarbon.com/en/markets-solutions/material/sigraflex-unreinforced-and-reinforced-graphite-gasket-sheets-made-from-flexible-graphite/)
- **S15** flexible-graphite grades and oxidation limits:
    - [NeoGraf GraFoil](https://www.neograf.com/products/gaskets-sealants/grafoil-flexible-graphite/); RAM Gaskets, Kaxite, GasketSales
- **S5** ASME B46.1:
    - surface texture for the mating seat
- **S11** frozen operating conditions:
    - [`Phase4_FEA_Summary_v3.md`](../../docs/Phase4_FEA_Summary_v3.md)
