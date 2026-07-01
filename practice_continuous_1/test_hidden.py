import pytest,random,math,scipy.stats
from solution import exp_pdf,exp_cdf,exp_quantile

def test_pdf_x0():     assert exp_pdf(3.0,0.0)==pytest.approx(3.0,abs=1e-4)
def test_cdf_large_x():assert exp_cdf(1.0,20)==pytest.approx(1.0,abs=1e-4)
def test_quantile_inv():
    lam=2.5
    for p in [0.1,0.25,0.5,0.75,0.9]:
        q=exp_quantile(lam,p)
        assert abs(exp_cdf(lam,q)-p)<1e-3

def test_rounding():
    r=exp_pdf(1.0,1.0); assert r==round(r,4)

def test_stress():
    random.seed(42)
    for _ in range(20):
        lam=random.uniform(0.5,5); x=random.uniform(0,5)
        assert exp_pdf(lam,x)==pytest.approx(round(scipy.stats.expon.pdf(x,scale=1/lam),4),abs=1e-4)
        assert exp_cdf(lam,x)==pytest.approx(round(scipy.stats.expon.cdf(x,scale=1/lam),4),abs=1e-4)
