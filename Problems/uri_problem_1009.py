# Problem 1009 - URI

# Input
name = input("")
salary_fix = float(input())
value_sold = float(input())

# Procedures
def salary_total(salary):
    return (0.15 * salary) + salary_fix

# Output
print("TOTAL = R$ %0.2f" % (salary_total(value_sold)))