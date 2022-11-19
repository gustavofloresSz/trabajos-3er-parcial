m=int(input('ingrese el numero de filas : '))
n=int(input('ingrese el numero de columnas : '))
A=[]
for i in  range(m):
    A.append([])
    for j in range(n):
        A[i].append(0)
print(A)
#el segundo for se pone el numero que queremos
for i in range(m):
    print(A[i])    #se ve mas bonito