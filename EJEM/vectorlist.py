n=int(input('ingrese la cantidad de elementos del vector'))
v=[]
for i in range(n):
    numero=int(input('ingrese elemnto de la posicion {}: '.format(i)))
    v.append(numero)
    print('vector: ',v)
