v=[]
for i in range(1,16):
    a=int(input('ingrese los carntes {}: '.format(i)))
    v.append(a)
print('los 15 carnets : ',v)
b=int(input('ingrese el carnet a buscar : '))
posi=[]
esta=False
for i in range(1,len(v)):
    if v[i]==b:
        posi=v.index(b)+1
        esta=True
        break
if esta==True:
    print('la posicion del carnet', b, 'es : ', posi)
else:
    print('el carnet no se encuentra en el vector')
