# Given paired observations (x_i, y_i) where y_i is a class label
# and x_i is an observed feature value, implement the three functions below.

def empirical_prior(samples: list[tuple[int, int]], c: int) -> float:
    """Return P_hat(Y = c), rounded to 4 decimal places."""
    # TODO
    count = 0
    for t in samples:
        if t[1] == c:
            count += 1
    prior = count / len(samples)
    return round(prior, 4)


def empirical_posterior(samples: list[tuple[int, int]], x_val: int, c: int) -> float:
    """Return P_hat(Y = c | X = x_val), rounded to 4 decimal places.
    Return 0.0 if no sample has X = x_val."""
    # TODO
    ## probability of x 
    count = 0
    for t in samples:
        if t[0] == x_val:
            count += 1
    prob_x = count / len(smaples)
    ## probaility of x and y
    count_ = 0
    for t in samples:
        if t[0] == x_val and t[1] == c:
            count += 1
    prob_x_and_y = count_ / len(samples)
    ## posterior
    posterior = prob_x_and_y / prob_x
    return round(posterior, 4)


def most_likely_class(samples: list[tuple[int, int]], x_val: int, classes: list[int]) -> int:
    """Return the class c* in classes that maximises P_hat(Y = c | X = x_val).
    Break ties by returning the smallest class label.
    If no sample has X = x_val, return the class with the highest prior."""
    # TODO
    c_list = []
    for c in classes:
        c_list.append(empirical_posterior(samples, x_val, c))
    return min(c_list)
