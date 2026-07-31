import numpy as np

def add_bias_column(X: list[list[float]]) -> list[list[float]]:
    """Prepend a column of 1.0 to each row of X."""
    # TODO
    return [[1.0] + row for row in X]

def normal_equations(X: list[list[float]], y: list[float]) -> list[float]:
    """Return OLS weights [w0, w1, ...] rounded to 4 dp.
    Internally adds a bias column to X."""
    # TODO
    X = np.array(add_bias_column(X))
    y = np.array(y)
    w_star = np.linalg.pinv(X.T @ X) @ X.T @ y
    return np.round(w_star, 4).tolist()
