# Red-Team Verdict — Direction 3 claim: "Safe diagnostic decision-making — measured refusal/escalation on false-premise fault reports"

Date: 2026-10-10. Method: 8 web searches (devpost, lablab, GitHub, product/pattern angles) + primary-source
verification of FaulT-Bench (arXiv HTML full text) and its repo. All numbers below read directly from
sources, not from FINDINGS.md.

## VERDICT: PARTIALLY_DIFFERENTIATED

The narrow claim survives: no artifact was found that demonstrates **measured refusal/escalation accuracy
on false-premise fault reports for equipment troubleshooting, evaluated on a public benchmark, as a
product demo**. The broad claim is broken on three edges: (1) refusal-as-product exists in adjacent
repair/diagnostic domains (unmeasured); (2) measured refusal exists in generic domains (not diagnostic);
(3) the mechanism itself is a documented pattern, not a novelty.

## Baseline verification (claimed numbers CONFIRMED against primary source)

From https://arxiv.org/html/2608.27021v1 (§5, Tables 4–7) — mean outcome scores:
- Correct-Fault (n=80): **0.932** (SADE 0.912 / CC-Baseline 0.942 / ReAct 0.941)
- Wrong-Device (n=24): **0.957** — misdirection does NOT hurt; it is +0.025 ABOVE accurate tickets
- Wrong-Cause (n=24): 0.911 (−0.021)
- False-Premise (n=72): **0.820** (SADE 0.745 / CC 0.870 / ReAct 0.848) — confirmed drop
- Over-diagnosis on healthy networks: SADE 24% (51/210), ReAct 16% (33/209), CC 11% (21/198) of answered runs
- Failure shape confirmed: agents disprove the reported symptom, keep probing, promote a benign standing
  condition to root cause instead of concluding "nothing is wrong."

WORDING FINDING (the claim understates this — it cuts against the candidate's framing):
- Abstract verbatim: "how a ticket is written matters more than what it claims: a confidently wrong
  report is handled about as well as an accurate one, while a vague, underspecified report degrades
  performance sharply."
- Naive→Naive-unsure (certainty withdrawn): outcome −0.182, over-diagnosis 16%→35%. Identifiers removed
  next: −0.141 further, over-diagnosis 47%. Outcome chain 0.820 → 0.638 → 0.497.
- CC-Baseline: certainty withdrawal alone −0.425, over-diagnosis 7%→51%; on no-detail tickets it
  exhausts the 20-turn budget in 49% of runs.
- IMPLICATION: "false premise" is the SMALLER failure slice. The collapse is on VAGUE/underspecified
  reports. A candidate pitched only on false-premise refusal is attacking the secondary finding.

## FaulT-Bench code/data: RELEASED (search #6 — resolved)

https://github.com/Overlxrd-uwu/FaulT-Bench — MIT license, dataset CC BY 4.0.
- 560 scenarios (200 core + 360 persona rewrites of 72 false-premise tickets), 8 Kathará topologies
- 3,960 frozen runs incl. full diagnosis + per-axis judge scores + investigation traces
- Verification tools that recompute every paper number without Docker or API keys
- Works with the SADE-NetworkAgent repo (agents + Kathará MCP tool layer)
Double-edged: makes the 4-5 day build far more feasible than FINDINGS.md assumed (dataset exists, no
synthesis needed); but also means any competing team can build the same fix on the same public data —
no data moat. Also: the benchmark is NETWORK equipment (Kathará/NIKA), not plant/factory equipment.

## Counterexamples (what breaks, what doesn't)

1. **Continuity** — https://devpost.com/software/continuity-y47f6o
   Board-level electronics repair diagnostic product. Explicit refusal positioning: "An AI repair tech
   can't be allowed to guess… a confident hallucination is worse than 'I don't know'"; agent may only
   cite database rows ("no row → no such part"); deterministic SQL verifier stamps VERIFIED before human
   sees it. DOES: refusal-by-construction as a shipped product capability in repair diagnostics.
   DOES NOT: any measured refusal/false-premise accuracy (no eval numbers on healthy-board tickets);
   single seeded board (ingestion listed as "What's next"); not manual-grounded; not benchmarked.
   → Breaks "no product anywhere"; does NOT break the measured-false-premise gap.

2. **Failure-Aware ERNIE** — https://baiduernieai.devpost.com/submissions/885496-failure-aware-ernie
   Fine-tuned ERNIE 4.5 0.3B with structured decide-correct|uncertain|refuse outputs; measured False
   Confidence Rate, Hallucination Rate, ECE; results: −11.8pp false confidence, +14.1% calibration,
   uncertainty expression 1.3%→12%. DOES: measured refusal accuracy as a hackathon capability.
   DOES NOT: industrial/equipment domain, no agentic tool use, no live-system probing, no fault scenarios.
   → Breaks "measured refusal is undemonstrated anywhere"; does NOT break it for equipment diagnosis.

3. **The Living Archive (Nemotron edition)** — https://devpost.com/software/the-living-archive-nemotron-edition
   Corpus QA that "refuses with a reason when the corpus is silent"; deterministic citation guard refused
   100% of unanswerable questions at 0% hallucination, with published JSONL + CI gate.
   → Same class as #2: measured refusal, generic QA domain.

4. **MindRAG** — https://arxiv.org/abs/2506.09247
   LLM agent framework for industrial condition monitoring explicitly targeting "reducing false alarms."
   Closest scholarly neighbor. DOES: names the exact industrial pain (high CM false-alarm rates) and
   builds agent decision support. DOES NOT: measure refusal accuracy, no false-premise fault-report eval,
   preliminary results with a single analyst, no public benchmark numbers.

5. **The abstention/escalation pattern is published prior art** (kills mechanism novelty):
   - https://tianpan.co/blog/2026/04/28/abstention-routing-not-prompt-pattern — typed abstention output,
     escalation routes, separate SLOs ("over-abstention <5%", "miscalibrated <2%")
   - https://litmusevals.org/ — 78,631 evals, 11 models: abstention collapse + one-line fix measured
   - https://dreaming.press/posts/when-should-an-ai-agent-ask-for-help.html — AbstentionBench (NeurIPS
     2025: abstention unsolved, reasoning FT degrades it), HiL-Bench (89%→24% success when details
     removed; agents guess instead of asking), R2V (external process verifier escalates — 93.3%
     TerminalBench). Establishes the known fix pattern: EXTERNAL verifier, not self-reported confidence.
   - https://ragexplainedbetter.com/generation/refusal/, https://jev101.org/recipes/decision-model-abstention
     — recipe-level guidance: measure don't-know rate AND over-refusal separately, refuse-enums, owners.
   → A hackathon pitch claiming "we invented refusal/escalation" dies here. Survivable claim: "first
   MEASURED refusal/escalation accuracy on false-premise fault reports, public benchmark, operator artifact."

6. **Same-event prior art (AMD ACT II)**:
   - https://lablab.ai/ai-hackathons/amd-developer-hackathon-act-ii/sune/saboteur — chaos-tests agents,
     resilience scorecard, deception detection; MI300X/vLLM cohort runs. Agent-failure QA, not diagnosis.
   - https://lablab.ai/ai-hackathons/amd-developer-hackathon-act-ii/live?track=1 — "TokenRouter — prove
     or escalate agent" (89.5% accuracy) placed #3 on the ACT II Track 1 leaderboard: "prove or escalate"
     as a phrase already scored well at this event, though in token-routing, not diagnostics.

Searches that returned nothing (labeled absences, not proof):
- site:lablab.ai industrial diagnostic refusal/escalation → no equipment-diagnostic refusal product
- GitHub "refusal calibration + diagnostic + escalation + industrial" → nothing combining all four
- "safe diagnostic product equipment refusal evidence" → nothing

## Feasibility in 4-5 days: STRONG (upgraded from FINDINGS.md's MEDIUM)

- Dataset problem SOLVED: FaulT-Bench released 560 scenarios + harness + 3,960 frozen runs (MIT/CC BY 4.0).
  The build reduces to: (a) reproduce/reuse baseline runs showing 11-24% over-diagnosis; (b) add a
  premise-verification + stopping layer (external verifier pattern per prior art — do NOT rely on the
  model's self-confidence, AbstentionBench shows that fails); (c) measure the 2x2: false-alarm rate on
  healthy networks, correct-"nothing wrong" rate, over-refusal on genuine-fault tickets, NFF handling;
  (d) operator-facing triage verdict UI.
- AMD fit: base agent on vLLM/MI300X per event requirement; FaulT-Bench verification tools run with no
  GPU at all; the frozen runs de-risk demo-day compute.
- OPEN RISKS: (1) Kathará/NIKA harness is Docker-based — must confirm Docker works on AMD Developer
  Cloud before committing (fallback: score against frozen runs + verify tools, demo the layer offline);
  (2) domain is networks, not factory equipment — pitch must say "equipment = network infrastructure"
  honestly or add a small synthetic equipment slice (adds risk, low reward); (3) the stopping-rule fix
  is the obvious next move the paper itself gestures at — other teams can land on it; speed + measurement
  rigor are the moat.

## Judges/scoring risk (Track 1: "results operators can understand")

- A leaderboard of refusal percentages is a research poster, not a product. To score as a product the
  refusal must BE the operator artifact: a triage verdict card per ticket — "fault verified + evidence /
  premise unverified + the 2 checks to run / no fault found + what was ruled out" — with citations, plus
  the measured false-alarm vs over-refusal trade-off shown as dispatch decisions avoided (wasted truck
  roll framing), not as model metrics.
- The persona finding is actually the more operator-legible story: "the ticket is underspecified — ask
  these two questions before dispatching" is behavior every operator understands; "false-premise refusal"
  is jargon. Recommend pitching premise+specificity gating with false-premise as the headline eval slice,
  not the whole product.

## Revised claim that survives red-team

"FaulT-Bench (public code + data) shows SOTA agents over-diagnose healthy networks (11-24% of answered
runs) and collapse further on vague tickets (outcome 0.820→0.497, over-diagnosis to 47%). No existing
system measures or fixes this as a product capability: adjacent products are honest-by-construction
without measurement (Continuity), measured refusal exists only in generic QA (Failure-Aware ERNIE, The
Living Archive), and industrial false-alarm work (MindRAG) has no refusal metric. We deliver the first
measured refusal/escalation benchmark result on false-premise and underspecified fault tickets, as an
operator-facing triage product, on AMD MI300X."
