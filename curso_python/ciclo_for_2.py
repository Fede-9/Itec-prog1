# Instruccion BREAK


colores = ['amarillo','rojo','verde','azul']


for color in colores:
    print(color)
    if color == 'rojo': 
        break


# sentencia in

palabra = 'rojo'

if 'r' in palabra:
    print('La letra R se encuentra dentro de la palabra')

else:
    print('La letra R no se encuentra dentro de la palabra')


print('--------------')
print('SEGUNDO EJEMPLO')

loteria = [10, 20, 13, 17, 8]

numero = 20

if numero in loteria:
    print(f'El numero {numero} esta dentro de la lista LOTERIA')

else:
    print(f'El numero {numero} NO esta dentro de la lista LOTERIA')