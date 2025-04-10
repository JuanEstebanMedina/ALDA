def validate_input(arr, target):
    """
    Validates the input for searching algorithms.

    Args:
        arr (list): The list of elements to search in.
        target: The target element to search for.

    Raises:
        TypeError: If the input is not valid.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if target is None:
        raise TypeError("Target cannot be None")


# def linear_search(arr, target):
#     """
#     Performs a linear search to find the index of the target element in the list.

#     Complexity:
#         - Worst-case: O(n)
#         - Average-case: O(n)
#         - Best-case: O(1)

#     Args:
#         arr (list): List of elements.
#         target: Element to search for.

#     Returns:
#         int: Index of the target element if found; otherwise, -1.
#     """
#     validate_input(arr, target)
#     for index, element in enumerate(arr):
#         if element == target:
#             return index
#     return -1


def binary_search(arr, target):
    """
    Performs a binary search to find the index of the target element in a sorted list.

    Complexity:
        - Worst-case: O(log n)
        - Average-case: O(log n)
        - Best-case: O(1) (target is found in the first guess)

    Args:
        arr (list): Sorted list of elements.
        target: Element to search for.

    Returns:
        int: Index of the target element if found; otherwise, -1.
    """
    validate_input(arr, target)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def ternary_search(arr, target):
    """
    Performs a ternary search to find the index of the target element in a sorted list.

    Complexity:
        - Worst-case: O(log₃ n)
        - Average-case: O(log₃ n)
        - Best-case: O(1)

    Args:
        arr (list): Sorted list of elements.
        target: Element to search for.

    Returns:
        int: Index of the target element if found; otherwise, -1.
    """
    validate_input(arr, target)
    left, right = 0, len(arr) - 1
    while left <= right:
        third = (right - left) // 3
        mid1 = left + third
        mid2 = right - third
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1
