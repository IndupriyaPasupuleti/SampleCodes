def nth_highest(nums, n):
    if n > len(nums) or n < 1:
        return None

    unique = list(set(nums))  # remove duplicates
    unique.sort(reverse=True)  # sort descending

    return unique[n - 1]  # nth highest


# Test
orders = [4, 2, 9, 5, 8, 9, 5]
n = 2
print(f"{n}th highest order count:", nth_highest(orders, n))
