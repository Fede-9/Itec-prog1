# 8. Ingresar nombres , luego buscar un nombre y de encontrarlo decir en qué posición está.

def cargarNombres(cant):
    for i in range(cant):
        n = input(f'Ingrese el nombre {i+1}: ')
        nombres.append(n)

def buscarNombre(nombre,lista):
    pos = 999
    result = ''
    for i in range(len(lista)):
        if lista[i].lower() == nombre.lower():
            pos = i
    if pos == 999:
        result = 'El nombre no se encontro'
    else:
        result = 'El nombre se encontro en la posicion ' + str(pos)
    return result

nombres = [] 
cargarNombres(3)
buscar = input('Ingrese el nombre a buscar: ')
print(buscarNombre(buscar, nombres))
print(nombres)