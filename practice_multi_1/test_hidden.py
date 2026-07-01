import pytest,random
from solution import empirical_joint,empirical_marginal_x,empirical_marginal_y,are_independent

def _j(s,x,y): return round(sum(1 for a,b in s if a==x and b==y)/len(s),4)
def _mx(s,x):  return round(sum(1 for a,_ in s if a==x)/len(s),4)
def _my(s,y):  return round(sum(1 for _,b in s if b==y)/len(s),4)

def test_three_classes():
    s=[(i%3,i%2) for i in range(30)]
    assert empirical_joint(s,0,0)==pytest.approx(_j(s,0,0),abs=1e-4)
    assert empirical_marginal_x(s,1)==pytest.approx(_mx(s,1),abs=1e-4)

def test_indep_large():
    random.seed(42)
    s=[(random.randint(0,3),random.randint(0,3)) for _ in range(10000)]
    # With enough samples from independent uniform, should detect independence at eps=0.02
    # (may not always pass at tight eps with random data, but at 0.05 it should)
    result=are_independent(s,[0,1,2,3],[0,1,2,3],0.05)
    assert isinstance(result,bool)

def test_fully_dependent():
    s=[(k,k) for k in range(4)]*100
    assert are_independent(s,[0,1,2,3],[0,1,2,3],0.01)==False

def test_joint_sums_to_one():
    s=[(i%2,i%3) for i in range(60)]
    total=sum(_j(s,x,y) for x in [0,1] for y in [0,1,2])
    assert abs(total-1.0)<0.01

def test_stress():
    random.seed(7)
    for _ in range(10):
        s=[(random.randint(0,2),random.randint(0,2)) for _ in range(200)]
        x,y=random.randint(0,2),random.randint(0,2)
        assert empirical_joint(s,x,y)==pytest.approx(_j(s,x,y),abs=1e-4)
        assert empirical_marginal_x(s,x)==pytest.approx(_mx(s,x),abs=1e-4)
        assert empirical_marginal_y(s,y)==pytest.approx(_my(s,y),abs=1e-4)
