import re
import sys

sys.setrecursionlimit(10000)


def normalize(text):
    """
    Normalizes the input text by removing non-alphanumeric characters and converting to lowercase.

    Args:
        text (str): The input text to normalize.

    Returns:
        str: The normalized text.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return re.sub(r"[^a-z0-9]", "", text.lower())


def is_palindrome_reverse(text):
    """
    Checks if a string is a palindrome by reversing it.

    Complexity:
        - Time: O(n)
        - Space: O(n)

    Args:
        text (str): The input text to check.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    text = normalize(text)
    return text == text[::-1]


def is_palindrome_iterative(text):
    """
    Checks if a string is a palindrome using two pointers.

    Complexity:
        - Time: O(n)
        - Space: O(1)

    Args:
        text (str): The input text to check.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    text = normalize(text)
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_recursive(text):
    """
    Checks if a string is a palindrome using recursive comparison by indices.

    More efficient than naive slicing as it avoids string copies.

    Complexity:
        - Time: O(n)
        - Space: O(n)

    Args:
        text (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    text = normalize(text)

    def helper(left, right):
        print(f"Comparing {left} and {right}")  # TEMPORAL
        if left >= right:
            return True
        if text[left] != text[right]:
            return False
        return helper(left + 1, right - 1)

    return helper(0, len(text) - 1)


def is_palindrome_stack(text):
    """
    Checks if a string is a palindrome using a stack.

    Complexity:
        - Time: O(n)
        - Space: O(n)

    Args:
        text (str): The input text to check.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    text = normalize(text)
    stack = list(text)
    for char in text:
        if char != stack.pop():
            return False
    return True
