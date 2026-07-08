import scipy.stats


def poisson_pmf(lam: float, k: int) -> float:
    """Return P(X = k) for X ~ Poisson(lam), rounded to 4 dp."""
    return round(float(scipy.stats.poisson.pmf(k, lam)), 4)


def poisson_cdf(lam: float, k: int) -> float:
    """Return P(X <= k) for X ~ Poisson(lam), rounded to 4 dp."""
    return round(float(scipy.stats.poisson.cdf(k, lam)), 4)


def poisson_approx_binomial(n: int, p: float, k: int) -> float:
    """Approximate P(Bin(n,p) = k) using Poisson(n*p), rounded to 4 dp."""
    return round(float(scipy.stats.poisson.pmf(k, n * p)), 4)
