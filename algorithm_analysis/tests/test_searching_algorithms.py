import pytest
import inspect
from algorithm_analysis.algorithms import searching


def get_searching_functions():
    return [
        func
        for name, func in inspect.getmembers(searching, inspect.isfunction)
        if name.endswith("_search")
    ]


@pytest.mark.parametrize("search_function", get_searching_functions())
def test_searching_success(search_function):
    data = [10, 20, 30, 40, 50, 60, 70]
    assert search_function(data, 10) == 0
    assert search_function(data, 40) == 3
    assert search_function(data, 70) == 6


@pytest.mark.parametrize("search_function", get_searching_functions())
def test_searching_not_found(search_function):
    data = [10, 20, 30, 40, 50]
    assert search_function(data, 999) == -1
    assert search_function([], 50) == -1
    assert search_function(data, -10) == -1


@pytest.mark.parametrize("search_function", get_searching_functions())
def test_searching_edge_cases(search_function):
    assert search_function([1], 1) == 0
    assert search_function([1], 0) == -1
    assert search_function([2, 2, 2, 2], 2) in [0, 1, 2, 3]


def test_invalid_input():
    for func in get_searching_functions():
        with pytest.raises(TypeError):
            func(None, 5)
        with pytest.raises(TypeError):
            func("notalist", 5)
        with pytest.raises(TypeError):
            func(42, 5)
        with pytest.raises(TypeError):
            func([], None)
