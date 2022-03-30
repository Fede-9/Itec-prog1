#Dada una lista cargada con 7 números enteros, obtener el promedio. 
# Mostrar por pantalla dicho promedio y los números de la lista que sean mayores que él.

num = []
suma = 0

for x in range(1,8):
    numero = int(input("ingrese un numero: "))
    num.append(numero)
    

for i in range(len(num)):
    suma += num[i]
    
promedio = suma/len(num)   # es lo mismo que poner  promedio = suma/7
mayor = []

for y in range(len(num)):
    if (num[y] > promedio):
        mayor.append(num[y])
        
print("el promedio es: ", promedio)
print("el o los numeros mayores al promedio son: ", mayor)


# # lista por comprension

numeros = [2,5,8,9,4,6,7]
cuenta = sum([num for num in numeros])
promedio = cuenta // len(numeros)
mayores = [mayor for mayor in numeros if mayor>promedio ]
print(promedio)
print(mayores)


#OTRA FORMA DE HACERLO

n = [2,5,3,6,4,8,7]
acum = 0
cont = 0

for z in range(len(n)):
    acum += n[z]
    cont += 1

mayor = []

for m in range(len(n)):
    if n[m] > (acum/cont):
        mayor.append(n[m])

print(f'Promedio: {acum/cont}')
print(f'Mayores al promedio: {mayor}')


