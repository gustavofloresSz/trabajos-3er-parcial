from collections import Counter
q=0
a=input('ingrese los caracteres ')
v=[]
x=0
for y in a:
    v.append(y)
for c in (v):
    if c in 'a e i o u':
        x=x+1
print('en el vector hay :',x, 'vocales')
t=Counter(a)
repite=t.most_common(1)[0]
print('la letra que mas se repite es :',repite)




#OTRA MANERA
a=input('ingrese los caracteres')
v=[]
x=0
maximo=[]
for y in a:
    v.append(y)
    maximo.append(a.count(y))
for c in (v):
    if c in 'a e i o u':
        x=x+1
print('en el vector hay :',x, 'vocales')
print(max(maximo))




