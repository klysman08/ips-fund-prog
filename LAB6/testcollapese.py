import pytest
from collapse import collapse

# Happy path tests with various realistic test values
@pytest.mark.parametrize("input_list, expected", [
    pytest.param([1, 2, 3, 4], [3, 7], id="even_number_of_elements"),
    pytest.param([1, 2, 3], [3, 3], id="odd_number_of_elements"),
    pytest.param([], [], id="empty_list"),
    pytest.param([5], [5], id="single_element"),
    pytest.param([1, 2, 3, 4, 5, 6], [3, 7, 11], id="multiple_pairs"),
    pytest.param([-1, -2, -3, -4], [-3, -7], id="negative_numbers"),
    pytest.param([0, 0, 0, 0], [0, 0], id="zeroes"),
])
def test_collapse_happy_path(input_list, expected):
    # Act
    result = collapse(input_list)

    # Assert
    assert result == expected

# Edge cases
@pytest.mark.parametrize("input_list, expected", [
    pytest.param([1], [1], id="single_element_edge_case"),
    pytest.param([1, 2], [3], id="pair_edge_case"),
])
def test_collapse_edge_cases(input_list, expected):
    # Act
    result = collapse(input_list)

    # Assert
    assert result == expected

# Error cases
@pytest.mark.parametrize("input_list, exception", [
    pytest.param(None, TypeError, id="none_input"),
    pytest.param("string", TypeError, id="string_input"),
    pytest.param(123, TypeError, id="integer_input"),
    pytest.param([1, "two", 3], TypeError, id="mixed_type_list"),
])
def test_collapse_error_cases(input_list, exception):
    # Act & Assert
    with pytest.raises(exception):
        collapse(input_list)
