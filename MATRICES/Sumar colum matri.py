import random
m=int(input('ingrese el numero de filas : '))
n=int(input('ingrese el numero de columnas : '))
A=[]
for i in range(m):
    A.append([])
    for j in range(n):
        num=random.randint(0,10)
        A[i].append(num)
print('matriz A: ')
for i in range(m):
    print(A[i])
for j in range(n):
    ac=0
    for i in range(m):
        ac=ac+A[i][j]
    print('la suma de elemntos de la columna '+str(j)+ ' es '+str(ac))
