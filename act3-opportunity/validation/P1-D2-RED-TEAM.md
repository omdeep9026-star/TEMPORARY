# P1 Direction-2 Red Team — Revision-conflict-aware evidence retrieval

Date: 2026-10-10. Method: adversarial search battery (6 angles, web_search limit 5–8 + browser
rendering of JS-heavy pages + GitHub API). Purpose: break the claim below before it enters the pitch.

## CLAIM UNDER TEST

"Revision-conflict-aware evidence retrieval for equipment manuals — same-question-different-answer
detection with precedence verdict and refusal. No product applies conflict/reversion detection to
equipment manual collections in a RAG retrieval path; closest is HoldPoint (construction RFIs,
hackathon, synthetic), Symaxx/Semitora (pattern published as advice), GVD (research framework),
ConflictRAG (generic research)."

## VERDICT: PARTIALLY_DIFFERENTIATED

The narrow claim technically survives — no found product executes the full combination
(equipment-manual corpus + query-time same-question-different-answer detection between retrieved
revisions + precedence verdict with both citations + refusal on unknown precedence). But the gap is
materially narrower and shakier than FINDINGS.md presented. Three counterexamples reduce the
mechanism's novelty; one of them is live on the same platform (lablab.ai) in the same AMD ecosystem,
overlapping ACT III's dates. Differentiation now rests on domain + verdict semantics + demo quality,
not on "nobody does this."

---

## COUNTEREXAMPLES FOUND (what breaks, what doesn't)

### Tier 1 — directly attacks the claim's core

**CE-1. "Saudi Sign Intelligence" — lablab.ai AMD AI League Match 3 submission (LIVE)**
https://lablab.ai/ai-hackathons/amd-lablab-ai-academy-challenge (submissions section, rendered DOM)
- Verbatim: "(3) Superseded revisions are detected from what a document says about itself and from
  revision families, then hidden, so the model never sees the decoy number." Plus verified
  code-level citation checks, empty-answer refusal, Qwen3-VL-8B on ROCm, 10/10 sample + 20/20
  stress set, 3–6 s/question.
- DOES: reversion detection + retrieval-path hiding + refusal in a RAG container, ON AMD hardware,
  ON lablab.ai — the same platform as ACT III. Match 3 (RAG) ran Sep 29 → Oct 13; ACT III runs
  Oct 12–18. ACT III judges plausibly reviewed this exact pattern days earlier.
- DOES NOT: equipment-manual domain (mixed enterprise document folder: specs, logs, CSVs, DOCX);
  pairwise same-question-different-answer conflict surfacing (it hides, not compares); precedence
  verdict with both citations; refusal tied to revision authority specifically.
- Impact: kills any pitch phrased as "we detect superseded revisions in the RAG path." The
  FINDINGS gap #2 ("the equipment-manual slice of revision-conflict-aware retrieval is open")
  survives only with domain + verdict-semantics qualifiers, and the sibling-event precedent must
  be acknowledged, not discovered by judges.

**CE-2. Author-it AION — commercial CCMS vendor, public torque-conflict proof point**
https://www.author-it.com/ai/proof
- Verbatim: three conflicting torque values (15 Nm from a 2012 sales handout, 22 Nm from the
  current service manual p.188, 51 Nm from a spec "superseded in 2019, that nobody removed from
  the folder"); architectural publishing gate — "A draft procedure, a superseded revision or an
  archived spec can't appear in an AION file… There's no setting to switch that off."
- DOES: a COMMERCIAL product makes the exact failure class (conflicting torque values on
  equipment/service documentation, superseded revision in the AI path) its marketing centerpiece,
  with a structural guarantee superseded content never reaches the AI output.
- DOES NOT: retrieval-path detection over an existing messy PDF corpus (requires content authored
  in Author-it's CCMS); query-time conflict detection; precedence verdict; refusal semantics.
- Impact: the "conflicting torque from a superseded revision" story is not virgin territory — a
  judge who knows Author-it has seen it as a vendor demo. The pitch must differentiate on
  detection/verdict over UNCONTROLLED legacy corpora (the realistic case), not on the failure mode.

**CE-3. MakinaRocks — commercial AI revision comparison for nuclear equipment documents**
https://www.makinarocks.ai/en/use-case/ai-powered-document-comparison-automating-revision-reviews-for-nuclear-equipment/
- DOES: deployed system — VLM extraction → structured data → vector embeddings → "comparing
  structured information across document versions, the system identifies specific changes" — for
  NUCLEAR EQUIPMENT requirements documents.
- DOES NOT: query-time RAG conflict verdict; same-question-different-answer detection at
  retrieval; refusal; it's an offline ingestion-side review workflow.
- Impact: "revision comparison on equipment documents" exists commercially in an adjacent domain
  (nuclear requirements docs, not manuals). Weakens "equipment slice is open" to "equipment-MANUAL
  query-time slice is open."

### Tier 2 — mechanism exists as shipped code / published prior art outside equipment manuals

**CE-4. ClawMem — OSS agent-memory RAG layer, 212 stars, MIT, created 2026-02-06**
https://github.com/yoloshii/ClawMem (docs/concepts/architecture.md)
- Verbatim: "retrieval can surface a superseded revision as though it were current — a quiet
  correctness problem"; `supersede` operation marks old rows inactive "with superseded_by set.
  The old row is filtered from retrieval but preserved for audit. Requires a configured judge."
- DOES: supersede-aware retrieval filtering with judge-mediated precedence in a shipped, popular
  RAG layer. DOES NOT: equipment manuals (agent memory/notes), pairwise conflict surfacing,
  precedence-verdict UX, refusal-on-unknown-authority.
- Impact: the "detect + filter superseded revisions in a RAG path" mechanism is shipped OSS with
  212 stars — the claim's phrase "in a RAG retrieval path" cannot carry the novelty alone.

**CE-5. Temporal-Aware RAG with Belief Revision — GitHub, created 2026-07-16, 0 stars**
https://github.com/Manvendra-SR/Temporal-Aware-RAG-with-Belief-Revision
- "Resolves conflicting information using belief revision and time-aware retrieval." Generic
  research repo. Confirms conflict-resolution-in-RAG-path exists as a public mechanism.

**CE-6. Alhena FAQ Conflict Detection — commercial product**
https://alhena.ai/blog/faq-conflict-detection-ai-knowledge-base
- DOES: shipped product doing semantic same-question-different-answer detection ("automatically
  checks whether a new or edited FAQ contradicts any existing FAQ"), MADAM-RAG frequency-bias
  framing. DOES NOT: equipment manuals; retrieval-path-at-query-time (edit-time QC layer);
  precedence verdicts. Impact: the flagship mechanism ("same-question-different-answer
  detection") already exists as a product feature in another document domain.

**CE-7. EACL 2026 industry paper — Compliance-Preserving Retrieval for Aircraft MRO Task Search**
https://aclanthology.org/2026.eacl-industry.23.pdf
- DOES: revision-cycle-aware retrieval on REAL equipment manuals (aircraft AMM), certified-source
  traceability, 49k-query benchmark + bilingual study with 10 licensed AMTs, 95% lookup-time
  reduction. Explicitly claims novelty for its constraint combination. DOES NOT: query-time
  conflict detection between revisions (sidesteps via stable-metadata embeddings); precedence
  verdict; refusal.
- Impact: the strongest academic prior art for "revision-aware retrieval on equipment manuals."
  FINDINGS' equipment-manual slice must cite and distinguish this paper; a pitch that ignores it
  is falsifiable by judges.

**CE-8. X-MADAM-RAG (arXiv 2606.12903) + ECON (deep-paper.org/en/paper/2410.04068) + Kontrast
(kenashe.ai audit blog) + re-query-on-conflict (theneuralbase.com)** — generic research/pattern
layer for conflict-aware aggregation, deterministic candidate grouping, evidence-conflict
detection. Supports the ConflictRAG-line prior art already in FINDINGS.

### Tier 3 — "pattern published as advice" is CONFIRMED and BROADER than FINDINGS recorded

FINDINGS credited only Symaxx/Semitora. Red team found five more sources publishing the mechanism
as advice/tutorial, several with runnable code:

| Source | URL | Contribution |
|---|---|---|
| TOMAS TECH | https://tomastc.com/en/blog/equipment-manual-search-ai-2026-en | Equipment manual search AI 2026: superseded-revision removal from retrieval path, refusal conditions, "wrong answer leads" framing (torque/shutdown) |
| Semitora (already in FINDINGS) | https://semitora.com/blog/en/rag-manufacturing-technical-documents/ | 7 controls incl. supersedes relationship, conflict flagging, expose-and-route |
| Helpfeel | https://en.helpfeel.com/blog/ai-manual-revision-check | REAL Graco manual revision conflict worked example (Rev C vs Rev H battery voltage wording), "revision conflict unresolved" disposition |
| ranknod (dev.to) | https://dev.to/ranknod/how-to-flag-stale-rag-documents-before-generation-2k08 | RUNNABLE freshness-gate code: superseded_revision / not_effective_yet / review_overdue |
| mikitadaroshkin | https://mikitadaroshkin.com/posts/rag-on-a-regulated-corpus | Bitemporal dedup-to-in-force-revision gate + audit: 26/38 wrong answers were faithful-to-superseded-revision |
| DocuShell | https://docushell.com/blog/how-do-i-turn-pdf-manuals-into-a-rag-knowledge-base | "If the evidence conflicts across editions, say so instead of choosing silently"; preserve supersession links |
| shakewellusa | https://shakewellusa.com/insights/rag-on-the-hangar-floor | Aviation: "quoting a superseded revision to a mechanic… The model didn't fail. The library did." |
| embernet.ai | https://embernet.ai/whitepapers/the-maintenance-assistant-that-knows-your-plant.html | "Indexing the share drive as-is. Superseded revisions… produce confident answers from the wrong document" as named anti-pattern; torque quote-don't-compute rule |
| mesengineer.com | https://mesengineer.com/2026/07/15/your-shop-floor-ai-agent-is-only-as-smart-as-the-context-you-feed-it | "spec revision C superseded revision B" shop-floor failure anecdote |

Also relevant: OxMaint (commercial aviation manual-management CMMS with revision-locked task cards,
effectivity-by-tail, supersession archiving — https://oxmaint.ai/industries/aviation-management/
aviation-technical-publication-manual-management-cmms) confirms "revision control as practice"
(FINDINGS [20]) and adds a commercial equipment-manual example; CN122088686A patent
(https://eureka.patsnap.com/patent/CN122088686A) covers LLM SOP extraction from maintenance
manuals into vector libraries.

### Search angle (6) — TMS/translation-QA tools on equipment manuals: CLOSED for QA, open for conflicts
Commercial translation-QA IS applied to equipment manuals: Stepes MRO translation names torque
values in its numbers/units checks (https://www.stepes.com/mro-translation-services/), Hansem
Device Term Guard automates term QA on manual pages
(https://hansem.com/blog/automated-term-consistency-device-term-guard/), and the OSS
claude-fidelity-translator does deterministic verification (numbers, citations, callout order) for
aerospace manuals (https://github.com/Tasdax123/claude-fidelity-translator). NONE do revision-
conflict detection, retrieval-path checks, or precedence verdicts. This angle yields no breaker.

### Angles (1) and (2) — Devpost / lablab site-scoped searches
- site:devpost.com manual revision conflict → no relevant project found (only ToS/help pages).
- site:lablab.ai revision conflict document → no direct hit; the CE-1 counterexample was found
  only by rendering the AMD AI League page DOM (site search does not index the submissions
  section). Lesson: lablab submission galleries are a blind spot for site-scoped search.

---

## HOLDPOINT VERIFICATION (as instructed)

https://github.com/luzzwaix/holdpoint — CONFIRMED genuine and NOT in the equipment-manual domain.
- Description: "Construction revision conflict detection with multi-model extraction and a
  deterministic decision engine."
- Stars: 1, Forks: 0, Watchers: 1, Open issues: 0, 2 commits. Created: 2026-08-16 (Impact Forge
  Summer 2026 badge). Live demo: https://holdpoint-alpha.vercel.app
- Domain evidence: drawing A12 Rev 3, RFI-047, embed plate EP-17 / column C14 clearance, HOLD POUR,
  work packages — construction RFIs/drawings throughout. No equipment-manual content.
- Deterministic engine confirmed: "deterministic normalization + precedence," 2-of-3 model
  consensus (DeepSeek V4 Flash + Qwen 3.8 + GLM-5.2 escalation), HOLD/PROCEED/NEEDS REVIEW,
  dependency propagation, re-verification after approval.
- Self-declared limitations: synthetic dataset, no production BIM/CAD parser, no document-control
  integration, "hackathon prototype and decision-support tool."
- FINDINGS' characterization (construction, hackathon, synthetic, deterministic precedence) is
  ACCURATE. Note for the pitch: HoldPoint is a near-zero-traction sibling (1 star), so "closest
  competitor" framing is safe — but the pattern match (newer doc supersedes scoped instruction →
  deterministic verdict → hold) is exactly what an ACT III judge will recognize; cite it as
  inspiration-transfer across domains rather than implying parallel discovery.

---

## IMPLEMENTATION FEASIBILITY (4–5 effective build days): FEASIBLE, two real risks

Proven-on-AMD components reduce infra risk: the lablab Match 3 pattern (resident model server +
stdlib thin client, Qwen3-VL-8B BF16 ~18 GB on MI300X, 12 s startup) is public
(https://dev.to/eterniti/the-amd-mini-challenge-3-citation-by-necessity-rag-on-rocm-4ljm), and
Docling/MinerU ingestion + bge embeddings are commoditized.

Sketch: Day 1–2 ingestion (Docling → markdown + revision-metadata extraction from manual
self-declaration: doc number, rev letter, date, supersedes field — Helpfeel's Graco example shows
real manuals carry these) + hybrid index. Day 2.5–3.5 conflict detection: group retrieved chunks by
(doc_id, section), pairwise NLI/LLM pass on numeric/procedural claims (ConflictRAG pattern:
embedding-MLP shortlist + selective LLM verdict), deterministic precedence engine
(newest-effective > OEM > local-procedure; unknown → refuse). Day 4 eval: golden set with answerable
/ conflict / refusal cases; report conflict-detection F1 + wrong-version-answer delta vs. a
baseline RAG that silently serves the superseded chunk (mikitadaroshkin's 26/38 audit is the
template). Day 4.5–5 demo UI: conflict card with both citations, precedence verdict, refusal state.

Risks: (a) REAL revision-family corpus — Graco public manuals (multiple revisions downloadable)
are the only confirmed real source found; a synthesized corpus is buildable in a day but is the
credibility weak point, so declare it; (b) conflict-detection F1 on OCR'd manual text is unproven —
budget a fallback where numeric-field comparison (pint unit-aware) carries the precision-critical
class and LLM/NLI covers procedural claims.

## "LINTING FEATURE" RISK (judges' perception): HIGH-MED without a workflow shell

The bare mechanism (flag conflicts + verdict) reads as a QA checkbox — "the RAG tells you when
it's unsure" — which threatens the 25% product and 20% business slices. Mitigations that make it
read as a product, in priority order:
1. Refusal as an ENFORCED STATE, not a warning: answer withheld, work-order sign-off blocked until
   precedence is resolved (OxMaint blocks sign-off on unacknowledged revisions — same pattern).
2. Conflict ledger as an auditable artifact: per-verdict traceability (which revision governed,
  when, by which rule) — turns a lint pass into a compliance record.
3. Measured delta vs. silent baseline RAG (the 26/38 wrong-version pattern) — judges reward
   demonstrated harm prevented, not mechanism existence.
4. Narrative anchored on the documented stakes (TOMAS TECH: "a tightening torque from a superseded
   revision — equipment breaks or someone gets hurt"), not on RAG plumbing.
5. Multi-source precedence (OEM vs plant-local procedure) — no counterexample implements this;
   it is the strongest remaining unclaimed semantic.

## BOTTOM LINE FOR THE PITCH

- Do NOT pitch "conflict/reversion detection in a RAG path" as the novelty — CE-1/CE-4/CE-6 kill it.
- Pitch the FULL COMBINATION on equipment manuals: same-question-different-answer detection
  BETWEEN RETRIEVED REVISIONS + precedence verdict citing both sources + refusal on unknown
  authority + enforced-state demo — over an UNCONTROLLED legacy PDF corpus (vs. Author-it's
  authoring-side gate and vs. Match 3's hide-don't-verdict).
- MUST cite-and-distinguish: CE-1 (lablab Match 3, same platform), Author-it AION, MakinaRocks,
  EACL 2026 MRO paper, ClawMem. Discovering these in the room is fatal; preempting them is a
  strength.
- Amendment to FINDINGS gap #2: keep the gap, add the qualifiers "query-time verdict semantics on
  uncontrolled corpora" and note the sibling-platform precedent; add CE-1 through CE-9 to the
  citation ledger.
