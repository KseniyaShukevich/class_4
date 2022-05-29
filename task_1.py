import sys

production, rate, premium = sys.argv[1:]

print('Заработная плата сотрудника: ', int(production) * int(rate) + int(premium))
