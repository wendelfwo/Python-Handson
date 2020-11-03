#import  math
# Problem 1043 - URI

# Input
sides = input().split(" ")

a = float(sides[0])
b = float(sides[1])
c = float(sides[2])

# Procedure
if (abs(b - c) < a) and (a < b + c):
    if (abs(a - c) < b) and (b < a + c):
        if (abs(b - a) < c) and (c < b + a):
            print("Perimetro = {}".format(a + b + c))

else:
    print("Area = {}".format((a * c + b * c)/ 2))