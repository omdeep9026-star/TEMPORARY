# Scoring Model — Part 8 definition

Date: 2026-10-09. The official Act 3 judging rubric (VERIFIED in EVENT-CONSTRAINTS.md) lists four
criteria with NO published numeric weights. This model therefore uses a disclosed provisional
weighting built on the official criteria, plus supplementary dimensions required by the mission
brief. All scores are 1–5 with written anchors. No false precision: every score carries a
rationale and confidence level.

## Official criteria (provisional weights, disclosed)

| Criterion | Official definition (abbreviated) | Weight | Anchor: 5 means |
|---|---|---|---|
| Application of Technology | How effectively the chosen model(s) are integrated | 30% | The model does real, load-bearing work shown in the demo; AMD component is visible and meaningful; integration is architectural, not cosmetic |
| Business Value | Impact and practical value in business areas | 25% | A named user with a named workflow; measurable benefit; credible willingness to pay |
| Originality | Uniqueness, creativity, ability to demonstrate behaviors | 25% | A mechanism or workflow nobody automated this way; differentiation is verifiable, not claimed |
| Presentation | Clarity and effectiveness of the presentation | 20% | A tired judge understands the problem and the proof in one pass; live demo is compact and complete |

Weighting rationale: the event's central statement ("the product should work, and AMD technology
should power a meaningful part of it") and the submission requirement of a working prototype make
working technology the anchor; the four business tracks with named users make business value
second; originality and presentation follow. The weights are provisional and disclosed.

## Supplementary dimensions (applied as gates and modifiers, not weights)

| Dimension | Definition | Scale |
|---|---|---|
| Problem significance | Severity × frequency of the underlying problem | 1–5 |
| Evidence quality | Source reliability, independence, recency | 1–5 |
| Competitive differentiation | Distance from the closest existing solution | 1–5 |
| Technical depth | Non-trivial mechanisms (deterministic verification, constrained generation) | 1–5 |
| End-to-end completeness | Workflow runs from real input to final artifact | 1–5 |
| Demonstration clarity | Compact, complete, verifiable live demo | 1–5 |
| Implementation feasibility | Fits 4–5 effective build days | 1–5 |
| Reliability & verifiability | Numbers reproducible without API keys; degradation toward accuracy | 1–5 |
| Measurable user benefit | Quantified improvement (time, cost, safety) | 1–5 |
| Potential for further development | Roadmap beyond the hackathon | 1–5 |

## Scoring procedure

1. Each surviving candidate is scored on the four weighted official criteria.
2. Supplementary dimensions are reported alongside as rationale; a candidate scoring ≤2 on
   implementation feasibility or reliability is disqualified regardless of weighted total.
3. Every score carries a rationale and a confidence level (HIGH/MED/LOW).
4. A candidate must not rank highly because it sounds futuristic, uses many agents, or has little
   visible competition — originality scores require verifiable differentiation, and "little
   visible competition" triggers a mandatory re-search before a high originality score stands.

## Candidate preliminary scores (pre-red-team; revised after red team)

### Candidate A — LEDGER (preservation-verified multilingual safety-document workbench)

| Criterion | Score | Rationale | Conf |
|---|---|---|---|
| Application of Technology | 4 | Open model via vLLM on AMD does the load-bearing generation work, shown live with endpoint status; deterministic gates are the differentiating layer; not GPU-heavy compute (no training) | MED |
| Business Value | 4 | Named user (EHS/safety manager), named workflow (translated safety docs), regulatory stakes documented; willingness to pay inferred from human-review costs (Korea: 40 min/briefing), not measured | MED |
| Originality | 4 | Deterministic preservation verification applied to translated safety documents — no direct competitor found across web+scholarly retrieval; mechanism proven on a different document class (Intact), applied where untouched; verifiable via harness | MED |
| Presentation | 4 | Compact 6-minute flow; the baseline-corruption pivot is a strong demo beat; risk: "verification" may read as linting if not staged well | MED |
| Weighted total | 4.05 / 5 | 0.30·4 + 0.25·4 + 0.25·4 + 0.20·4 | — |
| Problem significance | 4 | Safety-critical, workforce-wide, recurring; quantitative incident data thin | MED |
| Evidence quality | 4 | OSHA (regulator), Korea Herald (independent press), deployments; gap-claim labeled as absence-not-proof | HIGH |
| Competitive differentiation | 4 | No direct competitor found; SafetyBridge prompt-based; DeepL no verification | MED |
| Technical depth | 4 | Deterministic gates + ledger-constrained generation + adversarial harness; pint unit algebra; softening detection | HIGH |
| End-to-end completeness | 4 | Real input → verified multilingual artifact, all stages live or labeled | MED |
| Demonstration clarity | 4 | Six-minute single flow; fallback rehearsed | MED |
| Implementation feasibility | 4 | ~4 build days; risks in multilingual ledger rendering quality | MED |
| Reliability & verifiability | 5 | Gates and harness run with zero API keys; numbers reproducible by anyone | HIGH |
| Measurable user benefit | 3 | Corruption interception is measurable; real-world time savings inferred not measured | MED |
| Further development | 4 | Domain-general mechanism (Intact's own roadmap); compliance training, tenancy, benefit letters | MED |

### Candidate B — TRACEBOOK (technician evidence workbench)

| Criterion | Score | Rationale | Conf |
|---|---|---|---|
| Application of Technology | 3 | RAG + structured lookup on AMD; solid but commoditized pattern | HIGH |
| Business Value | 3 | Real user and pain; benefit claims are vendor-derived | MED |
| Originality | 2 | Adjacent to shipped vendor products (Siemens/Caterpillar) and published lab recipes; refusal + structured lookup is incremental | HIGH |
| Presentation | 3 | Answer-with-citations demos are common; risk of "another chatbot" | MED |
| Weighted total | 2.75 / 5 | — | — |
| Problem significance | 4 | Verified first-person pain, recurring | HIGH |
| Competitive differentiation | 2 | Incremental | HIGH |
| Technical depth | 3 | Confidence gates + structured lookup; not novel | MED |
| Implementation feasibility | 4 | Corpus and stack are proven | MED |
| Reliability & verifiability | 3 | Retrieval quality hard to reproduce crisply; refusal threshold tunable | MED |

### Candidate C — INTACT-ML (multilingual discharge verification) — DISQUALIFIED on originality

Weighted total ~3.4 but REJECTED: re-build of an existing hackathon project's exact mechanism one
month after publication (COMPETITIVE-INTELLIGENCE.md C3). Originality score of 1–2 stands
regardless of other dimensions. Listed for the audit trail.
