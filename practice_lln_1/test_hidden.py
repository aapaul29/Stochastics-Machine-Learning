import pytest,random
from solution import running_average,lln_converges,convergence_index

def _ra(s):
    out=[]; total=0
    for i,x in enumerate(s,1): total+=x; out.append(round(total/i,4))
    return out

def test_exact_ra():
    s=[1.0,3.0,2.0,4.0]
    assert running_average(s)==pytest.approx(_ra(s),abs=1e-4)

def test_large_sample():
    random.seed(42); s=[random.gauss(5,1) for _ in range(10000)]
    assert lln_converges(s,5.0,0.05)==True

def test_always_wrong():
    assert lln_converges([10.0]*100,0.0,0.1)==False

def test_conv_index_basic():
    s=[0.0,0.0,1.0,1.0,1.0]
    idx=convergence_index(s,1.0,0.01)
    assert idx<=5

def test_rounding():
    ra=running_average([1,2,3])
    assert all(x==round(x,4) for x in ra)

def test_stress():
    random.seed(7)
    for _ in range(5):
        s=[random.gauss(0,1) for _ in range(1000)]
        ra=running_average(s); ref=_ra(s)
        assert all(abs(a-b)<1e-3 for a,b in zip(ra,ref))
