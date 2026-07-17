import numpy as np

def add_bias_column(X: list[list[float]]) -> list[list[float]]:
    """Prepend a column of 1.0 to each row of X."""
    return [[1.0] + list(row) for row in X]

def normal_equations(X: list[list[float]], y: list[float]) -> list[float]:
    """Return OLS weights [w0, w1, ...] rounded to 4 dp."""
    Xb = np.array(add_bias_column(X), dtype=float)
    yv = np.array(y, dtype=float)
    w, _, _, _ = np.linalg.lstsq(Xb, yv, rcond=None)
    return [round(float(wi), 4) for wi in w]
