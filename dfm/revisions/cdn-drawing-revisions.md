# CDN Drawing Revision History
**Sheets:** CDN-000 (assembly), CDN-001 (nozzle body), CDN-002 (mounting flange).

**Purpose:** chronological record of every change to the drawing set. The sheets carry no on-sheet rev-history block (portfolio scope). 

**Authority:** frozen STEP contour (`geometry-freeze-2026-07-20`) for aero geometry; [`drawing-data.md`](../docs/drawing-data.md) for interface features. Where a drawing and a document disagreed, the drawing was authority and the document was reconciled to it.

**Issued set:** [`../drawing/`](../drawing/) CDN-000, CDN-001, CDN-002 at Rev C. Every item below is APPLIED on that set.

**Status key:** APPLIED = on the issued sheet · CARRY-FWD = decided, CAD edit pending.

---

## Revision register (newest first)

| # | Date | Sheet (CDN No.) | Change | Reason | Status | Source |
|---|---|---|---|---|---|---|
| R-30 | 08-13 | 000, 001, 002 | Sheets renumbered to 1/1 | three separate drawing numbers → each is a single-sheet drawing (Y14.1/Y14.100) | APPLIED (Rev C) | validation 2026-08-13 |
| R-29 | 08-13 | 000 | Gasket BOM item 5: add grade V15011W3 + Ø92.8 ID × Ø112.8 OD × 1.5 | procurement completeness (`gasket-spec.md` §8) | APPLIED (Rev C) | validation 2026-08-13 |
| R-28 | 08-13 | 001, 002 | N4 add "ASTM" prefix (ASTM A479/A479M-25) | match `manufacturing.md` §8 + assembly BOM | APPLIED (Rev C) | validation 2026-08-13 |
| R-27 | 08-13 | 001, 002 | Ø152 OD: remove erroneous basic box → general tol | basic w/o refining FCF is uncontrolled; matches `drawing-data.md` §4/§5 | APPLIED (Rev C) | validation 2026-08-13 |
| R-26 | 08-13 | 001, 002 | 8X Ø9: remove erroneous basic box; add size tol +0.22/0 (H13, ISO 273 med) | position-at-MMC hole needs size limits so MMC=9.0 supports ⌀0.9 Ⓜ (`inspection-plan.md` §1) | APPLIED (Rev C) | validation 2026-08-13 |
| R-25 | 08-13 | 001, 002 | Add `45°` **basic** bolt-spacing angle (single increment between two adjacent holes) | drafting completeness: documents the 8-hole equal spacing alongside "8X EQ SP"; single basic increment per Y14.5 (not "8X 45°") | APPLIED | Mark 2026-08-13 |
| R-24 | 08-12 | 001 | Restore gasket-seat "SERRATED (DO NOT LAP)" | flat = seat geometry, serrated = finish (Ra 3.2-6.3, not lapped) so graphite seats without weeping; R-23 removal was an error | APPLIED | gasket-spec |
| R-23 | 08-12 | 001 | Remove (27.4)/(57.6) reference dims | redundant; outer wall now defined by N8 | APPLIED | Eng-Tips |
| R-22 | 08-12 | 001 | Add external-wall note N8; renumber N8 to N13 (datum note = N9) | Option A needs the outer surface defined after (27.4)/(57.6) removed | APPLIED | drawing-data §6 |
| R-21 | 08-12 | 001 | Add central gage point (Ø45)@(170.29) ref | a Ø on the tapered edge is hard to make/gauge; ref because the taper is already fully basic | APPLIED | Eng-Tips (mfgenggear) |
| R-20 | 08-12 | 001 | Exit `198.44` to basic; `Ø60` to reference | bound the profile zone at the outlet; dimensioning type only, geometry unchanged | APPLIED | Eng-Tips (mfgenggear) |
| R-19 | 08-12 | 001 | Reword N6 to single basic authority (Option A) | remove dual authority (N6 table and boxed basics); Y14.5 §1.4 | APPLIED | Eng-Tips |
| R-18 | 08-10 | 001 | Promote `15` (Datum A to chamber inlet) to basic | gives the profile chain a continuous basic path from Datum A ("[90] has no basic path") | APPLIED | Eng-Tips (3DDave) |
| R-17 | 08-10 | 000 | Fasteners shown unsectioned | Y14.5 / Y14.3 convention | APPLIED | Eng-Tips F-1 (3DDave) |
| R-16 | 08-10 | 001, 002 | Add bolt-circle (phantom) line; attach Ø128 basic to it | a BCD must dimension a drawn circle | APPLIED: CDN-001 Ø128 basic on drawn circle (verified); CDN-002 Ø128-on-circle applied 08-13 | Eng-Tips F-2 (3DDave) |
| R-15 | 08-09 | 001 | Add ⊥0.05 A on the pilot (datum B) | datum B squareness to A was assumed, not controlled | APPLIED | r/Machinists (EvlCat) |
| R-14 | 08-09 | 001 | Datum B frame on the Ø92.8 FOS; remove erroneous basic box | FOS reference unambiguous (size locks the feature, not its location) | APPLIED | r/Machinists (Sacrificial_Buttloaf) |
| R-13 | 08-09 | 001, 002 | Ø128 BC basic; "8X Ø9 EQ SP"; position ⌖⌀0.9 Ⓜ A B | PCD was a linear dim; holes not defined equally spaced | APPLIED | r/Machinists (shelvock86) |
| R-12 | 08-09 | 001 | Cutting-plane line; section A-A to C-C; throat detail D | no cutting-plane line; avoid reusing datum letters A/B | APPLIED | r/Machinists (shelvock86) |
| R-11 | 08-09 | 001 | Add "(PARALLEL TO DATUM A)" to 4 +0.3/0 CTQ | a directed wall thickness needs a measurement direction | APPLIED | r/Machinists (shelvock86, Saerylol) |
| R-10 | 08-09 | 001 | Reduce front-view hole dims; drop 7.5/13.1; relocate finish symbols | readability | APPLIED | r/Machinists (shelvock86, archerdynamics) |
| R-9 | 08-09 | 001 | Ra restacked max-over-min; general-finish note; g6 to 3 decimals | B46.1 / Y14.36M self-check | APPLIED | self-check |
| R-8 | 08-07 | 001 | Remove spurious Ø91.76 (was measuring the outer wall) | Phase-8 audit finding 6 | APPLIED | self-check |
| R-7 | 08-06 | 000 | BOM to solution-annealed; fastener to ISO 4014; gasket = reinforced flexible graphite | Phase-8 self-check | APPLIED | self-check |
| R-6 | 08-04 | 002 | Recess depth 4.0 to 4.5 (Fix A) | Stack 3: prevent spigot-tip bottoming on the recess floor (worst-case gap -0.05 to +0.45) | APPLIED | phase5/stackup §3 |
| R-5 | 08-04 | 001, 002 | Bolt position ⌀1.0 to ⌀0.9 Ⓜ | Stack 2b: assembly guaranteed independent of MMC bonus | APPLIED | phase5/stackup |
| R-4 | 08-04 | 001 | Throat-wall band reconciled to 4 +0.3/0 | Stack 1; the drawing already carried +0.3, so the **docs** were updated, no sheet change | APPLIED (doc-side) | phase5/stackup §1 |
| R-3 | 08-01 | 001 | Inner contour = profile ⌓0.2 A\|B + total runout ⌰0.05 A\|B | runout holds coaxiality to 0.025; profile-only and composite fail the concentricity stack | APPLIED | self-check |
| R-2 | 07-31 | 001 | Spigot 4.00 to 4.75; R1.5 fillet | assembly finding: register engagement was 0 mm (4.00 - 1.5 gasket - 0.75 chamfer) | APPLIED | self-check |
| R-1 | 07-30 | 001, 002 | Datum scheme committed: A\|B (A = seal face, B = pilot Ø92.80), no C; floating-fastener position; joint = 8 x M8 | Phase-3 gate cross-check | APPLIED | self-check |

---