# Problem URI - 1047

# Input
times = input().split()

hour_initial = int(times[0])
minute_initial = int(times[1])
hour_final = int(times[2])
minute_final =int(times[3])

if hour_initial < hour_final:
    dh = hour_final - hour_initial
    if minute_initial < minute_final:
        dm = minute_final - minute_initial
    if minute_initial > minute_final:
        dh = dh -1
        dm = (60 - minute_initial) + minute_final
    if minute_initial == minute_final:
        dm = 0
if hour_initial > hour_final:
    dh = (24 - hour_initial) + hour_final
    if minute_initial < minute_final:
        dm = minute_final - minute_initial
    if minute_initial > minute_final:
        dh = dh - 1
        dm = (60 - minute_initial) + minute_final
    if minute_initial == minute_final:
        dm = 0
if hour_initial == hour_final:
    if minute_initial < minute_final:
        dm = minute_final - minute_initial
        dh = 0
    if minute_initial > minute_final:
        dm = (60 - minute_initial) + minute_final
        dh = 23
    if minute_final == minute_initial:
        dh = 24
        dm = 0

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(dh, dm))