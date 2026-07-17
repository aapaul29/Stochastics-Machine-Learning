import math

def fit_standardizer(X_train: list[list[float]]) -> tuple[list[float], list[float]]:
    """Return (mu, sigma) per feature, each rounded to 6 dp."""
    n = len(X_train)
    d = len(X_train[0])
    mu    = [round(sum(X_train[i][j] for i in range(n)) / n, 6) for j in range(d)]
    sigma = [round(math.sqrt(sum((X_train[i][j] - mu[j])**2 for i in range(n)) / n), 6)
             for j in range(d)]
    return mu, sigma

def apply_standardizer(X: list[list[float]],
                       mu: list[float], sigma: list[float]) -> list[list[float]]:
    """Standardize X using mu and sigma."""
    def std_val(v, m, s):
        return round((v - m) / s, 6) if s != 0 else 0.0
    return [[std_val(X[i][j], mu[j], sigma[j]) for j in range(len(mu))]
            for i in range(len(X))]
