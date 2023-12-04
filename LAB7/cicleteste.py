import pytest
from circle import Circle
from math import pi as PI

# Happy path tests with various realistic test values
@pytest.mark.parametrize("radius, expected_area, expected_perimeter", [
    (1, PI, 2 * PI),
    (0, 0, 0),
    (2.5, PI * 2.5**2, 2 * PI * 2.5),
    (10, PI * 10**2, 2 * PI * 10),
], ids=["radius-1", "radius-0", "radius-2.5", "radius-10"])
def test_circle_with_realistic_values(radius, expected_area, expected_perimeter):
    # Act
    circle = Circle(radius)
    area = circle.get_area()
    perimeter = circle.get_perimetro()

    # Assert
    assert area == expected_area
    assert perimeter == expected_perimeter

# Edge cases
@pytest.mark.parametrize("radius, expected_area, expected_perimeter", [
    (1e-10, PI * 1e-10**2, 2 * PI * 1e-10),
    (1e10, PI * 1e10**2, 2 * PI * 1e10),
], ids=["radius-very-small", "radius-very-large"])
def test_circle_with_edge_cases(radius, expected_area, expected_perimeter):
    # Act
    circle = Circle(radius)
    area = circle.get_area()
    perimeter = circle.get_perimetro()

    # Assert
    assert area == pytest.approx(expected_area)
    assert perimeter == pytest.approx(expected_perimeter)

# Error cases
@pytest.mark.parametrize("radius", [
    (-1),
    (-1e10),
    ("a"),
    (None),
    (complex(5, 3)),
], ids=["negative-radius", "very-negative-radius", "non-numeric-radius", "none-radius", "complex-radius"])
def test_circle_with_error_cases(radius):
    # Act & Assert
    with pytest.raises((ValueError, TypeError)):
        Circle(radius)
