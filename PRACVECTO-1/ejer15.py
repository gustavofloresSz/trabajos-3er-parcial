a=int(input('ingrese los estudiantes '))
v=[]
for i in range(a):
    b=float(input('ingrese las notas' .format(i)))
    v.append(b)
print('las notas de los estudiantes son = ',v)
for x in v:
    if x>=5.1:
        print('el est. aprobo con : ',x)
    elif x<5.1:
        print('el est. reprobo con : ',x)