import math, scipy.stats

def mean(samples: list) -> float:
    return scipy.stats.mean(samples)

def std_dev(samples: list) -> float:
    return scipy.stats.std(samples)

def t_statistic(samples: list[float], mu0: float) -> float:
    """Return t = (xbar - mu0) / (s / sqrt(n)), rounded to 4 dp."""
    # TODO
    n = len(samples)
    t = (mean(samples) - mu0) / std_dev(samples) / math.sqrt(n)
    return round(t, 4)

def p_value(samples: list[float], mu0: float) -> float:
    """Return two-sided p-value for one-sample t-test, rounded to 4 dp."""
    # TODO
    return -1.0

def reject_null(samples: list[float], mu0: float, alpha: float) -> bool:
    """Return True if p-value < alpha."""
    # TODO
    return False
