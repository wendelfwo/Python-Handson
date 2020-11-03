# Problem 1016 - URI

# Input
distance = int(input())

# Procedures
velocity_relative = 30
def time(delta_s):
    return 60 * (delta_s / velocity_relative)


# Output
print("%.d minutos" % time(distance))
