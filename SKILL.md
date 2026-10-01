---
name: scroll-animation-reference
description: Reference for implementing scroll-driven web animation — lerped scroll playheads, pinned and scrubbed sections, cinematic 3D camera paths, parallax and depth of field, frame sequences, kinetic typography, typography and WebGL glow, and reduced-motion handling. Use when a task calls for a scroll-linked visual effect and a proven implementation should be inspected before writing code.
---

# Scroll-driven animation reference

A lookup guide for scroll-linked visual effects. The workflow it supports is:

```
need an effect → pick the repository → open one specific example →
understand the mechanism → reimplement independently
```

**These repositories are for study, not for vendoring.** Read an example to understand the
mechanism and the parameter ranges, then write the code against your own scroll pipeline.
Vendor libraries solve a problem a different codebase already solved, and the examples here
are written against GSAP's plugin API, bespoke classes, or a specific scene graph.

## Lookup table

| Need | Repository | File / example to inspect | Technique | Reproduction notes |
|---|---|---|---|---|
| Smooth scroll feel | animation-handbook | `animations/01-scroll-based/smooth-scroll/` | Inertial scrolling | Track a target and ease toward it; never write scroll 1:1 |
| Lerped playhead | scroll-craft | `references/devices.md` §1 "The playhead is lerped" | Scroll writes a target; a rAF loop walks the value toward it | Lerp ~0.18/frame; add a deadband and coalesce seeks |
| Scrubbed animation | animation-handbook | `animations/01-scroll-based/scrub-animation/` | Scroll position drives a timeline both directions | Reverse must be exact; make every value a pure function of progress |
| Pinning | scroll-craft | `references/devices.md` §2 `pin` | Stage holds while its argument advances | Travel is `height − viewport`; minimum span ~1.2 viewport-heights |
| Cue windows | scroll-craft | `references/devices.md` §2 "The cue contract" | Timed windows with plateaus, overlap and a held close | Every window needs a plateau; overlap ~15% of the act |
| Pinned + sticky variants | animation-handbook | `animations/01-scroll-based/pin-animation/`, `sticky-section/` | CSS sticky vs. JS pin | Sticky is cheaper; pin allows scrubbed progress |
| Cinematic camera move | codrops-depth-gallery | `src/Experience/Scroll.js` | Scroll mapped to camera Z along a fixed stage | One `scrollToWorldFactor`; damp current toward target |
| Camera path | codrops-depth-gallery | `src/Experience/Scroll.js` `cameraZFromScroll()` | Linear scroll→world mapping | Interpolate waypoints for a curve, not a linear ramp |
| Bounded camera travel | codrops-depth-gallery | `src/Experience/Scroll.js` `updateCameraBounds()` | Camera range derived from measured scene depth | Clamp to geometry, not to scrollbar length |
| Velocity → intensity | codrops-depth-gallery | `src/Experience/Scroll.js` `updateVelocity()` | Damped scroll velocity drives visual response | Damping ~0.12; clamp and zero below a threshold |
| Depth / fog | codrops-depth-gallery | `src/Experience/Background/index.js` | Exponential fog plus depth grading | Density sets how fast the corridor reads as distance |
| Parallax | scroll-craft | `references/devices.md` §6 `parallax` | Layers travel at different rates | Rate in hundreds of px; adjacent planes differ 10–30% |
| Parallax / depth of field | animation-handbook | `animations/01-scroll-based/parallax-depth-of-field/` | Layered planes with a travelling focus plane | Blur by distance from focus; quantise blur to 0.5px |
| Frame sequence | animation-handbook | `animations/01-scroll-based/scroll-image-sequence/` | Scroll position selects a frame; playhead lerps | Each frame a pure function of its index; skip redraws |
| Scroll velocity skew | animation-handbook | `animations/01-scroll-based/scroll-velocity-skew/` | Rows lean with scroll velocity | Read velocity from a rAF delta, not from wheel events |
| Kinetic typography | scroll-craft | `references/devices.md` §5 `kinetic` | Split into lines/words/chars, staggered | Lines almost always; one per act, never characters |
| Masked text reveal | scroll-craft | `references/devices.md` §5 + `references/hero-depth.md` | Units rise from behind a mask | Reserve room for descenders or tails shear off |
| Clip-path reveal | animation-handbook | `animations/05-text-typography/text-clip-path-reveal/` | Wipe reveal on type | `clip-path` clips the border box, not the glyph ink |
| Text distortion | animation-handbook | `animations/05-text-typography/` (`text-morphing`, `glitch-text`, `outline-to-fill`) | Morph and glitch states per character | Keep it short; sustained distortion is unreadable |
| 3D typography | animation-handbook | `animations/06-3d-advanced/scroll-driven-3d-rotation/` | Scroll turns a 3D object pose to pose | Perspective belongs on the parent, not the rotating node |
| Typography glow | animation-handbook | `animations/05-text-typography/kinetic-typography/` | Per-character filter animation | Drive glow radius from progress; keep it sparse |
| Blur / deblur type | animation-handbook | `animations/01-scroll-based/scrub-animation/` | Blur-to-sharp as scroll advances | Pair with brightness for ignition rather than a plain fade |
| Travelling glow | animation-handbook | `animations/03-page-transitions/` (dissolve, crossfade) | Shadow offset and colour interpolate | The offset is what makes the light appear to travel |
| WebGL emissive glow | codrops-depth-gallery | `src/Experience/Gallery.js`, `src/Experience/Background/index.js` | Emissive materials plus rim lighting | Mark only a few emitters; glow on everything reads as noise |
| Bloom / post-processing | animation-handbook | `animations/06-3d-advanced/webgl-shader-animation/`, `canvas-particle-effect/` | Post-processing style effects | Cheap alternative to a full composer; check cost on software GL |
| Cinematic transition | scroll-craft | `references/devices.md` §4 `reveal`, §10 `drift` | Wipe as a state change; ground colour shifts between acts | Use wipes big; a wipe on a small element is a fidget |
| Continuous world / no seams | scroll-craft | `references/worldflight.md` | One fixed stage, scroll drives only timeline and opacity | Avoids the unpin seams that pinned acts produce |
| Ground drift | scroll-craft | `references/devices.md` §10 `drift` | Page ground interpolates between acts | 3–5 stops, one theme family; invisible frame to frame |
| Verification | scroll-craft | `references/verify.md`, `scripts/shoot.mjs` | Screenshots at several scroll positions per act | Failures live between the two frames you looked at |

---

## Scroll progress and playback

### Lerped scroll playhead

**Look up:** scroll-craft — `references/devices.md` §1 "The playhead is lerped"

**What it demonstrates:** Scroll events arrive at an uneven rate. Writing a value directly in a
scroll handler reproduces every gap between events and reads as a stutter rather than a glide.
Scroll should write a *target*; a rAF loop walks the current value toward it.

**How to reproduce:** In the scroll handler, store `scrollY / maxScroll` as a target only. In a
rAF loop, ease current toward target by a fixed fraction per frame. Ease in time terms rather
than per frame, so the glide lasts the same on 30, 60 and 120Hz displays.

**Important details:** Lerp around 0.18 per frame is a good starting point; 0.02 to 1 is the
usable range, and 0 is invalid (a playhead that never moves). Add a deadband — a write smaller
than about 8ms on desktop or 20ms on mobile costs a seek and shows nothing. Coalesce seeks so a
fast flick does not queue several. Ease rate should be 1.0 (no smoothing) under reduced motion.

**License:** MIT.

### Scrubbed timelines

**Look up:** animation-handbook — `animations/01-scroll-based/scrub-animation/`

**What it demonstrates:** A timeline whose progress is scroll position, so scrolling back plays
it back exactly. The example draws the whole route up front and places a marker at the point on
the path matching the current progress.

**How to reproduce:** Derive every visual from a single normalised progress value. Keep a frame
counter and direction readout if debugging. For determinism, make each rendered state a pure
function of progress so no accumulated state can drift.

**Important details:** `scrub: true` locks to scroll; a numeric value adds lag. The lag is a
design parameter, not smoothing to be minimised — values from 0.9 to 1.9 appear in production
work for heavier movement. Use a low lag where the reader is reading text and a high lag for
transitions and hero motion.

**License:** MIT.

### Scroll velocity → visual intensity

**Look up:** codrops-depth-gallery — `src/Experience/Scroll.js` `updateVelocity()`

**What it demonstrates:** Raw velocity from a per-frame delta, then a separately damped velocity
clamped to a range. Visual intensity is driven from the damped value so a fast scroll feels fast
and stopping settles.

**How to reproduce:** Compute raw velocity from the difference in current position per frame.
Damp it with a lerp around 0.12, clamp to a maximum (the example uses 1.5), and zero it below a
small threshold. Drive edge glow, motion blur or skew from the result.

**Important details:** Damp velocity separately from position — damping them together makes the
two fight. Normalise wheel deltas across `deltaMode` values (0 = pixels, 1 = lines, 2 = pages) or
intensity will differ wildly between browsers and trackpads.

**License:** MIT.

---

## Sections, pinning and cues

### Pinned sections

**Look up:** scroll-craft — `references/devices.md` §2 `pin`

**What it demonstrates:** The stage sticks for a few viewport-heights while copy states cross over
inside it. Appropriate when the beat is an argument rather than an image.

**How to reproduce:** Pin the stage over a taller section, and drive a timeline from the pinned
progress rather than from time. Space acts so the stage holds for a sensible duration.

**Important details:** Pinned travel is `max(height − viewport, 1)`; at a span of 1 or below the
travel is one pixel and progress jumps 0→1 between two scroll notches, so every cue snaps
instead of running. Minimum useful span is about 1.2 viewport-heights. Reserve
`anticipatePin` to avoid a flicker as the pin engages.

**License:** MIT.

### Cue windows, plateaus and overlaps

**Look up:** scroll-craft — `references/devices.md` §2 "The cue contract"

**What it demonstrates:** Copy within a pinned act is scheduled with explicit windows: an entry
value, a plateau, and an exit. Variants include a "greet" form that is already at full opacity
when the act begins, and a single-value form that holds.

**How to reproduce:** Express each cue as a window against act progress, with ramps of roughly
30% of the window at each end. Overlap successive windows by about 15% of the act.

**Important details:**
- Without a plateau a cue is a triangle touching full opacity for a single instant, so the
  reader must stop on exactly the right pixel and every heading reads slightly faded.
- A gap between cues reads as a loading failure; overlap is what prevents it.
- A hero cue needs the greet form, or the landing view has no headline on it.
- Only the *last* act may hold a cue. A held cue on a middle act stays lit through the entire
  unpin slide, travels a full viewport upward, and overlaps the following section.
- A pinned stage becomes fully visible roughly one viewport *before* its progress leaves 0, so
  give the act either a ground that is already visible or a first cue in greet form.
- Release the stage during the unpin slide, or a closing line rides the whole slide at full
  opacity onto the next section's heading.

**License:** MIT.

### Continuous world (avoiding seams)

**Look up:** scroll-craft — `references/worldflight.md`

**What it demonstrates:** A page of pinned acts has visible boundaries: the stage unsticks, a
static page slides past, then scrolling resumes. This mode removes the blocks entirely — one
fixed stage for the whole page, every leg mounted at once, scroll driving only the timeline and
overlay opacity.

**How to reproduce:** Use a single `position: fixed` stage containing all scene legs, plus an
empty spacer as the only in-flow element. Set the spacer height to the sum of leg weights plus
one viewport-height.

**Important details:** The extra viewport is not padding — without it the final frame is a place
the reader can never come to rest. Crossfades must be one-sided: the incoming leg fades up while
the outgoing leg holds underneath. Never swap a `src`; a src swap is a black frame, which is the
cut this mode exists to remove.

**License:** MIT.

---

## Camera, depth and 3D

### Cinematic camera movement

**Look up:** codrops-depth-gallery — `src/Experience/Scroll.js`

**What it demonstrates:** A fixed Three.js stage where scroll amount maps to camera Z through a
single world factor, with current position eased toward target every frame. Two rows of objects
flank the path so the movement reads as travel rather than as a zoom.

**How to reproduce:** Keep one `scrollToWorldFactor` and convert scroll amount to camera Z with
it. Ease camera position toward target with the same lerp used for the scroll value so the camera
never snaps. Animate a look-at target as well as position.

**Important details:** Read the camera's initial position from the scene rather than hardcoding
it. Keep the document as the scroll track and the canvas fixed. A corridor of objects on both
sides of the path is what sells forward motion; without it a dolly reads as a zoom.

**License:** MIT.

### Camera path interpolation

**Look up:** codrops-depth-gallery — `src/Experience/Scroll.js` `cameraZFromScroll()`

**What it demonstrates:** Scroll-to-position as a linear mapping, which is the base layer a path
is built on.

**How to reproduce:** Define one waypoint per section, each with a camera position and a look-at
target. Interpolate between neighbouring waypoints with Catmull-Rom rather than snapping, so the
path curves.

**Important details:** Clamp the interpolation index at both ends of the waypoint list. Apply a
dwell remap — faster at the edges, settling in the middle — so the camera arrives where the copy
is. Interpolating position and target with the same spline keeps the camera aimed along the path.

**License:** MIT.

### Camera travel bounded by scene depth

**Look up:** codrops-depth-gallery — `src/Experience/Scroll.js` `updateCameraBounds()`

**What it demonstrates:** Camera min and max are measured from the scene's own depth range plus a
view offset, not derived from how long the scrollbar happens to be.

**How to reproduce:** Measure the depth of the objects the camera travels through, add a small
offset at each end, and clamp camera Z into that range.

**Important details:** Scroll length is a design choice, so camera travel keyed to scroll length
will overshoot or under-run whenever content height changes. Keying to scene depth makes the
camera independent of page height. If a naive range inverts (min above max), collapse it to a
single value rather than letting the camera travel backwards.

**License:** MIT.

### Fog and atmospheric depth

**Look up:** codrops-depth-gallery — `src/Experience/Background/index.js`

**What it demonstrates:** Exponential fog grading the corridor, with a dim far plane giving the fog
something to grade against.

**How to reproduce:** Attach exponential fog to the scene and tint it to match the page ground
rather than leaving it fixed. Add a large, low-opacity, depth-write-disabled plane far down the
path.

**Important details:** Fog colour must track the background colour or the scene separates from the
page. Fog is the cheapest available depth cue in 3D — it does more for perceived distance than
extra geometry. Rim lighting is what separates an object from fog; key light alone leaves forms
flat against it.

**License:** MIT.

---

## Parallax and depth of field

### Parallax

**Look up:** scroll-craft — `references/devices.md` §6 `parallax`

**What it demonstrates:** Layers translating at different rates to create depth, plus guidance on
composing a layered scene from back to front.

**How to reproduce:** Assign each layer a rate and write `rate × (p − 0.5) × 100px`. Plan planes
back to front and cut the foreground so it does not cover the subject's call to action.

**Important details:** The rate unit is hundreds of pixels, not viewport fractions, so travel is
screen-height independent. Beyond roughly 200px of total travel it stops reading as depth and
starts reading as a bug. Adjacent planes should differ by 10–30%; larger differences read as
things sliding around. Three layers is plenty, five is a diorama. Never put body copy on a
parallax layer. Two traps: a global `max-width: 100%` shrinks an absolutely positioned plane on
phones so the layer never shows, and a `transition: transform` on a parallax layer eases every
per-frame write over its duration — parallaxed elements should transition opacity only.

**License:** MIT.

### Depth of field with a travelling focus

**Look up:** animation-handbook — `animations/01-scroll-based/parallax-depth-of-field/`

**What it demonstrates:** Five planes at increasing depth, a focus value travelling from far to
near, and each plane blurred by its distance from that focus.

**How to reproduce:** Give each layer a depth (0 = far, 1 = near) and a speed. Drive a focus
value from scroll progress and blur each layer proportionally to `|depth − focus|`. Ease the
focus toward the scroll position each frame.

**Important details:** Snapping blur to 0.5px steps lets the compositor reuse a rasterised layer
instead of re-filtering several full-bleed planes every frame. Keep all layout reads out of the
scroll handler — each one forces a synchronous reflow before the style writes that follow. Add a
gradient floor over the section's bottom edge to hide where planes are clipped.

**License:** MIT.

---

## Frame sequences

### Frame-sequence scrolling

**Look up:** animation-handbook — `animations/01-scroll-based/scroll-image-sequence/`

**What it demonstrates:** A sequence of frames where scroll position selects the target frame, a
lerped playhead eases toward it, and each frame is drawn as a pure function of its index.

**How to reproduce:** Decide the frame count. Map scroll progress across a section to a target
frame index, ease a shown index toward it, and draw the rounded index. Cache the last drawn index
and skip the draw when it is unchanged.

**Important details:** Determinism matters more than fidelity: because each frame is a pure
function of its index, scrubbing backwards is exact. Round to an integer before drawing, or the
same frame is redrawn repeatedly. Only touch the canvas while it is near the viewport. Preloading
a real image sequence is the usual alternative, but a procedural frame avoids shipping assets.
Under reduced motion, either write the final frame immediately or let the section be static.

**License:** MIT.

---

## Typography

### Kinetic typography

**Look up:** scroll-craft — `references/devices.md` §5 `kinetic`; animation-handbook —
`animations/05-text-typography/kinetic-typography/`

**What it demonstrates:** Headings split into lines, words or characters and staggered across a
cue window, with each unit entering from behind a mask.

**How to reproduce:** Split the element, then stagger the resulting units on a scrubbed timeline.
Lines are the default unit.

**Important details:** Lines almost always read correctly; words suit a short punch line;
characters approximately never, because they turn reading into waiting. One kinetic headline per
act at most. Line splitting measures real line boxes, so re-split after `document.fonts.ready` —
splitting against a fallback face measures the wrong boxes. Character splitting must preserve an
accessible label for the whole phrase, or a screen reader announces the heading letter by letter.

**License:** MIT.

### Masked text reveals

**Look up:** scroll-craft — `references/devices.md` §5 and `references/hero-depth.md`

**What it demonstrates:** Units that slide up from behind an overflow-hidden mask, entering from a
clean edge rather than simply fading in.

**How to reproduce:** Wrap each split unit in an element with `overflow: hidden` and animate the
inner unit's vertical offset to zero. Reserve padding for descenders.

**Important details:** A mask clipped exactly to the line box shears the tails off g, y, p and j
— this is the most common way the effect looks broken. Give the mask room below the line.

**License:** MIT.

### Character-level animation

**Look up:** animation-handbook — `animations/05-text-typography/` (`text-morphing`, `glitch-text`,
`outline-to-fill`, `enter-exit-typography`)

**What it demonstrates:** Per-character state changes — morphing, glitching, outline-to-fill, enter
and exit — each driven by scroll position.

**How to reproduce:** Split to characters, then drive a per-character value from progress or from a
staggered timeline. Randomise per character with a seeded helper so reversals stay deterministic.

**Important details:** Turning characters into `inline-block` spans disables kerning and ligatures,
so split text measures a few percent wider than the original string. Line breaks therefore shift
once splitting is applied; force line breaks explicitly (`white-space: nowrap` per line, plus author
breaks honoured as intent) rather than letting the browser re-wrap. Measure the real rendered
characters when deciding line breaks — measuring plain text in an offscreen probe fits words that
do not actually fit. Screen readers must get the original string, not the split nodes.

**License:** MIT.

### Clip-path and sliced type

**Look up:** animation-handbook — `animations/05-text-typography/text-clip-path-reveal/`;
`animations/01-scroll-based/zoom-into-image/`

**What it demonstrates:** A wipe or slice revealing type, and a small window opening to fill a box
as scroll advances.

**How to reproduce:** Animate `clip-path: inset()` values on a wrapper, or use an SVG `clipPath`
referenced by CSS and animate the element inside it.

**Important details:** `clip-path` is relative to the border box, not the glyph ink. A reveal on
type set with tight line-height clips ascenders and descenders and every figure renders as a plain
bar; give the reveal element room or put it on a wrapper and leave the type's box alone. Display
numerals and drop figures are the usual casualties. No static audit catches this — only a rendered
screenshot does.

**License:** MIT.

### Text on a path

**Look up:** animation-handbook — `animations/05-text-typography/text-on-path/`; scroll-craft —
`references/devices.md` §6 (parallax composition)

**What it demonstrates:** Glyphs distributed along a measured curve.

**How to reproduce:** Measure the path length, then place units at intervals along it using
`getPointAtLength`, offsetting each by progress.

**Important details:** Screen CTM scaling shrinks labels sized in drawing units, so compute a scale
factor from the CTM if labels must stay a fixed pixel size. Re-measure on resize.

**License:** MIT.

---

## Glow

### Typography glow

**Look up:** animation-handbook — `animations/05-text-typography/kinetic-typography/`

**What it demonstrates:** A per-character `filter` animating blur and brightness to zero, with a
stagger. Because the filter is per character, glow intensity is a single number that can be driven
directly from scroll progress.

**How to reproduce:** Apply `blur()` and `brightness()` per character on a scrubbed timeline. Add a
`drop-shadow()` with a small blur radius for the halo, and drive its radius from progress.

**Important details:** Use `drop-shadow` rather than `text-shadow` when animating per character —
it follows the glyph's alpha and works on any font. `brightness()` is the half that makes this read
as ignition rather than as a fade: the character is genuinely dark, then lights. Glow should be
squared against whatever drives it, so it only appears near the peak rather than sitting at a
constant. Quantise the radius (0.5px) and the per-character state, or the DOM is written every
frame for no visible change. Under reduced motion, write the lit end state and stop.

**License:** MIT.

### Travelling glow

**Look up:** animation-handbook — `animations/03-page-transitions/` (dissolve, crossfade)

**What it demonstrates:** A shadow whose *offset* and colour both interpolate, so the light appears
to travel across the element rather than merely changing intensity.

**How to reproduce:** Interpolate a `drop-shadow` offset and colour from scroll progress. Pair it
with a colour change between two tones in the same family.

**Important details:** The offset is what creates the sense of travel; a colour-only change reads as
a tint. Give the travel a window long enough to be seen — a short window completes the change while
the section is still entering. Keep a colour-changing glow on its own window if a cut or veil also
occupies the same section, otherwise the cut lands while the colour is still mid-transition and
obscures the element it is meant to reveal.

**License:** MIT.

### Emissive WebGL glow

**Look up:** codrops-depth-gallery — `src/Experience/Gallery.js`, `src/Experience/Background/`

**What it demonstrates:** Lighting built so a few objects read as light sources — emissive
materials, a rim light, and a dim far plane for the fog to grade against.

**How to reproduce:** Give selected materials an emissive colour. Add a directional light from
behind or below the camera axis so edges separate from the background. Drive emissive intensity or
edge opacity from damped scroll velocity.

**Important details:** Mark only a few emitters. Glow applied to every object reads as noise and
gives the eye nothing to land on. Emissive intensity is the cheap way to make geometry glow without
a post-processing pass, and it survives camera movement. Prefer it to bloom when frame budget is
tight.

**License:** MIT.

### Bloom and post-processing

**Look up:** animation-handbook — `animations/06-3d-advanced/webgl-shader-animation/`,
`canvas-particle-effect/`, `gpgpu-particle-system/`

**What it demonstrates:** Luminous effects achievable directly in a fragment shader, without a
post-processing composer.

**How to reproduce:** For a glow, a single-pass composer with a bright-pass threshold followed by
a separable blur is the minimum. Set `threshold` high enough that only deliberately bright pixels
contribute. Drive bloom strength from an existing damped velocity value so the scene brightens
together with everything else on a fast scroll.

**Important details:** A bloom pass is roughly ten extra full-screen draws per frame. Measure on
the target hardware — it is negligible on a GPU and can drop a software-rendered page to a third
of its frame rate. Detect a software renderer at startup and skip the pass, since the emissive
geometry still carries the scene. Render the bloom at reduced resolution: it is a soft wide halo,
so the lost detail is invisible. Threshold is the parameter that matters; strength without it just
washes the frame.

**License:** MIT. Note that `pmndrs/postprocessing` is Zlib-licensed and provides bloom as a
composable pass, but it is a library rather than an example set.

---

## Transitions and atmosphere

### Cinematic transitions

**Look up:** scroll-craft — `references/devices.md` §4 `reveal` and §10 `drift`

**What it demonstrates:** A wipe as a change of state rather than an introduction, used big;
background colour shifts between acts so the page reads as one continuous place.

**How to reproduce:** Animate a `clip-path` wipe from an edge on a full-bleed element, triggered by
scroll position rather than a timer. Interpolate the page background colour between per-act stops.

**Important details:** A wipe that runs edge to edge across a full-bleed image is a transition; the
same wipe on a small element is a fidget. Use it big. Keep the transition window on the scroll
edge itself so it cuts where the reader put it and reverses perfectly. Reach for the loudest wipe
variant roughly once per page.

**License:** MIT.

### Ground / environment drift

**Look up:** scroll-craft — `references/devices.md` §10 `drift`

**What it demonstrates:** The page ground colour interpolating between per-act values, so the
environment shifts as the reader travels.

**How to reproduce:** Give each section a background colour. Interpolate toward the current
section's colour in the frame loop, and tint any 3D fog to match.

**Important details:** Keep the set inside one theme family; drifting from near-black to cream
mid-page reads as the reader wondering whether something was clicked. Three to five stops across
a page, small steps — invisible frame to frame, obvious top to bottom. If several short sections
can be part-way through at once, paint grounds per section with a hard edge instead: a cut is an
interpolation between two chapter grounds, and chaptered pages refuse that softness. Interpolate
per section when acts are long enough that only one is ever part-way through.

**License:** MIT.

---

## Reduced motion

**Look up:** scroll-craft — `references/verify.md`; animation-handbook — the
`prefers-reduced-motion` guards throughout its demos

**What it demonstrates:** Both reference sets honour `prefers-reduced-motion: reduce`, each
mechanism resolving to a static end state rather than being zeroed arbitrarily.

**How to reproduce:** Detect the media query once. Under reduced motion:
- write the end state of every reveal immediately, rather than scrubbing it;
- set playhead smoothing to no smoothing, so scroll maps 1:1;
- zero parallax offsets and focus shifts, but keep content readable;
- disable wipes, velocity-driven intensity and colour travel;
- keep essential state tied to scroll. If a rail's transform *is* the navigation, zeroing it
  parks the act on its first screenful and makes everything past the fold unreachable — convert
  it to a native scroll region instead.

**Important details:** Under reduced motion, decorative motion goes and information does not. A
reduced-motion path that leaves the headline invisible, or hides the mechanism that lets the
reader reach later content, is worse than no accessibility support at all. Verify the reduced
path by forcing it and checking each act still reads and each section is still reachable.

**License:** MIT.

---

## Verifying scroll work

**Look up:** scroll-craft — `references/verify.md` and `scripts/shoot.mjs`

**What it demonstrates:** Every scroll position is a different frame, so failures live between
the two frames that were inspected. The harness walks each act at several positions, waits for
scrubbed media to settle, and reports dead scroll and cues that never reach full opacity.

**How to reproduce:** For each act, capture screenshots at several scroll positions including both
ends. Assert programmatically that driven values move monotonically with progress — opacity, glow
radius, blur, frame index, camera position — rather than trusting a single screenshot. Check for
horizontal overflow after splitting text. Confirm every reveal reaches its end state, and that no
element overlaps its neighbour at the boundary between two acts.

**Important details:** Sample a boundary where one act hands off to the next; most real bugs live
there and are invisible in a single frame. Sample the *whole* range, not just the ends — a cue
window with a gap is only visible mid-range. Check reduced motion separately, since it takes a
different code path. A pinned stage's cues can ride the unpin slide onto the following section,
which no static screenshot of either act will show.

---

## Licensing and reuse

Every repository named above is MIT-licensed: `nateherkai/scroll-craft`,
`matinmonshizadeh/animation-handbook`, `houmahani/codrops-depth-gallery`, and the Codrops
organisation's demo repositories. MIT permits use, modification and redistribution with
attribution and without warranty. Verifying a licence means reading the repository's licence file
rather than trusting a topic tag or a README badge.

Repositories worth knowing about and their restrictions:

- **`greensock/GSAP`** — the reference for ScrollTrigger itself, but as of 2025 the repository
  carries no licence file. GSAP is available under its own terms through a CDN; confirm current
  terms before redistributing it in a product.
- **`vaneenige/scroll-transitions-webgl`** — the strongest WebGL scroll-transition demonstration
  available, but its licence forbids redistributing it "as-is" or selling unmodified copies. Study
  the technique; do not reuse the code.
- **`basementstudio/scrollytelling`** — a well-built GSAP scrollytelling library, React-only, and
  its licence metadata is `NOASSERTION`, meaning it could not be confirmed as permissive.
- **`pmndrs/postprocessing`** — Zlib-licensed bloom and post-processing for three.js. A library
  rather than an example set.
- Codrops repositories from before roughly 2022 often have no licence file at all. Absence of a
  licence is not permission; exclude them rather than assuming permissiveness.

Study a reference implementation to understand a mechanism, its parameter ranges and its failure
modes. Write the code yourself against your own scroll pipeline. Copying an example wholesale
inherits its dependencies, its assumptions about page structure, and any licence conditions.

---

## Quick lookup

- Smooth / lerped scroll playhead → scroll-craft, `devices.md` §1
- Scrubbed timeline both directions → animation-handbook, `01-scroll-based/scrub-animation/`
- Pinned section → scroll-craft, `devices.md` §2
- Cue windows and plateaus → scroll-craft, `devices.md` §2 "The cue contract"
- Seamless continuous world → scroll-craft, `worldflight.md`
- Cinematic camera on scroll → codrops-depth-gallery, `Scroll.js`
- Camera path between waypoints → codrops-depth-gallery, `Scroll.js`
- Camera travel bounded by scene → codrops-depth-gallery, `updateCameraBounds()`
- Scroll velocity → intensity → codrops-depth-gallery, `updateVelocity()`
- Fog and atmospheric depth → codrops-depth-gallery, `Background/index.js`
- Emissive / rim-lit glow → codrops-depth-gallery, `Gallery.js`, `Background/index.js`
- Parallax → scroll-craft, `devices.md` §6
- Parallax depth of field → animation-handbook, `parallax-depth-of-field/`
- Frame-sequence scrolling → animation-handbook, `scroll-image-sequence/`
- Scroll velocity skew → animation-handbook, `scroll-velocity-skew/`
- Kinetic typography → scroll-craft `devices.md` §5 / animation-handbook `kinetic-typography/`
- Masked text reveal → scroll-craft `devices.md` §5
- Clip-path typography → animation-handbook, `text-clip-path-reveal/`
- Character-level type animation → animation-handbook, `05-text-typography/`
- Text on a path → animation-handbook, `text-on-path/`
- Typography glow → animation-handbook, `kinetic-typography/`
- Blur / deblur typography → animation-handbook, `scrub-animation/`
- Travelling glow → animation-handbook, `03-page-transitions/`
- Bloom / post-processing → animation-handbook, `06-3d-advanced/`
- Cinematic wipe transition → scroll-craft, `devices.md` §4
- Ground / environment drift → scroll-craft, `devices.md` §10
- Reduced motion → scroll-craft `verify.md` / animation-handbook demo guards
- Verifying scroll positions → scroll-craft, `verify.md`, `scripts/shoot.mjs`