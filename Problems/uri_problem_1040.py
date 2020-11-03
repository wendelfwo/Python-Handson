# Problem 1040 - URI

# Input
scores =  input().split(" ")
n1, n2, n3, n4 = scores

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

# Procedures
average1 = (2 * n1 + 3 * n2 + 4 * n3 + 1 * n4 ) / 10

if (average1 >= 5.0) and (average1 <= 6.9):
    note_exame = float(input())
    average2 = (note_exame + average1) / 2
    if average2 >= 5.0:
        print("Media: {:.1f}".format(average1))
        print("Aluno em exame.")
        print("Nota do exame: {:.1f}".format(note_exame))
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(average2))
    else:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(average2))

if average1 >= 7.0:
    print("Media: {:.1f}".format(average1))
    print("Aluno aprovado.")

if average1 < 5.0:
    print("Media: {:.1f}".format(average1))
    print("Aluno reprovado.")
