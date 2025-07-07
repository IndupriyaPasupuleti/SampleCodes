import threading

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Sort halves in separate threads
    left_thread = threading.Thread(target=lambda: merge_sort_in_place(left_half))
    right_thread = threading.Thread(target=lambda: merge_sort_in_place(right_half))

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    # Merge the sorted halves
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    return arr

def merge_sort_in_place(arr):
    # This function is called by the threads to sort their respective sub-arrays
    # For a true in-place merge sort, a more complex merging logic would be needed.
    # Here, it simplifies the example by relying on the main merge_sort to handle the merge.
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort_in_place(left)
    merge_sort_in_place(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage
if __name__ == "__main__":
    my_list = [38, 27, 43, 3, 9, 82, 10]
    print("Original list:", my_list)
    sorted_list = merge_sort(my_list)
    print("Sorted list:", sorted_list)
