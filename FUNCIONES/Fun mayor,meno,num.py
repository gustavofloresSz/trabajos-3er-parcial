def mayor(n1,n2):
    if n1>n2:
        r=n1
    else:
        r=n2
    return r
a=int(input('ingrese el primer numero '))
b=int(input('ingrese segundo numero '))
resultado=mayor(a,b)
print('el mayor es : ',resultado)
