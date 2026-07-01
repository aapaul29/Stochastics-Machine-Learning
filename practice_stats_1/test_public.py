import pytest
from solution import sample_mean,sample_variance,sample_median,sample_iqr

D=[2,4,4,4,5,5,7,9]

def test_mean():     assert sample_mean(D)==pytest.approx(5.0,abs=1e-4)
def test_var():      assert sample_variance(D)==pytest.approx(32/7,abs=1e-3)
def test_median_even(): assert sample_median([1,2,3,4])==pytest.approx(2.5,abs=1e-4)
def test_median_odd():  assert sample_median([1,2,3])==pytest.approx(2.0,abs=1e-4)
def test_var_n1():   assert sample_variance([5])==0.0
def test_iqr():      assert sample_iqr(D)==pytest.approx(2.5,abs=0.1)
def test_mean_const():assert sample_mean([3,3,3])==pytest.approx(3.0,abs=1e-4)
