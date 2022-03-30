# 13. Pedir el ingreso de un nombre completo (Juan Pérez) y mostrarlo invertido y con coma (Pérez, Juan).

def invertirNombre(nombre):
    aux = nombre.split()
    result = aux[1] + ', ' + aux[0]
    return result

nombre = input('Ingrese su nombre y apellido: ') 
nombreInvertido = invertirNombre(nombre)
print(nombreInvertido)