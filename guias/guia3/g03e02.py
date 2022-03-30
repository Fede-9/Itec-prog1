#Cargar letras en una lista (while). Contar las vocales (for). Mostrar el total.

preg1 = input("Desea ingresar una letra?: ")
lista = []
vocal = 0
vocales = []

while preg1 == 'si':
    letra = input("ingrese una letra: ")
    lista.append(letra)
    preg1 = input("Desea ingresar otra letra?: ")
    
for x in lista:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        vocal += 1
        vocales.append(x)


print("cantidad de vocales: ",vocal)
print('las vocales son: ',vocales)

# lista por comprension

letras = ['a','f','b','o','i']
vocales = [vocal for vocal in letras if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u']
print(vocales)