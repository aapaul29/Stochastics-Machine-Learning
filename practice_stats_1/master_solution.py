import statistics


def sample_mean(data: list[float]) -> float:
    """Return sample mean, rounded to 4 dp."""
    return round(sum(data) / len(data), 4)


def sample_variance(data: list[float]) -> float:
    """Return unbiased sample variance (N-1), rounded to 4 dp. Return 0.0 if N=1."""
    if len(data) == 1:
        return 0.0
    return round(statistics.variance(data), 4)


def sample_median(data: list[float]) -> float:
    """Return sample median, rounded to 4 dp."""
    return round(statistics.median(data), 4)


def sample_iqr(data: list[float]) -> float:
    """Return IQR = Q_0.75 - Q_0.25 using statistics.quantiles (exclusive), rounded to 4 dp."""
    q = statistics.quantiles(data, n=4)  # [Q1, Q2, Q3] with exclusive method
    return round(q[2] - q[0], 4)
