"""
Practice problem runner.

Usage:
    python run.py          # public tests only
    python run.py --all    # public + hidden (grading)
"""
import sys, argparse, traceback, random

try:
    from solution import empirical_prior, empirical_posterior, most_likely_class
except ImportError as e:
    print(f"[ERROR] Could not import solution.py: {e}"); sys.exit(1)

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
        return min(c for c in classes if priors[c] == max(priors.values()))
    return min(c for c in classes if posts[c] == max(posts.values()))

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

S = [(0,0),(0,1),(0,0),(1,1),(1,1),(0,1)]

PUBLIC_TESTS = [
    ("Prior P(Y=0)", lambda: approx(empirical_prior(S, 0), 2/6)),
    ("Prior P(Y=1)", lambda: approx(empirical_prior(S, 1), 4/6)),
    ("Posterior P(Y=0|X=0)", lambda: approx(empirical_posterior(S, 0, 0), 0.5)),
    ("Posterior P(Y=1|X=0)", lambda: approx(empirical_posterior(S, 0, 1), 0.5)),
    ("Posterior P(Y=1|X=1) = 1.0", lambda: approx(empirical_posterior(S, 1, 1), 1.0)),
    ("Unseen X → posterior 0.0", lambda: empirical_posterior(S, 99, 0) == 0.0),
    ("Most likely class X=1", lambda: most_likely_class(S, 1, [0,1]) == 1),
    ("Unseen X falls back to prior", lambda: most_likely_class(S, 99, [0,1]) == 1),
    ("Tie → smallest class label", lambda: most_likely_class([(0,0),(0,1)], 0, [0,1]) == 0),
]

HIDDEN_TESTS = [
    ("Three classes",
     lambda: approx(empirical_posterior([(0,0),(1,1),(2,2),(0,1),(1,2),(0,0)], 0, 0),
                    _posterior([(0,0),(1,1),(2,2),(0,1),(1,2),(0,0)], 0, 0))),
    ("Large input prior",
     lambda: (random.seed(42) or True) and (
         lambda s: approx(empirical_prior(s, 1), _prior(s, 1)))(
         [(random.randint(0,3), random.randint(0,2)) for _ in range(100_000)])),
    ("Most likely 3 classes",
     lambda: most_likely_class([(0,0)]*5+[(0,1)]*3+[(0,2)]*2, 0, [0,1,2]) ==
             _mlc([(0,0)]*5+[(0,1)]*3+[(0,2)]*2, 0, [0,1,2])),
    ("Unseen X → prior fallback class 1",
     lambda: most_likely_class([(0,0)]*2+[(0,1)]*8, 5, [0,1]) == 1),
    ("Output rounded to 4 dp",
     lambda: (lambda r: r == round(r,4))(empirical_prior(S, 0))),
    ("Stress test (20 random cases)",
     lambda: all(
         approx(empirical_prior(s,c), _prior(s,c)) and
         approx(empirical_posterior(s,x,c), _posterior(s,x,c)) and
         most_likely_class(s,x,[0,1,2,3]) == _mlc(s,x,[0,1,2,3])
         for s,c,x in [
             ([(random.randint(0,4),random.randint(0,3)) for _ in range(random.randint(20,500))],
              random.randint(0,3), random.randint(0,4))
             for _ in range(20)
         ]
     )),
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    random.seed(7)

    print("\n" + "="*55)
    print("  CODE EXPERT RUNNER  —  Empirical Bayes")
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
