import pytest, scipy.stats
from solution import standardize, normal_prob, normal_quantile

def test_std_basic():    assert standardize(1.5,1.0,0.5)==pytest.approx(1.0,abs=1e-4)
def test_std_zero():     assert standardize(2.0,2.0,1.0)==pytest.approx(0.0,abs=1e-4)
def test_prob_68():      assert normal_prob(0,1,-1,1)==pytest.approx(0.6827,abs=1e-3)
def test_prob_95():      assert normal_prob(0,1,-1.96,1.96)==pytest.approx(0.95,abs=1e-2)
def test_prob_full():    assert normal_prob(0,1,-10,10)==pytest.approx(1.0,abs=1e-4)
def test_quantile_975(): assert normal_quantile(0,1,0.975)==pytest.approx(1.96,abs=1e-2)
def test_quantile_med(): assert normal_quantile(5,2,0.5)==pytest.approx(5.0,abs=1e-4)
