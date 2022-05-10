N=int(input("введите кол-во билетов"))
P=N
S=0
while N>0:
        age=int(input("Введите возраст"))
        if age<18:
          ticket=0
          S=S+ticket
          N=N-1
        elif 18<=age<25:
          ticket=990
          S=S+ticket
          N=N-1
        else :
          ticket=1390
          S = S + ticket
          N=N-1
print("Общая стоимисть билетов",S)
if P>3:
    S=S-S*0.1
    print("сумма со скидкой 10%",S)

