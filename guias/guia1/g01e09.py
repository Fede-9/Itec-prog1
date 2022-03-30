#9-Realizar un algoritmo que permita ingresar un dato numérico y determinar si es un número positivo 
# de dos dígitos.

dato_numerico = int(input("ingrese un numero: "))
if ( dato_numerico >= 10) and (dato_numerico < 100):
    print(dato_numerico,"el numero es positivo de dos digitos")
elif dato_numerico < 10:
    print(dato_numerico, "es un numero positivo pero es menor que dos digitos") 
elif dato_numerico > 99:
    print(dato_numerico, "es un numero positivo pero tiene mas de dos digitos")





