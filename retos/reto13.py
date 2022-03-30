# MEDIR EL LARGO DE UN STRING

palabra = input (" Ingrese palabra: ")
cont = 0
while (cont < len (palabra) ):
    print (palabra[cont])
    cont += 1

print(f'Cantidad de letras de su palabra: {cont}')