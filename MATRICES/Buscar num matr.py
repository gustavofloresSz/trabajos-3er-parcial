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
x=int(input('ingrese el num a buscar'))
c=0
for i in range(m):
    for j in range(n):
        if A[i][j]==x:
            c=c+1
print('el num de veces que esta es :',c)
