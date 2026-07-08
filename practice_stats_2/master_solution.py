def empirical_cdf(samples: list[float], x: float) -> float:
    """Return F_hat(x) = #{i: x_i <= x} / N, rounded to 4 dp."""
    return round(sum(1 for xi in samples if xi <= x) / len(samples), 4)


def empirical_quantile(samples: list[float], p: float) -> float:
    """Return smallest sample value x such that F_hat(x) >= p."""
    s = sorted(samples)
    n = len(s)
    for x in s:
        if sum(1 for xi in s if xi <= x) / n >= p:
            return x
    return s[-1]
