# METHOD P2 — 10 alternative niches: large audience + constant fresh content

Date of research: 2026-10-11 (same-day continuation of phase 1; phase 1 files untouched in
/workspaces/TEMPORARY/niche-research/). Deliverable: FINDINGS-P2.md. Ledger:
citations-ledger-p2.json (61 sources, [1]–[61]).

## How candidates were chosen

Two-screen process:
1. Freshness screen (~96 web queries, waves 1/2/4 in raw/): every query asked about 2026
   developments, so results double as dated renewal evidence. Beats that returned only
   evergreen pages or stale coverage were dropped.
2. Competition screen (structured YouTube SERP extraction, raw/yt-competition-p2.json and
   -p2b.json, 28 queries): measured what exists per angle — dedicated channels vs news-clip
   fragments vs faceless attempts with single-digit views.

## Freshness evidence method and limits

- Dated examples in FINDINGS-P2.md are from retrieved pages: agency press releases, Federal
  Register notices, rate announcements, court filings, devaluations — each with its own date.
  Counting "stories in the last 30/90/180 days" from a single day's sampling UNDERCOUNTS (a
  SERP shows ~6 results per query, not the full firehose). Where a live statistics database
  exists (recallbench for recalls, FRED for prices), its YTD counts are cited directly [22].
- Google Trends RSS was verified accessible from this environment (raw/trends-rss-test.txt,
  fetched 2026-10-11: top US trending = "steelers schedule", "premier league standings"...) —
  it confirms a usable freshness pipeline exists for the user, but trending lists are sports/
  entertainment-heavy and were NOT used as niche evidence.
- Sustainable topics/week estimates are ORDER-OF-MAGNITUDE estimates from the density of dated
  events found in one day's sampling plus recurring-calendar items (quarterly rate caps,
  monthly settlement deadlines, weekly recall notices). They are labeled estimates, not counts.

## YouTube evidence method

Same as phase 1: search pages parsed from ytInitialData via curl; per-result title, videoId,
length, views, age, channel; channel scale from /@handle/about (raw/yt-channels-p2.json).
Views/ages as displayed 2026-10-11. Note: some "channel" handles resolved to different real
channels (e.g., blancolirio's about-page shows @FlightChops 364K subs) — where ambiguous,
the video's own displayed stats are used and channel scale is omitted.

## Monetization evidence and limits

- Creator-reported RPM tables [5][6] and first-person RPM threads [7] (same as phase 1).
- Card-affiliate economics: $100–800 per approved application CPA, vendor guide (Mar 2026) [9].
- Insurance-lead economics: $24–40/call, n=124 agencies, vendor benchmark (Aug 2026) [74].
- Medicare marketing spend: GAO documents direct-to-consumer drug advertising scale [41];
  no audited "Medicare media market size" figure was retrieved — labeled as a gap.
- NO RPM in FINDINGS-P2.md is measured for these niches. Finance-band context [6] is labeled
  as context. CPM ≠ RPM throughout.

## AI Overview status

Same constraint as phase 1 (Google CAPTCHA-walls this datacenter IP; verified twice on
2026-10-11). No AIO observation was made for any phase-2 niche. Every concept carries
pre-written test queries (10 each, section 10 of each concept) for manual/API testing from a
residential IP. Nothing in section 10 is a result; all are queries to run.

## Key limitations (cumulative)

1. AIO behavior untested everywhere (phase 1 + phase 2); kit queries provided.
2. Single-day sampling for freshness — undercounts actual story volume; treat weekly-pipeline
   numbers as floors-with-uncertainty, not measurements.
3. News-clip channels (CBS/ABC/local stations) dominate some SERPs — competition data reflects
   what surfaces in search, not total supply; "gap" claims are about DEDICATED explainer
   channels, verified per-query in raw/yt-competition-p2*.json.
4. RPM remains unmeasured per niche (no creator self-reports found for these exact angles).
5. Audience-size figures are indirect proxies (view counts on adjacent content, program
   enrollment data where public); no keyword-tool search volumes available in this environment.
