# AI-Overview Gap Test Kit — 40 queries across 10 niches

Status: READY TO RUN, NOT YET RUN. Every AIO claim in FINDINGS.md is marked UNMEASURED until
this kit (or an equivalent) is executed. Run from a residential IP, a clean browser profile, or
a SERP API (SerpApi / DataForSEO / ScraperAPI all expose AI Overview fields). Google blocks
datacenter IPs (verified 2026-10-11: CAPTCHA on google.com/sorry from 4.240.18.224).

## Recording protocol

For each query, record in aiov/results.csv:
- query_id, query_text, niche, date_time (UTC), surface ("google-web" or api name)
- aio_present (yes/no/interstitial-failed), aio_text_excerpt (<=2000 chars)
- yt_citations: list of youtube.com/watch URLs cited inside the AI Overview
- other_citations: non-YouTube sources cited
- classification, per the taxonomy below
- screenshot path (aiov/shots/<query_id>.png) — full-page capture including the AIO panel
- notes (anything odd: signed-out state, consent wall, location wording)

Taxonomy (mutually exclusive, in priority order — a "verified error" outranks "omission"):
1. VERIFIED-ERROR — the AIO asserts something checkable and an authoritative source contradicts
   it (cite both). E.g., a stated fee, threshold, rate, or rule that the official body contradicts.
2. UNSUPPORTED-CLAIM — the AIO states a specific number/rule with no citation or a citation that
   does not contain the number.
3. OMISSION — a question a specialist would answer has a whole dimension absent (e.g., "what does
   a survey include" answered without the Table A itemization or the survey-vs-surveyor distinction).
4. INCOMPLETENESS — the right dimension appears but is generic/hedged ("it depends" without the
   ranges the primary sources give).
5. NO-AIO — Google shows no AI Overview for the query (record this; it is a result, not a failure).
6. CITED-BUT-WEAK — AIO exists, cites a video/page that does not actually answer the question.

Sample size: 40 queries, 4 per niche. Report rates as X/4 with denominators — never as percentages
alone. Re-test any surprising result twice (same query, 24h apart) before calling it an error.

## The queries (4 per niche)

N1 marine-survey-economics:
- how much does a marine survey cost for a 35 foot boat
- what does a marine survey include haul out sea trial
- who pays for the boat survey buyer or seller
- do lenders and insurers require a marine survey and which type

N2 grain-contract-math:
- what is basis in grain marketing and why does it change
- how is shrink calculated when selling wet corn to the elevator
- what is a hedge-to-arrive contract risk to the farmer
- what do grain elevator discounts mean for test weight and moisture

N3 used-aircraft-buying:
- what does a prebuy inspection cost on a used single engine aircraft
- what is an annual inspection vs a prebuy on a Cessna 182
- how do you check an aircraft logbook before buying
- what squawks should ground a used aircraft purchase

N4 equine-money-decisions:
- how much does colic surgery cost for a horse with complications
- when is euthanasia chosen instead of colic surgery
- how much does it cost to own a horse per year realistically
- does horse insurance cover colic surgery and what is excluded

N5 legal-trust-accounting:
- what is the difference between IOLTA and a client trust account
- can a lawyer pay themselves from a trust account and when
- what happens if a law firm trust account goes negative
- how often must attorney trust accounts be reconciled

N6 commercial-title-survey:
- what is an ALTA survey and when is it required
- how much does an ALTA survey cost for a commercial property
- what are Table A items in an ALTA survey
- ALTA survey vs boundary survey difference

N7 equipment-auction-economics:
- what fees does a buyer pay at Ritchie Bros auctions
- how do you inspect an excavator before bidding at auction
- why do auction prices differ from dealer used prices
- what is a buyer's premium on heavy equipment

N8 dental-practice-transitions:
- how is a dental practice valued EBITDA multiple
- what does an associate buy-in to a dental practice look like
- DSO vs private sale of dental practice pros and cons
- what happens to patient records and goodwill in a dental sale

N9 quota-fishery-economics:
- how does Alaska halibut IFQ quota work and what does it cost to lease
- what happened to the Bering Sea snow crab fishery in 2023
- what is the difference between IFQ and IPQ in Alaska crab
- how do catch share quota transfers get priced

N10 340b-program-mechanics:
- what is the 340B drug pricing program and how do savings flow
- what is the 340B rebate model dispute about
- can contract pharmacies be restricted by manufacturers
- who is eligible as a 340B covered entity

## Control queries (mainstream, for contrast — run in the same session)

- best travel credit cards 2026 (expect heavy AIO + heavy YouTube citation)
- how to start a dropshipping business
- what is a roth ira

## Consistency checks

- Same browser, same session, same signed-out state for all 50 queries.
- Log failed/interstitial queries and re-run; do not silently drop them from the denominator.
- If using an API, spot-check 5 queries manually against the browser to validate the API's AIO
  field; report the disagreement rate.

## After running

Paste per-niche rates into the "AI Overview status" line of each concept in FINDINGS.md and
delete the "UNMEASURED" markers. Any VERIFIED-ERROR found should be logged in
aiov/verified-errors.md with both URLs (AIO screenshot + contradicting authority).
