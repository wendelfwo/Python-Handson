# Problem 1042 - URI

# Input
numbers = input().split(" ")

a, b, c = numbers

a = int(a)
b = int(b)
c = int(c)

if (a > b) and (b > c):
    print("{}\n{}\n{}\n".format(c, b, a))

elif (a > c) and (c > b):
    print("{}\n{}\n{}\n".format(b, c, a))

elif (b > a) and (a > c):
    print("{}\n{}\n{}\n".format(c, a, b))

elif (b > c) and (c > a):
    print("{}\n{}\n{}\n".format(a, c, b))

elif (c > a) and (a > b):
    print("{}\n{}\n{}\n".format(b, a, c))

elif (c > b) and (b > a):
    print("{}\n{}\n{}\n".format(a, b, c))

print("{}\n{}\n{}".format(a, b, c))