import random
import math

def simulate_exponential(lam: float, n: int, seed: int) -> list[float]:
    """Return n samples from Exp(lam) via inverse CDF. Set random.seed(seed) first."""
    # TODO
    random.seed(seed)
    return [round(- math.log(1 - random.random()) / lam, 4) for _ in range(n)]

def simulate_uniform(a: float, b: float, n: int, seed: int) -> list[float]:
    """Return n samples from Uniform(a,b) via inverse CDF. Set random.seed(seed) first."""
    # TODO
    random.seed(seed)
    return [round(a + (b - a) * random.random(), 4) for _ in range(n)]
