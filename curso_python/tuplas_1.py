# Tipo de Estructura TUPLA : parecidas a la listas pero se usan ()

loteria = (10, 20, 30, 40, 50)

print(loteria[0])

# Listas son MUTABLES

# las tuplas son INMUTABLES
# Las tuplas Gestionan la informacion en memoria de manera mucho mas eficiente que las listas

loteria_lista = list(loteria)
print(loteria_lista)

loteria_lista.append(900)
print(loteria_lista)

loteria = tuple(loteria_lista)
print(loteria)
print(type(loteria))

print('--------------')
print(loteria.index(900))