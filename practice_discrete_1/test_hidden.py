import pytest, random
from solution import empirical_pmf, empirical_mean, empirical_variance

def _pmf(s,k): return round(s.count(k)/len(s),4)
def _mean(s):  return round(sum(s)/len(s),4)
def _var(s):
    if len(s)==1: return 0.0
    m=sum(s)/len(s); return round(sum((x-m)**2 for x in s)/(len(s)-1),4)

def test_all_same():
    assert empirical_pmf([3]*10,3)==pytest.approx(1.0,abs=1e-4)
    assert empirical_variance([3]*10)==pytest.approx(0.0,abs=1e-4)

def test_two_elements():
    assert empirical_variance([0,1])==pytest.approx(0.5,abs=1e-4)

def test_large():
    random.seed(42); s=[random.randint(0,5) for _ in range(100_000)]
    assert empirical_mean(s)==pytest.approx(_mean(s),abs=1e-3)
    assert empirical_variance(s)==pytest.approx(_var(s),abs=1e-2)

def test_rounding():
    r=empirical_mean([0,1,2]); assert r==round(r,4)

def test_stress():
    random.seed(7)
    for _ in range(20):
        s=[random.randint(0,9) for _ in range(random.randint(2,200))]
        k=random.randint(0,9)
        assert empirical_pmf(s,k)==pytest.approx(_pmf(s,k),abs=1e-4)
        assert empirical_mean(s)==pytest.approx(_mean(s),abs=1e-4)
        assert empirical_variance(s)==pytest.approx(_var(s),abs=1e-4)
