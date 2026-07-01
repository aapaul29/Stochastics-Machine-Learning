import pytest
from solution import empirical_cdf, empirical_quantile

S=[1,3,2,5,4]

def test_cdf_exact():   assert empirical_cdf(S,3)==pytest.approx(0.6,abs=1e-4)
def test_cdf_between(): assert empirical_cdf(S,2.5)==pytest.approx(0.4,abs=1e-4)
def test_cdf_below():   assert empirical_cdf(S,0)==pytest.approx(0.0,abs=1e-4)
def test_cdf_above():   assert empirical_cdf(S,10)==pytest.approx(1.0,abs=1e-4)
def test_q_median():    assert empirical_quantile(S,0.5)==3
def test_q_min():       assert empirical_quantile(S,0.0)==1
def test_q_max():       assert empirical_quantile(S,1.0)==5
def test_cdf_monotone():
    vals=[empirical_cdf(S,x) for x in [0,1,2,3,4,5,6]]
    assert all(vals[i]<=vals[i+1] for i in range(6))
