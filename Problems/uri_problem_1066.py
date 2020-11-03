# Problem 1066 - URI

# Procedures
qtd_positive = 0
qtd_negative = 0
qtd_even = 0
qtd_odd = 0

for i in range(5):
    number = int(input())
    if number > 0:
        qtd_positive += 1
    if number < 0:
        qtd_negative += 1
    if number % 2 == 0:
        qtd_even += 1
    if number % 2 != 0:
        qtd_odd += 1

print("{} valor(es) par(es)".format(qtd_even))
print("{} valor(es) impar(es)".format(qtd_odd))
print("{} valor(es) positivo(s)".format(qtd_positive))
print("{} valor(es) negativo(s)".format(qtd_negative))