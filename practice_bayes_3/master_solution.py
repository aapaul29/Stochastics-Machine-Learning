def empirical_prior(samples: list[tuple[int, int]], c: int) -> float:
    """Return P_hat(Y = c), rounded to 4 decimal places."""
    return round(sum(1 for _, y in samples if y == c) / len(samples), 4)


def empirical_posterior(samples: list[tuple[int, int]], x_val: int, c: int) -> float:
    """Return P_hat(Y = c | X = x_val), rounded to 4 decimal places.
    Return 0.0 if no sample has X = x_val."""
    x_count = sum(1 for x, _ in samples if x == x_val)
    if x_count == 0:
        return 0.0
    xc_count = sum(1 for x, y in samples if x == x_val and y == c)
    return round(xc_count / x_count, 4)


def most_likely_class(samples: list[tuple[int, int]], x_val: int, classes: list[int]) -> int:
    """Return class label c* maximising P_hat(Y=c | X=x_val).
    Fall back to highest prior if no sample has X=x_val. Break ties by smallest label."""
    x_count = sum(1 for x, _ in samples if x == x_val)
    if x_count == 0:
        priors = {c: empirical_prior(samples, c) for c in classes}
        best = max(priors.values())
        return min(c for c in classes if priors[c] == best)
    posteriors = {c: empirical_posterior(samples, x_val, c) for c in classes}
    best = max(posteriors.values())
    return min(c for c in classes if posteriors[c] == best)
