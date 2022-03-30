def inputInt(mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = int(numero)
            validado = True
        except:
            print("Error. Debe ingresar un número entero")
    return numero

def inputFloat(mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = float(numero)
            validado = True
        except:
            print("Error. Debe ingresar un número real")
    return numero

def inputRangeInt(mensaje, vi, vf):
    valido = False
    while not valido:
        numero = input(mensaje)
        try:
            numero = int(numero)
            if vi <= numero <= vf:
                valido = True
            else:
                print('El rango de valores es de', vi,'a', vf)
        except:
            print("Error. Debe ingresar un número entero")
    return numero

# sirve para sumar N cantidad de numeros.
def suma(*args):  
    cont = 0
    for e in args:
        cont += e
    return cont

#Concatenar un número indeterminado de strings con un caracter determinado (por defecto un espacio)
def concatenar(*args, caracter=''):
    return caracter.join(args)


if __name__=='__main__': #para probar las funciones
    print(concatenar('como va?', 'buenas noches', 'hasta luego', 'hasta mañana'))
    print(concatenar('como va?', 'buenas noches', 'hasta luego', 'hasta mañana', caracter=' - '))
    print(concatenar('como va?', 'buenas noches', 'hasta luego', 'hasta mañana', caracter=' + '))
    print(suma(5,5,5))
