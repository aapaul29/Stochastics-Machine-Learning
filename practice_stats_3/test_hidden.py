import pytest,random,math
from solution import mle_exponential,mle_normal

def _exp(s): return round(1/(sum(s)/len(s)),4)
def _norm(s):
    mu=sum(s)/len(s); sig=math.sqrt(sum((x-mu)**2 for x in s)/len(s))
    return round(mu,4),round(sig,4)

def test_large_exp():
    random.seed(42)
    s=[random.expovariate(2) for _ in range(10000)]
    assert abs(mle_exponential(s)-2)<0.1

def test_large_normal():
    random.seed(42)
    s=[random.gauss(3,1.5) for _ in range(10000)]
    mu,sig=mle_normal(s)
    assert abs(mu-3)<0.05; assert abs(sig-1.5)<0.05

def test_rounding():
    r=mle_exponential([1,2,3]); assert r==round(r,4)

def test_stress():
    random.seed(7)
    for _ in range(20):
        s=[random.expovariate(random.uniform(0.5,3)) for _ in range(random.randint(2,500))]
        assert mle_exponential(s)==pytest.approx(_exp(s),abs=1e-4)
        mu,sig=mle_normal(s); em,es=_norm(s)
        assert mu==pytest.approx(em,abs=1e-4); assert sig==pytest.approx(es,abs=1e-4)
