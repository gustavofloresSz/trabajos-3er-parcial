def factorial(x):
    ac=1
    for i in range(1,x+1):
        ac=ac*i
    return ac
#inicia programa principal
n=int(input('ingrese el valor del numerador'))
k=int(input('ingrese el valor del denominador'))
combinatorio=factorial(n)/(factorial(k)*factorial(n-k))
print('el valor de la combiancion es : ',combinatorio)
