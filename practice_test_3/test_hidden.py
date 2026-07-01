import pytest,random,scipy.stats
from solution import welch_t_statistic,welch_p_value,reject_null

def _t(xs,ys): return round(scipy.stats.ttest_ind(xs,ys,equal_var=False).statistic,4)
def _p(xs,ys): return round(scipy.stats.ttest_ind(xs,ys,equal_var=False).pvalue,4)

def test_exact():
    xs=[2.1,2.5,2.3,2.8]; ys=[1.9,1.7,2.0,1.8]
    assert welch_t_statistic(xs,ys)==pytest.approx(_t(xs,ys),abs=1e-3)
    assert welch_p_value(xs,ys)==pytest.approx(_p(xs,ys),abs=1e-3)

def test_unequal_sizes():
    xs=[1,2,3,4,5]; ys=[10,11,12]
    assert reject_null(xs,ys,0.05)==(_p(xs,ys)<0.05)

def test_stress():
    random.seed(7)
    for _ in range(15):
        m=random.randint(5,100); n=random.randint(5,100)
        xs=[random.gauss(random.uniform(0,2),1) for _ in range(m)]
        ys=[random.gauss(random.uniform(0,2),1) for _ in range(n)]
        assert welch_t_statistic(xs,ys)==pytest.approx(_t(xs,ys),abs=1e-3)
        assert welch_p_value(xs,ys)==pytest.approx(_p(xs,ys),abs=1e-3)
        assert reject_null(xs,ys,0.05)==(_p(xs,ys)<0.05)
