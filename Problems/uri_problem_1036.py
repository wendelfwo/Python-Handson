# Problem 1035 - URI
import  math

# Input
numbers = input().split(" ")
a, b, c = numbers

a = float(a)
b = float(b)
c = float(c)

# Procedures
delta = b * b - 4 * a * c

if delta < 0 or a == 0:
    print("Impossivel calcular")

else:
    r1 = ((-1)*b + math.sqrt(delta))/ (2 * a)
    r2 = ((-1)*b - math.sqrt(delta))/ (2 * a)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))
