import random
A=[]
for i in range(7):
    A.append([])
    for j in range(3):
        num=random.randint(0,10)
        A[i].append(num)
print('la matriz es: ')
for i in range(7):
    print(A[i])
v=[]
for k in range(7):
    nomb=input('ingrese el nombre :'.format(k))
    v.append(nomb)
print('los estudiantes son:', v)

for j in range(7):
    ac=0
    for i in range(3):
        ac=ac+A[j][i]
        prom=ac/3
    print('promedio del est.',v[j], 'es: '+str(prom))
print('El promedio de los examenes es :')

for j in range(3):
    acexa=0
    for i in range(7):
        acexa=acexa+A[i][j]
        prom2=acexa/7
    print('promedio examen '+str(j+1)+ ' es '+str(prom2))