import numpy as np

def ridge_regression(X: list[list[float]], y: list[float], lam: float) -> list[float]:
    """Return Ridge regression weights [w0, w1, ...] rounded to 4 dp.
    Prepends a bias column to X before solving."""
    # TODO
    X = np.array(X)
    y = np.array(y)
    n = X.shape[0]
    X_b = np.hstack([np.ones((n, 1)), X])
    d = X_b.shape[1]
    I = np.eye(d)
    w_star = np.linalg.inv(X_b.T @ X_b + lam * I) @ X_b.T @ y

    return [round(float(w), 4) for w in w_star]
