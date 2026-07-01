"""
Practice problem runner.

Usage:
    python run.py          # public tests only
    python run.py --all    # public + hidden (grading)
"""
import sys, argparse, traceback, random

try:
    from solution import total_probability, most_likely_cause
except ImportError as e:
    print(f"[ERROR] Could not import solution.py: {e}"); sys.exit(1)

def _ref_total(priors, conditionals):
    return round(sum(p * c for p, c in zip(priors, conditionals)), 4)

def _ref_cause(priors, conditionals):
    unnorm = [p * c for p, c in zip(priors, conditionals)]
    return unnorm.index(max(unnorm))

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
    ("Three machines: total probability",
     lambda: approx(total_probability([0.5,0.3,0.2],[0.02,0.05,0.10]), 0.045)),
    ("Three machines: most likely cause",
     lambda: most_likely_cause([0.5,0.3,0.2],[0.02,0.05,0.10]) == 2),
    ("Two causes: total probability",
     lambda: approx(total_probability([0.6,0.4],[0.3,0.8]), 0.5)),
    ("Two causes: most likely cause",
     lambda: most_likely_cause([0.6,0.4],[0.3,0.8]) == 1),
    ("Uniform prior: highest likelihood wins",
     lambda: most_likely_cause([0.25,0.25,0.25,0.25],[0.1,0.5,0.3,0.4]) == 1),
    ("Tie: smaller index returned",
     lambda: most_likely_cause([0.5,0.5],[0.4,0.4]) == 0),
    ("Output rounded to 4 dp",
     lambda: (lambda r: r == round(r,4))(total_probability([0.5,0.3,0.2],[0.02,0.05,0.10]))),
]

HIDDEN_TESTS = [
    ("Four classes",
     lambda: most_likely_cause([0.4,0.3,0.2,0.1],[0.05,0.1,0.2,0.5]) == _ref_cause([0.4,0.3,0.2,0.1],[0.05,0.1,0.2,0.5])),
    ("Same conditional → most likely = argmax prior",
     lambda: most_likely_cause([0.1,0.5,0.4],[0.3,0.3,0.3]) == 1),
    ("Large partition (n=50)",
     lambda: (lambda: (
         random.seed(7),
         (lambda raw: (
             (lambda p, c: most_likely_cause(p, c) == _ref_cause(p, c))(
                 [r/sum(raw) for r in raw],
                 [random.random() for _ in range(50)]
             )
         ))([random.random() for _ in range(50)])
     ))()[-1]),
    ("Stress: total probability (30 cases)",
     lambda: all(
         approx(total_probability([r/sum(raw) for r in raw], conds), _ref_total([r/sum(raw) for r in raw], conds))
         for raw, conds in [
             ([random.random() for _ in range(random.randint(2,20))],
              [random.random() for _ in range(random.randint(2,20))])
             for _ in range(30)
         ]
     )),
    ("Stress: most likely cause (30 cases)",
     lambda: all(
         most_likely_cause(p, c) == _ref_cause(p, c)
         for p, c in [
             (lambda raw: ([r/sum(raw) for r in raw], [random.random() for _ in range(len(raw))]))(
                 [random.random() for _ in range(random.randint(2, 20))]
             )
             for _ in range(30)
         ]
     )),
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    random.seed(42)

    print("\n" + "="*55)
    print("  CODE EXPERT RUNNER  —  Law of Total Probability")
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
