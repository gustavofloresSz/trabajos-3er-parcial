import random
def leerMatriz(X,m,n):
    for i in range(m):
        X.append([])
        for j in range(n):
            num=random.randint(0,10)
            X[i].append(num)
def mostrarMatriz(X,m):
    for i in range(m):
        print(X[i])
def matrizNula(K,m,n):
    for i in range(m):
        K.append([])
        for j in range(n):
            K[i].append(0)
def restarMatrices(A,B,C,m,n):
    for i in range(m):
        for j in range(n):
            C[i][j]=A[i][j]-B[i][j]
#programa principal
fi=int(input('ingrese el numero de filas : '))
co=int(input('ingrese el numero de columnas : '))
A=[]
B=[]
C=[]
leerMatriz(A,fi,co)
print('matriz A:')
mostrarMatriz(A,fi)
leerMatriz(B,fi,co)
print('matriz B:')
mostrarMatriz(B,fi)
matrizNula(C,fi,co)
restarMatrices(A,B,C,fi,co)
print('matriz A-B es: ')
mostrarMatriz(C,fi)