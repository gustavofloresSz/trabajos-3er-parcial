vector=[1,4,3,7,9]
print(vector[3])
i=4
print(vector[i])
vector[2]=10
print(vector)
t=len(vector)
print('tamaño de vector es :',t)

vector.append(1)
print(vector)
veces=vector.count(1)        #count ve si se repite
print('el 1 se repite : ',veces)

#insert es insertamos el elemen en la posicion que eligamos,no lo rempla
vector.insert(2,25)
print(vector)

#remove quita el num que introduscamos
vector.remove(1)
print(vector)