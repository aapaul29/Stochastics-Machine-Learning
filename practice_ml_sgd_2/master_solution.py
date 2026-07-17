def poly_sgd_update(w: list[float], x: float, y: float, alpha: float) -> list[float]:
    """Return updated polynomial coefficients after one SGD step."""
    n = len(w)
    pred = sum(w[i] * x**i for i in range(n))
    err  = pred - y
    return [round(w[i] - alpha * 2 * err * x**i, 6) for i in range(n)]
