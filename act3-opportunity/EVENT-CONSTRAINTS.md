# Act 3 Hackathon — Event Constraints (verified against official sources)

Date compiled: 2026-10-09. All facts below were read directly from official event pages unless
marked ASSUMPTION or UNVERIFIED.

## Event identification

**AMD Developer Hackathon: ACT III** — organized by lablab.ai in partnership with AMD.

- Official event page: https://lablab.ai/ai-hackathons/amd-developer-hackathon-act-iii
- Official live page: https://lablab.ai/ai-hackathons/amd-developer-hackathon-act-iii/live
- Read directly from both pages (browser + web_extract) on 2026-10-09.

## Format and dates (VERIFIED)

- Hybrid hackathon: online build phase + on-site phase in Italy (Rome, Milan, Imperia).
- Online build: 12–18 October 2026 (live page: build "12-17 October"; submission close Sunday,
  Oct 18 15:00 UTC — the live page shows BOTH "Oct 17, 2026, 17:00 UTC" and "Oct 18, 2026,
  15:00 UTC" in different sections; treat Oct 18 15:00 UTC as the conservative deadline).
- Kickoff: Monday, Oct 12 2026, 15:00 UTC. Registration closes at kickoff.
- On-site phase: 17–18 October 2026, three cities (Rome: Link Campus University; Milan:
  SmartCityLab Milano; Imperia: IMPERIAWARE). On-site participation requires approval; travel
  and accommodation not covered.
- Prize pool: $12,000+ ($5,000 from AMD, $5,000 from Google, Evolus track prizes totaling
  €1,011.50, Vibe Generation special prize: AirPods 5 for team members).
- Scale: 5,002 registered builders, 871 teams forming (as of Oct 9, live page).

## Central challenge statement (VERIFIED, exact wording)

"Choose one of four business challenges and build a working product on AMD infrastructure. We
are looking for projects that solve a real problem for a real user. Your idea can use language
models, computer vision, audio, agents, predictive models, or a combination of technologies.
The important part is simple: **the product should work, and AMD technology should power a
meaningful part of it.**"

## The four tracks (VERIFIED, full briefs expanded from official page)

### Track 1 — Intelligent Industry (Vibe Generation)
"Help factories spot problems earlier and operate better."
- Factories produce data from machines, cameras, sensors, maintenance reports, technical
  manuals. "The problem is rarely a lack of information. The problem is knowing what matters
  and what to do next."
- Build: reduce downtime, improve quality, increase safety, or use resources more efficiently.
- Ideas listed: predict equipment failures; detect defects from images/video; explain production
  anomalies; help technicians search manuals and maintenance records; recommend maintenance
  actions; monitor safety conditions; reduce energy/material waste.
- Demo: process realistic industrial data → useful alert, explanation, recommendation, or
  action. Good projects show: a real manufacturing problem, a working product (not only a
  dashboard), results operators can understand, a measurable improvement in time/cost/safety/
  quality/efficiency.

### Track 2 — Health and Wellbeing (Vibe Generation)
"Make a part of the patient journey safer, clearer, or easier."
- "Patients and healthcare workers deal with long documents, scattered information, repetitive
  administration, language barriers, and limited time."
- Ideas: patient intake; medical record summaries; appointment preparation; care navigation;
  clearer discharge instructions; multilingual patient communication; healthcare document
  processing; administrative workflow automation; wellbeing and prevention support.
- Demo: realistic case from first input to final result; make uncertainty visible; know when a
  person needs to review or take over.
- SAFETY RULES: must not present autonomous diagnosis/treatment as medical advice; must explain
  handling of incorrect/unsupported responses, sensitive information, uncertain results, high
  risk decisions, human review.

### Track 3 — Reinvent Commerce (Vibe Generation)
"Help a business understand its customers and take better action."
- "Retailers have product data, transactions, inventory, reviews, support conversations, and
  marketing results. These sources are often disconnected, which makes it difficult to turn
  them into useful decisions."
- Ideas: shopping assistants; product discovery/recommendations; customer support; demand and
  inventory planning; catalogue enrichment; review and sentiment analysis; promotion planning;
  churn prevention; accessible/multilingual shopping; in-store computer vision.
- CONSTRAINT: "If your product predicts demand, sales, or customer behaviour, explain how the
  prediction was calculated. Do not use a language model as the only forecasting method."

### Track 4 — Create a New Kind of Experience (Vibe Generation)
"Build a media, marketing, or entertainment experience that was not practical before generative
AI. Do more than generate an image, advertisement, or chatbot. Create something that responds to
its audience, changes with context, or produces a different experience for each person."
- Ideas: personalized video; interactive stories; audience driven entertainment; adaptive
  campaigns; multilingual creative content; generative brand experiences; responsive sound or
  visual environments; new social media formats; accessible media experiences; creative quality
  control.
- Demo: experience changing for ≥2 audiences/situations/inputs; explain what was created, what
  models generated/decided, quality/consistency control, cost per generated experience, who
  would pay.

### Track 5 — Evolus Business Agents on AMD (Evolus)
"Build an AI agent that runs a real business process end to end, on Evolus, powered by an open
model served on AMD."
- Requirements (verified): (1) free Evolus event workspace at app.evolus.ai with event code
  shared at kickoff; (2) main agent must use an open model served on AMD infrastructure through
  own vLLM endpoint on AMD Developer Cloud; (3) at least two Evolus building blocks (workflows,
  document extractors, AI Tools, knowledge libraries, MCP connectors, sub-agents, chat widget);
  (4) drive Evolus from your app through its REST API; (5) containerized app, public GitHub
  repository, README that runs, no committed API keys.
- Sample use cases: invoice/order intake (email+PDF → extract fields → match order → flag
  mismatches); support desk on company knowledge; lead qualification; contract review;
  multilingual documents; meeting follow-up.
- Evolus-team judging reading: Application of Technology (depth of building-block use, AMD-hosted
  model integration); Business Value (real process, clear user, measurable gain); Originality (a
  process nobody automated this way); Presentation. Verification: Evolus team reviews workspace
  configuration and usage statistics.

## Technology requirement (VERIFIED)

Every project must run a meaningful part of its workload on AMD infrastructure/hardware:
AMD Developer Cloud, AMD Instinct accelerators, AMD ROCm, AMD Ryzen AI, AMD Radeon hardware, or
other approved AMD-powered infrastructure provided during the event. "The AMD component must be
part of the working product shown to the judges." Teams choose their own compatible models,
frameworks, and tools. Partner technologies (Google, Evolus) are optional and unlock extra
prize eligibility; a project may qualify for the main prize, one partner prize, or both.

## Judging criteria (VERIFIED — official rubric, no published weights)

The event page's "Judging Criteria" section lists four criteria. No numeric weights are
published anywhere on the official pages (VERIFIED ABSENCE — checked main page and live page):
1. **Application of Technology** — "How effectively the chosen model(s) are integrated into the
   solution."
2. **Presentation** — "The clarity and effectiveness of the project presentation."
3. **Business Value** — "The impact and practical value, considering how well it fits into
   business areas."
4. **Originality** — "The uniqueness and creativity of the solution, highlighting approaches and
   ability to demonstrate behaviors."

## Submission requirements (VERIFIED)

Project: project title; short and long descriptions; selected challenge; technology tags;
working prototype. Presentation: cover image; demo video; pitch presentation; clear explanation
of the problem and intended user. Also (from lablab guidelines links): original work,
MIT-compliant; containerized app, public GitHub repository, README that runs (per Evolus track
rules, which mirror general lablab submission rules).

## Implications for problem discovery (interpretations, not event claims)

- Interpretation: "the product should work" + "working prototype" + demo video make end-to-end
  reliability the highest-leverage property. A narrow, complete, verifiable workflow beats a
  broad, flaky one.
- Interpretation: every track is a business-track with a named user; judges score "Business
  Value ... how well it fits into business areas." Problem discovery must land on a real user
  with a real workflow, not a technology demo.
- Interpretation: with no published weights, assume approximate parity (25% each) and disclose
  this as a provisional weighting. Originality rewards "a process nobody automated this way" —
  differentiation must be mechanistic, not cosmetic.
- Interpretation: AMD must power "a meaningful part of the working product" — the architecture
  must put a real workload (model inference, or a GPU-compute step) on AMD infrastructure, and
  the demo must show it.

## Previous winners (partially verified)

- ASSUMPTION/UNVERIFIED: search results reference "ACT I winner (REPOMIND)" and "REPOMIND v3
  submitted to ACT II" from an unofficial aggregator page (hattasimae.online). No official
  winners list for ACT III exists yet (event has not run). Treat prior-finalist information as
  directional only.
- Officially verifiable: lablab.ai publishes winners across its channels after judging; nothing
  for this event is published yet.

## Gaps and uncertainties

- UNVERIFIED: exact submission deadline (Oct 17 17:00 UTC vs Oct 18 15:00 UTC conflicting
  strings on the live page; conservative planning assumes Oct 18 15:00 UTC).
- UNVERIFIED: judging weights (none published).
- UNVERIFIED: tracks labeled "Tracks TBA / Announced soon" on the live page while the main page
  lists the four Vibe Generation challenges plus Evolus — the main page briefs were read
  directly and are treated as authoritative.
- Development time available: build phase Oct 12–18 (6 days) for a team; this discovery process
  runs Oct 9 (pre-kickoff). Prototype must fit roughly 4–5 effective build days after setup.
