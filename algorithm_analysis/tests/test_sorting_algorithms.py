import pytest
from algorithm_analysis.algorithms.sorting import (
    bubble_sort,
    insertion_sort,
    quick_sort,
)


@pytest.mark.parametrize("sorting_function", [bubble_sort, insertion_sort, quick_sort])
def test_sorting_algorithms(sorting_function):
    assert sorting_function([3, 1, 2]) == [1, 2, 3]
    assert sorting_function([5, -1, 0, 3]) == [-1, 0, 3, 5]
    assert sorting_function([]) == []
    assert sorting_function([7]) == [7]
    assert sorting_function([3, 3, 3]) == [3, 3, 3]
    assert sorting_function([10, -2, 4, 0, 7, 1]) == [-2, 0, 1, 4, 7, 10]


def test_invalid_input():
    with pytest.raises(TypeError):
        bubble_sort(None)
    with pytest.raises(TypeError):
        insertion_sort("string")
    with pytest.raises(TypeError):
        quick_sort(123)
