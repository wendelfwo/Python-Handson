# Problem 1012 - URI

# Input
values = input().split(" ")

# Procedures
a, b, c = values
pi = 3.14159

triangule = (float(a) * float(c)) / 2.0
circle = pi * (float(c) * float(c))
trapezio = float(c) * (float(a) + float(b)) / 2.0
square = float(b) * float(b)
rectangle = float(a) * float(b)

# Output
print("TRIANGULO: %0.3f\n"
      "CIRCULO: %0.3f\n"
      "TRAPEZIO: %0.3f\n"
      "QUADRADO: %0.3f\n"
      "RETANGULO: %0.3f"
      % (triangule, circle, trapezio, square, rectangle))
