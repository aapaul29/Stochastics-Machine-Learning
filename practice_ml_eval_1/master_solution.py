def kfold_indices(n: int, k: int) -> list[tuple[list[int], list[int]]]:
    """Return k (train_indices, val_indices) tuples for k-fold CV."""
    # Build fold boundaries
    base = n // k
    extra = n % k
    folds = []
    start = 0
    for i in range(k):
        size = base + (1 if i < extra else 0)
        folds.append(list(range(start, start + size)))
        start += size

    result = []
    for i in range(k):
        val = folds[i]
        train = []
        for j in range(k):
            if j != i:
                train.extend(folds[j])
        result.append((sorted(train), sorted(val)))
    return result
