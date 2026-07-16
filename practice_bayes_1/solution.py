# Given:
#   prior                = P(H)
#   likelihood           = P(E | H)
#   likelihood_complement = P(E | ¬H)
#
# Implement the two functions below.

def marginal_probability(prior: float, likelihood: float, likelihood_complement: float) -> float:
    """Return P(E), rounded to 4 decimal places."""
    # TODO
    marginal_prob = prior * likelihood + (1 - prior) * likelihood_complement
    return round(marginal_prob, 4)


def bayes_posterior(prior: float, likelihood: float, likelihood_complement: float) -> float:
    """Return P(H | E) using Bayes' theorem, rounded to 4 decimal places."""
    # TODO
    marginal_prob = marginal_probability(prior, likelihood, likelihood_complement)
    posterior = (prior * likelihood) / marginal_prob
    return round(posterior, 4)
