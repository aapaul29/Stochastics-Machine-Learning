"""Public tests — run with: python run.py"""
import pytest
from solution import empirical_prior, empirical_posterior, most_likely_class

S = [(0,0),(0,1),(0,0),(1,1),(1,1),(0,1)]

def test_prior_class0():
    assert empirical_prior(S, 0) == pytest.approx(2/6, abs=0.0001)

def test_prior_class1():
    assert empirical_prior(S, 1) == pytest.approx(4/6, abs=0.0001)

def test_posterior_x0_c0():
    assert empirical_posterior(S, 0, 0) == pytest.approx(0.5, abs=0.0001)

def test_posterior_x0_c1():
    assert empirical_posterior(S, 0, 1) == pytest.approx(0.5, abs=0.0001)

def test_posterior_x1_c1():
    # Both X=1 samples have Y=1
    assert empirical_posterior(S, 1, 1) == pytest.approx(1.0, abs=0.0001)

def test_posterior_unseen_x():
    assert empirical_posterior(S, 99, 0) == 0.0

def test_most_likely_class_basic():
    assert most_likely_class(S, 1, [0, 1]) == 1

def test_most_likely_unseen_falls_back_to_prior():
    # X=99 unseen → return class with highest prior → class 1 (4/6)
    assert most_likely_class(S, 99, [0, 1]) == 1

def test_tie_returns_smaller():
    s = [(0,0),(0,1)]  # P(Y=0|X=0)=0.5, P(Y=1|X=0)=0.5 → tie → class 0
    assert most_likely_class(s, 0, [0, 1]) == 0
