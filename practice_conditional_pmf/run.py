"""
Practice problem runner — mimics Code Expert's test feedback.

Usage:
    python run.py              # public tests only (self-check)
    python run.py --all        # public + hidden (submit for grading)
"""

import sys
import traceback
import argparse

# ── import student solution ───────────────────────────────────────────────────
try:
    from solution import compute_conditional_pmf
except ImportError as e:
    print(f"[ERROR] Could not import solution.py: {e}")
    sys.exit(1)

# ── reference implementation (for hidden tests) ───────────────────────────────
def _ref(samples, y_target, x_values):
    matching = [x for x, y in samples if y == y_target]
    n = len(matching)
    if n == 0:
        return [0.0] * len(x_values)
    return [round(matching.count(k) / n, 2) for k in x_values]

# ── test harness ──────────────────────────────────────────────────────────────
def approx_equal(a, b, tol=0.01):
    if len(a) != len(b):
        return False
    return all(abs(x - y) <= tol for x, y in zip(a, b))

def run_test(name, fn, public=True):
    tag = "PUBLIC" if public else "HIDDEN"
    try:
        result = fn()
        if result:
            print(f"  [PASS] [{tag}] {name}")
            return True
        else:
            print(f"  [FAIL] [{tag}] {name}")
            return False
    except Exception:
        print(f"  [ERROR] [{tag}] {name}")
        traceback.print_exc()
        return False

# ── public tests ──────────────────────────────────────────────────────────────
PUBLIC_TESTS = [
    ("Basic binary (example 1)",
     lambda: approx_equal(
         compute_conditional_pmf([(0,1),(1,1),(0,1),(1,0),(0,0)], 1, [0,1]),
         [0.67, 0.33])),
    ("Basic ternary (example 2)",
     lambda: approx_equal(
         compute_conditional_pmf([(2,0),(0,1),(1,0),(2,0),(0,0)], 0, [0,1,2]),
         [0.25, 0.25, 0.5])),
    ("All same X value → [1.0, 0.0]",
     lambda: approx_equal(
         compute_conditional_pmf([(0,1),(0,1),(0,1),(1,0)], 1, [0,1]),
         [1.0, 0.0])),
    ("PMF sums to 1.0",
     lambda: abs(sum(compute_conditional_pmf([(0,2),(1,2),(2,2),(0,2),(1,1)], 2, [0,1,2])) - 1.0) < 0.02),
    ("No matching Y → all zeros",
     lambda: compute_conditional_pmf([(0,0),(1,0),(0,0)], 1, [0,1]) == [0.0, 0.0]),
    ("Single sample",
     lambda: approx_equal(
         compute_conditional_pmf([(1,3)], 3, [0,1,2]),
         [0.0, 1.0, 0.0])),
    ("Return length == len(x_values)",
     lambda: len(compute_conditional_pmf([(0,0),(1,1)], 0, [0,1,2])) == 3),
]

# ── hidden tests ──────────────────────────────────────────────────────────────
import random

HIDDEN_TESTS = [
    ("Condition on Y=0",
     lambda: (lambda s: approx_equal(
         compute_conditional_pmf(s, 0, [0,1]), _ref(s, 0, [0,1])))(
         [(0,0),(0,0),(1,0),(1,1),(0,1)])),
    ("Larger X alphabet",
     lambda: (lambda s: approx_equal(
         compute_conditional_pmf(s, 1, [0,1,2,3]), _ref(s, 1, [0,1,2,3])))(
         [(i%4, i%3) for i in range(30)])),
    ("Large input (100k samples)",
     lambda: (lambda s: approx_equal(
         compute_conditional_pmf(s, 1, [0,1,2]), _ref(s, 1, [0,1,2])))(
         random.seed(42) or [(random.randint(0,2), random.randint(0,1)) for _ in range(100_000)])),
    ("Y never occurs, longer alphabet",
     lambda: compute_conditional_pmf([(k,0) for k in [0,1,2]], 5, [0,1,2]) == [0.0,0.0,0.0]),
    ("Uniform distribution → all 0.25",
     lambda: approx_equal(
         compute_conditional_pmf([(k,1) for k in [0,1,2,3]], 1, [0,1,2,3]),
         [0.25,0.25,0.25,0.25])),
    ("Rounding: 2/3 → 0.67, 1/3 → 0.33",
     lambda: (lambda r: abs(r[0]-0.67)<0.005 and abs(r[1]-0.33)<0.005)(
         compute_conditional_pmf([(0,1),(0,1),(1,1)], 1, [0,1]))),
    ("Single x_value → [1.0]",
     lambda: approx_equal(
         compute_conditional_pmf([(7,2),(7,2),(7,3)], 2, [7]),
         [1.0])),
    ("All samples match Y",
     lambda: approx_equal(
         compute_conditional_pmf([(0,1),(1,1),(1,1),(0,1)], 1, [0,1]),
         [0.5, 0.5])),
    ("X value with zero count → 0.0 slot",
     lambda: approx_equal(
         compute_conditional_pmf([(0,1),(0,1),(2,0)], 1, [0,1,2]),
         [1.0, 0.0, 0.0])),
    ("Randomized stress (20 cases)",
     lambda: all(
         approx_equal(
             compute_conditional_pmf(s, y, [0,1,2,3]),
             _ref(s, y, [0,1,2,3]))
         for s, y in [
             (random.seed(7) or None, None) or
             ([(random.randint(0,3), random.randint(0,2)) for _ in range(random.randint(10,200))],
              random.randint(0,2))
             for _ in range(20)])),
]

# ── main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Include hidden tests (grading mode)")
    args = parser.parse_args()

    print("\n" + "="*55)
    print("  CODE EXPERT RUNNER")
    print("="*55)

    passed = 0
    total = 0

    print("\n── Public Tests ──────────────────────────────────────")
    for name, fn in PUBLIC_TESTS:
        ok = run_test(name, fn, public=True)
        passed += ok
        total += 1

    if args.all:
        print("\n── Hidden Tests ──────────────────────────────────────")
        random.seed(42)
        for name, fn in HIDDEN_TESTS:
            ok = run_test(name, fn, public=False)
            passed += ok
            total += 1

    print("\n" + "="*55)
    pct = round(100 * passed / total) if total else 0
    print(f"  SCORE: {passed}/{total}  ({pct}%)")
    if pct == 100:
        print("  ✓ Full marks!")
    elif pct >= 70:
        print("  ~ Good — check the failing cases above.")
    else:
        print("  ✗ Keep going — re-read the problem statement.")
    print("="*55 + "\n")

if __name__ == "__main__":
    main()
