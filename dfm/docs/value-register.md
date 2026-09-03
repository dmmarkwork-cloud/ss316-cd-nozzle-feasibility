# Value Register

Every as-designed value in the package, in one table, with its source, claim tier and the document that derives it.

**Use:** look a number up here, then go to the derivation if you need the reasoning. IDs are stable across edits, so cite `value-register.md#v-pilot-fit` rather than a section number.

> **Claim Tier**
> - **T1** verified against the frozen analysis or a primary source
> - **T2** derivable/reproducible
> - **T3** engineering judgment, stated as such
> - **T4** strategy, never on the drawing

---

## 1. Frozen geometry

Authority is the frozen STEP and [`Geometry_Freeze_Disposition.md`](../../docs/Geometry_Freeze_Disposition.md). Nothing here changes without a new geometry freeze (**A-03**).

| ID | Value | Tier | Source | Derived in |
|---|---|---|---|---|
| <a id="v-contour"></a>V-CONTOUR | Station table: inlet Ø84.80 at x −126.72 · cone start x −36.72 · R22.50 tangent x −18.184 · throat min Ø29.884 at x −1.614 · R5.73 tangent x +1.064 · exit Ø60.00 at x +56.72 | T1 | S11 | [`drawing-data.md`](drawing-data.md) §3.1 |
| <a id="v-bore"></a>V-BORE | Gas bore Ø84.80 (2 × 42.40) | T1 | S11 | [`drawing-data.md`](drawing-data.md) §3.1 |
| <a id="v-angles"></a>V-ANGLES | Converging half-angle 47.43°, diverging 14.91°, chord angle 14.81° | T1 (14.81 T2) | S11 | [`drawing-data.md`](drawing-data.md) §3.2 |
| <a id="v-arcs"></a>V-ARCS | Throat blends R22.50 upstream (1.5·Rt), R5.73 downstream (0.382·Rt); outer-wall offsets R18.50 / R1.73 | T1 (offsets T2) | S11 | [`drawing-data.md`](drawing-data.md) §3.2 |
| <a id="v-ratios"></a>V-RATIOS | Expansion ε = 4.00, contraction 7.99 ≈ 8:1, throat-area deviation −0.77 % | T1 (deviation T2) | S11 | [`drawing-data.md`](drawing-data.md) §3.2 |
| <a id="v-cyl"></a>V-CYL | Contraction cylinder 90.00 mm at Ø84.80; gas path inlet face to exit 183.44 mm | T1 (183.44 T2) | S11 | [`drawing-data.md`](drawing-data.md) §3.2 |
| <a id="v-exitplane"></a>V-EXITPLANE | Exit plane 198.44 mm basic, Datum A to theoretical sharp corner | T2 | S11 | [`drawing-data.md`](drawing-data.md) §4 |
| <a id="v-gage"></a>V-GAGE | Gage point (Ø45) at (170.29 from A), reference | T2 | S11 | [`drawing-data.md`](drawing-data.md) §4 |
| <a id="v-partlen"></a>V-PARTLEN | Part overall, spigot tip to outlet, 203.19 mm | T2 | S11 | [`drawing-data.md`](drawing-data.md) §4 |

## 2. Interface geometry

| ID | Value | Tier | Source | Derived in |
|---|---|---|---|---|
| <a id="v-throat-wall"></a>V-THROAT-WALL | Throat wall 4 +0.3 / 0 mm, protect-minimum. CTQ | value T1 / band T3 | S11 | [`stackup.md`](stackup.md) §1 |
| <a id="v-spigot"></a>V-SPIGOT | Spigot projection 4.75 mm, general ±0.10 | T3 | design | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) C-1 |
| <a id="v-engagement"></a>V-ENGAGEMENT | Register engagement 2.5 mm, 2.30 mm worst case | 2.5 T3 (design) / 2.30 T2 (derived) | assembly | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) C-1 · [`stackup.md`](stackup.md) §3.2 |
| <a id="v-recess"></a>V-RECESS | Recess depth 4.5 mm, general ±0.10 | T3 | stack | [`stackup.md`](stackup.md) §3 |
| <a id="v-chamfer"></a>V-CHAMFER | Recess-mouth chamfer 0.75 × 45°; recess-floor corner R0.5 to R1 | T3 | design | [`drawing-data.md`](drawing-data.md) §5 |
| <a id="v-fillet"></a>V-FILLET | Spigot/seat corner fillet R1.5, bounded R0.8 to R2 | T3 | design | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) C-1 |
| <a id="v-gasket-seat"></a>V-GASKET-SEAT | Gasket seat Ø92.80 → Ø112.80 flat band, 10 mm radial, no step | T3 | design | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) C-1 |
| <a id="v-boltcircle"></a>V-BOLTCIRCLE | Bolt circle Ø128 basic, 8 holes equally spaced, 45° basic increment | T3 | A-01 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) D-2 |
| <a id="v-flange-od"></a>V-FLANGE-OD | Flange OD Ø152, general tolerance | T3 | design | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) D-2 |
| <a id="v-flange-t"></a>V-FLANGE-T | Flange thickness 15 mm; the Datum A to chamber inlet `15` is basic | T3 | design | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) D-2 |
| <a id="v-recess-od"></a>V-RECESS-OD | Recess OD Ø94.3, general tolerance | T3 | design | [`drawing-data.md`](drawing-data.md) §5 |
| <a id="v-edge-dist"></a>V-EDGE-DIST | Outer edge distance 12 mm = 1.5·d; inner hole edge to seat band 7.6 mm, accepted | T3 | design | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) D-2 |
| <a id="v-assy-len"></a>V-ASSY-LEN | Assembly overall (214.44) reference seated; free-gasket stack 214.94 | T2 | derived | [`drawing-data.md`](drawing-data.md) §10 |

## 3. Fits and finishes

| ID | Value | Tier | Source | Derived in |
|---|---|---|---|---|
| <a id="v-pilot-dia"></a>V-PILOT-DIA | Pilot Ø92.80 = Ø84.80 bore + 2 × 4.00 wall. This feature is Datum B | T2 | S11 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) C-1 |
| <a id="v-pilot-fit"></a>V-PILOT-FIT | H7/g6 hole-basis locational clearance (ASME B4.2 analog LC1 to LC3) | T1 | S4 | [`interface-control-plan.md`](interface-control-plan.md) §2 |
| <a id="v-iso286-step"></a>V-ISO286-STEP | ISO 286-1 size step 80 to 120 mm | T1 | S4 | [`../sources/SOURCES.md`](../sources/SOURCES.md) S4 |
| <a id="v-pilot-limits"></a>V-PILOT-LIMITS | H7 = +0 / +0.035 → Ø92.800 / Ø92.835 · g6 = −0.012 / −0.034 → Ø92.766 / Ø92.788 | T1 | S4 | [`interface-control-plan.md`](interface-control-plan.md) §2 |
| <a id="v-pilot-clear"></a>V-PILOT-CLEAR | Clearance +0.012 min, +0.069 max diametral | T2 | S4 | [`interface-control-plan.md`](interface-control-plan.md) §2 |
| <a id="v-pilot-float"></a>V-PILOT-FLOAT | Pilot radial float 0.0345 mm | T2 | S4 | [`interface-control-plan.md`](interface-control-plan.md) §2 |
| <a id="v-bolt-hole"></a>V-BOLT-HOLE | 8 × Ø9.0 clearance hole, size +0.22 / 0 (H13), ISO 273 medium | T1 | S4 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) C-3 |
| <a id="v-ra-seat"></a>V-RA-SEAT | Gasket seat Ra 3.2 to 6.3 µm, serrated, not lapped | T2 | S5 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) C-4 |
| <a id="v-ra-pilot"></a>V-RA-PILOT | Pilot Ra 0.8 to 1.6 µm · contour 1.6 µm · general machined 3.2 µm | T3 | S5 | [`drawing-data.md`](drawing-data.md) §7 |
| <a id="v-gen-tol"></a>V-GEN-TOL | Title-block table: ±0.1 (0.5 to 6) · ±0.2 (>6 to 30) · ±0.3 (>30 to 120) · ±0.5 (>120 to 400) · angular ±0.5° · broken edges 0.3 | T3 | S12 | [`drawing-data.md`](drawing-data.md) §7 |

Fit derivation:

$$c_{\min} = 92.800 - 92.788 = +0.012 \text{ mm} \qquad c_{\max} = 92.835 - 92.766 = +0.069 \text{ mm}$$

$$e_{\text{pilot}} = \tfrac{1}{2} c_{\max} = 0.0345 \text{ mm radial}$$

## 4. GD&T controls

FCF numbering is canonical across the package. Frames 7 and 8 were appended so earlier "FCF #n" citations stay valid. Append only.

| ID | Value | Tier | Source | Derived in |
|---|---|---|---|---|
| <a id="v-fcf1-profile"></a>V-FCF1-PROFILE | FCF #1 internal contour, profile of a surface ⌓ 0.2 → A\|B | surface T1 / value T3 | S1 | [`function-analysis.md`](function-analysis.md) §3 |
| <a id="v-fcf2-ctq"></a>V-FCF2-CTQ | FCF #2 throat wall, 4 +0.3/−0, CTQ, parallel to Datum A | value T1 / band T3 | S11 | [`function-analysis.md`](function-analysis.md) §4 |
| <a id="v-fcf3-flatness"></a>V-FCF3-FLATNESS | FCF #3 seal face, flatness ⏥ 0.05 + Ra | T3 | S1, S5 | [`function-analysis.md`](function-analysis.md) §2 |
| <a id="v-fcf4-pilot"></a>V-FCF4-PILOT | FCF #4 pilot Ø, size H7/g6, Rule #1 envelope. This feature is Datum B | T1 | S1, S4 | [`function-analysis.md`](function-analysis.md) §5 |
| <a id="v-fcf5-position"></a>V-FCF5-POSITION | FCF #5 bolt pattern, position ⌖ ⌀0.9 Ⓜ → A\|B, both parts | T2 | S1, M3 | [`interface-control-plan.md`](interface-control-plan.md) §4 |
| <a id="v-fcf6-runout"></a>V-FCF6-RUNOUT | FCF #6 throat-to-mount, total runout ⌰ 0.05 → A\|B (0.025 radial) | surface T1 / value T3 | S1 | [`function-analysis.md`](function-analysis.md) §3 |
| <a id="v-fcf7-perp"></a>V-FCF7-PERP | FCF #7 pilot squareness, ⊥ 0.05 → A, both parts | T3 | S1 | [`function-analysis.md`](function-analysis.md) §7 |
| <a id="v-fcf8-para"></a>V-FCF8-PARA | FCF #8 flange outboard face, ∥ 0.05 → A, Part 2 | T3 | S1 | [`function-analysis.md`](function-analysis.md) §7 |
| <a id="v-datum"></a>V-DATUM | Datum frame A\|B: A = seal face (3 DOF), B = pilot Ø92.80 (2 DOF). No datum C | T3 | S1 | [`interface-control-plan.md`](interface-control-plan.md) §3 |
| <a id="v-tsafe"></a>V-TSAFE | T = H − F = 1.0 mm at MMC, tightened to Tsafe = 0.931 → ⌀0.9 Ⓜ | formula T2 / hole T1 | M3, S4 | [`stackup.md`](stackup.md) §2.3 |

$$T = H - F = 9.0 - 8.0 = 1.0 \text{ mm at MMC} \qquad T_{\text{safe}} = (H - F) - 2\,e_{\text{pilot}} = 0.931 \;\to\; \varnothing 0.9$$

## 5. Fasteners and preload

| ID | Value | Tier | Source | Derived in |
|---|---|---|---|---|
| <a id="v-bolt-spec"></a>V-BOLT-SPEC | 8 × M8 A286 (ASTM A453 Gr 660 / AMS 5732, UNS S66286), floating, nut behind | T2 (count T3) | S14 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) D-1 |
| <a id="v-bolt-area"></a>V-BOLT-AREA | Tensile stress area 36.6 mm² per bolt, Ab = 293 mm² for 8 | T2 | S14 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) D-1 |
| <a id="v-hot-yield"></a>V-HOT-YIELD | A286 hot 0.2 % yield 582 MPa at 527 °C, between 595 @ 425 °C and 580 @ 540 °C. Vendor typical, not minima | T2 | S14 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) C-6 |
| <a id="v-a286-cte"></a>V-A286-CTE | A286 CTE 16.9 × 10⁻⁶/°C (21 to 540 °C) against SS316 ~16.5 to 18 | T2 | S14 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) C-6 |
| <a id="v-a286-creep"></a>V-A286-CREEP | Creep onset ~380 MPa at 540 °C (1 %/1000 h) | T2 | S14 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) C-6 |
| <a id="v-applied"></a>V-APPLIED | Applied bolt stress 114 MPa = 20 % of hot yield | T2 | derived | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) D-1 |
| <a id="v-preload"></a>V-PRELOAD | Preload F0 = 1.4·Wm1/8 = 5.7 kN/bolt → 157 MPa = 27 % of hot yield (45.8 kN total) | T2 | derived | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) D-1 |
| <a id="v-torque"></a>V-TORQUE | Torque T = k·F0·d = 6.8 N·m (60 lbf·in) cold at nickel anti-seize k ≈ 0.15 | T2 | derived | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) D-1 |
| <a id="v-thermal-tighten"></a>V-THERMAL-TIGHTEN | Heating tightens the joint by +2.6 to +10.5 kN/bolt | T2 | S16 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) R4 |
| <a id="v-bolt-pitch"></a>V-BOLT-PITCH | Bolt pitch on Ø128: 48.98 mm chord, 50.27 mm arc | T2 | derived | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) D-1, D-2 |
| <a id="v-wrench"></a>V-WRENCH | Rear-nut access at Ø128 with a 13 mm socket: inboard 8.6 mm, socket-to-socket 32 mm, outboard to flange OD 3.0 mm (4.0 thin-wall) | T2 | CAD | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) R7 |

$$A_b = 8 \times 36.6 = 293 \text{ mm}^2 \qquad \sigma_{\text{applied}} = \frac{33\,400}{293} = 114 \text{ MPa}$$

$$F_0 = \frac{1.4\,W_{m1}}{8} = 5.7 \text{ kN/bolt} \quad\Rightarrow\quad \sigma_0 = \frac{5700}{36.6} = 157 \text{ MPa} \qquad T = k F_0 d = 6.84 \approx 6.8 \text{ N·m}$$

## 6. Gasket

| ID | Value | Tier | Source | Derived in |
|---|---|---|---|---|
| <a id="v-gasket-grade"></a>V-GASKET-GRADE | SGL SIGRAFLEX APX2 HOCHDRUCK V15011W3, oxidation- and corrosion-inhibited reinforced graphite, 0.5 mm APX2 foils + 0.05 mm 316L foils, per ASTM F2168-13 | T2 | S13, S15 | [`gasket-spec.md`](gasket-spec.md) §1 |
| <a id="v-gasket-dims"></a>V-GASKET-DIMS | Ø92.8 ID × Ø112.8 OD × 1.5 mm free, plain annular ring | T2 (thickness T3) | S13 | [`gasket-spec.md`](gasket-spec.md) §2 |
| <a id="v-gasket-comp"></a>V-GASKET-COMP | Compressed seated ~1.0 to 1.1 mm, compressibility 37 % (ASTM F36). Bounded parameter, not a tolerance | T2 | S13 | [`stackup.md`](stackup.md) §3 |
| <a id="v-bg"></a>V-BG | Effective seating width b = 5.0 mm, reaction diameter G = 102.8 mm | T2 | S13 | [`gasket-spec.md`](gasket-spec.md) §6 |
| <a id="v-my"></a>V-MY | Gasket factors m = 2.5, y = 3000 psi (20.7 N/mm²), datasheet ASTM columns | T2 | S13 | [`gasket-spec.md`](gasket-spec.md) §6 |
| <a id="v-wm1"></a>V-WM1 | Wm1 = 32.74 kN operating (H 16.59 + Hp 16.15) | T2 (method T1) | S13 | [`gasket-spec.md`](gasket-spec.md) §6 |
| <a id="v-wm2"></a>V-WM2 | Wm2 = 33.40 kN seating. Wgov = 33.4 kN, seating governs | T2 (method T1) | S13 | [`gasket-spec.md`](gasket-spec.md) §6 |
| <a id="v-envelope"></a>V-ENVELOPE | Bolt sizing envelope 35 kN | T3 | design | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) D-1 |
| <a id="v-seat-stress"></a>V-SEAT-STRESS | Delivered seating stress 20.7 N/mm² over πGb = 1615 mm², against a 20 to 270 N/mm² datasheet window | T2 | S13 | [`gasket-spec.md`](gasket-spec.md) §6 |
| <a id="v-gasket-temp"></a>V-GASKET-TEMP | 580 °C governs (datasheet max). Also in circulation: ~450 °C bare, ~510 to 525 °C generic inhibited, ~600 °C confined | T2 | S13, S15 | [`gasket-spec.md`](gasket-spec.md) §4 |
| <a id="v-gasket-relax"></a>V-GASKET-RELAX | Residual stress ≥ 45/50 N/mm², 90 % retained after 16 h at 300 °C (DIN 52913); oxidation ≤ 2 %/h at 670 °C for inhibited grades | T2 | S13, S15 | [`gasket-spec.md`](gasket-spec.md) §7 |

$$W_{m1} = 0.785\,G^2 P + 2b\pi G m P = 16.59 + 16.15 = 32.74 \text{ kN} \qquad W_{m2} = \pi b G y = 33.40 \text{ kN}$$

## 7. Material and stock

| ID | Value | Tier | Source | Derived in |
|---|---|---|---|---|
| <a id="v-material"></a>V-MATERIAL | Bar, ASTM A479/A479M-25 Type 316 (UNS S31600), solution-annealed | T1 | S6 | [`manufacturing.md`](manufacturing.md) §2 |
| <a id="v-condition"></a>V-CONDITION | Condition wording is "annealed" (A479), not "Condition A" (A276) | T1 | S6 | [`manufacturing.md`](manufacturing.md) §2.2 |
| <a id="v-minima"></a>V-MINIMA | A479 Table 2 annealed minima: tensile 515 MPa, yield 205 MPa, elongation 30 %, RA 40 %, at room temperature | T1 | S6 | [`manufacturing.md`](manufacturing.md) §2.1 |
| <a id="v-grade-id"></a>V-GRADE-ID | S31600: C 0.08 max, Cr 16.0 to 18.0, Ni 10.0 to 14.0, Mo 2.00 to 3.00. Distinct from 316L (S31603, C 0.030 max) | T1 | S6, S11 | [`manufacturing.md`](manufacturing.md) §2.1 |
| <a id="v-sensitization"></a>V-SENSITIZATION | Carbide-precipitation window 427 to 871 °C | T1 | S11 | [`manufacturing.md`](manufacturing.md) §2.3 |
| <a id="v-stock"></a>V-STOCK | ⌀160 mm round bar; Part 1 cut ~220 mm, Part 2 ~25 mm; buy ≈ 270 mm | T3 | S6 | [`manufacturing.md`](manufacturing.md) §4 |
| <a id="v-cert"></a>V-CERT | EN 10204 Type 3.1 mill test report on the delivered heat | T1 | S7 | [`../sources/SOURCES.md`](../sources/SOURCES.md) S7 |
| <a id="v-passivation"></a>V-PASSIVATION | ASTM A967 nitric-acid passivation after machining | T3 | S17 | [`manufacturing.md`](manufacturing.md) §5 |
| <a id="v-anneal"></a>V-ANNEAL | Distortion fallback is a full solution anneal ~1040 °C plus rapid cool. No 480 to 650 °C stress relief | T3 | S6, S11 | [`manufacturing.md`](manufacturing.md) §6 |
| <a id="v-power"></a>V-POWER | Machine to ~75 % of carbon-steel power rating | T1 | S9 | [`manufacturing.md`](manufacturing.md) §5 |

## 8. Operating conditions

| ID | Value | Tier | Source | Derived in |
|---|---|---|---|---|
| <a id="v-pc"></a>V-PC | Chamber pressure 2 MPa, working air, γ = 1.4 | T1 | S11 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) header |
| <a id="v-tc"></a>V-TC | Chamber temperature 800 K | T1 | S11 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) header |
| <a id="v-seat-temp"></a>V-SEAT-TEMP | Inlet wall and gasket seat ≈ 527 °C | T1 | S11 | [`inlet-joint-design-record.md`](inlet-joint-design-record.md) header |
| <a id="v-throat-temp"></a>V-THROAT-TEMP | Throat operating point 803.59 K (~530 °C), identical on every wall-thickness case | T1 | S11 | [`stackup.md`](stackup.md) §1.3 |
| <a id="v-hot-yield-316"></a>V-HOT-YIELD-316 | SS316 yield at 530.44 °C = 209.95 MPa; creep threshold ~410 °C | T2 | S11 | [`stackup.md`](stackup.md) §1.1 |
| <a id="v-sensitivity"></a>V-SENSITIVITY | Parent sweep: t 3.00 → ΔT 1.33 K, σ 3.94 MPa, FoS 53.3 · t 4.00 → 2.10, 4.92, 42.7 · t 5.00 → 2.71, 6.18, 34.0 | T2 | S11 | [`stackup.md`](stackup.md) §1.1 |
| <a id="v-scope"></a>V-SCOPE | Short-duration / ground-test firing only, not for continuous service in 427 to 871 °C. Qty 1 to 5 (A-02) | T1 (qty T4) | S11 | [`project-workflow.md`](project-workflow.md) §4 |

## 9. Stack results

| ID | Value | Tier | Source | Derived in |
|---|---|---|---|---|
| <a id="v-stack1"></a>V-STACK1 | Across the band: Δσ = 5.296 − 4.917 = 0.379 MPa, ΔT 0.18 K, FoS 42.7 → 39.6, yield margin 204.7 MPa. PASS | T2 | S11, M6 | [`stackup.md`](stackup.md) §1.2 |
| <a id="v-eacc"></a>V-EACC | Misalignment acceptance ≤ 0.10 mm radial. Does not stitch to the FEA | T3 | judgment | [`interface-control-plan.md`](interface-control-plan.md) §5 |
| <a id="v-cant"></a>V-CANT | Thrust-vector cant over L = 198.44 mm: 0.017° at e = 0.060, 0.029° at e = 0.100 | T2 | derived | [`interface-control-plan.md`](interface-control-plan.md) §5 |
| <a id="v-stack2"></a>V-STACK2 | eWC = 0.0345 + 0.0250 = 0.0595 ≈ 0.060 mm against ≤ 0.10. PASS, 1.68× | T2 | derived | [`stackup.md`](stackup.md) §2.2 |
| <a id="v-stack2b"></a>V-STACK2B | At strict MMC: required 1.0345 mm, available 1.0000 mm, overrun +0.0345 mm, covered by MMC bonus | T2 | M3 | [`stackup.md`](stackup.md) §2.3 |
| <a id="v-stack3"></a>V-STACK3 | Tip-floor gap: −0.050 mm at recess 4.0 (fail), +0.450 mm worst case and +0.750 nominal at 4.5. PASS | T2 | derived | [`stackup.md`](stackup.md) §3 |
| <a id="v-fixb"></a>V-FIXB | Rejected Fix B, tightening general ±0.10 → ±0.05: worst-case gap +0.050 mm only | T2 | derived | [`stackup.md`](stackup.md) §3.2 |

$$e_{\text{WC}} = 0.0345 + 0.0250 = 0.0595 \approx 0.060 \text{ mm} \qquad \frac{0.100}{0.0595} = 1.68\times$$

$$\text{gap} = D_{\text{recess}} - (S_{\text{spigot}} - g_{\text{compressed}}) = (4.50 - 0.10) - [(4.75 + 0.10) - 0.90] = +0.450 \text{ mm}$$

---

## Sources

- **S1** ASME Y14.5-2018:
    - FCF language, datum rules, Rule #1, floating-fastener rule, §11.6 composite profile
- **S4** ISO 286-1/-2 and ISO 273:
    - pilot fit class, 80 to 120 mm step, H7 = 0/+35 µm, g6 = −12/−34 µm, M8 medium clearance hole Ø9.0 (H13)
- **S5** ASME B46.1:
    - surface-texture callouts
- **S6** ASTM A479/A479M-25:
    - bar specification, S31600 composition, annealed minima, condition wording
- **S7** EN 10204 Type 3.1:
    - mill test certificate
- **S9** SSINA:
    - austenitic machining guidance
- **S11** frozen geometry and analysis:
    - [`Geometry_Freeze_Disposition.md`](../../docs/Geometry_Freeze_Disposition.md)
    - [`Phase5b_Sensitivity_Study.md`](../../docs/Phase5b_Sensitivity_Study.md)
    - [`ss316_properties.md`](../../docs/ss316_properties.md)
- **S12** title-block general-tolerance table
- **S13** ASME BPVC VIII-1 Mandatory Appendix 2 and the SIGRAFLEX APX2 HOCHDRUCK V15011W3 datasheet:
    - eq (1)/(2), Table 2-5.2, m and y factors
- **S14** A286 / ASTM A453 Gr 660:
    - hot yield, CTE, creep
- **S15** flexible-graphite oxidation limits
- **S16** thermal-gradient and bolted-joint thermal load references
- **S17** ASTM A967 passivation
- **M3** ASME Y14.5-2018 floating-fastener rule, MMC bonus, virtual condition
- **M6** ISO/IEC Guide 98-3:2008 (GUM)
- Source status: [`../sources/SOURCES.md`](../sources/SOURCES.md)
- Reproducing scripts: [`gasket_loads.py`](../calculations/gasket_loads.py) · [`stackup-analysis.py`](../calculations/stackup-analysis.py) · [`plot_stackups.py`](../calculations/plot_stackups.py)
