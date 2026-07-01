import pytest,random,scipy.stats
from solution import poisson_pmf,poisson_cdf,poisson_approx_binomial

def test_lam_small():  assert poisson_pmf(0.1,0)==pytest.approx(scipy.stats.poisson.pmf(0,0.1),abs=1e-4)
def test_lam_large():  assert poisson_pmf(50,50)==pytest.approx(scipy.stats.poisson.pmf(50,50),abs=1e-4)
def test_cdf_monotone():
    vals=[poisson_cdf(5,k) for k in range(15)]
    assert all(vals[i]<=vals[i+1] for i in range(14))
def test_approx_accuracy():
    # Bin(500,0.01) ≈ Poisson(5), check relative error < 5%
    for k in range(10):
        exact=scipy.stats.binom.pmf(k,500,0.01)
        approx=poisson_approx_binomial(500,0.01,k)
        if exact>1e-6: assert abs(approx-exact)/exact<0.05
def test_stress():
    random.seed(7)
    for _ in range(20):
        lam=random.uniform(0.5,20); k=random.randint(0,30)
        assert poisson_pmf(lam,k)==pytest.approx(round(scipy.stats.poisson.pmf(k,lam),4),abs=1e-4)
        assert poisson_cdf(lam,k)==pytest.approx(round(scipy.stats.poisson.cdf(k,lam),4),abs=1e-4)
