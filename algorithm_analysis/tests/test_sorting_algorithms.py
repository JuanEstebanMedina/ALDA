import pytest
import inspect
from algorithm_analysis.algorithms import sorting


def get_sorting_functions():
    return [
        func
        for name, func in inspect.getmembers(sorting, inspect.isfunction)
        if name.endswith("_sort")
    ]


@pytest.mark.parametrize("sorting_function", get_sorting_functions())
def test_sorting_algorithms(sorting_function):
    assert sorting_function([3, 1, 2]) == [1, 2, 3]
    assert sorting_function([5, -1, 0, 3]) == [-1, 0, 3, 5]
    assert sorting_function([]) == []
    assert sorting_function([7]) == [7]
    assert sorting_function([3, 3, 3]) == [3, 3, 3]
    assert sorting_function([10, -2, 4, 0, 7, 1]) == [-2, 0, 1, 4, 7, 10]


def test_invalid_input():
    for func in get_sorting_functions():
        with pytest.raises(TypeError):
            func(None)
            func("hello")
            func(123)
            func({})
            func(3.14)
            func(True)
