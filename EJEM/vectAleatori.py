import random
n=int(input('ingrese la cantidad de elementos del vector'))
u=[]
for i in range(n):
    num=random.randint(0,50)
    u.append(num)
print('vector: ',u)

#recorrer elemento uno a uno usando una variable
for numero in u:
    print(numero)