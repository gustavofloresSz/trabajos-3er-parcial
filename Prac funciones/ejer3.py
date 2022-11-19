def dibujo(fila,colum,simb):
    for i in range(1,colum+1):
        for j in range(1,fila+1):
            print(c,end='')
        print('')


a=int(input('ingrese num columas'))
b=int(input('ingrese num filas'))
c=input('ingrese caracter a utilizar')
resp=dibujo(a,b,c)
