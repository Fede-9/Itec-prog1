# Dado un archivo de texto en formato CSV (valores separados por coma), realizar
#  un programa que solicite un año entre 1980 y 1999 (ambos incluídos)
# y muestre los nombres de las personas nacidas en el verano (considerar que el verano de un año
#  incluye a los nacidos desde el 21 de diciembre del año anterior).
# De preferencia (no es obligatorio), hacer una función que reciba una fecha y que devuelva algún 
# valor que sirva para determinar si corresponde al verano del año pedido.

from funciones import *

arch = open('nacidos.csv', 'r')
nacidos = arch.readlines()
nacidos.pop(0) # quito la primer linea
arch.close()


def verano(fecha):  # aaaa-mm-dd
    retorno = 0
    
    a, m, d = [int(e) for e in fecha.split('-')]  # esto es una lista por comprencion / MIRAR COMO FUNCIONA EN LA CARPETA DE CLASES VIRTUALES

    if (m == 12 and d >= 21):
        retorno = a + 1   # retorna el año ingresado mas 1 año
    elif (m == 1) or (m == 2) or (m == 3 and d <= 20):
        retorno = a # retorna el mismo año ingresado
    else:
        retorno = -1    # retorna -1 me sirve como indicador de que no nacio en verano
    return retorno 


a = inputRangeInt('Ingrese un año entre 1980 y 1999: ', 1980, 1999)  # valido si es entero y si se encuentra en el rango.

for leer in nacidos:
    posiComa = leer.find(',')
    nombre = leer[:posiComa]
    fecha = leer[posiComa+1:posiComa+11]
    if a == verano(fecha):
        print(nombre)


