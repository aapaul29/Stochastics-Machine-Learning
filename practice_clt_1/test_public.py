import pytest, scipy.stats
from solution import clt_mean, clt_variance, clt_prob

poisson3 = scipy.stats.poisson(mu=3)
norm01   = scipy.stats.norm(0,1)
unif     = scipy.stats.uniform(0,1)

def test_mean_poisson():   assert clt_mean(poisson3,10)==pytest.approx(30.0,abs=1e-4)
def test_var_poisson():    assert clt_variance(poisson3,10)==pytest.approx(30.0,abs=1e-4)
def test_mean_norm():      assert clt_mean(norm01,5)==pytest.approx(0.0,abs=1e-4)
def test_var_unif():       assert clt_variance(unif,12)==pytest.approx(1.0,abs=1e-3)
def test_prob_wide():      assert clt_prob(norm01,100,-1000,1000)==pytest.approx(1.0,abs=1e-4)
def test_prob_positive():  assert 0 < clt_prob(poisson3,100,270,330) < 1
def test_prob_symmetric(): assert clt_prob(norm01,10,-1,1)==pytest.approx(clt_prob(norm01,10,-1,1),abs=1e-8)
