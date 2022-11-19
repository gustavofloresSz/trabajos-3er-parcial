#Avance 04/11
import random
n=int(input('ingrese tamaño del vector '))
v=[]
for i in range(n):
    x=random.randint(2,25)
    v.append(x)
print('vector : ',v)
elemento=int(input('ingrese elemento a buscar :'))
veces=v.count(elemento)
if veces>0:
    print('el elemento existe en el vector')
    for k in range(veces):
        v.remove(elemento)
    tam = len(v)
    print('el nuevo tamaño es : ', tam)
    print('el nuevo vector es : ',v)
else:
    print('el elemento no existe')


