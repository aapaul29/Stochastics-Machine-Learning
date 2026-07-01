import pytest, math, scipy.stats
from solution import confidence_interval

S=[2.1,1.9,2.0,2.2,1.8]

def test_basic():
    lo,hi=confidence_interval(S,0.5,0.05)
    assert lo==pytest.approx(2.0-1.96*0.5/math.sqrt(5),abs=1e-2)
    assert hi==pytest.approx(2.0+1.96*0.5/math.sqrt(5),abs=1e-2)

def test_symmetric():
    lo,hi=confidence_interval([0.0]*10,1.0,0.05)
    assert lo==-hi

def test_wider_at_99():
    lo95,hi95=confidence_interval(S,1.0,0.05)
    lo99,hi99=confidence_interval(S,1.0,0.01)
    assert hi99-lo99 > hi95-lo95

def test_mean_in_ci():
    lo,hi=confidence_interval(S,0.5,0.05)
    assert lo < 2.0 < hi

def test_rounding():
    lo,hi=confidence_interval(S,0.5,0.05)
    assert lo==round(lo,4); assert hi==round(hi,4)
