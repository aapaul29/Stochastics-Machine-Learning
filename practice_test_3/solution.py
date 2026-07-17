import math, scipy.stats

def mean(samples: list[float]) -> float:
    return sum(samples) / len(samples)

def std_dev(samples):
    n = len(samples)
    coefficient  = 1 / (n - 1)
    samples_mean = mean(samples)
    sum = 0
    for x in samples:
        sum += (x - samples_mean) ** 2
    var = coefficient * sum
    std = math.sqrt(var)
    return std

def welch_t_statistic(xs: list[float], ys: list[float]) -> float:
    """Return Welch's t statistic, rounded to 4 dp."""
    # TODO
    m = len(xs)
    n = len(ys)
    x_mean = mean(xs)
    y_mean = mean(ys)
    s_x = std_dev(xs)
    s_y = std_dev(ys)
    t = (x_mean - y_mean) / math.sqrt((s_x ** 2 / m) + (s_y ** 2 / n))
    return round(t, 4)

def welch_p_value(xs: list[float], ys: list[float]) -> float:
    """Return two-sided p-value for Welch's t-test, rounded to 4 dp."""
    # TODO
    ## compute nu
    m = len(xs)
    n = len(ys)
    s_x = std_dev(xs)
    s_y = std_dev(ys)
    nu = ((s_x ** 2 / m) + (s_y ** 2 / n)) ** 2 / ((s_x ** 2 / m) ** 2/(m - 1) + (s_y ** 2 / n) ** 2 / (n - 1))
    
    t = welch_t_statistic(xs, ys)
    p = 2 * (1 - scipy.stats.t.cdf(abs(t), df=nu))
    return round(p, 4)

def reject_null(xs: list[float], ys: list[float], alpha: float) -> bool:
    """Return True if p-value < alpha."""
    # TODO
    p = welch_p_value(xs, ys)
    return p < alpha
