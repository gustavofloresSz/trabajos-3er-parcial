import random
m=int(input('ingrese el numero de filas : '))
n=int(input('ingrese el numero de columnas : '))
A=[]
for i in range(m):
    A.append([])
    for j in range(n):
        num=random.randint(-100,100)
        A[i].append(num)
print('matriz A: ')
for i in range(m):
    print(A[i])
#el 0 no tiene signo, excluimos
acnega=0
acposi=0
for i in range(m):
    for j in range(n):
        if A[i][j]<0:
            acnega=acnega+A[i][j]
        else:
            if A[i][j]>0:
                acposi=acposi+A[i][j]
print('la suma de los num positivos de la matriz es : ',acnega)
print('la suma de los num negativos de la matriz es  : ',acposi)