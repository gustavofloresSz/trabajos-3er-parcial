import random
m=int(input('ingrese el numero de filas : '))
n=int(input('ingrese el numero de columnas : '))
A=[]
for i in range(m):
    A.append([])
    for j in range(n):
        num=random.randint(-50,50)
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
            acnega=acnega+1
        else:
            if A[i][j]>0:
                acposi=acposi+1
print('los numeros negativos que hay son : ',acnega)
print('los numeros positivos que hay son : ',acposi)