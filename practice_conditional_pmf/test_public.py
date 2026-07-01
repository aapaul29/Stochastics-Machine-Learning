"""
Public test cases — run with:  pytest test_public.py
These mirror what the grader checks but are not exhaustive.
"""
import pytest
from solution import compute_conditional_pmf


# ── helpers ──────────────────────────────────────────────────────────────────

def approx_list(expected, rel=1e-2):
    """Check each element up to 2 decimal places."""
    return pytest.approx(expected, abs=0.01)


# ── test cases ────────────────────────────────────────────────────────────────

def test_basic_binary():
    """Example from problem statement (binary X and Y)."""
    samples = [(0, 1), (1, 1), (0, 1), (1, 0), (0, 0)]
    result = compute_conditional_pmf(samples, y_target=1, x_values=[0, 1])
    assert result == approx_list([0.67, 0.33])


def test_basic_ternary():
    """Example from problem statement (ternary X)."""
    samples = [(2, 0), (0, 1), (1, 0), (2, 0), (0, 0)]
    result = compute_conditional_pmf(samples, y_target=0, x_values=[0, 1, 2])
    assert result == approx_list([0.25, 0.25, 0.5])


def test_all_same_x():
    """All matching samples have the same X value → one entry is 1.0."""
    samples = [(0, 1), (0, 1), (0, 1), (1, 0)]
    result = compute_conditional_pmf(samples, y_target=1, x_values=[0, 1])
    assert result == approx_list([1.0, 0.0])


def test_pmf_sums_to_one():
    """The returned PMF must sum to 1.0 (up to rounding)."""
    samples = [(0, 2), (1, 2), (2, 2), (0, 2), (1, 1)]
    result = compute_conditional_pmf(samples, y_target=2, x_values=[0, 1, 2])
    assert abs(sum(result) - 1.0) < 0.02


def test_no_matching_y():
    """No sample has Y = y_target → return list of zeros."""
    samples = [(0, 0), (1, 0), (0, 0)]
    result = compute_conditional_pmf(samples, y_target=1, x_values=[0, 1])
    assert result == [0.0, 0.0]


def test_single_sample():
    """Only one sample, and it matches."""
    samples = [(1, 3)]
    result = compute_conditional_pmf(samples, y_target=3, x_values=[0, 1, 2])
    assert result == approx_list([0.0, 1.0, 0.0])


def test_return_length():
    """Output length must equal len(x_values)."""
    samples = [(0, 0), (1, 1)]
    result = compute_conditional_pmf(samples, y_target=0, x_values=[0, 1, 2])
    assert len(result) == 3
