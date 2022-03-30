# A). Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
# Finalizar al ingresar el número 0, el cual no debe guardarse.
# Mostrar la lista en pantalla con un mensaje: 'La lista de números es: <lista> 

numero = int(input('ingrese un numero: '))
usuario = []
while numero != 0:
    usuario.append(numero)
    numero = int(input('ingrese un numero: '))

print(f'sus numeros son: {usuario}')


# B)
# A continuación, solicitar al usuario que ingrese un número y,
# si el número está en la lista, eliminar su primera ocurrencia.
# Mostrar un mensaje si no es posible eliminar. 

numero_usuario = int(input('ingrese un numero: '))

if numero_usuario in usuario:
    usuario.remove(numero_usuario)
    print(f'se ha eliminado el numero {numero_usuario} de la lista')
else:
    print(f'su numero {numero_usuario} no se encuentra en la lista')


# C)
# Definir una función que recorra la lista e imprima la sumatoria de todos los elementos. 

def sumatoria(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma 

print(f'La sumatoria de todos los numers de su lista es: {sumatoria(usuario)}')


# D)
# Utilizar una función para resolver la consigna.
# Solicitar al usuario otro número y crear una lista con los elementos de la lista original
# que sean menores que el número dado.
# Imprimir esta nueva lista, iterando por ella. 

def numero_menores(lista,limite):
    nueva_lista = []
    for numero in lista:
        if numero < limite:
            nueva_lista.append(numero)
    return nueva_lista

limite = int(input('filtrar numeros menores a: '))
lista_filtrada = numero_menores(usuario,limite)
print(f'la nueva lista es : {lista_filtrada} ')

