# Problem 1018 - URI

# Output
N = int(input())

# Procedures
notes_100 = N // 100
mod_100 =  N % 100

notes_050 = mod_100 // 50
mod_050 = mod_100 % 50

notes_020 = mod_050 // 20
mod_020 =  mod_050 % 20

notes_010 = mod_020 // 10
mod_010 =  mod_020 % 10

notes_005 = mod_010 // 5
mod_005 = mod_010 % 5

notes_002 = mod_005 // 2
mod_002 = mod_005 % 2

notes_001 = mod_002 // 1


# Output
print(N)
print('%d nota(s) de R$ 100,00' %notes_100)
print('%d nota(s) de R$ 50,00' %notes_050)
print('%d nota(s) de R$ 20,00' %notes_020)
print('%d nota(s) de R$ 10,00' %notes_010)
print('%d nota(s) de R$ 5,00' %notes_005)
print('%d nota(s) de R$ 2,00' %notes_002)
print('%d nota(s) de R$ 1,00' %notes_001)