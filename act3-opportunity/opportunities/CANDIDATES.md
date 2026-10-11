# Candidate Solutions — Part 5/6 output

Date: 2026-10-09. Generated ONLY after the problem investigation (Part 3–5) and competitive
invalidation scan (COMPETITIVE-INTELLIGENCE.md) completed. Three surviving candidates, ranked
provisionally; red team runs before final ranking (see validation/).

---

## Candidate A — LEDGER: Preservation-verified multilingual safety-document workbench (PRIMARY)

**Problem solved (from P4):** Multilingual workforces receive safety instructions, lockout/tagout
procedures, and compliance content translated by generic MT or ad-hoc AI with nobody checking the
result. "A poorly translated safety course can fail [OSHA's] bar even though a translation
technically exists" (icantech.ai). Korea's largest builders deployed AI translators but guarantee
quality with 40-minute human re-reading per briefing (Korea Herald). No deterministic
verification layer was found anywhere (COMPETITIVE-INTELLIGENCE.md C4).

**Proposed user experience:** An EHS manager or safety officer uploads an English safety document
(lockout/tagout procedure, toolbox talk, machine safety sheet) and picks target languages and a
reading level. The system returns, per language: a plain-language rendering at the chosen level,
plus a verification report — every quantity, unit, negation, urgency phrase, and regulatory
citation provably preserved, every added claim stripped, every output sentence traced to a source
fact. Documents that cannot be verified safely are flagged, not published.

**End-to-end workflow:**
1. Extract a fact ledger from the source document: quantities with units (pint-parsed,
   dimension-aware), machine/part names, negations, urgency/timeframe phrases, regulatory
   citations (e.g., OSHA 1910.147), hazard keywords.
2. A rewriter — an open model served via vLLM on AMD infrastructure — sees ONLY the ledger (never
   the source text) and renders the target language at the target reading level. This is the
   constraint in the architecture that removes the material it would hallucinate from.
3. Two deterministic gates, neither a model call: PRESERVATION (unit-aware magnitude comparison so
   500 kPa ≠ 50 kPa and 5 mg never matches 5 ml; strict name matching; citations must survive;
   urgency must be retained with explicit softening-phrase detection) and ADDITIONS (any claim not
   traceable to a ledger fact is stripped, not merely flagged).
4. On gate failure: one stricter rewrite, then template rendering of the ledger. The system
   degrades toward less fluent output, never toward less accurate output.

**Defining technical capability:** Deterministic, reproducible preservation verification of
translated safety-critical documents covering the FULL safety-critical fact class —
quantities+units (unit-aware magnitude), negations, urgency phrases with softening-severity
detection, AND regulatory citations — with ledger-constrained generation (rewriter never sees the
source), refusal-to-publish, and per-fact traceability — enforced by code, reproducible by anyone
with no API key, on an AMD-hosted open model.

**Strongest differentiation (RED-TEAM NARROWED — original broad claim retired):** The broad
claim "verification is new" does NOT survive red-team attack: deterministic verification of
translated safety-critical content exists in fragments — DoseGuard (Devpost ~Apr 2026, translated
medication instructions, numeric normalization + diacritic checklist), AlertProof ATX (Devpost
~Aug 2026, protected-fact registry + sabotage test for multilingual emergency messages), TrueCopy
(Devpost Sept 2026, deterministic refusal gate + adversarial harness on YouTube metadata),
SpecMake (commercial, unit-preserving translation into 14 languages + EU compliance cross-checks
on source), TMS QA tools (Xbench/Verifika/memoQ/Trados — number/omission/glossary/tag checks for
years), and DeepL TQE (model-based error detection). WHAT SURVIVES the attack: no product,
project, or research artifact combines preservation gates over the FULL safety-critical fact
class (negations + urgency-severity + citations on top of units/quantities) with
ledger-constrained generation, refusal-to-publish, and per-fact traceability, applied to
industrial safety documents. Negations and urgency are verifiably unchecked by every shipped tool
(TMS QA "cannot assess meaning"; negation is a documented unsolved MT failure mode, >60% quality
reduction in some directions — aclanthology.org/2020.findings-emnlp.345). The honest gap is "no
productized deterministic automation for the full safety-critical fact class on safety
documents," where OSHA's understandability standard and the EU Machinery Regulation (2023/1230,
effective Jan 2027) raise the stakes.

**Evidence supporting differentiation:** COMPETITIVE-INTELLIGENCE.md C4 (no direct competitor
found across web + scholarly retrieval; absence labeled as absence, not proof); icantech.ai OSHA
position; Korea Herald deployments; AD VERBUM/EU regulatory context; wave deep-dive ("Looking
under the Wrong Lamppost: On the Limitations of Automated Translation Quality" — automated
quality limitations documented in current research).

**Feasible implementation scope (RED-TEAM REVISED):** Python; pint for quantities; **Qwen 2.5
72B-Instruct as the PRIMARY rewriter** (officially supports 29+ languages including Spanish AND
Vietnamese — RED-TEAM FINDING: Llama 3.3 70B does NOT support Vietnamese per Meta's official
model card, and using it for Vietnamese contradicts Meta's usage guidance for safety-critical
tools; Llama 3.3 70B serves as a Spanish-only variant/ablation); vLLM on AMD Developer Cloud
MI300X (192 GB — a 70B BF16 model fits; AMD publishes an MXFP4 Llama-3.3-70B TP=1 for the
single-GPU case; pay-as-you-go and complimentary-credit paths documented; credits expire 10 days
from deposit); Docker flow for vLLM-ROCm (Python 3.12 + ROCm 7.x + glibc ≥ 2.35; budget 0.5–1
day setup + ~140 GB weight pre-pull on day 0/1); deterministic gates + adversarial corruption
harness run locally with zero API calls — harness EXTENDED to inject corruptions in the target
languages with per-type interception reporting; small real corpus (public OSHA/NIOSH-style LOTO
procedures, toolbox talks, machine safety sheets — US federal works, verify per-document
licenses); web UI for upload/language/level/report.

**Required adjustments from red team (binding for the build):**
1. Qwen 2.5 72B primary rewriter; Llama 3.3 Spanish-only ablation (day-1 side-by-side spike).
2. Honest ledger-recall reporting with extraction-miss flagging demo-visible (Intact precedent:
   83.6% self-reported).
3. Target-language corruption coverage in the harness (Spanish/Vietnamese corruptions, per-type
   interception numbers).
4. AMD access + Docker/vLLM setup secured day 0/1; MI300X-only credit awareness.
5. Pitch drops the misquoted Korea "40-minute" claim; demand presented as regulatory/qualitative;
   positioned explicitly against live-translation (Wordly) and human-review alternatives rather
   than claiming verification is "unsolved".
6. Related-work slide names DoseGuard/AlertProof/TMS-QA and the exact fact classes they cannot
   check; live demo leads with a DANGER→WARNING downgrade and dropped-citation interception (the
   sharpest mechanistic novelty); do not claim the gate architecture itself is novel in hackathon
   space (three of the closest competitors are Aug–Sept 2026 hackathon projects; the judging pool
   may overlap).

**Expected demo behavior:** Translate a real LOTO procedure to Spanish/Vietnamese at a chosen
reading level live; show the single-prompt baseline silently making a dangerous corruption
(decimal shift, softened urgency, dropped warning); show the ledger gates intercepting all
corruptions; run the adversarial corruption harness live (no API key needed) reproducing the
preservation numbers; show the per-fact traceability view.

**Most important risks and assumptions:**
- RISK: quantitative mistranslation incident data is thin (demand is qualitative: OSHA position,
  Korea deployments, EU regulation). Mitigation: demo shows the failure mode concretely with a
  baseline comparison.
- RISK: judges may read this as "a translation tool" and compare to DeepL. Mitigation: the demo
  leads with verification, not translation; DeepL is shown in the baseline as the tool whose
  output nobody checks.
- RISK: ledger recall (extraction misses) is the weak link (Intact self-reported 83.6%).
  Mitigation: report it honestly; scope the corpus to structured procedure documents.
- ASSUMPTION: an open model on vLLM/AMD can render ledger-constrained text in Spanish/Vietnamese
  at controlled reading levels at acceptable quality (Llama 3.3 70B multilingual capability —
  to be verified in a spike).

---

## Candidate B — TRACEBOOK: Technician evidence workbench with refusal and structured lookup

**Problem solved (from P1):** Technicians lose hours finding answers inside equipment
documentation; vendor copilots concentrate on routine failures; users distrust unverified LLM
answers; error-code indexes are "3 abstraction layers too shallow" (r/HVAC).

**Proposed user experience:** A technician enters a fault code or symptom; the workbench returns
exactly three ranked hypotheses, each citing manual page + revision, with structured lookup
(torque tables, error-code matrices as direct functions, not chunk retrieval) and explicit
refusal ("I do not have a confident answer; escalate") on low retrieval confidence.

**End-to-end workflow:** equipment/model selection → fault description or error code → parallel
retrieval (manuals, bulletins, error-code tables) → confidence gate → cited hypotheses or
refusal → session tied to a work-order ID for shift handoff.

**Defining technical capability:** Confidence-gated evidence retrieval with structured-data
lookup tools instead of chunk-only RAG, over a real public corpus.

**Strongest differentiation:** Attacks the VERIFIED gap (distrust, novel faults, shallow indexes)
rather than re-building the commoditized chatbot; refusal-on-low-confidence is the shop-floor
safety property practitioner write-ups emphasize.

**Closest competitors:** Siemens Industrial Copilot, Caterpillar variants, GrayCyan Diagnostics
RAG, P.I.T.O., published lab recipes (COMPETITIVE-INTELLIGENCE.md C2).

**Evidence supporting differentiation:** r/BMET + r/HVAC first-person evidence; practitioner
reports that gains concentrate on routine failures. DIFFERENTIATION IS INCREMENTAL — judges may
still see "another RAG chatbot."

**Feasible implementation scope:** Python + vLLM on AMD; Qdrant/FAISS; public manual corpus
(NIST MEP SOP library, MachineMetrics open docs); structured lookup tables; web UI.

**Expected demo behavior:** In-scope faults answered with page-level citations; out-of-scope
queries refused; error-code lookup returning exact torque/sequence from a table.

**Risks:** adjacency to a commoditized space is the main risk; the corpus is synthetic-adjacent
(public manuals are not the gatekept ones users actually need); originality scored against
shipped vendor products.

---

## Candidate C — INTACT-ML: Multilingual discharge-instruction verification (Track 2 variant)

**Problem solved (from P3):** LLM simplification of discharge instructions fails dangerously;
verification is unsolved; multilingual patient populations are underserved.

**Proposed approach:** The Intact mechanism (fact ledger + deterministic preservation gates)
extended to multilingual rendering of discharge documents.

**Closest competitors:** Intact itself (Devpost, Aug 2026 — the exact mechanism on English
discharge docs), VeriFact (research, EHR-bound), CREOLA, llm-medical-guard, Discharge Guard.

**Assessment:** COMPROMISED on originality — a hackathon re-build of an existing hackathon
project's exact mechanism, one month after it was published. Listed because it was generated and
rejected; the mechanism lives on inside Candidate A where it is applied to an untouched document
class. Track 2's safety rules (no autonomous diagnosis; human review) would also need careful
demo handling.

---

## Rejected during solution generation

- Generic multi-domain "verification platform" (Intact's own roadmap item) — rejected: vague
  without domain grounding; A grounds the same mechanism where it is demonstrable.
- Demand forecasting for commerce — barred by official Track 3 rules.
- PA automation — invalidated by competitive scan (C1).
