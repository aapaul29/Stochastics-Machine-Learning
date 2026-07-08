# Given:
#   prior                = P(H)
#   likelihood           = P(E | H)
#   likelihood_complement = P(E | not H)
#
# Implement the two functions below.

def marginal_probability(prior: float, likelihood: float, likelihood_complement: float) -> float:
    """Return P(E), rounded to 4 decimal places."""
    # TODO
    ## my solution
    marginal_prob = likelihood * prior + likelihood_complement * (1 - prior)
    marginal_rounded = round(marginal_prob, 4)
    return marginal_rounded


def bayes_posterior(prior: float, likelihood: float, likelihood_complement: float) -> float:
    """Return P(H | E) using Bayes' theorem, rounded to 4 decimal places."""
    # TODO
    ##my solution
    marginal_prob = likelihood * prior + likelihood_complement * (1 - prior)
    posterior_prob = likelihood * prior / marginal_prob
    posterior_rounded = round(posterior_prob, 4)
    return posterior_rounded
