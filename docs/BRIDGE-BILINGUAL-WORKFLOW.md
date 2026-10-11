# AI Bridge + Edge — Bilingual course documents

## Target
Use the owner's authorized Microsoft Edge session to study a Jetking lesson, then generate two independently readable instructional documents: English and Vietnamese. Never assume that an Edge browser session is accessible merely because AI Bridge is running.

## Preconditions
1. Owner starts AI Bridge and explicitly enables access to the correct Edge session.
2. Confirm a functioning execution channel (Bridge endpoint/tool and expected protocol), identify the intended browser window, and obtain the owner's approval for session use.
3. Owner logs in directly; do not request passwords, cookies, session tokens or MFA codes to be copied into prompts/repository.
4. Confirm material access and permissions before extracting notes/transcripts; observe website restrictions.

## Lesson contract
- `lesson_id`: 4371618
- `course_url`: https://www.jetking.co/learn/home/VN-course?lessonId=4371618
- `source_access`: browser-based, authorized
- `languages`: `en`, `vi`
- `output`: `lessons/4371618-<slug>.en.md`, `lessons/4371618-<slug>.vi.md`
- `status`: `AWAITING_SOURCE` until actual material reviewed.

## Edge source probe (2026-10-11 update)

The shared `AIBrigde` `browser:read_web` implementation supports
`payload.target_mode: "existing_url"` after
[Edge browser enhancement](https://github.com/nguyenletrian/AIBrigde/pull/2).

Before queuing a new source probe, confirm:

1. The AIBrigde worker has refreshed to a commit containing the enhancement
   (merged into `main` at `ab0901174d3895117ab53f86a728174812a79b03`).
2. The lesson is already open **once**, at the exact requested URL, in the
   worker-owned CDP Edge profile. The owner logs in directly.
3. The project's browser CDP host/port are confirmed from the worker's actual
   `AIBRIDGE_DEBUG_PORT` / profile settings, not inferred from
   `execution_target.port` or `delivery_target.port`.
4. Only then schedule one read-only task with:
   `{"url":"https://www.jetking.co/learn/home/VN-course?lessonId=4371618","extractor":"page_text","target_mode":"existing_url","provider":"OpenAI","via":"web"}`.
5. `read_web_result.extraction_state == "text_ready"` only shows top-level
   page text has stabilized; it does not prove actual lesson/audio/video was
   reviewed. Verify content relevance and access before moving
   `AWAITING_SOURCE -> SOURCE_READY`.

If there is no matching tab, duplicate matching tabs, empty text, or an
unreviewable media-only page, preserve `AWAITING_SOURCE`. Do not retry blindly
or send repeated `queue_exhausted` requests.

## Execution steps
1. Bridge opens the authorized URL in Edge and identifies the lesson title and available content.
2. Capture permitted notes and transcript/visible text with section references/timestamps if available. If content is inaccessible, stop and report the blocker.
3. Build a grounded lesson outline; distinguish concepts from the video, instructor examples, and original explanations from the AI.
4. Draft English document with `templates/lesson.en.md`.
5. Draft Vietnamese document with `templates/lesson.md`. Preserve topic parity, vocabulary, facts and exercises.
6. Run quality checks: source fidelity, terminology, missing topics, code/example correctness, bilingual parity, language fluency.
7. Create Markdown files and update `sources/lesson-index.csv` and revision history. Export DOCX/PDF when requested.
8. Report `READY_FOR_OWNER_TEST` only after both documents pass checks.

## Safety/rights
- Avoid bulk downloading, DRM circumvention and access bypass.
- Do not store session information, full copied course materials or private recordings in GitHub.
- Documents should be original explanatory notes/summaries, not substitute copies or extensive translated reproductions of restricted course content without authorization.
- Keep commands bounded and review outputs prior to commits.
