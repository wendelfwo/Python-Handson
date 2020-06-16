# Problem 1049 - URI

word_1 = input()
word_2 = input()
word_3 = input()

if (word_1 == "vertebrado"):
    if (word_2 == "ave"):
        if (word_3 == "carnivoro"):
            print("aguia")
        elif (word_3 == "onivoro"):
            print("pomba")
    elif (word_2 == "mamifero"):
        if (word_3 == "onivoro"):
            print("homem")
        elif (word_3 == "herbivoro"):
            print("vaca")
elif (word_1 == "invertebrado"):
    if (word_2 == "inseto"):
        if (word_3 == "hematofago"):
            print("pulga")
        elif (word_3 == "herbivoro"):
            print("lagarta")
    elif (word_2 == "anelideo"):
        if (word_3 == "hematofago"):
            print("sanguessuga")
        elif (word_3 == "onivoro"):
            print("minhoca")
