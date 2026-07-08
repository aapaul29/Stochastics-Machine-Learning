def compute_conditional_pmf(samples: list[tuple[int, int]],
                             y_target: int,
                             x_values: list[int]) -> list[float]:
    """Return empirical P(X = x | Y = y_target) for each x in x_values."""
    num_y = sum(1 for _, y in samples if y == y_target)
    if num_y == 0:
        return [0.0] * len(x_values)
    return [round(sum(1 for x, y in samples if x == xv and y == y_target) / num_y, 2)
            for xv in x_values]
