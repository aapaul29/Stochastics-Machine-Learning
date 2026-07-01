import pytest, math
from solution import mle_exponential, mle_normal

def test_exp_basic():
    assert mle_exponential([1.0,2.0,3.0])==pytest.approx(0.5,abs=1e-4)

def test_exp_constant():
    assert mle_exponential([2.0,2.0,2.0])==pytest.approx(0.5,abs=1e-4)

def test_normal_basic():
    mu,sig=mle_normal([1.0,2.0,3.0])
    assert mu==pytest.approx(2.0,abs=1e-4)
    assert sig==pytest.approx(math.sqrt(2/3),abs=1e-4)

def test_normal_constant():
    mu,sig=mle_normal([5.0,5.0,5.0])
    assert mu==pytest.approx(5.0,abs=1e-4); assert sig==pytest.approx(0.0,abs=1e-4)

def test_exp_single():
    assert mle_exponential([4.0])==pytest.approx(0.25,abs=1e-4)

def test_mle_uses_biased_sigma():
    # N=2: biased sigma = |x1-x2|/2, not sqrt((x1-x2)^2/1)
    mu,sig=mle_normal([0.0,2.0])
    assert mu==pytest.approx(1.0,abs=1e-4)
    assert sig==pytest.approx(1.0,abs=1e-4)  # sqrt((1+1)/2)=1
