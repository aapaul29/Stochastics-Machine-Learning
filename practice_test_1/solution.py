import scipy.stats
import math

def mean(samples):
    return sum(samples) / len(samples)

def confidence_interval(samples: list[float], sigma: float, alpha: float) -> tuple[float, float]:
    """Return (lo, hi) confidence interval for the mean, each rounded to 4 dp."""
    # TODO
    n = len(samples)
    sample_mean = mean(samples)
    ppf = scipy.stats.norm.ppf(1 - alpha / 2)
    lo = sample_mean - ppf * sigma / math.sqrt(n)
    hi = sample_mean + ppf * sigma / math.sqrt(n)

    return (round(lo, 4), round(hi, 4))
