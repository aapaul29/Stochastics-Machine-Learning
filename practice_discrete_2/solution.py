import scipy.stats

def binomial_pmf(n: int, p: float, k: int) -> float:
    """Return P(X=k) for X~Bin(n,p), rounded to 4 decimal places."""
    # TODO
    return round(scipy.stats.binom.pmf(k, n, p), 4)


def binomial_cdf(n: int, p: float, k: int) -> float:
    """Return P(X<=k) for X~Bin(n,p), rounded to 4 decimal places."""
    # TODO
    return round(scipy.stats.binom.cdf(k, n, p), 4)

def binomial_mean_variance(n: int, p: float) -> tuple[float, float]:
    """Return (E[X], Var(X)) for X~Bin(n,p), each rounded to 4 dp."""
    # TODO
    return (round(n * p, 4), round(n * p * (1 - p), 4))
