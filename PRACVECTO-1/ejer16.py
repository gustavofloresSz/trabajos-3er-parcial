a=int(input('ingrese tamaño del vector '))
v=[]
for c in range(a):
    b=int(input('ingrese los elemnetos del vector'.format(c)))
    v.append(b)
print(v)
menor=v[0]
for x in v:
    if x<=menor:
        menor=x
        repi=v.count(x)
print('el menor numero del vector es: ',menor)
print('y se repite : ', repi ,'veces')
