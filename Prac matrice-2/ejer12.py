import random
m=int(input('ingrese el numero de filas : '))
n=int(input('ingrese el numero de columnas : '))
A=[]
for i in range(m):
    A.append([])
    for j in range(n):
        num=random.randint(1,20)
        A[i].append(num)
print('matriz A: ')
for i in range(m):
    print(A[i])
vecmay=[]
mayor=A[0][0]
for i in range(m):
    for j in range(n):
        if A[i][j]>mayor:
            mayor=A[i][j]
    vecmay.append(mayor)
    mayor=0
print('el vector que contiene los num maximos de cada fila es :' ,vecmay)