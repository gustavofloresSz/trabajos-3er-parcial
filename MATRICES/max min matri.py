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
for i in range(m):
    if A[i]<=A[i]:
        max=max+1
#terminar esta mal ,no tdo revi

