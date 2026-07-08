import math


def mixture_pdf(x: float, weights: list[float], means: list[float], stds: list[float]) -> float:
    """Return f(x) for the Gaussian mixture, rounded to 4 dp."""
    total = 0.0
    for w, mu, sigma in zip(weights, means, stds):
        total += w * math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))
    return round(total, 4)


def mixture_mean(weights: list[float], means: list[float]) -> float:
    """Return E[X] = sum_k w_k * mu_k, rounded to 4 dp."""
    return round(sum(w * mu for w, mu in zip(weights, means)), 4)


def mixture_variance(weights: list[float], means: list[float], stds: list[float]) -> float:
    """Return Var(X) = sum_k w_k*(sigma_k^2 + mu_k^2) - (sum_k w_k*mu_k)^2, rounded to 4 dp."""
    second_moment = sum(w * (s ** 2 + mu ** 2) for w, mu, s in zip(weights, means, stds))
    mean_sq = mixture_mean(weights, means) ** 2
    return round(second_moment - mean_sq, 4)
