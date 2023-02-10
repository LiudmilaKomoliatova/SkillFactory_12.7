money = int(input("Введите сумму вклатда:"))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = [round(money + money * percent / 100) for percent in per_cent.values()]
print(f'Deposit = {deposit}')

i = deposit.index(max(deposit))
print(f'Максимальная сумма, которую вы можете заработать - {deposit[i]}')
