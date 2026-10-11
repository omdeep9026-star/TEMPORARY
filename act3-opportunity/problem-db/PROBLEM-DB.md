# Problem Intelligence Database

Date: 2026-10-09. Storage: structured markdown (simplest reliable mechanism in this environment;
SQLite unnecessary at this scale). Maintained across research rounds — subsequent investigations
build on these records. Sources are preserved per observation; duplicates merged with sources
retained. Record types are separated: FACT (observed), INTERPRETATION (inferred), HYPOTHESIS
(untested), SOLUTION (proposed, not validated).

Legend: CONF = confidence (HIGH/MED/LOW). Every claim carries its source URL or file reference.

---

## P1 — Factory/field technicians cannot find the answer inside equipment documentation

- **ID:** P1
- **Type:** FACT (pain observed directly, multiple independent users)
- **Problem description:** Technicians troubleshooting faults lose hours to (a) finding the right
  manual/wiring diagram/error-code index, then (b) digging through it for the one answer. Manuals
  are gatekept, unindexed, revision-ambiguous, or absent.
- **Target user:** Clinical engineering (biomed) technicians, diesel/HVAC/field technicians,
  plant maintenance staff at SMEs.
- **Context and trigger:** Equipment fault during operation; urgent repair; unfamiliar machine.
- **Current workflow:** Google → vendor portals → OneSourceDocs/CMMS subscriptions → personal PDF
  libraries → OneNote tags → ask colleagues → manufacturer phone call → trial-and-error.
- **Documented pain points:** "spending hours trying to find that one document, sometimes even
  days"; "hours digging through it just to find one answer"; troubleshooting programs gatekept to
  manager tablets; error indexes "3 abstraction layers too shallow"; intermittent faults lack a
  firm-diagnosis information path.
- **Supporting evidence:**
  - https://www.reddit.com/r/BMET/comments/1spuxgh/ (clinical engineering, multiple users)
  - https://reddit.com/r/DieselTechs/comments/1kfpdt1/
  - https://www.reddit.com/r/HVAC/comments/1dapuaq/
  - Scholarly: wave1-raw (Reducing Technician Search Burden; RAFT; TSG Suggester)
- **Independent corroboration:** Practitioner reports (vendor-claimed 15–30% MTTR reduction
  concentrated on routine failures; novel faults still dominated by human experience).
- **Existing solutions and workarounds:** OneSourceDocs, CMMS attachments, ManualsLib, Siemens
  Industrial Copilot and Caterpillar variants (major OEMs), ChatGPT/Claude ad-hoc use, tribal
  knowledge.
- **Known limitations of those solutions:** vendor copilots cover major equipment classes only;
  gains concentrate on routine failures; users distrust unverified LLM answers ("chat would just
  hallucinate... I'll have to look for it myself"); subscriptions don't cover gatekept manuals.
- **Counterevidence:** some technicians report manual hunting is rare; aggregators reduce the
  find-the-document half; the in-manual "dig" may be smaller than the document-finding half.
- **CONF:** HIGH that the pain is real; MED on which slice is biggest.
- **Remaining uncertainties:** slice size (finding vs digging); SME budgets; equipment-class
  coverage gaps.
- **Potential solution directions:** verification-grounded RAG over real corpora with refusal
  behavior; error-code structured lookup + troubleshooting; multimodal (photo → manual page).
- **Event fit:** Track 1 (Intelligent Industry). Official brief lists "help technicians search
  manuals and maintenance records" verbatim.

---

## P2 — Prior authorization paperwork consumes clinician time and delays care

- **ID:** P2
- **Type:** FACT (official professional-body survey, recurring annually)
- **Problem description:** US physicians complete 39–40 PAs/physician/week; 13 hours/week of
  physician+staff time; 89–94% report burnout contribution; 93–95% report care delays; 29%
  report serious adverse events.
- **Target user:** US physicians and practice staff; revenue-cycle teams.
- **Context and trigger:** Every prescription/order requiring payer approval.
- **Current workflow:** identify requirement → gather codes → clinical justification → submit via
  payer portal/fax/phone → follow up → appeal denials.
- **Documented pain points:** volume (40/week), time (13h), denials (31% often/always denied;
  74% say denials increased over 5 years), fax/portal fragmentation (CAQH: ~30% electronic).
- **Supporting evidence:**
  - https://www.ama-assn.org/system/files/prior-authorization-survey.pdf
  - https://www.ama-assn.org/practice-management/prior-authorization/fixing-prior-auth-nearly-40-prior-authorizations-week-way
  - https://www.ajmc.com/view/ama-survey-highlights-growing-burden-of-prior-authorization-on-physicians-patients
- **Independent corroboration:** CAQH report (via Innovaccer release); Becker's; physician survey
  on utilization management (AJMC).
- **Existing solutions:** Cohere Health, Voicecare AI, Innovaccer Flow Auth, LucasAI, HealOS,
  Optum InterQual Auth Accelerator, R1/Humata (see COMPETITIVE-INTELLIGENCE.md C1).
- **Known limitations of those solutions:** require EHR/payer integrations; enterprise sales
  cycles; none available to a hackathon team.
- **Counterevidence:** 61% of physicians worry AI increases denial rates; market saturated.
- **CONF:** HIGH that the problem is real; HIGH that the opportunity is invalidated.
- **Remaining uncertainties:** none material.
- **Potential solution directions:** (none viable for this event — rejected).
- **Event fit:** Track 2 nominally; REJECTED on competitive saturation + integration infeasibility.

---

## P3 — Patients don't understand discharge instructions; verification of simplified versions is unsolved

- **ID:** P3
- **Type:** FACT (peer-reviewed) + HYPOTHESIS (that a verification-first product is the right
  intervention — supported by Baker Institute and by Intact's results but not field-proven)
- **Problem description:** 63.8% of ED patients have no/poor understanding of return
  instructions; clear understanding → 30% fewer readmissions/ED visits. LLM simplification of
  instructions fails in dangerous ways (alters doses, drops warnings, invents reassurance);
  Baker Institute (July 2026): such tools "are not yet safe to deploy without further development."
- **Target user:** Hospital discharge staff; patients (secondary beneficiary); multilingual
  patient populations.
- **Context and trigger:** Discharge moment — patient tired, stressed, often reading a second
  language.
- **Current workflow:** clinician writes instructions (English, jargon-dense) → print → verbal
  explanation (often skipped) → patient reads alone.
- **Documented pain points:** comprehension failures; readmission cost; no verification layer
  between LLM output and the patient.
- **Supporting evidence:**
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC5805670/ (63.8% figure)
  - https://www.nso.com/Learning/Artifacts/Articles/defensive-documentation-3 (30% figure)
  - https://www.bakerinstitute.org/research/closing-patient-comprehension-gap-through-policy-and-artificial-intelligence
  - https://arxiv.org/html/2501.16672v1 (VeriFact — fact-checking against EHR)
  - https://www.nature.com/articles/s41746-025-01670-7 (CREOLA — hallucination 1.47%/omission
    3.45%; negation hallucinations most dangerous, concentrated in Plan sections)
  - https://devpost.com/software/intact-9j3a4c (Intact — deterministic preservation gates:
    100% vs 93.4% single-prompt baseline; ledger recall 83.6% self-reported)
- **Independent corroboration:** JAMA Network Open patient-friendly-language study; Nature npj
  study; Intact's adversarial results are self-reported but mechanically reproducible.
- **Existing solutions:** JAMA-endorsed generation workflows; scnsoft personalization layer;
  DoximityGPT; Devpost projects (Discharge Guard, CareGuard); VeriFact (research, EHR-bound);
  llm-medical-guard (rule-based, educational); Intact (hackathon, English-only documents).
- **Known limitations of those solutions:** generation without verification; VeriFact needs an
  EHR; Intact covers English discharge docs only, single-developer hackathon scope, ledger
  recall 83.6%.
- **Counterevidence:** hospital IT procurement is slow; clinical validation cycles are long; a
  hackathon cannot run patient studies.
- **CONF:** HIGH on the problem; MED on the solution hypothesis; MED-LOW on hackathon
  demonstrability without live clinical data.
- **Remaining uncertainties:** whether judges weigh Track 2's safety rules as a barrier; data
  access for a credible demo (synthetic vs public discharge corpora exist — MIMIC-III/IV
  require credentialing; Intact used synthetic documents).
- **Potential solution directions:** verification-first rewriting with deterministic preservation
  gates + multilingual rendering; but see C3 — directly compromised by Intact on originality for
  the English-discharge version.
- **Event fit:** Track 2. COMPROMISED as a direct re-build; open as a domain-general mechanism
  applied to a different document class.

---

## P4 — Translated safety-critical documents are unverified; workers act on translations nobody checked

- **ID:** P4
- **Type:** FACT (demand) + HYPOTHESIS (that deterministic preservation verification is the
  missing layer)
- **Problem description:** Multilingual workforces receive safety instructions, lockout/tagout
  procedures, and compliance content translated by generic MT or ad-hoc AI. A mistranslated
  safety course "can fail [OSHA's] bar even though a translation technically exists." Korea's
  largest builders deployed AI translators but with human verification as the guarantee. No
  deterministic verification layer was found anywhere.
- **Target user:** Safety officers/EHS managers at manufacturers, construction firms with
  multilingual workforces; compliance teams (EU Machinery Regulation context).
- **Context and trigger:** Translating/updating safety procedures, toolbox talks, compliance
  training; hiring seasonal foreign workers.
- **Current workflow:** generic MT (DeepL/Google) → occasionally a bilingual expert reviews →
  distribute. Korea: RED-TEAM CORRECTION — the originally cited "40-minute human re-reading" was
  the PRE-AI burden that the deployed AI translator ELIMINATED (toolbox meetings now 10–20 min);
  the flagship deployments verify translations via in-workflow Korean subtitles, and Korea's
  majors (Lotte Innovate, Daewoo Smarty, GS E&C Xi Voice) SELF-BUILT their translators in-house.
- **Documented pain points:** no verification; human review is the expensive bottleneck; units
  and regulatory citations get mistranslated; OSHA requires training "in a manner employees can
  understand."
- **Supporting evidence:**
  - https://icantech.ai/insights/ai-translation-localization-multilingual-workforce-training
    (OSHA language requirement; AI+human as industry standard)
  - https://www.koreaherald.com/article/10772020 (Lotte E&C / Daewoo E&C deployments. RED-TEAM
    CORRECTION: the "40 minutes" was the pre-AI human translation burden that the AI translator
    ELIMINATED — not a persisting bottleneck; the deployments verify via in-workflow Korean
    subtitles and the majors self-built their translators in-house)
  - RED-TEAM ADDED: https://devpost.com/software/doseguard (DoseGuard — deterministic
    verification of translated medication instructions, numeric normalization + 22-entry
    diacritic checklist, independent of back-translation); https://devpost.com/software/alertproof-atx
    (AlertProof ATX — protected-fact registry + deterministic checks + sabotage test for
    multilingual emergency messages); TMS QA tools (Xbench/Verifika/memoQ/Trados) ship
    number/omission/glossary checks but explicitly cannot assess meaning
  - https://github.com/pidoko/safetyBridge (WorkSafeBC hackathon — prompt-based, no gates)
  - EU Machinery Regulation / ISO 12100 language requirements (via AD VERBUM compliance
    positioning) — regulatory stakes rising
- **Independent corroboration:** Korea Herald (independent press); OSHA position (regulator);
  DeepL manufacturing white paper (market demand evidence).
- **Existing solutions:** DeepL/Google (generic, no domain verification), Vitra.ai (human review
  workflow), AD VERBUM (ISO-certified services), SafetyBridge (prompt-based hackathon project).
- **Known limitations of those solutions:** generic MT has no safety verification; human review
  doesn't scale and is the cost bottleneck; SafetyBridge has no verification gates at all.
- **Counterevidence:** quantitative failure-rate evidence is thin (no measurable mistranslation
  incident rate found); the market may exist unindexed; workers may not check verifications any
  more than they check translations.
- **CONF:** MED-HIGH that the gap is real (RED-TEAM REVISED: verification is an established
  industry PRACTICE — ISO 17100/18587, MTPE number/unit checks, commercial validators — the
  honest gap is "no productized deterministic automation for the full safety-critical fact class
  on safety documents"); MED on quantitative demand (no mistranslation-incident rate found;
  OSHA accident searches found none citing translation error as cause).
- **Remaining uncertainties:** measurable incident data; buyer willingness to pay (RED-TEAM:
  Korea majors self-build; free Spanish stock materials exist; Wordly live-translation attacks
  the same OSHA driver at ~$1,500/10h); whether verification is a wedge or a feature of EHS
  platforms/TMS QA gates (deflationary language-services market, Nimdzi <1% growth 2026).
- **Potential solution directions:** deterministic preservation verification for translated
  safety documents covering the FULL safety-critical fact class — quantities+units (unit-aware
  magnitude), negations, urgency phrases with softening-severity detection, AND regulatory
  citations — with ledger-constrained generation (rewriter never sees source), refusal-to-publish,
  and per-fact traceability. RED-TEAM NARROWING: DoseGuard (Devpost ~Apr 2026) and AlertProof ATX
  (Devpost ~Aug 2026) implement fragments in other document domains; TMS QA tools (Xbench/
  Verifika/memoQ/Trados) explicitly cannot assess meaning (no negation/urgency/citation gates);
  the narrowed claim survives; the broad "verification is new" claim does NOT.
- **Event fit:** Track 1 (Intelligent Industry — "monitor safety conditions", factory context) or
  Track 4 (multilingual creative content — weaker fit). Strong fit to Track 1's "results that
  operators can understand."

---

## P5 — Ecommerce catalog data is fragmented → INVALIDATED

- **ID:** P5. **Type:** FACT (market saturation).
- Status: REJECTED as an opportunity — ≥8 launched products with write-back (Ranketta, Adobe LLM
  Optimizer, Feedonomics Enrichment, BigCommerce Catalog Enrichment, Hypotenuse, Zoovu, GroupBy,
  Alhena). See COMPETITIVE-INTELLIGENCE.md C5. Sources retained:
  https://ranketta.com/blog/ai-product-enrichment ;
  https://www.digitalcommerce360.com/2026/09/30/commerce-product-catalogs-ai-discovery-enrichment-tools/

---

## P6 — Teachers spend hours preparing differentiated materials — NOT PURSUED

- **ID:** P6. **Type:** FACT (pain) — rejected for scope: crowded research space (FACET, AdaPT,
  multiple 2026 papers), weak fit to the event's four business tracks, education buyers are
  slow. Sources: wave2-raw.json (education-knowledge-access, education-feedback-grading).

## P7 — Administrative burden in digital government — NOT PURSUED

- **ID:** P7. **Type:** FACT (strong academic literature) — rejected for scope: hackathon cannot
  credibly integrate with government systems. Sources: wave2-raw.json (public-services-burden:
  "The accidental caseworker", "Administrative Literacy in the Digital Welfare State").

## P8 — Identity verification barriers for blind/low-vision users — NOT PURSUED (recorded for future rounds)

- **ID:** P8. **Type:** FACT (real underserved need; "Essential, Yet Overlooked: Identity
  Verification Barriers for Blind and Low Vision" in wave2-raw.json). No product scan executed;
  recorded as rejected-for-scope, not rejected-on-evidence.

---

## Rejected ideas log (with evidence)

| Idea | Evidence for rejection |
|---|---|
| Prior-auth automation product | Red ocean (8+ funded products); EHR/payer integration infeasible in hackathon; 61% physician distrust of AI in PA |
| Generic manual-RAG chatbot | Commoditized; Siemens/Caterpillar shipped; published lab recipe exists |
| Discharge instruction simplification (English) | Existing hackathon project (Intact, Aug 2026) does the exact mechanism |
| Ecommerce catalog enrichment | ≥8 launched products with write-back and distribution |
| Education differentiation agents | Crowded; weak business-track fit |
| Government service navigation | Integration infeasible |
| Demand forecasting with LLM | Explicitly barred by official Track 3 rules ("Do not use a language model as the only forecasting method") |
