#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados 
# por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

preg = input('Que productos se encuentran en la cesta? ')

for i in preg.split(','):
    print(i)