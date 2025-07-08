def find_largest(numbers):
    if not numbers:
        return None  # Handle empty list
    largest = numbers
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print(find_largest())
