# Tolerance stack-up: worst-case 1-D limit method (S10)
# Every input traced to a Phase 0-4 source doc. Reproduces the numbers in docs/stackup.md.

import matplotlib.pyplot as plt


def band(x): return f"{x:+.4f}"

print("="*70)
print("STACK 1 — ANALYSIS-LINK: throat-wall CTQ band -> DeltaT / stress")
print("="*70)
# Source: Phase5b_Sensitivity_Study.md tables 2.1 & 2.3 (t = 3,4,5 mm, Dirichlet BC)
t_data = {3:(1.33,3.9414,53.27), 4:(2.10,4.9171,42.70), 5:(2.71,6.1812,33.96)}  # (dT[K], sigma_vM[MPa], FoS)
sy = 209.95  # MPa @ 530.44 C (interp), Phase5b 2.3

def interp(t, idx):
    # piecewise-linear between the two bracketing sweep points
    lo = 4 if t>=4 else 3
    hi = lo+1
    f = (t-lo)/(hi-lo)
    a,b = t_data[lo][idx], t_data[hi][idx]
    return a + f*(b-a)

t_nom = 4.00                            # WALL BAND (T3, protect-minimum unilateral): 4 +0.3 / -0  (matches drawing CDN-001)
t_lo, t_hi = 4.00, 4.30
for label,t in [("min wall (4.00)",t_lo),("nominal (4.00)",t_nom),("max wall (4.30)",t_hi)]:
    dT  = interp(t,0); sig = interp(t,1); fos = sy/sig
    print(f"  {label:16s}: dT={dT:5.3f} K  sigma_vM={sig:5.3f} MPa  FoS(yield)={fos:5.1f}")
sig_lo, sig_hi = interp(t_lo,1), interp(t_hi,1)
print(f"  Stress excursion across band |d.sigma| = {abs(sig_hi-sig_lo):.3f} MPa")
print(f"  Yield margin at worst point  = {sy - max(sig_lo,sig_hi):.1f} MPa (FoS >= {sy/max(sig_lo,sig_hi):.1f})")
print(f"  T_throat identical across t (Dirichlet): 803.59 K -> creep-governed, BC/t-insensitive")

print()
print("="*70)
print("STACK 2 — MISALIGNMENT / CONCENTRICITY (radial, worst-case)")
print("="*70)
# 2a Throat-axis-to-mount-axis
# Pilot H7/g6 @ Ø92.80 (>80-100 band). ISO 286-2 (CONFIRM printed row C-2r)
H7 = (0.000, 0.035); g6 = (-0.012, -0.034)   # mm, hole & shaft deviations
cl_max = H7[1] - g6[1]        # max clearance = largest hole - smallest shaft
cl_min = H7[0] - g6[0]        # min clearance = smallest hole - largest shaft
pilot_float_radial = cl_max/2
runout_TIR = 0.05            # FCF #6 total runout A|B (T3 value)
runout_radial = runout_TIR/2
concentric_wc = pilot_float_radial + runout_radial
accept = 0.10                # T3 engineering judgment (ground-test prototype)
print(f"  Pilot fit  H7={H7} g6={g6}  -> clearance {cl_min:+.3f}..{cl_max:+.3f} (dia)")
print(f"  Pilot float (radial)        = {pilot_float_radial:.4f} mm")
print(f"  Body throat->pilot runout   = {runout_TIR:.3f} TIR -> {runout_radial:.4f} mm radial")
print(f"  Worst-case concentricity    = {concentric_wc:.4f} mm  vs accept <= {accept} (T3)")
print(f"  Margin ratio                = {accept/concentric_wc:.2f}x  -> {'PASS' if concentric_wc<=accept else 'FAIL'}")

# 2b Bolt-pattern assemblability (floating fastener, both parts) w/ pilot float
H, F = 9.0, 8.0              # clearance hole, fastener OD
T_pos = H - F               # floating-fastener position tol @ MMC (dia)
e_pattern = T_pos/2         # radial position error per part at MMC
avail_radial = (H-F)/2      # radial clearance per hole at MMC
need = e_pattern + e_pattern + pilot_float_radial
have = avail_radial + avail_radial
print(f"\n  [2b] Floating-fastener assemblability at strict MMC:")
print(f"       required (2*T/2 + pilot float) = {need:.4f} mm")
print(f"       available (2 * radial clear)   = {have:.4f} mm")
overrun = need - have
print(f"       overrun = {overrun:+.4f} mm  (covered by MMC bonus once holes > Ø{F + 2*overrun:.3f})")
T_pos_safe = (H - F) - 2*pilot_float_radial
print(f"       pilot-robust position tol      = ⌀{T_pos_safe:.3f} (round to ⌀0.9) if bonus not relied on")

print()
print("="*70)
print("STACK 3 — AXIAL TIP-FLOOR GAP (joint's #1 flagged item)")
print("="*70)
# gap = recess_depth - (spigot_proj - gasket_compressed)   [seated/compressed]
# General tol (title-block table §8): 0.5-6 mm -> ±0.1
S_nom, D_nom = 4.75, 4.00
g_seat = 1.0                 # compressed seated thickness (~1.0-1.1; APX2 HOCHDRUCK F36 37%, C-5r resolved 2026-08-12)
tol_gen = 0.10
def gap(D,S,g): return D - (S - g)
print(f"  Relation: gap = recess_depth - (spigot_proj - gasket_compressed)")
print(f"  Nominal: gap = {D_nom} - ({S_nom} - {g_seat}) = {gap(D_nom,S_nom,g_seat):.3f} mm")
# Worst case (min gap): D min, S max, g min
g_wc = gap(D_nom-tol_gen, S_nom+tol_gen, g_seat)          # gasket at design min 1.0
g_wc_over = gap(D_nom-tol_gen, S_nom+tol_gen, g_seat-0.1) # + gasket over-compression to 0.9
print(f"  Worst-case (gen ±0.1, g=1.0):  gap = {g_wc:+.3f} mm")
print(f"  + gasket over-compress (g=0.9): gap = {g_wc_over:+.3f} mm  -> {'NEGATIVE: metal bottoms' if g_wc_over<0 else 'ok'}")
# Fix A: deepen recess 4.0 -> 4.5
D_A = 4.5
gA = gap(D_A-tol_gen, S_nom+tol_gen, g_seat-0.1)
print(f"  FIX A deepen recess -> {D_A}: worst-case (g=0.9) gap = {gA:+.3f} mm -> PASS")
# Fix B: tighten S & D tol to ±0.05
tol_t = 0.05
gB = gap(D_nom-tol_t, S_nom+tol_t, g_seat-0.1)
print(f"  FIX B tighten S,D to ±0.05:    worst-case (g=0.9) gap = {gB:+.3f} mm -> {'PASS' if gB>0 else 'marginal'}")

# secondary: min register engagement = spigot - gasket - mouth chamfer (worst = S min, g max, chamfer max)
ch=0.75
E_min = (S_nom-tol_gen) - 1.5 - (ch+tol_gen)   # pre-compression free gasket 1.5, chamfer max
print(f"\n  [secondary] min register engagement (S min, free gasket 1.5, chamfer max) = {E_min:.2f} mm (>2 target)")

print()
print("="*70)
print("ADOPTED DECISIONS (2026-08-04)")
print("="*70)
D_adopt=4.5
print(f"  Stack 3 FIX A: recess {D_nom}->{D_adopt} mm")
print(f"    nominal gap = {gap(D_adopt,S_nom,g_seat):.3f} mm ; worst-case (g=0.9) = {gap(D_adopt-tol_gen,S_nom+tol_gen,g_seat-0.1):+.3f} mm -> PASS")
print(f"  Stack 2b: bolt position tightened to ⌀0.9 (T_safe={T_pos_safe:.3f}, bonus-independent)")



# Tolerance stack-up bar chart

x = [`x`,`x`,`x`]
y = [x,x,x,x,]

plt.barh(x,y)
plt.show()