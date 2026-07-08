import scipy.stats


def standardize(x: float, mu: float, sigma: float) -> float:
    """Return (x - mu) / sigma, rounded to 4 dp."""
    return round((x - mu) / sigma, 4)


def normal_prob(mu: float, sigma: float, a: float, b: float) -> float:
    """Return P(a <= X <= b) for X ~ N(mu, sigma^2), rounded to 4 dp."""
    return round(scipy.stats.norm.cdf(b, mu, sigma) - scipy.stats.norm.cdf(a, mu, sigma), 4)


def normal_quantile(mu: float, sigma: float, p: float) -> float:
    """Return the p-quantile of N(mu, sigma^2), rounded to 4 dp."""
    return round(scipy.stats.norm.ppf(p, mu, sigma), 4)
