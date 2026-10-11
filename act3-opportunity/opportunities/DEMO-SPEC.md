# Demonstration Specification — Candidate A (LEDGER)

Date: 2026-10-09. Pre-red-team specification; revised after red-team feedback where noted.

## Scenario (6 minutes, one continuous flow)

**Initial user input:** An EHS manager opens the web UI and uploads a real English lockout/tagout
procedure (public OSHA 1910.147-style document, ~2 pages, containing quantities, machine names,
negations, urgency phrases, and regulatory citations). Selects target languages: Spanish,
Vietnamese. Selects reading level: grade 6.

**Processing and intermediate actions (shown live, each on screen):**
1. **Fact-ledger extraction** — the document is parsed into a visible fact ledger: every quantity
   with its unit (6 ft, 480 V, 30 days), machine/part names, negation statements ("do NOT
   operate"), urgency/timeframe phrases ("immediately", "before each shift"), and regulatory
   citations (29 CFR 1910.147). The ledger is displayed as a table so judges see the extracted
   facts the rewriter will be allowed to use.
2. **Ledger-constrained translation** — the rewriter (open model served via vLLM on AMD Developer
   Cloud) renders the Spanish and Vietnamese versions from the ledger ONLY. The AMD endpoint
   status (model name, GPU, tokens/sec) is displayed during generation — this is the "AMD powers
   a meaningful part of the product" moment.
3. **Deterministic verification gates** — for each language, the preservation gate (unit-aware
   magnitude comparison, strict name matching, citation survival, urgency retention with
   softening-phrase detection) and the additions gate (untraceable claims stripped) run in
   milliseconds. The verification report is displayed per sentence: each output line traced to
   its source fact, with any stripped additions shown.

**Baseline comparison (the pivot of the demo):** The same document is sent to a single-prompt
baseline — the same open model given a plain "translate this and keep it accurate" prompt, and
separately to DeepL. A seeded corruption case is included in the corpus: the baseline output
silently shifts a decimal (480 V → 48 V), softens an urgency phrase ("immediately" → "when
convenient"), or drops a negation. The judges see the corrupted rendering side-by-side with the
verified rendering, and the verification report marking exactly what the baseline changed.

**Adversarial harness (verifiability moment):** Run live with zero API calls: the corruption
harness injects 9 corruption types (decimal shifts, unit swaps, altered frequencies, shortened
durations, dropped medications/steps, dropped warnings, softened urgency, invented advice,
negation flips) across the corpus and reproduces the interception numbers (target: 100%
dangerous-corruption interception, matching the architecture's design).

**Final artifact:** The verified multilingual rendering (per language) + verification report with
per-fact traceability + the harness results. The patient/worker-facing page shows the plain-language
document; the EHS-facing page shows the proof.

**How the result is verified:** Deterministic gates are code, not model calls — anyone can clone
the repo with no API key and reproduce every safety number. The harness is the reproduction
mechanism; the demo runs it live.

**Expected improvement vs baseline:** single-prompt baselines measurably corrupt safety-critical
content (Intact measured 93.4% preservation vs 100% for the gated workflow, 17 invented claims vs
0, 5 dangerous failures vs 0 across 3 documents). This project's own numbers must be reproduced
on its own corpus before final selection; the demo shows the mechanism, not the borrowed numbers.

**Failure cases and recovery behavior:**
- Extraction miss (fact absent from ledger): the system cannot verify downstream — flagged in the
  report; the demo states ledger recall honestly and shows the corpus scoping that limits it.
- Gate failure on a legitimate rewrite: one stricter rewrite, then template rendering of the
  ledger — output degrades toward less fluent, never toward less accurate. The demo can trigger
  this deliberately (a deliberately ambiguous ledger) to show the fallback.
- Live model endpoint down: the demo falls back to a pre-rendered verified artifact + recorded
  harness run (clearly labeled as recorded, never presented as live).
- Network failure: the harness and gates run fully offline; the translation step is the only
  network-dependent stage.

## Genuine live vs mock/simulated (separated explicitly)

| Stage | Status |
|---|---|
| Fact-ledger extraction | LIVE (deterministic, local) |
| Ledger-constrained translation | LIVE (open model via vLLM on AMD Developer Cloud) |
| Deterministic gates + verification report | LIVE (deterministic, local, zero API calls) |
| Baseline (single-prompt, DeepL) | LIVE where network permits; recorded fallback |
| Adversarial corruption harness | LIVE (deterministic, local, zero API calls) |
| Pre-rendered fallback artifacts | RECORDED (labeled as such, used only on live-endpoint failure) |

Never presented as real: no EHR integration, no payer integration, no production CMMS/MES hooks.
The demo operates on public documents and states this.
