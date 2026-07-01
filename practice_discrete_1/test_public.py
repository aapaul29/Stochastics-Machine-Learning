import pytest
from solution import empirical_pmf, empirical_mean, empirical_variance

S = [0, 1, 0, 2, 1, 0]

def test_pmf_0():       assert empirical_pmf(S, 0) == pytest.approx(0.5, abs=1e-4)
def test_pmf_1():       assert empirical_pmf(S, 1) == pytest.approx(2/6, abs=1e-4)
def test_pmf_unseen():  assert empirical_pmf(S, 9) == pytest.approx(0.0, abs=1e-4)
def test_pmf_sums():    assert sum(empirical_pmf(S,k) for k in {0,1,2}) == pytest.approx(1.0, abs=1e-3)
def test_mean():        assert empirical_mean(S) == pytest.approx(4/6, abs=1e-4)
def test_variance():    assert empirical_variance(S) == pytest.approx(0.6667, abs=1e-3)
def test_var_single():  assert empirical_variance([5]) == 0.0
