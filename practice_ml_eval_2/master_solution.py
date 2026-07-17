def accuracy(y_true: list[int], y_pred: list[int]) -> float:
    n = len(y_true)
    return round(sum(a == b for a, b in zip(y_true, y_pred)) / n, 4)

def precision(y_true: list[int], y_pred: list[int]) -> float:
    tp = sum(a == 1 and b == 1 for a, b in zip(y_true, y_pred))
    pp = sum(b == 1 for b in y_pred)
    return round(tp / pp, 4) if pp > 0 else 0.0

def recall(y_true: list[int], y_pred: list[int]) -> float:
    tp = sum(a == 1 and b == 1 for a, b in zip(y_true, y_pred))
    ap = sum(a == 1 for a in y_true)
    return round(tp / ap, 4) if ap > 0 else 0.0

def f1_score(y_true: list[int], y_pred: list[int]) -> float:
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    denom = p + r
    return round(2 * p * r / denom, 4) if denom > 0 else 0.0
