def average(values):
    """Calculates the average of the given list."""
    total = 0
    for n in values:
        total += float(n)
    return total / len(values)

# Display only when imported
print("Welcome, utils module has been imported and initialised!")

# If executed as script
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        nums = [float(x) for x in sys.argv[1:]]
        print("Average is", average(nums))
    else:
        print("No values provided")
