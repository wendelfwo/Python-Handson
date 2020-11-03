# Problem 1051 - URI

# Input
salary = float(input())
# Procedures

if salary <= 2000.00:
    print("Isento")

else:
    if salary > 2000.00 and salary <= 3000.00:
        rate = (salary - 2000.00) * 0.08

    if salary > 3000 and salary <= 4500:
        taxation_1 = 1000 * 0.08
        taxation_2 =  (salary - 3000) * 0.18
        rate = taxation_2 + taxation_1

    if salary > 4500:
        taxation_1 = 1000 * 0.08
        taxation_2 = 1500 * 0.18
        taxation_3 = (salary - 4500) * 0.28
        rate = taxation_1 + taxation_2 + taxation_3

    print("R$ {:.2f}".format(rate))

