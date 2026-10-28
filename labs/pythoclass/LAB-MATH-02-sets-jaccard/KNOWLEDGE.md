# Lab Math 02 — Sets and Jaccard — Knowledge guide

## Important ideas

- **Set:** collection of unique items, appropriate for course membership without duplicates.
- **Intersection (`&`):** subjects in both students' lists.
- **Union (`|`):** all subjects in either list, without repetition.
- **Difference (`-`):** subjects only in the first student's set.
- **Jaccard similarity:** intersection size divided by union size; results are between 0 and 1. A zero-size union must be handled.
- **`itertools.combinations(students, 2)`:** visits each unordered distinct pair only once.
- **Adjacency list:** a dictionary mapping each student to connected students. Undirected connections are stored twice, once at each endpoint.

See `docs/labs/LAB-MATH-02-sets-jaccard/LAB_EN_SOLVED.md` for each requirement with an explained solution immediately below.
