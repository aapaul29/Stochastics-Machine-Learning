# Given pairs of observations samples[i] (0 <= i < N)
# where samples[i][0] is an observation of X and
#       samples[i][1] is an observation of Y,
# return the empirical conditional PMF of X given Y = y_target
# as a list of floats indexed by x_values.
#
# P_hat(X = x_values[k] | Y = y_target) for each k
#
# Return a list of zeros if no sample has Y = y_target.
# Round each entry to 2 decimal places.

def compute_conditional_pmf(samples: list[tuple[int, int]],
                             y_target: int,
                             x_values: list[int]) -> list[float]:
    # TODO
    
    return -1
