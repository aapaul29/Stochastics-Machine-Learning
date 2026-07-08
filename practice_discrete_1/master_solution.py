def empirical_pmf(samples: list[int], k: int) -> float:
    """Return P_hat(X = k), rounded to 4 dp."""
    return round(samples.count(k) / len(samples), 4)


def empirical_mean(samples: list[int]) -> float:
    """Return sample mean, rounded to 4 dp."""
    return round(sum(samples) / len(samples), 4)


def empirical_variance(samples: list[int]) -> float:
    """Return unbiased sample variance (divided by N-1), rounded to 4 dp.
    Return 0.0 if len(samples) == 1."""
    n = len(samples)
    if n == 1:
        return 0.0
    mu = sum(samples) / n
    return round(sum((x - mu) ** 2 for x in samples) / (n - 1), 4)
