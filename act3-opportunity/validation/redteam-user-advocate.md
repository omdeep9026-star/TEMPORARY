# Red Team — USER ADVOCATE assessment: Candidate A (LEDGER)

Date: 2026-10-09. Reviewer role: user advocate. Scope: independent of other validation/ files
(except the mandated context set: EVENT-CONSTRAINTS.md, PROBLEM-DB.md, CANDIDATES.md,
COMPETITIVE-INTELLIGENCE.md, research/). User-side evidence gathered fresh via web_search on
2026-10-09 (r/SafetyProfessionals, EHS/SCHC practitioner sources, OSHA guidance, liability
guides). Sources inline.

## Verdict: UNCERTAIN — leaning PREFERRED for a compliance-driven segment, REJECTED for the named median user

The underlying problem (P4) survives user-side attack as real, current, and user-documented.
The specific product's preference case splits by buyer segment and weakens at exactly two
points: payment and trust. The median safety officer/EHS manager described in CANDIDATES.md is
documented to NOT pay for bilingual safety support and to prefer free MT + a bilingual
coworker; a compliance-heavy minority (multi-language SDS portfolios, EU-exposed manufacturers,
large construction firms already paying for human re-verification) plausibly WOULD prefer
LEDGER — as an augmentation layer, not as a replacement for bilingual-expert review.

## What holds (evidence FOR preference)

1. **The pain is real and first-person.** r/SafetyProfessionals: a safety pro "translating
   everything to Spanish so that our non-english speaking employees are actually included
   (My Spanish is terrible...)" (u/Accomplished_Shoe962, Oct 2024); a laid-off 5-year safety
   professional proposing a bilingual safety business because "communication gets lost in
   translation—especially when it comes to orientations, safety talks, or incident
   investigations" (u/BluePeak6430, Apr 2025); an ASCC member: "In the field, I leaned on
   Google Translate with little success." (ascconline.org).
2. **The quantitative failure-rate evidence PROBLEM-DB flagged as thin exists in practitioner
   form.** SCHC/Arcadis poster (Society for Chemical Hazard Communication, 2023 annual meeting):
   tested DeepL, ChatGPT, Azure against a standard Spanish SDS — **20% of DeepL, 32% of
   ChatGPT, 35% of Azure translations did not match** the standard in meaning or synonym; all
   three had spelling errors; conclusion: "it is essential to have a native/fluent speaker
   conduct a review." GLTaC poster (Doug Strock): free MT cannot produce regulation-mandated
   H&P phrases; worst case is "a complete opposite meaning"; the SDS author "is left with the
   decision to accept the risk in return for the immediate cost and time savings." This is
   EHS professionals measuring the exact failure mode LEDGER's gates intercept.
3. **The verification wedge matches a documented manual workflow.** SCHC's test case is
   literally hand-comparing MT output against a reference SDS. TheAICommand (WHS practice,
   2026) prescribes an "instruction ledger" + translation manifest + change alarm (withdraw
   dependent translations when the English source changes) — architecturally the same idea
   LEDGER proposes, assigned to a professional translator. Experts already want this artifact;
   nobody mechanizes it.
4. **Regulatory stakes are real, rising, and actively enforced.** OSHA 2010 Training Standards
   Policy Statement: training must be "in a manner that employees can understand"; CSHOs are
   instructed to verify language of delivery during inspections; penalties up to $16,550
   (serious) / $165,514 (willful/repeat) per violation as of 2026 (wordly.ai, safetyfolio.com).
   LOTO specifically: 29 CFR 1910.147(c)(7)(i) requires "a language and vocabulary the
   employees can understand." EU Machinery Regulation 2023/1230: an inadequate translation of
   a safety warning is a product defect with direct manufacturer liability (adverbum.com).
   CLP 1272/2008 mandates exact official H/P-code wording per EU language (kobaltlanguages.com).

## What does not hold (evidence AGAINST preference)

1. **Trust: no source supports AI verification replacing bilingual-expert review — several
   forbid it.** AD VERBUM: "The most ironclad defense available to a manufacturer in a
   documentation dispute is a certified human reviewer who can testify, on the record... MT
   cannot provide that. A light post-edit by a non-specialist cannot provide that." Courts in
   Germany/France accept certified translator declarations as due-diligence evidence; "no
   equivalent exists for MT output." WorkSafe Victoria's compliance code says machine-automated
   translation tools "cannot be guaranteed to be accurate and should not be used to translate
   OHS information" — in Victoria, worker-facing AI translation is effectively barred
   (theaicommand.com). An EHS manager would accept LEDGER as triage + documentation BEFORE a
   human sign-off, not as the guarantee itself. The product's "flagged, not published" framing
   is compatible with augmentation, but a demo that reads as automating the review step
   triggers the liability objection.
2. **Payment: the median named user is documented not to pay.** r/SafetyProfessionals
   (Apr 2025), on a bilingual safety consultant's offer: "Employers tend to be cheap when it
   comes to safety and will simply ask the bilingual employee to translate for them in a lot of
   cases" (u/KTX77625); "getting people to pay for it is hard especially with AI translators
   that are getting better and better... we hired a bilingual consultant/trainer and barely get
   [work]" (u/MWC13233, small safety consulting/training company). Most damaging: a
   manufacturing EHS user (u/FilibusterFerret) reports the company's AI document translation
   "was pretty clunky and I had to work with bilingual co-workers to clean up everything. But
   the last five or six months the tech has improved so much that I haven't needed to make any
   changes" — MT quality improvement is actively eroding even the review need for
   lower-stakes documents.
3. **Workers will not use the verification report.** Workers are the wrong audience for a
   per-fact traceability view. Worker-side evidence (CPWR study via HSI) says Spanish-speaking
   workers wanted "Spanish-language videos, graphics and other supporting materials" and live
   Q&A — not plainer text, not provenance UIs. Low-literacy workers "may have difficulty
   understanding more complex or technical topics, even with proper translation." The report's
   real audiences are the EHS manager, compliance/legal, and (in a dispute) auditors — a buyer
   feature, not a worker feature. This is fine for the pitch but the "secondary beneficiaries:
   the workers themselves" framing should not claim workers engage with the report.
4. **Reading level control: real but secondary.** It maps to explicit regulatory text —
   OSHA 1910.1030(g)(2)(ii) requires training "at an educational level and in a language
   understood by the employee," and OSHA interpretation treats vocabulary and literacy as
   counting separately from language (safetyregulatory.com). BUT for the lowest-literacy band,
   OSHA/NIOSH guidance prescribes pictograms, demonstrations, return-demonstration, and verbal
   instruction OVER written materials — "Handing someone a Spanish-language safety data sheet
   doesn't satisfy the training requirement" (safetyfolio.com). Plain-language TEXT rendering
   addresses the middle band (can read, but jargon-dense English source) only; the delivery-mode
   need workers actually voice (video/audio/live Q&A) is out of scope for Candidate A as
   specified.

## Rejection triggers (what would kill adoption)

1. **Ledger recall carried at Intact's 83.6%.** A 1-in-6 extraction miss rate contradicts
   "provably preserved" and would destroy trust the first time a missed fact is demonstrated.
   For the verification claim to be credible to this audience the demo must scope the corpus to
   structured procedure documents and report recall honestly.
2. **No human accountability layer.** An EHS manager signing an AI-verified translation has a
   weaker legal defense than signing a bilingual expert's review. "Ambiguous accountability:
   when an AI system fails and causes an accident, determining accountability is complex"
   (dangrinnell.substack.com, EHS AI risk management). LEDGER should position the gate output
   as input to a recorded human sign-off, not as the release decision.
3. **Jurisdictional bar.** WorkSafe Victoria's "keep AI out of the worker-facing OHS
   translation lane" position is a live regulatory precedent; expansion of such rules would
   reclassify the core mechanism as non-compliant in affected jurisdictions.
4. **Being mentally filed as "a translation tool."** Instant comparison to DeepL (free) loses.
   The wedge must be presented as compliance/audit infrastructure — the deterministic check +
   traceability record that generic MT and human-review workflows both lack.
5. **AI-skill gap of the user base.** 75% of EHS practitioners self-rate novice/beginner with
   AI tools (25% no AI skills at all; dangrinnell citing 2025 surveys); 66% of users rely on AI
   outputs without verification and 72% put less effort into tasks when using AI (interpro).
   Automation bias is a named risk in EHS practice — which cuts both ways: a deterministic gate
   is exactly the defense-in-depth EHS guidance (NIST AI RMF, HITL) calls for, but the UI must
   not invite rubber-stamping.

## Willingness-to-pay evidence (summary)

- **Negative for the median SME user:** r/SafetyProfessionals Apr 2025 thread — "Employers tend
  to be cheap when it comes to safety" (u/KTX77625); a small safety consulting firm hired a
  bilingual trainer and "barely get" business; AI translators "getting better and better" cited
  as the reason payment is hard (u/MWC13233); manufacturing user stopped reviewing AI
  translations after 5–6 months of quality gains (u/FilibusterFerret). Generic MT is near-free;
  professional translation runs $0.10–$0.40/word and interpreters $75–$200/hr — LEDGER sits
  between a barely-free option and the human option the buyer already avoids paying for.
- **Positive for compliance-driven segments:** OSHA per-violation penalties ($16,550/$165,514,
  2026) with active enforcement of the comprehension standard; EU Machinery Regulation
  2023/1230 making a mistranslated LOTO a product defect (adverbum.com); Korea's Lotte E&C /
  Daewoo E&C already pay for human re-verification at 40 minutes per briefing across 15
  languages (Korea Herald, via PROBLEM-DB); Kobalt Languages: "The cost of a single SDS error
  can exceed the cost of professional translation for an entire product portfolio"; hybrid
  AI+human SDS workflows cut cost/turnaround 40–60% while keeping compliance on regulated
  sections (kobaltlanguages.com) — the paid pattern is AI-draft + human-verify, which is
  exactly where LEDGER's gates slot in as the pre-review check and audit record.
- **Adoption context:** 82% of surveyed EHS/ops/risk professionals report some AI use in EHS
  programs (Wolters Kluwer "Safety Shift 2026," n=1,053) — buyers exist and are AI-active; but
  trust and governance are the emphasized conditions, and 75% self-rate AI novices/beginners.

## Recommendation to the selection panel

Proceed with Candidate A ONLY if reframed as **verification-and-audit infrastructure layered
into the existing AI+human workflow** (AI draft → deterministic preservation gates → recorded
human sign-off), with the buyer persona named as the compliance-driven EHS/documentation
manager at a multi-language manufacturer or EU-exposed equipment maker — not the SME safety
officer, who is documented not to pay. The demo must (a) show the gates catching corruptions a
single-prompt pass silently makes (the SCHC 20–35% mismatch rates give this demo a real number),
(b) report extraction recall honestly, and (c) never present the gate output as replacing human
accountability. As currently written in CANDIDATES.md ("Documents that cannot be verified
safely are flagged, not published" — a release-decision framing), the product would face the
liability and trust objections above from its own intended audience.
