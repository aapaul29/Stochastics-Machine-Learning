def mse(y_true: list[float], y_pred: list[float]) -> float:
    """Mean Squared Error, rounded to 4 dp."""
    n = len(y_true)
    return round(sum((a - b) ** 2 for a, b in zip(y_true, y_pred)) / n, 4)

def r_squared(y_true: list[float], y_pred: list[float]) -> float:
    """R², rounded to 4 dp."""
    n = len(y_true)
    mean_y = sum(y_true) / n
    ss_res = sum((a - b) ** 2 for a, b in zip(y_true, y_pred))
    ss_tot = sum((a - mean_y) ** 2 for a in y_true)
    if ss_tot == 0:
        return 1.0 if ss_res == 0 else 0.0
    return round(1 - ss_res / ss_tot, 4)
