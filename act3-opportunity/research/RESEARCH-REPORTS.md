# Research Campaign — Wave 1 & 2 Structured Reports (scholarly retrieval via Open Research)

Date: 2026-10-09. Mechanism: `orx discover` (alphaXiv keyword/embedding, OpenAlex) executed in the
main session per the installed `orx-lit-review` discipline. Raw JSON audit trail:
`research/wave1-raw.json`, `research/wave2-raw.json` (16 directions, 128 unique-ish candidates).

---

## Direction A — Industrial technician documentation & troubleshooting

**Research question:** What tasks do factory/field technicians repeatedly describe as frustrating,
and where does scholarly work target the same pain?

**Search methodology:** `orx discover keyword "technician troubleshooting manual retrieval
manufacturing" --limit 8`, `orx discover keyword "equipment failure prediction maintenance
decision support" --limit 8`, `orx discover keyword "field service technician workflow
documentation mobile" --limit 8`; web_search across r/BMET, r/DieselTechs, r/HVAC, r/MechanicAdvice.

**Findings (with citations):**
- Reddit r/BMET "Does anyone else waste hours searching for equipment manuals?" (clinical
  engineering, 3 years in): "Google search returns irrelevant results, spending hours trying to
  find that one document, sometimes even days... you spend hours digging through it just to find
  one answer." Users report already using ChatGPT/Claude and hitting hallucination walls:
  "after a certain amount of time, chat would just hallucinate... I'll have to look for it
  myself and add it again to the chat." https://www.reddit.com/r/BMET/comments/1spuxgh/
- Same thread: workflows are manual and fragmented — OneSourceDocs subscriptions, personal PDF
  libraries, OneNote tagging, shared drives, calling manufacturers. "If OneSource does not have
  the manual you are probably not going to get it."
- r/DieselTechs: "We (technicians) don't get service manuals or any type of troubleshooting
  manuals..." — troubleshooting programs gatekept to managers' tablets.
  https://reddit.com/r/DieselTechs/comments/1kfpdt1/
- r/HVAC: intermittent-fault diagnosis fails because "you don't have the information needed to
  make a firm diagnosis"; manufacturers provide "flow charts and code indexes that are about 3
  abstraction layers too shallow." https://www.reddit.com/r/HVAC/comments/1dapuaq/
- Scholarly: "Reducing Technician Search Burden: A Multimodal RAG for Cessna 172 Maintenance"
  (wave1-raw), "RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting",
  "TSG Suggester: Tree-Structured Knowledge-Graph Retrieval for Troubleshooting" — active
  research area, confirming the pain is real and current.
- Practitioner write-ups claim commercial copilots (Siemens Industrial Copilot, Caterpillar
  variants) deliver "15-30% reduction in mean-time-to-repair on covered equipment classes,
  concentrated on routine failures... novel or chained-cause faults see considerably smaller
  gains" — with the caveat these are vendor case studies, not independent audits.

**Problem candidates:** P1 (technician manual/error-code retrieval and in-manual answer finding);
P1b (intermittent-fault diagnosis support).

**Existing alternatives:** OneSourceDocs, CMMS attachments, ManualsLib, vendor copilots,
generic ChatGPT/Claude use, tribal knowledge / asking colleagues.

**Evidence quality:** First-person primary observations (Reddit threads, multiple independent
users, recent), corroborated by active scholarly literature and practitioner reports. Strong.

**Counterevidence:** Some technicians say manual hunting is rare ("I wouldn't spend 2 days
looking for a manual"); commercial copilots exist for major equipment classes; manual-finding
aggregators reduce the "find the document" half of the pain.

**Unanswered questions:** How big is the in-manual "dig for the answer" time vs the
document-finding time; which equipment classes lack copilot coverage; SME manufacturer budgets.

**Follow-up investigations:** Competitive scan of Siemens Industrial Copilot coverage; SME
manufacturer pain evidence; AMD-feasibility of on-prem RAG.

---

## Direction B — Health clinician administration & patient paperwork

**Research question:** Where do clinicians and patients lose time to documents and
administration, and is the pain recurring and measurable?

**Search methodology:** `orx discover embedding "clinicians spending time on documentation and
administrative tasks instead of patient care" --limit 8`; `orx discover keyword "discharge
instructions patient comprehension readability" --limit 8`; web_search AMA prior authorization
surveys + discharge comprehension studies.

**Findings (with citations):**
- AMA Prior Authorization Physician Survey (n=1,000 practicing physicians, fielded Dec 2024/2025
  editions): practices complete **39–40 PAs per physician per week**; physicians and staff spend
  **13 hours/week** on PA; **89–94%** report PA contributes to burnout; **93–95%** report PA
  delays access to necessary care; **29%** report PA caused a serious adverse event for a patient
  in their care; 40% of physicians have staff working exclusively on PA.
  https://www.ama-assn.org/system/files/prior-authorization-survey.pdf ;
  https://www.ama-assn.org/practice-management/prior-authorization/fixing-prior-auth-nearly-40-prior-authorizations-week-way
- Patient comprehension: "the least understood domain was the return to ED instructions, with
  63.8% of patients having no or poor understanding" (PMC5805670, cited by 95);
  "patients with a clear understanding of their home care instructions are 30% less likely to be
  readmitted or to visit the ED" (NSO/Cullman Regional).
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5805670/
- Scholarly: "AI-Generated Prior Authorization Letters: Strong Clinical Content, Weak..."
  (wave1 raw — the failure mode is documented), "Retrieval-Augmented Large Language Models for
  Schema-Constrained Clinical..." — active LLM work on exactly these documents.
- Track 2 official brief matches: "long documents, scattered information, repetitive
  administration, language barriers, and limited time."

**Problem candidates:** P2 (prior-auth preparation/appeals); P3 (discharge instruction
comprehension); P3b (multilingual patient communication).

**Existing alternatives:** EHR-integrated PA automation products (see competitive report),
ambient documentation, human scribes, teach-back protocols.

**Evidence quality:** Official professional-body surveys (n=1000, recurring annually), peer-reviewed
clinical studies, recent (2024–2026). Very strong.

**Counterevidence:** 61% of physicians worry AI will increase PA denial rates (Becker's summary of
AMA survey) — user trust in AI for this workflow is contested.

**Unanswered questions:** Whether a hackathon-scale tool can integrate with EHR/payer systems at
all (see competitive intelligence — it cannot credibly).

**Follow-up investigations:** Competitive intelligence on PA automation (executed — see below).

---

## Direction C — Commerce: catalog enrichment & review mining

**Research question:** Are disconnected commerce data sources a real underserved problem?

**Search methodology:** `orx discover keyword "product catalog enrichment ecommerce data quality"
--limit 8`; `orx discover openalex "customer reviews converting feedback into product decisions"
--limit 8`; web_search commercial enrichment tools 2026.

**Findings:** Official Track 3 brief names the disconnection. Scholarly work exists (TRACE: Agentic
Catalog Enrichment with Multi-source Evidence Grounding; DeepAffinity). BUT the commercial market
is saturated: Ranketta ("trusted by 1,200+ brands", per-SKU tracking across 8 engines,
confidence-scored enrichment write-back into Shopify/Shoptet/feeds), Adobe LLM Optimizer (one-click
write-back with rollback), Feedonomics Enrichment + BigCommerce Catalog Enrichment (launched
2026), Hypotenuse AI, Zoovu, GroupBy, Alhena AI.
https://ranketta.com/blog/ai-product-enrichment ;
https://www.digitalcommerce360.com/2026/09/30/commerce-product-catalogs-ai-discovery-enrichment-tools/

**Problem candidates:** P5 (catalog enrichment — invalidated as an opportunity by market
saturation); review-mining remains unfocused.

**Existing alternatives:** see above — at least eight credible commercial products with
write-back.

**Evidence quality:** Vendor claims are marketing; but the breadth of independent coverage
(trade press, multiple vendors, comparison guides) is itself the counterevidence.

**Counterevidence:** The market saturation IS the counterevidence. Rejected.

**Unanswered questions:** none material — opportunity rejected.

---

## Directions D–H (education, SMB, accessibility, public services, emerging, multilingual, safety reporting) — summary

**Research question:** Is there a validated, recurring, underserved problem in these domains
suitable for this event?

**Search methodology:** wave2 `orx discover` queries (embedding/keyword/openalex, one per
direction) + `orx discover keyword "safety critical information translation verification"`.

**Findings:**
- Education: active LLM work (FACET: Multi-Agent AI Supporting Teachers in Scaling
  Differentiated Learning; AdaPT Adaptive Lesson Plan Transformer; teacher AI-TPACK studies) —
  real pain (teacher prep hours) but crowded research space and weak fit to the four business
  tracks.
- SMB: GST compliance burden in India (two independent scholarly papers), administrative burden
  impact assessments — validated pain, but jurisdiction-specific and low demo fit.
- Accessibility: "Essential, Yet Overlooked: Identity Verification Barriers for Blind and Low
  Vision" — real underserved need; cognitive-load literature (C-LISTEN; developer cognitive load
  during GenAI).
- Public services: strong academic literature on administrative burden in digital government
  ("The accidental caseworker – How digital self-service influences citizens' [burden]";
  "Administrative Literacy in the Digital Welfare State: Migrants Navigating...") — validated
  and recurring, but a hackathon cannot credibly integrate with government systems.
- Multilingual enterprise: W-RAG (Source-Aware Retrieval for Enterprise Document Generation from
  Heterogeneous...), governed artifact generation (SAGE, GUIDE) — mechanism research exists.
- **Safety-critical translation verification**: `orx discover keyword "safety critical
  information translation verification"` returned only formal-verification papers from other
  domains (quantum ancilla safety, FTL proofs) — NO scholarly or product work on verifying
  translated safety documents by deterministic preservation checks. Absence of retrieval results
  is NOT proof of absence (noted per operating rules), but combined with the web evidence below,
  the verification layer appears genuinely open.

**Evidence quality:** Moderate-to-strong for pain; thin for product gaps (expected — gaps are
harder to retrieve).

**Counterevidence:** DeepL/Google Translate dominate generic translation; Korea deployments show
AI translators already adopted at construction firms (without verification guarantees).

**Unanswered questions:** Whether any Western product verifies translated safety documents
(covered by competitive intelligence below).

**Follow-up investigations:** executed — see competitive intelligence report.
