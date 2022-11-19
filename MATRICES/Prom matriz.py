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
ac=0
divi=m*n
for i in range(n):
    for j in range(n):
        ac=ac+A[i][j]
prom=ac/divi
print('el promedio es : ',prom)