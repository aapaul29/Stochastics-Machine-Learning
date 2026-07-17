import math

def assign_clusters(X: list[list[float]], centroids: list[list[float]]) -> list[int]:
    """Assign each point in X to the nearest centroid (0-indexed)."""
    def dist(a, b):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
    result = []
    for x in X:
        dists = [dist(x, c) for c in centroids]
        result.append(dists.index(min(dists)))
    return result
