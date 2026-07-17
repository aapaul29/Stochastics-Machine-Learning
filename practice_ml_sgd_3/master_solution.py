def minibatch_sgd_step(w: list[float], b: float,
                       X_batch: list[list[float]], y_batch: list[float],
                       alpha: float) -> tuple[list[float], float]:
    """One mini-batch gradient descent step."""
    m = len(X_batch)
    d = len(w)
    grad_w = [0.0] * d
    grad_b = 0.0
    for x, y in zip(X_batch, y_batch):
        err = sum(w[j]*x[j] for j in range(d)) + b - y
        for j in range(d):
            grad_w[j] += 2 * err * x[j]
        grad_b += 2 * err
    new_w = [round(w[j] - alpha * grad_w[j] / m, 6) for j in range(d)]
    new_b = round(b - alpha * grad_b / m, 6)
    return new_w, new_b
