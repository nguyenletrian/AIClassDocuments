# Curriculum QA and source-coverage status — 24/10/2026

## Deliverables created

- **46 chapter drafts** at `lessons/chapters/PY-01-*.vi.md` through `PY-46-*.vi.md` plus the existing **PCA pilot** at `lessons/pilot/AI-MATH-01-pca.vi.md`.
- Ordered `lessons/chapters/README.md` index into seven knowledge groups.
- Fixed 20 PCA questions and 80 answer options to appear in **one-line English — Vietnamese** format, e.g. `**Q1. What...? — Nghĩa tiếng Việt?**` and `A. English — Tiếng Việt`.
- **Permanent authoring contract:** `docs/CURRICULUM-STYLE-GUIDE.md`, linked from `AGENTS.md` and `templates/lesson.md`, required **before writing every future chapter**.
- Independent source ledger `sources/curriculum-source-coverage.csv` pinned to latest source revision (2026-10-24), hidden from student-facing lessons.

## What has actually been checked

A full 46-file GitHub source inspection checked the following **structural invariants**:

| Gate | Recorded outcome |
|---|---|
| 46 uniquely numbered Markdown chapters | 46/46 structurally present |
| 4 small concept sections in each generated chapter | 46/46 |
| 5 scenario headings per chapter | 46/46 |
| 20 English–Vietnamese MCQ questions per chapter | 46/46 |
| 80 same-line bilingual answer options per chapter | 46/46 |
| 20 answer-key rows per chapter | 46/46 |
| Python blocks, or Bash blocks for Git chapter | 9 illustrative snippets per chapter |
| Student-facing references to source repository | Generation contract disallows them; enforce again with automated test |

**These are structural checks, not an endorsement that every answer, translation, API, code output or pedagogical explanation is correct.** Newly generated lessons remain labeled `DRAFT`, not `CODE_VERIFIED` or `APPROVED`. A reusable `tests/test_curriculum_structure.py` has been added for later execution; **no successful Windows execution or GitHub Actions run is claimed**. Review the English quality and answer distractors, particularly those mechanically generated, before publishing to students.

## Source evidence and unreviewed files

Latest source repository revision: `nguyenletrian/PythoClass`, commit `37bcd2358ed616a9130ef954913adef728a1f9b8` (source file inventory grew from 65 to **68** files while this work was underway).

According to `sources/curriculum-source-coverage.csv`:

- 36 files: code/notebook **excerpts examined** for identifying concepts. This does **not** mean all cells were reviewed for correctness.
- 16: **pending deeper review**.
- 11: **binary unread** (DOCX/PPTX/XLSX/image) — GitHub `fetch_file` could not decode some DOCX bytes as UTF-8; content not inspected and additional topics in these may be missing.
- 3: **CSV schema unverified**.
- 2: **zero-byte** notebooks.

The 46 drafted chapters cover broad visible topic families, but **coverage of every single concept in all 68 files is not yet substantiated**. Before release, parse remaining binary materials with the appropriate office/document parsers, reconcile previously unread text/code and map any new minor concepts into the chapter index.

## Release readiness checklist

- [x] Same-line bilingual quiz standard recorded as durable guide
- [x] PCA quiz same-line format corrected and pilot images retained
- [x] 46 draft chapters created
- [x] Chapter index and internal source ledger created
- [x] Automated structure/syntax test authored
- [ ] Execute structure/syntax test and all code examples on supported Python environments
- [ ] Check math/API accuracy, English translations and correct quiz answers
- [ ] Complete binary/source reading and concept-by-concept coverage
- [ ] Add/verify chapter-specific illustrations wherever they materially aid comprehension
- [ ] Mark individual chapters `CODE_VERIFIED`, `EDITOR_REVIEWED`, then `APPROVED`
- [ ] When requested, export PDFs into `exports/pdf/` and visually inspect rendered pages

The Bridge worker goal remains **message review disabled** to prevent idle heartbeat spam; the old 18 task ACKs are untouched. The user's permission to draft the full curriculum is not permission to claim unrun tests passed.
