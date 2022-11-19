#avance 04/11
n=int(input('ingrese tamaño vector '))
t=[]
for i in range(n):
    x=float(input('ingrese las temperaturas {}: '.format(i)))
    t.append(x)
print('vector de temperatura es: ',t)
suma=0
for i in range(n):
    suma=suma+t[i]
prom=suma/n
print('el promedio es :',prom)
alta=t[0]
for i in range(n):
    if t[i]>alta:
        alta=t[i]
print('la temperatura mas alta es : ',alta)
menor=t[0]
for i in range(n):
    if t[i]<menor:
        menor=t[i]
print('la temperatura mas baja es : ',menor)
