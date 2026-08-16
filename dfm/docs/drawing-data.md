# Drawing Data Package


**Authority for geometry:** the frozen as-built contour, [`Geometry_Freeze_Disposition.md`](../../docs/Geometry_Freeze_Disposition.md) plus the frozen STEP. The drawn basic contour **is** the as-built STEP contour, not the clean nominal.

**Coordinate convention, matching the CAD:** origin at the **nominal throat**, **+x downstream** toward the exit, **−x upstream** toward the mount face. Radius `r` is from the axis, so `Ø = 2r`.

> **Claim Tier**
> - **T1** verified against the frozen analysis
> - **T2** derivable/reproducible
> - **T3** engineering judgment, stated as such
> - **T4** strategy, never on the drawing

| Item | Value | Tier | § |
|---|---|---|---|
| Drawing set | CDN-001 body · CDN-002 flange · CDN-000 assembly, Rev C (2026-08-13) | T3 | 2, 8 |
| Standards | ASME Y14.5-2018 with Rule #1 · ISO 286 · ISO 273 · ASME B46.1 | T1 | 2 |
| Sheet, projection, scale | A2, first-angle, 1:1 (throat detail 2:1) | T3 | 2 |
| Throat, as built | Ø29.884 at x −1.614; nominal Ø30.000 at x 0 is design intent | T1 | 3.1 |
| Contour angles | Converging 47.43°, diverging 14.91° | T1 | 3.2 |
| Throat blend arcs | R22.50 upstream, R5.73 downstream | T1 | 3.2 |
| Expansion, contraction ratio | 4.00, 7.99 ≈ 8:1 | T1 | 3.2 |
| Pilot Ø, Part 1 / Part 2 | Ø92.80 g6 / Ø92.80 H7 | T1 | 4, 5 |
| Spigot, engagement, recess | 4.75 mm, 2.5 mm, 4.5 mm | T3 | 4, 5 |
| Bolt holes | 8 × Ø9 +0.22/0 (H13), position ⌀0.9 Ⓜ → A\|B | T1 / T2 | 4, 5 |
| Bolt circle, flange OD, thickness | Ø128 basic, Ø152, 15 mm basic | T3 | 4, 5 |
| Throat wall, CTQ | 4 +0.3/−0, parallel to Datum A | value T1 / band T3 | 4, 6 |
| Exit plane, exit Ø | 198.44 basic, (Ø60) reference | T2 | 4 |
| Gage point | (Ø45) at (170.29 from A), reference | T2 | 4 |
| Finishes | Seat 3.2 to 6.3 · pilot 0.8 to 1.6 · contour 1.6 · general 3.2 µm | T2 / T3 | 7 |
| General tolerance | Title-block table, ±0.1 to ±0.5 by size | T3 | 7 |
| Material | ASTM A479/A479M-25 Type 316 (S31600), solution-annealed | T1 | 8, 10 |

---

## 1. Nomenclature


| Use on the drawing |  What it is |
|---|---|
| **Contraction section** *(or* **inlet plenum**)* | The integral cylindrical and converging zone upstream of the throat that is **part of Part 1**: Ø84.80 bore, ~90 mm cylinder, 47.43° cone. |
| **Chamber** | Reserved **only** for the *external* combustion and feed hardware the mounting flange bolts to. **Not drawn**, shown as an interface note. |
| **Throat** | The minimum-flow-area station, controlled by the two tangent blend arcs, not by an angle. |
| **Diverging section / bell** | Throat to exit, 14.91° straight taper. |
| **Spigot** *(male register land, Part 1, = Datum B)* | The Ø92.80 cylindrical land on the body that centres the flange. |
| **Recess** *(female, Part 2)* | The pocket in the flange that receives the spigot. |
| **Register bore** |Cylindrical wall of the recess, the female register surface the spigot OD fits against. |
| **Register** *(or* **pilot register***)* | The *fit* between spigot OD and register bore, H7/g6. A **function** (not a part). |
| **Register engagement** | Axial length over which spigot OD and register bore overlap at full Ø, the centring length. **= spigot projection − gasket gap − mouth chamfer.** |
| **Seal / mating face** ( Datum A) | The flat annular face that carries the gasket, the functional seat. |
| **Gasket seat** | The Ø92.80 → Ø112.80 **flat** annular band the gasket bears on, coplanar with the seating face out to the Ø152 OD. **No raised step.** |
| **Spigot / gasket-seat corner fillet** | There is **no** raised collar or step. The R1.5 fillet sits at the inner corner where the spigot meets the flat seat. |
| **Nozzle body** = **Part 1** | The machined C-D part: contour, wall, integral mount flange, spigot, seat. |
| **Mounting flange (ring)** = **Part 2** | The separate ring that registers on the spigot and clamps the gasket. |
| **CTQ** | Critical-to-quality feature, the **throat wall thickness**, t = 4.00 mm. |

---

## 2. Drawing set, projection, units, scale

| Item | Value | Basis · tier |
|---|---|---|
| Drawings in the set | **CDN-001** nozzle body · **CDN-002** mounting flange · **CDN-000** interface/assembly | A-06 two-part scope · T3 |
| Projection | **First-angle (ISO)**, symbol declared in the title block | T3 |
| Geometric tolerancing standard | **ASME Y14.5-2018**, **Rule #1 (envelope) applies** to features of size | S1 · note N1 |
| Units | **millimetres**, SI | STEP · T1 |
| Limits and fits | **ISO 286** (H7/g6) | S4 · **T1** |
| Clearance-hole series | **ISO 273** medium | S4 · **T1** |
| Surface texture | **ASME B46.1** (Ra) | S5 |
| General tolerances | **Explicit title-block table** (§7), **not** ISO 2768-2/-mK, which is withdrawn | A-05 · T3 |
| Sheet and scale | **A2, 1:1** on all three sheets; throat detail **2:1** on CDN-001 | T3 |

> Mixed **first-angle ISO projection** for view layout with **ASME Y14.5-2018** geometric tolerancing for the FCF language and Rule #1, and **ISO 286 / 273** for fits and holes. Its internally consistent **provided** the governing-standard note (N1) is present, because N1 is what makes Rule #1's envelope default unambiguous, and the H7/g6 pilot fit relies on that default.



## 3. Frozen Basic Geometry: Internal Gas-Side Contour

This is the **basic** geometry that the profile-of-a-surface tolerance references. All values read from the frozen STEP; the three analysis artifacts (STEP, CFD mesh, FEA mesh) agree to better than 0.1 µm.

### 3.1 Contour station table

| # | Station | x (mm) | r (mm) | Ø (mm) | Tier |
|---|---|---:|---:|---:|---|
| 1 | Inlet/mount face, contraction cylinder start | −126.72 | 42.400 | 84.80 | T1 |
| 2 | Cylinder end → converging cone start | −36.72 | 42.400 | 84.80 | T1 |
| 3 | Cone → upstream throat arc (R22.5) tangent | −18.184 | 22.221 | 44.442 | T1 |
| 4 | Throat minimum, as built | −1.614 | 14.942 | 29.884 | T1 |
| 5 | Throat nominal, design intent only, *not a controlling dimension* | 0.000 | 15.000 | 30.000 | T1 |
| 6 | Downstream throat arc (R5.73) → diverging cone tangent | +1.064 | 15.178 | 30.356 | T1 |
| 7 | Exit plane | +56.72 | 30.000 | 60.00 | T1 |

### 3.2 Angles, arcs and derived quantities

| Quantity | Value | Basis · Tier |
|---|---|---|
| Converging straight-taper half-angle | 47.43° | measured, all three sources · T1 |
| Diverging straight-taper half-angle | 14.91° | measured, all three sources · T1 |
| Diverging throat-to-exit chord angle | 14.81° | geometric · T2 |
| Upstream throat blend arc | R22.50 (= 1.5·Rt), centre (−1.614, 37.442) | measured · T1 |
| Downstream throat blend arc | R5.73 (= 0.382·Rt), centre (−0.411, 20.715) | measured · T1 |
| Outer-wall throat arcs, 4 mm radial offset | R18.50 upstream, R1.73 downstream | derived = inner − 4 · T2 |
| Contraction cylinder length | 90.00 mm at Ø84.80 | measured · T1 |
| Overall gas-path length, inlet face to exit | 183.44 mm | derived · T2 |
| Wall thickness, radial offset | 4.00 mm | design/frozen · T1 |
| Expansion ratio | ε = (30/15)² = **4.00** | T1 |
| Contraction ratio | (42.40/15)² = **7.99** ≈ 8:1 | T1 |
| Throat-area deviation, as-built vs nominal | (14.942/15.000)² − 1 = **−0.77 %** | T2 |

### 3.3 How the throat is controlled

The throat is **defined by the two tangent arcs R22.50 (upstream throat) R5.73 (downstream throat), drawn as basic geometry**. Their common tangent sits about 4.1° off the axis, which is *why* the true minimum Ø29.884 lands at x ≈ −1.614 rather than Ø30.000 at x = 0.

**Didn't place Ø30.00 size dimension at x = 0.**; it's a design intent, dispositioned use-as-is. The whole aerodynamic surface is controlled by **profile of a surface → A|B**, and the minimum throat Ø29.88 is referenced for inspection only.



## 4. Part 1: Nozzle Body

The aerodynamic contour is §3. The mount-end interface features follow.

| Feature | Nominal | Tolerance / fit | Source · Tier |
|---|---|---|---|
| Gas bore at inlet | Ø84.80 | general table | frozen STEP, 2 × 42.40 · T1 |
| Spigot OD, register surface, Datum B | Ø92.80 | g6 = −0.012 / −0.034 → Ø92.766 / 92.788 | bore + 2 × 4 mm wall; ISO 286 · **T1** |
| Spigot projection, past the body face | 4.75 mm | general ±0.10 | design · T3 |
| Register engagement, seated with gasket | 2.5 mm = 4.75 − 1.5 gasket − 0.75 mouth chamfer | verified in the CAD assembly | assembly-driven · T3 |
| Gasket seat, flat annular band | Ø92.80 → Ø112.80 (10 mm radial) | finish per §6 | design · T3 |
| Spigot / gasket-seat corner fillet | R1.5, bounded R0.8–R2 | general ±0.10 | stress relief + machinability · T3 |
| Bolt circle | Ø128 | basic | design · T3 |
| Bolt holes | 8 × Ø9.0 clearance, equally spaced on Ø128 | size +0.22 / 0 (H13); position ⌀0.9 Ⓜ → A\|B | M8 floating; ISO 273 medium · T1 |
| Mount-flange OD | Ø152 | general table | design · T3 |
| Mount-flange thickness, Datum A to chamber inlet face | 15 mm | basic | gasket-uniformity basis · T3 |
| Throat wall thickness (CTQ) | 4.00 mm | `4 +0.3 / −0`, protect minimum wall | frozen FEA · value T1 / band T3 |
| Exit plane, Datum A to theoretical sharp corner | 198.44 mm | basic, terminates the profile zone | derived · T2 |
| Exit diameter | (Ø60) | reference, falls out of the basic cone | derived · T2 |
| Gage point on the diverging cone | (Ø45) at (170.29 from A) | reference inspection anchor | derived · T2 |
| Part overall, spigot tip to outlet | 203.19 mm | stock-sizing basis | derived · T2 |

**Edge distances** (decision **D-2**). Outer edge to bolt hole is **12 mm = 1.5·d**. Inner bolt-hole edge to the gasket-seat band edge (Ø112.80) is **7.6 mm**, below 1.5·d, and is **accepted**: the seat is a **flat** band with no step, so that is a finish-zone boundary, not a structural one. **(T3)**

### Why the `15` and the `198.44` are basic dimensions?

Both are dimensioning-type decisions, not geometry changes. The `15` provides the profile-of-a-surface zone a continuous basic chain from Datum A to the first surface of the internal contour, and the frozen `90` chamber length then stacks basic behind it. The `198.44` bounds the profile zone at the outlet, so the exit Ø falls out of the basic cone and is shown reference.

The gage point stays **reference** (not basic); the diverging taper is already fully defined by the R5.73 tangent, the 14.91° basic angle and the 198.44 basic exit plane, so a basic gage point would over-define the line. It sits ~28 mm back from the edge-broken exit lip, which is hard to make and to gauge. - this was suggested by an external reviewer in Eng-Tips Forum (mfgenggear)

### Single basic authority

The sheet's basic dimensions define the contour, and note N6 reads "derived from the frozen model." There is deliberately no basic coordinate table in the notes as well as boxed basics on the face, because two definitions of one surface is a dual-authority ambiguity.


## 5. Part 2: Mounting Flange

| Feature | Nominal | Tolerance / fit | Source · Tier |
|---|---|---|---|
| Register bore, female recess | Ø92.80 | H7 = +0 / +0.035 → Ø92.800 / 92.835 | ISO 286 hole-basis · T1 |
| Recess depth | 4.5 mm | general ±0.10 | tip-floor stack · T3 |
| Register-recess corner treatment | 0.75 × 45° chamfer at the recess mouth; recess-floor internal corner R0.5–R1 | n/a | mating-corner clearance so Part 1's fillet clears and the faces seat flat, not a matching fillet · T3 |
| Bolt circle | Ø128 | basic | matches Part 1 · T3 |
| Bolt holes | 8 × Ø9.0 clearance, equally spaced | size 0.22 / 0 (H13); position ⌀0.9 Ⓜ → A\|B | M8 floating; ISO 273 · T1 |
| Bolt-hole type, both parts | Simple through-hole no thread | optional spotface on the two bolt-bearing faces to guarantee square seating | floating fastener · T3 |
| Flange OD | Ø152 | general table | matches Part 1 · T3 |
| Ring thickness | 15 mm | general table | confirmed in the assembly · T3 |
| Recess OD | Ø94.3 | general table | clears the spigot root fillet · T3 |
| Outboard face | flat, bolts to the external chamber | ∥ 0.05 → A | interface note · T3 |

**Fit result at Ø92.80**, ISO 286-1 **80–120 mm** size step:

$$c_{\min} = 92.800 - 92.788 = +0.012 \text{ mm} \qquad c_{\max} = 92.835 - 92.766 = +0.069 \text{ mm}$$
$$e_{\max} = \tfrac{1}{2} c_{\max} = 0.0345 \text{ mm radial float}$$

Never interference, so it always hand-assembles. Sliding/location fit, good for frequent disassembly. **(T1)**

**Assembly verification.** Three gates passed in the CAD assembly: no clash, rear-nut wrench access at Ø128 with a standard or thin-wall 13 mm socket, and a positive gasket-compression gap. The recess depth of 4.5 comes from the tip-floor stack, which failed worst-case at 4.0 and closes at **+0.45 mm** at 4.5.

---

## 6. Datum Scheme and FCF Schedule

**Datum frame: A** = seal/mating face, primary, seats flat and controls tilt · **B** = pilot Ø92.80, secondary, centres. **Two-datum A|B, no C.** Every FCF traces to a row of [`function-analysis.md`](function-analysis.md) §7.

| # | Feature | FCF | Value | Datum ref | Function protected | Tier |
|---|---|---|---|---|---|---|
| 1 | Internal contour, Part 1 | **⌓ Profile of a surface** | **0.2 total** (±0.1 band) | A\|B | Aerodynamic performance | surface **T1** / value **T3** |
| 2 | Throat wall, Part 1 | Dimension + tol, flagged **CTQ** | **`4 +0.3/−0`**, minimum protected, **(PARALLEL TO DATUM A)** | n/a | Creep life + pressure-boundary min-material + mfg minimum | value **T1** / band **T3** |
| 3 | Seal face, Part 1 | **⏥ Flatness** + Ra | **0.05** | n/a (form) | Gasket seal | **T3** |
| 4 | Pilot Ø, Part 1 | **Size H7/g6**, Rule #1 envelope is the control | Ø92.80 g6 | this *is* Datum B | Centres the flange | **T1** |
| 5 | Bolt pattern, both parts | **⌖ Position Ⓜ** | **⌀0.9 Ⓜ** | A\|B | Clamp, assembles without binding | **T2** |
| 6 | Throat-to-mount alignment, Part 1 | **⌰ Total runout** of the internal contour | **0.05** | A\|B | Thrust-axis alignment | surface **T1** / value **T3** |
| 7 | Pilot squareness, both parts | **⊥ Perpendicularity** | **0.05** | A | Keeps datum B square to the seat, so the pilot centres without tilting the joint | **T3** |
| 8 | Outboard face, Part 2 | **∥ Parallelism** | **0.05** | A | Keeps the external mounting face parallel to the sealed joint | **T3** |

$$\text{FCF \#5: } T = (H - F) - 2 e_{\text{pilot}} = (9.0 - 8.0) - 2(0.0345) = 0.931 \;\to\; \varnothing 0.9$$

### Unbendable Three Rules

1. **Bolt position is at MMC Ⓜ, referenced to A|B, never RFS.** The clearance plus the MMC bonus is the float that guarantees assembly after the pilot centres the part. RFS throws that bonus away.
2. **Pilot locates, bolts only clamp.** The bolt pattern does **not** enter the concentricity control. Including it would be redundant location.
3. **Total runout, not concentricity, not a throat-axis position, not composite profile.** Y14.5-2018 removed concentricity; the throat is a contour with no clean axis for position; and a composite profile's lower tier controls orientation and form, **not location**, so it would leave the throat offset at the 0.2 upper tier and the stack would fail. Total runout controls coaxiality directly.

**Cross-part concentricity stack:**

$$e_{\text{WC}} = \underbrace{0.0345}_{\text{pilot float}} + \underbrace{0.0250}_{\text{runout at } \varnothing 0.05 \text{ TIR}} = 0.060 \text{ mm} \;\le\; 0.100 \text{ mm} \quad (1.68\times)$$


## 7. Surface Finish and General Tolerance

Two different finishes on Part 1. **Do not blanket one Ra over the part.**

| Surface | Ra | Note | Tier |
|---|---|---|---|
| Gasket seat, Ø92.80 → Ø112.80 face | **3.2–6.3 µm** (125–250 µin) | Serrated / stock finish, NOT lapped. Soft graphite must bite the roughness; a lapped face weeps. | **T2** |
| Pilot register, Ø92.80 g6 | **0.8–1.6 µm** | Finer, it is a sliding-fit locating surface. | **T3** |
| Internal aero contour | **1.6 µm** | Smooth for flow. | **T3** |
| General machined surfaces | **3.2 µm** | Title-block default. | **T3** |

**General-tolerance table** (title block). Applies to any dimension without its own tolerance. **T3**, shop-standard values. The callout is this explicit table, **not** an ISO 2768 invocation.

| Linear dimension range (mm) | ± tolerance (mm) |
|---|---|
| 0.5 – 6 | 0.1 |
| > 6 – 30 | 0.2 |
| > 30 – 120 | 0.3 |
| > 120 – 400 | 0.5 |
| Angular, all | ± 0.5° |
| Broken edges / max corner radius unless noted | 0.3 |



## 8. Title block

| Field | Value |
|---|---|
| Part name | CDN-001 **CD-NOZZLE BODY** · CDN-002 **C-D NOZZLE MOUNTING FLANGE** · CDN-000 **C-D NOZZLE INLET JOINT ASSEMBLY** |
| Revision | **Rev C (2026-08-13)**. The letter advances on any controlled change to an issued sheet: **–** initial issue · **A** first external review · **B** second external review · **C** pre-release self-validation |
| Material | **Bar, stainless steel, ASTM A479/A479M-25 Type 316 (UNS S31600), solution-annealed** |
| Scale | 1:1 on A2; throat detail 2:1 |
| Units | mm |
| Projection | **First-angle**, ISO symbol shown |
| General tolerances | "UNLESS OTHERWISE SPECIFIED, SEE GENERAL-TOLERANCE TABLE" |
| Drawn by | **M. Yamanaka** |
| Sheet size | A2, each sheet 1/1 |



## 9. Drawing notes

```
N1  GEOMETRIC TOLERANCING PER ASME Y14.5-2018. RULE #1 (ENVELOPE PRINCIPLE) APPLIES.
N2  DIMENSIONS IN MILLIMETRES. FIRST-ANGLE PROJECTION.
N3  UNLESS OTHERWISE SPECIFIED, GENERAL TOLERANCES PER THE TITLE-BLOCK TABLE.
N4  MATERIAL: BAR, STAINLESS STEEL, ASTM A479/A479M-25 TYPE 316 (UNS S31600),
    SOLUTION-ANNEALED (OR LATEST REVISION AT ORDER).
N5  SCOPE: SHORT-DURATION / GROUND-TEST FIRING ONLY.
N6  INTERNAL AERODYNAMIC CONTOUR PER THE BASIC DIMENSIONS SHOWN, DERIVED FROM FROZEN MODEL;
    PROFILE ⌓0.2 A|B APPLIES TO THE INTERNAL SURFACE, INLET TO OUTLET.
N7  THROAT WALL THICKNESS IS CRITICAL-TO-QUALITY (CTQ): IT SETS THE PRESSURE-BOUNDARY
    MINIMUM-MATERIAL CONDITION, MUST SURVIVE CREEP AT THE THROAT OPERATING TEMPERATURE
    FOR THE FIRING DURATION, AND CARRIES THE MANUFACTURING MINIMUM THICKNESS.
    MINIMUM WALL SHALL BE PROTECTED.
N8  EXTERNAL WALL 4 mm NOMINAL, OFFSET FROM INTERNAL CONTOUR, GENERAL TOLERANCE;
    THROAT WALL PER CTQ.
N9  DATUM A = MATING/SEAL FACE.  DATUM B = PILOT Ø92.80 REGISTER.
N10 SURFACE TEXTURE PER ASME B46.1. UNLESS OTHERWISE SPECIFIED, ALL MACHINED SURFACES
    Ra 3.2 µm MAX.
N11 FITS PER ISO 286.  CLEARANCE HOLES PER ISO 273.
N12 GASKET AND FASTENERS ARE BOM ITEMS (NOT DETAIL-DRAWN).
N13 REMOVE ALL BURRS AND SHARP EDGES.
```

## 10. BOM

| Item | Spec | Tier |
|---|---|---|
| Part 1 and Part 2 stock | Bar, SS, ASTM A479/A479M-25 Type 316 (UNS S31600), solution-annealed; ⌀160 mm; cert EN 10204 Type 3.1 | S6/S7 · T1 |
| Fasteners, ×8 | M8 A286 (ASTM A453 Gr 660 / AMS 5732, UNS S66286), floating, clearance both parts plus nut; anti-seize k-factor torque | S14 · T2 |
| Gasket | Oxidation- and corrosion-inhibited flexible graphite, 316L SS reinforced, 1.5 mm, SIGRAFLEX APX2 HOCHDRUCK V15011W3, replaceable consumable | S13 · T2 |
| Governing bolt load | **33.4 kN** seating (Wm2). Preload F0 = 1.4·Wm1/8 = 5.7 kN/bolt → 157 MPa = **27 % of hot yield**; torque **6.8 N·m** cold | T2 · [`gasket_loads.py`](../calculations/gasket_loads.py) |

**Assembly overall length** on CDN-000 is (214.44) reference, seated = 198.44 (Datum A to exit) + 15 (flange) + 1.0 (gasket compressed). The free-gasket stack is 214.94; the 0.5 mm difference is gasket compression, and the issued sheet shows the seated figure.


## Sources

- **S1** ASME Y14.5-2018 · **S4** ISO 286 / ISO 273 · **S5** ASME B46.1 · **S6** ASTM A479 · **S7** EN 10204 · **S13** gasket m/y · **S14** A286
- **S11** frozen geometry:
    - [`Geometry_Freeze_Disposition.md`](../../docs/Geometry_Freeze_Disposition.md) and the frozen STEP
- Companion records:
    - [`inlet-joint-design-record.md`](inlet-joint-design-record.md) · [`interface-control-plan.md`](interface-control-plan.md) · [`function-analysis.md`](function-analysis.md) · [`stackup.md`](stackup.md)
- Assumptions:
    - A-05 general-tolerance table · A-06 two-part scope · A-08 floating fastener · A-09 two-datum A\|B
