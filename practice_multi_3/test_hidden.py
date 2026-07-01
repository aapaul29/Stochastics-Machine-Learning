import pytest,random,math,scipy.stats
from solution import mixture_pdf,mixture_mean,mixture_variance

def _phi(x,mu,sig): return scipy.stats.norm.pdf(x,mu,sig)
def _pdf(x,w,m,s): return round(sum(wi*_phi(x,mi,si) for wi,mi,si in zip(w,m,s)),4)
def _mean(w,m): return round(sum(wi*mi for wi,mi in zip(w,m)),4)
def _var(w,m,s): return round(sum(wi*(si**2+mi**2) for wi,mi,si in zip(w,m,s))-_mean(w,m)**2,4)

def test_three_components():
    w=[0.3,0.4,0.3]; m=[0,2,4]; s=[1,1,1]
    assert mixture_pdf(2.0,w,m,s)==pytest.approx(_pdf(2.0,w,m,s),abs=1e-4)
    assert mixture_mean(w,m)==pytest.approx(_mean(w,m),abs=1e-4)
    assert mixture_variance(w,m,s)==pytest.approx(_var(w,m,s),abs=1e-4)

def test_pdf_nonnegative():
    w=[0.5,0.5]; m=[-5,5]; s=[1,1]
    assert all(mixture_pdf(x,w,m,s)>=0 for x in range(-10,11))

def test_rounding():
    r=mixture_mean([0.5,0.5],[-1.0,1.0]); assert r==round(r,4)

def test_stress():
    random.seed(7)
    for _ in range(10):
        k=random.randint(2,5)
        raw=[random.random() for _ in range(k)]; s=sum(raw); w=[r/s for r in raw]
        m=[random.uniform(-3,3) for _ in range(k)]
        s2=[random.uniform(0.5,2) for _ in range(k)]
        x=random.uniform(-5,5)
        assert mixture_pdf(x,w,m,s2)==pytest.approx(_pdf(x,w,m,s2),abs=1e-4)
        assert mixture_mean(w,m)==pytest.approx(_mean(w,m),abs=1e-4)
        assert mixture_variance(w,m,s2)==pytest.approx(_var(w,m,s2),abs=1e-3)
