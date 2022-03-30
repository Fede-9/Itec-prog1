# METODO SIMPLE
precios = [3,5,8,6,4]
doblePrecios = []

for precio in precios:
    doblePrecios.append(precio*2)

print(doblePrecios)


# COMPRENSION DE LISTA  / primero ponemos lo que queremos que se añada a la lista 

doblePrecios = [precio * 2 for precio in precios]
print(doblePrecios)

print('-------------------------------------------------')

# raiz cuadrada de los numeros pares

nums = [1,2,3,4,5,6]
numerosParesAlCuadrado = []

for num in nums:
    if (num**2)%2 == 0:
        numerosParesAlCuadrado.append(num**2)

print(numerosParesAlCuadrado)


# COMPRENSION DE LISTA

numerosParesAlCuadrado = [num**2 for num in nums if(num**2)%2 == 0]
print(numerosParesAlCuadrado)
