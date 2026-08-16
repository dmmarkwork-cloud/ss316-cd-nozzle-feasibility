# Inspection Plan

How each CTQ feature is verified on the first article: acceptance criterion, method, instrument. One list feeding the drawing, the FAI and the RFQ.

**Method follows requirement type.** 3-D location against datums (position, profile, runout) uses coordinate metrology. Plain size or depth uses a handheld gauge. Thickness with no internal access uses ultrasonic. Finish uses a profilometer or Ra comparator. Flatness uses a CMM or surface plate.

**Gauge resolution** is 4 to 10 times finer than the tolerance:

$$\text{pilot g6 band} = 92.788 - 92.766 = 0.022 \text{ mm} \;\Rightarrow\; \text{resolution} \le \tfrac{0.022}{4} = 5.5\ \mu\text{m}$$
$$\text{throat wall band} = 0.30 \text{ mm} \;\Rightarrow\; \text{resolution} \le \tfrac{0.30}{10} = 30\ \mu\text{m}, \text{ met by the } 10\ \mu\text{m UT gauge}$$

> **Claim tiers:** **T1** verified against a primary source · **T2** derivable · **T3** engineering judgment.

| Item | Value | Tier | Row |
|---|---|---|---|
| Internal contour | Profile 0.2 (±0.1 radial), Ra 1.6 µm | surface T1 / value T3 | 1 |
| Exit gage point | (Ø45) at (170.29 from A), within the profile zone | ref | 1a |
| Throat wall, CTQ | Min ≥ 4.00, band 4 +0.3/0, parallel to Datum A | value T1 / band T3 | 2 |
| Throat-axis coaxiality | Total runout 0.05 (0.025 radial) | surface T1 / value T3 | 3 |
| Pilot register g6 | Ø92.766 / 92.788, Ra 0.8 to 1.6 µm | T1 | 4 |
| Register bore H7 | Ø92.800 / 92.835, clearance +0.012 / +0.069 | T1 | 5 |
| Bolt pattern | Position ⌀0.9 Ⓜ → A\|B, hole Ø9 +0.22/0 | position T2 / hole T1 | 6 |
| Spigot, recess | 4.75 mm, 4.5 mm | T3 | 7 |
| Pilot squareness | ⊥ 0.05 → A, both parts | T3 | 7a |
| Seal face | Flatness 0.05, Ra 3.2 to 6.3 µm serrated | T3 / T2 | 8 |
| Outboard face | ∥ 0.05 → A | T3 | 9 |
| General dimensions | Title-block table, ±0.1 to ±0.5 | T3 | G |
| First article | AS9102B Forms 1 to 3, 100 % inspection at qty 1 to 5 | n/a | §2, §3 |

---

## 1. CTQ Inspection Table

| # | Feature (part) | Drawing zone | Acceptance criterion (tier) | Method | Instrument |
|---|----------------|--------------|-----------------------------|--------|------------|
| 1 | Internal aero contour (Part 1) | FCF #1, profile → A\|B, frozen coord table | Profile **0.2** total (±0.1 radial); contour Ra 1.6 µm. Surface T1 / value T3 | Scan against the frozen CAD, fixtured on A\|B | CMM (scanning); profilometer for Ra |
| 1a | Exit gage point (Part 1) | `(Ø45)` at `(170.29 from A)`, reference | At the 170.29 gage plane the diverging-cone bore is **Ø45.0** nominal; accept **within the FCF #1 profile zone** (±0.1 radial). Reference anchor on the full cone, set back ~28 mm from the edge-broken exit lip. Surface T1 / value ref | Diameter at the defined axial station, a single-plane check of the profile-controlled cone | Bore gauge / inside micrometer (or CMM) |
| 2 | Throat wall thickness (Part 1) **[CTQ]** | detail C, `4 +0.3/0` | **Min wall ≥ 4.00**, band `4 +0.3/0`, measured parallel to Datum A. Basis: creep life + pressure-boundary min-material + mfg minimum. Value T1 / band T3 | Ultrasonic from the OD, there is no internal access; micrometer where reachable | UT thickness gauge (~0.01 mm); backup micrometer |
| 3 | Throat-axis coaxiality (Part 1) | FCF #6, total runout → A\|B | Total runout **0.05** (0.025 radial). Surface T1 / value T3 | Coordinate metrology in A\|B, or rotate on the datum axis and sweep an indicator | CMM (or bench centres + dial indicator) |
| 4 | Pilot register Ø92.80 g6 (**Datum B**) | FCF #4, Rule #1 envelope | g6 −0.012/−0.034 → **Ø92.766 / 92.788**; Ra 0.8–1.6 µm. **T1** | Local size plus MMC full-form envelope (Rule #1) | Micrometer + Go ring/snap gauge; profilometer |
| 5 | Register bore H7 (Part 2) | mating hole, H7/g6 fit | H7 0/+0.035 → **Ø92.800 / 92.835**; clearance +0.012/+0.069. **T1** | Internal size plus fit check | Bore gauge / inside micrometer + Go/No-Go plug gauge |
| 6 | Bolt pattern 8 × Ø9.0 (both) | FCF #5, position → A\|B | Position **⌀0.9 Ⓜ → A\|B**; hole **Ø9 +0.22/0** (H13). Position T2 / hole T1 | Coordinate metrology, MMC bonus applied | CMM (or functional gauge) |
| 7 | Spigot projection / recess depth | Part 1 spigot 4.75, Part 2 recess 4.5 | Projection **4.75**, recess **4.5**. Keeps the tip-floor gap at **+0.45 mm** worst case. T3 | Depth measurement | Depth micrometer (or CMM) |
| 7a | Pilot squareness (both parts) | FCF #7, ⊥ → A | Perpendicularity **0.05** to Datum A, on the Part 1 spigot and the Part 2 register bore. T3 | Coordinate metrology in A | CMM |
| 8 | Seal / gasket-seat face (Part 1, **Datum A**) | FCF #3, finish schedule | Flatness **0.05** (T3) + Ra **3.2–6.3 µm, serrated / stock finish, not lapped** (T2). Flat is the *geometry*, serrated is the *finish*: graphite needs tooth, a smooth face weeps | Flatness plus surface texture | CMM / surface plate + profilometer or Ra comparator |
| 9 | Outboard face (Part 2) | FCF #8, ∥ → A | Parallelism **0.05** to Datum A (T3) | Orientation against A | CMM / surface plate + indicator |
| G | General dimensions (both) | general-tolerance table | per the ± table, 0.1 to 0.5 by size. T3 | Direct | Calipers / height gauge, not CMM |

> **Inspect what function demands.** CTQs get coordinate metrology or precision gauging. General dimensions go to the title-block table with calipers, not a CMM. Rows 4, 5 and the hole in row 6 rest on printed standard rows and are **T1**. FCF numbering matches the drawing-data schedule.


## 2. First-article inspection

First article verified per **AS9102B**. Planned FAIRs are filled for all three drawings in [`../fair/`](../fair/), with **Results blank and "FAI Not Complete"** so no measured data is fabricated.


| Form | Title | Content |
|---|---|---|
| **Form 1** | Part Number Accountability | A479 Type 316 / UNS S31600 bar; heat and certificate traceability |
| **Form 2** | Product Accountability: Materials, Special Processes, Functional Testing | A479 material + EN 10204 3.1 certificate; passivation and solution anneal as special processes |
| **Form 3** | Characteristic Accountability, Verification, Compatibility Evaluation | Dimensional results for the §1 CTQ characteristics against a ballooned drawing |

**Deferred to actual manufacture, by design:** measured results, signatures, attached certificates, and the ballooned-drawing zone references in Box 6.



## 3. Duty and sampling

Quantity 1 to 5 prototype batch (**A-02**): **100 % inspection of every §1 CTQ on each article**, no sampling plan, because an AQL (Acceptable Quality Limit) needs a production run. General dimensions are verified to the title-block table.

**Scope:** short-duration / ground-test firing only. Inspection confirms as-built conformance, not service life.


## Sources

- **S1** ASME Y14.5-2018 and **S5** ASME B46.1:
    - FCFs, finish and the general-tolerance table, per [`drawing-data.md`](drawing-data.md) §6–7
- **S4** ISO 286-2 / ISO 273:
    - fit and clearance-hole rows, per [`inlet-joint-design-record.md`](inlet-joint-design-record.md) C-2 and C-3
- **S8** AS9102B:
    - first-article inspection forms
- Acceptance criteria and stack results:
    - [`stackup.md`](stackup.md)
- Material and scope:
    - [`manufacturing.md`](manufacturing.md)
