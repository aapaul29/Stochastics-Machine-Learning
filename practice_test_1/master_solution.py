import scipy.stats
import math


def confidence_interval(samples: list[float], sigma: float, alpha: float) -> tuple[float, float]:
    """Return (lo, hi) for a (1-alpha) CI for the mean with known sigma, each rounded to 4 dp."""
    n = len(samples)
    xbar = sum(samples) / n
    z = scipy.stats.norm.ppf(1 - alpha / 2)
    margin = z * sigma / math.sqrt(n)
    return round(xbar - margin, 4), round(xbar + margin, 4)
