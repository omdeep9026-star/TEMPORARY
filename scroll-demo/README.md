# Scroll Technique Lab

A single-file demo of professional scroll-driven animation techniques, built from eight
GitHub repositories researched specifically for this. Scroll is the only input; nothing
plays on a timer.

```
scroll-demo/
├── index.html   ← the entire demo (no build step, no package.json)
└── README.md
```

## Run it

ES modules will not load over `file://`, so it needs to be served over HTTP:

```sh
cd scroll-demo
python3 -m http.server 8000
# open http://localhost:8000
```

Any static server works. Dependencies come from CDN (three.js r180 via import map, GSAP
3.12.5 + ScrollTrigger via cdnjs), so the first load needs a network connection and
nothing else.

Press **D** in the page for a debug readout: scroll progress vs. target, current act,
lerped camera Z, scroll velocity, fps.

## Technique → source map

Every implemented technique, the repository it came from, and what was adapted. All
sources are MIT unless noted. "Concept" means the idea was reimplemented against this
demo's own scroll-progress pipeline rather than copied.

| Technique | Source repo | File / example | Adapted |
|---|---|---|---|
| Per-character "ignite": blur → sharp + brightness + glow | `codrops/ScrollBlurTypography` | `js/effect-1/blurScrollEffect.js` | Concept — one combined scrubbed filter instead of a plain fade |
| Per-character `drop-shadow` glow | `codrops/OnScrollTextHighlight` | `js/effect-13/highlightEffect.js` | Concept — glow radius derived from scroll progress, not a tween |
| Grid stagger from centre | `codrops/OnScrollTypographyAnimations` | `src/js/index.js` fx4 | Concept — computed per character instead of via `stagger:{grid:'auto'}` |
| 3D character flip (`perspective` on parent) | `codrops/OnScrollTypographyAnimations` | `src/js/index.js` fx6 / fx7 | Concept — finale headline |
| Line/word/char splitter | `codrops/ScrollBlurTypography` | `js/textSplitter.js` | Rewritten — measures real rendered chars, honours author `<br>` |
| Cue windows: plateau, overlap, held close | `nateherkai/scroll-craft` | `references/devices.md` §1–2 | Concept |
| Cue glow tied to opacity, with settle | `nateherkai/scroll-craft` | `references/devices.md` §2 | Concept — glow squared against opacity so it never sits at a constant |
| Travelling glow (offset + colour) | `codrops/TextClipScroll` | `js/index.js` effect-7 | Concept — driven from section progress, not a tween |
| Selective/global bloom | `mrdoob/three.js` | `examples/webgl_postprocessing_unreal_bloom.html` | Concept — global pass, high threshold |
| Emissive geometry + rim light | `mrdoob/three.js` | `examples/webgl_lights_physical.html` | Concept |
| Lerped scroll playhead | `nateherkai/scroll-craft` | `references/devices.md` §1 | Concept |
| Frame-rate-independent easing | `matinmonshizadeh/animation-handbook` | `01-scroll-based/scrub-animation` | Concept |
| Blur quantisation for compositor reuse | `matinmonshizadeh/animation-handbook` | `01-scroll-based/parallax-depth-of-field` | Concept |
| Canvas frame sequence | `matinmonshizadeh/animation-handbook` | `01-scroll-based/scroll-image-sequence` | Concept |
| Camera path, bounds, velocity damping | `houmahani/codrops-depth-gallery` | `src/Experience/Scroll.js` | Concept |

Sources were read but deliberately **not** used: `codrops/OnScrollSVGFilterText` and
`GooeyTextHoverEffect` (SVG gooey filters — slow on HTML text, and the organic edge fights
display type). `pmndrs/postprocessing` (Zlib) is a library rather than examples; three.js
addons cover the same ground with less indirection.

## Repositories used

### 1. `nateherkai/scroll-craft` — MIT — 2.9k★ — pushed 2026-09-30
<https://github.com/nateherkai/scroll-craft>

The most valuable find. Not a tutorial collection: a *craft standard* for scroll-driven
pages, backed by a documented 1,283-line reference engine and a nine-device kit. Its
`references/devices.md` is the sharpest writing I found on why scroll work usually looks
cheap, and it corrected several assumptions I would otherwise have shipped:

- **The playhead is lerped, never written 1:1.** Scroll events arrive at an uneven rate,
  so writing a value directly reproduces every gap between wheel notches and reads as a
  stutter. Scroll writes a *target*; a rAF loop walks the value toward it.
- **Clip time is not cue time.** A pinned stage is on screen for one viewport *before*
  pinning begins and one *after* it ends. Mapping an animation to pinned travel alone
  freezes it on frame one while it slides in and on the last frame while it slides out.
  The demo avoids this by mapping the camera to the act's whole visible life.
- **Cue windows need a plateau.** A cue with no plateau is a triangle that touches full
  opacity for a single instant, so every heading reads slightly faded. Windows must
  overlap so the stage is never empty, and the last cue must hold so the act ends on a
  statement.
- **Parallax rates live in hundreds of pixels, not viewport fractions.** Adjacent planes
  should differ by 10–30%; anything larger reads as things sliding around.
- **The ground should drift** between acts within one theme family — invisible frame to
  frame, obvious top to bottom.

### 2. `matinmonshizadeh/animation-handbook` — MIT — pushed 2026-10-01
<https://github.com/matinmonshizadeh/animation-handbook>

129 live, dependency-free technique demos across 7 categories (26 scroll-based, 18
3D/advanced, 12 page transitions, 14 typography). Every demo is a single self-contained
`index.html` with readable vanilla JS — the exact shape I needed for reference code I
could lift without untangling a framework. Three techniques came from here:

- **Frame-rate-independent easing.** `1 - Math.pow(1-EASE, dt/FRAME)` rather than a flat
  per-frame constant, so the glide lasts the same on a 30, 60 or 120Hz screen.
- **Blur quantisation for compositor reuse.** Snapping `blur()` to 0.5px steps lets the
  browser reuse the rasterised layer instead of re-filtering five full-bleed planes every
  frame. Their inline comment ("never in the scroll handler, where each one would force a
  synchronous reflow") is why all layout reads in this demo are hoisted out of the loop.
- **Deterministic frames.** Each frame is a pure function of its index, so scrubbing
  backwards is exact and a frame already on the canvas is not redrawn.

### 3. `houmahani/codrops-depth-gallery` — MIT — 113★ — pushed 2026-03-09
<https://github.com/houmahani/codrops-depth-gallery>

The one recent Three.js repo with real depth-scrolling craft in readable vanilla JS (no
React, no build step in the source). Its `src/Experience/Scroll.js` is the clearest
implementation I found of the scroll→camera binding:

- Scroll amount maps linearly to camera Z through a single `scrollToWorldFactor`.
- Camera travel is **bounded by the scene**, not by the scrollbar — `updateCameraBounds()`
  measures the gallery's depth range so the camera never enters or overshoots the geometry.
- **Velocity is damped separately** (`lerp(velocity, raw, 0.12)` then clamped) and used to
  drive visual intensity, so fast scrolling feels fast and stopping settles.

I rejected several higher-star candidates and why:

| Repo | Reason |
|---|---|
| `greensock/GSAP` | The canonical ScrollTrigger source, but it's the library, not examples — and as of 2025 no license file. Used as a CDN dependency instead. |
| `basementstudio/scrollytelling` (1.6k★) | Excellent library, React-only, and `NOASSERTION` license. Unliftable into a vanilla single file. |
| `locomotivemtl/locomotive-scroll` (8.9k★) | Strong smooth-scroll lib, but it intercepts the scrollbar, which fights the "scroll is the scrubber" model. Its example folder is a docs site, not source. |
| `drcmda/the-substance` (430★) | Superb scroll+shader work but React Three Fiber, and untouched since 2020. |
| `vaneenige/scroll-transitions-webgl` | The best WebGL transition demo ever made, but 2019, unmaintained, and its licence forbids redistribution "as-is". |
| `scrollama` (6k★) | The right tool for *step-based* data scrollytelling (IntersectionObserver, not scroll math). Right technique, wrong shape for a continuous cinematic demo. |

## Techniques demonstrated

Five acts, each using a different mechanism, all sharing one scroll-progress pipeline.

**Act 01 — Cinematic camera scrub (Three.js / WebGL)**
One `position: fixed` WebGL stage for the whole page; the document is only a scroll track.
Five camera legs (position + look-at target) interpolated with Catmull-Rom so the path
curves rather than snapping between waypoints. Exponential fog grades depth, a corridor of
40 monoliths flanking the path makes the dolly read as *travel* rather than zoom, and
1,400 dust points give in-scene parallax. Scroll velocity damps separately and drives edge
emissive intensity. *(scroll-craft dwell + playhead lerp; depth-gallery scroll→Z, bounds, velocity)*

**Act 02 — Pinned stage with scrubbed cue windows (GSAP ScrollTrigger)**
`pin` + `scrub: 0.6` on a 340vh section. Three cues stacked in one box so they crossfade
*in place*, each with an in-plateau and an out-plateau, windows overlapping ~10%, and the
closing cue holding to the end rather than fading out. The stack's box height is declared
at the display type scale, not the body scale — `em` on the container resolves against the
container's own size, which is what makes absolutely-positioned cue lines the right height.

**Act 03 — Canvas frame-sequence scrub**
120 procedurally drawn frames (wireframe cube + inner octahedron, hand-rolled perspective
divide — no 2D canvas API needed beyond paths). Scroll picks the target frame, a lerped
playhead eases toward it, and each frame is a pure function of its index so reversal is
exact. The canvas is only touched while near the viewport, and a frame already drawn is
never redrawn. *(animation-handbook scroll-image-sequence)*

**Act 04 — Layered parallax with a travelling focus plane**
Five SVG planes at depths 0.0 → 1.0 with speeds 0.00 → 0.70. The plane of sharp focus
travels from the far ridge to the foreground and every other plane is blurred by its
distance from it, quantised to 0.5px steps. A gradient floor hides the plane-clip line at
the section's bottom edge. *(animation-handbook parallax-depth-of-field)*

**Act 05 — Cinematic transition + travelling glow + ground drift**
The finale headline assembles with a per-character 3D flip while a `drop-shadow` travels
across it — offset and colour both interpolating ember → violet — so the light appears to
move over the letters. A one-sided veil then cuts, driven by section progress rather than a
timer, on a window deliberately placed *after* the type has assembled so it never blacks out
headline mid-read. The page ground interpolates between five near-black stops across the
page as the camera reaches each leg.

Throughout: **`prefers-reduced-motion`** handling on every mechanism — hero resolves to its
lit end state with no scrub, per-frame character filters never run, parallax offsets zero,
veil off, scrub instantaneous, cues still readable, camera still tracks the reader rather
than freezing.

## Typography notes

Two things the research changed, and both are load-bearing:

**Splitting changes how text measures.** Turning characters into `inline-block` spans
disables kerning and ligatures, so the split text is a few percent *wider* than the original
string. The splitter therefore measures the real rendered characters and pops the last word
when a line overflows, rather than measuring plain text in an offscreen probe — measuring
the probe's numbers fits words that do not actually fit, and a two-line headline silently
becomes three with a one-word orphan. `.tline` and the hero's line units are `nowrap` for
the same reason: line breaks are the splitter's decision, not the browser's.

**Screen readers must not read the split.** Each split element keeps an `aria-label` with
the original text and the split nodes are `aria-hidden`, so the headline is announced as a
sentence rather than letter by letter.

**Scrub lag is a design parameter, not smoothing.** The hero runs `scrub: 1.2` and the pinned
act `0.6`. The spread is deliberate: the hero wants weight, the pinned act wants precision
because the reader is reading the words. Smoothing everywhere would flatten that difference.

**Glow stays purposeful.** The pinned cue's glow is derived from its own opacity (squared, so
it only really appears near the plateau) and the closing cue settles from 16px to ~6.5px as
the act ends, rather than holding full neon across a third of the page. In the 3D scene only
every fourth monolith carries the hot emissive strip, because bloom multiplies brightness and
a bright edge on everything turns the corridor into a white tube.

## Performance notes

- All layout reads happen in `measure()` / `onResize()`, never inside the scroll handler
  or the frame loop, where each would force a synchronous reflow.
- Style writes are guarded by last-value caches (`lastBlur`, `lastOff`, `seqDrawn`) so an
  unchanged value costs nothing.
- `filter: blur()` is quantised and `translate3d` is used for all layer motion, keeping
  the work on the compositor.
- Canvas DPR is clamped to 2.
- Glow values are quantised (0.5px for cues, 1/64 for hero characters) so an unchanged
  value costs no DOM write.
- Bloom is a single global pass at `threshold 0.72` — only the deliberately bright pixels
  cross it. A selective two-composer pass was the fallback, not the plan; it proved
  unnecessary because the typography is DOM and therefore cannot be washed out by a WebGL
  bloom at all.
- **Bloom auto-disables on a software renderer.** `UnrealBloomPass` is roughly ten extra
  full-screen draws per frame; measured here at **10fps → 3fps** on SwiftShader, which would
  make the demo unusable in exactly the environments most likely to open it without a GPU.
  The renderer string is checked at startup and the composer is skipped when it matches
  SwiftShader / llvmpipe / software (a console note explains why). On a GPU it runs, at half
  resolution since the glow is a soft wide halo. The emissive geometry and rim light still
  carry the scene without it, so the difference is a softer glow, not a broken page. Set
  `window.__forceBloom = true` before load to override, or `window.__bloomOff` at runtime.

Verified in headless Chromium at 1280×577 across eleven sampled scroll positions, checking
that hero opacity/blur/glow, cue glow, finale glow and flip, veil, frame index and camera Z
all track progress monotonically. Two bugs in this pass were only visible from measurement,
not from looking: a held cue riding the un-pin slide at full opacity over the next section's
headline, and split text silently re-wrapping a two-line headline into three.

On the software rasteriser used for verification the demo holds ~11fps with bloom
auto-disabled and ~3fps with it forced on. On any GPU-backed browser the frame cost is far
lower — the per-frame work is one render call, a handful of guarded style writes, and two
lerps.
