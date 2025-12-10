def multiply(a, b=None):
    if b is None:
        return a * a
    else:
        return a * b

print(multiply(5))
print(multiply(5, 3))
print(multiply(12))
