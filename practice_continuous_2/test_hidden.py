import pytest,random,scipy.stats
from solution import standardize,normal_prob,normal_quantile

def test_shifted():
    assert normal_prob(3,2,1,5)==pytest.approx(round(scipy.stats.norm.cdf(5,3,2)-scipy.stats.norm.cdf(1,3,2),4),abs=1e-4)

def test_quantile_inverse():
    for p in [0.1,0.25,0.75,0.9]:
        q=normal_quantile(2,3,p)
        assert abs(scipy.stats.norm.cdf(q,2,3)-p)<1e-3

def test_prob_point():
    assert normal_prob(0,1,0,0)==pytest.approx(0.0,abs=1e-4)

def test_symmetry():
    assert normal_prob(0,1,-1,0)==pytest.approx(normal_prob(0,1,0,1),abs=1e-4)

def test_rounding():
    r=normal_prob(0,1,-1,1); assert r==round(r,4)

def test_stress():
    random.seed(7)
    for _ in range(20):
        mu=random.uniform(-5,5); sigma=random.uniform(0.5,5)
        a=random.uniform(-10,0); b=random.uniform(0,10)
        exp=round(scipy.stats.norm.cdf(b,mu,sigma)-scipy.stats.norm.cdf(a,mu,sigma),4)
        assert normal_prob(mu,sigma,a,b)==pytest.approx(exp,abs=1e-4)
