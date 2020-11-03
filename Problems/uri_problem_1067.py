# Problem 1067 - URI

# Input
number = int(input())

# Procedures
count = 1
while count <= number:
    if count % 2 != 0:
        print(count)

    count += 1
