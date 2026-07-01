import pytest
from solution import empirical_covariance, empirical_correlation

def test_cov_linear():  assert empirical_covariance([1,2,3,4,5],[2,4,6,8,10])==pytest.approx(5.0,abs=1e-4)
def test_corr_perfect():assert empirical_correlation([1,2,3,4,5],[2,4,6,8,10])==pytest.approx(1.0,abs=1e-4)
def test_corr_neg():    assert empirical_correlation([1,2,3],[-1,-2,-3])==pytest.approx(-1.0,abs=1e-4)
def test_cov_zero():    assert empirical_covariance([1],[2])==0.0
def test_corr_zero_var():assert empirical_correlation([1,1,1],[1,2,3])==0.0
def test_cov_independent():
    import random; random.seed(42)
    xs=[random.gauss(0,1) for _ in range(10000)]
    ys=[random.gauss(0,1) for _ in range(10000)]
    assert abs(empirical_covariance(xs,ys))<0.1
