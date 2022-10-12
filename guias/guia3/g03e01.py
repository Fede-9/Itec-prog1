#(4 de la guía 2) Pedir el ingreso de 10 números. Contar los mayores de 23.
#Almacenar los que cumplen la condición.  Mostrar los resultados.
num = []
acum = 0
for x in range (10):
    n = int(input("ingrese un numero: " ))
    if n > 23:
        acum += 1
        num.append(n)

print(f'La cantidad de numeros mayores a 23 son: {acum}')
print(f'Los numeros son: {num}')


# lista por comprension

numeros = [1,25,56,23,85,2,3,96]
mayores = [n for n in numeros if n > 23]
print(mayores)