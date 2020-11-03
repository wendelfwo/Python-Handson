# Problem 1013 - URI
import math

# Input
value = input().split(" ")

a, b, c = value

# Procedures
greatest = (int(a) + int(b) + abs(int(a) - int(b))) / 2
result = (int(greatest) + int(c) + abs(int(greatest) - int(c)))/ 2

#Output
print("%d eh o maior" %result)
