v1=[]
n1=int(input('ingrese tamaño del vec1 : '))
for i in range(n1):
    a=int(input('ingrese valores v1 :'.format(i)))
    v1.append(a)
print(v1)
v2=[]
n2=int(input('ingrese tamaño del vec2 : '))
for i in range(n2):
    b=int(input('ingrese valores v2 :'.format(i)))
    v2.append(b)
print(v2)
v3=[]
for i in range(n1):
    union=str(v2[i]),str(v1[i]).format(i)
    v3.append(union)
print('la union de los vectores es : ',v3)