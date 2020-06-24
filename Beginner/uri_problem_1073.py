# Problem 1073

# Input
number =  int(input())

# Procedures
if  number % 2 == 0:
    for item in range(2, number + 2, 2):
        print("{}^2 = {}".format(item, item * item))
else:
    for item in range(2, number + 1, 2):
        print("{}^2 = {}".format(item, item * item))