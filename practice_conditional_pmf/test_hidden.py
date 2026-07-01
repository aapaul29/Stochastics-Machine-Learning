"""
Hidden grading tests — NOT shown to student until after submission.
Run with:  pytest test_hidden.py
"""
import pytest
import random
from solution import compute_conditional_pmf


def approx_list(expected):
    return pytest.approx(expected, abs=0.01)


# ── reference implementation ──────────────────────────────────────────────────

def _ref(samples, y_target, x_values):
    matching = [x for x, y in samples if y == y_target]
    n = len(matching)
    if n == 0:
        return [0.0] * len(x_values)
    return [round(matching.count(k) / n, 2) for k in x_values]


# ── hidden tests ──────────────────────────────────────────────────────────────

def test_condition_on_y_zero():
    samples = [(0, 0), (0, 0), (1, 0), (1, 1), (0, 1)]
    assert compute_conditional_pmf(samples, 0, [0, 1]) == approx_list(_ref(samples, 0, [0, 1]))


def test_larger_x_alphabet():
    samples = [(i % 4, i % 3) for i in range(30)]
    assert compute_conditional_pmf(samples, 1, [0, 1, 2, 3]) == approx_list(_ref(samples, 1, [0, 1, 2, 3]))


def test_large_input():
    random.seed(42)
    samples = [(random.randint(0, 2), random.randint(0, 1)) for _ in range(100_000)]
    result = compute_conditional_pmf(samples, 1, [0, 1, 2])
    expected = _ref(samples, 1, [0, 1, 2])
    assert result == approx_list(expected)


def test_y_never_occurs_longer_alphabet():
    samples = [(k, 0) for k in [0, 1, 2]]
    result = compute_conditional_pmf(samples, 5, [0, 1, 2])
    assert result == [0.0, 0.0, 0.0]


def test_uniform_distribution():
    """Equal counts → each probability should be 1/len(x_values)."""
    x_values = [0, 1, 2, 3]
    samples = [(k, 1) for k in x_values]  # one of each
    result = compute_conditional_pmf(samples, 1, x_values)
    assert result == approx_list([0.25, 0.25, 0.25, 0.25])


def test_rounding_correctness():
    """2/3 must round to 0.67, not 0.6667."""
    samples = [(0, 1), (0, 1), (1, 1)]
    result = compute_conditional_pmf(samples, 1, [0, 1])
    assert result[0] == pytest.approx(0.67, abs=0.005)
    assert result[1] == pytest.approx(0.33, abs=0.005)


def test_single_x_value():
    """x_values has only one entry — PMF must be [1.0]."""
    samples = [(7, 2), (7, 2), (7, 3)]
    result = compute_conditional_pmf(samples, 2, [7])
    assert result == approx_list([1.0])


def test_all_samples_match_y():
    """Every sample has Y = y_target."""
    samples = [(0, 1), (1, 1), (1, 1), (0, 1)]
    result = compute_conditional_pmf(samples, 1, [0, 1])
    assert result == approx_list([0.5, 0.5])


def test_x_values_with_zero_count():
    """Some x_values never appear for the given y_target → those slots are 0.0."""
    samples = [(0, 1), (0, 1), (2, 0)]
    result = compute_conditional_pmf(samples, 1, [0, 1, 2])
    assert result == approx_list([1.0, 0.0, 0.0])


def test_consistent_with_reference_random():
    random.seed(7)
    for _ in range(20):
        n = random.randint(10, 200)
        samples = [(random.randint(0, 3), random.randint(0, 2)) for _ in range(n)]
        y_t = random.randint(0, 2)
        x_vals = [0, 1, 2, 3]
        result = compute_conditional_pmf(samples, y_t, x_vals)
        expected = _ref(samples, y_t, x_vals)
        assert result == approx_list(expected), f"Failed for y_target={y_t}"
