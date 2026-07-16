def mean(l: list) -> float:
    mean = sum(l) / len(l)
    return mean


def std_dev(l : list):
    N = len(l)
    coefficient = 1 / (N - 1)
    sum = 0
    for i in range(N):
        sum += (l[i] - mean(l)) ** 2
    std_dev = (coefficient * sum) ** 0.5
    return std_dev


def empirical_covariance(xs: list[float], ys: list[float]) -> float:
    """Return sample covariance (n-1), rounded to 4 dp. Return 0.0 if n<=1."""
    # TODO
    N = len(xs)
    if N <= 1:
        return 0.0
    x_mean = mean(xs)
    y_mean = mean(ys)
    coefficient = 1 / (N - 1)
    sum = 0
    for i in range(N):
        sum += (xs[i] - x_mean) * (ys[i] - y_mean)
    cov = coefficient * sum
    return round(cov, 4)


def empirical_correlation(xs: list[float], ys: list[float]) -> float:
    """Return sample correlation, rounded to 4 dp. Return 0.0 if either std is 0."""
    # TODO
    cov = empirical_covariance(xs, ys)
    std_dev_x = std_dev(xs)
    std_dev_y = std_dev(ys)
    if std_dev_x == 0 or std_dev_y == 0:
        return 0.0
    corr = cov / (std_dev_x * std_dev_y) 
    
    return round(corr, 4)
