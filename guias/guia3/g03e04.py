#Dada una lista con números, crear otra con los cuadrados de esos valores.


num = [2,5,3]
cuad = []

for i in range(len(num)):
    cuad.append(num[i] * num[i])

print(cuad)


#OTRA FORMA


numero = [2,3,4]
elevado = []

for x in range(len(numero)):
    elevado.append(numero[x]**2)

print(elevado)
