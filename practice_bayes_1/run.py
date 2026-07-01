"""
Practice problem runner.

Usage:
    python run.py          # public tests only
    python run.py --all    # public + hidden (grading)
"""
import sys, argparse, traceback, random

try:
    from solution import marginal_probability, bayes_posterior
except ImportError as e:
    print(f"[ERROR] Could not import solution.py: {e}"); sys.exit(1)

def _ref_marginal(p, l, lc):
    return round(l * p + lc * (1 - p), 4)

def _ref_posterior(p, l, lc):
    pe = l * p + lc * (1 - p)
    return round((l * p) / pe, 4)

def approx(a, b, tol=0.0001):
    return abs(a - b) <= tol

def run_test(name, fn, public=True):
    tag = "PUBLIC" if public else "HIDDEN"
    try:
        ok = fn()
        print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}")
        return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}")
        traceback.print_exc()
        return False

PUBLIC_TESTS = [
    ("Marginal: disease example",
     lambda: approx(marginal_probability(0.01, 0.99, 0.05), 0.0594)),
    ("Posterior: disease example",
     lambda: approx(bayes_posterior(0.01, 0.99, 0.05), 0.1667)),
    ("Marginal: symmetric prior",
     lambda: approx(marginal_probability(0.5, 0.8, 0.2), 0.5)),
    ("Posterior: symmetric prior",
     lambda: approx(bayes_posterior(0.5, 0.8, 0.2), 0.8)),
    ("Marginal: certain evidence",
     lambda: approx(marginal_probability(0.3, 1.0, 0.0), 0.3)),
    ("Posterior: certain evidence → 1.0",
     lambda: approx(bayes_posterior(0.3, 1.0, 0.0), 1.0)),
    ("Output rounded to 4 dp",
     lambda: bayes_posterior(0.01, 0.99, 0.05) == round(bayes_posterior(0.01, 0.99, 0.05), 4)),
]

HIDDEN_TESTS = [
    ("Low prior marginal",
     lambda: approx(marginal_probability(0.001, 0.95, 0.1), _ref_marginal(0.001, 0.95, 0.1))),
    ("Low prior posterior",
     lambda: approx(bayes_posterior(0.001, 0.95, 0.1), _ref_posterior(0.001, 0.95, 0.1))),
    ("High prior posterior",
     lambda: approx(bayes_posterior(0.9, 0.7, 0.4), _ref_posterior(0.9, 0.7, 0.4))),
    ("Equal likelihoods → posterior = prior",
     lambda: approx(bayes_posterior(0.3, 0.6, 0.6), 0.3)),
    ("Zero complement → posterior = 1",
     lambda: approx(bayes_posterior(0.5, 0.8, 0.0), 1.0)),
    ("Marginal symmetry",
     lambda: approx(marginal_probability(0.3, 0.9, 0.2), marginal_probability(0.7, 0.2, 0.9))),
    ("Stress test (50 random cases)",
     lambda: all(
         approx(marginal_probability(p, l, lc), _ref_marginal(p, l, lc)) and
         approx(bayes_posterior(p, l, lc), _ref_posterior(p, l, lc))
         for p, l, lc in [
             (random.uniform(0.01, 0.99), random.uniform(0.01, 1.0), random.uniform(0.01, 1.0))
             for _ in range(50)
         ]
     )),
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    random.seed(99)

    print("\n" + "="*55)
    print("  CODE EXPERT RUNNER  —  Bayes' Theorem")
    print("="*55)

    passed = total = 0

    print("\n── Public Tests ──────────────────────────────────────")
    for name, fn in PUBLIC_TESTS:
        passed += run_test(name, fn, public=True); total += 1

    if args.all:
        print("\n── Hidden Tests ──────────────────────────────────────")
        for name, fn in HIDDEN_TESTS:
            passed += run_test(name, fn, public=False); total += 1

    pct = round(100 * passed / total) if total else 0
    print("\n" + "="*55)
    print(f"  SCORE: {passed}/{total}  ({pct}%)")
    print("  ✓ Full marks!" if pct == 100 else ("  ~ Good — check failing cases." if pct >= 70 else "  ✗ Keep going."))
    print("="*55 + "\n")

if __name__ == "__main__":
    main()
