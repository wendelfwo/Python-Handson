# Problem URI - 1046
times = input().split()
time_initial, time_final = times

time_initial = int(times[0])
time_final = int(times[1])

# Procedures
if time_initial < time_final:
    delta = time_final - time_initial
else:
    delta = (24 - time_initial) + time_final

print("O JOGO DUROU {} HORAS(S)".format(delta))




