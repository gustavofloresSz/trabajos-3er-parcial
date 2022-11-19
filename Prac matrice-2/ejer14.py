import random
A=[]
for i in range(7):
    A.append([])
    for j in range(24):
        num=random.randint(5,33)
        A[i].append(num)
print('matriz A: ')
for i in range(7):
    print(A[i])
mayor=A[0][0]
menor=A[0][0]
for i in A:
    for j in i:
        if j>mayor:
            mayor=j
        if j<menor:
            menor=j
print('la maxima temperatura de la semana fue : ',mayor)
print('la minima temperatura de la semana fue : ',menor)
ac=0
for i in range(7):
    ac=0
    for j in range(24):
        ac=ac+A[i][j]*7
        prom=ac/168
print('la temperatura media de la semana es : ',prom)
for j in range(7):
    ac=0
    for i in range(24):
        ac=ac+A[j][i]
        promdia=ac/24
    print('la temperatura media del dia' ,j+1,'es : ',promdia)
vecmay=[]
mayor=A[0][0]
for i in range(7):
    for j in range(24):
        if A[i][j]>mayor:
            mayor=A[i][j]
    vecmay.append(mayor)
    mayor=0
maximo=max(vecmay)
print('el dia que se registro mayor temperatura fue :' ,maximo,'grados')