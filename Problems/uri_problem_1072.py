# Problem 1071 - URI

# Input
n = int(input())

# Procedures
into = 0
out = 0

for item in range(0,n):
    value = int(input())
    if value >= 10 and value <= 20:
        into += 1
    else:
        out += 1

# Output
print("{} in".format(into))
print("{} out".format(out))