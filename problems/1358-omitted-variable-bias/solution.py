import numpy as np


def ols(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Least squares with an intercept.

    Args:
        X (np.ndarray): (n, p) design matrix without an intercept column.
        y (np.ndarray): (n,) target.

    Returns:
        np.ndarray: (p + 1,) coefficients, intercept first.
    """
    X_design = np.column_stack([np.ones(len(X)), X])

    beta, *_ = np.linalg.lstsq(X_design, y, rcond=None)
    return beta


def omitted_variable_bias(X: np.ndarray, y: np.ndarray, omit_idx: int) -> tuple:
    """Return (full_kept, short, bias) for a two-column X."""
    keep_idx = 0 if omit_idx else 1
    beta_full = ols(X, y)
    
    full_kept = beta_full[1 + keep_idx]
    gamma_omitted = beta_full[1 + omit_idx]

    X_short = X[:, [keep_idx]]
    beta_short = ols(X_short, y)
    short = beta_short[1]

    X_aux = X[:, [keep_idx]]
    y_aux = X[:, omit_idx]
    delta = ols(X_aux, y_aux)[1]

    bias = gamma_omitted * delta

    return full_kept, short, bias
