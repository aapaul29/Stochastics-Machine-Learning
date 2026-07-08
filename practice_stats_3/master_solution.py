import math


def mle_exponential(samples: list[float]) -> float:
    """Return MLE for lambda of Exp(lambda): 1 / x_bar, rounded to 4 dp."""
    return round(len(samples) / sum(samples), 4)


def mle_normal(samples: list[float]) -> tuple[float, float]:
    """Return (mu_hat, sigma_hat) MLE for Normal.
    mu_hat = x_bar, sigma_hat = sqrt(1/N * sum((x_i - x_bar)^2)), both rounded to 4 dp."""
    n = len(samples)
    mu = sum(samples) / n
    sigma = math.sqrt(sum((x - mu) ** 2 for x in samples) / n)
    return round(mu, 4), round(sigma, 4)
