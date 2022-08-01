#Cargar letras en una lista (while). Contar las vocales (for). Mostrar el total.

preg1 = input("Cuantas letras desea ingresar? ")
lista = []
total = 0
vocales = []
aux = 0

while aux < int(preg1):
    letra = input("ingrese una letra: ")
    lista.append(letra)
    aux += 1
    
for x in lista:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        total += 1
        vocales.append(x)


print("cantidad de vocales: ",total)
print('las vocales son: ',vocales)

# lista por comprension

letras = ['a','f','b','o','i']
vocales = [vocal for vocal in letras if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u']
print(vocales)