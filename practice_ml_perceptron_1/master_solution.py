def perceptron_predict(w: list[float], b: float, x: list[float]) -> int:
    """Return +1 if w·x + b >= 0, else -1."""
    return 1 if sum(wi * xi for wi, xi in zip(w, x)) + b >= 0 else -1

def perceptron_update(w: list[float], b: float, x: list[float],
                      y: int, alpha: float) -> tuple[list[float], float]:
    """Apply perceptron update if misclassified."""
    if perceptron_predict(w, b, x) == y:
        return list(w), b
    new_w = [round(wi + alpha * y * xi, 6) for wi, xi in zip(w, x)]
    new_b = round(b + alpha * y, 6)
    return new_w, new_b
