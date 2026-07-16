# A partition {A_1, ..., A_n} of the sample space is given as:
#   priors       = [P(A_1), ..., P(A_n)]   (sum to 1)
#   conditionals = [P(B|A_1), ..., P(B|A_n)]

def total_probability(priors: list[float], conditionals: list[float]) -> float:
    """Return P(B) using the Law of Total Probability, rounded to 4 decimal places."""
    # TODO
    prob = 0
    for i in range(len(priors)):
        prob += priors[i] * conditionals[i]
    return round(prob, 4)


def most_likely_cause(priors: list[float], conditionals: list[float]) -> int:
    """Return the 0-based index of A_i with the highest posterior P(A_i | B).
    Break ties by returning the smaller index."""
    # TODO
    prob_b = total_probability(priors, conditionals)
    posterior_list = []
    for i in range(len(priors)):
        posterior = priors[i] * conditionals[i] / prob_b
        posterior_list.append(posterior)
    max_value = max(posterior_list)
    max_index = 0
    for i in range(len(posterior_list)):
        if posterior_list[i] == max_value:
            max_index = i
            break
        
    return max_index
