def marginal_probability(prior: float, likelihood: float, likelihood_complement: float) -> float:
    """Return P(E), rounded to 4 decimal places."""
    return round(likelihood * prior + likelihood_complement * (1 - prior), 4)


def bayes_posterior(prior: float, likelihood: float, likelihood_complement: float) -> float:
    """Return P(H | E) using Bayes theorem, rounded to 4 decimal places."""
    pe = likelihood * prior + likelihood_complement * (1 - prior)
    return round((likelihood * prior) / pe, 4)
