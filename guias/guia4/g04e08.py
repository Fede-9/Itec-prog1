#En los siguientes ejercicios (6 a 11) trabajamos con el texto:
#  “Quiero comer manzanas, solamente manzanas.”, considerar que una palabra es toda secuencia de 
# caracteres diferentes de los separadores (los caracteres separadores son el espacio, la coma y el punto).

#8. Contar la cantidad de letras (no incluir los separadores).

cadena = "Quiero comer manzanas, solamente manzanas."
cadena1 = ''
for i in range(len(cadena)):
    if cadena[i] != ' ' and cadena[i] != ',' and cadena[i] != '.':
        cadena1 += cadena[i]

print(cadena1)
print('la cantidad de letras es: ', len(cadena1))