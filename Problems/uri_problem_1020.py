# Problem 1020 - URI

# Input
days = int(input())


# Procedures
years = days // 360

days -= years * 365

months = days // 30

days -= months * 30


# Output
print("%d ano(s)\n%d mes(es)\n"
      "%d dia(s)" %(years, months, days))