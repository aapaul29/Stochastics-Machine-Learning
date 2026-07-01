# Given paired observations (x_i, y_i) where y_i is a class label
# and x_i is an observed feature value, implement the three functions below.

def empirical_prior(samples: list[tuple[int, int]], c: int) -> float:
    """Return P_hat(Y = c), rounded to 4 decimal places."""
    # TODO
    return -1.0


def empirical_posterior(samples: list[tuple[int, int]], x_val: int, c: int) -> float:
    """Return P_hat(Y = c | X = x_val), rounded to 4 decimal places.
    Return 0.0 if no sample has X = x_val."""
    # TODO
    return -1.0


def most_likely_class(samples: list[tuple[int, int]], x_val: int, classes: list[int]) -> int:
    """Return the class c* in classes that maximises P_hat(Y = c | X = x_val).
    Break ties by returning the smallest class label.
    If no sample has X = x_val, return the class with the highest prior."""
    # TODO
    return -1
