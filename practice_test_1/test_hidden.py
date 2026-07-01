import pytest,random,math,scipy.stats
from solution import confidence_interval

def _ci(s,sig,alpha):
    n=len(s); xbar=sum(s)/n; z=scipy.stats.norm.ppf(1-alpha/2)
    m=z*sig/math.sqrt(n)
    return round(xbar-m,4),round(xbar+m,4)

def test_exact():
    s=[1.0,2.0,3.0,4.0,5.0]
    assert confidence_interval(s,2.0,0.05)==pytest.approx(_ci(s,2.0,0.05),abs=1e-4)

def test_single_sample():
    s=[3.0]
    lo,hi=confidence_interval(s,1.0,0.05); elo,ehi=_ci(s,1.0,0.05)
    assert lo==pytest.approx(elo,abs=1e-4); assert hi==pytest.approx(ehi,abs=1e-4)

def test_lo_lt_hi():
    lo,hi=confidence_interval([1,2,3],0.5,0.05); assert lo<hi

def test_stress():
    random.seed(7)
    for _ in range(15):
        n=random.randint(2,200); s=[random.gauss(0,1) for _ in range(n)]
        sig=random.uniform(0.5,3); alpha=random.choice([0.01,0.05,0.1])
        lo,hi=confidence_interval(s,sig,alpha); elo,ehi=_ci(s,sig,alpha)
        assert lo==pytest.approx(elo,abs=1e-4); assert hi==pytest.approx(ehi,abs=1e-4)
