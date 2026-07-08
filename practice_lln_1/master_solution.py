def running_average(samples: list[float]) -> list[float]:
    """Return list where element n is the mean of samples[0..n-1], rounded to 4 dp."""
    avgs = []
    total = 0.0
    for i, x in enumerate(samples, 1):
        total += x
        avgs.append(round(total / i, 4))
    return avgs


def lln_converges(samples: list[float], true_mean: float, eps: float) -> bool:
    """Return True if the final running average is within eps of true_mean."""
    ra = running_average(samples)
    return abs(ra[-1] - true_mean) < eps


def convergence_index(samples: list[float], true_mean: float, eps: float) -> int:
    """Return smallest 1-indexed n such that all subsequent averages stay within eps.
    Return N if no such n exists."""
    ra = running_average(samples)
    n = len(ra)
    for i in range(n - 1, -1, -1):
        if abs(ra[i] - true_mean) >= eps:
            return i + 2
    return 1
