#En los siguientes ejercicios (6 a 11) trabajamos con el texto:
#  “Quiero comer manzanas, solamente manzanas.”, considerar que una palabra es toda secuencia de 
# caracteres diferentes de los separadores (los caracteres separadores son el espacio, la coma y el punto).

# 11. Averiguar qué cantidad de letras tiene la palabra más larga y cual es.

cadena = 'Quiero comer manzanas, solamente manzanas.'
palabra = cadena.split()
print('La palabra mas larga es: ', max(palabra))
print('La cantidad de letras que tiene es de', len(max(palabra)), 'letras')

#OTRA FORMA DE HACERLO

frase = input('Ingrese su frase: ')
fraseSplit = frase.split(' ')
pos = 0
lengthWord = 0
mayor = 0

for i in range(len(fraseSplit)):
    for char in fraseSplit[i]:
        if char.lower() >= 'a' and char.lower() <= 'z':
            lengthWord = lengthWord + 1
if lengthWord > mayor:
    mayor = lengthWord
    pos = i

print('La palabra mas larga es:',fraseSplit[pos])