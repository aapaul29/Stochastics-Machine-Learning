import pytest, scipy.stats
from solution import t_statistic, p_value, reject_null

S=[2.5,3.1,2.8,3.2,2.9]

def test_t_sign():      assert t_statistic(S,3.0)<0  # mean<mu0 → t<0
def test_p_range():     assert 0 < p_value(S,3.0) < 1
def test_no_reject():   assert reject_null(S,3.0,0.05)==False
def test_reject():
    # Clearly different from 0
    assert reject_null([10.0]*20,0.0,0.05)==True
def test_t_zero():
    # mean == mu0 → t=0
    assert t_statistic([1.0,2.0,3.0],2.0)==pytest.approx(0.0,abs=1e-4)
def test_p_one_at_t0():
    # t=0 → p=1
    assert p_value([1.0,2.0,3.0],2.0)==pytest.approx(1.0,abs=1e-4)
def test_rounding():
    r=t_statistic(S,3.0); assert r==round(r,4)
