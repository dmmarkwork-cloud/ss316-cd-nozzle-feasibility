# Tolerance Stack-Up

Three worst-case stacks close the drawing package against the frozen analysis and against assembly.

All arithmetic is reproduced by [`stackup-analysis.ipynb`](../calculations/stackup-analysis.ipynb); the summary figure is regenerated from the same primitive inputs by [`plot_stackups.ipynb`](../calculations/plot_stackups.ipynb).

![Stack-up summary](../images/stackup-summary.png)

| Stack | Question it answers | Stitches to the FEA? | Verdict |
|---|---|---|---|
| **1. Analysis-link** | Does the throat-wall tolerance band carry a structural penalty? | **Yes**, the only one that does | Band is structurally free. **PASS** |
| **2. Misalignment** | How far can the thrust axis sit off the mount axis? | **No**, acceptance is T3 judgment | 0.060 vs ≤ 0.10 mm. **PASS, 1.68×** |
| **3. Axial tip-floor** | Does the spigot tip stay clear of the recess floor so the gasket sets axial position? | No | Failed at recess 4.0, closed by deepening to 4.5. **PASS, +0.45 mm** |

> **Claim tiers:** **T1** verified against a primary or frozen source · **T2** derivable/reproducible · **T3** engineering judgment, stated as such.

| Item | Value | Tier | § |
|---|---|---|---|
| Method | Worst-case 1-D limit, not RSS | T3 | 0 |
| Throat-wall band | 4 +0.3 / 0, protect-minimum | value T1 / band T3 | 1 |
| Yield at 530.44 °C | 209.95 MPa | T2 | 1.1 |
| Stress across the band | 4.917 → 5.296 MPa, Δ 0.379 | T2 | 1.2 |
| FoS across the band | 42.7 → 39.6 | T2 | 1.2 |
| Throat temperature | 803.59 K on every case | T1 | 1.3 |
| Pilot float | 0.0345 mm radial | T2 | 2.1 |
| Runout contribution | 0.0250 mm radial (⌀0.05 TIR) | value T3 | 2.1 |
| Worst-case concentricity | 0.0595 ≈ 0.060 mm against ≤ 0.10 | T2 / accept T3 | 2.2 |
| Margin | 1.68× | T2 | 2.2 |
| Bolt position, bonus-independent | Tsafe = 0.931 → ⌀0.9 Ⓜ | T2 | 2.3 |
| Recess depth | 4.50 mm, was 4.00 | T3 | 3.2 |
| Tip-floor gap | +0.450 mm worst case, +0.750 nominal | T2 | 3.2 |
| Minimum register engagement | 2.30 mm | T2 | 3.2 |

---

## Method; why worst-case and not RSS?

**Worst-case (WC) 1-D limit stack.** Each contributor is taken to its tolerance extreme and the extremes are summed arithmetically. The result is the largest deviation the assembly can exhibit.

**Why not RSS.** Root-sum-square assumes a population of parts with known, centred, independent process distributions. This is a **qty 1–5 prototype batch** (**A-02**) with **no process-capability data**, so there is no distribution to root-sum. At this volume the defensible choice is the worst-case limit method: it guarantees every one of the ≤ 5 parts assembles and functions, at the cost of being conservative. RSS is the documented upgrade path once a production process with measured Cpk exists.

### The variant differs per stack

The worst-case family is right for the package, but the variant differs, so a blanket "1-D limit stack" label would not be accurate:

| Stack | True resultant | Method used | Note |
|---|---|---|---|
| **1** | Performance quantity from an FEA response surface. No dimensional loop. | Governing-limit identification plus sensitivity propagation at the band extremes | A propagation, not a stack |
| **2a** | Radial location magnitude, physically 2-D but the requirement is a direction-free radial zone | Worst-case reduced to a 1-D collinear sum | Exact: by the triangle inequality the maximum occurs when the vectors are collinear, which is physically reachable |
| **2b** | 2-D pattern fit under a rigid pilot translation | Worst-case 1-D per-hole check | Conservative: ignores the pattern's rigid-group float. Adequate because 2b is non-binding |
| **3** | 1-D axial clearance closing on a gap | Worst-case 1-D on the metal, bounding minimum on the gasket | Gasket treated as a bounded parameter, not a toleranced dimension |

---

## 1. Stack 1: Analysis-link, throat-wall CTQ band

This is the page that connects the drawing package to the frozen FEA. It takes the throat wall thickness (the CTQ) off the drawing with its tolerance band and propagates that band through the parent sensitivity study's own ΔT and stress results.

### 1.1 Inputs

| Input | Value | Source · tier |
|---|---|---|
| Throat wall nominal (CTQ) | **4.00 mm** | frozen geometry A-03 · **T1** |
| Tolerance band | **`4 +0.3 / −0`**, protect-minimum, unilateral | Phase-5 decision · **T3** |
| Yield strength @ 530.44 °C | **209.95 MPa** (interpolated) | sensitivity study · **T2** |

Parent sensitivity data (Dirichlet thermal BC, 2-D axisymmetric):

| t (mm) | ΔT_throat (K) | σ_vM,throat (MPa) | FoS (yield) |
|---:|---:|---:|---:|
| 3.00 | 1.33 | 3.94 | 53.3 |
| 4.00 | 2.10 | 4.92 | 42.7 |
| 5.00 | 2.71 | 6.18 | 34.0 |

### 1.2 Propagation across the band

Piecewise-linear interpolation between the bracketing sweep points:

| Wall | ΔT_throat (K) | σ_vM,throat (MPa) | FoS (yield) |
|---|---:|---:|---:|
| min = 4.00, protected floor | 2.10 | 4.92 | 42.7 |
| max = 4.30 | 2.28 | 5.30 | 39.6 |
| **Excursion across the band** | **0.18 K** | **0.38 MPa** | 42.7 → 39.6 |

$$\Delta\sigma = 5.296 - 4.917 = 0.379 \text{ MPa} \qquad \text{yield margin at the worst point} = 209.95 - 5.30 = 204.7 \text{ MPa}$$

### 1.3 Result: the band is structurally free

Across the entire tolerance band the von Mises throat stress moves by **0.38 MPa** and the yield factor of safety stays near **40**, against 204.7 MPa of yield margin remaining at the worst point. The band is nowhere near a structural limit.

The governing constraint is **creep, not yield**. The throat temperature is **803.59 K on every case** because the thermal solution pins the gas-side temperature, all cases sit above the SS316 creep threshold of ~410 °C, and creep life in this regime is insensitive to both the boundary-condition choice and the wall thickness. **The tolerance band does not move the gas-side temperature, so it cannot touch the governing limit.**

The band is therefore set by **manufacturing capability and wall-thickness inspection resolution**, not by the stress result. **PASS.**

> **Provenance guard.** The parent study establishes that the stress-versus-thickness trend in this data is a boundary-condition artifact, so it must not be quoted as evidence that a thicker or thinner wall is safer. The 0.38 MPa figure is used only to bound the excursion as negligible in either direction.

### Why `4 +0.3 / 0` and not a symmetric band

The analyzed 4.00 mm is the guaranteed minimum, so variation adds material only and the pressure boundary is never thinner than what was analyzed. The upper bound is structurally free out to 4.30, so the width is set by producibility. The throat wall is the difference of two controlled surfaces, the inner aero contour (profile 0.2 = ±0.1 on radius) and the outer wall, so its scatter stacks wider than a plain 4 mm dimension's general ±0.1; the **+0.3** absorbs that while protecting the floor.

---

## 2. Stack 2: Misalignment/Concentricity

**Question:** how far can the aerodynamic throat axis sit off the mount axis?

### 2.1 Contributors

| # | Contributor | Value (radial) | Source · tier |
|---|---|---:|---|
| 1 | Pilot fit float, Ø92.80 H7/g6, cmax = +0.069 mm diametral | **0.0345 mm** | ISO 286-2, 80–120 mm step · **T1** |
| 2 | Body throat-to-pilot total runout, ⌀0.05 TIR | **0.0250 mm** | FCF #6 · **T3 (value)** |
| | **Worst-case sum** | **0.0595 ≈ 0.060 mm** | **T2 arithmetic** |

**Fit derivation.** H7 = +0 / +0.035, g6 = −0.012 / −0.034.

$$c_{\max} = \text{(largest hole)} - \text{(smallest shaft)} = 0.035 - (-0.034) = 0.069 \text{ mm diametral}$$
$$e_{\text{pilot}} = \tfrac{1}{2} c_{\max} = 0.0345 \text{ mm radial}$$
$$c_{\min} = 0.000 - (-0.012) = +0.012 \text{ mm} > 0 \;\Rightarrow\; \text{never interference}$$

**Contributor independence.** Throat-to-pilot runout is referenced to datum B on the **body**; pilot float is the **body-to-ring** fit. Two distinct interfaces in series, independent, therefore summable.

### 2.2 Result

$$e_{\text{WC}} = 0.0345 + 0.0250 = 0.0595 \approx 0.060 \text{ mm} \qquad\text{vs}\qquad e_{\text{acc}} \le 0.10 \text{ mm}$$

$$\text{margin} = \frac{0.100}{0.0595} = 1.68 \quad \Rightarrow \quad \textbf{PASS}$$

**The bolt-pattern position deliberately does not enter this control.** The pilot locates and the bolts only clamp; including both would be redundant location.

> **The acceptance criterion is T3 judgment and this stack does not stitch to the FEA.** The parent analysis is 2-D axisymmetric and says nothing about acceptable thrust-axis misalignment. The ≤ 0.10 mm limit holds thrust-vector cant under 0.03° over the 198.44 mm length; the derivation is in [`interface-control-plan.md`](interface-control-plan.md) §5.

### 2.3 Bolt-pattern assemblability under pilot float

A reviewer will ask whether the pilot float eats into the floating-fastener clearance. Base position tolerance $T = H - F = 9.0 - 8.0 = \varnothing 1.0$.

At **strict MMC** (holes exactly Ø9, bolt exactly Ø8):

$$\text{required} = \tfrac{T}{2} + \tfrac{T}{2} + e_{\text{pilot}} = 0.500 + 0.500 + 0.0345 = 1.0345 \text{ mm}$$
$$\text{available} = 2 \times \tfrac{H-F}{2} = 1.0000 \text{ mm} \quad\Rightarrow\quad \text{overrun} = +0.0345 \text{ mm}$$

The overrun is covered by **MMC bonus** as soon as the holes depart MMC, which is trivially true at Ø9 nominal. To guarantee assembly **independent of bonus**:

$$T_{\text{safe}} = (H - F) - 2 e_{\text{pilot}} = 1.000 - 2(0.0345) = 0.931 \;\to\; \textbf{round down to } \varnothing 0.9 \text{ Ⓜ}$$

**Decision: ⌀0.9 Ⓜ → A|B on both parts.** Assembly is guaranteed at strict MMC without relying on the bonus.

> **Method caveat.** This is a conservative 1-D screen of a 2-D problem: the per-hole check ignores the pattern's rigid-group float, so it under-credits clearance and errs safe. Adequate only because the check is non-binding. If it ever governs, upgrade to a 2-D virtual-condition boundary.

---

## 3. Stack 3: Axial engagement, spigot tip to recess floor

**Question:** does the spigot tip stay clear of the recess floor at all tolerance extremes, so the **gasket** rather than metal bottoming sets the joint's axial position? Bottoming would unload the gasket and break the seal.

### 3.1 The chain

$$\text{gap} = D_{\text{recess}} - \left(S_{\text{spigot}} - g_{\text{compressed}}\right)$$

| Contributor | Nominal | Tolerance | Source · tier |
|---|---:|---:|---|
| Recess depth, Part 2 | **4.50 mm** | general ±0.10 | **T3** |
| Spigot projection, Part 1 | 4.75 mm | general ±0.10 | **T3** |
| Gasket compressed, seated | 1.00 mm | **bounded parameter**, ~1.0–1.1 mm | datasheet · **T2** |
| Recess-mouth chamfer | 0.75 mm | general ±0.10 | affects engagement, not floor gap |

> **The gasket contributor is not a tolerance.** Compressed thickness is a load-dependent material response (compression set, over-torque, relaxation) with a one-sided worst bound, thinner under more load. It is treated as a bounded parameter gated by the datasheet, not summed as a symmetric ±. The rows below apply worst-case arithmetic to the metal loop and a bounding minimum to the gasket.

### 3.2 Why the recess was deepened to 4.5

At the original recess depth of 4.00 mm:

| Case | D | S | g | Gap | |
|---|---:|---:|---:|---:|---|
| Nominal | 4.00 | 4.75 | 1.00 | **+0.250** | seats on gasket |
| Worst-case, general ±0.1 | 3.90 | 4.85 | 1.00 | **+0.050** | 50 µm, effectively zero margin |
| Worst-case + gasket over-compression | 3.90 | 4.85 | 0.90 | **−0.050** | metal bottoms; gasket unloads |

$$\text{gap}_{\text{WC}} = (4.00 - 0.10) - \big[(4.75 + 0.10) - 0.90\big] = 3.90 - 3.95 = -0.050 \text{ mm}$$

**FAIL.** Even inside the stated compressed range the gap collapses to 50 µm, and any over-torque drives it negative.

Two fixes were available:

| Fix | Change | Worst-case gap | Cost |
|---|---|---:|---|
| **A, deepen the recess** *(ADOPTED)* | 4.00 → **4.50 mm** | **+0.450 mm** | a deeper pocket into the aerodynamically benign inlet cavity; ~10.5 mm of flange wall remains behind the floor |
| B, tighten the tolerances | general ±0.10 → ±0.05 on both | +0.050 mm | still fights gasket variability; buys margin only against the metal |

$$\text{Fix A: } \text{gap}_{\text{WC}} = (4.50 - 0.10) - \big[(4.75 + 0.10) - 0.90\big] = 4.40 - 3.95 = +0.450 \text{ mm}$$

**Fix A was adopted.** It buys margin against **all** contributors including the gasket, costs nothing to machine, and does not depend on the gasket's compressed thickness. Nominal gap 0.75 mm, worst case +0.45 mm. **PASS.**

Register engagement is unaffected. It is set by spigot minus gasket minus chamfer, and stays at 2.30 mm worst case:

$$E_{\min} = (4.75 - 0.10) - 1.50 - (0.75 + 0.10) = 2.30 \text{ mm}$$

---

## 4. Summary

| Stack | Worst case | Acceptance | Verdict | Drawing consequence |
|---|---|---|---|---|
| 1 · Analysis-link | Δσ 0.38 MPa, FoS ~40 across the band | not yield-governed; creep governs | **PASS** | **`4 +0.3/0 [CTQ]`** on CDN-001 |
| 2 · Misalignment | 0.060 mm radial | ≤ 0.10 mm (T3) | **PASS 1.68×** | **⌀0.9 Ⓜ** bolt position, bonus-independent |
| 3 · Axial tip-floor | +0.45 mm | > 0, gasket sets position | **PASS** | recess **4.50** on CDN-002 |

None of the three reopens the frozen geometry or the analysis. The outcome is drawing tolerances plus one Part-2 depth change.

---

## Sources

- **S10 / M1** Fischer, *Mechanical Tolerance Stackup and Analysis*, 2nd ed. (CRC, 2011):
    - worst-case versus statistical method selection; radial and geometric stacks
- **M2** Drake (ed.), *Dimensioning and Tolerancing Handbook* (McGraw-Hill, 1999):
    - Ch. 9, worst-case §9-9, RSS §9-12, comparison of variation models §9-22, geometric tolerances §9-24
- **M3** ASME Y14.5-2018:
    - floating-fastener rule $T = H - F$, MMC bonus, virtual condition
- **M4** ASME Y14.5.1-2019:
    - mathematical position boundary, the rigorous basis for the 2-D pattern fit if Stack 2b ever binds
- **M5** ASME V&V 10-2019 / VVUQ 10.2-2021:
    - model-form uncertainty framing for the FEA behind Stack 1
- **M6** ISO/IEC Guide 98-3:2008 (GUM) + Suppl. 1:
    - interval and Monte-Carlo propagation, the formal basis for Stack 1
- **S4** ISO 286-2 / ISO 273:
    - pilot fit and clearance-hole rows
- **S11** frozen geometry and the wall-thickness sensitivity study:
    - [`Phase5b_Sensitivity_Study.md`](../../docs/Phase5b_Sensitivity_Study.md)
