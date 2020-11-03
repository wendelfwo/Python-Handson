# Problem 1008 - URI

# Input
number_employees = int(input())
work_hour = int(input())
receive_hour = float(input())

# Procedures
def salary(quant_hour, value_hour):
    return quant_hour * value_hour

# Output
print("NUMBER = %d\nSALARY = U$ %0.2f" %
      (number_employees, salary(work_hour,receive_hour)))