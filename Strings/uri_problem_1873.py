# Problem 1873 - URI

# Input
cases =  int(input())

# Procedures
for case in range(cases):
    weapons = input().split(" ")
    weapon_1 = weapons[0].lower()
    weapon_2 = weapons[1].lower()

    if weapon_1 == weapon_2:
        print("empate")
    else:
        if weapon_1 == "tesoura" and weapon_2 == "papel":
            print("rajesh")
        elif weapon_1 == "papel" and weapon_2 == "pedra":
            print("rajesh")
        elif weapon_1 == "pedra" and weapon_2 == "lagarto":
            print("rajesh")
        elif weapon_1 == "lagarto" and weapon_2 == "spock":
            print("rajesh")
        elif weapon_1 == "spock" and weapon_2 == "tesoura":
            print("rajesh")
        elif weapon_1 == "tesoura" and weapon_2 == "lagarto":
            print("rajesh")
        elif weapon_1 == "lagarto" and weapon_2 == "papel":
            print("rajesh")
        elif weapon_1 == "papel" and weapon_2 == "spock":
            print("rajesh")
        elif weapon_1 == "spock" and weapon_2 == "pedra":
            print("rajesh")
        elif weapon_1 == "pedra" and weapon_2 == "tesoura":
            print("rajesh")
        else:
            print("sheldon")