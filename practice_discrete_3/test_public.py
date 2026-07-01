import pytest, scipy.stats
from solution import poisson_pmf, poisson_cdf, poisson_approx_binomial

def test_pmf_basic():   assert poisson_pmf(3.0,2)==pytest.approx(scipy.stats.poisson.pmf(2,3.0),abs=1e-4)
def test_cdf_basic():   assert poisson_cdf(3.0,2)==pytest.approx(scipy.stats.poisson.cdf(2,3.0),abs=1e-4)
def test_pmf_k0():      assert poisson_pmf(2.0,0)==pytest.approx(scipy.stats.poisson.pmf(0,2.0),abs=1e-4)
def test_approx():      assert poisson_approx_binomial(1000,0.003,2)==pytest.approx(scipy.stats.poisson.pmf(2,3.0),abs=1e-4)
def test_pmf_sums():    assert sum(poisson_pmf(2.0,k) for k in range(20))==pytest.approx(1.0,abs=1e-3)
def test_cdf_large_k(): assert poisson_cdf(1.0,50)==pytest.approx(1.0,abs=1e-4)
