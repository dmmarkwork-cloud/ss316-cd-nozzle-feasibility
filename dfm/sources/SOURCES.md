# Source Ledger

Every standard, datasheet and primary document the package rests on, with the status of each and what it is used for.

**Rule:** no dimension, tolerance, fit class or material value enters a drawing without a source and a claim tier from this ledger.

> **Claim Tier**
> - **T1** verified against the frozen analysis
> - **T2** derivable/reproducible
> - **T3** engineering judgment, stated as such
> - **T4** strategy, never on the drawing

---

## Standards and codes

| # | Source | Used for | Status |
|---|--------|----------|--------|
| **S1** | **ASME Y14.5-2018**, *Dimensioning and Tolerancing* | GD&T language, datum rules, Rule #1 envelope, feature control frames, floating-fastener rule, composite-profile behaviour (§11.6) | **RESOLVED, T1.** Working from the standard directly. |
| **S3** | ASME Y14.100 | General drawing practices, sheet format, notes | **Not adopted.** Sheet format, notes and title block follow general ASME drafting practice, self-checked against a Y14.5-aligned drawing checklist. No formal Y14.100 revision-history block is used, which is a portfolio-scope decision. Adopt one if the package moves to controlled release. |
| **S4** | **ISO 286-2** (limits and fits) + **ISO 273** (clearance holes) | Pilot fit H7/g6; M8 clearance hole | **RESOLVED, T1.** H7/g6 at the **80–120 mm** size step = 0/+35 and −12/−34 µm → clearance **+0.012 / +0.069 mm**. ISO 273:1979 M8 medium = **Ø9.0 (H13)**; fine 8.4, coarse 10.0. Verified against the reproduced tables and cross-checked to the IT-grade and fundamental-deviation formulas. |
| **S5** | **ASME B46.1** | Surface-texture callouts (Ra) | **RESOLVED.** Finish is called out on both detail sheets: general finish note plus Ra 0.8–6.3 by surface, symbols per B46.1 / Y14.36M. Ra values sourced to gasket and machinist handbook practice (T2/T3). |
| **S7** | **EN 10204 Type 3.1** | Mill test certificate in the RFQ and FAIR Form 2 | **RESOLVED, T1.** 3.1 = a certificate reporting specific test results on the delivered product, validated by the manufacturer's authorised inspection representative independent of the manufacturing department. (3.2 is the independent third-party equivalent.) |
| **S8** | **AS9102B** | First-article inspection concept and the filled FAIRs | **RESOLVED.** Forms 1–3 confirmed against the AS9102B form set. Planned FAIRs filled for all three drawings, Results blank and "FAI Not Complete", so no measured data is fabricated. |
| **S12** | Explicit title-block general-tolerance table | Control of untoleranced dimensions | **RESOLVED (A-05).** Explicit table in the title block, ASME style. ISO 2768-2 / -mK deliberately **not** used: the geometrical half is withdrawn, superseded by ISO 22081:2021. |
| **S13** | **ASME BPVC VIII-1 (2021) Mandatory Appendix 2**, §2-5 eq (1)/(2), Tables 2-5.1 and 2-5.2 | Gasket seating and operating bolt load | **RESOLVED. Method T1, factors T2.** Formulas verified verbatim against a licensed copy; *b* and *G* derived per Table 2-5.2. Factors from the SIGRAFLEX APX2 HOCHDRUCK V15011W3 datasheet, ASTM columns, **m = 2.5, y = 3000 psi** → Wm1 32.7 / Wm2 33.4 kN, seating governs. Flexible graphite is **not** in Table 2-5.1, so the factors are datasheet-sourced rather than code-tabulated. **Residuals:** 527 °C service confirmation and binding design values. |
| **S17** | **ASTM A967** | Passivation after machining, on the BOM and FAIR | **NAMED, T3.** Nitric-acid passivation removes free iron and restores the chromium-oxide film. |

## Materials

| # | Source | Used for | Status |
|---|--------|----------|--------|
| **S6** | **ASTM A479/A479M** Type 316 (S31600), annealed | Bar stock specification for the BOM | **RESOLVED, T1.** §1.1 pressure-vessel bar scope; §2.2 adopted as SA-479 in ASME BPVC II; Table 1 S31600 composition, distinct from 316L (S31603); Table 2 annealed minima 515/205 MPa. **Finding:** A479 designates the condition **"annealed,"** not "Condition A", which is A276's term. Current edition **A479/A479M-25**; scope, composition and minima are edition-stable. |
| **S14** | **A286 / ASTM A453 Gr 660** (AMS 5732, UNS S66286); hot yield from the TorqBolt published property table | Bolt material specification and hot-capacity check | **RESOLVED, T2.** Sizing is governed by the hot yield **582 MPa at 527 °C**, interpolated from 595 @ 425 °C and 580 @ 540 °C: applied stress 114 MPa (20 % of yield), preload 157 MPa (27 %). Source is the **TorqBolt published property table** for the solution-980 °C / age-720 °C condition, which is the AMS 5732 condition on the BOM; AMS 5732 itself publishes no elevated-temperature yield curve. Values are vendor **typical**, not guaranteed minima; on a minimum basis (~520 MPa) bolt sizing is unaffected and the thermal worst case moves from 76 % to ~85 % of yield. **T1 upgrade path = ASME II-D Table Y-1.** *(A previously-carried ASME II-D ~190 MPa screen has been omitted: it was never traced to a primary source and was non-governing.)* |
| **S15** | Flexible-graphite oxidation limits: SGL SIGRAFLEX, NeoGraf GraFoil, and gasket-industry sources | Seal survivability at 527 °C in air | **T2/T3.** Bare graphite ~500 °C in air, ~600 °C confined; inhibited grades rated higher. Drives the inhibited-grade and replaceable-consumable decision. |
| **S9** | **SSINA** austenitic-stainless machining guidelines | Manufacturing route justification and shop practice | **RESOLVED, T1.** *Stainless Steel for Machining* plus *Design Guidelines*. 300-series austenitics are the least machinable of the common grades: rigid setup, positive feed, no dwelling, sharp tools, flood coolant, ~75 % power. |

## Methods

| # | Source | Used for | Status |
|---|--------|----------|--------|
| **S10 / M1** | Fischer, *Mechanical Tolerance Stackup and Analysis*, 2nd ed. (CRC, 2011) | Worst-case method selection; radial and geometric stacks | **T2, method.** |
| **M2** | Drake (ed.), *Dimensioning and Tolerancing Handbook* (McGraw-Hill, 1999), Ch. 9 | Stack variants: worst-case §9-9, RSS §9-12, comparison of variation models §9-22, geometric tolerances §9-24 | **T2, method.** |
| **M3** | ASME Y14.5-2018 (= S1) | Floating-fastener T = H − F, MMC bonus, virtual condition | **T1.** |
| **M4** | ASME Y14.5.1-2019 | Mathematical position boundary, the rigorous 2-D basis for the bolt-pattern fit | **T2, method.** Named as the upgrade path if that check ever binds. |
| **M5** | ASME V&V 10-2019 / VVUQ 10.2-2021 | Model-form uncertainty framing for the FEA behind the analysis-link stack | **T2, method.** |
| **M6** | ISO/IEC Guide 98-3:2008 (GUM) + Suppl. 1 | Interval and Monte-Carlo propagation of an input tolerance through a model | **T2, method.** |
| **S16** | Timoshenko & Goodier; Boley & Weiner; Incropera; Budynas (Shigley); VDI 2230 | Thermal-gradient stress and bolted-joint thermal load, first-order analytical models | **T2.** |

## Frozen project data

| # | Source | Used for | Status |
|---|--------|----------|--------|
| **S11** | The parent analysis project: frozen geometry, wall-thickness decision, operating loads | Contour, CTQ basis, operating conditions | **FROZEN, T1.** As-built contour per [`Geometry_Freeze_Disposition.md`](../../docs/Geometry_Freeze_Disposition.md). Sealed with a SHA-256 hash manifest and a git tag. Verified consistent across the STEP, the CFD mesh, the FEA mesh and the CAD master. |

---

## Standing residuals

Two items remain open. Both are stated rather than hidden, both reduce to one manufacturer enquiry, and neither changes a drawn dimension or the bolt sizing.

| Item | Why it is open | Why the package is still defensible |
|---|---|---|
| Gasket **527 °C air rating** | The datasheet maximum is 580 °C but it says "consult manufacturer above 480 °C", and the seat runs at 527 °C | The seat is confined with only the inner edge exposed, the firing is short-duration, and the gasket is a replaceable consumable with teardown inspection of recession |
| Gasket **binding design m/y** | Published factors are "typical, non-binding" | Adequate at T2 for this package; the bolts are sized to a 35 kN envelope so any qualifying grade lands inside it |

**A note on sources not committed here.** Licensed standards (ASME BPVC, Y14.5, B46.1, ASTM) are cited by identifier and clause. Scans are deliberately not committed to this repository.
