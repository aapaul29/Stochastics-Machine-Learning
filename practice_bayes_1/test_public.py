"""Public tests — run with: python run.py"""
import pytest
from solution import marginal_probability, bayes_posterior

def test_marginal_disease():
    assert marginal_probability(0.01, 0.99, 0.05) == pytest.approx(0.0594, abs=0.0001)

def test_posterior_disease():
    assert bayes_posterior(0.01, 0.99, 0.05) == pytest.approx(0.1667, abs=0.0001)

def test_marginal_fair():
    # P(H)=0.5, P(E|H)=0.8, P(E|¬H)=0.2 → P(E)=0.5
    assert marginal_probability(0.5, 0.8, 0.2) == pytest.approx(0.5, abs=0.0001)

def test_posterior_fair():
    # P(H|E) = 0.4/0.5 = 0.8
    assert bayes_posterior(0.5, 0.8, 0.2) == pytest.approx(0.8, abs=0.0001)

def test_certain_evidence():
    # P(E|H)=1, P(E|¬H)=0 → P(E)=P(H), P(H|E)=1
    assert marginal_probability(0.3, 1.0, 0.0) == pytest.approx(0.3, abs=0.0001)
    assert bayes_posterior(0.3, 1.0, 0.0) == pytest.approx(1.0, abs=0.0001)

def test_rounding():
    result = bayes_posterior(0.01, 0.99, 0.05)
    # Must be rounded to 4 decimal places
    assert result == round(result, 4)
