#Pasar una palabra a mayúsculas cambiando los caracteres uno por uno usando
#  la tabla ASCII de referencia (googlear la tabla y las funciones de conversión en Python).

palabra = 'tablero'
nueva_palabra = ''

for letra in palabra:
    #print(letra)
    mayuscula = ord(letra)-32
    chr(mayuscula)
    nueva_palabra += chr(mayuscula)
print(nueva_palabra)