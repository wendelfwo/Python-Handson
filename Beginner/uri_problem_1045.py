# Problem 1045 - URI

# Input
sides = input().split(" ")

a = float(sides[0])
b = float(sides[1])
c = float(sides[2])

# Procedures
list = [a, b, c]
list.sort(reverse=True)

a = list[0]
b = list[1]
c = list[2]

if a >= b + c:
    print("NAO FORMA TRIANGULO")

else:
    if a * a == (b * b) + (c * c):
        print("TRIANGULO RETANGULO")

    if a * a > (b * b) + (c * c):
        print("TRIANGULO OBTUSANGULO")

    if  a * a < (b * b) + (c * c):
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")

    if (a == b  != c) or (b == c  != a) or (a == c  != b):
        print("TRIANGULO ISOSCELES")
