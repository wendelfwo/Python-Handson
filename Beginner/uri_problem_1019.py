# Problem 1019 - URI

# Input
seconds = int(input())

# Procedures
hours =  seconds // 3600
seconds = seconds - (hours * 3600)

minutes = seconds // 60

seconds = seconds - (minutes * 60)

# Output
print("%d:%d:%d"%(hours, minutes, seconds))

