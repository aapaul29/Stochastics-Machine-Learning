import scipy.stats


def clt_mean(distribution, n: int) -> float:
    """Return E[S_n] = n * mu, rounded to 4 dp."""
    return round(n * float(distribution.mean()), 4)


def clt_variance(distribution, n: int) -> float:
    """Return Var(S_n) = n * sigma^2, rounded to 4 dp."""
    return round(n * float(distribution.var()), 4)


def clt_prob(distribution, n: int, a: float, b: float) -> float:
    """Return P(a <= S_n <= b) via CLT approximation, rounded to 4 dp."""
    mu = float(distribution.mean())
    sigma = float(distribution.var()) ** 0.5
    sn_mean = n * mu
    sn_std = (n ** 0.5) * sigma
    prob = (scipy.stats.norm.cdf((b - sn_mean) / sn_std)
            - scipy.stats.norm.cdf((a - sn_mean) / sn_std))
    return round(prob, 4)
