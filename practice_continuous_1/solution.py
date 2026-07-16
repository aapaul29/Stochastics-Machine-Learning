import math

def exp_pdf(lam: float, x: float) -> float:
    """PDF of Exp(lam) at x, rounded to 4 dp. Return 0.0 if x < 0."""
    # TODO
    if x < 0:
        return 0.0
    exp_pdf = lam * math.exp(-lam * x)
    return round(exp_pdf, 4)

def exp_cdf(lam: float, x: float) -> float:
    """CDF of Exp(lam) at x, rounded to 4 dp. Return 0.0 if x < 0."""
    # TODO
    if x < 0:
        return 0.0
    exp_cdf = 1 - math.exp(-lam * x)
    return round(exp_cdf, 4)

def exp_quantile(lam: float, p: float) -> float:
    """Quantile Q(p) of Exp(lam), rounded to 4 dp."""
    # TODO
    quantile = - math.log(1 - p) / lam
    return round(quantile, 4)
