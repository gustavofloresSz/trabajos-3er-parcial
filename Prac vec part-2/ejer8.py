import random
n=int(input('ingrese tamaño del vector '))
v=[]
for i in range(n):
    x=random.randint(0,1000)
    v.append(x)
print('vector : ',v)
for i in range(n):
    for j in range(i+1,n):
        if v[i]>v[j]:
            aux=v[i]
            v[i]=v[j]
            v[j]=aux
print('el vector ordenado es : ',v)
print('el num menor es :',v[0])
print('el num mayor es :',v[n-1])