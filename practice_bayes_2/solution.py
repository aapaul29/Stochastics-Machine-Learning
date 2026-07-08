# A partition {A_1, ..., A_n} of the sample space is given as:
#   priors       = [P(A_1), ..., P(A_n)]   (sum to 1)
#   conditionals = [P(B|A_1), ..., P(B|A_n)]

def total_probability(priors: list[float], conditionals: list[float]) -> float:
    """Return P(B) using the Law of Total Probability, rounded to 4 decimal places."""
    # TODO
    return -1.0


def most_likely_cause(priors: list[float], conditionals: list[float]) -> int:
    """Return the 0-based index of A_i with the highest posterior P(A_i | B).
    Break ties by returning the smaller index."""
    # TODO
    return -1
