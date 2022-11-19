def duplicar(u):
    for i in range(len(u)):
        u[i]=u[i]*2
print('inicio')
v=[3,2,6]
print('vector antes de la funcion ',v)
duplicar(v)
print('valor del vector : ',v)
print('fin')