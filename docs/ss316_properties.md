# SS316 Material Properties

**Grade:** Type 316 / UNS S31600 / EN 1.4401
**Condition:** Annealed
**Compiled:** 2026-05-04
**Verification:** All values cross-checked against primary sources on 2026-05-04. Direct reads, interpolations, and source switches are explicitly flagged.

---

## ⚠ Important Note on the 600 °C Column

600 °C falls inside the **carbide precipitation range (427–871 °C)** for unstabilized 316. The values below are valid for short-time analysis (e.g. peak stress checks during transient events), but **continuous service at 600 °C is not recommended for standard 316.** Use **316L** or **316Ti** for sustained operation in this temperature window.

Additionally, at 600 °C the material is approaching its **creep regime** (typically taken as 0.4 × T_melt in K, ≈ 410 °C for 316). Yield strength alone is no longer the right design parameter for sustained loading; creep-rupture data (e.g. ASME II-D allowable stresses, which incorporate time-dependent behavior above ~454 °C) should be used instead. The σ_y at 600 °C value is included here for reference only.

Also: most primary sources (BS EN 10088-1, SSINA Table 5) only publish elevated-temperature data up to 500 °C. Values at 600 °C are sourced from a different (compatible) primary table — INCO Publication 2980 — and explicitly flagged.

---

## Properties

| Property | Symbol | 20 °C | 200 °C | 400 °C | 600 °C | Unit | Method |
|---|---|---|---|---|---|---|---|
| Young's Modulus | E | 200 | 186 | 172 | 152* | GPa | direct; *source switch¹ |
| Yield Strength (0.2% offset, typical) | σ_y | 310 | 263² | 238² | 195² | MPa | typical, interp² |
| Ultimate Tensile Strength (typical) | σ_u | 621 | 553² | 496² | 399² | MPa | typical, interp² |
| Thermal Conductivity³ | k | 14.0 | 16.0 | 18.6 | 21.5* | W/(m·K) | direct; *source switch¹ |
| Thermal Expansion (mean, 20 °C → T) | α | 16.0⁴ | 16.5 | 17.5 | 18.5* | ×10⁻⁶ /K | direct; *extrapolated¹ |
| Density | ρ | 7950 | 7880 | 7801² | 7713² | kg/m³ | direct, interp² |
| Poisson's Ratio | ν | ~0.30 (data scatters 0.26–0.34, T-dependent⁵) | | | | — | — |

¹ Primary sources for E, k, and α (BS EN 10088-1 and SSINA Table 5) stop at 500 °C. The 600 °C values come from BSSA INCO 2980 (for E and k) or extrapolation of the EN 10088-1 trend cross-checked against INCO 2980 304 data and Atlas/Ulbrich 316 datasheets (for α). At 200/400 °C where sources overlap, agreement is within ~2 %.
² Linearly interpolated from source table values; arithmetic shown in "Source data" below.
³ Source tabulates this for 316L (UNS S31603) at 20/200/400 °C. Standard engineering practice treats 316 and 316L as identical for thermal conductivity — the chemistry difference is in carbon content, which does not affect k meaningfully. The 600 °C value is from INCO 2980 which IS 316-specific.
⁴ The 20 °C entry is the mean coefficient from 20 °C → 100 °C; α is undefined at a single point.
⁵ Source measurement data is noisy and non-monotonic: 0.26 (150 °C), 0.29 (260 °C), 0.34 (370 °C), 0.30 (480 °C), 0.32 (590 °C). ν = 0.30 is the standard engineering value used for 316 across the 20–600 °C range.

---

## Maximum Service Temperature

| Service mode | Temperature limit |
|---|---|
| Continuous (oxidizing atmosphere) | 925 °C (1700 °F) |
| Intermittent (oxidizing atmosphere) | 870 °C (1600 °F) |

**Avoid continuous service in 427–871 °C** (800–1600 °F) — carbide precipitation in unstabilized 316 in this range degrades corrosion resistance. Use 316L or 316Ti for continuous service in this window.

The intermittent limit is *lower* than the continuous limit because thermal cycling causes oxide scale to crack and spall, accelerating surface degradation.

---

## Source Data (Direct Reads from Primary Sources)

### Modulus of elasticity — BS EN 10088-1 (via BSSA), GPa

| 20 °C | 100 °C | 200 °C | 300 °C | 400 °C | 500 °C |
|---|---|---|---|---|---|
| 200 | 194 | 186 | 179 | 172 | 165 |

For 600 °C (from BSSA INCO 2980, units kgf/mm² × 10³ converted via × 9.807 → MPa, then ÷1000 → GPa):

$$E_{590} = 15.6 \times 9.807 = 152.99 \text{ GPa}$$

$$E_{650} = 15.1 \times 9.807 = 148.09 \text{ GPa}$$

$$E_{600} = 152.99 + (148.09 - 152.99) \times \frac{600 - 590}{650 - 590} = 152.17 \text{ GPa}$$

### Mean coefficient of thermal expansion — BS EN 10088-1 (via BSSA), ×10⁻⁶ /K

Between 20 °C and T:

| 20→100 °C | 20→200 °C | 20→300 °C | 20→400 °C | 20→500 °C |
|---|---|---|---|---|
| 16.0 | 16.5 | 17.0 | 17.5 | 18.0 |

For 20→600 °C: linear extrapolation of the EN 10088-1 trend (+0.5 per 100 °C) gives **18.5 × 10⁻⁶/K**. Cross-checks: INCO 2980 304 at 20→600 °C = 18.3 (304 ≈ 316 thermally); Ulbrich 316 datasheet (0–649 °C) = 18.5. Agreement is good.

### Thermal conductivity — SSINA Table 5 / Nickel Institute brochure 11021, W/(m·K)

Tabulated for 316L (applied to 316; see note ³):

| 20 °C | 100 °C | 200 °C | 300 °C | 400 °C | 500 °C |
|---|---|---|---|---|---|
| 14.0 | 14.9 | 16.0 | 17.3 | 18.6 | 19.9 |

For 600 °C (BSSA INCO 2980 in kcal/m·hr·°C, × 1.163 → W/(m·K)):

$$k_{600} = 18.5 \times 1.163 = 21.52 \text{ W/(m} \cdot \text{K)}$$

Sanity check at 400 °C overlap: INCO 2980 gives 16.0 × 1.163 = 18.61, vs SSINA Table 5 = 18.6 — exact agreement.

### Density — INCO Publication 2980 (via BSSA), kg/m³

| 20 °C | 90 °C | 200 °C | 320 °C | 430 °C | 540 °C | 650 °C |
|---|---|---|---|---|---|---|
| 7950 | 7920 | 7880 | 7830 | 7790 | 7740 | 7690 |

200 °C is a direct read. Interpolation arithmetic for 400 °C and 600 °C:

$$\rho_{400} = 7830 + (7790 - 7830) \times \frac{400 - 320}{430 - 320} = 7800.9 \text{ kg/m}^{3}$$

$$\rho_{600} = 7740 + (7690 - 7740) \times \frac{600 - 540}{650 - 540} = 7712.7 \text{ kg/m}^{3}$$

### Tensile properties — SSINA Table 1 / Nickel Institute brochure 9004 (AISI Designers' Handbook)

Annealed condition typical short-time elevated temperature values. Source originally tabulated in °F and ksi (1 ksi = 6.89476 MPa):

| Source temp | Converted | σ_u (ksi / MPa) | σ_y (ksi / MPa) |
|---|---|---|---|
| Room | ~21 °C | 90 / 621 | 45 / 310 |
| 400 °F | 204 °C | 80 / 552 | 38 / 262 |
| 600 °F | 316 °C | 75 / 517 | 36 / 248 |
| 800 °F | 427 °C | 71 / 490 | 34 / 234 |
| 1000 °F | 538 °C | 64 / 441 | 30 / 207 |
| 1200 °F | 649 °C | 53 / 365 | 27 / 186 |

Interpolation arithmetic:

$$\sigma_{y, 200} = 310 + (262 - 310) \times \frac{200 - 21}{204 - 21} = 263.1 \text{ MPa}$$

$$\sigma_{y, 400} = 248 + (234 - 248) \times \frac{400 - 316}{427 - 316} = 237.8 \text{ MPa}$$

$$\sigma_{y, 600} = 207 + (186 - 207) \times \frac{600 - 538}{649 - 538} = 195.3 \text{ MPa}$$

$$\sigma_{u, 200} = 621 + (552 - 621) \times \frac{200 - 21}{204 - 21} = 553.1 \text{ MPa}$$

$$\sigma_{u, 400} = 517 + (490 - 517) \times \frac{400 - 316}{427 - 316} = 496.2 \text{ MPa}$$

$$\sigma_{u, 600} = 441 + (365 - 441) \times \frac{600 - 538}{649 - 538} = 398.9 \text{ MPa}$$

---

## Working Equations

Total thermal strain at temperature T using the mean coefficient:

$$\varepsilon_{\text{thermal}} = \alpha_{\text{mean}}(T) \times (T - T_{\text{ref}})$$

Linearized von Mises yield check at temperature T with safety factor n:

$$\sigma_{\text{vM}} \leq \frac{\sigma_{y}(T)}{n}$$

Definition of the mean coefficient of thermal expansion (the value at a single T is the instantaneous coefficient, not the mean):

$$\alpha_{\text{mean}}(T) = \frac{1}{T - T_{\text{ref}}} \int_{T_{\text{ref}}}^{T} \alpha(T') \, dT'$$

---

## Sources

| Property | Primary source | Verification |
|---|---|---|
| E at 20/200/400 °C, α at 20/200/400 °C | BS EN 10088-1 (via BSSA) | Direct fetch 2026-05-04 |
| E at 600 °C | BSSA INCO Publication 2980 | Direct fetch 2026-05-04 |
| α at 600 °C | Extrapolated from EN 10088-1; cross-check INCO 2980 (304) and Atlas/Ulbrich (316) | Direct fetch 2026-05-04 |
| k at 20/200/400 °C | SSINA Table 5 / Nickel Institute brochure 11021 | Direct fetch 2026-05-04 |
| k at 600 °C | BSSA INCO Publication 2980 | Direct fetch 2026-05-04 |
| σ_y, σ_u | SSINA Table 1 / Nickel Institute brochure 9004 (AISI Designers' Handbook) | Direct fetch 2026-05-04 |
| ρ, ν | INCO Publication 2980 (via BSSA) | Direct fetch 2026-05-04 |
| Max service temperature, carbide precipitation range | SSINA Tables 1–2 | Direct fetch 2026-05-04 |

**Reference URLs:**

- BSSA elevated-temperature physical properties: https://bssa.org.uk/bssa_articles/elevated-temperature-physical-properties-of-stainless-steels/
- SSINA composition/properties: https://www.ssina.com/education/technical-resources/composition-properties/

---

## Notes on Use

- **σ_y values here are typical** (annealed mill data, AISI legacy). For pressure-vessel code work, use EN 10028-7 minimum design values or ASME BPVC Section II-D allowable stresses instead. Spec-minimum values are roughly 50–70 % of the typical values listed here.
- **σ_y at 600 °C is reference only** — design at this temperature must use creep-rupture data, not yield strength, because 316 is in its creep regime above ~410 °C.
- **200 °C, 400 °C, and 600 °C values for σ_y and σ_u are interpolated** from source rows in 200 °F (~111 °C) increments; interpolation introduces ±2–3 % uncertainty.
- **Density at 200 °C is a direct read** (exact temperature match in source). Density at 400 °C and 600 °C is interpolated; uncertainty < 0.5 %.
- **k at 20/200/400 °C is from SSINA Table 5 (listed for 316L); k at 600 °C is from INCO 2980 (316-specific)**. Both sources are consistent within ~1 % at the 400 °C overlap point.
- **α is a mean coefficient referenced to 20 °C** — appropriate for total ΔL calculations from a 20 °C reference state. For instantaneous α(T) in transient thermal FEA, derive from the mean curve by differentiating, or use a finer-resolution reference table.
- For real components, **always cross-check against the mill test report (MTR)** — handbook values are reference points, not design values.

---

## Scope

This datasheet covers **standard Type 316 only**. It does NOT apply to:

- **316L** (UNS S31603, EN 1.4404) — lower carbon, approximately 10–15 % lower yield strength
- **316H** (UNS S31609) — higher carbon, intended for service above 500 °C
- **316Ti** (UNS S31635, EN 1.4571) — titanium-stabilized for elevated-temperature corrosion resistance

Verify grade before applying these values.
