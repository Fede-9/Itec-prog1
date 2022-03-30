#En los siguientes ejercicios (6 a 11) trabajamos con el texto:
#  “Quiero comer manzanas, solamente manzanas.”, considerar que una palabra es toda secuencia de 
# caracteres diferentes de los separadores (los caracteres separadores son el espacio, la coma y el punto).

# 9. Contar la cantidad de palabras.

cadena = 'Quiero comer manzanas, solamnete manzanas.'
palabras = cadena.split()
print('cantidad de palabras: ', len(palabras))