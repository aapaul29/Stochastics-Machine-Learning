import scipy.stats

def poisson_pmf(lam: float, k: int) -> float:
    """Return P(X=k) for X~Poisson(lam), rounded to 4 decimal places."""
    # TODO
    return(round(scipy.stats.poisson.pmf(k, lam), 4))
    

def poisson_cdf(lam: float, k: int) -> float:
    """Return P(X<=k) for X~Poisson(lam), rounded to 4 decimal places."""
    # TODO
    return(round(scipy.stats.poisson.cdf(k, lam), 4))

def poisson_approx_binomial(n: int, p: float, k: int) -> float:
    """Approximate P(Bin(n,p)=k) using Poisson(n*p), rounded to 4 dp."""
    # TODO
    approx = poisson_pmf(n * p, k)
    return round(approx, 4)
