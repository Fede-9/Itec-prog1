#Dada una serie de números reales positivos, determinar el valor máximo y mostrarlo al final. 
# Se deberá ir preguntando si hay más números para ingresar.

preg1 = input("desea ingresar una serie de numeros reales positivos? ")
numeros = []
mayor = 0

while preg1 == 'si':
    preg2 = int(input("ingrese un numero: "))
    numeros.append(preg2)
    preg1 = input("hay mas numeros para ingresar? ")

mayor = max(numeros)
print("los numeros ingresados son: ", numeros)
print("el maximo valor ingresado es: ", mayor)