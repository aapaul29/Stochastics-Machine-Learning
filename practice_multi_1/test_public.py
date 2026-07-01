import pytest
from solution import empirical_joint,empirical_marginal_x,empirical_marginal_y,are_independent

S=[(0,0),(0,1),(1,0),(1,1)]

def test_joint():      assert empirical_joint(S,0,0)==pytest.approx(0.25,abs=1e-4)
def test_margx():      assert empirical_marginal_x(S,0)==pytest.approx(0.5,abs=1e-4)
def test_margy():      assert empirical_marginal_y(S,1)==pytest.approx(0.5,abs=1e-4)
def test_indep():      assert are_independent(S,[0,1],[0,1],0.01)==True
def test_not_indep():
    s=[(0,0),(0,0),(1,1),(1,1)]  # X=Y always
    assert are_independent(s,[0,1],[0,1],0.01)==False
def test_joint_unseen(): assert empirical_joint(S,0,9)==pytest.approx(0.0,abs=1e-4)
def test_margx_sums():   assert sum(empirical_marginal_x(S,x) for x in [0,1])==pytest.approx(1.0,abs=1e-3)
