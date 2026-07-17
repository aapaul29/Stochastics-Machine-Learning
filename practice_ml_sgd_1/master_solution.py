def sgd_update(w: list[float], b: float, x: list[float],
               y: float, alpha: float) -> tuple[list[float], float]:
    """Return (w_new, b_new) after one SGD step on sample (x, y)."""
    pred = sum(wi * xi for wi, xi in zip(w, x)) + b
    err  = pred - y
    new_w = [round(wi - alpha * 2 * err * xi, 6) for wi, xi in zip(w, x)]
    new_b = round(b - alpha * 2 * err, 6)
    return new_w, new_b
