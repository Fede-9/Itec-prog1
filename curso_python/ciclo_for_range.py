# Funcion range()

#Va a retornar una secuencia de numeros enteros

# print(range(5)) # ----> 0, 1, 2, 3, 4

lista_numeros = list(range(10, 20))

print(lista_numeros)


for numero in range(10):
    print(numero)

print('-----------------------')
print('EJEMPLO CON FOR')

colores = ['amarillo','rojo','azul','verde']

for color in colores:
    print(color)

print('-----------------------')
print('-----------------------')

# colores[0] # ----> 'amarillo'
# colores[1] # ----> 'rojo'
# colores[2] # ----> 'azul'
# colores[3] # ----> 'verde'

for indice in range(4):
    print(colores[indice])