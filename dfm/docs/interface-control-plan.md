# Interface Control Plan: Two-Part Scope (Nozzle Body + Mounting Flange)

**Feeds:** [`function-analysis.md`](function-analysis.md) (interface and datums) and the datum scheme.

> **Standing rules apply**: every dimension/tolerance/fit carries a source and a claim tier (**T1 verified** · **T2 derivable/reproducible** · **T3 engineering judgment** · **T4 strategy**). GD&T is applied only where function demands it.

| Item | Value | Tier | § |
|---|---|---|---|
| Fit class | H7/g6 hole-basis locational clearance | T1 | 2 |
| Pilot size step | ISO 286-1, 80 to 120 mm | T1 | 2 |
| Hole and shaft deviations | H7 +0 / +0.035, g6 −0.012 / −0.034 | T1 | 2 |
| Clearance | +0.012 min, +0.069 max diametral | T2 | 2 |
| Pilot radial float | 0.0345 mm | T2 | 2 |
| Datum reference frame | A = mating face, B = pilot, no C | T3 | 3 |
| Fastener condition | Floating, clearance holes both parts + nut | T3 | 4 |
| Position tolerance | T = H − F = 1.0 mm at MMC, tightened to ⌀0.9 Ⓜ | T2 | 4 |
| Clearance hole | Ø9.0 (H13), ISO 273 medium | T1 | 4 |
| Cross-part concentricity | 0.0595 ≈ 0.060 mm | T2 | 5 |
| Misalignment acceptance | ≤ 0.10 mm radial | T3 | 5 |
| Thrust-vector cant at the limit | 0.029° over L = 198.44 mm | T2 | 5 |

---

## Why two parts?

One real machined-to-machined interface demonstrates what a single part can only imply: a controlled fit, a cross-part datum reference frame, a functional bolt-pattern position tolerance, and a stack-up that closes across a joint. The scope is deliberately minimal: exactly two parts, **one** pilot fit, **one** bolt pattern, no third part, and no clocking pin unless function proves it necessary.

---

## 1. The Defined Interface

> One joint. It exercises a fit, a datum scheme, a position tolerance, and a cross-part stack.

- **Part 1, Nozzle body** (primary machined part):
    1. the frozen C-D contour
    2. a short cylindrical pilot register
    3. a bolt circle at the inlet/mount end
    4. seal/mating face
- **Part 2, Mounting flange** (ring):
    1. bore that registers on the body's pilot (the locating interface)
    2. a matching bolt circle (the *clamping* interface)
    3. its own outboard face that bolts to the engine/chamber (external, represented by an interface-control note, not drawn as a third part)
- **Fasteners & gasket:**
    1. BOM lines (bolts per bolt circle; gasket/seal one line). Not detail-drawn.

## 2. Decision 1: Fit class on the pilot register

**Chosen:** hole-basis **H7/g6**, a *locational clearance* fit (ISO 286-1/-2, source **S4**). ASME B4.2 analog: Locational Clearance ~LC1–LC3.

**Function it protects:** the pilot centers the flange on the body so the throat axis stays concentric with the mount axis. It must center well and remain hand-assemblable and serviceable (no press) on a part that sees elevated temperature.

### Why H7/g6?

| Fit type | Example | Rejected because |
|---|---|---|
| Interference / transition | H7/p6, H7/n6 | Requires pressing; a hot-section flange must be removable and can't be precision-pressed. |
| Running/clearance (loose) | H8/e8, H7/f7 | Too much play; poor centering; degrades throat-to-mount concentricity, the thing the pilot exists to protect. |
| **Locational clearance** | **H7/g6** | **Small guaranteed clearance, good centering, hand assembly, feeds a bounded stack.** |

### As-designed values

Pilot **Ø92.80**, in the ISO 286-1 **80–120 mm** size step. **T1.**

| | Hole (H7) | Shaft (g6) |
|---|---|---|
| Deviations | +0 / +0.035 | −0.012 / −0.034 |
| Limits | Ø92.800 / Ø92.835 | Ø92.766 / Ø92.788 |

$$c_{\min} = 92.800 - 92.788 = +0.012 \text{ mm} \qquad c_{\max} = 92.835 - 92.766 = +0.069 \text{ mm}$$

$$e_{\text{pilot}} = \tfrac{1}{2} c_{\max} = 0.0345 \text{ mm radial float}$$

Minimum clearance is positive, so the joint never interferes and always hand-assembles.

> **Thermal note (T3):** flange and body are both SS316, so their CTEs are matched. With no large temperature *gradient* across the joint, differential growth is small and thermal binding is not the governing concern. That is *why* a snug locational clearance (g6) is acceptable rather than an oversized clearance.

## 3. Decision 2: Datum scheme

**Assembly datum reference frame (mating):**

- **Datum A, mating face** (primary):
    1. the flat seat
    2. constrains tip/orientation (3 DOF: one translation + two rotations)
- **Datum B, pilot diameter** (secondary):
    1. centers the part (2 DOF: two radial translations)
    2. the radial locator
    3. carries **⊥ 0.05 → A** so it stays square to the seat
- **Datum C, one bolt hole or clocking feature** (tertiary):
    1. **not used**
    2. would clock rotation (1 DOF), only if function needs a defined angular orientation
    3. the nozzle is axisymmetric in function and the 8-hole pattern is non-indexed, so the scheme is **two-datum A|B**

> **On over-constraint:** a rigid part must be located by **one** set of features. If the pilot fully centres the flange **and** the bolt holes are also tightly toleranced to locate, the two fight to define the same position and the bolts bind. That is redundant location.

**The design rule:** decide which feature **locates** and which merely **fastens**.

- Pilot Ø = **locator** → tight (H7/g6), becomes **datum B**.
- Bolt holes = **clamp only** → **clearance holes** with a generous **position tolerance at MMC**, referenced to A|B. The clearance + MMC bonus is the float that guarantees the bolts always pass regardless of where the pilot centered the part.

## 4. Decision 3: Bolt-pattern position tolerance

Because the bolts only clamp, their position tolerance is sized by the **fastener-clearance condition**, not pulled from thin air.

**Two cases**:

1. **Floating fastener** (bolt passes through clearance holes in *both* parts, nut behind; the default here, simplest and symmetric):
$$T = H - F$$
where:

**H** = MMC (minimum) clearance-hole Ø;

**F** = MMC (maximum) fastener Ø.

**T** = clearance hole location tolerance at MMC

> Each part gets the same T

2. **Fixed fastener** (bolt threads into the body; flange has the clearance hole; use if the body is tapped):
$$T = \frac{H - F}{2}$$

The tapped holes get an equal position tolerance **with a projected tolerance zone** equal to the flange thickness, so the bolt's *protruding* axis is controlled, not just the thread.

**Assumption A-08 (T3): floating fastener** (clearance holes both parts + nut). Chosen for simplicity and to keep threads out of the SS316 body, which avoids galling and stripped-thread repair on a frequently-disassembled prototype.

> Formula is **T2** (standard, reproducible). Hole size cites **ISO 273**: M8 medium = **Ø9.0 (H13)**, **T1**.

### As-designed value

$$T = H - F = 9.0 - 8.0 = 1.0 \text{ mm at MMC}$$

Tightened to **⌀0.9 Ⓜ** so assembly is guaranteed at strict MMC without relying on the bonus. See [`stackup.md`](stackup.md) §2.3.

### Sanity check on the MMC logic

As holes depart MMC (get larger) they earn bonus tolerance equal to the departure, which is why clearance-hole position at MMC is the correct, non-over-constraining callout. Do not use RFS here because it throws away the bonus that makes assembly robust.

---

## 5. Decision 4: Cross-part tolerance stack

This page stitches the drawings to the analysis. It is a *genuine* cross-part stack, worst-case 1-D.

**Question answered:** how far can the throat axis be from the mount axis?

**Contributors (radial):**

1. Pilot fit clearance (max) → flange radial float = $c_{\max}/2$ = **0.0345 mm**
2. Body's own throat-axis-to-pilot total runout → radial = TIR/2 = **0.0250 mm**

**Key result of the datum decision:** the **bolt-pattern position does NOT enter the concentricity stack**. The pilot governs centering, the bolts only clamp.

$$e_{\text{WC}} = 0.0345 + 0.0250 = 0.0595 \approx \mathbf{0.060 \text{ mm}}$$

$$\frac{e_{\text{acc}}}{e_{\text{WC}}} = \frac{0.100}{0.0595} = 1.68 \quad \Rightarrow \quad \textbf{PASS}$$

**Acceptance criterion (T3): throat axis within 0.10 mm radial of the mount axis.** The parent project is 2-D axisymmetric and contains no acceptable-misalignment limit, so this criterion is engineering judgment and does **not** stitch to the FEA. The analysis link is the *thickness → ΔT/stress* propagation in [`stackup.md`](stackup.md) §1. Basis for the 0.10 mm:

$$\theta_{\text{cant}} = \arctan\!\left(\frac{e}{L}\right), \qquad L = 198.44 \text{ mm (Datum A → exit plane)}$$

$$\theta\big|_{e = 0.060} = 0.017^\circ \qquad \theta\big|_{e = 0.100} = 0.029^\circ$$

The limit holds thrust-vector cant under ~0.03°, an order of magnitude inside the alignment tolerance of a realistic ground-test thrust stand. The 0.10 mm is **T3**, selected; the trigonometry is T2.

---

## 6. Assumption register additions

| ID | Assumption | Basis | Tier | Impact if wrong |
|----|-----------|-------|------|-----------------|
| A-06 | Part set = **two parts**: nozzle body + separate bolted mounting flange; gasket = BOM line | Interface competence needs one real machined-to-machined joint; minimal scope (2, not 3) | T3 | Reverts to a single part via the degrade-gracefully rule |
| A-07 | Pilot register **H7/g6** locational clearance locates the flange (datum B) | Centering + hand assembly + matched-CTE joint; ISO 286 (S4) | T3 (values T1) | Loose → concentricity degrades; interference → not serviceable |
| A-08 | Bolt pattern = **floating fastener**, position ⌀T at MMC, T = H−F | Simplest robust clamp; ISO 273 hole (S4) | T3 (formula T2) | Wrong case → holes bind or over-toleranced |
| A-09 | **Two-datum A\|B** mating scheme (add C only if clocking proven) | Axisymmetric function; avoids needless tertiary | T3 | Missing C if an indexed feature is later required |

---

## Sources

- **S1** ASME Y14.5-2018:
    - position/MMC/datum rules for §3–§4
- **S4** ISO 286-1/-2 (or ASME B4.2):
    - the pilot fit class, **80–120 mm** step, H7 = 0/+35 µm, g6 = −12/−34 µm
- **ISO 273**:
    - clearance-hole series, M8 medium = Ø9.0 (H13)
- **S10** stack-up method text:
    - worst-case 1-D method used in §5, worked in [`stackup.md`](stackup.md)
