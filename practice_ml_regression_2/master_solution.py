import numpy as np

def ridge_regression(X: list[list[float]], y: list[float], lam: float) -> list[float]:
    """Return Ridge regression weights [w0, w1, ...] rounded to 4 dp."""
    Xb = np.column_stack([np.ones(len(X)), np.array(X, dtype=float)])
    yv = np.array(y, dtype=float)
    d  = Xb.shape[1]
    w  = np.linalg.solve(Xb.T @ Xb + lam * np.eye(d), Xb.T @ yv)
    return [round(float(wi), 4) for wi in w]
