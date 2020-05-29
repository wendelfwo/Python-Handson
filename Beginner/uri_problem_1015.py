# Problem 1015 - URI
import math

# Input
point_1 = input().split(" ")
point_2 = input().split(" ")

x1, y1 = point_1
x2, y2 = point_2


# Procedures
distance = math.sqrt(((float(x2) - float(x1)) * (float(x2) - float(x1))) +
                     ((float(y2) - float(y1)) * (float(y2) - float(y1))))

# Output
print("%0.4f" %distance)
