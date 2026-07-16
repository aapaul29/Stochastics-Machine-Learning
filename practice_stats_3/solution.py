import math

def mean(samples: list) -> float:
    return sum(samples) / len(samples)

def mle_exponential(samples: list[float]) -> float:
    """Return MLE lambda_hat = 1/mean(samples), rounded to 4 dp."""
    # TODO
    lam = 1 / mean(samples)
    return round(lam, 4)

def mle_normal(samples: list[float]) -> tuple[float, float]:
    """Return (mu_hat, sigma_hat) where sigma uses MLE (divide by N), each rounded to 4 dp."""
    # TODO
    N = len(samples)
    mu = mean(samples)
    sum = 0
    coefficient = 1 / N
    for i in range(N):
        sum += (samples[i] - mu) ** 2
    var = coefficient * sum
    std = var ** 0.5
    return (round(mu, 4), round(std, 4))
