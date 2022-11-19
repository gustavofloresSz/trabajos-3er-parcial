def serie(exponen):
    ac=0
    for i in range(1,exponen+1):
        ac=ac+(1/2**i)
    return ac
a=int(input('ingrese valor del exponente'))
resp=serie(a)
print('la suma de los numeros es : ',resp)


