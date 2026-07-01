import pytest
from solution import running_average, lln_converges, convergence_index

def test_ra_length():  assert len(running_average([1,2,3,4]))==4
def test_ra_values():  assert running_average([2,4,6])==pytest.approx([2.0,3.0,4.0],abs=1e-4)
def test_ra_single():  assert running_average([5])==pytest.approx([5.0],abs=1e-4)
def test_converges_true():
    s=[1.0]*100+[1.05]*100
    assert lln_converges(s,1.025,0.1)==True
def test_converges_false():
    assert lln_converges([100.0]*10,0.0,0.1)==False
def test_ra_rounding():
    ra=running_average([1,2]); assert all(x==round(x,4) for x in ra)
def test_convergence_index():
    s=[1.0]*1000
    assert convergence_index(s,1.0,0.01)==1
