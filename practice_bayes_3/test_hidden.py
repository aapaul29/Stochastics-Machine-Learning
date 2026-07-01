"""Hidden grading tests."""
import pytest, random
from solution import empirical_prior, empirical_posterior, most_likely_class

def _prior(samples, c):
    return round(sum(1 for _, y in samples if y == c) / len(samples), 4)

def _posterior(samples, x_val, c):
    match_x = [y for x, y in samples if x == x_val]
    if not match_x: return 0.0
    return round(sum(1 for y in match_x if y == c) / len(match_x), 4)

def _mlc(samples, x_val, classes):
    posts = {c: _posterior(samples, x_val, c) for c in classes}
    if all(v == 0.0 for v in posts.values()):
        priors = {c: _prior(samples, c) for c in classes}
        return min((c for c in classes if priors[c] == max(priors.values())))
    return min((c for c in classes if posts[c] == max(posts.values())))

S = [(0,0),(0,1),(0,0),(1,1),(1,1),(0,1)]

def test_three_classes():
    s = [(0,0),(1,1),(2,2),(0,1),(1,2),(0,0)]
    assert empirical_prior(s, 0) == pytest.approx(_prior(s, 0), abs=0.0001)
    assert empirical_posterior(s, 0, 0) == pytest.approx(_posterior(s, 0, 0), abs=0.0001)

def test_large_input():
    random.seed(42)
    s = [(random.randint(0,3), random.randint(0,2)) for _ in range(100_000)]
    c = random.randint(0,2)
    assert empirical_prior(s, c) == pytest.approx(_prior(s, c), abs=0.0001)
    assert empirical_posterior(s, 2, c) == pytest.approx(_posterior(s, 2, c), abs=0.0001)

def test_most_likely_three_classes():
    s = [(0,0)]*5 + [(0,1)]*3 + [(0,2)]*2
    assert most_likely_class(s, 0, [0,1,2]) == _mlc(s, 0, [0,1,2])

def test_unseen_x_prior_fallback():
    s = [(0,0)]*2 + [(0,1)]*8
    # unseen X=5 → falls back to prior → class 1 wins
    assert most_likely_class(s, 5, [0,1]) == 1

def test_rounding_4dp():
    r = empirical_prior(S, 0)
    assert r == round(r, 4)

def test_stress():
    random.seed(7)
    for _ in range(20):
        n = random.randint(20, 500)
        s = [(random.randint(0,4), random.randint(0,3)) for _ in range(n)]
        c = random.randint(0,3)
        x = random.randint(0,4)
        assert empirical_prior(s, c) == pytest.approx(_prior(s, c), abs=0.0001)
        assert empirical_posterior(s, x, c) == pytest.approx(_posterior(s, x, c), abs=0.0001)
        assert most_likely_class(s, x, [0,1,2,3]) == _mlc(s, x, [0,1,2,3])
