import pytest,random,math
from solution import empirical_covariance,empirical_correlation

def _cov(xs,ys):
    n=len(xs)
    if n<=1: return 0.0
    mx=sum(xs)/n; my=sum(ys)/n
    return round(sum((x-mx)*(y-my) for x,y in zip(xs,ys))/(n-1),4)

def _std(xs):
    n=len(xs)
    if n<=1: return 0.0
    m=sum(xs)/n; return math.sqrt(sum((x-m)**2 for x in xs)/(n-1))

def _corr(xs,ys):
    sx,sy=_std(xs),_std(ys)
    if sx==0 or sy==0: return 0.0
    return round(_cov(xs,ys)/(sx*sy),4)

def test_two_elements():
    assert empirical_covariance([0,2],[0,4])==pytest.approx(_cov([0,2],[0,4]),abs=1e-4)

def test_corr_range():
    import random; random.seed(7)
    for _ in range(10):
        xs=[random.gauss(0,1) for _ in range(50)]
        ys=[random.gauss(0,1) for _ in range(50)]
        r=empirical_correlation(xs,ys)
        assert -1.0<=r<=1.0

def test_rounding():
    r=empirical_covariance([1,2,3],[1,2,3]); assert r==round(r,4)

def test_stress():
    random.seed(42)
    for _ in range(20):
        n=random.randint(2,200)
        xs=[random.gauss(0,2) for _ in range(n)]
        ys=[x+random.gauss(0,1) for x in xs]
        assert empirical_covariance(xs,ys)==pytest.approx(_cov(xs,ys),abs=1e-3)
        assert empirical_correlation(xs,ys)==pytest.approx(_corr(xs,ys),abs=1e-3)
