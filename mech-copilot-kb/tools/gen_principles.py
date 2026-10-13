#!/usr/bin/env python3
"""Generate kb/principles/*.json + kb/assets/diagrams/*.svg (2.5D-style diagrams).
All content authored for this KB, CC0. Diagrams are hand-built SVG (no deps)."""
import json, os

ROOT = os.path.join(os.path.dirname(__file__), "..", "kb")
PRI = os.path.join(ROOT, "principles")
DIA = os.path.join(ROOT, "assets", "diagrams")
os.makedirs(PRI, exist_ok=True); os.makedirs(DIA, exist_ok=True)

def svg_wrap(body, w=480, h=260, title=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="sans-serif">
<rect width="{w}" height="{h}" fill="#0e1420"/>
<text x="16" y="24" fill="#7fd4ff" font-size="15" font-weight="bold">{title}</text>
{body}
</svg>'''

def arrow(x1, y1, x2, y2, color="#ffd166", w=2.5, label=""):
    head = 8
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    hx1 = x2 - head * math.cos(ang - 0.45); hy1 = y2 - head * math.sin(ang - 0.45)
    hx2 = x2 - head * math.cos(ang + 0.45); hy2 = y2 - head * math.sin(ang + 0.45)
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"/>'
    s += f'<polygon points="{x2},{y2} {hx1},{hy1} {hx2},{hy2}" fill="{color}"/>'
    if label:
        s += f'<text x="{(x1+x2)/2}" y="{(y1+y2)/2 - 8}" fill="{color}" font-size="12" text-anchor="middle">{label}</text>'
    return s

def circle_joint(x, y, r=5, fill="#0e1420", stroke="#7fd4ff"):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'

diagrams = {}

# FBD: block on incline with weight, normal, friction
diagrams["PR-FBD-01"] = svg_wrap(f'''
<polygon points="60,210 420,210 420,120" fill="none" stroke="#8899aa" stroke-width="2"/>
<rect x="200" y="150" width="60" height="40" fill="#1d2c45" stroke="#7fd4ff" stroke-width="2" transform="rotate(-23 230 170)"/>
{arrow(230, 170, 230, 105, "#ff6b6b", 3, "W = mg")}
{arrow(230, 170, 296, 148, "#7fd4ff", 3, "N")}
{arrow(230, 170, 178, 152, "#ffd166", 3, "Ff")}
<text x="330" y="200" fill="#8899aa" font-size="12">incline angle theta</text>
''', title="Free-body diagram: block on incline")

# DOF / planar joint cheat table drawn as boxes
diagrams["PR-DOF-01"] = svg_wrap(f'''
<rect x="40" y="50" width="120" height="60" fill="#1d2c45" stroke="#7fd4ff"/>
<text x="100" y="75" fill="#cde" font-size="13" text-anchor="middle">revolute (pin)</text>
<text x="100" y="95" fill="#8899aa" font-size="12" text-anchor="middle">R: removes 2</text>
{circle_joint(100, 120)}
<rect x="180" y="50" width="120" height="60" fill="#1d2c45" stroke="#7fd4ff"/>
<text x="240" y="75" fill="#cde" font-size="13" text-anchor="middle">prismatic (slide)</text>
<text x="240" y="95" fill="#8899aa" font-size="12" text-anchor="middle">P: removes 2</text>
<line x1="180" y1="125" x2="300" y2="125" stroke="#7fd4ff" stroke-width="2"/>
<rect x="320" y="50" width="120" height="60" fill="#1d2c45" stroke="#7fd4ff"/>
<text x="380" y="75" fill="#cde" font-size="13" text-anchor="middle">rigid (fixed)</text>
<text x="380" y="95" fill="#8899aa" font-size="12" text-anchor="middle">removes 3 (planar)</text>
<text x="240" y="190" fill="#ffd166" font-size="13" text-anchor="middle">Gruebler: DOF = 3(n-1) - 2j1 - j2</text>
''', title="Planar joint types and DOF")

# lever
diagrams["PR-LVR-01"] = svg_wrap(f'''
<line x1="80" y1="160" x2="400" y2="140" stroke="#cde" stroke-width="8" stroke-linecap="round"/>
<path d="M 240 150 L 240 200 L 252 185 L 228 185 Z" fill="#8899aa"/>
{arrow(120, 120, 120, 150, "#ff6b6b", 3, "F1")}
{arrow(380, 105, 380, 138, "#7fd4ff", 3, "F2")}
<text x="120" y="110" fill="#ff6b6b" font-size="12" text-anchor="middle">d1</text>
<text x="380" y="95" fill="#7fd4ff" font-size="12" text-anchor="middle">d2</text>
<text x="240" y="230" fill="#ffd166" font-size="13" text-anchor="middle">F1*d1 = F2*d2 (equilibrium)</text>
''', title="Lever: moment balance about fulcrum")

# gear mesh
diagrams["PR-GTR-01"] = svg_wrap(f'''
<circle cx="180" cy="140" r="55" fill="none" stroke="#7fd4ff" stroke-width="2.5" stroke-dasharray="6 4"/>
<circle cx="305" cy="140" r="90" fill="none" stroke="#7fd4ff" stroke-width="2.5" stroke-dasharray="6 4"/>
<circle cx="180" cy="140" r="50" fill="#1d2c45" stroke="#cde" stroke-width="2"/>
<circle cx="305" cy="140" r="85" fill="#1d2c45" stroke="#cde" stroke-width="2"/>
{circle_joint(180, 140, 4)}{circle_joint(305, 140, 4)}
{arrow(180, 70, 220, 70, "#ffd166", 2.5, "w1 (fast)")}
{arrow(305, 35, 265, 35, "#7fd4ff", 2.5, "w2 = w1*z1/z2")}
<text x="242" y="150" fill="#8899aa" font-size="12" text-anchor="middle">C = m(z1+z2)/2</text>
''', 480, 260, "Gear train: ratio = z2/z1, centre distance")

# belt
diagrams["PR-BLT-01"] = svg_wrap(f'''
<circle cx="150" cy="130" r="45" fill="#1d2c45" stroke="#cde" stroke-width="2"/>
<circle cx="330" cy="130" r="70" fill="#1d2c45" stroke="#cde" stroke-width="2"/>
<path d="M 150 85 A 45 45 0 0 1 150 175 L 260 200 A 70 70 0 0 0 260 60 Z" fill="none" stroke="#ffd166" stroke-width="4"/>
{circle_joint(150, 130, 4)}{circle_joint(330, 130, 4)}
<text x="240" y="245" fill="#ffd166" font-size="13" text-anchor="middle">i = D2/D1 (flat) - timing belts: no slip</text>
''', title="Belt drive: tension side vs slack side")

# four-bar
diagrams["PR-4BAR-01"] = svg_wrap(f'''
{circle_joint(80, 200)}{circle_joint(360, 200)}
<line x1="80" y1="200" x2="360" y2="200" stroke="#8899aa" stroke-width="5"/>
<line x1="80" y1="200" x2="130" y2="90" stroke="#7fd4ff" stroke-width="5"/>
<line x1="130" y1="90" x2="300" y2="70" stroke="#ffd166" stroke-width="5"/>
<line x1="300" y1="70" x2="360" y2="200" stroke="#7fd4ff" stroke-width="5"/>
{circle_joint(130, 90)}{circle_joint(300, 70)}
{arrow(130, 90, 172, 62, "#ff6b6b", 2.5, "v")}
<text x="105" y="230" fill="#8899aa" font-size="12">ground</text>
<text x="95" y="150" fill="#cde" font-size="12">crank</text>
<text x="200" y="60" fill="#ffd166" font-size="12">coupler</text>
<text x="330" y="150" fill="#cde" font-size="12">rocker</text>
''', title="Four-bar linkage (crank-rocker)")

# stress / beam
diagrams["PR-STR-01"] = svg_wrap(f'''
<rect x="60" y="80" width="20" height="100" fill="#1d2c45" stroke="#7fd4ff" stroke-width="2"/>
<rect x="80" y="118" width="280" height="24" fill="#1d2c45" stroke="#cde" stroke-width="2"/>
{arrow(360, 130, 360, 175, "#ff6b6b", 3, "F")}
<text x="70" y="70" fill="#7fd4ff" font-size="12">wall (fixed)</text>
<text x="230" y="215" fill="#ffd166" font-size="13" text-anchor="middle">sigma = M*c/I - max at outer fibres</text>
<text x="230" y="237" fill="#8899aa" font-size="12" text-anchor="middle">cantilever: M(x) = F*(L-x)</text>
''', title="Bending stress in a cantilever")

# fatigue SN curve
diagrams["PR-FAT-01"] = svg_wrap('''
<line x1="70" y1="210" x2="420" y2="210" stroke="#8899aa" stroke-width="2"/>
<line x1="70" y1="210" x2="70" y2="40" stroke="#8899aa" stroke-width="2"/>
<polyline points="70,60 160,95 240,150 320,165 410,165" fill="none" stroke="#ffd166" stroke-width="3"/>
<line x1="70" y1="165" x2="410" y2="165" stroke="#ff6b6b" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="390" y="158" fill="#ff6b6b" font-size="12" text-anchor="end">endurance limit Se</text>
<text x="245" y="235" fill="#8899aa" font-size="12" text-anchor="middle">cycles N (log)</text>
<text x="30" y="130" fill="#8899aa" font-size="12">stress</text>
<text x="150" y="120" fill="#ffd166" font-size="12">stress concentration + rough finish shift curve DOWN</text>
''', title="S-N curve: fatigue life vs stress amplitude")

# bearing
diagrams["PR-BRG-01"] = svg_wrap(f'''
<circle cx="240" cy="130" r="85" fill="none" stroke="#cde" stroke-width="2"/>
<circle cx="240" cy="130" r="35" fill="none" stroke="#cde" stroke-width="2"/>
<circle cx="240" cy="55" r="11" fill="#1d2c45" stroke="#7fd4ff" stroke-width="2"/>
<circle cx="240" cy="205" r="11" fill="#1d2c45" stroke="#7fd4ff" stroke-width="2"/>
<circle cx="165" cy="130" r="11" fill="#1d2c45" stroke="#7fd4ff" stroke-width="2"/>
<circle cx="315" cy="130" r="11" fill="#1d2c45" stroke="#7fd4ff" stroke-width="2"/>
{arrow(240, 130, 240, 130, "#0000", 0)}
{arrow(150, 45, 190, 85, "#ff6b6b", 2.5, "radial load")}
{arrow(330, 220, 300, 190, "#7fd4ff", 2.5, "axial: only small (deep-groove)")}
<text x="240" y="250" fill="#ffd166" font-size="13" text-anchor="middle">L10 = (C/P)^3 million revolutions</text>
''', title="Deep-groove ball bearing")

# torsion
diagrams["PR-TOR-01"] = svg_wrap(f'''
<rect x="90" y="122" width="300" height="16" fill="#1d2c45" stroke="#cde" stroke-width="2"/>
{arrow(90, 130, 60, 105, "#ff6b6b", 2.5, "T")}
{arrow(390, 130, 420, 155, "#ff6b6b", 2.5, "T")}
<text x="240" y="105" fill="#ffd166" font-size="13" text-anchor="middle">tau_max = 16*T / (pi*d^3)</text>
<text x="240" y="180" fill="#8899aa" font-size="12" text-anchor="middle">double d -> 8x torsional strength</text>
''', title="Shaft torsion")

# fastener
diagrams["PR-FST-01"] = svg_wrap(f'''
<rect x="150" y="60" width="180" height="18" fill="#1d2c45" stroke="#cde" stroke-width="2"/>
<rect x="150" y="150" width="180" height="18" fill="#1d2c45" stroke="#cde" stroke-width="2"/>
<rect x="232" y="78" width="16" height="72" fill="#3a4a63" stroke="#7fd4ff" stroke-width="2"/>
<rect x="224" y="40" width="32" height="20" fill="#3a4a63" stroke="#7fd4ff" stroke-width="2"/>
<rect x="224" y="150" width="32" height="18" fill="#3a4a63" stroke="#7fd4ff" stroke-width="2"/>
{arrow(210, 50, 235, 50, "#ffd166", 2.5)}
{arrow(270, 50, 245, 50, "#ffd166", 2.5, "preload")}
<text x="240" y="205" fill="#ffd166" font-size="13" text-anchor="middle">clamp joint with preload; F_tight < 75% of proof load</text>
''', title="Bolted joint: preload clamps members")

# spring
diagrams["PR-SPR-01"] = svg_wrap(f'''
<path d="M 200 60 L 260 75 L 200 90 L 260 105 L 200 120 L 260 135 L 200 150 L 260 165 L 200 180" fill="none" stroke="#7fd4ff" stroke-width="4" stroke-linecap="round"/>
<line x1="160" y1="60" x2="160" y2="180" stroke="#8899aa" stroke-width="2" stroke-dasharray="4 4"/>
{arrow(320, 60, 320, 110, "#ff6b6b", 2.5, "F = k*x")}
{arrow(320, 180, 320, 130, "#ff6b6b", 2.5)}
<text x="300" y="225" fill="#ffd166" font-size="13" text-anchor="middle">U = 0.5*k*x^2; solid height limits stroke</text>
''', title="Compression spring: F = kx")

# thermal
diagrams["PR-THM-01"] = svg_wrap(f'''
<rect x="80" y="100" width="140" height="60" fill="#5b3a4a" stroke="#ff6b6b" stroke-width="2"/>
<rect x="240" y="100" width="140" height="60" fill="#1d2c45" stroke="#7fd4ff" stroke-width="2"/>
<text x="150" y="135" fill="#ffb3b3" font-size="13" text-anchor="middle">Al: a = 23 um/m-K</text>
<text x="310" y="135" fill="#9fd0ff" font-size="13" text-anchor="middle">Steel: a = 12 um/m-K</text>
{arrow(240, 90, 240, 60, "#ffd166", 2.5, "dT")}
<text x="240" y="210" fill="#ffd166" text-anchor="middle" font-size="13">dL = a*L*dT - bimetal joints bend or shear</text>
''', title="Differential thermal expansion")

# tolerance stack
diagrams["PR-TOL-01"] = svg_wrap(f'''
<rect x="70" y="110" width="120" height="40" fill="#1d2c45" stroke="#cde" stroke-width="2"/>
<rect x="190" y="110" width="100" height="40" fill="#1d2c45" stroke="#ffd166" stroke-width="2"/>
<rect x="290" y="110" width="120" height="40" fill="#1d2c45" stroke="#cde" stroke-width="2"/>
<text x="130" y="135" fill="#cde" font-size="12" text-anchor="middle">A +0/-0.1</text>
<text x="240" y="135" fill="#ffd166" font-size="12" text-anchor="middle">B +/-0.05</text>
<text x="350" y="135" fill="#cde" font-size="12" text-anchor="middle">C +/-0.1</text>
<text x="240" y="205" fill="#ffd166" font-size="13" text-anchor="middle">worst-case gap = sum of tolerances (0.35)</text>
<text x="240" y="225" fill="#8899aa" font-size="12" text-anchor="middle">statistical (RSS) is smaller: sqrt(sum ti^2)</text>
''', title="Tolerance stack-up")

# lubrication / wear
diagrams["PR-LUB-01"] = svg_wrap(f'''
<rect x="100" y="90" width="280" height="20" fill="#3a4a63" stroke="#cde"/>
<rect x="100" y="150" width="280" height="20" fill="#3a4a63" stroke="#cde"/>
<rect x="100" y="110" width="280" height="40" fill="#274b2a" opacity="0.8"/>
<text x="240" y="135" fill="#a5f0a5" font-size="13" text-anchor="middle">oil film - full-film lubrication</text>
{arrow(240, 65, 240, 90, "#ff6b6b", 2.5, "load")}
<text x="240" y="215" fill="#ffd166" font-size="13" text-anchor="middle">film failure -> asperity contact -> adhesive wear</text>
''', title="Lubrication regimes")

# assembly order
diagrams["PR-ASM-01"] = svg_wrap(f'''
<rect x="60" y="40" width="100" height="36" fill="#1d2c45" stroke="#cde"/><text x="110" y="63" fill="#cde" font-size="12" text-anchor="middle">1. housing</text>
<rect x="190" y="40" width="100" height="36" fill="#1d2c45" stroke="#cde"/><text x="240" y="63" fill="#cde" font-size="12" text-anchor="middle">2. bearing in</text>
<rect x="320" y="40" width="100" height="36" fill="#1d2c45" stroke="#cde"/><text x="370" y="63" fill="#cde" font-size="12" text-anchor="middle">3. shaft in</text>
<rect x="125" y="110" width="100" height="36" fill="#1d2c45" stroke="#ffd166"/><text x="175" y="133" fill="#ffd166" font-size="12" text-anchor="middle">4. gear on</text>
<rect x="255" y="110" width="100" height="36" fill="#1d2c45" stroke="#ffd166"/><text x="305" y="133" fill="#ffd166" font-size="12" text-anchor="middle">5. retention</text>
<line x1="160" y1="76" x2="185" y2="110" stroke="#8899aa"/><line x1="290" y1="76" x2="270" y2="110" stroke="#8899aa"/>
<line x1="370" y1="76" x2="320" y2="110" stroke="#8899aa"/><line x1="225" y1="146" x2="255" y2="146" stroke="#8899aa"/>
<text x="240" y="195" fill="#ffd166" font-size="13" text-anchor="middle">disassembly = reverse order; check hidden retainers</text>
''', title="Assembly sequence / disassembly dependencies")

# friction/lubrication (PR-FRI-01) reuse LUB visual
diagrams["PR-FRI-01"] = svg_wrap(f'''
<rect x="100" y="90" width="280" height="20" fill="#3a4a63" stroke="#cde"/>
<rect x="100" y="150" width="280" height="20" fill="#3a4a63" stroke="#cde"/>
<rect x="100" y="110" width="280" height="40" fill="#274b2a" opacity="0.8"/>
<text x="240" y="135" fill="#a5f0a5" font-size="13" text-anchor="middle">film - pair property, not material property</text>
{arrow(240, 65, 240, 90, "#ff6b6b", 2.5, "N")}
{arrow(160, 180, 320, 180, "#ffd166", 2.5, "F_f = mu*N")}
<text x="240" y="215" fill="#ffd166" font-size="13" text-anchor="middle">mu varies 2-5x with condition - never quote one number</text>
''', title="Friction and wear")

# stress/materials (PR-MAT-01): stress-strain style chart
diagrams["PR-MAT-01"] = svg_wrap('''
<line x1="70" y1="210" x2="420" y2="210" stroke="#8899aa" stroke-width="2"/>
<line x1="70" y1="210" x2="70" y2="40" stroke="#8899aa" stroke-width="2"/>
<polyline points="70,205 150,140 200,110 260,100 380,70" fill="none" stroke="#ffd166" stroke-width="3"/>
<circle cx="150" cy="140" r="5" fill="#ff6b6b"/>
<text x="160" y="150" fill="#ff6b6b" font-size="12">yield sigma_y</text>
<circle cx="380" cy="70" r="5" fill="#7fd4ff"/>
<text x="372" y="60" fill="#7fd4ff" font-size="12" text-anchor="end">UTS (fracture)</text>
<text x="240" y="235" fill="#8899aa" font-size="12" text-anchor="middle">strain</text>
<text x="30" y="130" fill="#8899aa" font-size="12">stress</text>
<text x="240" y="45" fill="#ffd166" font-size="12">E = slope (stiffness) - same for steel in tension/compression</text>
''', title="Material: stress-strain behaviour")

# shaft torsion (PR-SFT-01)
diagrams["PR-SFT-01"] = svg_wrap(f'''
<rect x="90" y="122" width="300" height="16" fill="#1d2c45" stroke="#cde" stroke-width="2"/>
{arrow(90, 130, 60, 105, "#ff6b6b", 2.5, "T")}
{arrow(390, 130, 420, 155, "#ff6b6b", 2.5, "T")}
{arrow(240, 70, 240, 118, "#7fd4ff", 2.5, "bending load F")}
<text x="240" y="180" fill="#ffd166" font-size="13" text-anchor="middle">tau = 16T/(pi d^3), sigma_b = 32M/(pi d^3)</text>
<text x="240" y="205" fill="#8899aa" font-size="12" text-anchor="middle">support at both ends; cantilever raises M fast</text>
''', title="Shaft: combined torsion + bending")

principles = [
 dict(id="PR-FBD-01", level="foundation", category="statics",
   title="Force, torque and free-body diagrams",
   simple="A free-body diagram isolates one part and draws every force and moment acting on it. If it is not accelerating, forces and moments sum to zero.",
   equations=["sum F = 0", "sum M = 0", "W = m*g"],
   variables={"F": "force (N)", "M": "moment (N*m)", "m": "mass (kg)", "g": "9.81 m/s^2"},
   visual="assets/diagrams/PR-FBD-01.svg",
   failure_modes=["missing a reaction force", "ignoring friction direction", "treating a moving part as static"],
   example="Gear on a shaft: weight of gear, belt pull, bearing reactions form a force couple the shaft bending must carry.",
   agent_use="Before proposing any load-bearing modification, enumerate supports and loads on the changed part; if any reaction is unknown, mark the analysis incomplete rather than guessing.",
   limits="Static equilibrium only. Dynamics, vibration and stress distribution need a solver or measured data; margin calls belong to a human engineer.",
   verify_with=["static hand calc", "PyNiteFEA beam/frame model", "CalculiX for continuum stress"]),
 dict(id="PR-DOF-01", level="foundation", category="kinematics",
   title="Degrees of freedom and constraints",
   simple="Every free body in a plane has 3 DOF (x, y, rotation). Each joint removes some. Fully-constrained means zero DOF left; a mechanism keeps exactly the motion you want.",
   equations=["Gruebler (planar): DOF = 3(n-1) - 2*j1 - j2"],
   variables={"n": "links incl. ground", "j1": "full joints (revolute/prismatic)", "j2": "half joints (cam/slider contact)"},
   visual="assets/diagrams/PR-DOF-01.svg",
   failure_modes=["under-constrained assembly drifts", "over-constrained assembly cannot be built or binds", "two bearings on one shaft misaligned -> binding"],
   example="A drawer on two slides is over-constrained if the slides are not parallel - it jams.",
   agent_use="Count DOF after adding/removing any joint. build123d Joint ranges give the intended motion; a modification that removes a needed DOF or adds a conflict must be flagged.",
   limits="Rigid-body kinematics. Elastic deformation, clearances and manufacturing error require measurement or simulation.",
   verify_with=["build123d joint graph", "FreeCAD Assembly solver (Ondsel)"]),
 dict(id="PR-LVR-01", level="foundation", category="statics",
   title="Levers and moment balance",
   simple="A lever trades distance for force. Force times distance from the pivot must balance on both sides.",
   equations=["F1*d1 = F2*d2", "MA = d1/d2"],
   variables={"F": "force (N)", "d": "perpendicular distance to pivot (mm)", "MA": "mechanical advantage"},
   visual="assets/diagrams/PR-LVR-01.svg",
   failure_modes=["pivot placed at the load point - no advantage", "ignoring the lever's own bending", "pivot bearing not sized for the reaction force"],
   example="Bolt cutter: 25 mm handle to 5 mm jaw gives MA 5; pivot pin carries the full combined reaction.",
   agent_use="When modifying link geometry, recompute the pivot reaction; larger MA means larger pivot load, not a free lunch.",
   limits="Rigid-body assumption; real links flex and pivots have friction.",
   verify_with=["static moment calc"]),
 dict(id="PR-GTR-01", level="foundation", category="gears",
   title="Gears, ratios and centre distance",
   simple="Meshing gears must share the same module (tooth size). Speed ratio is the inverse tooth ratio; torque scales the other way.",
   equations=["C = m*(z1+z2)/2", "i = z2/z1", "torque_out = torque_in * i * eta"],
   variables={"m": "module (mm)", "z": "tooth count", "C": "centre distance (mm)", "eta": "mesh efficiency ~0.94-0.97"},
   visual="assets/diagrams/PR-GTR-01.svg",
   failure_modes=["mixing modules - teeth destroy each other", "wrong centre distance - interference or backlash", "undercut on small pinions (z < 17 at 20 deg PA)"],
   example="18T driving 30T at module 2: ratio 1.667, centre distance 48 mm exactly.",
   agent_use="Any change to z or m must update centre distance and check every meshing partner in the assembly graph. Use the KB compatibility rule: modules must match exactly.",
   limits="Kinematics and ratio only. Tooth strength (Lewis), contact stress and lubrication need real calculation or datasheets.",
   verify_with=["centre-distance check (agent-side)", "FCGear/KISSsoft for tooth geometry", "datasheet for ratings"]),
 dict(id="PR-BLT-01", level="foundation", category="drives",
   title="Belt and pulley drives",
   simple="Belts transmit motion over distance. Flat/round belts can slip; timing belts (GT2 etc.) have teeth and cannot slip.",
   equations=["i = D2/D1", "belt_length approx 2C + pi/2*(D1+D2) + (D2-D1)^2/(4C)"],
   variables={"D": "pitch diameter", "C": "centre distance", "i": "ratio"},
   visual="assets/diagrams/PR-BLT-01.svg",
   failure_modes=["insufficient tension - ratcheting", "over-tension - bearing overload", "misalignment - belt walks off the pulley"],
   example="3D printer GT2 16T-to-16T is 1:1; 16T-to-32T halves speed and doubles torque.",
   agent_use="When swapping pulleys, recompute belt length; a change that breaks the approximate-length formula within +/-2% needs a tensioner.",
   limits="Length is an approximation; exact belt math and tension ratings come from manufacturer data.",
   verify_with=["belt-length check (agent-side)", "vendor datasheet"]),
 dict(id="PR-SFT-01", level="foundation", category="shafts",
   title="Shafts: torsion and bending",
   simple="Shafts carry torque (twist) and often bending (transverse loads). Stress grows with the inverse cube of diameter - small size changes matter hugely.",
   equations=["tau = 16*T/(pi*d^3)", "sigma_b = 32*M/(pi*d^3)"],
   variables={"T": "torque (N*mm)", "M": "bending moment (N*mm)", "d": "diameter (mm)"},
   visual="assets/diagrams/PR-TOR-01.svg",
   failure_modes=["keyway/notch as stress riser", "cantilever mounting", "diameter step without fillet"],
   example="6 mm shaft vs 8 mm shaft: 8 mm carries ~2.4x the torque at the same stress.",
   agent_use="A diameter reduction request triggers a torsion/bending sanity check against the stated load; refuse to certify, present numbers only.",
   limits="Solid round shaft, elastic range. Fatigue, keys and couplings need more analysis.",
   verify_with=["hand calc", "CalculiX for stepped shafts"]),
 dict(id="PR-BRG-01", level="foundation", category="bearings",
   title="Bearings and supported rotation",
   simple="A bearing lets a shaft rotate while holding it radially (and often axially). Life scales with (load rating / applied load)^3 for ball bearings.",
   equations=["L10 = (C/P)^3 million revs"],
   variables={"C": "dynamic load rating (N, from datasheet)", "P": "equivalent applied load (N)"},
   visual="assets/diagrams/PR-BRG-01.svg",
   failure_modes=["contamination -> brinelling", "overload -> spalling", "electrical arcing (VFDs)", "press-fit too tight -> lost internal clearance"],
   example="608ZZ in a printed housing: printed seat is usually slightly oversize; a too-tight seat preloads the bearing to early failure.",
   agent_use="Never invent a C rating. If the user asks for life, require a datasheet value; otherwise present the formula with P only.",
   limits="Catalogue-dependent. Lubrication condition and temperature change everything.",
   verify_with=["datasheet lookup (human)", "formula check (agent)"]),
 dict(id="PR-FST-01", level="foundation", category="fasteners",
   title="Fasteners and preload",
   simple="A tightened bolt stretches like a spring; the stretch clamps the parts. Most bolted joints fail by loosening or by overtightening, not by breaking.",
   equations=["T = K*F*d (K ~ 0.2 dry)", "clamp < 75% proof load"],
   variables={"T": "torque (N*m)", "F": "preload (N)", "d": "nominal dia (m)", "K": "nut factor"},
   visual="assets/diagrams/PR-FST-01.svg",
   failure_modes=["vibration loosening - use lock feature", "thread galling (stainless)", "over-torque strip"],
   example="M5 bolt torqued to ~5 N*m (dry K=0.2) gives ~5 kN clamp - enough for most small brackets.",
   agent_use="When a fastener change is proposed, check diameter class and mate's hole size; flag any torque requirement as human-verified.",
   limits="K varies 0.1-0.3 with lubrication; threaded-joint standards (VDI 2230) needed for real design.",
   verify_with=["torque tables (human)", "QCAD library hole sizes"]),
 dict(id="PR-SPR-01", level="foundation", category="springs",
   title="Springs: stiffness and energy",
   simple="A spring pushes back proportionally to how much you compress it. Stiffness k depends on wire diameter, coil diameter, number of coils and material.",
   equations=["F = k*x", "U = 0.5*k*x^2", "k_helix = G*d^4 / (8*n*D^3)"],
   variables={"k": "rate (N/mm)", "x": "deflection (mm)", "G": "shear modulus", "n": "active coils", "D": "mean coil dia"},
   visual="assets/diagrams/PR-SPR-01.svg",
   failure_modes=["solid-height collision", "stress relaxation at temperature", "surge (dynamic resonance)"],
   example="Pen spring vs valve spring: same shape, k differs 100x via wire diameter to the 4th power.",
   agent_use="Never assume k. The KB spring stub deliberately has rate=null; a rate must come from the wire-coil formula with real dimensions or a datasheet.",
   limits="Linear range only; buckling and surge need checks.",
   verify_with=["coil formula (agent, with given dims)", "measurement (human)"]),
 dict(id="PR-MAT-01", level="foundation", category="materials",
   title="Materials: stiffness, strength and failure modes",
   simple="Stiffness (E) resists stretch; strength (yield) resists permanent dent; toughness resists cracking. Steel is ~3x stiffer than aluminium but 3x denser - the shapes differ, not just the material.",
   equations=["sigma = F/A", "epsilon = sigma/E", "ductile: yield then neck; brittle: fracture at UTS"],
   variables={"E": "Young's modulus (GPa)", "sigma_y": "yield strength (MPa)", "K_IC": "fracture toughness"},
   visual="assets/diagrams/PR-STR-01.svg",
   failure_modes=["yield (permanent set)", "brittle fracture (printed plastics, low T)", "creep (plastics under sustained load)"],
   example="PLA brackets sag under sustained load at room temperature (creep); PETG or aluminium for loaded brackets.",
   agent_use="Any material swap must compare E, sigma_y, density and temperature limits from the KB materials table; unknown material = refuse, ask for datasheet.",
   limits="Nominal handbook values only; batch, direction (anisotropy of prints) and processing vary.",
   verify_with=["materials table (KB)", "datasheet (human)"]),
 dict(id="PR-FRI-01", level="foundation", category="tribology",
   title="Friction, lubrication and wear",
   simple="Friction resists sliding in proportion to normal force. Lubrication replaces metal-on-metal contact with fluid film; wear follows when the film fails.",
   equations=["F_f = mu*N", "PV limit for bushings"],
   variables={"mu": "friction coefficient (pair-dependent!)", "N": "normal force", "P": "pressure", "V": "sliding speed"},
   visual="assets/diagrams/PR-LUB-01.svg",
   failure_modes=["dry running a plain bush", "wrong grease - plastics crack (polycarbonate + mineral oil)", "fretting under vibration"],
   example="3D-printed bushings run quietly in PTFE-lined or oil-impregnated bronze; direct steel-on-PLA galls.",
   agent_use="Friction is a pair property - never quote a single 'friction of steel'. Use pair tables or state a range and mark unverified.",
   limits="mu varies 2-5x with condition; PV limits are vendor data.",
   verify_with=["tribology pair table (KB, cited)", "vendor data"]),
 dict(id="PR-TOL-01", level="foundation", category="manufacturing",
   title="Tolerances, fits and stack-up",
   simple="No dimension is exact. Stacked tolerances add up; fit classes (H7/g6 etc.) decide whether parts slide, locate or press.",
   equations=["worst case = sum of |t_i|", "RSS = sqrt(sum t_i^2)"],
   variables={"t_i": "individual tolerance", "H7": "hole tolerance class", "g6": "shaft class (sliding fit)"},
   visual="assets/diagrams/PR-TOL-01.svg",
   failure_modes=["all tolerances stacked - interference impossible to assemble", "3D-printed holes shrink - use polyholes/undersize", "tolerance on both flanges of a gasket - leak path"],
   example="Two flanges each +/-0.1 mm with a 0.15 mm gasket may leak at worst case; spec the gasket first.",
   agent_use="Any added interface adds tolerance to the stack; run the stack check on the assembly's critical dimension and warn before worst case exceeds the gap.",
   limits="Simple 1D stacks only; 2D/3D stacks and GD&T need CAD-level analysis.",
   verify_with=["stack check (agent)", "fit tables (KB)"]),
 dict(id="PR-ASM-01", level="foundation", category="assembly",
   title="Assembly order and disassembly dependencies",
   simple="Assemblies have an order: what must be inside goes in first. Disassembly is the reverse, and hidden retainers (circlips, set screws, threadlocker) block parts.",
   equations=[],
   variables={"BOM": "bill of materials", "precedence": "which part before which"},
   visual="assets/diagrams/PR-ASM-01.svg",
   failure_modes=["bearing trapped behind a shoulder with no puller access", "fastener unreachable after next step", "gasket omitted - leak"],
   example="Press bearing into housing BEFORE inserting the shaft; afterwards the shoulder blocks the press.",
   agent_use="The KB assembly graph stores install_order and blockers; any proposed modification must preserve a valid topological order or list the required full teardown.",
   limits="Graph is static; actual service procedure should follow the OEM manual for real equipment.",
   verify_with=["assembly graph check (agent)", "human service manual"]),
 dict(id="PR-4BAR-01", level="advanced", category="linkages",
   title="Four-bar linkages and motion transmission",
   simple="Four bars, four pins: fix one bar (ground) and the others move in a determined path. Grashof's rule says which link can fully rotate.",
   equations=["Grashof: s + l <= p + q"],
   variables={"s,l": "shortest/longest link", "p,q": "other two"},
   visual="assets/diagrams/PR-4BAR-01.svg",
   failure_modes=["non-Grashof crank cannot pass through dead points", "transmission angle < 40 deg - high joint forces", "coupler path has cusps"],
   example="Windshield wiper: crank-rocker converts motor rotation into a sweep.",
   agent_use="When link lengths change, re-check Grashof and keep the transmission angle above ~40 deg through the working arc; else flag as unverified geometry.",
   limits="Position kinematics only; velocities/accelerations need solving over the cycle (Pyslvs or numeric).",
   verify_with=["Grashof + angle check (agent)", "Pyslvs path solve (optional, AGPL)"]),
 dict(id="PR-FAT-01", level="advanced", category="failure",
   title="Fatigue, stress concentration and safety factor",
   simple="Parts break at loads far below their static strength if the load repeats. Cracks start at stress concentrations: holes, corners, scratches.",
   equations=["n = S_allow / sigma_actual", "Kt: geometric concentration factor", "Se: endurance limit (~0.5*UTS steel)"],
   variables={"n": "safety factor", "Kt": "notch factor", "Se": "endurance limit"},
   visual="assets/diagrams/PR-FAT-01.svg",
   failure_modes=["sharp inside corners", "thread runout in the stress zone", "polishing improves life; notching kills it"],
   example="Fillet radius at a shaft shoulder changes fatigue life by orders of magnitude.",
   agent_use="Any geometry change that adds a sharp corner in a cyclic-load path triggers a fatigue warning; never output a numeric life without a full load-history and material S-N data.",
   limits="S-N curves are material- and condition-specific; real fatigue design needs standards (FKM etc.).",
   verify_with=["CalculiX stress field (verified FEA)", "human review of load history"]),
 dict(id="PR-THM-01", level="advanced", category="thermal",
   title="Thermal expansion and material pairing",
   simple="Materials grow when heated, each at its own rate. Joining two different materials means the joint sees the difference.",
   equations=["dL = alpha*L*dT"],
   variables={"alpha": "CTE (um/m-K)", "dT": "temperature change (K)"},
   visual="assets/diagrams/PR-THM-01.svg",
   failure_modes=["aluminium bolted to steel - bolt loosens when hot", "bearing housing shrink fit lost when hot", "glass-metal seals crack"],
   example="An aluminium plate on a steel frame 1 m long and 50 K hotter is 0.55 mm longer - enough to bind slides.",
   agent_use="Cross-material interfaces with expected dT > 30 K trigger a CTE comparison and a slip-joint/slot suggestion.",
   limits="Uniform-temperature assumption; gradients need heat-transfer analysis.",
   verify_with=["CTE table (KB)", "thermal FEA (future)"]),
]

with open(os.path.join(DIA, "_readme.txt"), "w") as f:
    f.write("Diagrams authored for this KB (CC0). Generated by tools/gen_principles.py.\n")

count = 0
for p in principles:
    # write diagram svg
    with open(os.path.join(DIA, p["id"] + ".svg"), "w") as f:
        f.write(diagrams[p["id"]])
    p["schema"] = "0.1"
    p["type"] = "principle"
    p["license"] = "CC0-1.0"
    p["provenance"] = {"source": "authored for this KB; standard ME textbook content (Shigley-level), no text copied", "license": "CC0-1.0"}
    with open(os.path.join(PRI, p["id"] + ".json"), "w") as f:
        json.dump(p, f, indent=1)
    count += 1
with open(os.path.join(PRI, "_index.json"), "w") as f:
    json.dump({"schema": "0.1", "count": count,
               "foundation": [p["id"] for p in principles if p["level"] == "foundation"],
               "advanced": [p["id"] for p in principles if p["level"] == "advanced"]}, f, indent=1)
print(f"wrote {count} principles + {len(diagrams)} svg diagrams")
