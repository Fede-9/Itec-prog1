# 14. Pedir dos nombres y edades respectivas y luego construir una sola cadena con 
# un texto que muestre el nombre del mayor y cuanto le lleva al menor.
#(Ejemplo:  entrada -> 'Juan' 30 'Pedro' 23 / salida -> 'Juan le lleva 7 años a Pedro')

nombre1 = input('Ingrese su nombre: ')
edad1 = int(input(f'Ingrese la edad de {nombre1} : '))
nombre2 = input('Ingrese otro nombre: ')
edad2 = int(input(f'Ingrese la edad de  {nombre2} : '))

if edad1 > edad2:
    diferencia = edad1 - edad2
    print(f'{nombre1} le lleva {diferencia} años a {nombre2}')
elif edad2 > edad1:
    diferencia = edad2 - edad1
    print(f'{nombre2} le lleva {diferencia} años a {nombre1}')
else:
    print(f'{nombre1} y {nombre2} tienen la misma edad')