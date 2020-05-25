# Problem 1006 - URI

# Input
A = float(input())
B = float(input())
C = float(input())

# Procedures
def average(grade1,grade2, grade3):
    return ((grade1 * 2) + (grade2 * 3) + (grade3 * 5))/10

# Outup
print("MEDIA = %0.1f" %(average(A, B, C)))
