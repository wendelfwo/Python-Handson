# Problem 1048 - URI

# Input
salary = float(input())

# Procedures
if salary <= 400.00:
    percent = 0.15
    reajust = percent * salary
    new_salary =  reajust + salary
elif (salary > 400.0) and (salary <= 800.00):
    percent = 0.12
    reajust = percent * salary
    new_salary = reajust + salary
elif (salary > 800.00) and (salary <= 1200.00):
    percent = 0.10
    reajust = percent * salary
    new_salary =  reajust + salary
elif (salary > 1200.00) and (salary <= 2000.00):
    percent = 0.07
    reajust = percent * salary
    new_salary = reajust + salary
else:
    percent = 0.04
    reajust = percent * salary
    new_salary = reajust + salary


# Ouput
print("Novo salario: {:.2f}".format(new_salary))
print("Reajuste ganho: {:.2f}".format(reajust))
print("Em percentual: {:.0f} %".format(percent * 100))