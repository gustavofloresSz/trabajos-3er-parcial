#ver bien,las comas dan los incisos / dif pdf
import random
B=[]
for i in range(5):
    B.append([])
    for j in range(3):
        a=random.randint(1,10)
        B[i].append(a)
print('matriz de sodas es : ')
for i in range(5):
    print(B[i])
#buscando donde se consume mas cocacola inciso a)
mayor=B[0][0]
posicion=0
for j in range(3):
    if mayor<B[0][j]:
        mayor=B[0][j]
        posicion=j
if posicion==0:
    print('se consume mas cocacola en Santa Cruz con: ',mayor)
elif posicion==1:
    print('se consume mas cocacola en Beni con: ',mayor)
else:
    print('se consume mas cocacola en Tarija con: ', mayor)
#buscando la bebida mas consumida
suma=[]
for i in range(5):
    ac=0
    for j in range(3):
        ac=ac+B[i][j]
    suma.append(ac)
print('cantidades total por bebidas: ',suma)
max=suma[0]
posicion=0
for k in range(5):
    if max<suma[k]:
        max=suma[k]
        posicion=k
if posicion==0:
    print('la soda mas consumida es cocacola: ',max)
elif posicion==1:
    print('la soda mas consumida es fanta: ', max)
elif posicion==2:
    print('la soda mas consumida es sprite: ', max)
elif posicion==3:
    print('la soda mas consumida es seven up: ', max)
else:
    print('la soda mas consumida es pepsi: ', max)
#bebida menor consumida beni
menor=B[0][1]
posicion=0
for i in range(5):
    if menor>B[i][1]:
        menor=B[i][1]
        posicion=i
if posicion==0:
    print('la soda menos consumida en beni es cocacola con: ',menor)
elif posicion==1:
    print('la soda menos consumida en beni es fanta con: ', menor)
elif posicion==2:
    print('la soda menos consumida en beni es sprite con: ', menor)
elif posicion==3:
    print('la soda menos consumida en beni es seven up con: ', menor)
else:
    print('la soda menos consumida en beni es pepsi con: ', menor)