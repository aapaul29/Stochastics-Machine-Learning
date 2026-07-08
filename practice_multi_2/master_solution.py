def empirical_covariance(xs: list[float], ys: list[float]) -> float:
    """Return unbiased sample covariance (divided by N-1), rounded to 4 dp.
    Return 0.0 if N <= 1."""
    n = len(xs)
    if n <= 1:
        return 0.0
    xbar = sum(xs) / n
    ybar = sum(ys) / n
    return round(sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / (n - 1), 4)


def empirical_correlation(xs: list[float], ys: list[float]) -> float:
    """Return Pearson correlation coefficient, rounded to 4 dp.
    Return 0.0 if either variance is zero."""
    n = len(xs)
    if n <= 1:
        return 0.0
    xbar = sum(xs) / n
    ybar = sum(ys) / n
    var_x = sum((x - xbar) ** 2 for x in xs) / (n - 1)
    var_y = sum((y - ybar) ** 2 for y in ys) / (n - 1)
    if var_x == 0 or var_y == 0:
        return 0.0
    cov = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / (n - 1)
    return round(cov / (var_x ** 0.5 * var_y ** 0.5), 4)
