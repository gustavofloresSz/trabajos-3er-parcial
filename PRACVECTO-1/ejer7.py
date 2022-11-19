a=int(input('ingrese la cantidad de elementos del vector '))
v=[]
for i in range(a):
    b=int(input('ingrese los valores del vector : ' .format(i)))
    v.append(b)
print(v)
sigue=True
c=0
x=a-1
while c<=x and sigue==True:
    if v[c]==v[x]:
        c=c+1
        x=x-1
    else:
        sigue=False
if sigue==False:
    print('distinto')
else:
    print('igual')
