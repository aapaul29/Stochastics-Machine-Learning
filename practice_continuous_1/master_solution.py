import math


def exp_pdf(lam: float, x: float) -> float:
    """Return f(x) = lam * exp(-lam*x) for x >= 0, else 0.0. Rounded to 4 dp."""
    if x < 0:
        return 0.0
    return round(lam * math.exp(-lam * x), 4)


def exp_cdf(lam: float, x: float) -> float:
    """Return F(x) = 1 - exp(-lam*x) for x >= 0, else 0.0. Rounded to 4 dp."""
    if x < 0:
        return 0.0
    return round(1 - math.exp(-lam * x), 4)


def exp_quantile(lam: float, p: float) -> float:
    """Return Q(p) = -ln(1-p) / lam. Rounded to 4 dp."""
    return round(-math.log(1 - p) / lam, 4)
