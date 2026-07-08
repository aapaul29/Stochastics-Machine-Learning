import random
import math


def simulate_exponential(lam: float, n: int, seed: int) -> list[float]:
    """Sample n values from Exp(lam) via inverse CDF using random.random()."""
    random.seed(seed)
    return [round(-math.log(1 - random.random()) / lam, 4) for _ in range(n)]


def simulate_uniform(a: float, b: float, n: int, seed: int) -> list[float]:
    """Sample n values from Uniform(a, b) via inverse CDF using random.random()."""
    random.seed(seed)
    return [round(a + (b - a) * random.random(), 4) for _ in range(n)]
