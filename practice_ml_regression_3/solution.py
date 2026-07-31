def mse(y_true: list[float], y_pred: list[float]) -> float:
    """Mean Squared Error, rounded to 4 dp."""
    # TODO
    n = len(y_true)
    mse = 0
    for i in range(n):
        mse += 1 / n * (y_true[i] - y_pred[i]) ** 2
    return round(mse, 4)

def r_squared(y_true: list[float], y_pred: list[float]) -> float:
    """Coefficient of determination R², rounded to 4 dp."""
    # TODO
    true_mean = sum(y_true) / len(y_true)
    numerator = 0
    denominator = 0
    for i in range(len(y_true)):
        numerator += (y_true[i] - y_pred[i]) ** 2
        denominator += (y_true[i] - true_mean) ** 2
    if denominator == 0:
        return 1.0
    r_squared = 1 - numerator/ denominator
    return round(r_squared, 4)
    
