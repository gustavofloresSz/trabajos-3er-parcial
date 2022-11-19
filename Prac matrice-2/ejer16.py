import numpy as np
A=[]
for i in range(3):
    A.append([])
    print('elementos fila ',i)
    for j in range(3):
        num=int(input('ingrese elemento de columna {}: '.format(j)))
        A[i].append(num)
print('la matriz es: ')
for i in range(3):
    print(A[i])
determinante=np.linalg.det(A)
print('el determinante de la matriz es : ' ,int(determinante))