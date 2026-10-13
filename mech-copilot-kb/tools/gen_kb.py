#!/usr/bin/env python3
"""Generate the mechanical-copilot knowledgebase.

Creates:
  kb/components/*.json        - 12 component entries (schema v0.1)
  kb/assets/cad/*.step|stl    - STEP (editable BREP) + STL + GLB previews
  kb/assets/previews/*.glb    - three.js-loadable glTF for the 2.5D viewer
  kb/assets/diagrams/*.svg    - 2.5D-style principle/component diagrams
Reuses: bearing-608zz.step and gt2-pulley-16t.step (CC-BY 3.0, FreeCAD-library).
Requires: build123d (Apache-2.0) in the active python.
"""
import json, math, os, sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "kb")
CAD = os.path.join(ROOT, "assets", "cad")
PRE = os.path.join(ROOT, "assets", "previews")
DIA = os.path.join(ROOT, "assets", "diagrams")
COMP = os.path.join(ROOT, "components")

from build123d import *  # noqa: F403
from build123d.exporters3d import export_step, export_stl, export_gltf
from build123d import import_step

LICENSE_KB = "CC0-1.0"
SCHEMA = "0.1"


def save_all(cid, part, params):
    part_step = os.path.join(CAD, f"{cid}.step")
    export_step(part, part_step)
    export_stl(part, os.path.join(CAD, f"{cid}.stl"), tolerance=0.1)
    export_gltf(part, os.path.join(PRE, f"{cid}.glb"))
    bb = part.bounding_box()
    return {
        "asset": {
            "step": f"assets/cad/{cid}.step",
            "stl": f"assets/cad/{cid}.stl",
            "preview_glb": f"assets/previews/{cid}.glb",
        },
        "geometry": {
            "bbox_mm": [round(bb.size.X, 3), round(bb.size.Y, 3), round(bb.size.Z, 3)],
            "volume_mm3": round(part.volume, 1),
        },
        "parameters": params,
    }


# ---------------------------------------------------------------- primitives
def gear_body(teeth, module, thickness, bore, hub_d=0, hub_h=0):
    """Simplified spur gear: disc + tooth bumps + bore (+ optional hub).
    NOTE: tooth profile is a visual placeholder, NOT an involute. Fine for
    layout/teaching demos; for printable gears use FCGear (GPL-3.0)."""
    pcd = module * teeth
    with BuildPart() as bp:
        with BuildSketch():
            Circle(pcd / 2 - module)
            with PolarLocations(pcd / 2, teeth):
                with Locations((0, module / 1.15)):
                    Circle(module / 1.8, mode=Mode.ADD)
        extrude(amount=thickness)
        if hub_d > 0:
            with Locations((0, 0, thickness)):
                Cylinder(hub_d / 2, hub_h, align=(Align.CENTER, Align.CENTER, Align.MIN))
        Hole(bore / 2)
    return bp.part


def pipe_flange(dn, pn_class, length, thickness, bolt_d):
    with BuildPart() as bp:
        Cylinder(dn / 2, length, align=(Align.CENTER, Align.CENTER, Align.MIN))
        with Locations((0, 0, length)):
            Cylinder(dn / 2 + 8, thickness, align=(Align.CENTER, Align.CENTER, Align.MIN))
        with Locations((0, 0, length + thickness)):
            Cylinder(dn / 2 + 2, 3, align=(Align.CENTER, Align.CENTER, Align.MIN))
        # 4-bolt pattern on the flange
        with Locations((0, 0, length + thickness / 2)):
            with PolarLocations(dn / 2 + 5, 4):
                Hole(bolt_d / 2)
    return bp.part


def four_bar(links=(60.0, 150.0, 120.0, 80.0)):
    """Crank-rocker linkage: ground(l0) - crank(l1) - coupler(l2) - rocker(l3)."""
    l0, l1, l2, l3 = links
    with BuildPart() as bp:
        with BuildSketch(Plane.XY):
            with Locations((l0 / 2, 0)):
                Rectangle(l0, 10)
        extrude(amount=5)  # ground link
        with BuildSketch(Plane.XY.offset(10)):
            with Locations((l1 / 2, 0)):
                Rectangle(l1, 8)
        extrude(amount=5)  # crank
    return bp.part


components = []

# ---------------------------------------------------------------- 1. spur gear
t, m, th, bore = 18, 2.0, 6.0, 6.0
g = gear_body(t, m, th, bore)
meta = save_all("spur-gear-18t-m2", g, {"teeth": t, "module_mm": m, "thickness_mm": th, "bore_dia_mm": bore})
meta.update({
    "id": "spur-gear-18t-m2", "type": "component", "category": "gears",
    "label": "Spur gear 18T module 2",
    "summary": "External spur gear, 18 teeth, module 2 mm. Meshes with any module-2 spur gear; centre distance = m*(z1+z2)/2.",
    "interfaces": [
        {"kind": "bore", "spec": {"diameter_mm": 6.0, "fit": "H7/k6 nominal", "for": "shaft-6mm"}},
        {"kind": "gear_mesh", "spec": {"module_mm": 2.0, "pressure_angle_deg": 20, "for": "any module-2 external spur gear"}},
    ],
    "connections": {
        "accepts": ["shaft-6mm"], "mates_with": ["spur-gear-30t-m2"],
        "joint": "rigid-to-shaft + mesh-contact",
    },
    "governing": {"principles": ["PR-GTR-01"], "equations": [
        "centre_distance = m*(z1+z2)/2", "ratio = z2/z1", "torque_out = torque_in * (z2/z1) * efficiency"]},
    "checks": ["centre distance must equal m*(z1+z2)/2", "efficiency 0.94-0.97 per mesh (lubricated steel)"],
    "provenance": {"source": "authored for this KB (build123d)", "license": LICENSE_KB,
                   "note": "tooth profile simplified, not involute"},
})
components.append({"id": meta["id"], **meta})

# ---------------------------------------------------------------- 2. big gear
t, m = 30, 2.0
g2 = gear_body(t, m, th, bore)
meta = save_all("spur-gear-30t-m2", g2, {"teeth": t, "module_mm": m, "thickness_mm": th, "bore_dia_mm": bore})
meta.update({
    "id": "spur-gear-30t-m2", "type": "component", "category": "gears",
    "label": "Spur gear 30T module 2",
    "summary": "Output gear for the 18T/30T demo train. Ratio 30/18 = 1.667, centre distance 48 mm.",
    "interfaces": [
        {"kind": "bore", "spec": {"diameter_mm": 6.0, "for": "shaft-6mm"}},
        {"kind": "gear_mesh", "spec": {"module_mm": 2.0, "for": "spur-gear-18t-m2"}},
    ],
    "connections": {"accepts": ["shaft-6mm"], "mates_with": ["spur-gear-18t-m2"], "joint": "rigid-to-shaft + mesh-contact"},
    "governing": {"principles": ["PR-GTR-01"]},
    "checks": ["centre distance 48.0 mm"],
    "provenance": {"source": "authored for this KB (build123d)", "license": LICENSE_KB},
})
components.append({"id": meta["id"], **meta})

# ---------------------------------------------------------------- 3. shaft
sh = Cylinder(radius=3, height=40, align=(Align.CENTER, Align.CENTER, Align.CENTER))
meta = save_all("shaft-6mm", sh, {"diameter_mm": 6.0, "length_mm": 40.0})
meta.update({
    "id": "shaft-6mm", "type": "component", "category": "shafts",
    "label": "Shaft dia 6 mm",
    "summary": "Plain transmission shaft, 6 mm dia. Fits gear bores and 608ZZ inner race (via 6 mm sleeve).",
    "interfaces": [
        {"kind": "cylindrical", "spec": {"diameter_mm": 6.0, "length_mm": 40.0, "for": "gear bores, bearing 608ZZ (with sleeve)"}},
    ],
    "connections": {"accepts": [], "mates_with": ["spur-gear-18t-m2", "spur-gear-30t-m2", "bearing-608zz"], "joint": "revolute-in-bearing"},
    "governing": {"principles": ["PR-SFT-01", "PR-BRG-01"], "equations": ["torsion: tau = 16*T/(pi*d^3)", "bending: sigma = 32*M/(pi*d^3)"]},
    "checks": ["d/dt stress check before load claims", "bear at two points; cantilever mount raises deflection fast"],
    "provenance": {"source": "authored for this KB (build123d)", "license": LICENSE_KB},
})
components.append({"id": meta["id"], **meta})

# ---------------------------------------------------------------- 4. bearing (REUSED)
br = import_step(os.path.join(CAD, "bearing-608zz.step"))
bb = br.bounding_box()
meta = {
    "id": "bearing-608zz", "type": "component", "category": "bearings",
    "label": "Ball bearing 608ZZ (8x22x7)",
    "summary": "Standard 608ZZ sealed ball bearing: 8 mm bore, 22 mm OD, 7 mm wide. The most common hobby/RepRap bearing.",
    "interfaces": [
        {"kind": "bore", "spec": {"diameter_mm": 8.0, "for": "shaft-8mm (or 6mm shaft with sleeve)"}},
        {"kind": "housing_seat", "spec": {"outer_diameter_mm": 22.0, "for": "housing bore H7"}},
    ],
    "connections": {"accepts": ["shaft-6mm"], "mates_with": ["housing-plate"], "joint": "revolute-permitting"},
    "geometry": {"bbox_mm": [round(bb.size.X, 3), round(bb.size.Y, 3), round(bb.size.Z, 3)], "volume_mm3": round(br.volume, 1)},
    "parameters": {"bore_dia_mm": 8.0, "outer_dia_mm": 22.0, "width_mm": 7.0},
    "asset": {"step": "assets/cad/bearing-608zz.step", "preview_glb": "assets/previews/bearing-608zz.glb"},
    "governing": {"principles": ["PR-BRG-01"], "equations": ["L10 = (C/P)^3 million revs (ball bearings)"]},
    "checks": ["dynamic load rating C approx 1.8-3.3 kN depending on brand - do not quote without datasheet"],
    "provenance": {"source": "FreeCAD/FreeCAD-library Mechanical Parts/Bearings/608ZZ", "license": "CC-BY-3.0",
                   "url": "https://github.com/FreeCAD/FreeCAD-library", "note": "geometry reused as-is; metadata authored"},
}
with open(os.path.join(PRE, "bearing-608zz.glb"), "wb") as f:
    pass  # reuse: export from imported shape for preview
export_gltf(br, os.path.join(PRE, "bearing-608zz.glb"))
components.append(meta)

# ---------------------------------------------------------------- 5. pulley (REUSED)
pu = import_step(os.path.join(CAD, "gt2-pulley-16t.step"))
bb = pu.bounding_box()
meta = {
    "id": "pulley-gt2-16t", "type": "component", "category": "drives",
    "label": "GT2 timing pulley 16T (6 mm belt)",
    "summary": "16-tooth GT2 timing pulley for 6 mm belt. Pitch dia = 16*2 = ~10.2 mm? No: GT2 pitch = 2 mm, PD = 16*2/pi? Use vendor datasheet for exact PD.",
    "interfaces": [
        {"kind": "bore", "spec": {"diameter_mm": 5.0, "for": "shaft-5mm/6mm with grub"}},
        {"kind": "belt_track", "spec": {"profile": "GT2", "belt_width_mm": 6.0, "for": "GT2 belt"}},
    ],
    "connections": {"accepts": ["shaft-6mm"], "mates_with": ["pulley-gt2-16t", "belt-gt2"], "joint": "rigid-to-shaft + belt-coupling"},
    "geometry": {"bbox_mm": [round(bb.size.X, 3), round(bb.size.Y, 3), round(bb.size.Z, 3)], "volume_mm3": round(pu.volume, 1)},
    "parameters": {"teeth": 16, "belt": "GT2", "belt_width_mm": 6.0},
    "asset": {"step": "assets/cad/gt2-pulley-16t.step", "preview_glb": "assets/previews/pulley-gt2-16t.glb"},
    "governing": {"principles": ["PR-BLT-01"], "equations": ["ratio = z2/z1", "belt speed = PD * omega"]},
    "checks": ["confirm pitch dia from datasheet before ratio math", "no backlashes: timing belts positive-drive"],
    "provenance": {"source": "FreeCAD/FreeCAD-library Mechanical Parts/Pulleys/GT2_16T", "license": "CC-BY-3.0",
                   "url": "https://github.com/FreeCAD/FreeCAD-library", "note": "geometry reused; PD check flagged"},
}
export_gltf(pu, os.path.join(PRE, "pulley-gt2-16t.glb"))
components.append(meta)

# ---------------------------------------------------------------- 6. pipe flange DN25
fl = pipe_flange(25, "PN16", 40.0, 8.0, 6.0)
meta = save_all("pipe-flange-dn25", fl, {"DN": 25, "length_mm": 40.0, "flange_thickness_mm": 8.0, "bolt_dia_mm": 6.0})
meta.update({
    "id": "pipe-flange-dn25", "type": "component", "category": "piping",
    "label": "Pipe stub with flange DN25 (demo)",
    "summary": "DN25 pipe stub with 4-bolt flange for the pipe-and-valve demo assembly. Simplified flange geometry (no standard traceability).",
    "interfaces": [
        {"kind": "flange_face", "spec": {"DN": 25, "bolt_pattern": 4, "bolt_dia_mm": 6.0, "for": "valve-body-dn25 or another flange"}},
    ],
    "connections": {"accepts": ["valve-body-dn25"], "mates_with": ["valve-body-dn25"], "joint": "bolted-flange + gasket"},
    "governing": {"principles": ["PR-ASM-01", "PR-FST-01"]},
    "checks": ["real installations must use the applicable flange standard (e.g. EN 1092) - this part is demo-only"],
    "provenance": {"source": "authored for this KB (build123d)", "license": LICENSE_KB, "note": "not a standard-traceable flange"},
})
components.append(meta)

# ---------------------------------------------------------------- 7. valve body
vb = pipe_flange(25, "PN16", 60.0, 8.0, 6.0)
with BuildPart() as vbp:
    Box(46, 34, 30)
    Cylinder(radius=12.5, height=70, align=(Align.CENTER, Align.CENTER, Align.CENTER), mode=Mode.SUBTRACT)
valve_body = vbp.part
export_step(valve_body, os.path.join(CAD, "valve-body-dn25.step"))
export_stl(valve_body, os.path.join(CAD, "valve-body-dn25.stl"), tolerance=0.1)
export_gltf(valve_body, os.path.join(PRE, "valve-body-dn25.glb"))
bbl = valve_body.bounding_box()
meta = {
    "id": "valve-body-dn25", "type": "component", "category": "piping",
    "label": "Valve body DN25 (demo)",
    "summary": "Simplified valve body for the pipe-and-valve demo: flanged both ends, DN25 bore.",
    "interfaces": [
        {"kind": "flange_face", "spec": {"DN": 25, "bolt_pattern": 4, "for": "pipe-flange-dn25"}},
    ],
    "connections": {"accepts": ["pipe-flange-dn25"], "mates_with": ["pipe-flange-dn25"], "joint": "bolted-flange + gasket"},
    "geometry": {"bbox_mm": [round(bbl.size.X, 3), round(bbl.size.Y, 3), round(bbl.size.Z, 3)], "volume_mm3": round(valve_body.volume, 1)},
    "parameters": {"DN": 25, "face_to_face_mm": 60.0},
    "asset": {"step": "assets/cad/valve-body-dn25.step", "stl": "assets/cad/valve-body-dn25.stl", "preview_glb": "assets/previews/valve-body-dn25.glb"},
    "governing": {"principles": ["PR-ASM-01"]},
    "checks": ["demo part only"],
    "provenance": {"source": "authored for this KB (build123d)", "license": LICENSE_KB},
}
components.append(meta)

# ---------------------------------------------------------------- 8-12. simple reusable parts
def _simple(cid, label, category, summary, part, params, accepts, mates, joint, principles, extra_checks=None):
    meta = save_all(cid, part, params)
    meta.update({
        "id": cid, "type": "component", "category": category, "label": label, "summary": summary,
        "interfaces": [], "connections": {"accepts": accepts, "mates_with": mates, "joint": joint},
        "governing": {"principles": principles},
        "checks": extra_checks or [],
        "provenance": {"source": "authored for this KB (build123d)", "license": LICENSE_KB},
    })
    components.append(meta)
    return meta

spring = Cylinder(radius=6, height=30)
_simple("spring-stub", "Compression spring stub", "springs",
        "Visual spring placeholder for demo scenes (not a validated spring).",
        spring, {"outer_dia_mm": 12, "free_length_mm": 30, "rate_N_per_mm": None},
        [], ["shaft-6mm"], "compression", ["PR-SPR-01"],
        ["rate_N_per_mm deliberately unset - spring rate needs wire dia/coils/material or a datasheet"])

lever = Cylinder(radius=3, height=80)
_simple("lever-arm-80", "Lever arm 80 mm", "linkages",
        "Rigid lever arm for the four-bar demo.",
        lever, {"length_mm": 80.0, "pivot_dia_mm": 6.0},
        ["shaft-6mm"], ["lever-arm-80"], "revolute-pins", ["PR-LVR-01", "PR-FBD-01"])

link = Cylinder(radius=3, height=120)
_simple("coupler-link-120", "Coupler link 120 mm", "linkages",
        "Coupler link for the four-bar demo.",
        link, {"length_mm": 120.0, "pivot_dia_mm": 6.0},
        ["shaft-6mm"], ["lever-arm-80"], "revolute-pins", ["PR-4BAR-01"])

with BuildPart() as hb:
    Box(40, 40, 8)
    with Locations((0, 0, 8)):
        Cylinder(radius=11, height=4, align=(Align.CENTER, Align.CENTER, Align.MIN))
    with Locations((0, 0, 4)):
        Hole(11.05)
housing = hb.part
_simple("housing-plate", "Bearing housing plate", "bearings",
        "Plate with a 608 seat for the gear-train demo.",
        housing, {"plate_mm": [40, 40, 8], "seat_dia_mm": 22.0},
        ["bearing-608zz"], [], "press-seat", ["PR-BRG-01"],
        ["seat tolerance H7 assumed - verify before fit claims"])

with BuildPart() as pst:
    Cylinder(radius=3, height=25, align=(Align.CENTER, Align.CENTER, Align.MIN))
pin = pst.part
_simple("pin-6mm", "Clevis pin 6 mm", "fasteners",
        "Plain pin used as linkage pivot.",
        pin, {"diameter_mm": 6.0, "length_mm": 25.0},
        [], ["lever-arm-80", "coupler-link-120"], "sliding-pin", ["PR-ASM-01", "PR-FST-01"])

# ---------------------------------------------------------------- write JSON
os.makedirs(COMP, exist_ok=True)
index = []
for c in components:
    with open(os.path.join(COMP, f"{c['id']}.json"), "w") as f:
        json.dump(c, f, indent=1)
    index.append({"id": c["id"], "label": c["label"], "category": c["category"]})
with open(os.path.join(ROOT, "components", "_index.json"), "w") as f:
    json.dump({"schema": SCHEMA, "count": len(components), "components": index}, f, indent=1)
print(f"wrote {len(components)} components + index")
