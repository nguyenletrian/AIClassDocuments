# Lab Math 03–04 — Store Matrix, Linear Systems, Ranking and PCA

> **English teaching edition reconstructed from notebook headings/code**, not a verbatim Word assignment translation. Store values and all four numbered tasks are taken from `2. Math/labs3_4.ipynb` (source snapshot 27 Oct 2026). Each English task is immediately followed by its annotated code solution.

**Prerequisites:** `python -m pip install numpy scikit-learn`. **Run:** `python SOLUTION_ANNOTATED.py`.

**Dataset:** Eight stores (A–H), columns: Orders (count), Customers (count), Revenue (currency units), Employees (count). Refer to [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) for the original eight data rows and detailed comments.

## Task 1 — Data Exploration and Matrix Creation

**English lab requirement:** Create an 8×4 NumPy matrix for Stores A–H containing orders, customers, revenue and employee counts. Display the matrix shape, all customer counts and their average.

**Annotated solution (run inside this folder):**

```python
from SOLUTION_ANNOTATED import task1_explore

# Slice column 1 (Customers) across every row; calculate the mean.
shape, customers, mean_customers = task1_explore()
print(shape, customers.tolist(), mean_customers)
```

**Why and how:** NumPy slicing uses `matrix[:, 1]` for every row of the Customers column. The complete implementation is fully commented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 2 — Finding Evaluation Weights Using a Linear System

**English lab requirement:** Given the 3×3 coefficient matrix A = [[3,4,10],[4,5,14],[2,2,7]] and scores b = [135,182,86], solve A·w=b and verify the resulting three weights.

**Annotated solution (run inside this folder):**

```python
from SOLUTION_ANNOTATED import task2_weights

# np.linalg.solve finds unique weights without manually inverting A.
weights = task2_weights()
print(weights)
```

**Why and how:** An invertible system gives a unique set of component weights. The complete implementation is fully commented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 3 — Calculating and Ranking Store Performance

**English lab requirement:** Convert Orders/100, Customers/100 and Revenue/10000 into three score components. Use matrix multiplication with w to score every store, rank them, and find the winner.

**Annotated solution (run inside this folder):**

```python
from SOLUTION_ANNOTATED import task2_weights, task3_rank

# Matrix multiplication combines eight rows with three weights.
components, totals, ranking, winner = task3_rank(weights=task2_weights())
print(ranking)
print('Winner:', winner)
```

**Why and how:** The fourth column (Employees) is not part of this weighted score; it is used in the next task. The complete implementation is fully commented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 4 — Data Standardization and Dimensionality Reduction Using PCA

**English lab requirement:** Standardize all four numeric store features, check that each standardized column has mean approximately 0 and variance approximately 1, reduce them to two principal components and report explained variance.

**Annotated solution (run inside this folder):**

```python
from SOLUTION_ANNOTATED import task4_pca

# StandardScaler removes incompatible scales; PCA returns two features.
scaled, projected, variance = task4_pca()
print('Projection shape:', projected.shape)
print('Retained variance:', variance.sum())
```

**Why and how:** `fit_transform` estimates and applies the feature scaling; `PCA(n_components=2)` keeps two orthogonal directions. In real predictive ML, fit scaling on training data only; here PCA is exploratory. The complete implementation is fully commented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Source and assumptions

Source: teacher notebook `nguyenletrian/PythoClass/2. Math/labs3_4.ipynb`, source commit `851d67d`. Original notebook provides the data and four numbered headings. These English requirements are faithful reconstructions of its actual code. Revenue is treated as a numeric amount with no invented currency, and the benchmark matrix A and b are supplied evaluation data rather than derived directly from the eight rows. There is no train/test split because this notebook is an exploratory PCA example.
