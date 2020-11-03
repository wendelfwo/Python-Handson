# Problem 1064 - URI

# Procedures
qtd = 0
sum = 0

for i in range(6):
    number = float(input())
    if number > 0:
        qtd += 1
        sum += number
# Ouput
print("{} valores positivos".format(qtd))
print("{:.1f}".format(sum/qtd))