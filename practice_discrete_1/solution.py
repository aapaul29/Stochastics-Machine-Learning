def empirical_pmf(samples: list[int], k: int) -> float:
    """Return P_hat(X=k), rounded to 4 decimal places."""
    # TODO
    N = len(samples)
    count = 0
    for sample in samples:
        if sample == k:
            count += 1
    pmf = count / N
    return round(pmf, 4)

def empirical_mean(samples: list[int]) -> float:
    """Return sample mean, rounded to 4 decimal places."""
    # TODO
    N = len(samples)
    mean = 1 / N * sum(samples)
    return round(mean, 4)

def empirical_variance(samples: list[int]) -> float:
    """Return unbiased sample variance (n-1), rounded to 4 dp. 0.0 if n==1."""
    # TODO
    ## Handle Exception
    if len(samples) == 1:
        return 0.0
    ## variance
    N = len(samples)
    mean = empirical_mean(samples)
    var = 1 / (N - 1) * sum((s - mean) ** 2 for s in samples)
    return round(var, 4)
