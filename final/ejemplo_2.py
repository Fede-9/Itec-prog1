# 1. Escribir un programa que le pida al usuario su nombre y luego lo imprima por la consola  concatenando el texto “Nombre:”.

nombre = input('Ingrese nombre: ')
print(f'Nombre: {nombre}')

# 2. Crear una lista vacía, imprimir el campo id, el tipo y el valor de la lista. Luego agregar un número
# a la lista y volver a imprimir id,tipo y valor. ¿Cuáles son las diferencias?

# lista = []
# print(id(lista))
# print(type(lista))
# print(lista)
# lista.append(9)
# print(id(lista))
# print(type(lista))
# print(lista)

# 3. Crear una lista vacia y agregarle 5 nombres. Ordenar la lista.

nombres = []
nombres.extend(['Fede','Lucas','Adrian','Juan','Facu'])
nombres.sort()
print(nombres)




# 4. Escribir la función “es_par()” la cual recibe un número entero y devuelve True si el número es par o False si es impar.

def esPar(num):
    if num % 2 == 0: 
        return True
    else:
        return False

print(esPar(4))
print(esPar(3))



# 5. Escribir una función que reciba un string y reemplace los espacios por un caracter que reciba por  argumento. La función debera devolver el nuevo string.

def reemplazo(cadena):
    nuevaCadena = cadena + cadena.join('-')
    return nuevaCadena

print(reemplazo('Hola todo bien'))