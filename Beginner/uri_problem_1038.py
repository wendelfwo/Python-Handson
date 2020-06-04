# Problem 1039 - URI

# Input
numbers = input().split(" ")
code, amont = numbers

code = int(code)
amont = int(amont)

# Procedures
if code == 1:
    value = amont * 4.00
if code == 2:
    value = amont * 4.50
if code == 3:
    value = amont * 5.00
if code == 4:
    value = amont * 2.00
if code == 5:
    value = amont * 1.50

# Output
print("Total: R$ {:.2f}".format(value))