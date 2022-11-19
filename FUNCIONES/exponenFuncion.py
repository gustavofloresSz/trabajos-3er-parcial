def termino(exponente):
    r=4**exponente
    return r
#programa principal
n=int(input('ingrese valor de n : '))
ac=0
for i in range(1,n+1):
    ac=ac+termino(i)
print('el resultado es : ',ac)