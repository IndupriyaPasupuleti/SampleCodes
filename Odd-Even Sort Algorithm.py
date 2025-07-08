def odd_even_sort(arr):
    """
    Sorts a list using the Odd-Even Sort algorithm.

    Args:
        arr: The list to be sorted.

    Returns:
        The sorted list.
    """
    n = len(arr)
    sorted_flag = False  # Flag to track if the array is sorted

    while not sorted_flag:
        sorted_flag = True  # Assume sorted at the beginning of each pass

        # Odd Phase: Compare and swap elements at odd indices (1, 3, 5, ...)
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False  # A swap occurred, so the array is not yet sorted

        # Even Phase: Compare and swap elements at even indices (0, 2, 4, ...)
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False  # A swap occurred, so the array is not yet sorted

    return arr

# Example Usage:
my_list = [5, 2, 8, 1, 9, 4, 7, 3]
sorted_list = odd_even_sort(my_list)
print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")
