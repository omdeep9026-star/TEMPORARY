# Candidate comparison — scroll-driven / scrollytelling animation repos

Selection criteria, in order: (1) real working examples with readable source, (2) recency /
active maintenance, (3) coverage of the requested technique list, (4) license, (5) liftability
into a single vanilla HTML file.

Activity and license figures are from the GitHub API on 2026-10-01 unless noted.

## Considered

| Repo | ★ | Last push | License | Verdict |
|---|---|---|---|---|
| **nateherkai/scroll-craft** | 2890 | 2026-09-30 | MIT | **SELECTED** |
| **matinmonshizadeh/animation-handbook** | 6 | 2026-10-01 | MIT | **SELECTED** — star count is meaningless here, see note |
| **houmahani/codrops-depth-gallery** | 113 | 2026-03-09 | MIT | **SELECTED** |
| greensock/GSAP | 28749 | 2026-04-13 | none stated | Rejected — the library, not examples; no license file in repo |
| basementstudio/scrollytelling | 1665 | 2024-02-22 | NOASSERTION | Rejected — React-only, no clear license |
| locomotivemtl/locomotive-scroll | 8869 | 2026-06-30 | MIT | Rejected — intercepts scrollbar; docs site not source |
| drcmda/the-substance | 430 | 2020-06-07 | MIT | Rejected — R3F, stale |
| vaneenige/scroll-transitions-webgl | 156 | 2019-11-17 | custom, no redistribution | Rejected — unmaintained, license forbids as-is reuse |
| russellsamora/scrollama | 6001 | — | MIT | Rejected for this demo — correct step-based tool, wrong shape |
| motiondivision/motion | 33790 | 2026-10-01 | MIT | Rejected — library, no scroll examples |
| pmndrs/react-three-fiber | 32644 | 2026-10-01 | MIT | Rejected — library |
| amatonsingh431 / and ~40 GitHub "scroll-animation" topic repos | <20 | 2025–2026 | mostly none | Rejected in bulk — single demos or tutorial clones, no example density |
| thomson159/scrollytelling | 2 | archived 2025-03-09 | MIT | Rejected — archived |

## Why the three selected

### nateherkai/scroll-craft
Highest-value documentation found on this subject by a wide margin, and the only candidate
whose source is a *documented engine* (1,283 lines) rather than a pile of demos.
`references/devices.md` (552 lines) enumerates nine devices with the failure modes spelled
out; `references/worldflight.md` covers the single-fixed-stage pattern used for Act 01.
Techniques that changed the demo's construction:

- Lerped playhead, never a 1:1 scroll write.
- Cue windows need plateaus, must overlap, and the last cue must hold.
- `clip-path` is relative to the border box, not the ink — line-height below 1 shears
  ascenders and descenders (relevant to the kinetic line masks).
- Parallax rates in hundreds of px, adjacent planes differing 10–30%.
- Ground drift across acts within one theme family.
- `max(height - viewport, 1)` pinning math: a pinned act below ~1.2 viewport-heights of
  travel has no room for cues to play.

### matinmonshizadeh/animation-handbook
129 self-contained `index.html` demos, zero dependencies, zero build. Only 6 stars, which
is why a stars-sorted search nearly buried it — the highest-leverage pick of the three and
the direct counter-example to ranking by popularity. Directly used: scrub-animation,
scroll-image-sequence, parallax-depth-of-field, pin-animation, sticky-section,
stacking-cards, section-wipe, scroll-background-color, scrollytelling.

### houmahani/codrops-depth-gallery
The only recent, MIT, vanilla-JS Three.js repo found with genuine depth-scrolling craft and
readable source. `src/Experience/Scroll.js` supplies the scroll→camera binding: a single
`scrollToWorldFactor`, camera travel bounded by measured scene depth rather than by the
scrollbar, and separately damped velocity for visual intensity.

## Techniques extracted into the demo

| Technique | Source |
|---|---|
| Lerped scroll playhead, frame-rate independent | scroll-craft + animation-handbook |
| Single fixed WebGL stage, no seams | scroll-craft worldflight |
| Camera path interpolation + dwell remap | scroll-craft + depth-gallery |
| Camera travel bounded by scene, not scrollbar | depth-gallery |
| Separately damped scroll velocity → visual intensity | depth-gallery |
| Fog as depth cue for camera travel | depth-gallery |
| Pinned stage, scrubbed timeline | scroll-craft + animation-handbook |
| Cue windows with plateaus, overlap, held close | scroll-craft |
| Per-line kinetic type reveal behind masks | scroll-craft |
| Canvas frame-sequence scrub, deterministic frames | animation-handbook |
| Layered parallax with travelling focus plane | animation-handbook |
| Blur quantisation for compositor reuse | animation-handbook |
| Ground drift between acts | scroll-craft |
| Progress-driven cinematic transition (no timer) | scroll-craft + animation-handbook |
| `prefers-reduced-motion` honoured per mechanism | all three |

## Rejected on licence grounds

`vaneenige/scroll-transitions-webgl` remains the single best WebGL scroll-transition demo
that exists and its technique was studied, but its licence forbids redistribution
"as-is" and sale of unmodified copies, so no code was taken — only the one-sided-crossfade
idea, which scroll-craft also documents and which was implemented independently.
