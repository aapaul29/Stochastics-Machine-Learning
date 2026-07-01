import pytest,random,math,scipy.stats
from solution import t_statistic,p_value,reject_null

def _t(s,mu0):
    n=len(s); xbar=sum(s)/n; std=math.sqrt(sum((x-xbar)**2 for x in s)/(n-1))
    return round((xbar-mu0)/(std/math.sqrt(n)),4)
def _p(s,mu0):
    t=_t(s,mu0); return round(2*scipy.stats.t.sf(abs(t),df=len(s)-1),4)

def test_exact():
    s=[2.5,3.1,2.8,3.2,2.9]
    assert t_statistic(s,3.0)==pytest.approx(_t(s,3.0),abs=1e-4)
    assert p_value(s,3.0)==pytest.approx(_p(s,3.0),abs=1e-4)

def test_large_effect():
    s=[100.0]*30
    assert reject_null(s,0.0,0.01)==True

def test_stress():
    random.seed(7)
    for _ in range(15):
        n=random.randint(5,200); mu=random.uniform(-5,5)
        s=[random.gauss(mu,1) for _ in range(n)]
        mu0=random.uniform(-5,5)
        assert t_statistic(s,mu0)==pytest.approx(_t(s,mu0),abs=1e-4)
        assert p_value(s,mu0)==pytest.approx(_p(s,mu0),abs=1e-4)
        assert reject_null(s,mu0,0.05)==(_p(s,mu0)<0.05)
