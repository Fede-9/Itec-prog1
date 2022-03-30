# 6. Definir una lista de 10 posiciones con letras. Contar las vocales y mostrar el total.

def contar_vocales(lista):
    total = 0
    for i in range(len(lista)):
        if lista[i] in ('a','e','i','o','u'):
            total += 1
    return total
    

# chars = ['a','b','c','d','e','f','g','h','j','k']
letras = []
for i in range(11):
    x = input('Ingrese una la letra: ')
    letras.append(x)

result = contar_vocales(letras)

print('La lista contiene',result,'vocales')