import pytest, random, math
from solution import simulate_exponential, simulate_uniform

def test_exp_length():   assert len(simulate_exponential(1.0,10,42))==10
def test_unif_length():  assert len(simulate_uniform(0,1,10,42))==10
def test_exp_positive(): assert all(x>=0 for x in simulate_exponential(2.0,100,0))
def test_unif_range():   assert all(0<=x<=5 for x in simulate_uniform(0,5,100,0))
def test_exp_seed():
    a=simulate_exponential(1.0,5,42); b=simulate_exponential(1.0,5,42)
    assert a==b
def test_exp_mean_approx():
    # E[Exp(2)] = 0.5; sample mean of 10k samples should be close
    s=simulate_exponential(2.0,10000,99)
    assert abs(sum(s)/len(s)-0.5)<0.05
def test_unif_mean_approx():
    s=simulate_uniform(2,4,10000,99)
    assert abs(sum(s)/len(s)-3.0)<0.05
