"""Hidden grading tests."""
import pytest, random
from solution import total_probability, most_likely_cause

def _ref_total(priors, conditionals):
    return round(sum(p * c for p, c in zip(priors, conditionals)), 4)

def _ref_cause(priors, conditionals):
    unnorm = [p * c for p, c in zip(priors, conditionals)]
    return unnorm.index(max(unnorm))

def test_four_classes():
    p = [0.4, 0.3, 0.2, 0.1]
    c = [0.05, 0.1, 0.2, 0.5]
    assert total_probability(p, c) == pytest.approx(_ref_total(p, c), abs=0.0001)
    assert most_likely_cause(p, c) == _ref_cause(p, c)

def test_all_same_conditional():
    # P(B|A_i) same for all → posterior = prior → most likely = argmax prior
    p = [0.1, 0.5, 0.4]
    c = [0.3, 0.3, 0.3]
    assert most_likely_cause(p, c) == 1

def test_large_partition():
    random.seed(7)
    n = 50
    raw = [random.random() for _ in range(n)]
    s = sum(raw)
    priors = [r/s for r in raw]
    conditionals = [random.random() for _ in range(n)]
    assert total_probability(priors, conditionals) == pytest.approx(_ref_total(priors, conditionals), abs=0.0001)
    assert most_likely_cause(priors, conditionals) == _ref_cause(priors, conditionals)

def test_one_dominant_cause():
    p = [0.01] * 9 + [0.91]
    c = [0.9] * 9 + [0.01]
    # unnorm for first 9: 0.01*0.9=0.009; last: 0.91*0.01=0.0091 — first index wins
    assert most_likely_cause(p, c) == _ref_cause(p, c)

def test_stress_total():
    random.seed(42)
    for _ in range(30):
        n = random.randint(2, 20)
        raw = [random.random() for _ in range(n)]
        s = sum(raw)
        priors = [r/s for r in raw]
        conditionals = [random.random() for _ in range(n)]
        assert total_probability(priors, conditionals) == pytest.approx(_ref_total(priors, conditionals), abs=0.0001)

def test_stress_cause():
    random.seed(13)
    for _ in range(30):
        n = random.randint(2, 20)
        raw = [random.random() for _ in range(n)]
        s = sum(raw)
        priors = [r/s for r in raw]
        conditionals = [random.random() for _ in range(n)]
        assert most_likely_cause(priors, conditionals) == _ref_cause(priors, conditionals)
