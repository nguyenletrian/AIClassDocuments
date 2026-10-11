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
