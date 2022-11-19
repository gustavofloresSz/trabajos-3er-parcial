def recortar(numero,minimo,maximo):
    if numero<minimo:
        r=minimo
    elif numero>maximo:
        r=maximo
    else:
        r=numero
    return r
#program inicio
num=int(input('ingrese el numero a recortar : '))
maxi=int(input('ingrese el valor del maximo : '))
mini=int(input('ingrese el valor del minimo : '))
resp=recortar(num,mini,maxi)
print('el resultado es : ',resp)