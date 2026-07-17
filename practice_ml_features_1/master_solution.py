def poly_features(x: float, degree: int) -> list[float]:
    """Return [1, x, x^2, ..., x^degree], each rounded to 6 dp."""
    return [round(x ** i, 6) for i in range(degree + 1)]
