# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después 
# muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input('Frase: ')
vocal=input('Vocal: ')
nuevaFrase=''
for i in range(len(frase)):
    if frase[i] != vocal:
        nuevaFrase+=frase[i]
    elif frase[i] == vocal:
        nuevaFrase+=vocal.upper() 

print(nuevaFrase)
