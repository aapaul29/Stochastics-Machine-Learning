import scipy.stats
import math


def welch_t_statistic(xs: list[float], ys: list[float]) -> float:
    """Return Welch t-statistic, rounded to 4 dp.
    Returns inf if denominator is 0 and means differ, 0.0 if means equal."""
    m, n = len(xs), len(ys)
    xbar = sum(xs) / m
    ybar = sum(ys) / n
    sx2 = sum((x - xbar) ** 2 for x in xs) / (m - 1) if m > 1 else 0.0
    sy2 = sum((y - ybar) ** 2 for y in ys) / (n - 1) if n > 1 else 0.0
    denom = math.sqrt(sx2 / m + sy2 / n)
    if denom == 0:
        return 0.0 if xbar == ybar else math.copysign(math.inf, xbar - ybar)
    return round((xbar - ybar) / denom, 4)


def _welch_dof(xs, ys):
    m, n = len(xs), len(ys)
    xbar = sum(xs) / m
    ybar = sum(ys) / n
    sx2 = sum((x - xbar) ** 2 for x in xs) / (m - 1) if m > 1 else 0.0
    sy2 = sum((y - ybar) ** 2 for y in ys) / (n - 1) if n > 1 else 0.0
    a, b = sx2 / m, sy2 / n
    if a + b == 0:
        return 1.0
    num = (a + b) ** 2
    den = (a ** 2 / (m - 1) if m > 1 else 0.0) + (b ** 2 / (n - 1) if n > 1 else 0.0)
    return num / den if den != 0 else 1.0


def welch_p_value(xs: list[float], ys: list[float]) -> float:
    """Return two-sided p-value for Welch t-test, rounded to 4 dp."""
    t = welch_t_statistic(xs, ys)
    if math.isinf(t):
        return 0.0
    nu = _welch_dof(xs, ys)
    return round(2 * (1 - scipy.stats.t.cdf(abs(t), df=nu)), 4)


def reject_null(xs: list[float], ys: list[float], alpha: float) -> bool:
    """Return True if we reject H0: mu_x = mu_y at significance level alpha."""
    return welch_p_value(xs, ys) < alpha
