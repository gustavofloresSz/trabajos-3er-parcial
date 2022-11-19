def posi(num1):
    if num1>0:
        r='P'
        return r
    else:
        r='N'
        return r
x=int(input('ingrese valor de num : '))
resp=posi(x)
print(resp)