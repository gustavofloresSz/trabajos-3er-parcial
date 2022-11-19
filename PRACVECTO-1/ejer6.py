v=[]
for i in range(10):
    num=int(input('ingrese numeros : '.format(i)))
    v.append(num)
print('vector: ',v)
a=0
while a>=0:
    a=int(input('ingrese valores '))
    existe=False
    for y in v:
        if a==y:
            existe=True
    if existe==True:
        print('el numero existe en el vector')
    else:
        print('el numero no existe en el vector')