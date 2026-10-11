# Jetking 4371618 — post-restart Edge source probe (2026-10-11)

## Evidence received

- Task: `aiclassdocuments-jetking4371618-postrestart-readonly-probe-20261011`; Bridge returned `success: true` for the transport.
- `read_web_connection`: `127.0.0.1:9223`, actual worker-owned Edge CDP endpoint.
- Mode: `target_mode=temporary`, `extractor=page_text`; temporary source tab was closed and Architect ChatGPT tab preserved.
- Source: `https://www.jetking.co/learn/home/VN-course?lessonId=4371618`; title `Jetking`.
- DOM: `readyState=complete`, `bodyPresent=true`, `bodyTextLength=2761`, `iframeCount=0`, `videoCount=0`; `extraction_state=text_ready`, 13 observations.
- Page chrome shows course `Advanced Diploma in AI Agent`, module `Maths, Statistics and Probability for Machine Learning`, and `Slides lesson` with `Page 1 / 44`.
- Some visible headings are recognizable (e.g. `Foundations of Mathematics for ML`), but the PDF/slide text is severely interleaved/reordered (example: `iotrm rfeitj nntiMgthumaetaera`), and the result is capped.

## Architect assessment

**Transport/access probe succeeded; lesson-content extraction failed quality validation.**
The `text_ready` signal proves repeated DOM snapshots stabilized, not legibility, full lesson capture, or correctness. Only slide 1 was observed; there is **no evidence** the other 43 slides, lesson audio/video, or examples were reviewed.

Therefore the source state remains `AWAITING_SOURCE`, not `SOURCE_READY`. No bilingual lesson document should be generated from this malformed extraction.

## Recommended next bounded probe

1. Enhance AIBrigde with a read-only, bounded DOM layout diagnostic for the slide viewer (bounding rectangles, text spans, and visible page indicator), without reading credentials or protected media APIs.
2. Identify whether text runs can be correctly ordered by their on-screen coordinates. When not possible, use owner-approved visible screenshot/notes or transcript rather than fabricating slide text.
3. Verify one slide's extracted content against what the owner sees before attempting page-by-page acquisition; comply with Jetking access and usage rights.
4. Preserve the authorized Edge session and ChatGPT tab; do not automatically click download, extract cookies, or bypass site protection.
5. Mark `SOURCE_READY` only after traceable, legible source text/images have actually been reviewed. Then produce independent English and Vietnamese instructional summaries.

This assessment acknowledges the Bridge transport task as completed; **it does not approve the lesson source**.
