def highest_product_of_three(arr):
    if len(arr) < 3:
        raise ValueError("Need at least three numbers")

    arr.sort()

    # Option 1: Product of three largest numbers
    max1 = arr[-1] * arr[-2] * arr[-3]

    # Option 2: Product of two smallest and the largest number
    max2 = arr[0] * arr[1] * arr[-1]

    return max(max1, max2)

# Example:
nums = [-10, -10, 5, 2]
result = highest_product_of_three(nums)
print(result)  # Output: 500
