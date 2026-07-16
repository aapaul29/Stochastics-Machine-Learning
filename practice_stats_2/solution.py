def empirical_cdf(samples: list[float], x: float) -> float:
    """Return F_hat(x) = #{xi <= x} / N, rounded to 4 dp."""
    # TODO
    N = len(samples)
    count = 0
    for i in range(N):
        if samples[i] <= x:
            count += 1
    cdf = count / N
    return round(cdf, 4)

def empirical_quantile(samples: list[float], p: float) -> float:
    """Return smallest sample value x with F_hat(x) >= p."""
    # TODO
    sorted_samples = sorted(samples)
    for x in samples:
        cdf = empirical_cdf(samples, x)
        if cdf >= p:
            return x
