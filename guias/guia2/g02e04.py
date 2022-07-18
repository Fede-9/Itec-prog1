#Pedir el ingreso de 10 números. Contar los mayores de 23. Mostrar el resultado.

cont = 0
for x in range (10):
    numero = int(input(f"{x+1} - ingrese un numero: "))
    if numero > 23:
        cont = cont + 1
print(f'Cantida de numeros mayores a 23: {cont}')