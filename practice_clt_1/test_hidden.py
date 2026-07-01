import pytest,scipy.stats,math
from solution import clt_mean,clt_variance,clt_prob

def _prob(d,n,a,b):
    mu=d.mean(); sig=math.sqrt(d.var()*n)
    return round(scipy.stats.norm.cdf(b,n*mu,sig)-scipy.stats.norm.cdf(a,n*mu,sig),4)

def test_exponential():
    d=scipy.stats.expon(scale=2)
    assert clt_mean(d,10)==pytest.approx(20.0,abs=1e-4)
    assert clt_variance(d,10)==pytest.approx(round(10*d.var(),4),abs=1e-4)

def test_prob_exp():
    d=scipy.stats.expon(scale=1); n=50
    assert clt_prob(d,n,40,60)==pytest.approx(_prob(d,n,40,60),abs=1e-4)

def test_prob_binomial():
    d=scipy.stats.binom(n=10,p=0.3)
    assert clt_prob(d,50,100,160)==pytest.approx(_prob(d,50,100,160),abs=1e-3)

def test_prob_zero_interval():
    d=scipy.stats.norm(0,1)
    assert clt_prob(d,10,0,0)==pytest.approx(0.0,abs=1e-4)

def test_rounding():
    d=scipy.stats.poisson(mu=3); r=clt_mean(d,10); assert r==round(r,4)

def test_stress():
    import random; random.seed(7)
    dists=[scipy.stats.norm(random.uniform(-2,2),random.uniform(0.5,2)) for _ in range(5)]
    for d in dists:
        n=random.randint(20,200); a=n*d.mean()-2*math.sqrt(n*d.var()); b=n*d.mean()+2*math.sqrt(n*d.var())
        assert clt_prob(d,n,a,b)==pytest.approx(_prob(d,n,a,b),abs=1e-4)
