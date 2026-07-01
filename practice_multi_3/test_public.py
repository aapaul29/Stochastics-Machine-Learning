import pytest, math, scipy.stats
from solution import mixture_pdf, mixture_mean, mixture_variance

W=[0.5,0.5]; M=[-1.0,1.0]; S=[0.5,0.5]

def test_mean_symmetric():  assert mixture_mean(W,M)==pytest.approx(0.0,abs=1e-4)
def test_variance():        assert mixture_variance(W,M,S)==pytest.approx(1.25,abs=1e-4)
def test_pdf_positive():    assert mixture_pdf(0.0,W,M,S)>0
def test_single_component():
    w=[1.0]; m=[2.0]; s=[1.0]
    assert mixture_pdf(2.0,w,m,s)==pytest.approx(round(scipy.stats.norm.pdf(2.0,2.0,1.0),4),abs=1e-4)
    assert mixture_mean(w,m)==pytest.approx(2.0,abs=1e-4)
    assert mixture_variance(w,m,s)==pytest.approx(1.0,abs=1e-4)
def test_pdf_integrates():
    import numpy as np
    xs=list(range(-100,101)); dx=0.1
    total=sum(mixture_pdf(x*dx,W,M,S)*dx for x in range(-100,101))
    assert abs(total-1.0)<0.05
