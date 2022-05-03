money=float(input("Введите сумму вклада"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a=round(float(per_cent['ТКБ']*(money/100)),3)
b=round(float(per_cent['СКБ']*(money/100)),3)
c=round(float(per_cent['ВТБ']*(money/100)),3)
d=round(float(per_cent['СБЕР']*(money/100)),3)
deposit=[a,b,c,d]
print ("Ваш доход по депозиту",deposit)
deposit.sort()
print("Максимальная сумма, которую вы можете заработать",deposit[-1])

