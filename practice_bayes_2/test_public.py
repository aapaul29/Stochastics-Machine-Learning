"""Public tests — run with: python run.py"""
import pytest
from solution import total_probability, most_likely_cause

def test_three_machines_total():
    assert total_probability([0.5, 0.3, 0.2], [0.02, 0.05, 0.10]) == pytest.approx(0.045, abs=0.0001)

def test_three_machines_cause():
    assert most_likely_cause([0.5, 0.3, 0.2], [0.02, 0.05, 0.10]) == 2

def test_two_causes_total():
    # P(B) = 0.6*0.3 + 0.4*0.8 = 0.18 + 0.32 = 0.5
    assert total_probability([0.6, 0.4], [0.3, 0.8]) == pytest.approx(0.5, abs=0.0001)

def test_two_causes_most_likely():
    # P(A0|B) ∝ 0.6*0.3=0.18, P(A1|B) ∝ 0.4*0.8=0.32 → index 1
    assert most_likely_cause([0.6, 0.4], [0.3, 0.8]) == 1

def test_uniform_prior_highest_likelihood_wins():
    # Equal priors → highest conditional wins
    assert most_likely_cause([0.25, 0.25, 0.25, 0.25], [0.1, 0.5, 0.3, 0.4]) == 1

def test_tie_returns_smaller_index():
    # P(A0|B) ∝ 0.5*0.4=0.2, P(A1|B) ∝ 0.5*0.4=0.2 → tie → index 0
    assert most_likely_cause([0.5, 0.5], [0.4, 0.4]) == 0

def test_total_rounding():
    result = total_probability([0.5, 0.3, 0.2], [0.02, 0.05, 0.10])
    assert result == round(result, 4)
