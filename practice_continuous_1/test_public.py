import pytest, math, scipy.stats
from solution import exp_pdf, exp_cdf, exp_quantile

def test_pdf_basic():   assert exp_pdf(2.0,1.0)==pytest.approx(2*math.exp(-2),abs=1e-4)
def test_cdf_basic():   assert exp_cdf(2.0,1.0)==pytest.approx(1-math.exp(-2),abs=1e-4)
def test_quantile():    assert exp_quantile(2.0,0.5)==pytest.approx(math.log(2)/2,abs=1e-4)
def test_pdf_neg():     assert exp_pdf(1.0,-1.0)==0.0
def test_cdf_neg():     assert exp_cdf(1.0,-1.0)==0.0
def test_cdf_zero():    assert exp_cdf(1.0,0.0)==pytest.approx(0.0,abs=1e-4)
def test_quantile_p0():  assert exp_quantile(1.0,1e-9)==pytest.approx(0.0,abs=1e-3)
