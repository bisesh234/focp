import math

squares=[4,9,16,25]
for s in squares:
 print(math.sqrt(s))


# Task 2: Append next three square values (49, 64, 81)
squares.append(49)
squares.append(64)
squares.append(81)


# Task 3: Extend with 121, 144, 169
squares.extend([121, 144, 169])


# Task 4: Insert value 2 at the beginning
squares.insert(0, 2)


# Task 5: Remove value 49
squares.remove(49)


print(squares)