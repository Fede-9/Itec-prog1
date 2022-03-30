#Cargar una lista con números. Invertir los elementos sin usar otra lista

cant = int(input("cuantos numeros desea ingresar? "))
lista = []

for i in range(cant):
    n = int(input("ingrese un numero: "))
    lista.append(n)

print("numeros ingresados: ", lista)
print("numeros invertidos: ",lista[::-1])



# lista por comprension

numeros = [1,2,3,4,5,6]
reversa = [num for num in numeros[::-1]]
print(reversa)