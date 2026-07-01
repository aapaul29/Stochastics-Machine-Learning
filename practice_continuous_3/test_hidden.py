import pytest,random,math
from solution import simulate_exponential,simulate_uniform

def ref_exp(lam,n,seed):
    random.seed(seed)
    return [round(-math.log(1-random.random())/lam,4) for _ in range(n)]

def ref_unif(a,b,n,seed):
    random.seed(seed)
    return [round(a+(b-a)*random.random(),4) for _ in range(n)]

def test_exp_exact():    assert simulate_exponential(1.0,5,42)==ref_exp(1.0,5,42)
def test_unif_exact():   assert simulate_uniform(0,1,5,42)==ref_unif(0,1,5,42)
def test_exp_lam2():     assert simulate_exponential(2.0,5,7)==ref_exp(2.0,5,7)
def test_unif_shifted(): assert simulate_uniform(3,7,5,7)==ref_unif(3,7,5,7)
def test_exp_large():    assert simulate_exponential(0.5,1000,1)==ref_exp(0.5,1000,1)
def test_rounding():
    s=simulate_exponential(1.0,5,42)
    assert all(x==round(x,4) for x in s)
