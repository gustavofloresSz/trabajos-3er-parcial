#ejer 2 practica funciones - fala desde restar
import random
def leervector(a,tam):
    for i in range(tam):
        x=random.randint(0,10)
        a.append(x)
def sumavectores(a,b,c,tam):
    for i in range(tam):
        c.append(0)
    for i in range(tam):
        c[i]=a[i]+b[i]

#desde aqui hacer
def restavectores (a,b,d,tam):
    #poner aqui la operacion
def productovectorial(a,b,tam):
    # poner aqui la operacion
    return productovectorial
def intercalarvectores(a,b,f,tam):
    #poner aqui la operacion


#programa principal
n=int(input('ingrese tamaño de los vectores '))
v=[]
u=[]
z=[]
leervector(v,n)
print('vector v: ',v)
leervector(u,n)
print('vector u: ',u)
sumavectores(v,u,z,n)
print('la suma de los vectores es: ',z)

w=[]