#!/usr/bin/env python3
"""Write kb/assemblies/*.json, kb/scenarios/*.json, kb/validation_rules.json."""
import json, os

ROOT = os.path.join(os.path.dirname(__file__), "..", "kb")

# ------------------------------------------------------------------ assemblies
geartrain = {
  "id": "ASM-GEARTRAIN-01", "type": "assembly", "label": "Parallel-shaft gear train (18T -> 30T)",
  "category": "drives",
  "summary": "Two spur gears on parallel shafts in a housing plate. Demonstrates ratio, centre-distance and bearing constraints. Built from KB components; tooth geometry simplified.",
  "parameters": {
    "centre_distance_mm": {"value": 48.0, "equation": "m*(z1+z2)/2", "tolerance": "±0.05 mm", "verified": "exact arithmetic"},
    "ratio": {"value": 1.667, "equation": "z2/z1 = 30/18", "verified": "exact arithmetic"},
    "efficiency_per_mesh": {"value": None, "range": [0.94, 0.97], "note": "literature range for lubricated steel spur gears; not measured", "verified": False}
  },
  "graph": {
    "parts": [
      {"part": "housing-plate", "quantity": 1, "role": "ground"},
      {"part": "bearing-608zz", "quantity": 2, "role": "support", "note": "one per gear axis"},
      {"part": "shaft-6mm", "quantity": 2, "role": "shaft"},
      {"part": "spur-gear-18t-m2", "quantity": 1, "role": "driver"},
      {"part": "spur-gear-30t-m2", "quantity": 1, "role": "driven"}
    ],
    "edges": [
      {"from": "spur-gear-18t-m2", "rel": "press onto", "to": "shaft-6mm", "interface": "bore-6"},
      {"from": "spur-gear-30t-m2", "rel": "press onto", "to": "shaft-6mm", "interface": "bore-6"},
      {"from": "shaft-6mm", "rel": "rotates in", "to": "bearing-608zz", "interface": "bore-8-sleeved"},
      {"from": "bearing-608zz", "rel": "seated in", "to": "housing-plate", "interface": "seat-22H7"},
      {"from": "spur-gear-18t-m2", "rel": "meshes with", "to": "spur-gear-30t-m2", "interface": "gear-mesh-m2"}
    ],
    "install_order": ["housing-plate", "bearing-608zz", "shaft-6mm", "spur-gear-18t-m2", "spur-gear-30t-m2"],
    "disassembly_blockers": ["gear press-fit on shaft requires puller", "bearing seat may need bearing puller"]
  },
  "checks": [
    {"id": "CHK-CENTRE-DIST", "rule": "centre_distance == m*(z1+z2)/2 ±0.05", "status": "agent-verifiable"},
    {"id": "CHK-MODULE-MATCH", "rule": "all meshing gears share module", "status": "agent-verifiable"},
    {"id": "CHK-BEARING-COUNT", "rule": "each loaded shaft supported by >=2 bearings OR 1 bearing + moment-free mount", "status": "agent-verifiable"},
    {"id": "CHK-TORQUE-RATING", "rule": "tooth strength vs torque", "status": "requires-real-solver-or-datasheet"}
  ],
  "repair_scenarios": ["SC-GEAR-NOISE-01"],
  "view": {
    "layered_diagram": "layer side view: two circles tangent at centre distance; exploded view: housing z=0, bearing z=8, gears z=20",
    "animation": "rotate driver; driven spins at -z2/z1 * w1"
  },
  "provenance": {"source": "authored; components as listed", "license": "CC0-1.0 (KB metadata)", "component_licenses": ["CC0-1.0", "CC-BY-3.0 (608ZZ geometry)"]}
}

fourbar = {
  "id": "ASM-FOURBAR-01", "type": "assembly", "label": "Crank-rocker four-bar linkage",
  "category": "linkages",
  "summary": "Ground 150 - crank 60 - coupler 120 - rocker 80 (mm), four pin joints. Demonstrates DOF counting, Grashof condition and transmission angle.",
  "parameters": {
    "link_lengths_mm": {"ground": 150, "crank": 60, "coupler": 120, "rocker": 80},
    "DOF": {"value": 1, "equation": "3*(4-1) - 2*4 = 1", "verified": "exact arithmetic"},
    "grashof": {"value": "s+l = 60+150 = 210 <= p+q = 120+80 = 200 -> FALSE",
                "note": "this configuration is a NON-Grashof double-rocker: crank cannot fully rotate. Flag for demo: swap ground/shortest to get crank-rocker.",
                "verified": "exact arithmetic"}
  },
  "graph": {
    "parts": [
      {"part": "ground (150 mm, virtual)", "quantity": 1, "role": "ground"},
      {"part": "lever-arm-80", "quantity": 1, "role": "crank-standin", "note": "crank is 60 mm; use parametric lever variant"},
      {"part": "coupler-link-120", "quantity": 1, "role": "coupler"},
      {"part": "lever-arm-80", "quantity": 1, "role": "rocker"},
      {"part": "pin-6mm", "quantity": 4, "role": "pivot"}
    ],
    "edges": [
      {"from": "ground(150)", "rel": "pin at", "to": "crank(60)", "interface": "pin-6"},
      {"from": "crank(60)", "rel": "pin at", "to": "coupler-link-120", "interface": "pin-6"},
      {"from": "coupler-link-120", "rel": "pin at", "to": "lever-arm-80", "interface": "pin-6"},
      {"from": "lever-arm-80", "rel": "pin to ground", "to": "ground(150)", "interface": "pin-6"}
    ],
    "install_order": ["ground", "crank", "coupler", "rocker (pins inserted last)"],
    "disassembly_blockers": ["cotter pins on pivot pins (not modelled)"]
  },
  "checks": [
    {"id": "CHK-GRASHOF", "rule": "s + l <= p + q for full crank rotation", "status": "agent-verifiable"},
    {"id": "CHK-DOF-PLANAR", "rule": "DOF == 1 for a single-input mechanism", "status": "agent-verifiable"},
    {"id": "CHK-TRANSMISSION-ANGLE", "rule": "transmission angle >= 40 deg through working arc", "status": "requires-numeric-solve"}
  ],
  "repair_scenarios": ["SC-LINKAGE-BIND-01"],
  "view": {
    "layered_diagram": "top view, four bars with pin markers; animate crank at 1 rev/s",
    "animation": "numeric crank rotation, coupler curve trace"
  },
  "provenance": {"source": "authored", "license": "CC0-1.0"}
}

pipevalve = {
  "id": "ASM-PIPEVALVE-01", "type": "assembly", "label": "Pipe-and-valve demo (DN25 flanged)",
  "category": "piping",
  "summary": "Two DN25 pipe stubs bolted to a DN25 valve body through gaskets. Demonstrates bolted joints, gasket dependencies and flange compatibility.",
  "parameters": {
    "DN": {"value": 25},
    "gasket_thickness_mm": {"value": 2.0, "note": "consumable; drives tolerance stack"},
    "bolt_count_per_joint": {"value": 4},
    "flange_gap_worst_case_mm": {"value": 0.35, "equation": "stack of flange tolerances", "verified": "illustrative stack, not measured"}
  },
  "graph": {
    "parts": [
      {"part": "pipe-flange-dn25", "quantity": 2, "role": "pipe"},
      {"part": "valve-body-dn25", "quantity": 1, "role": "valve"},
      {"part": "gasket-dn25", "quantity": 2, "role": "seal", "note": "virtual part: no geometry, thickness 2 mm"},
      {"part": "bolt-M6x40", "quantity": 16, "role": "fastener", "note": "4 per flange joint, 2 joints"}
    ],
    "edges": [
      {"from": "pipe-flange-dn25", "rel": "bolts to", "to": "valve-body-dn25", "interface": "flange-DN25", "requires": ["gasket-dn25", "bolt-M6x40"]},
      {"from": "gasket-dn25", "rel": "sandwiched by", "to": "flange faces", "interface": "flange-DN25"}
    ],
    "install_order": ["valve-body-dn25", "gasket-dn25", "pipe-flange-dn25", "bolt-M6x40 (finger tight all, then torque sequence)"],
    "disassembly_blockers": ["gasket destroyed on removal - replace on reassembly", "bolt torque sequence required on rebuild"]
  },
  "checks": [
    {"id": "CHK-DN-MATCH", "rule": "all mated flanges share DN", "status": "agent-verifiable"},
    {"id": "CHK-GASKET-PRESENT", "rule": "every bolted flange joint lists a gasket", "status": "agent-verifiable"},
    {"id": "CHK-PRESSURE-RATING", "rule": "PN class >= line pressure with margin", "status": "requires-standard-or-datasheet"},
    {"id": "CHK-TORQUE-SEQ", "rule": "torque sequence and values", "status": "human-verified"}
  ],
  "repair_scenarios": ["SC-VALVE-LEAK-01"],
  "view": {
    "layered_diagram": "section view: pipe-flange | gasket | valve-face, bolts crossing stack",
    "animation": "exploded view steps through install_order"
  },
  "provenance": {"source": "authored", "license": "CC0-1.0", "note": "flange geometry is demo-only, NOT standard-traceable (EN 1092 / ASME B16.5)"}
}

for a in (geartrain, fourbar, pipevalve):
    with open(os.path.join(ROOT, "assemblies", a["id"] + ".json"), "w") as f:
        json.dump(a, f, indent=1)

# ------------------------------------------------------------------ scenarios
scenarios = [
 {
  "id": "SC-GEAR-NOISE-01", "assembly": "ASM-GEARTRAIN-01", "symptom": "Grinding / whining noise from gearbox after months of use; worsens under load.",
  "probable_causes": [
    {"cause": "centre distance drifted (bearing wear / housing wear)", "evidence_to_collect": "measure actual centre distance; compare 48.0 ±0.05", "kb_refs": ["PR-GTR-01"]},
    {"cause": "tooth wear or chipping from debris", "evidence_to_collect": "inspect tooth flanks; look for pitting on pitch line", "kb_refs": ["PR-GTR-01", "PR-LUB-01"]},
    {"cause": "lubrication lost", "evidence_to_collect": "check for oil film; discoloration", "kb_refs": ["PR-LUB-01"]}
  ],
  "procedures": [
    "1. power off, lock out", "2. open housing; photograph gear mesh before touching",
    "3. check bearings for roughness by hand-rotation", "4. measure centre distance with calipers",
    "5. if bearing rough -> replace bearing (608ZZ, cheap); if centre distance ok and teeth pitted -> replace gear pair"
  ],
  "verification": "after rebuild: run at no load 5 min, then load; noise should not recur",
  "safety_notes": "rotating machinery: guards back on before power",
  "kb_refs": ["PR-GTR-01", "PR-BRG-01", "PR-LUB-01", "PR-ASM-01"],
  "provenance": {"source": "authored", "license": "CC0-1.0"}
 },
 {
  "id": "SC-LINKAGE-BIND-01", "assembly": "ASM-FOURBAR-01", "symptom": "Mechanism binds mid-stroke; motor stalls at same position every cycle.",
  "probable_causes": [
    {"cause": "transmission angle too small at that crank position", "evidence_to_collect": "measure crank angle at stall; compute transmission angle", "kb_refs": ["PR-4BAR-01"]},
    {"cause": "pivot pin seized / no lubrication", "evidence_to_collect": "disconnect coupler; check each joint moves freely", "kb_refs": ["PR-FRI-01"]},
    {"cause": "bent link changed effective length", "evidence_to_collect": "compare link lengths to 60/120/80", "kb_refs": ["PR-4BAR-01", "PR-MAT-01"]}
  ],
  "procedures": [
    "1. mark stall position", "2. disconnect coupler pins one at a time to isolate the stiff joint",
    "3. clean + lubricate pivot pins", "4. if binding is positional, redesign link ratio (agent can recompute Grashof + angles)"
  ],
  "verification": "full rotation by hand without stall; motor current flat over cycle",
  "safety_notes": "store energy in mechanism may snap when freed",
  "kb_refs": ["PR-4BAR-01", "PR-FRI-01", "PR-DOF-01"],
  "provenance": {"source": "authored", "license": "CC0-1.0"}
 },
 {
  "id": "SC-VALVE-LEAK-01", "assembly": "ASM-PIPEVALVE-01", "symptom": "Weeping at flange joint after valve replacement.",
  "probable_causes": [
    {"cause": "gasket not replaced or wrong thickness", "evidence_to_collect": "check gasket; 2 mm spec", "kb_refs": ["PR-TOL-01"]},
    {"cause": "uneven bolt torque - flange cocked", "evidence_to_collect": "measure flange gap at 4 points", "kb_refs": ["PR-FST-01"]},
    {"cause": "flange face damage (scored)", "evidence_to_collect": "visual + feel", "kb_refs": ["PR-ASM-01"]}
  ],
  "procedures": [
    "1. depressurize and drain", "2. break joint; inspect faces; replace gasket ALWAYS",
    "3. clean faces; no old gasket fragments", "4. finger-tight all bolts, then torque in cross sequence in 3 steps",
    "5. torque values from a human-verified table - agent must not invent them"
  ],
  "verification": "pressure test per site procedure before returning to service",
  "safety_notes": "line contents may be hazardous; verify zero energy before breaking joint",
  "kb_refs": ["PR-FST-01", "PR-TOL-01", "PR-ASM-01"],
  "provenance": {"source": "authored", "license": "CC0-1.0"}
 }
]
for s in scenarios:
    with open(os.path.join(ROOT, "scenarios", s["id"] + ".json"), "w") as f:
        json.dump(s, f, indent=1)

# ------------------------------------------------------------------ validation rules
rules = {
  "schema": "0.1",
  "rules": [
    {"id": "R-GEAR-MODULE", "applies_to": "gear_mesh edges", "check": "module_a == module_b", "on_fail": "block + explain tooth-size mismatch", "refs": ["PR-GTR-01"]},
    {"id": "R-GEAR-CENTRE", "applies_to": "gear_mesh edges", "check": "|centre_distance - m*(za+zb)/2| <= 0.05 mm", "on_fail": "block + suggest centre distance", "refs": ["PR-GTR-01"]},
    {"id": "R-BORE-FIT", "applies_to": "bore interfaces", "check": "shaft_dia <= bore_dia + 0.1 mm", "on_fail": "block; explain interference needs press spec", "refs": ["PR-TOL-01"]},
    {"id": "R-GRASHOF", "applies_to": "four-bar parameter changes", "check": "report s+l vs p+q; warn if crank rotation required and non-Grashof", "on_fail": "warn + suggest which link to re-ground", "refs": ["PR-4BAR-01"]},
    {"id": "R-DOF", "applies_to": "assembly graph edits", "check": "DOF of mechanism unchanged unless user asked", "on_fail": "warn with DOF count before/after", "refs": ["PR-DOF-01"]},
    {"id": "R-GASKET", "applies_to": "bolted flange joints", "check": "gasket part present in requires list", "on_fail": "block + cite SC-VALVE-LEAK-01", "refs": ["PR-FST-01"]},
    {"id": "R-MATERIAL-KNOWN", "applies_to": "material fields", "check": "material in KB materials table", "on_fail": "refuse to quote strength numbers; request datasheet", "refs": ["PR-MAT-01"]},
    {"id": "R-SPRING-RATE", "applies_to": "springs", "check": "rate is null unless wire dia + coils + material given", "on_fail": "keep null; show formula", "refs": ["PR-SPR-01"]},
    {"id": "R-LOAD-CLAIMS", "applies_to": "any force/stress/life claim", "check": "must be either (a) exact arithmetic shown, or (b) labeled estimate, or (c) solver output with job files", "on_fail": "strip claim; emit unverified label", "refs": ["PR-FBD-01", "PR-FAT-01"]},
    {"id": "R-ASSEMBLY-ORDER", "applies_to": "graph edits", "check": "install_order remains a valid topological order", "on_fail": "block + show conflicting edge", "refs": ["PR-ASM-01"]}
  ],
  "labeling_policy": {
    "verified-arithmetic": "exact algebra/geometry derived from parameters - shown with the formula",
    "estimate": "closed-form approximations with stated assumptions (belt length, bolt torque via K=0.2)",
    "solver-verified": "produced by CalculiX/PyNite run; job files retained",
    "unverified-proposal": "everything else; MUST be labeled in UI and responses",
    "never-do": "invent load ratings, material strengths, torque values, or simulation results"
  },
  "provenance": {"source": "authored", "license": "CC0-1.0"}
}
with open(os.path.join(ROOT, "validation_rules.json"), "w") as f:
    json.dump(rules, f, indent=1)

print("wrote 3 assemblies, 3 scenarios, validation_rules.json")
