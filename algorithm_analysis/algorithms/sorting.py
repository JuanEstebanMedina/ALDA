def bubble_sort(arr):
    """
    Sorts a list using the Bubble Sort algorithm.

    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. The process repeats until
    the list is sorted. This algorithm is simple but inefficient for large datasets.

    Complexity:
        - Worst-case: O(n^2)
        - Average-case: O(n^2)
        - Best-case: O(n) (when the list is already sorted)

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.

    Raises:
        TypeError: If the input is not a list.

    Example:
        >>> bubble_sort([5, 3, 8, 4, 2])
        [2, 3, 4, 5, 8]
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    """
    Sorts a list using the Insertion Sort algorithm.

    Insertion Sort builds the sorted list one item at a time, taking each element
    and inserting it into its correct position relative to the already sorted part
    of the list. It is efficient for small datasets or nearly sorted data.

    Complexity:
        - Worst-case: O(n^2)
        - Average-case: O(n^2)
        - Best-case: O(n) (when the list is already sorted)

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.

    Raises:
        TypeError: If the input is not a list.

    Example:
        >>> insertion_sort([7, 3, 5, 2, 4])
        [2, 3, 4, 5, 7]
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(arr):
    """
    Sorts a list using the Quick Sort algorithm.

    Quick Sort is a divide-and-conquer algorithm that works by selecting a pivot
    element and partitioning the other elements into two sub-arrays:
    - Elements smaller than the pivot.
    - Elements greater than the pivot.
    These sub-arrays are recursively sorted and combined to form the final sorted list.

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

    Example:
        >>> quick_sort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]
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
