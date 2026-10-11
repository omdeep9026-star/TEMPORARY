# METHOD — 10 unique faceless-YouTube niche opportunities

Date of research: 2026-10-11 (single-day campaign, UTC).
Deliverable: FINDINGS.md (10 concepts). This file documents how the evidence was produced.

## Tools verified before use

- `orx 0.2.14` installed but NOT needed: orx is a paper/repo discovery CLI; this mission needed
  web/community/YouTube evidence, so `web_search`, `web_extract`, browser, and curl were used instead.
- Browser (datacenter IP) successfully loaded YouTube and rendered full search snapshots.
- `web_search` (Bing-backed), `web_extract` (Exa/Firecrawl/Keenable backends, keyless), curl.

## Search campaign (all raw JSON saved in raw/)

| File | Contents | Count |
|---|---|---|
| raw/wave1-discovery.json | open-web discovery across 25 candidate industries | 25 queries |
| raw/wave2-community.json | Reddit/community probes per industry + regulatory edge cases | 25 queries |
| raw/wave3-youtube-competition.json | YouTube existence probes per candidate | 25 queries |
| raw/wave4-demand-monetization.json | RPM/CPM evidence, AIO accuracy studies, demand drivers | 20 queries |
| raw/wave5-gap-probes.json | gap checks for weak candidates (marine claims, art title) | 8 queries |
| raw/wave6-final-probes.json | quota prices, crab collapse, watch parts, ad economics | 8 queries |
| raw/extract-*.json | full-page extracts of ~40 primary/secondary sources | 5 files |
| raw/yt-competition.json | structured YouTube SERP data, 2 queries x 28 niches | 56 queries |
| raw/yt-channels.json / yt-channels2.json | channel subscriber/video counts, 16 channels | 16 lookups |
| raw/yt-watch-laytime.json | final YouTube probes (watch econ) | 3 queries |

Total: ~155 search queries + 56 structured YouTube SERP extractions + 16 channel lookups.
Citation ledger: citations-ledger.json (66 registered sources, [1]–[66]).

## YouTube evidence method

YouTube search pages were fetched and parsed from `ytInitialData` (curl), plus one
browser-rendered cross-check. Recorded per result: title, videoId, length, view count,
upload age, channel. Channel scale from /@handle/about pages. Views/ages are as
displayed at retrieval time (2026-10-11). "View velocity" is NOT computed except where
noted, because ages are coarse ("3y ago") — treat view counts as point-in-time.

## AI Overview testing — what was and was NOT done (read this first)

**The user's requested AI Overview methodology could not be executed from this environment.**
Attempted surfaces and outcomes:

| Surface | Attempt | Result |
|---|---|---|
| Google Search SERP via curl (AIO markers) | 2 queries | No AI Overview content in HTML (JS-gated) |
| Google Search in browser | 2 queries | CAPTCHA wall (google.com/sorry, IP 4.240.18.224) |
| Bing SERP via curl | 2 queries | Bot-walled; returned irrelevant cached results |
| Brave Search / Ecosia via curl | 2 queries | JS shells, no usable content |
| Perplexity in browser | 1 query | Cloudflare "Just a moment..." |

Therefore: **no claim in FINDINGS.md is based on a live AI Overview observation by this agent.**
Zero AIO observations were made; AI Overview citation rates and verified error rates for the 10
niches are UNMEASURED. What was done instead:

1. Third-party AIO context retrieved and cited: BrightEdge-via-SEL (+25.21% YoY YouTube citations
   in AI Overviews; strongest for instructional/visual content) [1], Guardian (Jan 2026: AIOs cite
   YouTube more than any medical site) [2], Oumi (Apr 2026: ~50% of AIO results untrustworthy;
   "millions of incorrect results per hour" claim picked up by NDTV/NYPost) [3], NYT AIO accuracy
   piece (Apr 2026) [4].
2. **A ready-to-run test kit was built** (AIOV-GAP-KIT.md): 40 pre-written queries across the 10
   niches, a recording template, an error taxonomy (verified error / omission / incompleteness /
   unsupported claim / stale number), and a screenshot convention. It must be run from a
   residential IP (or with a SERP API), and its results should replace the "AIO status" lines in
   FINDINGS.md.

Hypothesis (user's): obscure niches benefit from AIO gaps. Status: plausible but UNVERIFIED here;
BrightEdge's data suggests AIOs increasingly DO cite YouTube for instructional queries [1], which
cuts both ways — gaps may exist where AIOs answer generically instead of citing videos, but AIOs
may also cite videos heavily in exactly these niches. Do not assume AIO confusion guarantees views.

## Monetization evidence and its limits

- Creator-reported RPM tables: 1of10 [5] and CreatorAdvance [6] — finance/investing $10–30 and
  legal grouped in "highest-paying niches $10–32 RPM"; most channels $2–5. These are aggregated
  creator reports, not audited data.
- First-person RPM examples on r/PartneredYoutube: $13–$22 RPM in gaming with long-form content;
  CPM $40–50 [7]. RPM ≠ CPM (RPM is after YouTube's 45% cut; CPM is advertiser-side).
- Insurance-lead economics (buying-intent proxy for claim/coverage audiences): $24–40/call auto,
  $30–40/call home; ~$40/CPC on broad "car insurance"; n=124 agencies (Quotely internal
  benchmark, Aug 2026) [51].
- **No RPM number in FINDINGS.md is a measurement of these niches.** Comparable-niche ranges are
  labeled as such; everything else is an assumption and marked.

## Key limitations

1. AIO behavior untested (see above) — biggest open item.
2. View counts are point-in-time YouTube displays, not audited analytics; view velocity mostly
   not derived (coarse ages).
3. Search-volume data (Ahrefs/Google Keyword Planner) not available in this environment —
   zero-exact-match observations prove absence of exact matches only.
4. Reddit extraction is rate-limited/blocked for some threads (403s on r/Watches, r/LawFirm,
   r/PartneredYoutube full comments); where extraction failed, search-snippet titles are the
   evidence and are labeled.
5. Single-day snapshot: pricing pages (survey fees, buyer premiums) move; dates recorded per source.
6. The 10 concepts are research objects, not recommendations — no ranking, no winner, per brief.
