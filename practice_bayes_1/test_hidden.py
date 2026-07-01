"""Hidden grading tests."""
import pytest
from solution import marginal_probability, bayes_posterior

def _ref_marginal(p, l, lc):
    return round(l * p + lc * (1 - p), 4)

def _ref_posterior(p, l, lc):
    pe = l * p + lc * (1 - p)
    return round((l * p) / pe, 4)

def test_low_prior():
    assert marginal_probability(0.001, 0.95, 0.1) == pytest.approx(_ref_marginal(0.001, 0.95, 0.1), abs=0.0001)

def test_low_prior_posterior():
    assert bayes_posterior(0.001, 0.95, 0.1) == pytest.approx(_ref_posterior(0.001, 0.95, 0.1), abs=0.0001)

def test_high_prior():
    assert bayes_posterior(0.9, 0.7, 0.4) == pytest.approx(_ref_posterior(0.9, 0.7, 0.4), abs=0.0001)

def test_equal_likelihoods():
    # P(E|H) = P(E|¬H) → posterior equals prior
    p = 0.3
    assert bayes_posterior(p, 0.6, 0.6) == pytest.approx(p, abs=0.0001)

def test_zero_likelihood_complement():
    assert bayes_posterior(0.5, 0.8, 0.0) == pytest.approx(1.0, abs=0.0001)

def test_marginal_symmetry():
    # marginal(p, l, lc) == marginal(1-p, lc, l)
    a = marginal_probability(0.3, 0.9, 0.2)
    b = marginal_probability(0.7, 0.2, 0.9)
    assert a == pytest.approx(b, abs=0.0001)

def test_stress():
    import random
    random.seed(99)
    for _ in range(50):
        p  = random.uniform(0.01, 0.99)
        l  = random.uniform(0.0, 1.0)
        lc = random.uniform(0.0, 1.0)
        assert marginal_probability(p, l, lc) == pytest.approx(_ref_marginal(p, l, lc), abs=0.0001)
        pe = _ref_marginal(p, l, lc)
        if pe > 0:
            assert bayes_posterior(p, l, lc) == pytest.approx(_ref_posterior(p, l, lc), abs=0.0001)
