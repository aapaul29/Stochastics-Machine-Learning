import random

def epsilon_greedy(q_values: list[float], epsilon: float, seed: int) -> int:
    """Epsilon-greedy action selection."""
    random.seed(seed)
    u = random.random()
    n = len(q_values)
    if u < epsilon:
        return random.randint(0, n - 1)
    else:
        best_val = max(q_values)
        return q_values.index(best_val)
