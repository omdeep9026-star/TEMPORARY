# Red Team — Technical Investigation: Candidate A "LEDGER"

Date: 2026-10-09. Investigator: technical red-team subagent (independent). Method: every
load-bearing claim below was verified by direct web retrieval from official sources (AMD
documentation, Meta model cards, vLLM recipes/docs) or read from the discovery workspace
(EVENT-CONSTRAINTS.md, opportunities/CANDIDATES.md, opportunities/DEMO-SPEC.md,
COMPETITIVE-INTELLIGENCE.md). Sources listed inline.

**Verdict: FEASIBLE_WITH_RISK** — build days estimate ≈ 4.5 of the 4–5 effective days available.
Demonstration route: credible. The stack is verified end-to-end and the deterministic bulk of the
architecture is ordinary Python, but the Llama 3.3 Vietnamese gap, ledger-recall precedent, and
non-English gate soundness are real, named risks with required mitigations — not blockers.

---

## 1. What was verified (independent checks)

### 1.1 AMD Developer Cloud can host the rewriter — VERIFIED

- Official AMD Developer Cloud page: AMD Instinct MI300X access in two configurations —
  **1× GPU (192 GB GPU memory, 20 vCPUs, 240 GB RAM, 720 GB boot + 5 TB scratch NVMe)** and
  8× GPU (1,536 GB) — with a browser Jupyter container on VM launch.
  https://www.amd.com/en/developer/resources/cloud-access/amd-developer-cloud.html
- Access options: pay-as-you-go (Digital Ocean, Vultr) or complimentary credits for AMD AI
  Developer Program members ($100 in credits; the general cloud-access page also describes ~25
  complimentary credit-hour grants "in AMD's sole discretion"). Key terms: **complimentary
  credit applies only to MI300X use; credits expire ten (10) days from deposit; a powered-off
  instance is still billed until destroyed.**
  https://www.amd.com/en/developer/resources/cloud-access.html
- MI325X is also reachable via Vultr (announced Feb 2025, first cloud provider) and the AMD
  Instinct Evaluation Program — a paid/secondary fallback path.
  https://www.businesswire.com/news/home/20250218448181/en/
- Capacity check: a 70B model in BF16 (~140 GB weights) fits on a single MI300X (192 GB) with a
  usable KV cache; AMD also publishes an MXFP4-quantized Llama-3.3-70B (TP=1) for exactly this
  single-GPU case. The small 1×-GPU ADC configuration suffices for the rewriter; no 8× node needed.

### 1.2 vLLM on ROCm is first-class for both candidate models — VERIFIED

- AMD's own ROCm blog: "vLLM V1 Meets AMD Instinct GPUs" **features Llama 3.3-70B on MI300X**
  specifically. https://rocm.blogs.amd.com/software-tools-optimization/vllmv1-rocm-llm/README.html
- ROCm documentation (v7.1.0) has a dedicated vLLM V1 optimization page for MI300X/MI325X/MI350X/
  MI355X, with working examples including `vllm serve meta-llama/Llama-3.3-70B-Instruct`, AMD
  Quark-quantized variants (`amd/Llama-3.3-70B-Instruct-MXFP4-Preview`, TP=1; FP8-KV), on-the-fly
  FP8/PTPC-FP8, and the `VLLM_ROCM_USE_AITER=1` backend switch.
  https://rocm.docs.amd.com/en/docs-7.1.0/how-to/rocm-for-ai/inference-optimization/vllm-optimization.html
- vLLM project recipes verify Qwen2.5-VL-72B/7B on **4× MI300X/MI325X/MI355X** with BF16,
  including the exact serve commands; the recipes note the ROCm wheel requires **Python 3.12,
  ROCm 7.0, glibc ≥ 2.35 — otherwise use the Docker flow**.
  https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen2.5-VL.html
- Independent performance evaluations of Llama 3.3 70B under vLLM on MI300X exist (Moreh
  technical report, ROCm 6.8.5) and the vLLM MI300X best-practices guide (Oct 2024) documents
  serving patterns (TP sizing, `--num-scheduler-steps`, CK Flash Attention).
  https://moreh.io/technical-report/moreh-vllm-performance-evaluation-llama-3-3-70b-on-amd-instinct-mi300x-gpus-250830/
  https://vllm.ai/blog/2024-10-23-vllm-serving-amd

### 1.3 Multilingual capability of the rewriter candidates — VERIFIED, with a material finding

- **Llama 3.3 70B (official Meta model card): supported languages = English, German, French,
  Italian, Portuguese, Hindi, Spanish, and Thai. VIETNAMESE IS NOT SUPPORTED.** Meta states it
  "strongly discourage[s] developers from using this model to converse in non-supported languages
  without implementing finetuning and system controls." For a safety-critical document tool this
  is not a cosmetic caveat.
  https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/MODEL_CARD.md
  (mirrored on NVIDIA NIM and Hugging Face model cards)
- **Qwen2.5-72B-Instruct (official model card): multilingual support for over 29 languages,
  including Spanish AND Vietnamese.** Qwen2.5-72B posts Multi-Translation 39.0 vs Llama-3-70B
  38.0; the Qwen2 technical report reports dedicated Vietnamese evaluation scores.
  https://www.modelscope.cn/models/qwen/Qwen2.5-72B-Instruct
  https://qwenlm.github.io/blog/qwen2.5-llm/ ; https://arxiv.org/html/2407.10671v1
- Consequence: **the architecture should name Qwen 2.5 72B as the primary rewriter** (it covers
  both demo languages), with Llama 3.3 70B as a Spanish-only variant or A/B comparison. A
  Vietnamese demo on Llama 3.3 would contradict Meta's own usage guidance — a judge-visible
  liability for a safety product.

### 1.4 Event-requirement fit — VERIFIED against workspace constraint file

- EVENT-CONSTRAINTS.md (verified against official event pages): "the AMD component must be part
  of the working product shown to the judges" — the LEDGER demo shows the AMD-hosted rewriter
  rendering live with endpoint status (model, GPU, tokens/sec); that satisfies the requirement
  *if* the endpoint is live during the demo (see risk 5).
- The build phase is Oct 12–18 with ~4–5 effective days after setup (EVENT-CONSTRAINTS.md); the
  estimate in §3 fits inside that window.
- The demo's verification numbers must be reproduced on the project's own corpus (DEMO-SPEC.md
  correctly says the borrowed Intact numbers are shown as mechanism evidence, not results).

### 1.5 Architecture internal consistency — assessed from CANDIDATES.md / DEMO-SPEC.md

The six components (ledger extraction; ledger-only rewriter; two deterministic gates; fallback
chain; 9-type corruption harness; web UI) are mutually consistent and the fallback direction
("degrade toward less fluent, never less accurate") is correctly specified. Two design-level
observations:
- The gates are **only** sound for facts that reach the ledger: extraction recall is the ceiling
  on every downstream guarantee (Intact self-reported 83.6% recall — COMPETITIVE-INTELLIGENCE.md
  C3). The architecture handles this honestly (flag + corpus scoping), which is the right call,
  but it must be demo-visible.
- The ADDITIONS gate ("claims not traceable to ledger facts are stripped") needs a
  sentence→fact traceability representation from extraction onward; it cannot be bolted on after
  the rewriter exists. This is a sequencing constraint for the build plan, not a feasibility
  problem.

---

## 2. Key technical risks (ranked)

1. **Vietnamese output from Llama 3.3 70B is unsupported by Meta's own model card.** The demo
   spec promises Spanish *and* Vietnamese. Using Llama for Vietnamese contradicts Meta's usage
   guidance for a safety-critical tool. Mitigation (required): primary rewriter = Qwen 2.5 72B
   (29+ languages incl. both); keep Llama 3.3 70B as Spanish variant/ablation; run a day-1 spike
   comparing Vietnamese output quality side-by-side before locking the model choice.
2. **Ledger recall is the weak link and gates cannot see past it** (precedent: Intact 83.6%
   self-reported). A missed quantity or negation is silently absent from every downstream check —
   the one corruption class the architecture is structurally blind to. Mitigation: scope the
   corpus to structured procedure documents (numbered LOTO steps, sheets); measure and publish
   recall on the project corpus; make the extraction-miss flagging path part of the demo.
3. **Gate soundness in Spanish/Vietnamese is hand-written, language-specific code.** Unit-aware
   magnitude comparison and negation/urgency/softening-phrase detection need per-language
   lexicons/regexes; Vietnamese adds diacritics and syllable segmentation. A lexicon gap produces
   either a false "VERIFIED" (dangerous false negative — worse than a failure) or constant false
   failures. Mitigation: the 9-corruption-type harness must be extended to inject corruptions
   *in the target languages* and report per-type interception; treat gate test coverage as a
   deliverable, not an afterthought.
4. **AMD Developer Cloud access logistics.** Complimentary hours require AMD AI Developer
   Program approval; credits expire ~10 days from deposit and cover MI300X only; powered-off
   instances still bill until destroyed. If approval/credits don't land early in the build
   window, the fallback is pay-as-you-go MI300X/MI325X (Digital Ocean, Vultr) on a card.
   Mitigation: request access day 0; pull model weights immediately; destroy instances after use.
5. **ROCm environment setup cost.** The vLLM ROCm wheel wants Python 3.12 + ROCm 7.0 +
   glibc ≥ 2.35 → Docker flow is the realistic path; MI300X serving benefits from AMD-specific
   flags (`VLLM_ROCM_USE_AITER=1`, scheduler steps). Budget ~0.5–1 day on day 1 and pre-pull
   weights (~140 GB); not a blocker but it consumes the schedule's slack.
6. **Demo live-dependence on the AMD endpoint.** Translation is the only network stage; the
   gates and harness run fully offline with zero API keys (a genuine strength for the
   verifiability moment). DEMO-SPEC.md already specifies recorded-artifact fallback labeled as
   recorded. Residual risk is moderate and mitigated by design.
7. **Corpus legality (minor).** Public OSHA/NIOSH-style LOTO procedures and toolbox talks: US
   federal government works are generally public domain; verify per-document licenses when
   assembling the corpus. Minor effort.

## 3. Implementation complexity and build-day estimate (≈ 4.5 days)

| Component | Complexity | Estimate |
|---|---|---|
| AMD access + vLLM ROCm Docker + weights pulled (parallel, day 1) | Medium (one-time setup) | 0.5–1.0 d |
| Fact-ledger extraction (pint quantities, machine names, negations, urgency, citations) | Medium-high (hardest local part: negation + citation patterns) | 1.0–1.5 d |
| PRESERVATION + ADDITIONS gates with per-sentence traceability | Medium (language-pair lexicons; test coverage critical) | 1.0 d |
| Adversarial corruption harness, 9 types, incl. target-language injections | Low-medium | 0.5 d |
| Fallback chain (stricter rewrite → template rendering) | Low | 0.5 d |
| Web UI (upload / language / level / report) | Low | 0.5–1.0 d |
| Corpus assembly + demo rehearsal + own-corpus numbers | Low | 0.5 d |

The workload is dominated by deterministic local Python (zero-API-call by design), which
de-risks the schedule; the only GPU dependency is the rewriter endpoint. Total ≈ 4.5 effective
days against 4–5 available — feasible with the day-1 AMD setup running in parallel with local
work. Serving is proven on 1× MI300X (BF16 or MXFP4/FP8 variants), so the small ADC
configuration suffices.

## 4. Demonstration route — credibility assessment

**Credible.** The demo (DEMO-SPEC.md) satisfies the event's verified requirement ("AMD
technology should power a meaningful part of it", shown to judges): the AMD-hosted rewriter is
the translation engine itself, not a garnish, and the demo displays endpoint status during
generation. The verifiability moment (offline 9-type corruption harness with zero API keys) is
runnable live regardless of venue network conditions — a robust property for an on-site demo in
Italy. The baseline comparison (single-prompt + DeepL silently corrupting, gates intercepting)
is mechanically honest and reproducible. Required adjustments from this investigation: (a) the
Vietnamese rendering must come from Qwen 2.5 72B, not Llama 3.3; (b) the extraction-miss
flagging path and honest recall number should appear in the demo, since ledger recall is the
one structural blind spot; (c) reproduce preservation/interception numbers on the project's own
corpus before final selection, per DEMO-SPEC.md's own rule.

## 5. Verdict

**FEASIBLE_WITH_RISK.** Nothing found invalidates the architecture: the serving stack is
verified end-to-end on official sources (AMD Developer Cloud MI300X; vLLM-on-ROCm featuring
Llama 3.3 70B; Qwen2.5 verified on MI300X-class GPUs), the deterministic components are
well-scoped Python, and the demo route meets the AMD-visibility requirement with offline
fallbacks. The risks are specific and mitigable: model choice must shift to Qwen 2.5 72B for
the Spanish+Vietnamese demo (Llama 3.3's Vietnamese gap is documented by Meta itself), ledger
recall must be measured and shown honestly, gate soundness in target languages needs
adversarial test coverage, and AMD cloud credits/approval plus ROCm Docker setup must be
secured on day 1. Estimate ≈ 4.5 effective build days.
