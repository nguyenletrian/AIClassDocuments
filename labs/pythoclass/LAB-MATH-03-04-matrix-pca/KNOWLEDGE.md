# Lab Math 03–04 — Matrices and PCA — Knowledge guide

## Important ideas

- **NumPy array:** a rectangular set of numerical observations. The sample has 8 rows and 4 features.
- **Column indexing `X[:, 1]`:** keep all rows and select the second column (Customers).
- **Linear system `A @ w = b`:** solve three equations for three weights using `np.linalg.solve`. The matrix must have full rank.
- **Matrix multiplication `S @ w`:** collapse three component scores per store into one weighted total.
- **Standardization:** center each feature and scale its variance to 1 so large currencies do not dwarf small count columns.
- **PCA:** project correlated standardized features onto orthogonal directions of maximal variance; `explained_variance_ratio_` reports retained variation.

See `docs/labs/LAB-MATH-03-04-matrix-pca/LAB_EN_SOLVED.md` for the English requirements and fully annotated solutions.
