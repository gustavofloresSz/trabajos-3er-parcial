import random
m=int(input('ingrese el numero de filas : '))
n=int(input('ingrese el numero de columnas : '))
A=[]
for i in range(m):
    A.append([])
    for j in range(n):
        num=random.randint(0,20)
        A[i].append(num)
print('matriz A: ')
for i in range(m):
    print(A[i])
cpar=0
cimpar=0
for i in range(m):
    for j in range(n):
        residuo=A[i][j]%2
        if residuo==0:
            cpar=cpar+1
        else:
            cimpar=cimpar+1
print('el num de pares es : ',cpar)
print('el num de impares es : ',cimpar)