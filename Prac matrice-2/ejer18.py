import random
m=int(input('ingrese el numero de filas : '))
A=[]
for i in range(m):
    A.append([])
    for j in range(3):
        num=random.randint(1,20)
        A[i].append(num)
print('matriz A: ')
for i in range(m):
    print(A[i])
for j in range(m):
    ac=0
    for i in range(2):
        ac=ac+A[j][i]
    A[j][2]=ac
print('la suma de las las columnas y puesta en la 3ra columna es : ')
for i in range(m):
    print(A[i])