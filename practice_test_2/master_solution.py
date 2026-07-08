import scipy.stats
import math


def t_statistic(samples: list[float], mu0: float) -> float:
    """Return the one-sample t-statistic, rounded to 4 dp.
    Returns inf if s=0 and xbar != mu0, 0.0 if s=0 and xbar == mu0."""
    n = len(samples)
    xbar = sum(samples) / n
    var = sum((x - xbar) ** 2 for x in samples) / (n - 1) if n > 1 else 0.0
    s = math.sqrt(var)
    if s == 0:
        return 0.0 if xbar == mu0 else math.copysign(math.inf, xbar - mu0)
    return round((xbar - mu0) / (s / math.sqrt(n)), 4)


def p_value(samples: list[float], mu0: float) -> float:
    """Return the two-sided p-value, rounded to 4 dp."""
    n = len(samples)
    t = t_statistic(samples, mu0)
    if math.isinf(t):
        return 0.0
    return round(2 * (1 - scipy.stats.t.cdf(abs(t), df=n - 1)), 4)


def reject_null(samples: list[float], mu0: float, alpha: float) -> bool:
    """Return True if we reject H0: mu = mu0 at significance level alpha."""
    return p_value(samples, mu0) < alpha
