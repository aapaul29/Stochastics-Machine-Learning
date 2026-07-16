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
   ## Handle Exception
    y_list = [t[1] for t in samples]
    if y_target not in y_list:
        return [0] * len(x_values)
    ## probability of y:
    count = 0
    for t in samples:
        if t[1] == y_target:
            count += 1
    prob_y = count / len(samples)
    ## probability of x and y
    prob_x_and_y = []
    for x in x_values:
        count = 0
        for t in samples:
            if t[0] == x and t[1] == y_target:
                count += 1
        prob = count / len(samples)
        prob_x_and_y.append(prob)
    ##output list
    output = []
    for prob in prob_x_and_y:
        conditional = prob/ prob_y
        output.append(conditional)
    
    return output
    

    
    
