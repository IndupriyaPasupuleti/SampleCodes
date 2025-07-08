def find_min_max_iterative(arr):
    if not arr:
        return None, None  

    smallest = arr[0]
    largest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
        if arr[i] > largest:
            largest = arr[i]

    return smallest, largest

# Test
my_array = [5, 2, 9, 1, 7, 3]
min_val, max_val = find_min_max_iterative(my_array)
print(f"Smallest element: {min_val}")
print(f"Largest element: {max_val}")
