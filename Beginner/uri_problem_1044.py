# Problem 1044 - URI

numbers = input().split(" ")

x = int(numbers[0])
y = int(numbers[1])

if (x % y) == 0 or (y % x) ==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")