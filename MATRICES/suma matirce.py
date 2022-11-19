import random
m=int(input('ingrese el numero de filas : '))
n=int(input('ingrese el numero de comulnas: '))
B=[]
for i in range(m):
    B.append([])
    for j in range(n):
        a=random.randint(1,10)
        B[i].append(a)
print('matriz B : ')
for i in range(m):
    print(B[i])
A=[]
for i in range(m):
    A.append([])
    for j in range(n):
        a=random.randint(1,10)
        A[i].append(a)
print('matriz A : ')
for i in range(m):
    print(A[i])
#creando lo matriz nula
C=[]
for i in range(m):
    C.append([])
    for j in range(n):
        C[i].append(0)
print('matriz C inical: ')
for i in range(m):
    print(C[i])
for i in range(m):
    for j in range(n):
        C[i][j]=A[i][j]+B[i][j]
print('A+b es : ')
for i in range(m):
    print(C[i])