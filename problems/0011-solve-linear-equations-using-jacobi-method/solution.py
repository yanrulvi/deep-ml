import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float).ravel()

    D = np.diag(A)
    R = A - np.diag(D)

    x = np.zeros_like(b, dtype=float)

    for _ in range(n):
        x = (b - R @ x) / D

    return x.tolist()