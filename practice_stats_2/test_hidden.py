import pytest,random
from solution import empirical_cdf,empirical_quantile

def _cdf(s,x): return round(sum(1 for xi in s if xi<=x)/len(s),4)
def _q(s,p):
    ss=sorted(s)
    for x in ss:
        if _cdf(s,x)>=p: return x
    return ss[-1]

def test_duplicates():
    s=[1,1,2,2,3]
    assert empirical_cdf(s,1)==pytest.approx(0.4,abs=1e-4)
    assert empirical_quantile(s,0.3)==1

def test_single():
    s=[5.0]
    assert empirical_cdf(s,5)==pytest.approx(1.0,abs=1e-4)
    assert empirical_quantile(s,0.5)==5.0

def test_large():
    import numpy as np; random.seed(42)
    s=[random.gauss(0,1) for _ in range(10000)]
    assert abs(empirical_cdf(s,0)-0.5)<0.02

def test_stress():
    random.seed(7)
    for _ in range(15):
        s=[random.randint(0,20) for _ in range(random.randint(5,200))]
        x=random.uniform(0,20); p=random.uniform(0,1)
        assert empirical_cdf(s,x)==pytest.approx(_cdf(s,x),abs=1e-4)
        assert empirical_quantile(s,p)==_q(s,p)
