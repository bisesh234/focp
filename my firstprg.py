# Ask the user for a number
number = input("Enter a number: ")

# Convert input into an integer
number = int(number)

# Print back the number
print("The numbered entered was", number)

# Check if the number is even or odd
if (number % 2) == 0:
    print("That is an even number")
else:
    print("That is an odd number")

# Check if divisible by 10
if number % 10 == 0:
    print("The number is divisible by 10")
else:
    print("The number is NOT divisible by 10")
