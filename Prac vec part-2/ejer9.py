import random
n=int(input('ingrese tamaño del vector 1 = '))
v1=[]
for i in range(n):
    xa=random.randint(0,100)
    v1.append(xa)
print('vector 1: ',v1)
n2=int(input('ingrese tamaño del vector 2 = '))
v2=[]
for i in range(n2):
    xb=random.randint(0,100)
    v2.append(xb)
print('vector 2: ',v2)
ac1=0
for i in range(n):
    ac1=ac1+v1[i]
print('suma total del vec1 : ',ac1)
ac2=0
for i in range(n2):
    ac2=ac2+v2[i]
print('suma total del vec1 : ',ac2)
v3=[]
total=ac1+ac2
v3.append(total)
print('la suma total de los 2 vectores es = ',v3)