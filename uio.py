import sys

count = len(sys.argv)

if count > 1:
    total = 0
    for n in sys.argv[1:]:
        total += float(n)

    average = total / (count - 1)

    print("Total is", total)
    print("Average is", average)
else:
    print("No arguments were provided")
