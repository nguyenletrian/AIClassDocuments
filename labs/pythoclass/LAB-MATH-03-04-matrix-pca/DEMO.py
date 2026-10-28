# Teacher notebook code cells copied into one Python file for reference only.
# Some cells prompt for user input or depend on earlier cells; this is not
# the polished solution. Use SOLUTION.py or docs/labs/<folder> instead.
# Source at 2026-10-27 snapshot: 2. Math/labs3_4.ipynb

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# ----- Next notebook cell -----

stores = np.array(["A", "B", "C", "D", "E", "F", "G", "H"])

X = np.array([
    [300, 400, 100000, 20],
    [400, 500, 140000, 25],
    [200, 200,  70000, 15],
    [500, 600, 180000, 30],
    [350, 450, 115000, 22],
    [450, 550, 160000, 28],
    [250, 300,  85000, 18],
    [600, 700, 210000, 35]
])

print("X: \n",X)
print("Shape of X:", X.shape)

# Extract Customers column (index 1)
customers = X[:, 1]
print("Customers:", customers)
print("Average number of customers:", np.mean(customers))

# ----- Next notebook cell -----

# Coefficient matrix
A = np.array([
    [3, 4, 10],
    [4, 5, 14],
    [2, 2,  7]
])

# Evaluation scores for stores A, B, and C
b = np.array([135, 182, 86])

# Solve the linear system A @ w = b
w = np.linalg.solve(A, b)

print("Coefficient matrix A: \n", A)
print("Result vector b:", b)
print("Weight vector w:", w)

# ----- Next notebook cell -----

# Convert Orders, Customers, and Revenue into component scores
S = np.column_stack((
    X[:, 0] / 100,
    X[:, 1] / 100,
    X[:, 2] / 10000
))
print("Component score matrix S: \n", S)

# Calculate total scores using matrix multiplication
total_scores = S @ w

print("Total scores:")
for i in range(len(stores)):
    print(f"Store {stores[i]}: {total_scores[i]:.2f}")

# Find the store with the highest score
best_index = np.argmax(total_scores)

print("Best-performing store:", stores[best_index])
print("Highest total score:", round(total_scores[best_index], 2))

# ----- Next notebook cell -----

# Standardize all four features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Standardized data:")
print(X_scaled)

print("Mean of standardized features:")
print(X_scaled.mean(axis=0))

print("Variance of standardized features:")
print(X_scaled.var(axis=0))

# Reduce the data to two principal components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Reduced data:")
print(X_pca)

print("Shape after PCA:", X_pca.shape)

print("Explained variance ratio:")
print(pca.explained_variance_ratio_)

print(
    "Total explained variance: "
    f"{pca.explained_variance_ratio_.sum() * 100:.2f}%"
)
