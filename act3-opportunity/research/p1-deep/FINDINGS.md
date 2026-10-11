# P1 Deep Research — Structured Findings (pre-red-team synthesis)

Date: 2026-10-10. Sources registered in citation ledger (34 URLs). Raw retrieval JSON:
research/p1-deep/wave-scholarly.json, wave-github*.json, wave-repos.json, papers-metadata.json.
Record types: FACT (verified by direct page/repo read) / INTERPRETATION / HYPOTHESIS (untested).
Separation maintained per opportunity-discovery skill rule 5.

## 1. State of the art in industrial RAG — what is ALREADY SOLVED (do not pitch these as innovation)

| Capability | Status | Evidence |
|---|---|---|
| Manual-page RAG with citations | SHIPPED (Siemens Industrial Copilot for Operations combs "documents, manuals, and spare part lists"; vendor lab recipe published) | [21] COMPETITIVE-INTELLIGENCE.md C2 |
| Multimodal retrieval (text+image pages) | SOLVED in research — Cessna 172 MM MMR, 93.37% recall@5, $0.0091/query | [14] |
| Hybrid retrieval (vector+BM25+RRF) | COMMODITIZED (RAFT default; every tutorial) | [2] |
| Structured QA benchmarks on industrial manuals | SOLVED — Industrial-Instruction: 13.6k–26k QA pairs from 906 Panasonic manuals, 5 query–document relationship classes, open data+code | [3][4][5] |
| Layout-aware PDF→markdown ingestion | COMMODITIZED — Docling (MIT), MinerU (Apache-2.0+terms), Unstructured hi_res | [33][34] |
| Parts-table extraction from engineering diagrams | SOLVED in research — Enginuity benchmark; Claude Sonnet 4.5 extraction at 98.7% item accuracy | [6][7] |
| Troubleshooting guide GENERATION from manuals | SOLVED in research — Hitachi (36–64% extraction coverage, 88–100% precision, 2024, 17 citations); TSGen (Microsoft, FSE 2026, from incident data); Gixo/kenexai products | [10][exa 87lnhd1rxld] |
| Troubleshooting guide EXTRACTION from flowchart images | SOLVED — FlowExtract (APMS 2026, YOLOv8+EasyOCR+arrow tracing, MIT); VLM relation extraction shown BROKEN (rel F1 < 0.11) | [8][9] |
| Fault-tree INTERACTION benchmark | SOLVED — JFTA-Bench (3,130 entries, fault trees as images, multi-turn, vague-info simulation); FaulT-Bench (200 scenarios, false-premise tickets) | [11][13] |
| Conflict detection in RAG (generic) | SOLVED in research — ConflictRAG (88.7% F1, embedding-MLP+selective LLM); contrachecker (PyPI, direct/transitive/bridge) | [15] |
| Cross-document version linking + rule-level conflict resolution | SOLVED in research — GVD (Governed Versioning and Deduplication, Centific, 2026-09) | [16] |
| Revision-control practice for manuals | ESTABLISHED PRACTICE — document-management products implement effective dates, isolation of superseded revisions, approval chains | [20] |
| Deterministic-layer-decides architecture pattern | COMMON in hackathon space — AgeBand, HoldPoint, TrueCopy, SafeO (lablab + Impact Forge 2026) | [22] |
| Bayesian self-escalation / when-to-ask-for-help | SOLVED in research (decision-theoretic formulation) | [18] |
| Vendor copilot MTTR gains | CONCENTRATED on routine failures (15–30% vendor-claimed; novel faults human-dominated) | COMPETITIVE-INTELLIGENCE.md C2 |

## 2. What remains UNSOLVED for P1 (verified gaps — labeled as absence of evidence)

1. RED-TEAM CORRECTED (was overstated): execution per se is SOLVED — StepFly (Microsoft,
   FSE 2026, MIT) executes LLM-extracted TSG DAGs; Amazon runs a production SOP-tree executor
   with true/false/"no data" verdicts; IETM 2025 publishes interactive equipment fault-tree
   execution. The defensible gap: no artifact binds EXECUTION to REAL equipment manuals with
   per-node source citations, refusal on missing evidence, and a public-benchmark evaluation.
   StepFly/Amazon operate in cloud-ops/SOP domains, not equipment documentation. FieldMate AI
   (lablab, Sep 2026) is a same-domain stepwise-guidance hackathon project to out-differentiate.
   [RED-TEAM-d1.md: 15 counterexamples verified]
2. RED-TEAM NARROWED: the claim "no product applies conflict/reversion detection to equipment
   manuals in a RAG path" does NOT survive as phrased — Saudi Sign Intelligence (lablab AMD AI
   League Match 3, same platform as ACT III) hides superseded revisions in the RAG path ON AMD;
   ClawMem (212★ MIT) ships supersede-aware retrieval filtering; Alhena ships
   same-question-different-answer detection; Author-it AION makes conflicting-torque-from-
   superseded-revision its marketing proof; MakinaRocks does revision comparison on nuclear
   equipment documents; EACL 2026 industry paper does revision-cycle-aware retrieval on real
   aircraft AMMs. The surviving gap: query-time same-question-different-answer detection
   BETWEEN RETRIEVED REVISIONS + precedence verdict citing both sources + refusal on unknown
   authority, over UNCONTROLLED legacy PDF corpora. Multi-source precedence (OEM vs plant-local)
   is the strongest unclaimed semantic. [../validation/P1-D2-RED-TEAM.md: 9 counterexamples +
   9 advice sources verified]
3. Nobody demonstrates a measured advantage of structured/functional retrieval units over
   chunk RAG on a PUBLIC industrial manual benchmark where the baseline is reproducible.
   Industrial-Instruction ships exactly the benchmark (five relationship classes, held-out
   1,000-item split) but no published baseline-vs-structured-retrieval comparison on it.
   (The financial text-and-table equivalent exists: arXiv 2604.01733, ten strategies.)
4. RED-TEAM CORRECTED (Direction 3): FaulT-Bench released its full code+data
   (github.com/Overlxrd-uwu/FaulT-Bench, MIT + CC BY 4.0: 560 scenarios, 8 topologies, 3,960
   frozen runs, no-Docker verification tools). The failure mode is public knowledge with public
   baselines; the UNBUILT gap is the FIX as a measured product capability — an external
   premise-verification + evidence-gating layer (prior art says external verifier, not
   self-confidence) with measured false-premise/underspecificity/over-refusal numbers and an
   operator-facing verdict artifact. Also: vague/underspecified tickets are the BIGGER failure
   slice (outcome 0.820→0.497, over-diagnosis to 47%), not false premises. [REDTEAM-CLAIM3.md]
4. EngIntervene (ICLR 2027) shows constraint-aware diagnosis (T3) is where multimodal models
   FAIL — no system demonstrates safe diagnostic decision-making on engineering content.
5. NO systematic retrieval-strategy ablation exists on a public INDUSTRIAL manual benchmark.
   The equivalent exists for financial text-and-table QA (arXiv 2604.01733: ten strategies,
   hybrid+rerank Recall@5 0.816, BM25 beats dense on financial docs) — the industrial
   equivalent is open. Industrial-Instruction ships the benchmark (five relationship classes,
   held-out 1,000-item split) but publishes only fine-tuning results (Set-Match 28.5%→42.0%),
   no retrieval ablation.
6. Structure-aware chunking for industrial documents is SOLVED in research: MultiDocFusion
   (EMNLP 2025 main: hierarchical multimodal chunking, +8–15% retrieval precision), SCAN,
   D-RAC, EnSI-RAG — ingestion innovation is NOT a differentiator.

## 3. The three candidate directions (pre-red-team)

### Direction 1 — Guided troubleshooting: manual-grounded interactive decision-tree execution
Fault code/symptom in → system executes (not just retrieves) a decision tree extracted from the
manual, each node citing manual page + revision, with refusal when evidence is missing.
- Resources: Industrial-Instruction corpus (CC-BY-NC), Enginuity, FlowExtract (MIT) for
  flowchart→graph, JFTA-Bench protocol for multi-turn eval, RAFT for stateful retrieval.
- Closest competitors: TSG Suggester (recommends guides, doesn't execute), TSGen (generates
  from incidents), Gixo (generation product), Siemens copilot (chat, no tree execution).
- Difficulty: MEDIUM-HIGH (tree extraction from text is doable; execution+eval harness ~2 days).

### Direction 2 — Revision-conflict-aware evidence: same-question-different-answer detection
Ingest manual corpus with revision metadata; when retrieval returns conflicting procedure
claims (torque values, sequences, thresholds), surface the conflict with both citations and a
precedence verdict (newest-effective / OEM / local-procedure), refuse when precedence unknown.
- Resources: ConflictRAG (method), GVD (method), Semitora/Symaxx (pattern as advice,
  non-competing), HoldPoint (construction domain, proves pattern, different domain).
- Closest competitors: HoldPoint (construction RFIs, not equipment manuals); TMS QA tools
  (pairwise document QA, not retrieval-path).
- Difficulty: MEDIUM (conflict classification via NLI/LLM on retrieved pairs; precedence rules
  deterministic).

### Direction 3 — Safe diagnostic decision-making: refusal/escalation on false-premise faults
System distinguishes "fault confirmed with evidence" from "no documented answer" from
"premise unverified — verify before acting", evaluated on false-premise fault scenarios.
- Resources: FaulT-Bench (proves the failure mode: agents over-diagnose healthy systems),
  RegLLM harness (escalation labels), PHM Society eval framework.
- Closest competitors: FaulT-Bench is a benchmark, not a product; no system demonstrates the
  fix.
- Difficulty: MEDIUM (needs a fault-scenario dataset — would have to synthesize from manual
  content; the build is mostly evaluation).

## 4. Established vs unproven (honesty ledger)
- ESTABLISHED: retrieval, citations, hybrid search, multimodal page retrieval, QA benchmarks,
  guide generation, conflict detection as a research method, revision control as practice.
- UNPROVEN (our potential novelty): executing manual-grounded decision trees interactively with
  per-node evidence + refusal; revision-conflict-aware retrieval on equipment manuals; a
  measured structured-retrieval advantage on the public Panasonic benchmark; safe
  false-premise refusal for equipment faults.
