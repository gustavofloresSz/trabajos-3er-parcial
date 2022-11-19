m=int(input('ingrese el numero de filas : '))
n=int(input('ingrese el numero de columnas : '))
A=[]
for i in range(m):
    A.append([])
    print('elementos fila ',i)
    for j in range(n):
        num=int(input('ingrese elemento de columna {}: '.format(j)))
        A[i].append(num)
print('la matriz es: ')
for i in range(m):
    print(A[i])
transp=[]
for i in range(n):
    transp.append([])
    for j in range(m):
        transp[i].append(A[j][i])
print('la trasnpuesta de la matriz A es :')
for i in range(n):
    print(transp[i])