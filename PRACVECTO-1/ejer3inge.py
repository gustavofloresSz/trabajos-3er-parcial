n=int(input('ingrese el tamaño del vector :'))
v=[]
for i in range(n):
    letra=input('ingree la palabra ')
    v.append(letra)
print('vector : ',v)
c=0
for i in range(n):
    if v[i]=='a' or v[i]=='e' or v[i]=='i' or v[i]=='o' or v[i]=='u':
        c=c+1
print('el num de vocales es : ',c)
repetido=[]
for i in range(n):
    veces=v.count(v[i])
    repetido.append(veces)
print('vec de repeticiones : ',repetido)
mayor=repetido[0]
for i in range(n):
    if repetido[i]>mayor:
        mayor=repetido[i]
        posimayor=i
print('la letra que mas se repite es : ',v[posimayor])
print('el num de veces que se repite es : ',mayor)