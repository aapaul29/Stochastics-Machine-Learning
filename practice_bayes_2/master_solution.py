def total_probability(priors: list[float], conditionals: list[float]) -> float:
    """Return P(B) using the Law of Total Probability, rounded to 4 decimal places."""
    return round(sum(p * c for p, c in zip(priors, conditionals)), 4)


def most_likely_cause(priors: list[float], conditionals: list[float]) -> int:
    """Return the 0-based index of A_i with the highest posterior P(A_i | B).
    Break ties by returning the smaller index."""
    scores = [p * c for p, c in zip(priors, conditionals)]
    return scores.index(max(scores))
