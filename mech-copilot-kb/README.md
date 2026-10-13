# Mech Copilot Knowledgebase - MVP (verified vertical slice)

A self-contained, offline engineering knowledgebase + 2.5D workspace for an AI
mechanical-design copilot, built for a five-day hackathon on AMD infrastructure.

Status: **working vertical slice, all pieces executed and verified** (see
"Verified evidence" below). Not a production engineering tool.

## One-paragraph answer

Reuse existing geometry, do not generate it: build123d (Apache-2.0, Python,
OCCT-backed) is the CAD foundation; a small hand-curated JSON knowledgebase
(12 components, 16 principles, 3 assemblies, 3 repair scenarios, 10 validation
rules - all CC0 except 2 reused CC-BY parts) is what the agent actually reads;
three.js renders the GLB previews in a 2.5D web workspace; a stdlib HTTP
backend glues them; an LLM is optional and only ever picks a tool call - every
number comes from labeled calculators. A 7B-class model runs locally on AMD
via Ollama (ROCm) or llama.cpp (HIP/Vulkan). Geometry kernels and FEM stay on
CPU; the GPU accelerates inference (and later sparse solvers via rocALUTION).

## Verified evidence (what was actually run)

| Claim | Evidence |
|---|---|
| build123d 0.13.0 installs and runs headless | `pip install build123d` in clean venv; import + builds OK |
| Parametric parts generate fast | 2 gears + shaft, STEP+STL+GLB export in 2.4 s total |
| STEP round-trip of reused assets | 608ZZ bearing imports at exactly 22.0 x 22.0 x 7.0 mm |
| GLB previews load in three.js r160 | screenshot: gear rendered in canvas |
| SVG principle diagrams render | screenshot: gear-mesh diagram in canvas + inspector |
| Agent retrieval + validation + labeling | `tools/kb_agent.py demo` full flow; blocked proposal A, corrected proposal B passes with open items |
| HTTP backend + traversal guard | `/api/kb`, `/api/entry`, `/api/agent`, `/kb-assets/*` all 200; `../` -> 403 |
| End-to-end prompt -> reply in browser | "Run demo flow" button; reply shows `[verified-with-open-items]` label + PASS/OPEN lines |

## Run it

```bash
# backend + 2.5D workspace (stdlib only)
cd mech-copilot-kb
python3 tools/serve.py 8765
# open http://127.0.0.1:8765  - click entries, hit "Run demo flow"

# agent CLI
python3 tools/kb_agent.py search "gear noise"
python3 tools/kb_agent.py validate ASM-GEARTRAIN-01
python3 tools/kb_agent.py calc centre_distance '{"z1":18,"z2":45,"module":2}'
python3 tools/kb_agent.py demo

# optional: local LLM on AMD (only chooses intents; never computes numbers)
# Ollama:   ollama serve   (ROCm build; see https://docs.ollama.com/gpu)
# llama.cpp server (HIP or Vulkan build), then:
LLM_URL=http://127.0.0.1:8080/v1/chat/completions LLM_MODEL=qwen2.5:7b python3 tools/serve.py 8765

# regenerate geometry/KB (needs: pip install build123d)
/tmp/mkb_venv/bin/python tools/gen_kb.py          # components + STEP/STL/GLB
python3 tools/gen_principles.py                   # principles + SVG diagrams
python3 tools/gen_assemblies.py                   # assemblies, scenarios, rules
```

## Decision table (primary stack)

| Layer | Choice | License | Why (verified) | AMD relevance |
|---|---|---|---|---|
| CAD kernel / parametric | **build123d 0.13** (+ OCCT via OCP wheels) | Apache-2.0 | Python-native, joints (Rigid/Revolute/Linear/Cylindrical/Ball with ranges), STEP/STL/GLF export proven in 2.4 s | CPU (geometry kernels are single-thread CPU work) |
| Alternate / legacy import | FreeCAD 1.x headless (Assembly WB built on Ondsel solver since 1.0) | LGPL-2.1+ | Use for FCStd and for its Assembly solver if assembly motion is demoed | CPU |
| Reusable parts | FreeCAD-library (bearings, pulleys, fasteners; STEP/STL/FCStd) + QCAD `libraries/` (DXF, per-file CC0/PD) | CC-BY-3.0 / CC0 | 608ZZ bearing imported at exact 22x22x7 mm | n/a |
| Knowledgebase | hand-curated JSON in `kb/` (this repo) | CC0 (ours) | <100 entries; token-overlap retrieval beats a vector DB at this size; zero deps | CPU |
| Retrieval | BM25-lite in `tools/kb_agent.py` | MIT-style (ours) | top-hit correct in demo; no embeddings needed | CPU |
| 2.5D frontend | three.js r160 + GLTFLoader + OrbitControls | MIT | GLB + SVG both render; ~250 lines total | WebGL on any GPU incl. AMD |
| Backend | Python stdlib `http.server` | - | serves UI + KB assets + agent API; swap for FastAPI later | CPU |
| LLM inference | Ollama (ROCm) or llama.cpp (HIP or Vulkan backend) | MIT | Ollama lists RX 6800+/7900/MI300 and more; llama.cpp documents HIP + Vulkan builds | **this is where AMD GPUs pay off** |
| FEM (phase 2, not MVP) | CalculiX (GPL-2.0) via FreeCAD FEM; PyNiteFEA (MIT) for beams/frames | GPL-2.0 / MIT | CalculiX GPU path exists but is CUDA-only (PaStiX+CUDA); keep solvers on CPU | CPU; rocALUTION is the future HIP path for sparse solves |

## Folder structure

```
mech-copilot-kb/
  README.md                 <- this file
  kb/                       <- THE knowledgebase (offline, self-contained)
    components/*.json       <- 12 component entries (schema 0.1)
    principles/*.json       <- 16 principles (13 foundation, 3 advanced)
    assemblies/*.json       <- 3 assemblies w/ graphs, checks, install order
    scenarios/*.json        <- 3 repair scenarios
    validation_rules.json   <- 10 rules + labeling policy
    assets/
      cad/*.step|stl        <- editable BREP + mesh (reused CC-BY + authored CC0)
      previews/*.glb|.bin   <- three.js-loadable previews
      diagrams/*.svg        <- 2.5D-style principle diagrams
  tools/
    gen_kb.py               <- regenerates components + geometry (build123d)
    gen_principles.py       <- regenerates principles + diagrams
    gen_assemblies.py       <- regenerates assemblies/scenarios/rules
    kb_agent.py             <- agent tool interface (search/get/validate/calc/demo)
    serve.py                <- stdlib backend (UI + API + assets)
  web/
    index.html              <- 2.5D workspace (three.js, no build step)
```

## Component schema (v0.1) - fields in every entry

```
id, type, category, label, summary
parameters      {name: {value, unit, range|note, verified}}
geometry        {bbox_mm, volume_mm3}
asset           {step, stl, preview_glb}
interfaces      [{kind: bore|flange_face|gear_mesh|belt_track|cylindrical|housing_seat, spec}]
connections     {accepts:[ids], mates_with:[ids], joint}
governing       {principles:[PR-...], equations:[...]}
checks          [agent-verifiable / requires-solver notes]
provenance      {source, license, url, note}
```

Assembly entries add: `graph{parts, edges(rel/interface/requires), install_order,
disassembly_blockers}`, `checks[{id, rule, status}]`, `view{layered_diagram,
animation}`, `repair_scenarios`.

Principle entries: `level, simple, equations, variables, visual, failure_modes,
example, agent_use, limits, verify_with`.

## Example entries (5 of 12+16+3+3)

1. `kb/components/spur-gear-18t-m2.json` - 18T module-2 gear; authored CC0;
   simplified (non-involute) teeth; carries centre-distance + ratio equations.
2. `kb/components/bearing-608zz.json` - REUSED geometry (FreeCAD-library,
   CC-BY-3.0), exact 8x22x7 mm; L10 formula present, C-rating deliberately
   absent ("do not quote without datasheet").
3. `kb/principles/PR-GTR-01.json` - gears/ratios/centre distance: explanation,
   3 equations, failure modes, agent-use rule, explicit limits (no tooth
   strength claims without a solver/datasheet).
4. `kb/assemblies/ASM-GEARTRAIN-01.json` - 18T->30T train, install order
   housing->bearing->shaft->gears, check CHK-CENTRE-DIST as agent-verifiable
   arithmetic, CHK-TORQUE-RATING marked requires-solver.
5. `kb/scenarios/SC-VALVE-LEAK-01.json` - flange weep: probable causes w/
   evidence-to-collect, 5-step procedure, explicit "agent must not invent
   torque values".

## AI workflow (retrieval -> modification -> validation)

```
prompt -> [optional LLM picks ONE intent (JSON, no numbers)]
       -> kb_search (BM25-lite) grounds the answer in entries
       -> propose_change(assembly, overrides) runs validation rules:
            R-GEAR-MODULE, R-GEAR-CENTRE, R-DOF, R-GRASHOF, R-GASKET, ...
       -> every emitted number is labeled:
            verified-arithmetic | estimate | solver-verified | unverified-proposal
       -> reply cites PR-*/SC-* entries and lists human-owned open items
```

Labeling policy lives in `kb/validation_rules.json`: the agent never invents
load ratings, material strengths, torque values, or simulation results.
Calculators available today: centre distance, gear ratio, belt length,
shaft torsion, tolerance stack (WC+RSS), planar DOF, Grashof.

## 2.5D interface coverage

| Requirement | How it is met |
|---|---|
| Layered diagrams / cross-sections | principle SVGs render as textured planes in the 3D scene + inline in inspector |
| Exploded assemblies | assembly `graph.install_order` drives the explode order (demo shows list; per-part offsets are day-4 work) |
| Component highlight/selection | entry chips + KB list selection; per-part hover highlight is day-4 |
| Animated motion, force arrows | assembly `view.animation` spec present; crank animation day-4-5 |
| Parameter sliders | live for every numeric component parameter in the inspector |
| Before/after comparison | proposal + validation side-by-side in the reply block (extend to dual renders day 5) |
| Explanations linked to parts | every check/citation carries `refs` back to PR-*/SC-* entries |

## Five-day plan (with explicit scope cuts)

| Day | Deliver | Cut on this day |
|---|---|---|
| 1 | Env: venv + build123d + three.js page; KB schema; 12 components w/ GLB previews | no FreeCAD integration, no FCGear |
| 2 | Principles (16) + diagrams; retrieval (BM25-lite) + `kb_agent.py` CLI | no embeddings, no vector DB |
| 3 | 3 assemblies + validation rules + calculators; demo flow end-to-end in CLI | no DOF solving, no path tracing |
| 4 | Web UI: browser, inspector, sliders, prompt panel wired to `/api/agent`; per-part highlight + explode view | no animation timeline editor |
| 5 | LLM intent-planner on AMD (Ollama ROCm or llama.cpp HIP/Vulkan); one mechanically-meaningful validation (centre-distance + Grashof + stack) polished; demo script + fallback if GPU misbehaves | no FEM in the demo path; CalculiX shown as screenshot/CLI only |
| Always | verified/estimate/unverified labeling in every reply | no invented numbers, ever |

Fallback: if the AMD GPU inference path stalls, the regex intent-matcher in
`serve.py` runs the identical demo offline (this is the default and it is what
was verified).

## Licensing summary

- KB metadata, diagrams, authored geometry: **CC0-1.0** (this repo).
- Reused geometry: 608ZZ bearing + GT2 pulley STEP from FreeCAD/FreeCAD-library
  **CC-BY-3.0** (attribution per-file required; author in provenance fields).
- Code: build123d **Apache-2.0**, three.js **MIT**, QCAD libraries **CC0/PD per
  item**, Ollama/llama.cpp **MIT**. GPL-2.0 tools (CalculiX, OpenSCAD, FCGear)
  are invoked as separate processes only - never linked - so copyleft does not
  reach this repo's code.
- FreeCAD itself is LGPL-2.1+; safe to call headless as a subprocess.
- Avoid: Khan Academy (CC-BY-NC-SA: non-commercial), PhET (GPL-3.0 app code),
  507movements.com site images (requests no mirroring; the 1868 book itself is
  public domain - rescan from Internet Archive/Wikimedia instead).

## Risks / limits (labelled honestly)

1. **Tooth geometry is simplified** (cylindrical bumps, not involutes) - fine
   for ratio/centre-distance teaching; swap in FCGear before printing gears.
2. **Valve/flange geometry is demo-only**, not EN 1092/ASME-traceable.
3. **No simulation in the demo path** - CHK-TORQUE-RATING and
   CHK-TRANSMISSION-ANGLE stay OPEN; that is the point of the labeling policy.
4. **Datasheet numbers deliberately absent** (bearing C, torque tables, spring
   rates) - entries say where they must come from.
5. **three.js loads addons from unpkg CDN** in the current HTML; vendor the
   three.module.js + addons into `web/vendor/` for true offline demo (15 min).
6. **`.glb` files are glTF-JSON + external `.bin`** (build123d exporter) - the
   backend serves both; any fix must keep the pair together.
7. AMD GPU is **inference-only in this MVP**: geometry kernels (OCCT), BM25
   retrieval, and the stdlib backend are CPU work; FEM on GPU is future work
   (rocALUTION/hipSPARSE exist for sparse solves; CalculiX's only GPU path is
   CUDA via PaStiX).
