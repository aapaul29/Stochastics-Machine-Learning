import pytest,random,statistics,numpy as np
from solution import sample_mean,sample_variance,sample_median,sample_iqr

def test_large():
    random.seed(42); d=[random.gauss(10,2) for _ in range(10000)]
    assert abs(sample_mean(d)-10)<0.1
    assert sample_variance(d)==pytest.approx(statistics.variance(d),abs=0.1)

def test_sorted_unchanged():
    d=[1,2,3,4,5]
    assert sample_median(d)==pytest.approx(3.0,abs=1e-4)

def test_iqr_uniform():
    d=list(range(0,101))
    assert sample_iqr(d)==pytest.approx(np.percentile(d,75)-np.percentile(d,25),abs=1.0)

def test_rounding():
    r=sample_mean([1,2,3]); assert r==round(r,4)

def test_stress():
    random.seed(7)
    for _ in range(10):
        d=[random.gauss(0,3) for _ in range(random.randint(2,500))]
        assert sample_mean(d)==pytest.approx(statistics.mean(d),abs=1e-3)
        assert sample_variance(d)==pytest.approx(statistics.variance(d),abs=1e-3)
        assert sample_median(d)==pytest.approx(statistics.median(d),abs=1e-3)
