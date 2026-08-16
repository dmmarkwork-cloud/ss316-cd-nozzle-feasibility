"""
Gasket bolt-load + margin calc, CONFIRMED gasket = SIGRAFLEX APX2 HOCHDRUCK V15011W3.
Method: ASME BPVC VIII-1 (2021) Mandatory Appendix 2, eq (1) Wm1 and eq (2) Wm2.
  - b, G derived per Table 2-5.2 (flat gasket, sketch 1a/1b): b0 = N/2; b0 <= 6 mm -> b = b0, G = mean dia.
Inputs m, y from the SGL APX2 HOCHDRUCK datasheet (ASTM columns, grade V15011W3, 1.5 mm):
  m = 2.5, y = 3000 psi.  (Datasheet also lists DIN/EN m=1.3, VU=20 N/mm^2 - different framework, not used here.)
Reproduce:  python3 gasket_loads.py
"""
import math

# --- Joint geometry (full seat), verified vs ASME Table 2-5.2 ---
gasket_ID, gasket_OD = 92.8, 112.8         # mm
N  = (gasket_OD - gasket_ID)/2             # contact width = 10.0 mm
b0 = N/2                                    # basic seating width, sketch 1a/1b = 5.0 mm
b  = b0 if b0 <= 6.0 else 0.5*math.sqrt(b0/25.4)*25.4   # b0<=6mm -> b=b0
G  = (gasket_OD + gasket_ID)/2 if b0 <= 6.0 else gasket_OD - 2*b   # mean dia = 102.8 mm
P  = 2.0                                    # MPa, chamber pressure

# --- Gasket factors, CONFIRMED product (APX2 HOCHDRUCK V15011W3, ASTM columns) ---
m       = 2.5
y_psi   = 3000.0
psi     = 0.00689476
y       = y_psi*psi                         # 20.68 MPa

# --- Bolt loads, ASME App 2 ---
H   = 0.785*G**2*P                          # hydrostatic end force
Hp  = 2*b*math.pi*G*m*P                     # gasket contact compression under pressure
Wm1 = H + Hp                                # operating
Wm2 = math.pi*b*G*y                         # seating
Wgov = max(Wm1, Wm2)
gmode = "seating (Wm2)" if Wm2 >= Wm1 else "operating (Wm1)"

# --- Gasket seating-stress check (delivered over effective area = pi*G*b) ---
A_eff   = math.pi*G*b                       # effective seating area, mm^2
sigma_seat = Wm2/A_eff                      # = y by construction, N/mm^2
VU, VO, BO300 = 20.0, 270.0, 210.0          # datasheet: min assy / max at 20C / max at 300C, N/mm^2

# --- Bolt margins: 8 x M8 A286 ---
n_bolt, As_bolt = 8, 36.6                    # stress area per M8, mm^2
Ab = n_bolt*As_bolt                          # 292.8 ~ 293 mm^2
screen = 190.0                               # conservative II-D screen allowable, MPa (non-governing)
yld_hot = 582.0                              # A286 datasheet hot yield at 527C, MPa (governing basis)
req_screen = Wgov/screen
margin_screen = Ab/req_screen
sigma_bolt_gov = Wgov/Ab                     # applied bolt stress at governing load, MPa
preload = 1.4*Wm1                            # assembly preload target (tightness), N
sigma_preload = preload/Ab

print(f"geometry:  N={N:.1f}  b0={b0:.1f}  b={b:.1f} mm  G={G:.1f} mm  (ASME Table 2-5.2)")
print(f"factors :  m={m}  y={y_psi:.0f} psi = {y:.2f} N/mm^2   [APX2 HOCHDRUCK V15011W3, ASTM]")
print("-"*60)
print(f"H   = {H/1000:6.2f} kN   Hp = {Hp/1000:6.2f} kN")
print(f"Wm1 = {Wm1/1000:6.2f} kN  (operating)")
print(f"Wm2 = {Wm2/1000:6.2f} kN  (seating)")
print(f"Wgov= {Wgov/1000:6.2f} kN  -> GOVERNING = {gmode}")
print("-"*60)
print(f"gasket seating stress (over pi*G*b={A_eff:.0f} mm^2) = {sigma_seat:.1f} N/mm^2")
print(f"   check: VU {VU} <= {sigma_seat:.1f} <= VO {VO} (20C) / BO {BO300} (300C)  -> seated, not crushed")
print("-"*60)
print(f"bolts: {n_bolt} x M8 A286, Ab = {Ab:.0f} mm^2")
print(f"req area @190 MPa screen = {req_screen:.0f} mm^2  -> margin {margin_screen:.2f}x")
print(f"applied bolt stress @Wgov = {sigma_bolt_gov:.0f} MPa = {sigma_bolt_gov/yld_hot*100:.0f}% of 582 hot yield")
print(f"preload 1.4xWm1 = {preload/1000:.1f} kN total = {sigma_preload:.0f} MPa = {sigma_preload/yld_hot*100:.0f}% hot yield")
print(f"envelope check: Wgov {Wgov/1000:.1f} kN <= 35 kN design envelope: {'OK' if Wgov<=35000 else 'EXCEEDS'}")
