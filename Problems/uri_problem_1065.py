# Problem 1065 - URI

# Procedures
qtd = 0

for i in range(5):
    number = int(input())
    if number % 2 == 0:
        qtd += 1

print("{} valores pares".format(qtd))

