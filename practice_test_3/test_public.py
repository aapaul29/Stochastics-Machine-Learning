import pytest, scipy.stats
from solution import welch_t_statistic, welch_p_value, reject_null

XS=[2.1,2.5,2.3,2.8]; YS=[1.9,1.7,2.0,1.8]

def test_t_positive():  assert welch_t_statistic(XS,YS)>0
def test_p_range():     assert 0<welch_p_value(XS,YS)<1
def test_same_means():  assert welch_t_statistic([1,2,3],[1,2,3])==pytest.approx(0.0,abs=1e-4)
def test_reject():
    # Very different means → reject
    assert reject_null([10.0]*20,[0.0]*20,0.05)==True
def test_no_reject():
    # Identical samples
    assert reject_null([1,2,3],[1,2,3],0.05)==False
def test_scipy_agrees():
    t_ref,p_ref=scipy.stats.ttest_ind(XS,YS,equal_var=False)
    assert welch_t_statistic(XS,YS)==pytest.approx(round(t_ref,4),abs=1e-3)
    assert welch_p_value(XS,YS)==pytest.approx(round(p_ref,4),abs=1e-3)
