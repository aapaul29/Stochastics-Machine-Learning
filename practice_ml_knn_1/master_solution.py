import math
from collections import Counter

def euclidean_distance(x1: list[float], x2: list[float]) -> float:
    """Euclidean distance between two vectors, rounded to 6 dp."""
    return round(math.sqrt(sum((a - b) ** 2 for a, b in zip(x1, x2))), 6)

def knn_classify(X_train: list[list[float]], y_train: list[int],
                 x_query: list[float], k: int) -> int:
    """k-NN classification."""
    distances = [(euclidean_distance(x, x_query), i) for i, x in enumerate(X_train)]
    distances.sort(key=lambda d: d[0])  # stable sort
    k_labels = [y_train[i] for _, i in distances[:k]]
    counts = Counter(k_labels)
    return min(counts, key=lambda c: (-counts[c], c))
