import pytest,random,scipy.stats
from solution import binomial_pmf,binomial_cdf,binomial_mean_variance

def _pmf(n,p,k): return round(scipy.stats.binom.pmf(k,n,p),4)
def _cdf(n,p,k): return round(scipy.stats.binom.cdf(k,n,p),4)
def _mv(n,p): return (round(n*p,4),round(n*p*(1-p),4))

def test_p_zero():     assert binomial_pmf(10,0.0,0)==pytest.approx(1.0,abs=1e-4)
def test_p_one():      assert binomial_pmf(10,1.0,10)==pytest.approx(1.0,abs=1e-4)
def test_large_n():
    n,p,k=1000,0.4,410
    assert binomial_pmf(n,p,k)==pytest.approx(_pmf(n,p,k),abs=1e-4)
    assert binomial_cdf(n,p,k)==pytest.approx(_cdf(n,p,k),abs=1e-4)
def test_cdf_monotone():
    vals=[binomial_cdf(10,0.5,k) for k in range(11)]
    assert all(vals[i]<=vals[i+1] for i in range(10))
def test_stress():
    random.seed(42)
    for _ in range(20):
        n=random.randint(5,100); p=random.uniform(0.1,0.9); k=random.randint(0,n)
        assert binomial_pmf(n,p,k)==pytest.approx(_pmf(n,p,k),abs=1e-4)
        assert binomial_cdf(n,p,k)==pytest.approx(_cdf(n,p,k),abs=1e-4)
        m,v=binomial_mean_variance(n,p); em,ev=_mv(n,p)
        assert m==pytest.approx(em,abs=1e-4); assert v==pytest.approx(ev,abs=1e-4)
