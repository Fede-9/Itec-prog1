#Pedir el ingreso de 10 números. Contar los mayores de 23. Mostrar el resultado.

cant = 0
for x in range (10):
    numero = int(input("ingrese un numero: "))
    if numero > 23:
        cant = cant + 1
print(f'Cantida de numeros mayores a 23: {cant}')