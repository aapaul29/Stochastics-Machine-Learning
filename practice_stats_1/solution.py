import math

def sample_mean(data: list[float]) -> float:
    """Return sample mean, rounded to 4 dp."""
    # TODO
    mean = sum(data) / len(data)
    return round(mean, 4)

def sample_variance(data: list[float]) -> float:
    """Return unbiased sample variance (n-1), rounded to 4 dp. Return 0.0 if n==1."""
    # TODO
    N = len(data)
    if N == 1:
        return 0.0
    coefficient = 1 / (N - 1)
    mean = sample_mean(data)
    sum = 0
    for x in data:
        sum += (x - mean) ** 2
    variance = coefficient * sum
    return round(variance, 4)

def sample_median(data: list[float]) -> float:
    """Return sample median, rounded to 4 dp."""
    # TODO
    data_sorted = sorted(data)
    N = len(data)
    if N % 2 == 0:
        return round(1 / 2 * (data_sorted[N // 2 - 1] + data_sorted[N // 2]), 4)
    else:
        return round(data_sorted[N // 2], 4)
    
def quantile(data: list, p: float) -> float:
    data_sorted = sorted(data)
    n = len(data)
    h = (n - 1) * p - 1
    lower = math.floor(h)
    upper = math.ceil(h)
    quantile = data_sorted[lower] + (h - lower) * (data_sorted[upper] - data_sorted[lower])
    return quantile

def sample_iqr(data: list[float]) -> float:
    """Return IQR = Q0.75 - Q0.25, rounded to 4 dp."""
    # TODO
    iqr = quantile(data, 0.75) - quantile(data, 0.25)
    return round(iqr, 4)
