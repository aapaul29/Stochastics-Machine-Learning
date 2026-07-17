import math

def update_centroids(X: list[list[float]], assignments: list[int],
                     k: int) -> list[list[float]]:
    """Recompute centroids as mean of assigned points."""
    d = len(X[0])
    sums   = [[0.0] * d for _ in range(k)]
    counts = [0] * k
    for x, z in zip(X, assignments):
        for j in range(d):
            sums[z][j] += x[j]
        counts[z] += 1
    centroids = []
    for j in range(k):
        if counts[j] == 0:
            centroids.append([0.0] * d)
        else:
            centroids.append([round(sums[j][dim] / counts[j], 6) for dim in range(d)])
    return centroids

def kmeans_converged(old_centroids: list[list[float]],
                     new_centroids: list[list[float]], tol: float) -> bool:
    """True if every centroid moved by at most tol."""
    for old, new in zip(old_centroids, new_centroids):
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(old, new)))
        if dist > tol:
            return False
    return True
