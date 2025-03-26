def bubble_sort(arr):
    """
    Sorts a list using the Bubble Sort algorithm.
    Optimized with early termination when no swaps are made in a pass.

    Complexity:
        - Worst-case: O(n^2)
        - Average-case: O(n^2)
        - Best-case: O(n)

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new sorted list.

    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    n = len(arr)
    result = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def insertion_sort(arr):
    """
    Sorts a list using the Insertion Sort algorithm.

    Complexity:
        - Worst-case: O(n^2)
        - Average-case: O(n^2)
        - Best-case: O(n) (When list is already sorted)

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new sorted list.

    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def quick_sort(arr):
    """
    Sorts a list using the Quick Sort algorithm.

    Complexity:
        - Worst-case: O(n^2) (when the pivot is always the smallest or largest element)
        - Average-case: O(n log n)
        - Best-case: O(n log n)

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new sorted list.

    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
