# Problem 1020 - URI

# Input
value = float(input())

# Procedures
notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for note in notes:
    qtd_notes = int(value / note)
    print('{} nota(s) de R$ {:.2f}'.format(qtd_notes, note))
    value -= qtd_notes * note

print('MOEDAS:')
for coin in coins:
    qtd_coins = int(round(value,2) / coin)
    print('{} moeda(s) de R$ {:.2f}'.format(qtd_coins, coin))
    value -= qtd_coins * coin
