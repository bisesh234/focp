def findMax(a, b):
    """Finds the maximum of two values."""
    if a > b:
        max_value = a
    else:
        max_value = b
    return max_value

print(findMax(3, 9))
print(findMax(10, 4))
print(findMax(5, 5))
