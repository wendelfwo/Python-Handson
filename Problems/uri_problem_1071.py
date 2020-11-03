# Problem 1071 - URI

# Input
value_x = int(input())
value_y = int(input())

# Procedures
sum = 0

if value_x > value_y and abs(value_y) % 2 != 0:
    for number in range(value_y + 2,value_x, 2):
        sum += number

if value_x > value_y and abs(value_y) % 2 == 0:
    for number in range(value_y + 1,value_x, 2):
        sum += number

if value_y > value_x and abs(value_x) % 2 != 0:
    for number in range(value_x + 2,value_y, 2):
        sum += number

if value_y > value_x and abs(value_x) % 2 == 0:
    for number in range(value_x + 1,value_y, 2):
        sum += number

#Output
print("{}".format(sum))