import pytest
import inspect
from algorithm_analysis.algorithms import palindromes


def get_palindrome_functions():
    return [
        func
        for name, func in inspect.getmembers(palindromes, inspect.isfunction)
        if name.startswith("is_palindrome_")
    ]


@pytest.mark.parametrize("palindrome_function", get_palindrome_functions())
def test_valid_palindromes(palindrome_function):
    valid_cases = [
        "racecar",
        "A man, a plan, a canal. Panama",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?",
        "Madam In Eden, I'm Adam",
        "Able was I ere I saw Elba",
        "Never odd or even",
        "12321",
        "0_0 (: /-\\ :) 0–0",
    ]
    for case in valid_cases:
        assert palindrome_function(case), f"Failed for: {case}"


@pytest.mark.parametrize("palindrome_function", get_palindrome_functions())
def test_invalid_palindromes(palindrome_function):
    invalid_cases = [
        "hello",
        "Palindrome",
        "This is not a palindrome",
        "12345",
        "Not a palindrome!",
    ]
    for case in invalid_cases:
        assert palindrome_function(case) is False, f"Failed for: {case}"


@pytest.mark.parametrize("palindrome_function", get_palindrome_functions())
def test_edge_cases(palindrome_function):
    edge_cases = [
        ("", True),
        ("a", True),
        (" ", True),
        ("!", True),
        ("aa", True),
        ("ab", False),
    ]
    for case, expected in edge_cases:
        assert palindrome_function(case) is expected, f"Failed for: {case}"


@pytest.mark.parametrize("palindrome_function", get_palindrome_functions())
def test_invalid_input(palindrome_function):
    invalid_inputs = [None, 12321, ["a", "b", "a"], {"text": "radar"}]
    for input_value in invalid_inputs:
        with pytest.raises(TypeError):
            palindrome_function(input_value)
