def q_update(q_sa: float, reward: float, max_q_next: float,
             alpha: float, gamma: float) -> float:
    """One Bellman Q-learning update, rounded to 6 dp."""
    target = reward + gamma * max_q_next
    return round(q_sa + alpha * (target - q_sa), 6)
