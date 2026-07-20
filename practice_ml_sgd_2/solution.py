def polynomial(w: list[float], x: float) -> float:
    ip = 0
    for i in range(len(w)):
        ip += w[i] * x ** i
    return ip


def poly_sgd_update(w: list[float], x: float, y: float, alpha: float) -> list[float]:
    """Return updated polynomial coefficients after one SGD step.
    Each coefficient rounded to 6 decimal places."""
    # TODO
    w_new = []
    for i in range(len(w)):
        gradient = 2 * (polynomial(w, x) - y) * x ** i
        w_i = w[i] - alpha * gradient
        w_new.append(w_i)

    return w_new
