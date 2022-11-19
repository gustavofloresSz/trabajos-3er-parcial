#avance 04/11
n=int(input('ingrese el tamaño del vector : '))
v=[]
for i in range(n):
    x=int(input('ingrese elemntos de la posicion {}:'.format(i)))
    v.append(x)
print('vector : ',v)
menor=v[0]
for i in range(n):
    if v[i]<menor:
        menor=v[i]
print('el elemento menor es: ',menor)
mayor=v[0]
for i in range(n):
    if v[i]>mayor:
        mayor=v[i]
print('el elemento mayor es: ',mayor)