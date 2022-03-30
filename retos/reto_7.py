#Generar primero una lista con los números entre 0 y 10, luego generar otra lista con los números del 11 al 20. 
#Unir ambas lista e imprimir el resultado.
n1 = []
n2 = []

for i in range(0,11):
    n1.append(i)

for e in range(11,21):
    n2.append(e)

lista = n1 + n2
print(lista)

