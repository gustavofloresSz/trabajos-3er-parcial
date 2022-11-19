m=int(input('ingrese el numero de filas : '))
n=int(input('ingrese el numero de columnas : '))
A=[]
for i in range(m):
    A.append([])
    print('elementos fila ',i)
    for j in range(n):
        num=int(input('ingrese elemento de columna {}: '.format(j)))
        A[i].append(num)
print('matriz A: ')

for i in range(m):
    print(A[i])