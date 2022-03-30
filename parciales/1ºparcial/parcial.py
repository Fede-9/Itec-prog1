# Dada la siguiente lista de diccionarios con datos de remeras, sus talles, colores y cantidades:

remeras = [
   {'talle': 'S', 'colores': {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1}},
   {'talle': 'M', 'colores': {'rojo': 7, 'verde': 1, 'azul': 3, 'blanco': 7}},
   {'talle': 'L', 'colores': {'rojo': 2, 'verde': 0, 'azul': 4, 'blanco': 4}},
   {'talle': 'XL', 'colores': {'rojo': 3, 'verde': 5, 'azul': 7, 'blanco': 2}}
 ]

# Obtener:
# 1-Las faltantes, por talle y color.
# 2-El o los colores de remeras de menor cantidad.
# 3-Las remeras con mayor stock, por talle y color.



cantidadRojo = []
cantidadVerde = []
cantidadAzul = []
cantidadBlanco = []
nombreMenor = ''
cantidadTotal = []


for i in range(len(remeras)):
    remera = remeras[i]   # {'talle': 'S', 'colores': {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1}}
    talle = remera['talle']
    colores = remera['colores'] # {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1}
    cantidadRojo.append(colores['rojo'])
    cantidadVerde.append(colores['verde'])
    cantidadAzul.append(colores['azul'])
    cantidadBlanco.append(colores['blanco'])
    cantidadTotal.append(colores['rojo'] + colores['verde'] + colores['azul'] + colores['blanco'])
    
    for color in colores: # {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1} voy recorriendo esto
        if colores[color] == 0:
            colorFaltante = color
            print(f'Faltantes: {talle} {colorFaltante}')

# ACTIVIDAD Nº2
cantidadRojo=sum(cantidadRojo) 
cantidadVerde=sum(cantidadVerde) 
cantidadAzul=sum(cantidadAzul) 
cantidadBlanco=sum(cantidadBlanco) 
cantidadTotal=sum(cantidadTotal)

lista = [cantidadRojo, cantidadVerde, cantidadAzul, cantidadBlanco]
nombresColores = ['rojo','verde','azul','blanco']

for e in range(len(lista)):
    if lista[e] < cantidadTotal:
        cantidadTotal=lista[e]
        nombreMenor=nombresColores[e]

print(f'Color de menor cantidad: {nombreMenor}')

# ACTIVIDAD Nº3
