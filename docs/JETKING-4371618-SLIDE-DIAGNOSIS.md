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
