# P1 Deep Research — FINAL: recommended approach for AMD Act 3 Track 1

Date: 2026-10-10. Full pipeline: environment → constraints (EVENT-CONSTRAINTS.md) → research
campaign (research/p1-deep/) → 3 candidate directions → 3 independent red teams
(RED-TEAM-d1.md, ../validation/P1-D2-RED-TEAM.md, REDTEAM-CLAIM3.md) → this recommendation.
All 54 sources in the citation ledger; every competitive claim verified by direct page/repo read.

---

## Part 1 — What is ALREADY SOLVED in industrial RAG (never pitch these as innovation)

| Capability | Status | Key evidence [ledger id] |
|---|---|---|
| Manual-page RAG + citations | SHIPPED (Siemens Industrial Copilot combs "documents, manuals, spare part lists") | [21] |
| Multimodal page retrieval | SOLVED in research (Cessna 172 MMR: 93.37% recall@5, $0.0091/query) | [14] |
| Hybrid retrieval (vector+BM25+RRF) | COMMODITIZED (RAFT default; published recipes) | [2] |
| Industrial QA benchmark from real manuals | SOLVED (Industrial-Instruction: 906 Panasonic manuals, 13.6k–26k QA pairs, 5 relationship classes, open data+FAISS index+code) | [3][4][5] |
| Layout-aware ingestion | COMMODITIZED (Docling MIT, MinerU, MultiDocFusion EMNLP 2025: +8–15% retrieval precision) | [33][34] |
| Parts-table extraction from diagrams | SOLVED (Enginuity: 98.7% item accuracy; first open benchmark) | [6][7] |
| Troubleshooting-guide GENERATION | SOLVED (Hitachi 2024 36–64% coverage/88–100% precision; TSGen FSE 2026; Gixo product) | [10][exa] |
| Troubleshooting-guide EXECUTION (generic) | SOLVED (StepFly Microsoft FSE 2026 MIT: DAG execution, ~94% success; Amazon production SOP-tree agent with true/false/"no data" verdicts; IETM fault-tree execution Sensors 2025) | [35][36][38] |
| Conflict detection in RAG (generic) | SOLVED (ConflictRAG 88.7% F1; ClawMem 212★ MIT ships supersede-aware retrieval filtering; Alhena ships same-question-different-answer detection) | [15][44] |
| Revision-aware retrieval on equipment manuals | STRONG PRIOR ART (EACL 2026 industry: aircraft AMM, certified-source traceability, 49k queries; MakinaRocks nuclear revision comparison; Author-it AION makes conflicting-torque-from-superseded-revision its marketing proof) | [45][43][42] |
| Revision control as practice | ESTABLISHED (document-management products: effective dates, isolation, approval chains; OxMaint aviation CMMS) | [20] |
| Superseded-revision hiding in RAG path ON AMD+lablab | EXISTS (Saudi Sign Intelligence, AMD AI League Match 3, same platform as ACT III: "superseded revisions are detected... then hidden, so the model never sees the decoy number") | [41] |
| Abstention/refusal as a pattern | PUBLISHED PRIOR ART (AbstentionBench NeurIPS 2025; typed-abstention routing; refusal-as-product in adjacent domains: Continuity board repair; measured refusal in generic QA: Failure-Aware ERNIE) | [47][48][49] |
| Bayesian self-escalation | SOLVED in research | [18] |
| Structure-aware chunking / graph RAG | COMMODITIZED (LightRAG 40k★, microsoft/graphrag 36k★, both MIT) | |

## Part 2 — The three candidate directions, post-red-team

All three verdicts: PARTIALLY_DIFFERENTIATED. Each survives ONLY in its narrowed form.

### Direction 1 — Manual-grounded decision-tree execution with evidence accountability
- NARROWED CLAIM (survives): no artifact binds execution to REAL equipment manuals with
  per-node source citations, refusal where the manual has no answer, and a public-benchmark
  evaluation. Execution alone is broken (StepFly, Amazon, IETM 2025); "StepFly for equipment
  manuals" is what it sounds like.
- Red-team essentials: cite StepFly/Amazon/IETM/FieldMate in the deck; benchmark eval is the
  most defensible element; never lead with "execution".
- Difficulty: MEDIUM-HIGH (eval-scenario authoring is the long pole). Closest: StepFly [35].

### Direction 2 — Revision-conflict-aware evidence with precedence verdicts
- NARROWED CLAIM (survives): query-time same-question-different-answer detection BETWEEN
  RETRIEVED REVISIONS + precedence verdict citing both sources + refusal on unknown authority,
  on UNCONTROLLED legacy PDF corpora of equipment manuals. Kills: "conflict detection in a RAG
  path" (ClawMem, Alhena, Saudi Sign Intelligence), "torque conflict story" (Author-it),
  "revision comparison on equipment docs" (MakinaRocks).
- Red-team essentials: MUST cite-and-distinguish Saudi Sign Intelligence (same platform),
  Author-it, MakinaRocks, EACL 2026 MRO, ClawMem; multi-source precedence (OEM vs plant-local)
  is the strongest unclaimed semantic; refusal as enforced state + auditable conflict ledger.
- Difficulty: MEDIUM. Corpus risk: Graco public manuals only confirmed real multi-revision source.

### Direction 3 — Measured safe-diagnosis on false-premise + underspecified fault tickets
- NARROWED CLAIM (survives): first MEASURED refusal/escalation accuracy on false-premise AND
  underspecified fault reports, on a public benchmark, as an operator-facing product. Kills:
  "refusal is new" (AbstentionBench, Continuity, Failure-Aware ERNIE), "false-premise only" (the
  wording finding: vague tickets collapse 0.820→0.497, over-diagnosis to 47% — the bigger slice).
- Red-team essentials: FaulT-Bench data is PUBLIC (no moat, but build is de-risked); the fix is
  an EXTERNAL premise-verification layer, not model self-confidence; refusal must BE the operator
  artifact (triage verdict card), not a metrics table.
- Difficulty: STRONG feasibility (dataset+harness+3,960 frozen runs released, MIT/CC BY 4.0).

## Part 3 — RECOMMENDATION: Direction 3 fused with Direction 2's verdict semantics
### "FAULTGATE — evidence-gated triage for equipment fault reports"

**The smallest technically meaningful innovation that is provable:** an external,
deterministic premise-verification + evidence-gating layer in front of a troubleshooting LLM,
measured on FaulT-Bench's public benchmark. SOTA agents over-diagnose healthy systems (11–24%
of answered runs) and collapse on vague tickets (outcome 0.820→0.497; over-diagnosis to 47%).
No existing system measures or fixes this. The fix pattern (external verifier, not
self-confidence) is published but UNBUILT as a product with measured numbers — and the
benchmark, harness, and 3,960 frozen baseline runs are public, so the improvement is
demonstrable with zero API keys and a reproducible delta.

**Why this wins over D1/D2 for a 5-day hackathon:**
1. Benchmark + baselines exist (no dataset authoring risk — the D1/D2 long pole).
2. Numbers are reproducible without API keys (verification tools ship with FaulT-Bench).
3. The demo is an operator artifact (triage verdict card), not a chatbot and not a lint pass.
4. AMD requirement is clean: base agent on vLLM/MI300X; the gate is deterministic code.
5. Domain honesty: network equipment IS plant-adjacent infrastructure (Track 1 "Intelligent
   Industry" covers technical infrastructure operations); say so explicitly.

**Architecture:**
```
Fault ticket (arbitrary wording, possibly false/vague)
        ↓
[P1] PREMISE GATE (deterministic + cheap LLM checks, NOT self-confidence):
     - ticket claims a fault X on device D with evidence E?
     - does the ticket name identifiers/symptoms at all (specificity score)?
     - prior-tool outputs (ping/log checks) consistent with a fault existing?
        ↓
   ├─ premise VERIFIED → run troubleshooting agent (vLLM on AMD MI300X)
   │        ↓
   │    [P2] EVIDENCE GATE: every root-cause claim must cite an observed
   │    system state (tool output), not model memory — else REFUSE/escalate
   │        ↓
   │    VERDICT CARD: fault confirmed + evidence / rule-outs / fix
   ├─ premise UNVERIFIABLE (vague) → ASK-THE-OPERATOR card: the 2 checks
   │   to run before dispatch (measured: kills the 0.820→0.497 collapse)
   └─ premise FALSE (system healthy) → "NOTHING WRONG + what was ruled out"
        (measured: kills the 11–24% over-diagnosis / benign-as-root-cause failure)
```

**Tech stack (all free/open):**
- Benchmark + data: FaulT-Bench (MIT code, CC BY 4.0 dataset, 560 scenarios, 8 Kathará
  topologies, 3,960 frozen runs) — github.com/Overlxrd-uwu/FaulT-Bench [46]
- Agents to gate: SADE/ReAct from SADE-NetworkAgent (per FaulT-Bench acknowledgements) [46]
- AMD: vLLM (Apache-2.0) on AMD Developer Cloud MI300X (192 GB) serving the open model
  (e.g., Qwen3-32B or Llama-3.3-70B-AWQ); ROCm vLLM V1 documented [25][26]
- Gate: Python stdlib + small judge calls via the same vLLM endpoint; deterministic checks in
  code (identifier extraction, tool-output consistency, specificity scoring)
- Eval: FaulT-Bench verification tools (no Docker/GPU needed) + own harness for the gated runs
- UI: single-page verdict card (any stack)

**Repository structure:**
```
faultgate/
├── README.md               # runs from clone; no committed keys
├── LICENSE                 # MIT
├── docker-compose.yml      # vLLM-ROCm + app
├── faultgate/
│   ├── premise_gate.py     # deterministic specificity + consistency checks
│   ├── evidence_gate.py    # root-cause claims must cite observed state
│   ├── verdict_card.py     # operator artifact rendering
│   └── agent_client.py     # thin client over vLLM endpoint
├── baselines/              # frozen FaulT-Bench run ingestion (ungated)
├── eval/
│   ├── run_gated_benchmark.py
│   └── results/            # gated vs ungated deltas
├── ui/
└── docs/
    ├── related-work.md     # StepFly/Continuity/ERNIE/AbstentionBench/HoldPoint + distinctions
    └── demo-script.md
```

**Implementation steps (5 days):**
1. Day 0/1: AMD Developer Cloud access + vLLM endpoint serving an open model; clone
   FaulT-Bench; run the no-Docker verification tools to reproduce baseline tables (0.932/0.820/
   over-diagnosis 11–24%). Confirm Docker on the cloud box; if unavailable, gate frozen runs.
2. Day 1–2: premise gate (deterministic specificity scoring + tool-output consistency);
   integrate as a wrapper in front of the SADE/ReAct agent.
3. Day 2–3: evidence gate + verdict-card rendering; run gated benchmark on the 72
   false-premise + 360 persona scenarios (the headline slices).
4. Day 3–4: measure the 2×2 — false-alarm rate on healthy networks, correct-"nothing wrong"
   rate, over-refusal rate on genuine faults (80 correct-fault scenarios guard this), plus
   outcome-score delta vs the 0.820/0.497 baselines.
5. Day 4–5: UI polish, demo video, related-work slide, honest limitations (network domain,
   Kathará emulation, hackathon-scale).

**Benchmark dataset:** FaulT-Bench 560 scenarios (80 correct-fault / 72 false-premise /
24 wrong-device / 24 wrong-cause / 360 persona rewrites), 8 topologies, 3,960 frozen baseline
runs. CC BY 4.0. All paper numbers recomputable with zero API keys [46].

**Evaluation metrics (pre-registered):**
- Over-diagnosis rate on healthy networks (baseline: SADE 24%, ReAct 16%, CC 11%) → target <5%
- Correct "nothing wrong" verdicts on false-premise tickets (baseline: outcome 0.820)
- Outcome score on vague persona tickets (baseline chain: 0.820→0.638→0.497) → target ≥0.80
- Over-refusal rate on genuine-fault tickets (the safety trade-off, target <10%)
- Wrong-device misdirection robustness (baseline 0.957 — must not regress)

**Demo scenario (6 min):**
1. Show a false-premise ticket hitting the UNGATED agent (frozen run replay): it probes,
   disproves the symptom, then promotes a benign condition to root cause — on screen.
2. Same ticket through FAULTGATE: NOTHING WRONG + what was ruled out, with evidence.
3. A vague ticket: UNGATED collapses (replay); FAULTGATE returns an ASK-THE-OPERATOR card
   with the 2 checks to run.
4. A genuine fault through FAULTGATE: confirmed with evidence, correct fix (no over-refusal).
5. Live numbers: the 2×2 table, gated vs ungated, computed by the no-API-key verification
   tools, AMD endpoint status visible.

**Honest limitations (state in the deck):** network equipment, not factory machinery (Track 1
covers infrastructure operations; say so); Kathará emulation, not physical plants; the
premise-gate fix is the paper's own suggested next move — our contribution is building it,
measuring it, and shipping it as an operator artifact before anyone else does; refusal
mechanisms are established prior art — our contribution is the MEASURED product capability.

**Why the competitive risk is manageable:** Continuity (refusal-by-construction, no
measurement), Failure-Aware ERNIE (measured refusal, generic QA, not agentic), AbstentionBench
(benchmark, no product), MindRAG (industrial false alarms, no refusal metric) — none combines
measured false-premise + specificity-gated refusal + public benchmark + operator artifact. The
lablab precedent (TokenRouter "prove or escalate", ACT II T1 #3) shows judges reward this
pattern; Saudi Sign Intelligence (Match 3) hides superseded revisions but does not gate fault
premises. Cite all five in the deck.

**Fallback if D3 feels too research-shaped for the team:** Direction 2 narrowed (D2's full
combination) is the second choice — feasible, real corpus risk manageable with declared
synthesis, and the enforced-state + multi-source-precedence semantics are unclaimed. Direction 1
is third: the eval-scenario authoring risk and "StepFly for equipment manuals" pitch-sound risk
are real, and FieldMate (same-event-risk) crowds it.

## Sources

[2] https://github.com/microsoft/RAFT
[3] https://arxiv.org/abs/2608.22817
[4] https://github.com/parssky/industrial-instruction
[5] https://huggingface.co/datasets/Parssky/industrial-instruction-dataset
[6] https://arxiv.org/abs/2606.03410
[7] https://huggingface.co/datasets/enginuity2025/enginuity-bench
[10] https://arxiv.org/abs/2604.06770
[14] https://arxiv.org/abs/2608.18465
[15] https://arxiv.org/html/2605.17301v2
[18] https://arxiv.org/abs/2608.24087
[20] https://tomastc.com/en/blog/equipment-manual-search-ai-2026-en
[21] https://press.siemens.com/global/en/pressrelease/siemens-industrial-copilot-expanded-adopted-thyssenkrupp
[25] https://www.amd.com/en/developer/resources/cloud-access/amd-developer-cloud.html
[26] https://rocm.docs.amd.com/en/docs-7.1.0/how-to/rocm-for-ai/inference-optimization/vllm-optimization.html
[33] https://github.com/docling-project/docling
[34] https://github.com/opendatalab/MinerU
[35] https://github.com/microsoft/StepFly
[36] https://arxiv.org/abs/2510.10074
[38] https://pmc.ncbi.nlm.nih.gov/articles/PMC12431284
[41] https://lablab.ai/ai-hackathons/amd-lablab-ai-academy-challenge/saudi-sign-intelligence/saudi-sign-intelligence-grounded-rag-on-amd
[42] https://www.author-it.com/ai/proof
[43] https://www.makinarocks.ai/en/use-case/ai-powered-document-comparison-automating-revision-reviews-for-nuclear-equipment
[44] https://github.com/yoloshii/ClawMem
[45] https://aclanthology.org/2026.eacl-industry.23.pdf
[46] https://github.com/Overlxrd-uwu/FaulT-Bench
[47] https://co-r-e.com/method/false-premise-tickets
[48] https://devpost.com/software/continuity-y47f6o
[49] https://baiduernieai.devpost.com/submissions/885496-failure-aware-ernie
