def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

print(calcAve(2, 4, 6))
print(calcAve(10, 20))
print(calcAve(1, 2, 3, 4, 5))
