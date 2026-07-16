import scipy.stats

def standardize(x: float, mu: float, sigma: float) -> float:
    """Return (x - mu) / sigma, rounded to 4 decimal places."""
    # TODO
    standardized = (x - mu) / sigma
    return round(standardized, 4)

def normal_prob(mu: float, sigma: float, a: float, b: float) -> float:
    """Return P(a <= X <= b) for X~N(mu, sigma^2), rounded to 4 dp."""
    # TODO
    prob = scipy.stats.norm.cdf(standardize(b, mu, sigma)) - scipy.stats.norm.cdf(standardize(a, mu, sigma))
    return round(prob, 4)

def normal_quantile(mu: float, sigma: float, p: float) -> float:
    """Return the p-quantile of N(mu, sigma^2), rounded to 4 dp."""
    # TODO
    quantile = scipy.stats.norm.ppf(p, mu, sigma)
    return round(quantile, 4)
