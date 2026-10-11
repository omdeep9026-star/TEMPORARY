# Red Team — Competitive Intelligence Investigation (Candidate A: LEDGER)

Date: 2026-10-09. Investigator: competitive-intelligence red team subagent. Method: 15 web
searches (web_search) + 4 full-page extractions (web_extract) across Devpost, GitHub, lablab.ai,
Product Hunt, TMS vendor docs (Xbench, Verifika, memoQ, Crowdin, DeepL, Lokalise/Smartling),
spec-sheet tools, and scholarly (arXiv/ACL). Target: break the prior C4 conclusion that "no
deterministic verification product exists" for translated safety documents.

## Verdict: the strong form of the prior conclusion is BROKEN

The prior scan (COMPETITIVE-INTELLIGENCE.md C4) claimed: "nobody found offering deterministic
preservation verification for translated safety documents." That claim does not survive:

1. **Deterministic verification of translated safety-critical content already exists at hackathon
   scale.** DoseGuard (Devpost, SoCal Claude Builder Club Hackathon, ~Apr 2026) applies
   deterministic, model-independent checks to translated medication instructions: field
   canonicalization and numeric normalization comparing translated output against originals, plus
   a dedicated 22-entry diacritic validation checklist that runs "entirely independent of the
   back-translation pipeline." https://devpost.com/software/doseguard
2. **The deterministic-refusal-gate pattern (refuse to publish, name the broken rule, adversarial
   corruption harness) already exists.** TrueCopy (Devpost, DevNetwork [API + Cloud + AI]
   Hackathon, first commit 6 Sept 2026) refuses to publish any translation failing 7 pure string
   rules (URLs byte-for-byte, timestamps well-formed, @handles/#hashtags/promo codes preserved),
   "no model in the loop, identical verdict every time," with an adversarial attack section and a
   self-found echo-rule hole. https://devpost.com/software/truecopy — different fact class
   (YouTube metadata), but the exact gate/refusal/adversarial-harness mechanism.
3. **Fact-registry + deterministic checks + multilingual drafts + sabotage test already exist.**
   AlertProof ATX (Devpost, ~Aug 2026) is a pre-publication verification assistant for emergency
   messages: reviewer-owned protected facts (time, place, action, contact, prohibitions),
   claim-by-claim verification matrix across English/Spanish/Vietnamese/Arabic/Pashto drafts,
   deterministic schema-validated checks, and a "sabotage test that intentionally mutates a
   high-risk fact to prove the verifier can block it." https://devpost.com/software/alertproof-atx
4. **Deterministic number/unit/terminology QA for translated documents is commoditized.** Xbench,
   Verifika, memoQ, Trados and Crowdin have shipped these checks for years: number mismatches,
   omissions, URL/alphanumeric mismatches, glossary/term-base enforcement, tag validation
   (https://docs.xbench.net/online-help/dialogs/main-window/qa ;
   https://e-verifika.com/checks_in_detail — includes digit-to-text conversion and
   imperial/metric-parenthesis skip settings ;
   https://docs.memoq.com/current/en/Concepts/concepts-quality-assurance-qa-warnings.html).
5. **A major translation vendor now ships automated error detection.** DeepL's Translation
   Quality Evaluation (TQE) AI model "detects potential errors in DeepL translations and flags
   them to human reviewers" (model-based, not deterministic).
   https://www.linkedin.com/posts/deepl_how-were-building-translation-quality-evaluation-activity-7485273902072553472-46nj
6. **A commercial industrial-domain product does structured, unit-preserving translation.**
   SpecMake (live pricing; onboarding Q1 2027) extracts property-value-unit triples with
   confidence scores and source anchors, translates into 14 languages with "numerical values and
   units pass through untouched," standards codes verbatim, grammar validation, and EU
   compliance cross-checks (CE, REACH, ATEX, Machinery Regulation).
   https://www.specmake.com/features/translation ; https://www.specmake.com/how-it-works

## What was NOT found (the surviving differentiation — labeled as absence of evidence)

No product, project, or research artifact was found that combines ALL of:
- Deterministic preservation gates over the FULL safety-critical fact class: quantities+units
  (unit-aware magnitude), negations, urgency/timeframe phrases with softening detection, AND
  regulatory citations — enforced by code with a refusal-to-publish path.
- Ledger-constrained generation (rewriter never sees source text, sees only the fact ledger).
- Applied to industrial safety documents (lockout/tagout, toolbox talks, machine safety sheets).
- On an open model served on AMD infrastructure.

Specifically verified absences:
- **Negations and urgency: no shipped tool checks them deterministically.** TMS QA tools check
  "things that can be confirmed without reading for meaning... What they don't assess is meaning,
  accuracy, or register" (https://snapintel.io/blog/best-translation-qa-tools-in-2026-xbench-verifika-and-the-alternatives-compared).
  The safety signal-word hierarchy check (DANGER→WARNING downgrades, ANSI Z535/ISO 3864) is
  documented as a MANUAL two-pass human review process, not automated — "it took us two completed
  projects to catch this systematically"
  (https://chatscontrol.com/blog/mtpe-technical-manuals-workflow-quality-checks).
- **Regulatory citations: no built-in deterministic gate in any shipped TMS** (Xbench/Verifika/
  memoQ checklists and regex features let users hand-build such checks, but nothing ships one for
  citations).
- **Negation is a documented, unsolved failure mode in MT** (quality reductions >60% in some
  directions; automatic metrics are bad estimators when negation is present):
  https://aclanthology.org/2020.findings-emnlp.345.pdf
- **No one has applied the ledger mechanism to industrial safety documents.** DoseGuard =
  medication labels/discharge (medical); AlertProof ATX = emergency alerts (drafts are prepared
  fixtures, public build calls no live model); TrueCopy = YouTube metadata; SpecMake = spec-sheet
  data (extraction-based translation, no preservation gates on generated translations, no
  negation/urgency/citation verification, compliance runs on source not translation); Intact =
  English discharge docs only.
- lablab AMD/IBM hackathon space: closest are Chaukidar (ACT II — multilingual LLM-output safety
  audits, not document verification),
  https://lablab.ai/ai-hackathons/amd-developer-hackathon-act-ii/punkrockers/chaukidar ;
  TransCreate (token-survival sentinel pipeline for developer videos),
  https://lablab.ai/ai-hackathons/ibm-bob-2-hackathon/deep-saha/transcreate-cultural-localization-for-developers ;
  AgeBand ("LLM estimates → deterministic layer decides" — different domain),
  https://lablab.ai/ai-hackathons/amd-developer-hackathon-act-ii/kiano/ageband ;
  Every Tongue (Scripture grounding + back-translation + review notes, no deterministic gates),
  https://lablab.ai/ai-hackathons/amd-developer-hackathon-act-ii/bulletproof-automation/every-tongue-ai-scripture-study-in-any-language
  — the "deterministic layer decides" PATTERN is now common in lablab hackathons, but none does
  fact-ledger-constrained safety-document translation with preservation gates.
- Prior-scan findings confirmed: SafetyBridge is prompt-based with no gates (GitHub created
  2025-10-20, Claude Sonnet 4 translation, "preserves regulatory citations exactly" is a prompt
  feature; disclaimer requires qualified bilingual review),
  https://github.com/pidoko/safetyBridge ; VelocityEHS Global List Translator is an enterprise
  EHS translation feature with no verification,
  https://www.ehs.com/blogs/standardizing-jsa-risk-assessments-multilingual-workforces ;
  MixTranslate (launched 22 Jul 2026) is model-comparison QE scoring, not deterministic,
  https://finance.yahoo.com/technology/ai/articles/mixtranslate-introduces-ai-translation-agent-153500366.html

## Closest competitors (threat-ranked)

| Competitor | Threat | What it does | URL |
|---|---|---|---|
| DoseGuard | HIGH | Deterministic verification of translated medication instructions (Yoruba): numeric normalization + 22-entry diacritic checklist independent of back-translation; ensemble OCR; FDA grounding; clinician escalation. Hackathon, medical domain | https://devpost.com/software/doseguard |
| AlertProof ATX | HIGH | Fact registry + deterministic checks + multilingual emergency-message drafts (EN/ES/VI/AR/PS) + sabotage test; no live model in public build; student team. Hackathon, ~Aug 2026 | https://devpost.com/software/alertproof-atx |
| SpecMake | MEDIUM | Commercial spec-sheet document intelligence: extraction with unit/value preservation into 14-language translation, grammar validation, EU compliance cross-checks. Launched; no preservation gates on translations, no negation/urgency/citation checks | https://www.specmake.com/features/translation |
| TrueCopy | MEDIUM | Deterministic refusal gate over translated YouTube metadata (URLs/timestamps/handles); adversarial harness; Sept 2026. Proves the gate pattern, different domain and fact class | https://devpost.com/software/truecopy |
| Xbench / Verifika / memoQ / Trados / Crowdin | MEDIUM | Shipped deterministic TMS QA for years: numbers, omissions, glossary, tags, URLs. No negation, urgency, or citation gates; no meaning assessment | https://docs.xbench.net/online-help/dialogs/main-window/qa |
| DeepL TQE | MEDIUM | Shipped AI-model error detection flagging DeepL translations to human reviewers; model-based, not deterministic, not domain-specific | https://www.linkedin.com/posts/deepl_how-were-building-translation-quality-evaluation-activity-7485273902072553472-46nj |
| Intact | MEDIUM | The mechanism ancestor: fact ledger + deterministic preservation gates (pint unit-aware) on English discharge docs; Devpost Aug 2026; domain-general version explicitly not built | https://devpost.com/software/intact-9j3a4c |
| SafetyBridge | LOW | Prompt-based AI multilingual safety-doc translation (WorkSafeBC InnoFest 2025); citation preservation claimed at prompt level; no verification gates | https://github.com/pidoko/safetyBridge |
| VelocityEHS Global List Translator | LOW | Enterprise EHS multilingual risk-terminology translation; no verification layer | https://www.ehs.com/blogs/standardizing-jsa-risk-assessments-multilingual-workforces |
| MixTranslate | LOW | 20+ model comparison with QE quality scores for translations; launched Jul 2026; not deterministic, not safety-specific | https://finance.yahoo.com/technology/ai/articles/mixtranslate-introduces-ai-translation-agent-153500366.html |
| TransCreate (IBM Bob hackathon) | LOW | Token-survival sentinel pipeline for developer-video subtitles; QE heuristics; Sept 2026 | https://lablab.ai/ai-hackathons/ibm-bob-2-hackathon/deep-saha/transcreate-cultural-localization-for-developers |

## Searches executed (web_search unless noted)

1. site:devpost.com multilingual safety translation verification
2. site:github.com translation safety verification lockout tagout OSHA multilingual (0 results)
3. "safety-critical" translation verification deterministic product QA
4. machine translation quality assurance safety critical industrial documents tool
5. Xbench Verifika QA check negation omission number mismatch translation features
6. Phrase memoQ Crowdin QA checks regulatory citation urgency negation translation quality
7. site:lablab.ai multilingual translation safety verification hackathon
8. site:producthunt.com AI translation compliance verification safety
9. Lokalise Smartling "quality assurance" checks numbers glossary AI hallucination translation feature
10. "translation validation" OR "preservation check" LLM generated translation tool github 2026
11. DeepL API verify translation quality feature numbers glossary hallucination check
12. arxiv translation quality estimation negation numbers safety critical instructions multilingual verification
13. "fact ledger" constrained generation translation safety verification multilingual
14. specmake document intelligence translation spec sheets structured extraction product pricing
15. "translation verification" OR "verify translations" startup launch 2026 deterministic safety multilingual OSHA EHS
16. web_extract: devpost.com/software/alertproof-atx, /software/truecopy, /software/doseguard (full pages)
17. web_extract: github.com/pidoko/safetyBridge (full page)

## Assessment for the selection decision

**Candidate A survives as PARTIALLY_DIFFERENTIATED.** The originality claim must be narrowed
from "no deterministic verification product exists for translated safety documents" (broken:
DoseGuard, AlertProof ATX, TMS QA, DeepL TQE) to the defensible form:

> Deterministic preservation verification of translated safety documents exists only in
> fragments: TMS QA checks numbers/terminology but not negations, urgency, or citations and
> "cannot assess meaning"; hackathon projects prove the gate pattern in adjacent domains
> (medical labels, emergency alerts, YouTube metadata); no product combines preservation gates
> over the full safety-critical fact class (units+quantities, negations, urgency phrases,
> regulatory citations) with ledger-constrained generation, refusal-to-publish, and per-fact
> traceability — applied to industrial safety documents where OSHA's "in a manner employees
> can understand" standard and the EU Machinery Regulation raise the stakes.

Concrete demo implications (the red team's recommended adjustments):
1. Lead with the fact-class argument, not "verification is new": show DoseGuard/TMS QA in the
   related-work slide and name exactly which safety-critical fact classes they cannot check
   (negations, urgency severity, citations).
2. The negation + urgency + citation gates are the sharpest mechanistic novelty — nothing
   shipped checks them deterministically (cite snapintel + ChatsControl manual-two-pass
   evidence). Demonstrate a DANGER→WARNING downgrade and a dropped citation being intercepted.
3. The "deterministic layer decides" architecture pattern is no longer novel in hackathon
   space (AgeBand, SafeO, TrueCopy, WorldReady at lablab). Judges may have seen it. What
   remains defensible: applying it to safety-document preservation with a regulatory-stakes
   user (EHS manager), and the strip-not-flag additions gate.
4. Risk acknowledged: three of the closest competitors are recent hackathon projects
   (Aug–Sept 2026). If this event's judging pool overlaps, the pattern-recognition risk rises.
   The domain grounding (industrial LOTO/toolbox talks, OSHA/EU citations) is what keeps it
   differentiated — no project in that space has claimed safety documents.
5. The absence claim must be stated as absence-of-evidence: 15 searches + 4 extractions found
   no full-combination product; the market may exist in unindexed forms (internal enterprise
   tools, Japan/Korea regional vendors are plausible blind spots — science.co.jp documents the
   physical-AI translation-safety concern but ships human review as the guarantee).
