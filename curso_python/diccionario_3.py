# Metodos utiles Aplicados a Diccionarios

informacion = {'color':'verde', 'cantidad':10, 'tipo':'C'}

print(informacion)

# Keys() : con esta funcion pueda acceder ala claves del diccionario.
print('-----------------KEYS-------------')

lista_de_claves = list(informacion.keys())

print(lista_de_claves)
print(type(lista_de_claves))

# Values() : me muestra los valores de las claves.
print('-----------------VALUES-------------')

lista_de_valores = list(informacion.values())

print(lista_de_valores)
print(type(lista_de_valores))

# Items() : dentro de la lista una tupla con clave y valor me muestra.
print('-----------------ITEMS-------------')

lista_items = list(informacion.items())
print(lista_items)