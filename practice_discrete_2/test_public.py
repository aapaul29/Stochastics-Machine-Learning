import pytest
from solution import binomial_pmf, binomial_cdf, binomial_mean_variance
import scipy.stats

def test_pmf_basic():  assert binomial_pmf(10,0.3,3)==pytest.approx(scipy.stats.binom.pmf(3,10,0.3),abs=1e-4)
def test_cdf_basic():  assert binomial_cdf(10,0.3,3)==pytest.approx(scipy.stats.binom.cdf(3,10,0.3),abs=1e-4)
def test_mv_basic():
    m,v=binomial_mean_variance(10,0.3)
    assert m==pytest.approx(3.0,abs=1e-4); assert v==pytest.approx(2.1,abs=1e-4)
def test_pmf_k0():     assert binomial_pmf(5,0.5,0)==pytest.approx((0.5)**5,abs=1e-4)
def test_cdf_k_n():    assert binomial_cdf(5,0.5,5)==pytest.approx(1.0,abs=1e-4)
def test_pmf_sums():   assert sum(binomial_pmf(8,0.4,k) for k in range(9))==pytest.approx(1.0,abs=1e-3)
def test_mv_fair():
    m,v=binomial_mean_variance(20,0.5)
    assert m==pytest.approx(10.0,abs=1e-4); assert v==pytest.approx(5.0,abs=1e-4)
