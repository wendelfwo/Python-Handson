# Problem 1014 - URI

# Input
distance = int(input())
fuel = float(input())


# Procedures
def consumption(x, y):
    return x / y


# Output
print("%0.3f km/l" % consumption(distance, fuel))
