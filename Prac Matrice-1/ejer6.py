print('calculo=1, fisica=2, progra=3, estadistica=4, algebra=5')
#para seleccionar despues de cual queremos saber la nota
m=int(input('ingrese el numero de filas : '))
A=[]
for i in range(m):
    A.append([])
    print('elementos fila ',i)
    for j in range(5):
        num=float(input('ingrese nota de cada estudiante {}: '.format(j)))
        A[i].append(num)
print('la matriz es: ')
for i in range(m):
    print(A[i])
for j in range(5):
    ac=0
    for i in range(m):
        ac=ac+A[i][j]/m
    print('el promedio de cada materia'+str(j)+ ' es '+str(ac))
acAprob=0
x=int(input('ingrese la materia de la cual desea saber los aprobados :'))
for j in range(x):
    acAprob=0
    for i in range(m):
        if A[i][j]>=5.1:
            acAprob=acAprob+1
print('el num de aprobados de la materia es : ',acAprob)
vec=[]
for i in range(5):
    for j in range(m):
        vec.append(A[j][i])
    print('la mayor nota de la materia ',i+1,'es' ,'=' ,max(vec))
    print('la menor nota de la materia ', i+1,'es','=', min(vec))
    vec=[]
#convertimos a vector y buscamos el max y min ahi.