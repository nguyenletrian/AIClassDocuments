"""Lab Math 03-04 — store evaluation using matrices, linear systems and PCA.

Adapted from 2. Math/labs3_4.ipynb. Run:
    python SOLUTION_ANNOTATED.py

Requires numpy and scikit-learn; prints results without opening a GUI.
"""
import numpy as np  # Arrays, descriptive statistics and matrix multiplication.
from sklearn.preprocessing import StandardScaler  # Scale each feature.
from sklearn.decomposition import PCA  # Reduce correlated features to 2 axes.

# Rows A-H represent stores. Each column has a specified real-world unit:
# Orders (count), Customers (count), Revenue (currency units), Employees (count).
STORE_NAMES = np.array(list("ABCDEFGH"))
STORE_DATA = np.array([
    [300, 400, 100000, 20],
    [400, 500, 140000, 25],
    [200, 200, 70000, 15],
    [500, 600, 180000, 30],
    [350, 450, 115000, 22],
    [450, 550, 160000, 28],
    [250, 300, 85000, 18],
    [600, 700, 210000, 35],
], dtype=float)  # Shape (8,4), with numeric values compatible with NumPy.

# A and b are supplied evaluation coefficients and observed benchmark scores.
EQUATION_MATRIX = np.array([[3, 4, 10], [4, 5, 14], [2, 2, 7]], dtype=float)
EQUATION_SCORES = np.array([135, 182, 86], dtype=float)


def task1_explore(stores=STORE_DATA):
    """Inspect matrix dimensions, customer counts and mean customer traffic."""
    if stores.ndim != 2 or stores.shape[1] != 4:
        raise ValueError("Expect a matrix with four store features.")
    customers = stores[:, 1]  # ':' means all rows; index 1 is Customers.
    mean_customers = float(np.mean(customers))  # Mean over all eight stores.
    return stores.shape, customers, mean_customers


def task2_weights(A=EQUATION_MATRIX, b=EQUATION_SCORES):
    """Solve A @ w = b for weights of Orders, Customers and Revenue."""
    # np.linalg.solve avoids manually computing the matrix inverse.
    if A.shape != (3, 3) or b.shape != (3,):
        raise ValueError("Expected a 3x3 matrix and a three-element score vector.")
    if np.linalg.matrix_rank(A) < 3:  # A singular matrix has no unique answer.
        raise ValueError("The benchmark system has no unique solution.")
    weights = np.linalg.solve(A, b)
    assert np.allclose(A @ weights, b)  # Reconstruct the input equations.
    return weights


def task3_rank(stores=STORE_DATA, names=STORE_NAMES, weights=None):
    """Build dimensionless components, combine weights, rank all stores."""
    if weights is None:
        weights = task2_weights()
    # Scale columns as in the original notebook before applying weights.
    components = np.column_stack((
        stores[:, 0] / 100,  # One score unit per 100 orders.
        stores[:, 1] / 100,  # One score unit per 100 customers.
        stores[:, 2] / 10000,  # One score unit per 10,000 revenue units.
    ))
    totals = components @ weights  # (8x3) @ (3,) -> eight store scores.
    ranked = sorted(zip(names.tolist(), totals.tolist()),
                    key=lambda pair: (-pair[1], pair[0]))
    winner_index = int(np.argmax(totals))  # Index of highest score.
    return components, totals, ranked, names[winner_index]


def task4_pca(stores=STORE_DATA):
    """Standardize four columns, then project stores onto two PCA axes."""
    # Different units (currency, people) must not bias distance by magnitude.
    scaler = StandardScaler()  # By default centers and scales each column.
    standardized = scaler.fit_transform(stores)
    # PCA finds directions containing the largest variation in scaled data.
    pca = PCA(n_components=2)  # We want a shape of (8 stores, 2 axes).
    projected = pca.fit_transform(standardized)
    retained = pca.explained_variance_ratio_  # Fraction on each retained axis.
    assert projected.shape == (stores.shape[0], 2)
    assert np.allclose(standardized.mean(axis=0), 0, atol=1e-12)
    assert np.allclose(standardized.var(axis=0), 1, atol=1e-12)
    assert np.isfinite(projected).all()
    return standardized, projected, retained


def main():
    """Print intermediate results for every English task and check shapes."""
    shape, customers, mean_customers = task1_explore()
    print("Task 1 - Store matrix shape:", shape)
    print("Customers:", customers.astype(int).tolist())
    print("Mean customers:", round(mean_customers, 2))

    weights = task2_weights()
    print("Task 2 - Weights:", np.round(weights, 6).tolist())

    components, scores, ranking, best = task3_rank(weights=weights)
    print("Task 3 - Component matrix shape:", components.shape)
    print("Scores:", np.round(scores, 2).tolist())
    print("Ranking:", [(name, round(score, 2)) for name, score in ranking])
    print("Best store:", best)

    standardized, projection, ratios = task4_pca()
    print("Task 4 - Standardized shape:", standardized.shape)
    print("PCA projected shape:", projection.shape)
    print("Explained variance fractions:", np.round(ratios, 4).tolist())
    print("Total variance retained:", f"{ratios.sum() * 100:.2f}%")
    assert len(ranking) == len(STORE_NAMES)
    assert projection.shape == (8, 2)


if __name__ == "__main__":
    main()  # Execute this demonstration only when launched as a script.
