#Generar 10 números aleatorios y calcular el máximo y el mínimo.

from random import randint

lista=[]

for i in range(11):
    lista.append(randint(1,100))

maximo = max(lista)
minimo = min(lista)
print(lista)
print(f'Maximo: {maximo}')
print(f'Minimo: {minimo}')

###################################################################
print('-----------------------------------------')
auxMaximo = 0
auxMinimo = 100

for x in range(len(lista)):
    if lista[x] > auxMaximo:
        auxMaximo = lista[x]
    if lista[x] < auxMinimo:
        auxMinimo = lista[x]

print('Maximo:', auxMaximo)
print('Minimo:', auxMinimo)

