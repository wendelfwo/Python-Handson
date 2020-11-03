# Problem 1060 - URI

# Procedures
qnt = 0

for item in range(6):
    number = float(input())
    if number > 0:
        qnt += 1
# Output
print("{} valores positivos".format(qnt))
