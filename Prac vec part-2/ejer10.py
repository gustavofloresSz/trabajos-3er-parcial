v=[]
for i in range(1,8):
    a=int(input('ingrese venta de cada dia {}: '.format(i)))
    v.append(a)
print(v)
mayor=v[0]
for i in range(1,len(v)):
    if v[i]>mayor:
        mayor=v[i]
print('la mayor venta fue : ',mayor)
dia=v.index(mayor)+1
print('la mayor venta fue el dia : ',dia)
#index nos da posicion, de elemen que no se repitan