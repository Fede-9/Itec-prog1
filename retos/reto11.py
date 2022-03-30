#Generar números aleatorios pares entre 100 y 130, salvo 110 y 120.

from  random import randint

lista = []

for i in range(4):
    lista.append(randint(100,130))

listaDefinitiva = []

for x in range(len(lista)):
    if lista[x] % 2 == 0 and lista[x] != 110 and lista[x] != 120:
        listaDefinitiva.append(lista[x])

print(listaDefinitiva)

