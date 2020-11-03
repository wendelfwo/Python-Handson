# Problem 1079 - URI

# Input
n = int(input())

# Procedures
for i in range(n):
    values = input().split(" ")
    value1 = float(values[0])
    value2 = float(values[1])
    value3 = float(values[2])

    mean = (value1 * 2 + value2 * 3 + value3 * 5) / 10

    print("{:.1f}".format(mean))