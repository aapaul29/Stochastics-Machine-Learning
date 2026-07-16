import math
def gaussian(x: float, weight: float, mean: float, std: float) -> float:
    gaussian = weight * 1 / (std * math.sqrt(2 * math.pi)) * math.exp(-(x - mean) ** 2 / (2 * std ** 2))
    return gaussian

def mixture_pdf(x: float, weights: list[float], means: list[float], stds: list[float]) -> float:
    """Return the mixture PDF at x, rounded to 4 dp."""
    # TODO
    mixture_pdf = 0
    for i in range(len(weights)):
        mixture_pdf += gaussian(x, weights[i], means[i], stds[i])
    return round(mixture_pdf, 4)

def mixture_mean(weights: list[float], means: list[float]) -> float:
    """Return E[X] for the mixture, rounded to 4 dp."""
    # TODO
    expectation = 0
    for i in range(len(weights)):
        expectation += weights[i] * means[i]
    return round(expectation, 4)

def mixture_variance(weights: list[float], means: list[float], stds: list[float]) -> float:
    """Return Var(X) for the mixture, rounded to 4 dp."""
    # TODO
    summand_1 = 0
    summand_2 = 0
    for i in range(len(weights)):
        summand_1 += weights[i] * (stds[i] ** 2 + means[i] ** 2)
    for i in range(len(weights)):
        summand_2 += (weights[i] * means[i]) 
    variance = summand_1 - summand_2 ** 2
    return round(variance, 4)
