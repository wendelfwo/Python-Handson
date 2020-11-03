# Problem 1010 - URI

# Input
line1 = input().split(" ")
line2 = input().split(" ")


# Procedures
code1, units1, price1 = line1
code2, units2, price2 = line2

value_to_pay = ((int(units1) * float(price1)) + (int(units2) * float(price2)))


# Output
print("VALOR A PAGAR: R$ %0.2f" % value_to_pay)
