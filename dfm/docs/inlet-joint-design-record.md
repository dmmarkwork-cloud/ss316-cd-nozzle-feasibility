# Inlet Bolted-Joint Design Record

Every resolved decision for the inlet flange joint (register fit, gasket, bolting, flange geometry), each with its source and claim tier.

**Governing rule:** nothing is "closed" while it rests on an unconfirmed source or contradicts another live record.

**Frozen operating conditions:** Pc = **2 MPa** (working air, γ = 1.4), Tc = **800 K**; mount-end chamber bore **Ø84.80**; inlet/chamber wall ≈ **527 °C**. **(T1)**

> **Claim Tier**
> - **T1** verified against the frozen analysis
> - **T2** derivable/reproducible
> - **T3** engineering judgment, stated as such
> - **T4** strategy, never on the drawing

| Item | Value | Tier | § |
|---|---|---|---|
| Gas bore | Ø84.80 | T1 | C-1 |
| Register land | Ø92.80 = bore + 2 × 4.00 wall | T2 | C-1 |
| Register fit | H7/g6, clearance +0.012 / +0.069 | T1 | C-2 |
| Spigot projection | 4.75 mm | T3 | C-1 |
| Register engagement, seated | 2.5 mm | T3 | C-1 |
| Gasket seat | Ø92.80 → Ø112.80 flat band, R1.5 inner fillet | T3 | C-1 |
| Clearance hole | Ø9 +0.22/0 (H13) | T1 | C-3 |
| Seat finish, pilot finish | Ra 3.2 to 6.3 µm, Ra 0.8 to 1.6 µm | T2 / T3 | C-4 |
| Gasket factors | m = 2.5, y = 3000 psi | T2 | C-5 |
| Governing bolt load | 33.4 kN seating (Wm2) | T2 | C-5 |
| A286 hot yield at 527 °C | 582 MPa | T2 | C-6 |
| Fasteners | 8 × M8 A286, applied 114 MPa (20 % of hot yield) | T2 | D-1 |
| Preload | 5.7 kN/bolt = 157 MPa (27 %), torque 6.8 N·m cold | T2 | D-1 |
| Bolt circle, flange OD, thickness | Ø128, Ø152, 15 mm | T3 | D-2 |
| Bolt-pattern position | ⌀0.9 Ⓜ → A\|B | T2 | D-2 |
| Datum scheme | A = mating face, B = pilot Ø92.80, no C | T3 | D-3 |
| Cross-part concentricity | 0.060 mm against ≤ 0.10 (1.68×) | T2 / accept T3 | D-3 |

---

## 1. The joint as built

A two-part bolted inlet joint. The **nozzle body** (Part 1) carries a projecting pilot register (spigot), a flat gasket seat, and a bolt flange at the mount end. A **mounting flange ring** (Part 2) registers on the pilot and clamps the gasket. Male pilot on the body, female recess in the ring, floating fasteners.

| Feature | Value |
|---|---|
| Gas bore (ID) | **Ø84.80** |
| Spigot OD, datum B | **Ø92.80 g6**, projecting **4.75 mm** upstream → **2.5 mm** register engagement |
| Register bore, Part 2 | **Ø92.80 H7**, recess depth **4.5 mm** |
| Gasket seat | **Ø92.80 → Ø112.80** flat band (10 mm radial), Ra 3.2–6.3 µm serrated |
| Corner fillet | **R1.5** where the spigot meets the flat seat |
| Bolt circle | **Ø128** basic |
| Flange OD | **Ø152** |
| Flange thickness | **15 mm** |
| Fasteners | **8 × M8 A286**, Ø9.0 clearance holes both parts, nut behind |
| Gasket | Oxidation- and corrosion-inhibited flexible graphite, **1.5 mm**, replaceable consumable |
| Governing bolt load | **33.4 kN** (seating, Wm2) |
| Bolt-pattern position | **⌀0.9 Ⓜ → A\|B**, both parts |
| Datum scheme | **A = mating face**, **B = pilot Ø92.80**, two-datum A\|B, no C |

---

## 2. Decision Records

### C-1 · Pilot register geometry

- **Gas bore Ø84.80**, read directly from the frozen STEP (2 × 42.40 chamber radius). **T1.**
- **Register land Ø92.80** = bore + 2 × 4.00 mm frozen wall. **T2.** The 4 mm wall is the derivation input and is stated explicitly for that reason.
- **Pilot fit surface** H7/g6 at Ø92.80, ISO 286. **(T1)**
- **Spigot projection 4.75 mm → register engagement 2.5 mm**, seated:

$$E = S - g_{\text{free}} - c = 4.75 - 1.50 - 0.75 = 2.5 \text{ mm}$$

  where $S$ = spigot projection, $g_{\text{free}}$ = free gasket thickness, $c$ = recess-mouth chamfer. **(T3)**

  The spigot was originally 4.00 mm. At that length the same subtraction gives **0 mm engagement**: the pilot would never enter the bore. Caught in the CAD assembly and corrected by lengthening to 4.75.

- **Gasket seat is a flat band, no collar or shoulder.** The Ø92.80 → Ø112.80 seat is coplanar with the seating face out to the Ø152 OD. The **R1.5 fillet sits at the inner corner** between the spigot and the seat, for stress relief and machinability. Bounded **R0.8–R2**: at least a standard turning-insert nose radius, at most what preserves the 10 mm seat width. **(T3)**

---
### C-2 · Register fit, H7/g6 at Ø92.80

ISO 286-1 **80–120 mm** size step. **(T1)**

| | Hole (H7) | Shaft (g6) |
|---|---|---|
| Deviations | +0 / +35 µm | −12 / −34 µm |
| Limits | Ø92.800 / Ø92.835 | Ø92.766 / Ø92.788 |

$$c_{\min} = +0.012 \text{ mm} \qquad c_{\max} = +0.069 \text{ mm} \qquad e_{\text{pilot}} = \tfrac{1}{2}c_{\max} = 0.0345 \text{ mm}$$

Sliding/location fit, never interference, good for frequent disassembly with no galling from a press. The 0.0345 mm is the **fit contribution only**, not a total concentricity budget; the runout contribution is allocated in D-3.

---

### C-3 · Clearance hole

M8 floating fastener → **Ø9.0 (H13)**, ISO 273:1979 medium series (fine 8.4, coarse 10.0). **(T1)**

The hole carries **size limits Ø9 +0.22/0** on the sheet. A position-at-MMC hole must have them, or the ⌀0.9 Ⓜ has no maximum-material condition and no bonus.

---

### C-4 · Gasket-seat surface finish

**Ra 3.2–6.3 µm (125–250 µin), serrated / stock finish, not lapped.** Soft graphite must bite into the roughness to seal; a lapped face can weep. Measured per ASME B46.1. **(T2)**

Two different finishes on one part: the Ø92.80 g6 pilot is a sliding-fit surface and takes a **finer** Ra 0.8–1.6 µm. Do not blanket one Ra over the part.

---

### C-5 · Gasket loads: ASME BPVC VIII-1 Appendix 2

**Method, T1**, verified verbatim against the 2021 code, eq (1) and (2):

$$W_{m1} = 0.785\,G^2 P + 2b\pi G m P \qquad W_{m2} = \pi b G y$$

Effective width and reaction diameter per Table 2-5.2 (flat gasket, sketch 1a/1b): $b_0 = N/2 = 5.0$ mm, and since $b_0 \le 6$ mm, $b = b_0$ and $G$ = mean diameter = 102.8 mm.

**Factors, T2:** SIGRAFLEX APX2 HOCHDRUCK V15011W3 datasheet, ASTM columns, **m = 2.5, y = 3000 psi (20.7 N/mm²)**.

**Result:** $W_{m1}$ = 32.7 kN (operating), $W_{m2}$ = **33.4 kN (seating)** → **seating governs**. Reproduced by [`gasket_loads.py`](../calculations/gasket_loads.py). Full spec in [`gasket-spec.md`](gasket-spec.md).


---

### C-6 · Bolt material and hot capacity

- Material: **A286 (ASTM A453 Gr 660 / AMS 5732, UNS S66286)**.
- Hot **0.2 % yield ≈ 582 MPa @ 527 °C**, interpolated between 595 @ 425 °C and 580 @ 540 °C. **(T2)** This is the governing sizing basis. Source is the TorqBolt published property table for the solution-980 °C / age-720 °C condition, which is the AMS 5732 condition on the BOM; AMS 5732 itself publishes no elevated-temperature curve. These are vendor **typical** values, not guaranteed minima. A minimum basis near ~520 MPa leaves bolt sizing unaffected. See **S14**.
- **CTE = 16.9 × 10⁻⁶/°C** (21–540 °C), close to SS316 (~16.5–18), so the register fit and preload hold through the thermal cycle. **(T2)**
- **Creep negligible:** onset ~380 MPa @ 540 °C (1 %/1000 h) against a preload stress of **~157 MPa**, a factor of ~2.4 below. **(T2)**
- ASME **II-D allowable ~190 MPa** used only as a *conservative sizing screen* (1.67× cover). **Non-governing**, so the exact II-D row is not adopted and nothing published depends on it. **(T3)**
7 °C value would be an extrapolation past the rated temperature, which is not defensible.

----

### D-1 · Bolt size and count

**8 × M8 A286** on the Ø128 bolt circle.

$$A_b = 8 \times 36.6 = 293 \text{ mm}^2 \qquad A_{\text{req}} = \frac{33\,400}{190} = 176 \text{ mm}^2 \qquad \text{margin} = 1.67\times$$

$$\sigma_{\text{applied}} = \frac{33\,400}{293} = 114 \text{ MPa} = 20\% \text{ of the 582 MPa hot yield}$$

$$F_0 = \frac{1.4\,W_{m1}}{8} = 5.7 \text{ kN/bolt} \quad\Rightarrow\quad \sigma_0 = \frac{5700}{36.6} = 157 \text{ MPa} = 27\% \text{ of hot yield}$$

Bolt spacing 6.2 × d (48.98 mm chord between adjacent holes on the Ø128 circle). Sized to a **35 kN envelope** so any qualifying reinforced-graphite grade lands inside it and a gasket substitution cannot silently invalidate the calculation.

**Eight chosen over more or fewer** to serve the frequent-disassembly priority (few fasteners to service) while keeping gasket-stress distribution acceptable.

**A286 galls**, so the torque spec is set with an anti-seize k-factor, not a bare-thread table: $T = k F_0 d = 0.15 \times 5700 \times 0.008 = 6.8$ N·m cold.

### D-2 · Flange geometry

- Bolt circle **Ø128**, flange OD **Ø152**, clearance hole **Ø9**.
- Outer edge distance **12 mm = 1.5 × d** ✓. Inner bolt-hole edge to the gasket-seat band edge (Ø112.80) is **7.6 mm (< 1.5 × d)**, accepted: the seat is a **flat** band with no step, so this is a finish-zone boundary, not a structural one. **(T3)**
- **Bolt-pattern position tolerance**, floating fastener (**A-08**):

$$T = H - F = 9.0 - 8.0 = 1.0 \text{ mm at MMC}$$

  Tightened to **⌀0.9 Ⓜ** so assembly is guaranteed independent of MMC bonus: the pilot float would otherwise consume the ⌀1.0 clearance at strict MMC.

$$T_{\text{safe}} = (H - F) - 2 e_{\text{pilot}} = 1.000 - 2(0.0345) = 0.931 \;\to\; \varnothing 0.9$$

- **Flange thickness 15 mm is governed by gasket uniformity, not bending.** Bending is non-governing (FoS ≈ 6 at 15 mm). The thickness is set so the flange stays rigid enough not to bow between the 8 bolts and unload the gasket.
- The `15` from Datum A to the chamber inlet face is dimensioned **basic** on CDN-001, so the profile-of-a-surface chain has a continuous basic path from Datum A to the internal contour. The frozen `90` chamber length then stacks basic behind it. Value and basis unchanged; only the dimensioning type.

> **Method-validity flag.** The 15 mm is quantified with the TEMA bolt-spacing relation $B_{s,\max} = 2d + 6t/(m+0.5)$. TEMA is a heat-exchanger standard, used here as a recognised quantification of the general gasket-uniformity principle. That is a method-validity judgment (R5), not a nozzle-specific code, and it is flagged rather than hidden.

> **Thickness held at 15 mm at m = 2.5. DECIDED (T3).** The rule closes at m = 2.0 ($B_{s,\max}$ = 52.0 mm ≥ 50.27 mm pitch) but not at the confirmed m = 2.5 ($B_{s,\max}$ = 46.0 mm, which would ask for $t \ge 17.1$ mm). The thickness is held because TEMA is a screening proxy for gasket-stress uniformity, not a strength check, and the governing structural check is unchanged at FoS ≈ 6. The unloading it guards against is bounded by the re-torque protocol and by heating tightening the joint (+2.6 to +10.5 kN/bolt) over a short-duration ground test.
>

### D-3 · Datum scheme and cross-part concentricity

- **Two-datum A|B** (A-09). **Datum A = mating face**, primary, seats flat, controls tilt. **Datum B = pilot Ø92.80**, secondary, centres, carrying **⊥ 0.05 → A**. 
- **Alignment control = total runout** of the internal contour → A|B. Surface **T1**, value **T3**. Position of a throat axis was rejected: the throat is a contour, not a clean feature of size, so a derived axis is ill-defined.
- **Pilot locates, bolts only clamp.** The bolt-pattern position is sized by fastener clearance and does not enter the concentricity control. No redundant location.
- **Cross-part concentricity stack**, worst-case 1-D radial:

$$e_{\text{WC}} = \underbrace{0.0345}_{\text{pilot float}} + \underbrace{0.0250}_{\text{runout, }\varnothing 0.05 \text{ TIR}} = 0.0595 \approx 0.060 \text{ mm} \;\le\; 0.100 \text{ mm} \quad (1.68\times)$$

  The 0.10 mm acceptance is **T3** engineering judgment with a written basis: it holds thrust-vector cant under 0.03° over the 198.44 mm length. See [`interface-control-plan.md`](interface-control-plan.md) §5.

---

## 3. Seal selection: Path A vs Path B

The gasket seat runs at ~527 °C in working **air**. Bare flexible graphite oxidises in air above ~450–500 °C; confined in a flange with only the edges exposed, the effective limit rises to ~600 °C. At 527 °C confined, graphite is workable but life-limited by inner-edge oxidation, which forced an explicit seal decision.

| Path | Verdict | Basis |
|---|---|---|
| **A. Oxidation-inhibited flexible graphite, replaceable consumable** | **CHOSEN** | Inhibited grades are rated ~510 °C+ in air and lose ≤ 2 %/h even at 670 °C against up to 40 %/h for conventional foil. Only the inner edge sees gas, so recession is slow and inspectable. Leaves bolts, flange, register and seat finish unchanged. |
| B. Metal seal (C-ring, spring-energized, or lapped metal-to-metal) | Not chosen | Removes the oxidation life-limit, but needs a finer seat finish across the whole seat, a machined groove at tight tolerance, and different seating factors. Larger redesign, higher cost, less forgiving of surface defects. |

Path A holds provided its conditions do: an oxidation- **and** corrosion-inhibited grade, a set replacement interval, logged inner-edge recession at teardown, and the joint kept dry between tests. **Path B is the documented upgrade path** if the article ever requires a sealed-for-life joint.

---

## 4. Risk register

| # | Risk | Status and mitigation |
|---|---|---|
| R1 | **Graphite inner-edge oxidation** | Life-limiting, not sudden. Inhibited grade + consumable replacement + teardown inspection of recession. |
| R2 | **Radial thermal gradient in the flange** | Thermal hoop stress reaches SS316 hot yield if the bore-to-OD ΔT exceeds ~120 °C. Secondary and self-limiting: exceeding yield means local plasticity and shakedown, not burst. The real consequence is low-cycle thermal fatigue at the inner edge over repeated firings. **Deferred** to the analysis repo as a cyclic-life item, outside DFM scope. |
| R3 | **Gasket preload relaxation** | The real preload-loss path, not the metal. Managed by re-torque on every assembly plus gasket replacement, not set-and-forget. |
| R4 | **Differential thermal expansion, metal** | **Resolved.** SS316 members expand more than the A286 bolt, so heating *tightens* the joint (+2.6 to +10.5 kN/bolt) and bolt stress stays under yield in every case. Not a relaxation risk. |
| R5 | **Method-validity flags** | Appendix-2 m/y is a *room-temperature* seating model used at 527 °C; TEMA is a *heat-exchanger* rule used on a nozzle flange. Both are stated T3 assumptions. TEMA does not close at m = 2.5; thickness held per §D-2. |
| R6 | **Galvanic couple, graphite to SS316** | Graphite is cathodic to SS316; with moisture it can pit the flange faces. Specify a corrosion-inhibited grade and keep the joint dry between tests. |
| R7 | **Rear-nut wrench access** | Checked in the CAD assembly: the nut on the body back-face at Ø128 clears with a standard or thin-wall 13 mm socket. Inboard 8.6 mm, socket-to-socket 32 mm, outboard to flange OD 3.0 mm (4.0 thin-wall). An impact socket is marginal at 1.5 mm. |

---

## 5. Tier summary

| Item | Tier | Note |
|---|---|---|
| C-1 bore Ø84.80 | **T1** | frozen STEP read |
| C-1 register land Ø92.80 | **T2** | bore + 2 × 4 mm wall |
| C-1 engagement + datum B | **T3** | design |
| C-1 gasket seat Ø112.80 flat + R1.5 fillet | **T3** | design |
| C-2 H7/g6 deviations | **T1** | ISO 286-2, 80–120 mm step |
| C-2 pilot float 0.0345 | **T2** | fit-only |
| C-3 clearance hole Ø9 | **T1** | ISO 273 M8 medium, H13 |
| C-4 Ra 3.2–6.3 serrated | **T2** | ASME B46.1 + finish rationale |
| C-5 method, ASME App-2 | **T1** | verified verbatim vs the 2021 code |
| C-5 m, y, design load | **T2** | APX2 HOCHDRUCK datasheet → governing 33.4 kN |
| C-6 A286 hot properties | **T2** | datasheet |
| C-6 ASME II-D allowable | **T3** | non-governing conservative screen, not adopted |
| D-1 bolt sizing | **T2 / T3** | calculation / choice |
| D-2 flange geometry | **T3** | design + TEMA method flag; thickness **held at 15 mm** at m = 2.5, §D-2 |
| D-2 position tol ⌀0.9 Ⓜ | **T2** | T = (H − F) − 2·e_pilot, bonus-independent |
| D-3 datum scheme A\|B | **T3** | two-datum, no clocking |
| D-3 concentricity stack | **T3** | 0.060 mm vs ≤ 0.10 acceptance |

---

## Sources

- **S11** frozen geometry and conditions:
    - [`Geometry_Freeze_Disposition.md`](../../docs/Geometry_Freeze_Disposition.md), frozen STEP
- **S4** limits and fits:
    - ISO 286-2 (H7/g6), ISO 273 (clearance holes)
- **S5** ASME B46.1:
    - surface texture; gasket-seat Ra from gasket-handbook practice
- **S13** ASME BPVC VIII-1 Mandatory Appendix 2:
    - flange bolt-load method, eq (1)/(2), Table 2-5.2
    - gasket m/y from the SIGRAFLEX APX2 HOCHDRUCK V15011W3 datasheet
- **S14** A286 / ASTM A453 Gr 660:
    - hot yield / CTE / creep vs temperature from the TorqBolt published property table, solution-980 °C / age-720 °C condition = the AMS 5732 condition; vendor typical values, not minima. The governing sizing basis
    - AMS 5732 cited for the material spec and heat-treatment condition only; it publishes no elevated-temperature yield curve
    - ASME BPVC II-D allowable, non-governing screen, not adopted; Table Y-1 is the T1 upgrade path
- **S15** flexible-graphite oxidation limits:
    - air vs confined service, inhibited grades
