"""
Tolerance stack-up figure for the SS316 C-D nozzle DFM package.

Regenerates dfm/images/stackup-summary.png.

Every number plotted is DERIVED from the same primitive inputs used by
stackup-analysis.py (fit deviations, hole/fastener sizes, nominal lengths,
general tolerance). Nothing is a transcribed result, so the figure cannot
silently disagree with the calculation.

Source of record: dfm/docs/stackup.md sections 2 and 3.
Method: worst-case 1-D limit stack (S10, Fischer 2nd ed.). Worst case rather
than RSS because this is a qty 1-5 prototype batch with no process-capability
data to root-sum.

Scope note: Stack 1 (analysis-link, throat-wall band -> stress) is deliberately
NOT plotted. It is a sensitivity propagation through an FEA response surface,
not an additive dimensional stack; drawing it as a contributor bar would assert
a method it does not use. See stackup-method-justification.md.

Note on glyphs: the MMC modifier is written "(M)" rather than the circled-M
character, which is absent from the default Matplotlib font. On the drawings it
is the circled symbol per ASME Y14.5-2018.

Usage
-----
    python plot_stackups.py                  write the PNG to dfm/images/
    python plot_stackups.py --show           write it and open a preview window
    python plot_stackups.py <output_path>    write it somewhere else

The default output path is resolved relative to THIS FILE, not to the shell's
current directory, so the PNG always lands in dfm/images/ no matter where the
script is launched from.
"""

import sys
from pathlib import Path

import matplotlib

SHOW = "--show" in sys.argv
if not SHOW:
    # File-only backend: no GUI toolkit needed, byte-identical output anywhere.
    matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

DEFAULT_OUT = Path(__file__).resolve().parent.parent / "images" / "stackup-summary.png"

# ----------------------------------------------------------------------------
# PRIMITIVE INPUTS  (mirror of stackup-analysis.py)
# ----------------------------------------------------------------------------
H7 = (0.000, +0.035)      # hole deviations, Ø92.80 pilot bore    ISO 286-2
g6 = (-0.012, -0.034)     # shaft deviations, Ø92.80 pilot        ISO 286-2
RUNOUT_TIR = 0.05         # total runout, throat -> pilot, A|B    CDN-001 FCF 6
ACCEPT_CONC = 0.10        # acceptance, radial                    T3 judgment

HOLE = 9.0                # clearance hole Ø                      ISO 273 medium
BOLT = 8.0                # fastener Ø, M8
POS_ADOPTED = 0.9         # adopted position tolerance            DECIDED 2026-08-04

SPIGOT = 4.75             # spigot projection, Part 1
RECESS_OLD = 4.00         # recess depth, Part 2, pre-fix
RECESS_NEW = 4.50         # recess depth, Part 2, Fix A adopted
GASKET_SEAT = 1.00        # compressed seated thickness, APX2
GASKET_OVER = 0.90        # over-compressed bound
TOL_GEN = 0.10            # general tolerance, 0.5-6 mm band

# ----------------------------------------------------------------------------
# DERIVED
# ----------------------------------------------------------------------------
pilot_float = (H7[1] - g6[1]) / 2.0          # max diametral clearance -> radial
runout_radial = RUNOUT_TIR / 2.0
conc_wc = pilot_float + runout_radial

per_part_base = (HOLE - BOLT) / 2.0
per_part_adopt = POS_ADOPTED / 2.0
avail = 2 * per_part_base
req_base = 2 * per_part_base + pilot_float
req_adopt = 2 * per_part_adopt + pilot_float


def gap(recess, spigot, gasket):
    return recess - (spigot - gasket)


gap_pre_wc = gap(RECESS_OLD - TOL_GEN, SPIGOT + TOL_GEN, GASKET_SEAT)
gap_pre_over = gap(RECESS_OLD - TOL_GEN, SPIGOT + TOL_GEN, GASKET_OVER)
gap_new_wc = gap(RECESS_NEW - TOL_GEN, SPIGOT + TOL_GEN, GASKET_SEAT)
gap_new_over = gap(RECESS_NEW - TOL_GEN, SPIGOT + TOL_GEN, GASKET_OVER)

# ----------------------------------------------------------------------------
# PALETTE  (validated light-mode, adjacent and all-pairs CVD gates)
# ----------------------------------------------------------------------------
SURFACE = "#fcfcfb"
INK, INK_2, MUTED = "#0b0b0b", "#52514e", "#898781"
GRID, AXIS = "#e1e0d9", "#c3c2b7"
C_RUNOUT = "#2a78d6"      # slot 1 blue
C_PILOT = "#eb6834"       # slot 2 orange  (same entity keeps its hue, panels A+B)
C_PATTERN = "#1baf7a"     # slot 3 aqua
C_GOOD, C_CRIT = "#0ca30c", "#d03b3b"

BAR_H = 0.40


def style(ax, xlim, xlabel):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(AXIS)
    ax.spines["bottom"].set_linewidth(0.8)
    ax.xaxis.grid(True, color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    ax.tick_params(colors=MUTED, labelsize=9, length=0)
    ax.set_xlim(*xlim)
    ax.set_xlabel(xlabel, color=INK_2, fontsize=9, labelpad=5)
    for lbl in ax.get_yticklabels():
        lbl.set_color(INK)
        lbl.set_fontsize(9.2)


def header(ax, title, desc, r):
    """r = this panel's height ratio; offsets are scaled so the header sits a
    constant physical distance above every panel regardless of its height."""
    ax.text(0, 1 + 0.345 / r, title, transform=ax.transAxes, color=INK,
            fontsize=11.5, weight="bold", va="bottom")
    ax.text(0, 1 + 0.085 / r, desc, transform=ax.transAxes, color=INK_2,
            fontsize=8.7, va="bottom", linespacing=1.55)


def stacked(ax, y, segs, gapw):
    left = 0.0
    for i, (val, col) in enumerate(segs):
        w = val - (gapw if i < len(segs) - 1 else 0.0)
        ax.barh(y, w, left=left, height=BAR_H, color=col, zorder=3)
        left += val
    return left


fig, axes = plt.subplots(3, 1, figsize=(10.0, 9.6), dpi=150,
                         gridspec_kw={"height_ratios": [0.85, 1.0, 1.5],
                                      "hspace": 1.05})
fig.patch.set_facecolor(SURFACE)

# ============================================================================
# PANEL A — concentricity
# ============================================================================
ax = axes[0]
style(ax, (0, 0.138), "radial deviation (mm)")
header(ax, "A · Thrust-axis concentricity (Stack 2a)",
       "How far the throat axis can sit off the mount axis.\n"
       "Acceptance is engineering judgment for a ground-test prototype, not analysis-derived.", 0.85)

stacked(ax, 0, [(pilot_float, C_PILOT), (runout_radial, C_RUNOUT)], gapw=0.0007)
ax.axvline(ACCEPT_CONC, color=C_CRIT, lw=1.6, ls=(0, (5, 3)), zorder=4)
ax.text(ACCEPT_CONC + 0.002, 0.50, f"acceptance ≤ {ACCEPT_CONC:.2f}  (T3 judgment)",
        color=C_CRIT, fontsize=8.5, va="center")
ax.text(pilot_float / 2, 0, f"{pilot_float:.4f}", color="white", fontsize=8.5,
        ha="center", va="center", weight="bold", zorder=5)
ax.text(pilot_float + runout_radial / 2, 0, f"{runout_radial:.4f}", color="white",
        fontsize=8.5, ha="center", va="center", weight="bold", zorder=5)
ax.text(conc_wc + 0.003, 0.16, f"Σ {conc_wc:.4f} mm", color=INK,
        fontsize=9.5, va="center", weight="bold")
ax.text(conc_wc + 0.003, -0.20, f"PASS · {ACCEPT_CONC / conc_wc:.2f}× margin",
        color=C_GOOD, fontsize=9, va="center", weight="bold")
ax.set_yticks([0])
ax.set_yticklabels(["worst case"])
ax.set_ylim(-0.75, 0.78)

# ============================================================================
# PANEL B — bolt-pattern assemblability
# ============================================================================
ax = axes[1]
style(ax, (0, 1.42), "radial requirement at strict MMC (mm)")
header(ax, "B · Bolt-pattern assemblability (Stack 2b)",
       "Pilot float eats into floating-fastener clearance; tightening position buys it back.\n"
       "Conservative 1-D screen of a 2-D pattern fit, so it errs safe.", 1.0)

stacked(ax, 1, [(2 * per_part_base, C_PATTERN), (pilot_float, C_PILOT)], gapw=0.007)
stacked(ax, 0, [(2 * per_part_adopt, C_PATTERN), (pilot_float, C_PILOT)], gapw=0.007)
ax.axvline(avail, color=INK, lw=1.6, zorder=4)
ax.text(avail - 0.015, 1.62, f"available clearance {avail:.3f}", color=INK,
        fontsize=8.6, va="center", ha="right")
ax.text(2 * per_part_base / 2, 1, f"{2*per_part_base:.3f}", color="white",
        fontsize=8.5, ha="center", va="center", weight="bold", zorder=5)
ax.text(2 * per_part_adopt / 2, 0, f"{2*per_part_adopt:.3f}", color="white",
        fontsize=8.5, ha="center", va="center", weight="bold", zorder=5)
LBL_X = max(req_base, avail) + 0.025
ax.text(LBL_X, 1.16, f"{req_base:.4f}", color=INK, fontsize=9.5,
        va="center", weight="bold")
ax.text(LBL_X, 0.82, f"+{req_base - avail:.4f} overrun", color=C_CRIT,
        fontsize=8.8, va="center", weight="bold")
ax.text(LBL_X, 0.16, f"{req_adopt:.4f}", color=INK, fontsize=9.5,
        va="center", weight="bold")
ax.text(LBL_X, -0.18, "PASS · bonus-independent", color=C_GOOD,
        fontsize=8.8, va="center", weight="bold")
ax.set_yticks([1, 0])
ax.set_yticklabels(["required at ⌀1.0\nbase, H − F", "required at ⌀0.9 (M)\nadopted"])
ax.set_ylim(-0.8, 1.95)

# ============================================================================
# PANEL C — axial tip-floor gap
# ============================================================================
ax = axes[2]
style(ax, (-0.16, 0.78), "worst-case gap (mm)      gap = recess − (spigot − gasket)")
header(ax, "C · Axial tip-floor gap (Stack 3)",
       "The spigot tip must stay clear of the recess floor so the gasket, not metal, sets axial position.\n"
       "Fix A (recess 4.00 → 4.50 mm) adopted 2026-08-04.", 1.5)

rows = [
    (3, gap_pre_wc,   f"recess {RECESS_OLD:.2f} · gasket {GASKET_SEAT:.2f}"),
    (2, gap_pre_over, f"recess {RECESS_OLD:.2f} · gasket {GASKET_OVER:.2f}"),
    (1, gap_new_wc,   f"recess {RECESS_NEW:.2f} · gasket {GASKET_SEAT:.2f}"),
    (0, gap_new_over, f"recess {RECESS_NEW:.2f} · gasket {GASKET_OVER:.2f}"),
]
for y, val, _ in rows:
    col = C_GOOD if val > 0 else C_CRIT
    ax.barh(y, val, height=BAR_H, color=col, zorder=3)
    tag = "PASS" if val > 0 else "FAIL · metal bottoms, gasket unloads"
    x = max(val, 0.0) + 0.014
    ax.text(x, y, f"{val:+.3f}   {tag}", color=col, fontsize=9,
            va="center", ha="left", weight="bold", zorder=5)

ax.axvline(0, color=INK, lw=1.6, zorder=4)
ax.axhline(1.5, color=AXIS, lw=0.8, zorder=2)
ax.set_yticks([r[0] for r in rows])
ax.set_yticklabels([r[2] for r in rows])
ax.set_ylim(-0.8, 3.75)

# ============================================================================
# CHROME
# ============================================================================
fig.text(0.055, 0.975, "Worst-case tolerance stack-ups · SS316 C-D nozzle inlet joint",
         ha="left", va="top", color=INK, fontsize=14.5, weight="bold")
fig.text(0.055, 0.949,
         "Worst-case 1-D limit method (S10). Worst case, not RSS: qty 1–5 prototype batch, "
         "no process-capability data to root-sum.",
         ha="left", va="top", color=INK_2, fontsize=9.2)

fig.legend(
    handles=[Patch(fc=C_PILOT, label="Pilot fit float, Ø92.80 H7/g6"),
             Patch(fc=C_RUNOUT, label="Total runout ⌀0.05 TIR → A|B"),
             Patch(fc=C_PATTERN, label="Bolt-pattern position, both parts")],
    loc="lower left", bbox_to_anchor=(0.05, 0.034), ncol=3, frameon=False,
    fontsize=9, labelcolor=INK_2, handlelength=1.1, handleheight=1.1,
    columnspacing=2.0, borderpad=0)
fig.text(0.055, 0.010,
         "Source: dfm/docs/stackup.md §2–3 · regenerate with dfm/calculations/plot_stackups.py",
         ha="left", va="center", color=MUTED, fontsize=7.8)

fig.subplots_adjust(left=0.20, right=0.955, top=0.848, bottom=0.105)

paths = [a for a in sys.argv[1:] if not a.startswith("--")]
out = Path(paths[0]) if paths else DEFAULT_OUT
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, facecolor=SURFACE, dpi=150)
print(f"wrote {out}")
print(f"  A  concentricity {conc_wc:.4f} vs {ACCEPT_CONC:.2f}  -> {ACCEPT_CONC/conc_wc:.2f}x")
print(f"  B  required {req_base:.4f} / {req_adopt:.4f} vs available {avail:.4f}")
print(f"  C  gap pre {gap_pre_over:+.3f} -> post {gap_new_over:+.3f}")

if SHOW:
    plt.show()
