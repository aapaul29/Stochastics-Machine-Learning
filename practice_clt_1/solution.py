import scipy.stats
import math

def standardized(distribution, a, n):
    Z = (a - n * distribution.mean()) / (math.sqrt(n) * distribution.std())
    return Z

def clt_mean(distribution, n: int) -> float:
    """Return E[S_n] = n * E[X], rounded to 4 dp."""
    # TODO
    clt_mean = distribution.mean() * n
    return round(clt_mean, 4)

def clt_variance(distribution, n: int) -> float:
    """Return Var(S_n) = n * Var(X), rounded to 4 dp."""
    # TODO
    clt_variance = n * distribution.var()
    return round(clt_variance, 4)

def clt_prob(distribution, n: int, a: float, b: float) -> float:
    """Return P(a <= S_n <= b) via CLT normal approximation, rounded to 4 dp."""
    # TODO
    prob = scipy.stats.norm.cdf(standardized(distribution, b, n)) - scipy.stats.norm.cdf(standardized(distribution, a, n))
    return round(prob, 4)
