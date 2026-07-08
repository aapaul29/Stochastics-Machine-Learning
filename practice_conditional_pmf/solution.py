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
    output = []
    num_tuples = len(samples)
    num_y_target = 0
    for t in samples:
        if t[1] == y_target:
            num_y_target += 1
    if num_y_target == 0:
        return [0.0] * len(x_values)
    prob_y = num_y_target / num_tuples
    x_and_y = 0
    for x in x_values:
        for t in samples:
            if t[0] == x and t[1] == y_target:
                x_and_y += 1
        output.append(x_and_y /num_y_target)
        x_and_y = 0
    return output
