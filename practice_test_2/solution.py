import math, scipy.stats

def mean(samples: list) -> float:
    return sum(samples) / len(samples)

def std_dev(samples: list) -> float:
    n = len(samples)
    sum = 0
    coefficient = 1 / (n - 1)
    samples_mean = mean(samples)
    for x in samples:
        sum += (x - samples_mean) ** 2
    var = coefficient * sum
    std = math.sqrt(var)
    return std

def t_statistic(samples: list[float], mu0: float) -> float:
    n = len(samples)
    s = std_dev(samples)
    if s == 0:
        xbar = mean(samples)
        return round(math.inf if xbar > mu0 else (-math.inf if xbar < mu0 else 0.0), 4)
    t = (mean(samples) - mu0) / (s / math.sqrt(n))
    return round(t, 4)


def p_value(samples: list[float], mu0: float) -> float:
    """Return two-sided p-value for one-sample t-test, rounded to 4 dp."""
    # TODO
    n = len(samples)
    t = t_statistic(samples, mu0)
    p = 2 * (1 - scipy.stats.t.cdf(abs(t), df=n-1))
    return round(p, 4)

def reject_null(samples: list[float], mu0: float, alpha: float) -> bool:
    """Return True if p-value < alpha."""
    # TODO
    p = p_value(samples, mu0)
    return p < alpha
    
