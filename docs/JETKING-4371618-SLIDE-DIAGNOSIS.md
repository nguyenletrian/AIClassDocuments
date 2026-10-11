# Jetking lesson 4371618 — first slide-layout probe and next validation gate

Date: 2026-10-11

## Observed worker result

Task: `aiclassdocuments-jetking4371618-slide-layout-probe-20261011`

- `success=true` describes a successful transport/diagnostic invocation, **not**
  successful source extraction or lesson reading.
- Actual worker-managed Edge CDP endpoint: `127.0.0.1:9223`.
- `target_mode=temporary`; Bridge closed only its temporary lesson tab, preserving
  the Architect ChatGPT tab.
- `probe=slide_layout_probe_v1`, `state=no_visible_slide_layer`,
  `textLayerCount=0`, `visibleCanvasCount=0`,
  `visibleTextSpanCount=0`, `pageIndicator=null`.
- `domOrderPreview` and `visualOrderPreview` were empty.
- An earlier, independently completed `page_text` probe had displayed Jetking
  lesson text, course heading and slide counter `Page 1 / 44`, but the text
  ran together and was not a reliable lesson transcription.

## Interpretation

The missing page counter in this second result means that **early SPA
hydration remains a possible explanation**; a false zero cannot prove the
Jetking slide viewer is inaccessible or textless. Alternatively, the viewer
may render slide text in non-PDF DOM nodes. Neither hypothesis has been
verified. The lesson remains **AWAITING_SOURCE**.

## Approved bounded next check

AIBrigde shared commit `185b1b3480aa25d7e5a4f88d8df007dac3a96998`
(PR #6) adds a hydration-aware, bounded, read-only slide diagnostic.
After managed restart, run **one** `slide_layout_probe` in a temporary
CDP tab, and inspect: `extraction_state`, `observation_count`,
`pageIndicator`, `bodyTextLength`, `textLayerCount`,
`genericTextNodeCount`, `genericVisualOrderPreview` and
`visibleSlideContainers`. It must not click, turn slides, download video,
access cookies or tokens, or preserve copyrighted source passages in Git.

Only when the page has been observed and its text can be independently
checked for correctness should the next source-collection step be designed.
Do not publish bilingual learning documents as lesson-grounded before then.

If the result is `viewer_not_hydrated`, do **not** repeat the same
temporary-tab probe automatically. The owner may need to open the lesson
in the managed Edge profile and provide a visible slide or permitted notes.


## Second bounded probe — hydrated viewer (2026-10-11)

Task: `aiclassdocuments-jetking4371618-hydrated-dom-probe-20261011`.
The Bridge delivered the **same** successful result three times with the
same `delivery_id=55b29e22c93bae242856`. It is a duplicate delivery, **not**
three independent slide observations. The Architect recorded one result
and acknowledged the task once; no replacement task is queued.

- Edge CDP `127.0.0.1:9223`, `browser_relaunched=false`.
- `read_web_temp_closed=true` and Architect ChatGPT URL unchanged.
- `domReadyState=complete`, `extraction_state=viewer_dom_stable`,
  `observation_count=17`, `bodyTextLength=2761`.
- `pageIndicator={current:1,total:44}`; only **slide 1** was observed.
- `state=visible_text_layer`, `textLayerCount=2`,
  `visibleTextSpanCount=7`, `visibleCanvasCount=2`;
  `genericTextNodeCount=15`.
- Both DOM order and coordinate-sorted visual previews remain
  **unreadable/interleaved**. A minimal diagnostic example is
  `del1uo M` (do not infer the original source text).
- Ordinary HTML course navigation names the topic
  `1. Foundations of Mathematics for ML`; this metadata does not
  establish what the 44 slides say.

**Diagnosis:** initial all-zero result was consistent with premature SPA
inspection, now resolved by the hydration wait. However the readable-text
problem persists despite PDF-style geometry and generic DOM fallback.
Neither visual coordinate sorting nor the stabilizing wait reliably
reconstructs the lesson. Transport success is not source-content success.

**Decision:** keep `sources/lesson-index.csv` at `AWAITING_SOURCE`.
No word reconstruction by guessing, no automated iteration over 44 slides,
and no supposedly lesson-grounded English/Vietnamese documents yet.

**Next validation gate:** independently inspect a single **rendered**
first-slide visual or owner-provided authorized source notes/transcript,
then compare the visual against extracted text. Any screenshot should be
owner-approved, limited to the currently visible first slide, processed
privately rather than checked into the public Git repository, and comply
with the Jetking course's applicable access/use restrictions. If readable
visual or permitted transcript is unavailable, stop at `AWAITING_SOURCE`.
