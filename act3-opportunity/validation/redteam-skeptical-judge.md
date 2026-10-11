# Red Team — Skeptical Judge: Candidate A (LEDGER)

Date: 2026-10-09. Role: independent skeptical judge simulating a tired judge at AMD ACT III
demo day. Inputs read: EVENT-CONSTRAINTS.md (verified event facts), problem-db/PROBLEM-DB.md
(P4), opportunities/CANDIDATES.md (Candidate A), opportunities/DEMO-SPEC.md,
validation/COMPETITIVE-INTELLIGENCE.md (C4), plus judge-behavior research (lablab.ai's own
"How to Win an AI Hackathon" guide and independent hackathon-judge write-ups). No other
validation/ files read, per task constraints.

## Verdict

**STRONG — conditional on demo execution.** As a judge would actually apply the four criteria,
LEDGER lands in the 7–8/10 band on every criterion with headroom on Application of Technology
and Originality, and it survives the panel-reconvene test ("which one was that again?") with a
repeatable one-liner: "the one that catches the 480-volt decimal shift before your workers read
it." But three of its strengths are load-bearing demo moments that fail visibly if executed
carelessly: the baseline-corruption pivot, the stakes-first framing, and the AMD visibility.
The candidate is strong; the demo as specced has four identifiable ways to lose the room.

## Where the demo loses the room

1. **The pivot depends on stochastic behavior — or looks scripted.** The demo's emotional core
   is the baseline silently corrupting 480 V → 48 V. But the spec's phrase "a seeded corruption
   case is included in the corpus" is ambiguous between (a) a genuine captured baseline failure
   and (b) a pre-scripted corruption. A good model with a "keep it accurate" prompt often does
   NOT shift decimals on any given run. If the live baseline happens to behave and the team
   falls back to the seeded case, a judge who asks "did the model actually do that, or did you
   script it?" — one of the three questions judges reliably ask ("what was real versus mocked")
   — gets a fuzzy answer, and credibility is gone. The pivot must be a genuine, pre-captured
   baseline output with declared provenance, never a seeded/faked artifact.

2. **Eight stages in six minutes guarantees something is rushed.** Upload, ledger extraction,
   two-language generation, gates, verification report, baseline comparison, adversarial
   harness, traceability view. The most cuttable: the traceability view (fold into the
   verification report — it is the same table wearing a different title) and the second
   language. A demo that tries to show everything shows nothing twice.

3. **Table-heavy, text-dense UI reads like a compliance dashboard.** Fact-ledger table,
   per-sentence report, 9-row harness matrix — a judge at demo #30 glazes at tables. The
   harness must compress to one line ("9 corruption types injected, all intercepted, 0 dangerous
   failures") plus ONE dramatized example already shown in the side-by-side. The ledger table
   should highlight 4–5 rows (the voltage, the negation, the citation), not scroll.

4. **Dead air during live generation.** A 2-page document × two languages on a 70B-class model
   is the slowest stage. The AMD telemetry (model, GPU, tokens/sec) is the right thing to show
   during generation — it doubles as the AMD-requirement moment — but the narration during that
   window must carry the architecture story ("the model sees only the ledger; we removed the
   material it could hallucinate from"), not a tour of a progress bar.

## What a tired judge misunderstands

- **"It's DeepL with extra steps" / "a document linter"** — if the opening 30 seconds lead with
  the product name. "Preservation-verified multilingual safety-document workbench" is
  jargon-dense; a tired judge parses neither "preservation-verified" nor "workbench" in 30
  seconds. The opening must lead with the worker-safety stakes: "your workers are reading the
  translation nobody checked."
- **"So the gates catch everything"** — overclaiming invites the extraction-recall probe
  (see residual risks). Say the scoping and the measured recall out loud before a judge asks.
- **"So it's just regex on translations?"** — underselling. The innovation is the architecture
  (rewriter never sees the source), not the checks; if the gates are described before the
  ledger constraint, the judge misses the actual mechanism.
- **"Fake corruption"** — the scripted-looking-baseline risk above.
- **"Isn't this the medical one?"** — the mechanism's lineage is a medical-discharge project;
  if Intact is mentioned early, the judge may mis-map it to Track 2 with its safety-rules
  baggage. The industrial framing must come first.
- **"Multilingual workforce" stays abstract** — without one concrete number (% of manufacturing
  workforce foreign-born; Korea's 15 designated languages; 40 minutes of human re-reading per
  briefing), "multilingual workers" is a category, not a user.

## Is "translation verification" compelling, or a linting tool?

Honest answer: **as described, it sounds like a linting tool; as demonstrated, it is the most
visceral moment available in this lane.** Nobody's pulse rises at "we verify translations." But
"here is what your Spanish-speaking line worker would have read — 48 volts instead of 480,
'when convenient' instead of 'immediately' — and here is the verified version" is a genuine
aha moment: concrete, dangerous, and instantly understandable across technical backgrounds.
The demo plan correctly leads with verification and positions DeepL as "the tool whose output
nobody checks." The linting perception is a framing risk carried entirely by the first 30
seconds, not a design flaw. Demo > description — which is exactly why this candidate belongs in
a live demo rather than a slide deck.

## Scoring as a judge would apply the criteria (no published weights; parity assumed)

**Application of Technology: 8.5/10.** The AI is meaningfully integrated, not a wrapper:
ledger-constrained generation is an architectural constraint, and the model performs the hard
generative task (multilingual rendering at controlled reading level). AMD hosts the core
generative workload with live endpoint telemetry — this satisfies "the AMD component must be
part of the working product shown to judges" and is visible at the exact moment generation
happens. Docking: one model, and "the model sees only the ledger" must be narrated in one clear
sentence or a judge scoring "how effectively the models are integrated" misreads it as
underuse. The deterministic gates are good engineering but are not model calls — do not let
them dominate the technology story.

**Presentation: 7.5/10.** Strong bones: one continuous flow, a side-by-side pivot, an explicit
live-vs-recorded honesty table, offline-capable fallbacks. Risks: eight stages in six minutes,
table-heavy UI, jargon-dense title, and a reading-level claim that is unverifiable on screen.
With rehearsal discipline (stakes first, decimal-shift beat as the remembered moment, harness
compressed), this reaches 8–8.5. As specced without that discipline: 6.5–7.

**Business Value: 7.5/10.** A named, specific user (EHS manager at a multilingual manufacturer),
a real regulatory stake (OSHA "in a manner employees can understand"; EU Machinery Regulation),
and a documented, expensive human-review bottleneck. The Korea Herald figure is a ready-made
cost anchor — human verification ≈ 40 minutes per briefing; LEDGER ≈ seconds — and it is in the
material but absent from the demo plan. Weaknesses: no TAM figure, no revenue model, no
measurable incident rate; judges applying the rubric ask "who pays?" and "EHS managers" is a
user, not a buyer case. One pitch line (per-worker/per-document pricing vs 40-minute human
review) moves this to 8.

**Originality: 8/10.** No direct competitor found for deterministic preservation verification of
translated safety documents (C4, absence labeled as absence); the application to this document
class is genuinely novel; the zero-API-key reproducible corruption harness is a fresh demo
behavior that directly answers "ability to demonstrate behaviors." Vulnerability: the Intact
lineage — identical mechanism (fact ledger + pint gates + corruption harness, published one
month prior). Discovery probability among judges is low, but citing Intact early in the pitch
hands a judge the "Intact for factories" frame. Cite it in the repo/README (honesty, and it
pre-empts discovery); in the pitch, say plainly what is new: multilingual rendering, industrial
safety domain, regulatory framing.

Weighted at parity: ≈ 7.9/10 — the 7–8 band on lablab-style scales = strong, top-quartile
plausible, winner possible if the execution conditions are met and no competing team lands a
comparable safety-verification story.

## Conditions attached to the verdict (pre-demo fixes, all cheap)

1. Pre-capture genuine baseline failures on the actual corpus; declare their provenance on
   screen. Never present a seeded corruption as model output.
2. Lead the spoken pitch with the worker-safety stakes; retire the jargon title from speech.
   One-line identity: "the one that catches the decimal shift before your workers read it."
3. One language live (Spanish); Vietnamese only as a second pass if time permits.
4. Compute and display a readability metric for the output live — or drop the reading-level
   claim. Unsupported claims invite probing.
5. Compress the harness to one line plus the already-shown example.
6. Add the cost anchor (seconds vs 40-minute human review) and one revenue-model line.

## Residual risks that cannot be fixed by demo craft

- **The ledger-recall hole:** a fact the extractor misses is silently absent from the ledger,
  the rewrite omits it, and the gates PASS it — the safety guarantee is only as strong as
  extraction recall (Intact self-reported 83.6%). "Flagged in the report" is impossible for
  never-extracted facts. Mitigation is honest scoping: restrict the corpus to structured LOTO
  procedures where extraction is near-deterministic, measure and state recall, and never claim
  general coverage.
- **Intact lineage:** permanent, low-probability originality exposure; handled by honest citing
  and a crisp delta statement.
- **Thin demand quantification:** OSHA position + Korea deployments + EU regulation are
  qualitative; no measurable mistranslation-incident rate was found. The demo's baseline
  comparison substitutes for incident data, but a business judge wanting market evidence gets
  a cost-avoidance argument, not a market-size one.
- **AMD endpoint availability during the event:** vLLM/ROCm setup friction in a 4–5 effective
  build day is real (the planned spike is the right mitigation). If the endpoint is down at
  demo time, the recorded fallback must keep the AMD story visible and labeled as recorded —
  an AMD-less live demo silently forfeits the event's central requirement.
